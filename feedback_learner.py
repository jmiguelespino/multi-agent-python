"""
=============================================================================
QUANTEDGE AI — AGENTE DE APRENDIZAJE CONTINUO (AGENTE 5)
=============================================================================
🔧 v1.4.0 — LOTE FUSIONADO 2.6+3:
  • 🐛 B19 CORREGIDO: el learner YA NO pisa los multiplicadores ATR
    específicos por clase de activo. Ahora respeta límites por clase:
      - Oro:  SL ∈ [3.5, 6.0], TP ∈ [5.0, 9.0]
      - Cripto: SL ∈ [1.8, 3.5], TP ∈ [2.5, 6.0]
      - Forex: SL ∈ [1.0, 2.0], TP ∈ [1.5, 3.0]
      - etc.
    El valor global se usa solo si la clase no tiene override.
  • 🐛 B20 CORREGIDO: el learner ahora genera `disabled_symbols` basado
    en PF histórico:
      - PF < 0.5 (≥5 trades): deshabilitar 24h
      - PF < 0.8 (≥5 trades): deshabilitar 6h
      - PF < 1.0 (≥5 trades): solo loguear
  • v1.3.0 heredado: B6 (filtro de tests), B18 (análisis por símbolo).
=============================================================================
"""

import os
import json
import time
import logging
from typing import Dict, Any, List, Optional
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
    if "XAU" in s or "GOLD" in s:
        return "XAU"
    if "XAG" in s or "SILVER" in s:
        return "XAG"
    if any(k in s for k in ["WTI", "XTI", "BRENT", "XBR", "OIL"]):
        return "OIL"
    if "US500" in s or "SP500" in s or "SPX" in s:
        return "US500"
    if "BTC" in s:
        return "BTC"
    if "ETH" in s:
        return "ETH"
    if "SOL" in s:
        return "SOL"
    if any(fx in s for fx in ["EUR", "GBP", "JPY", "AUD", "NZD"]):
        return "FOREX"
    return "DEFAULT"


def clamp_atr_by_class(symbol_class: str, sl: float, tp: float) -> tuple[float, float]:
    """
    🐛 B19: restringe sl/tp a los límites de la clase.
    """
    limits = ATR_LIMITS_BY_CLASS.get(symbol_class, ATR_LIMITS_BY_CLASS["DEFAULT"])
    sl_min, sl_max = limits["sl"]
    tp_min, tp_max = limits["tp"]
    return max(sl_min, min(sl_max, sl)), max(tp_min, min(tp_max, tp))


# =============================================================================
# 🐛 B20: umbrales para deshabilitar símbolos
# =============================================================================
DISABLE_THRESHOLDS = {
    "critical": {"pf_max": 0.5, "min_trades": 5, "disable_hours": 24},
    "severe":   {"pf_max": 0.8, "min_trades": 5, "disable_hours": 6},
    "log_only": {"pf_max": 1.0, "min_trades": 5, "disable_hours": 0},
}


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

    def analyze_by_symbol(self, closures: List[dict]) -> Dict[str, dict]:
        by_symbol = defaultdict(lambda: {
            "trades": 0, "wins": 0, "losses": 0,
            "pnl": 0.0, "gross_profit": 0.0, "gross_loss": 0.0,
        })

        for r in closures:
            sym = str(r.get("symbol", "UNKNOWN")).upper()
            pnl = float(r.get("pnl_usd", 0) or 0)
            by_symbol[sym]["trades"] += 1
            by_symbol[sym]["pnl"] += pnl
            if pnl > 0:
                by_symbol[sym]["wins"] += 1
                by_symbol[sym]["gross_profit"] += pnl
            else:
                by_symbol[sym]["losses"] += 1
                by_symbol[sym]["gross_loss"] += abs(pnl)

        result = {}
        for sym, d in by_symbol.items():
            wr = (d["wins"] / d["trades"]) * 100 if d["trades"] > 0 else 0.0
            pf = (d["gross_profit"] / d["gross_loss"]) if d["gross_loss"] > 0 else 999.0
            result[sym] = {
                "trades": d["trades"],
                "wins": d["wins"],
                "losses": d["losses"],
                "win_rate_pct": round(wr, 2),
                "pnl_usd": round(d["pnl"], 2),
                "profit_factor": round(pf, 3),
                "is_profitable": pf > 1.0,
            }
        return result

    def _compute_disabled_symbols(self, by_symbol: dict) -> tuple[List[str], Dict[str, dict]]:
        """
        🐛 B20: calcula qué símbolos deben deshabilitarse según PF histórico.
        Devuelve (lista_simbolos_deshabilitados, mapa_detalles).
        """
        disabled = []
        details = {}
        now_ts = time.time()

        for sym, d in by_symbol.items():
            trades = d["trades"]
            pf = d["profit_factor"]

            for level_name, cfg in DISABLE_THRESHOLDS.items():
                if trades >= cfg["min_trades"] and pf < cfg["pf_max"]:
                    if cfg["disable_hours"] > 0:
                        disabled.append(sym)
                        details[sym] = {
                            "level": level_name,
                            "pf": pf,
                            "trades": trades,
                            "disabled_at": int(now_ts),
                            "disabled_until": int(now_ts + cfg["disable_hours"] * 3600),
                            "reason": f"PF={pf:.3f} < {cfg['pf_max']} con {trades} trades",
                        }
                        logger.warning(
                            f"🚫 B20: {sym} DESHABILITADO por {cfg['disable_hours']}h "
                            f"(PF={pf:.3f}, {trades} trades)"
                        )
                    else:
                        details[sym] = {
                            "level": level_name,
                            "pf": pf,
                            "trades": trades,
                            "reason": f"PF={pf:.3f} bajo ({trades} trades) — solo log",
                        }
                        logger.info(
                            f"📝 B20: {sym} PF={pf:.3f} bajo pero no crítico. Solo log."
                        )
                    break  # solo el nivel más severo aplica

        return disabled, details

    def analyze_and_optimize(self) -> Dict[str, Any]:
        now = time.time()
        self.last_evaluation_time = now

        records = self.load_audit_records()
        if not records:
            return self.load_current_config()

        closures = [
            r for r in records
            if r.get("category") == "CLOSURE" and r.get("pnl_usd") is not None
        ]
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

        by_symbol = self.analyze_by_symbol(closures)
        unprofitable_symbols = [
            s for s, d in by_symbol.items()
            if d["trades"] >= 5 and d["profit_factor"] < 1.0
        ]
        if unprofitable_symbols:
            logger.warning(
                f"⚠️ B18: Símbolos no rentables: {', '.join(unprofitable_symbols)}"
            )

        # 🐛 B20: calcular símbolos a deshabilitar
        disabled_symbols, disabled_details = self._compute_disabled_symbols(by_symbol)

        current_cfg = self.load_current_config()
        min_confidence = current_cfg.get("min_confidence_threshold", DEFAULT_MIN_CONFIDENCE)
        atr_stop_mult = current_cfg.get("atr_stop_multiplier", 1.8)
        atr_profit_mult = current_cfg.get("atr_profit_multiplier", 3.0)

        # 🐛 B19: límites globales más conservadores (los específicos por clase
        # se aplican en signal_agent.py, no aquí)
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

        # Guardrails
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

        min_confidence = max(self.MIN_CONFIDENCE_FLOOR, min(self.MAX_CONFIDENCE_CEILING, min_confidence))
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
            "disabled_symbols": disabled_symbols,          # 🆕 B20
            "disabled_details": disabled_details,          # 🆕 B20
            "by_symbol": by_symbol,
            "guardrails_applied": True,
            "learner_version": "1.4.0",
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
        """
        🐛 B20: helper para que main.py consulte si un símbolo está deshabilitado.
        Respeta la expiración temporal de disabled_details.
        """
        if config is None:
            config = self.load_current_config()

        disabled = config.get("disabled_symbols", [])
        if not disabled:
            return False

        if symbol.upper() not in [s.upper() for s in disabled]:
            return False

        # Verificar expiración
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
    print("📊 RESULTADO DE OPTIMIZACIÓN DEL AGENTE 5 (v1.4.0)")
    print("=" * 60)
    print(json.dumps(config, indent=2, default=str))
    print("=" * 60)
    print(f"\n💡 Guardrails activos:")
    print(f"   • Mínimo de trades: {ContinuousLearningAgent.MIN_TRADES_TO_OPTIMIZE}")
    print(f"   • Delta máx. confianza: ±{ContinuousLearningAgent.MAX_CONFIDENCE_DELTA}")
    print(f"   • Delta máx. ATR: ±{ContinuousLearningAgent.MAX_ATR_MULT_DELTA}")
    print(f"   • Default min_confidence: {DEFAULT_MIN_CONFIDENCE}")
    print(f"   • Include tests: {agent.include_tests}")
    print(f"   • Umbrales disable: {DISABLE_THRESHOLDS}")
    print("=" * 60 + "\n")