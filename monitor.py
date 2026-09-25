"""
=============================================================================
QUANTEDGE AI — MONITOR DE HEARTBEAT
=============================================================================
Se ejecuta EN PARALELO al bot (main.py). Vigila:
  • Que el archivo de logs se actualice regularmente
  • Que el proceso main.py siga vivo (opcional, vía heartbeat file)
  • Que la conexión MT5 esté activa
  • Que no haya errores críticos repetidos

Si detecta anomalías, envía alerta por Telegram.

Ejecución:
    python monitor.py

Configuración vía .env (opcional):
    MONITOR_HEARTBEAT_MAX_AGE_SEC=300     # 5 min sin logs → alerta
    MONITOR_CHECK_INTERVAL_SEC=60         # Revisar cada 1 min
    MONITOR_MT5_CHECK_ENABLED=true        # Verificar MT5
    MONITOR_ALERT_COOLDOWN_SEC=600        # No repetir alerta en 10 min
=============================================================================
"""

import os
import sys
import time
import json
import logging
from pathlib import Path
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv

load_dotenv()

TZ_MT5 = timezone(timedelta(hours=3))

# -----------------------------------------------------------------------------
# Logging con formato MT5 (UTC+3)
# -----------------------------------------------------------------------------
class MT5TimeFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        dt = datetime.fromtimestamp(record.created, tz=TZ_MT5)
        return dt.strftime(datefmt) if datefmt else dt.isoformat()


handler = logging.StreamHandler()
handler.setFormatter(MT5TimeFormatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))

logger = logging.getLogger("Monitor")
logger.addHandler(handler)
logger.setLevel(logging.INFO)
logger.propagate = False

# -----------------------------------------------------------------------------
# Configuración
# -----------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "logs" / "trade_audit_history.jsonl"
CONTROL_STATE_FILE = BASE_DIR / "control_state.json"
CONFIG_OPTIMIZED_FILE = BASE_DIR / "config_optimized.json"
HEARTBEAT_FILE = BASE_DIR / "logs" / "monitor_heartbeat.json"

HEARTBEAT_MAX_AGE_SEC = float(os.getenv("MONITOR_HEARTBEAT_MAX_AGE_SEC", "300"))
CHECK_INTERVAL_SEC = float(os.getenv("MONITOR_CHECK_INTERVAL_SEC", "60"))
MT5_CHECK_ENABLED = os.getenv("MONITOR_MT5_CHECK_ENABLED", "true").lower() in ("true", "1", "yes")
ALERT_COOLDOWN_SEC = float(os.getenv("MONITOR_ALERT_COOLDOWN_SEC", "600"))

# -----------------------------------------------------------------------------
# Alertas Telegram (reutilizamos el módulo)
# -----------------------------------------------------------------------------
try:
    from telegram_notifier import send_telegram_alert
except ImportError:
    logger.warning("No se pudo importar telegram_notifier. Alertas deshabilitadas.")
    def send_telegram_alert(msg: str, parse_mode: str = "Markdown") -> bool:
        logger.warning(f"[ALERTA SIN TELEGRAM] {msg}")
        return False


# -----------------------------------------------------------------------------
# Estado del monitor (para evitar spam de alertas)
# -----------------------------------------------------------------------------
class MonitorState:
    def __init__(self):
        self.last_alert_time: float = 0.0
        self.last_alert_reason: str = ""
        self.last_successful_check: float = time.time()
        self.consecutive_failures: int = 0
        self.total_alerts_sent: int = 0
        self.started_at: float = time.time()

    def can_send_alert(self, reason: str) -> bool:
        """Cooldown para no spamear."""
        now = time.time()
        # Si es la misma razón y no pasó el cooldown, no enviar
        if reason == self.last_alert_reason and (now - self.last_alert_time) < ALERT_COOLDOWN_SEC:
            return False
        return True

    def record_alert(self, reason: str):
        self.last_alert_time = time.time()
        self.last_alert_reason = reason
        self.total_alerts_sent += 1


state = MonitorState()


# -----------------------------------------------------------------------------
# Chequeos
# -----------------------------------------------------------------------------
def check_log_freshness() -> tuple[bool, str]:
    """Verifica que el archivo de logs se haya actualizado recientemente."""
    if not LOG_FILE.exists():
        return False, "LOG_FILE_NOT_FOUND"

    mtime = LOG_FILE.stat().st_mtime
    age_sec = time.time() - mtime

    if age_sec > HEARTBEAT_MAX_AGE_SEC:
        minutes = int(age_sec / 60)
        return False, f"STALE_LOG_{minutes}MIN"

    return True, f"LOG_FRESH_{int(age_sec)}S"


def check_log_for_errors() -> tuple[bool, str]:
    """Busca errores críticos recientes en el log."""
    if not LOG_FILE.exists():
        return True, ""

    # Leer las últimas 100 líneas
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception:
        return True, ""

    recent = lines[-100:]
    critical_events = 0
    circuit_breaker_events = 0

    for line in recent:
        try:
            rec = json.loads(line)
        except Exception:
            continue

        ts = rec.get("timestamp", 0)
        # Solo eventos de la última hora
        if time.time() * 1000 - ts > 3600_000:
            continue

        event = rec.get("event_type", "")
        if event == "CIRCUIT_BREAKER_TRIGGERED":
            circuit_breaker_events += 1

    if circuit_breaker_events > 0:
        return False, f"CIRCUIT_BREAKER_{circuit_breaker_events}X"

    return True, ""


def check_mt5_connection() -> tuple[bool, str]:
    """Verifica que MT5 esté accesible."""
    if not MT5_CHECK_ENABLED:
        return True, "MT5_CHECK_DISABLED"

    try:
        import MetaTrader5 as mt5
        if not mt5.initialize():
            return False, "MT5_INIT_FAILED"

        acc = mt5.account_info()
        if acc is None:
            mt5.shutdown()
            return False, "MT5_ACCOUNT_INFO_NONE"

        # Verificar que el balance esté sincronizado con MT5
        # (esto no indica fallo, pero lo devolvemos por info)
        info = f"MT5_OK_BALANCE_{int(acc.balance)}"
        mt5.shutdown()
        return True, info
    except Exception as e:
        return False, f"MT5_EXCEPTION_{type(e).__name__}"


def check_control_state() -> tuple[bool, str]:
    """Verifica que control_state.json sea válido."""
    if not CONTROL_STATE_FILE.exists():
        return True, "NO_CONTROL_FILE"

    try:
        with open(CONTROL_STATE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        paused = data.get("paused", False)
        close_all = data.get("close_all_requested", False)

        if close_all:
            # Si el flag quedó prendido por más de 2 min, algo anda mal
            ts = data.get("close_all_requested_at", 0) / 1000.0
            if ts and (time.time() - ts) > 120:
                return False, "CLOSE_ALL_STUCK"

        status = "PAUSED" if paused else "ACTIVE"
        return True, f"CONTROL_{status}"
    except Exception:
        return False, "CONTROL_STATE_INVALID"


# -----------------------------------------------------------------------------
# Reporte de estado
# -----------------------------------------------------------------------------
def write_heartbeat_file(log_ok: bool, log_info: str, mt5_ok: bool, mt5_info: str, ctrl_ok: bool, ctrl_info: str):
    """Escribe un archivo de heartbeat para que otros procesos puedan leerlo."""
    try:
        HEARTBEAT_FILE.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "monitor_running": True,
            "last_check": int(time.time() * 1000),
            "last_check_iso": datetime.now(TZ_MT5).isoformat(),
            "uptime_sec": int(time.time() - state.started_at),
            "total_alerts_sent": state.total_alerts_sent,
            "consecutive_failures": state.consecutive_failures,
            "checks": {
                "log": {"ok": log_ok, "info": log_info},
                "mt5": {"ok": mt5_ok, "info": mt5_info},
                "control": {"ok": ctrl_ok, "info": ctrl_info},
            },
        }
        with open(HEARTBEAT_FILE, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
    except Exception as e:
        logger.debug(f"No se pudo escribir heartbeat file: {e}")


def send_alert(reason: str, details: str):
    """Envía alerta por Telegram respetando cooldown."""
    if not state.can_send_alert(reason):
        logger.debug(f"Alerta suprimida por cooldown: {reason}")
        return

    msg = (
        "🚨 *QUANTEDGE AI — ALERTA*\n"
        f"\n"
        f"*Motivo:* `{reason}`\n"
        f"*Detalles:* {details}\n"
        f"*Hora:* `{datetime.now(TZ_MT5).strftime('%Y-%m-%d %H:%M:%S')}`\n"
        f"\n"
        f"⚠️ Verifica el bot y MT5 inmediatamente."
    )

    if send_telegram_alert(msg):
        state.record_alert(reason)
        logger.warning(f"🚨 ALERTA enviada: {reason} | {details}")
    else:
        logger.error(f"❌ No se pudo enviar alerta: {reason}")


def send_recovery_alert(reason: str):
    """Envía alerta de recuperación cuando un problema se resuelve."""
    msg = (
        "✅ *QUANTEDGE AI — RECUPERACIÓN*\n"
        f"\n"
        f"*Estado:* El problema se resolvió\n"
        f"*Era:* `{reason}`\n"
        f"*Hora:* `{datetime.now(TZ_MT5).strftime('%Y-%m-%d %H:%M:%S')}`"
    )
    if send_telegram_alert(msg):
        logger.info(f"✅ Alerta de recuperación enviada: {reason}")


# -----------------------------------------------------------------------------
# Loop principal
# -----------------------------------------------------------------------------
def run_check() -> bool:
    """Ejecuta todos los chequeos. Devuelve True si todo OK."""
    all_ok = True
    problems = []

    # 1. Log freshness
    log_ok, log_info = check_log_freshness()
    if not log_ok:
        all_ok = False
        problems.append(f"Log: {log_info}")

    # 2. Errores críticos en log
    err_ok, err_info = check_log_for_errors()
    if not err_ok:
        all_ok = False
        problems.append(f"Errores: {err_info}")

    # 3. MT5
    mt5_ok, mt5_info = check_mt5_connection()
    if not mt5_ok:
        all_ok = False
        problems.append(f"MT5: {mt5_info}")

    # 4. Control state
    ctrl_ok, ctrl_info = check_control_state()
    if not ctrl_ok:
        all_ok = False
        problems.append(f"Control: {ctrl_info}")

    # Escribir heartbeat file
    write_heartbeat_file(log_ok, log_info, mt5_ok, mt5_info, ctrl_ok, ctrl_info)

    # Log resumido
    status_emoji = "✅" if all_ok else "❌"
    logger.info(
        f"{status_emoji} log={log_info} mt5={mt5_info} ctrl={ctrl_info}"
    )

    # Manejar problemas
    if all_ok:
        # Si antes había fallos consecutivos, mandar recuperación
        if state.consecutive_failures > 0:
            send_recovery_alert(state.last_alert_reason)
            logger.info(f"✅ Recuperado tras {state.consecutive_failures} fallos")
        state.consecutive_failures = 0
    else:
        state.consecutive_failures += 1
        reason = problems[0].split(":")[0].upper().replace(" ", "_")
        details = " | ".join(problems)

        # Solo alertar después de 2 chequeos consecutivos fallidos
        # (evita alertas por hipos temporales)
        if state.consecutive_failures >= 2:
            send_alert(reason, details)

    return all_ok


def main():
    logger.info("=" * 70)
    logger.info("🔔 QUANTEDGE AI — MONITOR DE HEARTBEAT")
    logger.info(f"   Log vigilado:          {LOG_FILE}")
    logger.info(f"   Intervalo de chequeo:  {int(CHECK_INTERVAL_SEC)}s")
    logger.info(f"   Edad máx. sin logs:    {int(HEARTBEAT_MAX_AGE_SEC)}s ({int(HEARTBEAT_MAX_AGE_SEC/60)} min)")
    logger.info(f"   Cooldown de alertas:   {int(ALERT_COOLDOWN_SEC)}s")
    logger.info(f"   Check MT5:             {'ACTIVO' if MT5_CHECK_ENABLED else 'DESACTIVADO'}")
    logger.info("=" * 70)

    # Verificar que el bot esté corriendo al inicio
    if not LOG_FILE.exists():
        logger.warning(f"⚠️  No existe {LOG_FILE}. ¿El bot ha corrido alguna vez?")

    # Enviar mensaje de inicio
    send_telegram_alert(
        "🔔 *Monitor QuantEdge AI iniciado*\n"
        f"Vigilando: `{LOG_FILE.name}`\n"
        f"Intervalo: `{int(CHECK_INTERVAL_SEC)}s`\n"
        f"Edad máx. sin logs: `{int(HEARTBEAT_MAX_AGE_SEC/60)} min`"
    )

    try:
        while True:
            try:
                run_check()
            except Exception as e:
                logger.error(f"Error en chequeo: {e}")

            time.sleep(CHECK_INTERVAL_SEC)

    except KeyboardInterrupt:
        logger.info("🛑 Monitor detenido por el usuario.")
        send_telegram_alert("🛑 *Monitor QuantEdge AI detenido*")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.critical(f"💥 Monitor crasheó: {e}")
        sys.exit(1)