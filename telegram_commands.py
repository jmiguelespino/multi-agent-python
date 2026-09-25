"""
=============================================================================
QUANTEDGE AI — CONTROL REMOTO POR TELEGRAM
=============================================================================
Comandos: /status /pause /resume /positions /close_all /config /help

Ejecución:
    python telegram_commands.py
=============================================================================
"""

import os
import sys
import json
import time
import logging
import urllib.request
import urllib.parse
from pathlib import Path
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv

load_dotenv()

TZ_MT5 = timezone(timedelta(hours=3))


class MT5TimeFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        dt = datetime.fromtimestamp(record.created, tz=TZ_MT5)
        return dt.strftime(datefmt) if datefmt else dt.isoformat()


handler = logging.StreamHandler()
handler.setFormatter(MT5TimeFormatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
logger = logging.getLogger("TelegramCommands")
logger.addHandler(handler)
logger.setLevel(logging.INFO)

BASE_DIR = Path(__file__).resolve().parent
CONTROL_STATE_FILE = BASE_DIR / "control_state.json"
CONFIG_OPTIMIZED_FILE = BASE_DIR / "config_optimized.json"
AUDIT_LOG_FILE = BASE_DIR / "logs" / "trade_audit_history.jsonl"

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "").strip()
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "").strip()
POLL_TIMEOUT = 30

if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
    print("❌ Faltan TELEGRAM_TOKEN o TELEGRAM_CHAT_ID en el .env")
    sys.exit(1)


DEFAULT_STATE = {
    "paused": False,
    "paused_since": None,
    "paused_by": None,
    "last_command": None,
    "last_command_time": None,
    "close_all_requested": False,
    "close_all_requested_at": None,
}


def load_control_state() -> dict:
    if not CONTROL_STATE_FILE.exists():
        return dict(DEFAULT_STATE)
    try:
        with open(CONTROL_STATE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        for k, v in DEFAULT_STATE.items():
            data.setdefault(k, v)
        return data
    except Exception:
        return dict(DEFAULT_STATE)


def save_control_state(state: dict):
    try:
        with open(CONTROL_STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2)
    except Exception as e:
        logger.error(f"Error guardando control_state.json: {e}")


def telegram_api(method: str, params: dict) -> dict:
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/{method}"
    data = urllib.parse.urlencode(params).encode("utf-8")
    req = urllib.request.Request(url, data=data)
    try:
        with urllib.request.urlopen(req, timeout=POLL_TIMEOUT + 5) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        logger.error(f"Error llamando a Telegram API ({method}): {e}")
        return {"ok": False}


def send_message(text: str, parse_mode: str = "Markdown") -> bool:
    res = telegram_api("sendMessage", {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": parse_mode,
    })
    return res.get("ok", False)


def get_updates(offset: int = 0) -> list:
    res = telegram_api("getUpdates", {
        "offset": offset,
        "timeout": POLL_TIMEOUT,
        "allowed_updates": json.dumps(["message"]),
    })
    if not res.get("ok"):
        return []
    return res.get("result", [])


def read_config_optimized() -> dict:
    if CONFIG_OPTIMIZED_FILE.exists():
        try:
            with open(CONFIG_OPTIMIZED_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def count_recent_closures(hours: int = 24) -> dict:
    if not AUDIT_LOG_FILE.exists():
        return {"total": 0, "pnl": 0.0}
    cutoff_ms = int((time.time() - hours * 3600) * 1000)
    total = 0
    pnl = 0.0
    try:
        with open(AUDIT_LOG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    rec = json.loads(line.strip())
                except Exception:
                    continue
                if rec.get("category") == "CLOSURE" and rec.get("timestamp", 0) >= cutoff_ms:
                    total += 1
                    pnl += float(rec.get("pnl_usd") or 0.0)
    except Exception:
        pass
    return {"total": total, "pnl": round(pnl, 2)}


def try_get_mt5_status() -> dict:
    try:
        import MetaTrader5 as mt5
        if not mt5.initialize():
            return {}
        acc = mt5.account_info()
        positions = mt5.positions_get() or []
        if acc is None:
            mt5.shutdown()
            return {}
        return {
            "login": acc.login,
            "server": acc.server,
            "balance": round(acc.balance, 2),
            "equity": round(acc.equity, 2),
            "margin_free": round(acc.margin_free, 2),
            "positions": [
                {
                    "ticket": p.ticket,
                    "symbol": p.symbol,
                    "type": "BUY" if p.type == mt5.ORDER_TYPE_BUY else "SELL",
                    "volume": p.volume,
                    "price_open": p.price_open,
                    "price_current": p.price_current,
                    "sl": p.sl,
                    "tp": p.tp,
                    "profit": round(p.profit, 2),
                }
                for p in positions
            ],
        }
    except Exception as e:
        logger.debug(f"MT5 no disponible: {e}")
        return {}


def cmd_status() -> str:
    state = load_control_state()
    config = read_config_optimized()
    daily = count_recent_closures(24)
    mt5_status = try_get_mt5_status()

    paused_line = "⏸️ *PAUSADO*" if state["paused"] else "▶️ *ACTIVO*"

    lines = [
        "📊 *QuantEdge AI — Estado*",
        "",
        f"*Estado:* {paused_line}",
    ]
    if state["paused"] and state.get("paused_since"):
        lines.append(f"_Pausado desde: {state['paused_since']}_")

    lines.append("")

    if mt5_status:
        lines.append("*Cuenta MT5:*")
        lines.append(f"  • Login: `#{mt5_status['login']}`")
        lines.append(f"  • Servidor: `{mt5_status['server']}`")
        lines.append(f"  • Balance: `${mt5_status['balance']:,.2f}`")
        lines.append(f"  • Equidad: `${mt5_status['equity']:,.2f}`")
        lines.append(f"  • Margen libre: `${mt5_status['margin_free']:,.2f}`")
        lines.append(f"  • Posiciones abiertas: `{len(mt5_status['positions'])}`")
    else:
        lines.append("*Cuenta MT5:* _no disponible (terminal cerrado?)_")

    lines.append("")
    lines.append("*Últimas 24h:*")
    lines.append(f"  • Cierres: `{daily['total']}`")
    pnl_emoji = "🟢" if daily["pnl"] >= 0 else "🔴"
    lines.append(f"  • PnL: {pnl_emoji} `${daily['pnl']:,.2f}`")

    if config:
        lines.append("")
        lines.append("*Configuración del Learner:*")
        lines.append(f"  • Confianza mínima: `{config.get('min_confidence_threshold', 'N/D')}%`")
        lines.append(f"  • SL ATR: `{config.get('atr_stop_multiplier', 'N/D')}×`")
        lines.append(f"  • TP ATR: `{config.get('atr_profit_multiplier', 'N/D')}×`")
        lines.append(f"  • Trades analizados: `{config.get('total_trades_analyzed', 0)}`")

    return "\n".join(lines)


def cmd_positions() -> str:
    mt5_status = try_get_mt5_status()
    if not mt5_status:
        return "❌ *MT5 no disponible.* Abre el terminal MetaTrader 5."

    positions = mt5_status["positions"]
    if not positions:
        return "📭 *No hay posiciones abiertas.*"

    lines = [f"📈 *Posiciones abiertas ({len(positions)}):*", ""]
    total_pnl = 0.0
    for p in positions:
        pnl = p["profit"]
        total_pnl += pnl
        emoji = "🟢" if pnl >= 0 else "🔴"
        lines.append(
            f"{emoji} `#{p['ticket']}` *{p['symbol']}* {p['type']} {p['volume']}\n"
            f"   Entrada: `${p['price_open']}` → Actual: `${p['price_current']}`\n"
            f"   SL: `${p['sl']}` | TP: `${p['tp']}` | PnL: `${pnl:,.2f}`"
        )
    lines.append("")
    lines.append(f"*PnL total flotante:* `${total_pnl:,.2f}`")
    return "\n".join(lines)


def cmd_pause() -> str:
    state = load_control_state()
    if state["paused"]:
        return "⚠️ El bot *ya estaba pausado*."
    state["paused"] = True
    state["paused_since"] = datetime.now(TZ_MT5).strftime("%Y-%m-%d %H:%M:%S")
    state["paused_by"] = "telegram"
    state["last_command"] = "pause"
    state["last_command_time"] = int(time.time() * 1000)
    save_control_state(state)
    return "⏸️ *Bot pausado.* No se ejecutarán nuevas órdenes hasta `/resume`."


def cmd_resume() -> str:
    state = load_control_state()
    if not state["paused"]:
        return "⚠️ El bot *ya estaba activo*."
    state["paused"] = False
    state["paused_since"] = None
    state["paused_by"] = None
    state["last_command"] = "resume"
    state["last_command_time"] = int(time.time() * 1000)
    save_control_state(state)
    return "▶️ *Bot reanudado.*"


def cmd_close_all() -> str:
    state = load_control_state()
    state["close_all_requested"] = True
    state["close_all_requested_at"] = int(time.time() * 1000)
    state["last_command"] = "close_all"
    state["last_command_time"] = int(time.time() * 1000)
    save_control_state(state)
    return "🚨 *Solicitud de CIERRE TOTAL registrada.*"


def cmd_config() -> str:
    config = read_config_optimized()
    if not config:
        return "📭 *No hay `config_optimized.json` todavía.*"
    lines = ["⚙️ *Configuración actual:*", ""]
    for k, v in config.items():
        lines.append(f"  • `{k}`: `{v}`")
    return "\n".join(lines)


def cmd_help() -> str:
    return (
        "🤖 *QuantEdge AI — Comandos*\n"
        "\n"
        "`/status`      — Estado del bot\n"
        "`/pause`       — Pausar nuevas órdenes\n"
        "`/resume`      — Reanudar\n"
        "`/positions`   — Posiciones abiertas\n"
        "`/close_all`   — Cerrar TODAS\n"
        "`/config`      — Configuración del learner\n"
        "`/help`        — Ayuda\n"
    )


COMMANDS = {
    "/status": cmd_status,
    "/pause": cmd_pause,
    "/resume": cmd_resume,
    "/positions": cmd_positions,
    "/close_all": cmd_close_all,
    "/config": cmd_config,
    "/help": cmd_help,
    "/start": cmd_help,
}


def handle_command(text: str, chat_id: str) -> str:
    if str(chat_id) != str(TELEGRAM_CHAT_ID):
        logger.warning(f"Comando ignorado de chat no autorizado: {chat_id}")
        return "⛔ No autorizado."

    cmd = text.strip().split()[0].lower() if text.strip() else ""
    handler = COMMANDS.get(cmd)
    if handler:
        try:
            return handler()
        except Exception as e:
            logger.error(f"Error ejecutando {cmd}: {e}")
            return f"❌ Error ejecutando `{cmd}`: `{e}`"
    return f"❓ Comando desconocido: `{cmd}`\nUsa `/help`."


def main():
    logger.info("=" * 60)
    logger.info("🤖 QuantEdge AI — Telegram Control Bot")
    logger.info(f"   Chat autorizado: {TELEGRAM_CHAT_ID}")
    logger.info("=" * 60)

    me = telegram_api("getMe", {})
    if not me.get("ok"):
        logger.error("❌ No se pudo conectar con Telegram. Revisa TELEGRAM_TOKEN.")
        sys.exit(1)
    logger.info(f"✅ Conectado como @{me['result'].get('username', '?')}")

    send_message("🤖 *QuantEdge AI Control* iniciado.\nUsa `/help` para comandos.")

    offset = 0
    while True:
        try:
            updates = get_updates(offset)
            for upd in updates:
                offset = upd["update_id"] + 1
                msg = upd.get("message")
                if not msg:
                    continue
                text = msg.get("text", "")
                chat_id = msg.get("chat", {}).get("id")
                user = msg.get("from", {}).get("username", "?")
                if not text:
                    continue
                logger.info(f"📨 Comando de @{user}: {text}")
                response = handle_command(text, chat_id)
                send_message(response)
        except KeyboardInterrupt:
            logger.info("🛑 Detenido por el usuario.")
            break
        except Exception as e:
            logger.error(f"Error en loop: {e}")
            time.sleep(3)


if __name__ == "__main__":
    main()