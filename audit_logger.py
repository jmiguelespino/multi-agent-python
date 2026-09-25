"""
=============================================================================
QUANTEDGE AI — AUDITORÍA INSTITUCIONAL Y REGISTRO HISTÓRICO DE CICLO DE VIDA
=============================================================================
🔧 v1.6.0 — LOTE FUSIONADO 2.6+3:
  • 🐛 O3 OPTIMIZADO: buffer in-memory + flush periódico cada 5s o 50 líneas.
    Reduce I/O de disco drásticamente.
  • B6, B5, v1.3 heredados.
=============================================================================
"""
import os
import json
import time
import atexit
import threading
import logging
from datetime import datetime
from typing import Dict, Any, Optional, List

from time_utils import now_mt5_ms, now_mt5_iso

logger = logging.getLogger("AuditLogger")
logger.propagate = False

LOGS_DIR = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

AUDIT_LOG_FILE = os.path.join(LOGS_DIR, "trade_audit_history.jsonl")

IMPORTANT_REJECTION_EVENTS = {
    "CIRCUIT_BREAKER_TRIGGERED",
    "ASSET_BLOCKED",
    "ORDER_REJECTED",
}

TEST_COMMENT_MARKERS = ("qtest", "test", "integration", "smoke")


# =============================================================================
# 🐛 O3: Buffer de escritura
# =============================================================================
class _BufferedWriter:
    """Buffer in-memory con flush periódico para reducir I/O."""

    FLUSH_INTERVAL_SEC = 5.0
    FLUSH_MAX_LINES = 50

    def __init__(self, path: str):
        self.path = path
        self._buffer: List[str] = []
        self._lock = threading.Lock()
        self._last_flush_ts = time.time()

    def write(self, line: str):
        with self._lock:
            self._buffer.append(line)
            should_flush = (
                len(self._buffer) >= self.FLUSH_MAX_LINES
                or (time.time() - self._last_flush_ts) >= self.FLUSH_INTERVAL_SEC
            )
            if should_flush:
                self._flush_locked()

    def _flush_locked(self):
        if not self._buffer:
            return
        try:
            with open(self.path, "a", encoding="utf-8") as f:
                f.writelines(self._buffer)
            self._buffer.clear()
            self._last_flush_ts = time.time()
        except Exception as e:
            logger.error(f"Error en flush de audit log: {e}")

    def flush(self):
        with self._lock:
            self._flush_locked()

    def maybe_flush_periodic(self):
        """Llamado desde el main loop para forzar flush si toca."""
        with self._lock:
            if (time.time() - self._last_flush_ts) >= self.FLUSH_INTERVAL_SEC:
                self._flush_locked()


_writer = _BufferedWriter(AUDIT_LOG_FILE)


def flush_audit_log():
    """Fuerza el flush del buffer. Llamar antes de cerrar el bot."""
    _writer.flush()


atexit.register(flush_audit_log)


# =============================================================================
# Detección de tests
# =============================================================================
def _detect_is_test(metadata: Optional[Dict[str, Any]], details: str = "") -> bool:
    if metadata:
        if metadata.get("is_test") is True:
            return True
        comment = str(metadata.get("comment", "")).lower()
        if any(marker in comment for marker in TEST_COMMENT_MARKERS):
            return True

    details_lower = str(details).lower()
    if any(marker in details_lower for marker in TEST_COMMENT_MARKERS):
        return True

    return False


# =============================================================================
# API principal
# =============================================================================
def log_audit_event(
    event_type: str,
    category: str,
    symbol: str,
    reason: str,
    details: str = "",
    side: Optional[str] = None,
    price: Optional[float] = None,
    volume: Optional[float] = None,
    stop_loss: Optional[float] = None,
    take_profit: Optional[float] = None,
    old_stop_loss: Optional[float] = None,
    new_stop_loss: Optional[float] = None,
    pnl_usd: Optional[float] = None,
    pnl_percent: Optional[float] = None,
    ticket: Optional[int] = None,
    order_id: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:

    now_ms = now_mt5_ms()
    iso_time = now_mt5_iso()

    if side is not None and hasattr(side, "value"):
        side = side.value
    elif side is not None:
        side = str(side)

    is_test = _detect_is_test(metadata, details)

    record = {
        "id": f"AUD-{now_ms}-{os.urandom(2).hex().upper()}",
        "timestamp": now_ms,
        "iso_time": iso_time,
        "event_type": event_type,
        "category": category,
        "symbol": symbol,
        "reason": reason,
        "details": details,
        "side": side,
        "price": price,
        "volume": volume,
        "stop_loss": stop_loss,
        "take_profit": take_profit,
        "old_stop_loss": old_stop_loss,
        "new_stop_loss": new_stop_loss,
        "pnl_usd": pnl_usd,
        "pnl_percent": pnl_percent,
        "ticket": ticket,
        "order_id": order_id,
        "metadata": metadata or {},
        "is_test": is_test,
    }

    EVENTS_TO_NOT_PERSIST = {
        "COOLDOWN_BLOCKED",
        "MAX_POSITIONS_BLOCKED",
        "QUOTA_REACHED",
        "ANALYSIS_CONFIDENCE_THRESHOLD",
    }

    should_persist = True

    if category == "REJECTION" and event_type not in IMPORTANT_REJECTION_EVENTS:
        should_persist = False

    if event_type in EVENTS_TO_NOT_PERSIST:
        should_persist = False

    if should_persist:
        line = json.dumps(record, default=str) + "\n"
        try:
            _writer.write(line)
        except Exception as e:
            logger.error(f"Error escribiendo en audit log: {e}")

    EVENTS_TO_SILENCE_IN_CONSOLE = {
        "COOLDOWN_BLOCKED",
        "MAX_POSITIONS_BLOCKED",
        "QUOTA_REACHED",
        "ANALYSIS_CONFIDENCE_THRESHOLD",
        "ORDER_REJECTED",
    }

    if event_type in EVENTS_TO_SILENCE_IN_CONSOLE:
        return record

    test_tag = " [TEST]" if is_test else ""

    if category == "CLOSURE":
        logger.info(f"📉 {symbol} | {event_type}{test_tag} | PnL: ${pnl_usd if pnl_usd else 0:.2f}")
    elif category == "PROTECTION":
        logger.info(f"🛡️ [BLINDAJE] {symbol} | {event_type}: {reason} | SL: ${old_stop_loss} ➔ ${new_stop_loss}")
    elif category == "ORDER":
        if event_type == "OPEN_POSITION_DETECTED":
            logger.info(f"🟢 [POSICIÓN ABIERTA] Ticket #{ticket} | {side} {volume} {symbol} @ ${price} | SL: ${stop_loss} | TP: ${take_profit}")
        elif event_type == "ORDER_FILLED":
            logger.info(f"🎯 [NUEVA ORDEN] {symbol} | {side} {volume} lotes @ ${price} | SL: ${stop_loss} | TP: ${take_profit}")

    return record


def log_analysis_detected(symbol: str, confidence: float, signal_type: str, price: float, confluence_details: dict):
    return log_audit_event(
        event_type="ANALYSIS_CONFIDENCE_THRESHOLD",
        category="ANALYSIS",
        symbol=symbol,
        reason=f"Confluencia detectada: {confidence}% >= 85.0%",
        details=f"Tipo: {signal_type} @ ${price}",
        side=signal_type,
        price=price,
        metadata={**confluence_details, "overall_confidence": confidence}
    )


def log_rejection(
    symbol: str,
    reason: str,
    event_type: str = "ORDER_REJECTED",
    details: str = "",
    side: Optional[str] = None,
    price: Optional[float] = None,
    volume: Optional[float] = None,
    metadata: Optional[Dict[str, Any]] = None
):
    if event_type in IMPORTANT_REJECTION_EVENTS:
        return log_audit_event(
            event_type=event_type,
            category="REJECTION",
            symbol=symbol,
            reason=reason,
            details=details,
            side=side,
            price=price,
            volume=volume,
            metadata=metadata
        )
    else:
        logger.debug(f"⏸️  [Rechazo] {symbol} | {event_type}: {reason}")
        return {"rejected": True, "persisted": False, "event_type": event_type}


def log_break_even(
    symbol: str,
    ticket: Optional[int],
    old_sl: float,
    new_sl: float,
    current_price: float,
    profit_locked_usd: float = 0.0,
    order_id: Optional[str] = None
):
    return log_audit_event(
        event_type="SL_MODIFIED_BREAK_EVEN",
        category="PROTECTION",
        symbol=symbol,
        reason="Stop Loss movido a Break-Even tras alcanzar +1.2x ATR.",
        details=f"Precio actual ${current_price}. Ganancia asegurada: ${profit_locked_usd:.2f} USD.",
        ticket=ticket,
        order_id=order_id,
        price=current_price,
        old_stop_loss=old_sl,
        new_stop_loss=new_sl
    )


def log_trailing_stop(
    symbol: str,
    ticket: Optional[int],
    old_sl: float,
    new_sl: float,
    current_price: float,
    order_id: Optional[str] = None
):
    return log_audit_event(
        event_type="TRAILING_STOP_UPDATED",
        category="PROTECTION",
        symbol=symbol,
        reason="Trailing Stop dinámico ajustado.",
        details=f"Precio actual ${current_price}. Nuevo SL: ${new_sl}",
        ticket=ticket,
        order_id=order_id,
        price=current_price,
        old_stop_loss=old_sl,
        new_stop_loss=new_sl
    )


def log_order_filled(
    symbol: str,
    side: str,
    volume: float,
    fill_price: float,
    sl: float,
    tp: float,
    ticket: Optional[int] = None,
    order_id: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None
):
    side_str = side.value if hasattr(side, "value") else str(side)

    return log_audit_event(
        event_type="ORDER_FILLED",
        category="ORDER",
        symbol=symbol,
        reason="Orden ejecutada y posición abierta en MetaTrader 5.",
        details=f"{side_str} {volume} {symbol} @ ${fill_price} | SL: ${sl} | TP: ${tp}",
        side=side_str,
        price=fill_price,
        volume=volume,
        stop_loss=sl,
        take_profit=tp,
        ticket=ticket,
        order_id=order_id,
        metadata=metadata
    )


def log_position_closed(
    symbol: str,
    side: str,
    volume: float,
    entry_price: float,
    exit_price: float,
    pnl_usd: float,
    pnl_percent: float,
    reason: str,
    ticket: Optional[int] = None,
    order_id: Optional[str] = None,
    duration_sec: int = 0,
    is_test: bool = False
):
    reason_upper = str(reason).upper() if reason else "UNKNOWN"

    if reason_upper == "TAKE_PROFIT":
        event_type = "TAKE_PROFIT_HIT"
    elif reason_upper == "STOP_LOSS":
        event_type = "STOP_LOSS_HIT"
    elif reason_upper == "TRAILING_STOP":
        event_type = "TRAILING_STOP_HIT"
    elif reason_upper == "MANUAL_CLOSE":
        event_type = "MANUAL_CLOSE"
    elif reason_upper == "UNKNOWN":
        event_type = "CLOSE_UNKNOWN"
    else:
        event_type = "MANUAL_CLOSE"

    side_str = side.value if hasattr(side, "value") else str(side)

    metadata = {
        "duration_sec": duration_sec,
        "entry_price": entry_price,
        "exit_price": exit_price,
        "close_reason": reason_upper,
    }
    if is_test:
        metadata["is_test"] = True

    return log_audit_event(
        event_type=event_type,
        category="CLOSURE",
        symbol=symbol,
        reason=f"Posición cerrada por {reason_upper}.",
        details=f"Entrada: ${entry_price} ➔ Salida: ${exit_price} | Duración: {duration_sec}s | PnL: ${pnl_usd:.2f}",
        side=side_str,
        price=exit_price,
        volume=volume,
        pnl_usd=pnl_usd,
        pnl_percent=pnl_percent,
        ticket=ticket,
        order_id=order_id,
        metadata=metadata
    )