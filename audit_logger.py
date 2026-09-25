"""
=============================================================================
QUANTEDGE AI — AUDITORÍA INSTITUCIONAL Y REGISTRO HISTÓRICO DE CICLO DE VIDA
=============================================================================
🔧 v1.3:
  • 🐛 BUG #2 de hora CORREGIDO: `iso_time` ahora está en hora MT5 (UTC+3),
    consistente con los logs de consola.
    Antes: "2026-09-25T02:31:01.871644Z" (UTC)
    Ahora: "2026-09-25T05:31:01.871644+03:00" (MT5)
  • `timestamp` se mantiene en epoch UTC (para comparaciones y cálculos).
  • Solo 1 archivo JSONL (eliminado ../public/).
  • Los rechazos comunes NO se escriben al JSONL (rate limiter).
  • Solo persisten eventos críticos (CIRCUIT_BREAKER, ASSET_BLOCKED).
  • logger.propagate = False.
  • Normalización de side Enum → string.
=============================================================================
"""
import os
import json
import time
import logging
from datetime import datetime
from typing import Dict, Any, Optional

from time_utils import now_mt5_ms, now_mt5_iso

logger = logging.getLogger("AuditLogger")
logger.propagate = False

# 🔧 v1.2: solo 1 directorio de logs
LOGS_DIR = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

AUDIT_LOG_FILE = os.path.join(LOGS_DIR, "trade_audit_history.jsonl")

# 🔧 Eventos de rechazo que SÍ se persisten al JSONL
IMPORTANT_REJECTION_EVENTS = {
    "CIRCUIT_BREAKER_TRIGGERED",
    "ASSET_BLOCKED",
    "ORDER_REJECTED",
}


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

    # 🐛 BUG #2 de hora CORREGIDO:
    # timestamp → epoch UTC (ms) para comparaciones
    # iso_time  → hora MT5 (UTC+3) con sufijo "+03:00"
    now_ms = now_mt5_ms()
    iso_time = now_mt5_iso()

    # Normalizar side si es Enum
    if side is not None and hasattr(side, "value"):
        side = side.value
    elif side is not None:
        side = str(side)

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
        "metadata": metadata or {}
    }

    # 🔧 v1.2: Solo escribimos al JSONL eventos importantes
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
        line = json.dumps(record) + "\n"
        try:
            with open(AUDIT_LOG_FILE, "a", encoding="utf-8") as f:
                f.write(line)
        except Exception as e:
            logger.error(f"Error escribiendo en {AUDIT_LOG_FILE}: {e}")

    # ─── Salida en consola (solo eventos importantes) ────────────────
    EVENTS_TO_SILENCE_IN_CONSOLE = {
        "COOLDOWN_BLOCKED",
        "MAX_POSITIONS_BLOCKED",
        "QUOTA_REACHED",
        "ANALYSIS_CONFIDENCE_THRESHOLD",
        "ORDER_REJECTED",
    }

    if event_type in EVENTS_TO_SILENCE_IN_CONSOLE:
        return record

    if category == "CLOSURE":
        logger.info(f"📉 {symbol} | {event_type} | PnL: ${pnl_usd if pnl_usd else 0:.2f}")
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
    """
    🔧 v1.2: Solo persiste rechazos importantes al JSONL.
    Los comunes (COOLDOWN, QUOTA) solo van a debug.
    """
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
        reason="Stop Loss movido a Break-Even tras alcanzar +1.2x ATR de recorrido favorable.",
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
        reason="Trailing Stop dinámico ajustado para bloquear utilidades.",
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
    duration_sec: int = 0
):
    event_type = (
        "TAKE_PROFIT_HIT" if reason == "TAKE_PROFIT"
        else "STOP_LOSS_HIT" if reason == "STOP_LOSS"
        else "TRAILING_STOP_HIT" if reason == "TRAILING_STOP"
        else "MANUAL_CLOSE"
    )
    side_str = side.value if hasattr(side, "value") else str(side)

    return log_audit_event(
        event_type=event_type,
        category="CLOSURE",
        symbol=symbol,
        reason=f"Posición cerrada por {reason}.",
        details=f"Entrada: ${entry_price} ➔ Salida: ${exit_price} | Duración: {duration_sec}s | PnL: ${pnl_usd:.2f}",
        side=side_str,
        price=exit_price,
        volume=volume,
        pnl_usd=pnl_usd,
        pnl_percent=pnl_percent,
        ticket=ticket,
        order_id=order_id,
        metadata={"duration_sec": duration_sec, "entry_price": entry_price, "exit_price": exit_price, "close_reason": reason}
    )