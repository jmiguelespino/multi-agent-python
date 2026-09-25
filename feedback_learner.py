"""
=============================================================================
QUANTEDGE AI — AGENTE DE APRENDIZAJE CONTINUO (AGENTE 5)
=============================================================================
🔧 v1.2.1:
  • logger.propagate = False para evitar doble logging.
  • Guardrails anti-overfitting (v1.2).
=============================================================================
"""

import os
import json
import time
import logging
from typing import Dict, Any, List, Optional

logger = logging.getLogger("FeedbackLearner")
logger.propagate = False  # 🔧 evita duplicación con el root logger

LOGS_DIR = os.path.join(os.path.dirname(__file__), "logs")
AUDIT_LOG_FILE = os.path.join(LOGS_DIR, "trade_audit_history.jsonl")
CONFIG_OPTIMIZED_FILE = os.path.join(os.path.dirname(__file__), "config_optimized.json")


class ContinuousLearningAgent:
    MIN_TRADES_TO_OPTIMIZE = 30
    MAX_CONFIDENCE_DELTA = 2.0
    MAX_ATR_MULT_DELTA = 0.3
    MIN_CONFIDENCE_FLOOR = 80.0
    MAX_CONFIDENCE_CEILING = 95.0
    MIN_ATR_STOP = 1.0
    MAX_ATR_STOP = 3.5
    MIN_ATR_PROFIT = 1.5
    MAX_ATR_PROFIT = 6.0

    def __init__(
        self,
        log_path: str = AUDIT_LOG_FILE,
        config_path: str = CONFIG_OPTIMIZED_FILE,
        evaluation_interval_sec: float = 300.0,
        lookback_days: int = 30,
    ):
        self.log_path = log_path
        self.config_path = config_path
        self.evaluation_interval_sec = evaluation_interval_sec
        self.lookback_days = lookback_days
        self.last_evaluation_time: float = 0.0

        self._last_min_confidence: Optional[float] = None
        self._last_atr_stop_mult: Optional[float] = None
        self._last_atr_profit_mult: Optional[float] = None

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

        try:
            with open(self.log_path, "r", encoding="utf-8") as f:
                for line in f:
                    line_str = line.strip()
                    if not line_str:
                        continue
                    try:
                        rec = json.loads(line_str)
                        if rec.get("timestamp", 0) >= cutoff_ms:
                            records.append(rec)
                    except json.JSONDecodeError:
                        continue
        except Exception as e:
            logger.error(f"Error al leer archivo de auditoría para aprendizaje: {e}")

        return records

    def analyze_and_optimize(self) -> Dict[str, Any]:
        now = time.time()
        self.last_evaluation_time = now

        records = self.load_audit_records()
        if not records:
            return self.get_default_config()

        closures = [
            r for r in records
            if r.get("category") == "CLOSURE" and r.get("pnl_usd") is not None
        ]
        total_trades = len(closures)

        if total_trades < self.MIN_TRADES_TO_OPTIMIZE:
            logger.info(
                f"📊 [FeedbackLearner] Solo {total_trades} cierres registrados. "
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

        current_cfg = self.load_current_config()
        min_confidence = current_cfg.get("min_confidence_threshold", 86.0)
        atr_stop_mult = current_cfg.get("atr_stop_multiplier", 1.8)
        atr_profit_mult = current_cfg.get("atr_profit_multiplier", 3.0)

        if win_rate < 50.0:
            min_confidence = 90.0
            atr_stop_mult = 2.2
            logger.info(f"📉 [FeedbackLearner] Win Rate bajo ({win_rate:.1f}%). Endureciendo.")
        elif win_rate < 55.0:
            min_confidence = 88.5
            atr_stop_mult = 2.0
            logger.info(f"📊 [FeedbackLearner] Win Rate mediocre ({win_rate:.1f}%). Subiendo umbral.")
        elif win_rate >= 70.0:
            min_confidence = 85.0
            logger.info(f"🔥 [FeedbackLearner] Excelente Win Rate ({win_rate:.1f}%). Relajando.")

        if profit_factor < 1.0:
            min_confidence = max(min_confidence, 89.0)
            logger.info(f"⚠️ [FeedbackLearner] Profit Factor {profit_factor:.2f} < 1.0. Endureciendo.")
        elif profit_factor > 2.0:
            atr_profit_mult = atr_profit_mult * 1.1
            logger.info(f"🚀 [FeedbackLearner] Profit Factor {profit_factor:.2f} > 2.0. Extendiendo TP.")

        # GUARDRAIL: limitar delta de confianza
        if self._last_min_confidence is not None:
            if abs(min_confidence - self._last_min_confidence) > self.MAX_CONFIDENCE_DELTA:
                if min_confidence > self._last_min_confidence:
                    min_confidence = self._last_min_confidence + self.MAX_CONFIDENCE_DELTA
                else:
                    min_confidence = self._last_min_confidence - self.MAX_CONFIDENCE_DELTA
                logger.info(f"🔒 Delta de confianza limitado a ±{self.MAX_CONFIDENCE_DELTA} → {min_confidence:.1f}%")

        if self._last_atr_stop_mult is not None:
            if abs(atr_stop_mult - self._last_atr_stop_mult) > self.MAX_ATR_MULT_DELTA:
                if atr_stop_mult > self._last_atr_stop_mult:
                    atr_stop_mult = self._last_atr_stop_mult + self.MAX_ATR_MULT_DELTA
                else:
                    atr_stop_mult = self._last_atr_stop_mult - self.MAX_ATR_MULT_DELTA
                logger.info(f"🔒 Delta de SL limitado a ±{self.MAX_ATR_MULT_DELTA} → {atr_stop_mult:.2f}×")

        if self._last_atr_profit_mult is not None:
            if abs(atr_profit_mult - self._last_atr_profit_mult) > self.MAX_ATR_MULT_DELTA:
                if atr_profit_mult > self._last_atr_profit_mult:
                    atr_profit_mult = self._last_atr_profit_mult + self.MAX_ATR_MULT_DELTA
                else:
                    atr_profit_mult = self._last_atr_profit_mult - self.MAX_ATR_MULT_DELTA
                logger.info(f"🔒 Delta de TP limitado a ±{self.MAX_ATR_MULT_DELTA} → {atr_profit_mult:.2f}×")

        min_confidence = max(self.MIN_CONFIDENCE_FLOOR, min(self.MAX_CONFIDENCE_CEILING, min_confidence))
        atr_stop_mult = max(self.MIN_ATR_STOP, min(self.MAX_ATR_STOP, atr_stop_mult))
        atr_profit_mult = max(self.MIN_ATR_PROFIT, min(self.MAX_ATR_PROFIT, atr_profit_mult))

        min_confidence = round(min_confidence, 1)
        atr_stop_mult = round(atr_stop_mult, 2)
        atr_profit_mult = round(atr_profit_mult, 2)

        optimized_config = {
            "updated_timestamp": int(now * 1000),
            "updated_iso": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(now)),
            "total_trades_analyzed": total_trades,
            "win_rate_pct": round(win_rate, 2),
            "total_pnl_usd": round(total_pnl, 2),
            "profit_factor": round(profit_factor, 2),
            "wins": len(wins),
            "losses": len(losses),
            "min_confidence_threshold": min_confidence,
            "atr_stop_multiplier": atr_stop_mult,
            "atr_profit_multiplier": atr_profit_mult,
            "guardrails_applied": True,
            "learner_version": "1.2.1",
        }

        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(optimized_config, f, indent=2)
            logger.info(
                f"💾 config_optimized.json | "
                f"conf={min_confidence}% | SL={atr_stop_mult}× | TP={atr_profit_mult}×"
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
            "min_confidence_threshold": 86.0,
            "atr_stop_multiplier": 1.8,
            "atr_profit_multiplier": 3.0
        }


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    agent = ContinuousLearningAgent()
    config = agent.analyze_and_optimize()
    print("\n" + "=" * 60)
    print("📊 RESULTADO DE OPTIMIZACIÓN DEL AGENTE 5 (v1.2.1)")
    print("=" * 60)
    print(json.dumps(config, indent=2))
    print("=" * 60)
    print(f"\n💡 Guardrails activos:")
    print(f"   • Mínimo de trades: {ContinuousLearningAgent.MIN_TRADES_TO_OPTIMIZE}")
    print(f"   • Delta máx. confianza: ±{ContinuousLearningAgent.MAX_CONFIDENCE_DELTA}")
    print(f"   • Delta máx. ATR: ±{ContinuousLearningAgent.MAX_ATR_MULT_DELTA}")
    print("=" * 60 + "\n")