"""
=============================================================================
QUANTEDGE AI — AGENTE DE APRENDIZAJE CONTINUO (AGENTE 5)
=============================================================================
🔧 v1.5.1 — Lote 3.5 (fixes urgentes B20 + B23):
  • 🐛 B20.1 CORREGIDO: min_trades_to_disable subido de 5 a 30.
  • 🐛 B20.2 CORREGIDO: PF calculado sobre últimos 50 trades.
  • 🐛 B20.3 CORREGIDO: histéresis (PF bajo Y WR bajo).
  • 🐛 B20.4 CORREGIDO: re-habilitación automática.
  • 🐛 B23 CORREGIDO: clamp duro para atr_stop_mult y atr_profit_mult.
    Antes: el learner multiplicaba por 1.15/1.10 cada vez que corría,
    acumulando valores absurdos como 13.65.
    Ahora: SL ∈ [1.0, 6.0] y TP ∈ [2.0, 9.0].
  • v1.4.0 heredado: B19 (límites ATR por clase), B6 (filtro tests).
=============================================================================
"""

import os
import json
import time
import logging
from typing import Dict, Any, List, Optional, Tuple
from collections import defaultdict
from datetime import datetime, timezone, timedelta

from time_utils import now_mt5, TZ_MT5

logger = logging.getLogger("FeedbackLearner")
logger.propagate = False

LOGS_DIR = os.path.join(os.path.dirname(__file__), "logs")
AUDIT_LOG_FILE = os.path.join(LOGS_DIR, "trade_audit_history.jsonl")
CONFIG_OPTIMIZED_FILE = os.path.join(os.path.dirname(__file__), "config_optimized.json")

DEFAULT_MIN_CONFIDENCE = 90.0


# =============================================================================
# 🐛 B19: límites por clase de activo
# =============================================================================
ATR_LIMITS_BY_CLASS = {
    "XAU":    {"sl": (3.5, 6.0), "tp": (5.0, 9.0)},
    "XAG":    {"sl": (2.0, 4.0), "tp": (3.0, 6.0)},
    "OIL":    {"sl": (1.5, 3.0), "tp": (2.5, 5.0)},
    "US500":  {"sl": (1.5, 3.0), "tp": (2.5, 5.0)},
    "BTC":    {"sl": (1.8, 3.5), "tp": (2.5, 6.0)},
    "ETH":    {"sl": (1.8, 3.5), "tp": (2.5, 6.0)},
    "SOL":    {"sl": (1.8, 3.5), "tp": (2.5, 6.0)},
    "FOREX":  {"sl": (1.0, 2.0), "tp": (1.5, 3.0)},
    "DEFAULT": {"sl": (1.0, 3.5), "tp": (1.5, 6.0)},
}


def get_class_of(symbol: str) -> str:
    s = symbol.upper()
    if "XAU" in s or "GOLD" in s: return "XAU"
    if "XAG" in s or "SILVER" in s: return "XAG"
    if any(k in s for k in ["WTI", "XTI", "BRENT", "XBR", "OIL"]): return "OIL"
    if "US500" in s or "SP500" in s or "SPX" in s: return "US500"
    if "BTC" in s: return "BTC"
    if "ETH" in s: return "ETH"
    if "SOL" in s: return "SOL"
    if any(fx in s for fx in ["EUR", "GBP", "JPY", "AUD", "NZD"]): return "FOREX"
    return "DEFAULT"


def clamp_atr_by_class(symbol_class: str, sl: float, tp: float) -> tuple:
    limits = ATR_LIMITS_BY_CLASS.get(symbol_class, ATR_LIMITS_BY_CLASS["DEFAULT"])
    sl_min, sl_max = limits["sl"]
    tp_min, tp_max = limits["tp"]
    return max(sl_min, min(sl_max, sl)), max(tp_min, min(tp_max, tp))


# =============================================================================
# 🐛 B20: umbrales para deshabilitar símbolos (v1.5.0 — con histéresis)
# =============================================================================
DISABLE_THRESHOLDS = {
    # Crítico: se requiere PF MUY bajo Y WR MUY bajo Y trades suficientes
    "critical": {
        "pf_max": 0.5,
        "wr_max": 40.0,
        "min_trades": 30,
        "disable_hours": 24,
    },
    "severe": {
        "pf_max": 0.8,
        "wr_max": 45.0,
        "min_trades": 30,
        "disable_hours": 6,
    },
    "log_only": {
        "pf_max": 1.0,
        "wr_max": 50.0,
        "min_trades": 30,
        "disable_hours": 0,
    },
}

# 🐛 B20.2: ventana temporal para calcular PF/WR
PF_LOOKBACK_DAYS = 30
PF_LOOKBACK_TRADES = 50  # últimos N trades

# 🐛 B20.4: re-habilitación automática
REENABLE_MIN_TRADES = 10
REENABLE_MIN_PF = 1.0
REENABLE_MIN_WR = 45.0


class ContinuousLearningAgent:
    MIN_TRADES_TO_OPTIMIZE = 30
    MAX_CONFIDENCE_DELTA = 2.0
    MAX_ATR_MULT_DELTA = 0.3
    MIN_CONFIDENCE_FLOOR = 80.0
    MAX_CONFIDENCE_CEILING = 95.0

    def __init__(
        self,
        log_path: str = AUDIT_LOG_FILE,
        config_path: str = CONFIG_OPTIMIZED_FILE,
        evaluation_interval_sec: float = 300.0,
        lookback_days: int = 30,
        include_tests: bool = False,
    ):
        self.log_path = log_path
        self.config_path = config_path
        self.evaluation_interval_sec = evaluation_interval_sec
        self.lookback_days = lookback_days
        self.include_tests = include_tests
        self.last_evaluation_time: float = 0.0

        self._last_min_confidence: Optional[float] = None
        self._last_atr_stop_mult: Optional[float] = None
        self._last_atr_profit_mult: Optional[float] = None

        env_conf = os.getenv("MIN_CONFIDENCE_THRESHOLD")
        if env_conf is not None:
            try:
                env_conf_f = float(env_conf)
                if abs(env_conf_f - DEFAULT_MIN_CONFIDENCE) > 0.01:
                    logger.warning(
                        f"⚠️ B13: MIN_CONFIDENCE_THRESHOLD del .env ({env_conf_f}) "
                        f"difiere del default ({DEFAULT_MIN_CONFIDENCE})."
                    )
            except ValueError:
                pass

        self._load_last_state()

    def _load_last_state(self):
        if not os.path.exists(self.config_path):
            return
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                cfg = json.load(f)
            self._last_min_confidence = cfg.get("min_confidence_threshold")
            self._last_atr_stop_mult = cfg.get("atr_stop_multiplier")
            self._last_atr_profit_mult = cfg.get("atr_profit_multiplier")
            logger.info(
                f"📂 Estado previo del learner: "
                f"conf={self._last_min_confidence} | "
                f"SL={self._last_atr_stop_mult} | "
                f"TP={self._last_atr_profit_mult}"
            )
        except Exception as e:
            logger.debug(f"No se pudo cargar estado previo: {e}")

    def load_audit_records(self) -> List[dict]:
        records = []
        if not os.path.exists(self.log_path):
            return records

        cutoff_ms = int((time.time() - self.lookback_days * 86400) * 1000)
        skipped_tests = 0

        try:
            with open(self.log_path, "r", encoding="utf-8") as f:
                for line in f:
                    line_str = line.strip()
                    if not line_str:
                        continue
                    try:
                        rec = json.loads(line_str)
                        if rec.get("timestamp", 0) < cutoff_ms:
                            continue
                        if not self.include_tests and rec.get("is_test") is True:
                            skipped_tests += 1
                            continue
                        records.append(rec)
                    except json.JSONDecodeError:
                        continue
        except Exception as e:
            logger.error(f"Error al leer archivo de auditoría: {e}")

        if skipped_tests > 0:
            logger.info(f"🧪 B6: {skipped_tests} registros de test filtrados del aprendizaje.")

        return records

    def _filter_recent_closures(self, closures: List[dict]) -> List[dict]:
        """
        🐛 B20.2: devuelve solo los últimos N cierres (por timestamp).
        Esto evita que un día malo de hace 20 días hunda el PF.
        """
        if len(closures) <= PF_LOOKBACK_TRADES:
            return closures
        sorted_by_time = sorted(closures, key=lambda r: r.get("timestamp", 0), reverse=True)
        return sorted_by_time[:PF_LOOKBACK_TRADES]

    def analyze_by_symbol(self, closures: List[dict]) -> Dict[str, dict]:
        """
        🐛 B20.2: ahora analiza solo los últimos PF_LOOKBACK_TRADES por símbolo.
        """
        by_symbol_trades: Dict[str, List[dict]] = defaultdict(list)
        for r in closures:
            sym = str(r.get("symbol", "UNKNOWN")).upper()
            by_symbol_trades[sym].append(r)

        result = {}
        for sym, trades in by_symbol_trades.items():
            trades_sorted = sorted(trades, key=lambda r: r.get("timestamp", 0), reverse=True)
            trades_recent = trades_sorted[:PF_LOOKBACK_TRADES]

            trades_count = len(trades_recent)
            if trades_count == 0:
                continue

            wins = 0
            losses = 0
            gross_profit = 0.0
            gross_loss = 0.0
            pnl_sum = 0.0

            for t in trades_recent:
                pnl = float(t.get("pnl_usd", 0) or 0)
                pnl_sum += pnl
                if pnl > 0:
                    wins += 1
                    gross_profit += pnl
                else:
                    losses += 1
                    gross_loss += abs(pnl)

            wr = (wins / trades_count) * 100 if trades_count > 0 else 0.0
            pf = (gross_profit / gross_loss) if gross_loss > 0 else (999.0 if gross_profit > 0 else 0.0)

            result[sym] = {
                "trades": trades_count,
                "trades_total_hist": len(trades),
                "wins": wins,
                "losses": losses,
                "win_rate_pct": round(wr, 2),
                "pnl_usd": round(pnl_sum, 2),
                "profit_factor": round(pf, 3),
                "is_profitable": pf > 1.0,
            }
        return result

    def _compute_disabled_symbols(
        self,
        by_symbol: dict,
        current_disabled: Dict[str, dict]
    ) -> Tuple[List[str], Dict[str, dict]]:
        """
        🐛 B20.1 / B20.3 / B20.4:
          - min_trades = 30
          - Requiere PF bajo Y WR bajo simultáneamente
          - Re-habilita automáticamente si el símbolo se recupera
        """
        disabled = []
        details = {}
        now_ts = time.time()

        for sym, d in by_symbol.items():
            trades = d["trades"]
            pf = d["profit_factor"]
            wr = d["win_rate_pct"]

            # 🐛 B20.4: primero, ¿el símbolo estaba deshabilitado y ahora es rentable?
            if sym in current_disabled:
                prev = current_disabled[sym]
                if trades >= REENABLE_MIN_TRADES and pf >= REENABLE_MIN_PF and wr >= REENABLE_MIN_WR:
                    logger.info(
                        f"✅ B20.4: {sym} RE-HABILITADO automáticamente "
                        f"(PF={pf:.3f} ≥ {REENABLE_MIN_PF}, WR={wr:.1f}% ≥ {REENABLE_MIN_WR}%, "
                        f"{trades} trades recientes)"
                    )
                    continue
                else:
                    disabled_until = prev.get("disabled_until", 0)
                    if now_ts < disabled_until:
                        disabled.append(sym)
                        details[sym] = prev
                        logger.debug(
                            f"⏸️  B20: {sym} sigue deshabilitado hasta "
                            f"{datetime.fromtimestamp(disabled_until, tz=TZ_MT5).strftime('%H:%M')}"
                        )
                        continue
                    else:
                        logger.info(f"⏰ B20: {sym} — deshabilitación expirada, reevaluando")

            # Análisis normal de deshabilitación
            for level_name, cfg in DISABLE_THRESHOLDS.items():
                if trades < cfg["min_trades"]:
                    continue

                if pf < cfg["pf_max"] and wr < cfg["wr_max"]:
                    if cfg["disable_hours"] > 0:
                        disabled.append(sym)
                        details[sym] = {
                            "level": level_name,
                            "pf": pf,
                            "wr": wr,
                            "trades": trades,
                            "disabled_at": int(now_ts),
                            "disabled_until": int(now_ts + cfg["disable_hours"] * 3600),
                            "reason": f"PF={pf:.3f} < {cfg['pf_max']} Y WR={wr:.1f}% < {cfg['wr_max']}% ({trades} trades)",
                        }
                        logger.warning(
                            f"🚫 B20: {sym} DESHABILITADO por {cfg['disable_hours']}h "
                            f"(PF={pf:.3f}, WR={wr:.1f}%, {trades} trades)"
                        )
                    else:
                        details[sym] = {
                            "level": level_name,
                            "pf": pf,
                            "wr": wr,
                            "trades": trades,
                            "reason": f"PF={pf:.3f} bajo Y WR={wr:.1f}% bajo — solo log",
                        }
                        logger.info(f"📝 B20: {sym} PF={pf:.3f} WR={wr:.1f}% — solo log")
                    break

        return disabled, details

    def analyze_and_optimize(self) -> Dict[str, Any]:
        now = time.time()
        self.last_evaluation_time = now

        records = self.load_audit_records()
        if not records:
            return self.load_current_config()

        closures_all = [
            r for r in records
            if r.get("category") == "CLOSURE" and r.get("pnl_usd") is not None
        ]

        closures = self._filter_recent_closures(closures_all)
        total_trades = len(closures)

        if total_trades < self.MIN_TRADES_TO_OPTIMIZE:
            logger.info(
                f"📊 [FeedbackLearner] Solo {total_trades} cierres. "
                f"Se requieren ≥{self.MIN_TRADES_TO_OPTIMIZE} para optimizar."
            )
            return self.load_current_config()

        wins = [r for r in closures if (r.get("pnl_usd") or 0) > 0]
        losses = [r for r in closures if (r.get("pnl_usd") or 0) <= 0]

        win_rate = (len(wins) / total_trades) * 100.0 if total_trades > 0 else 0.0
        total_pnl = sum((r.get("pnl_usd") or 0) for r in closures)
        sum_wins = sum((r.get("pnl_usd") or 0) for r in wins)
        sum_losses = abs(sum((r.get("pnl_usd") or 0) for r in losses))
        profit_factor = (sum_wins / sum_losses) if sum_losses > 0 else (99.0 if sum_wins > 0 else 1.0)

        by_symbol = self.analyze_by_symbol(closures_all)
        unprofitable_symbols = [
            s for s, d in by_symbol.items()
            if d["trades"] >= 30 and d["profit_factor"] < 1.0
        ]
        if unprofitable_symbols:
            logger.warning(
                f"⚠️ B18: Símbolos no rentables: {', '.join(unprofitable_symbols)}"
            )

        # 🐛 B20: calcular símbolos a deshabilitar (con histéresis + re-habilitación)
        current_cfg = self.load_current_config()
        current_disabled = current_cfg.get("disabled_details", {})
        disabled_symbols, disabled_details = self._compute_disabled_symbols(by_symbol, current_disabled)

        min_confidence = current_cfg.get("min_confidence_threshold", DEFAULT_MIN_CONFIDENCE)
        atr_stop_mult = current_cfg.get("atr_stop_multiplier", 1.8)
        atr_profit_mult = current_cfg.get("atr_profit_multiplier", 3.0)

        if profit_factor < 1.0:
            min_confidence = max(min_confidence, 92.0)
            atr_profit_mult = atr_profit_mult * 1.15
            logger.warning(f"🔴 B18: PF={profit_factor:.2f} < 1.0. Endureciendo: conf≥92%, TP×1.15")
        elif profit_factor < 1.3:
            min_confidence = max(min_confidence, 90.5)
            logger.info(f"🟡 B18: PF={profit_factor:.2f} bajo. Subiendo conf a 90.5%")

        if win_rate < 50.0:
            min_confidence = max(min_confidence, 90.0)
            atr_stop_mult = max(atr_stop_mult, 2.2)
            logger.info(f"📉 Win Rate bajo ({win_rate:.1f}%). Endureciendo.")
        elif win_rate < 55.0:
            min_confidence = max(min_confidence, 88.5)
            atr_stop_mult = max(atr_stop_mult, 2.0)
        elif win_rate >= 70.0:
            min_confidence = 85.0
            logger.info(f"🔥 Excelente Win Rate ({win_rate:.1f}%). Relajando.")

        if profit_factor > 2.0:
            atr_profit_mult = atr_profit_mult * 1.1
            logger.info(f"🚀 PF {profit_factor:.2f} > 2.0. Extendiendo TP.")

        # Guardrails de delta
        if self._last_min_confidence is not None:
            if abs(min_confidence - self._last_min_confidence) > self.MAX_CONFIDENCE_DELTA:
                if min_confidence > self._last_min_confidence:
                    min_confidence = self._last_min_confidence + self.MAX_CONFIDENCE_DELTA
                else:
                    min_confidence = self._last_min_confidence - self.MAX_CONFIDENCE_DELTA
                logger.info(f"🔒 Delta confianza limitado a ±{self.MAX_CONFIDENCE_DELTA} → {min_confidence:.1f}%")

        if self._last_atr_stop_mult is not None:
            if abs(atr_stop_mult - self._last_atr_stop_mult) > self.MAX_ATR_MULT_DELTA:
                if atr_stop_mult > self._last_atr_stop_mult:
                    atr_stop_mult = self._last_atr_stop_mult + self.MAX_ATR_MULT_DELTA
                else:
                    atr_stop_mult = self._last_atr_stop_mult - self.MAX_ATR_MULT_DELTA
                logger.info(f"🔒 Delta SL limitado a ±{self.MAX_ATR_MULT_DELTA} → {atr_stop_mult:.2f}×")

        if self._last_atr_profit_mult is not None:
            if abs(atr_profit_mult - self._last_atr_profit_mult) > self.MAX_ATR_MULT_DELTA:
                if atr_profit_mult > self._last_atr_profit_mult:
                    atr_profit_mult = self._last_atr_profit_mult + self.MAX_ATR_MULT_DELTA
                else:
                    atr_profit_mult = self._last_atr_profit_mult - self.MAX_ATR_MULT_DELTA
                logger.info(f"🔒 Delta TP limitado a ±{self.MAX_ATR_MULT_DELTA} → {atr_profit_mult:.2f}×")

        # Clamps absolutos
        min_confidence = max(self.MIN_CONFIDENCE_FLOOR, min(self.MAX_CONFIDENCE_CEILING, min_confidence))

        # 🐛 B23 CORREGIDO: clamp duro para ATR multipliers (evita acumulación infinita)
        atr_stop_mult = max(1.0, min(6.0, atr_stop_mult))
        atr_profit_mult = max(2.0, min(9.0, atr_profit_mult))

        min_confidence = round(min_confidence, 1)
        atr_stop_mult = round(atr_stop_mult, 2)
        atr_profit_mult = round(atr_profit_mult, 2)

        mt5_now = now_mt5()

        optimized_config = {
            "updated_timestamp": int(mt5_now.timestamp() * 1000),
            "updated_iso": mt5_now.isoformat(),
            "total_trades_analyzed": total_trades,
            "win_rate_pct": round(win_rate, 2),
            "total_pnl_usd": round(total_pnl, 2),
            "profit_factor": round(profit_factor, 2),
            "wins": len(wins),
            "losses": len(losses),
            "min_confidence_threshold": min_confidence,
            "atr_stop_multiplier": atr_stop_mult,
            "atr_profit_multiplier": atr_profit_mult,
            "unprofitable_symbols": unprofitable_symbols,
            "disabled_symbols": disabled_symbols,
            "disabled_details": disabled_details,
            "by_symbol": by_symbol,
            "guardrails_applied": True,
            "learner_version": "1.5.1",
            "include_tests": self.include_tests,
        }

        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(optimized_config, f, indent=2, default=str)
            logger.info(
                f"💾 config_optimized.json | "
                f"conf={min_confidence}% | SL={atr_stop_mult}× | TP={atr_profit_mult}× | "
                f"PF={profit_factor:.2f} | disabled={len(disabled_symbols)}"
            )
        except Exception as e:
            logger.error(f"Error al guardar config_optimized.json: {e}")

        self._last_min_confidence = min_confidence
        self._last_atr_stop_mult = atr_stop_mult
        self._last_atr_profit_mult = atr_profit_mult

        return optimized_config

    def auto_evaluate_if_needed(self) -> Dict[str, Any]:
        now = time.time()
        if now - self.last_evaluation_time >= self.evaluation_interval_sec:
            return self.analyze_and_optimize()
        return self.load_current_config()

    def load_current_config(self) -> Dict[str, Any]:
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return self.get_default_config()

    def get_default_config(self) -> Dict[str, Any]:
        return {
            "min_confidence_threshold": DEFAULT_MIN_CONFIDENCE,
            "atr_stop_multiplier": 1.8,
            "atr_profit_multiplier": 3.0,
            "disabled_symbols": [],
            "disabled_details": {},
        }

    def is_symbol_disabled(self, symbol: str, config: Optional[dict] = None) -> bool:
        if config is None:
            config = self.load_current_config()

        disabled = config.get("disabled_symbols", [])
        if not disabled:
            return False

        if symbol.upper() not in [s.upper() for s in disabled]:
            return False

        details = config.get("disabled_details", {})
        sym_detail = details.get(symbol.upper(), {})
        disabled_until = sym_detail.get("disabled_until", 0)

        if disabled_until and time.time() > disabled_until:
            logger.info(f"⏰ B20: {symbol} sale de deshabilitación (expiró)")
            return False

        return True


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    agent = ContinuousLearningAgent(include_tests=False)
    config = agent.analyze_and_optimize()
    print("\n" + "=" * 60)
    print("📊 RESULTADO DE OPTIMIZACIÓN DEL AGENTE 5 (v1.5.1)")
    print("=" * 60)
    print(json.dumps(config, indent=2, default=str))
    print("=" * 60)
    print(f"\n💡 Fixes aplicados:")
    print(f"   • B20.1: min_trades_to_disable = {DISABLE_THRESHOLDS['critical']['min_trades']}")
    print(f"   • B20.2: PF sobre últimos {PF_LOOKBACK_TRADES} trades")
    print(f"   • B20.3: histéresis (PF bajo Y WR bajo)")
    print(f"   • B20.4: re-habilitación si PF ≥ {REENABLE_MIN_PF} Y WR ≥ {REENABLE_MIN_WR}% Y ≥ {REENABLE_MIN_TRADES} trades")
    print(f"   • B23:   clamp duro ATR (SL ∈ [1.0, 6.0], TP ∈ [2.0, 9.0])")
    print("=" * 60 + "\n")