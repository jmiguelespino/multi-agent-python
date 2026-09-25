"""
=============================================================================
QUANTEDGE AI — MÓDULO DE TIEMPO UNIFICADO
=============================================================================
Reglas del proyecto:
  • MT5 opera en UTC+3 (IC Markets SC Demo).
  • El PC puede estar en cualquier zona horaria.
  • Presentación (logs, ISO strings, JSONL `iso_time`) → hora MT5 (UTC+3).
  • Cálculos internos (duración, expiración, comparaciones) → epoch UTC.

Uso:
    from time_utils import (
        TZ_MT5,
        now_mt5,           # datetime con tzinfo UTC+3
        now_mt5_ms,        # int epoch UTC en milisegundos (para JSONL `timestamp`)
        now_mt5_iso,       # str ISO en hora MT5 (termina en "+03:00")
        mt5_ms_to_epoch,   # convierte time_msc de MT5 a epoch UTC real (segundos)
        epoch_to_mt5_iso,  # convierte epoch UTC a ISO hora MT5
    )

⚠️ Regla crítica sobre `p.time_msc` de MT5:
    MT5 devuelve `time_msc` con la hora del servidor (UTC+3) "disfrazada" como
    si fuera epoch UTC. Es decir, un trade a las 05:31:01 hora MT5 se reporta
    como `2026-09-25T05:31:01Z` cuando en realidad es `2026-09-25T02:31:01Z`.
    `mt5_ms_to_epoch()` corrige ese desfase.
=============================================================================
"""
from datetime import datetime, timezone, timedelta
from typing import Optional


# Zona horaria del servidor MT5 (IC Markets SC Demo)
TZ_MT5 = timezone(timedelta(hours=3))


# =============================================================================
# AHORA (en hora MT5 y en epoch UTC)
# =============================================================================
def now_mt5() -> datetime:
    """Devuelve un datetime con tzinfo UTC+3 en el momento actual."""
    return datetime.now(TZ_MT5)


def now_mt5_ms() -> int:
    """
    Devuelve epoch UTC en milisegundos.
    Este es el valor que se guarda en el JSONL como `timestamp`.
    Es invariante a la zona horaria del PC.
    """
    return int(datetime.now(TZ_MT5).timestamp() * 1000)


def now_mt5_iso() -> str:
    """
    Devuelve string ISO 8601 en hora MT5, con sufijo de zona "+03:00".
    Este es el valor que se guarda en el JSONL como `iso_time`.
    Ejemplo: "2026-09-25T05:31:01.871644+03:00"
    """
    return datetime.now(TZ_MT5).isoformat()


# =============================================================================
# CONVERSIÓN MT5 → EPOCH UTC
# =============================================================================
def mt5_ms_to_epoch(time_msc: Optional[int]) -> float:
    """
    Convierte un `time_msc` de MT5 (milisegundos, en hora del servidor UTC+3
    reportada como si fuera epoch UTC) a epoch UTC real en segundos.

    Ejemplo:
        time_msc = 1790303461871
        MT5 lo reporta como 2026-09-25T05:31:01.871 (hora MT5)
        Realmente son 2026-09-25T02:31:01.871 UTC
        → return 1790292661.871

    Args:
        time_msc: valor de `p.time_msc` o `d.time_msc` de MT5.

    Returns:
        Epoch UTC en segundos (float). Devuelve 0.0 si `time_msc` es inválido.
    """
    if not time_msc or time_msc <= 0:
        return 0.0
    try:
        # MT5 reporta epoch en hora del servidor (UTC+3) "disfrazado" de UTC.
        # Restamos el offset del servidor para obtener epoch UTC real.
        SERVER_OFFSET_SECONDS = 3 * 3600  # UTC+3
        return (time_msc / 1000.0) - SERVER_OFFSET_SECONDS
    except (ValueError, OSError, OverflowError):
        return 0.0

def mt5_sec_to_epoch(time_sec: Optional[int]) -> float:
    """
    Igual que `mt5_ms_to_epoch` pero para `time` (segundos) en lugar de `time_msc`.
    """
    if not time_sec or time_sec <= 0:
        return 0.0
    return mt5_ms_to_epoch(time_sec * 1000)


# =============================================================================
# CONVERSIÓN EPOCH UTC → HORA MT5
# =============================================================================
def epoch_to_mt5_iso(epoch_seconds: Optional[float]) -> str:
    """
    Convierte epoch UTC (segundos) a string ISO en hora MT5.
    Ejemplo: 1790293261.871 → "2026-09-25T05:31:01.871000+03:00"
    """
    if not epoch_seconds or epoch_seconds <= 0:
        return ""
    try:
        dt_mt5 = datetime.fromtimestamp(epoch_seconds, tz=TZ_MT5)
        return dt_mt5.isoformat()
    except (ValueError, OSError, OverflowError):
        return ""


def epoch_ms_to_mt5_iso(epoch_ms: Optional[int]) -> str:
    """
    Igual que `epoch_to_mt5_iso` pero acepta epoch en milisegundos.
    Útil para formatear el `timestamp` del JSONL.
    """
    if not epoch_ms or epoch_ms <= 0:
        return ""
    return epoch_to_mt5_iso(epoch_ms / 1000.0)


# =============================================================================
# HELPERS ADICIONALES
# =============================================================================
def epoch_to_mt5_datetime(epoch_seconds: Optional[float]) -> Optional[datetime]:
    """Convierte epoch UTC a datetime con tzinfo UTC+3."""
    if not epoch_seconds or epoch_seconds <= 0:
        return None
    try:
        return datetime.fromtimestamp(epoch_seconds, tz=TZ_MT5)
    except (ValueError, OSError, OverflowError):
        return None


def format_duration_sec(seconds: int) -> str:
    """
    Formatea una duración en segundos a string legible.
    Ej: 3661 → "1h 1m 1s"
    """
    if seconds < 0:
        return f"-{format_duration_sec(-seconds)}"
    if seconds < 60:
        return f"{seconds}s"
    if seconds < 3600:
        return f"{seconds // 60}m {seconds % 60}s"
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours}h {minutes}m {secs}s"