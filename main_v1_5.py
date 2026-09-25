"""
=============================================================================
QUANTEDGE AI — MOTOR AUTÓNOMO DE TRADING INSTITUCIONAL MULTI-ACTIVO (UTC+3)
=============================================================================
🔧 v1.5.0:
  • Reporte diario con DESGLOSE POR ACTIVO (PnL, win rate, PF).
  • Recomendaciones automáticas por activo.
  • Cooldown de 5 min tras "Invalid stops".
  • Cooldown de 30 min tras "Market closed".
  • Control remoto vía control_state.json.
  • Sin doble logging.
=============================================================================
"""

import os
import sys
import json
import time
import asyncio
import logging
from pathlib import Path
from datetime import datetime, timezone, timedelta
from typing import Dict, List
from collections import defaultdict
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

env_file = BASE_DIR.parent / '.env'
if not env_file.exists():
    env_file = BASE_DIR / '.env'
load_dotenv(dotenv_path=env_file)

# 🔧 Eliminar handlers preexistentes del root logger
for h in logging.root.handlers[:]:
    logging.root.removeHandler(h)

import MetaTrader5 as mt5
from signal_agent import StrategySignalAgent
from risk_guardian import InstitutionalRiskGuardian
from execution_agent import ExecutionOMSAgent
from feature_agent import IngestionFeatureAgent
from feedback_learner import ContinuousLearningAgent
from data_streamer import Tick
from telegram_notifier import send_telegram_alert
from audit_logger import log_order_filled, log_rejection

# =============================================================================
# CONSTANTES Y RUTAS
# =============================================================================
CONTROL_STATE_FILE = BASE_DIR / "control_state.json"
AUDIT_LOG_FILE = BASE_DIR / "logs" / "trade_audit_history.jsonl"
CONFIG_OPTIMIZED_FILE = BASE_DIR / "config_optimized.json"
DAILY_REPORT_STATE_FILE = BASE_DIR / "logs" / "daily_report_state.json"

DEFAULT_CONTROL_STATE = {
    "paused": False,
    "close_all_requested": False,
}

DAILY_REPORT_HOUR = int(os.getenv("DAILY_REPORT_HOUR", "23"))
DAILY_REPORT_MINUTE = int(os.getenv("DAILY_REPORT_MINUTE", "59"))


# =============================================================================
# CONTROL STATE
# =============================================================================
def read_control_state() -> dict:
    if not CONTROL_STATE_FILE.exists():
        return dict(DEFAULT_CONTROL_STATE)
    try:
        with open(CONTROL_STATE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        for k, v in DEFAULT_CONTROL_STATE.items():
            data.setdefault(k, v)
        return data
    except Exception:
        return dict(DEFAULT_CONTROL_STATE)


def reset_close_all_flag():
    try:
        state = read_control_state()
        state["close_all_requested"] = False
        with open(CONTROL_STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2)
    except Exception:
        pass


# =============================================================================
# DAILY REPORT STATE
# =============================================================================
def read_daily_report_state() -> dict:
    if not DAILY_REPORT_STATE_FILE.exists():
        return {"last_report_date": None, "last_report_timestamp": None}
    try:
        with open(DAILY_REPORT_STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"last_report_date": None, "last_report_timestamp": None}


def write_daily_report_state(date_str: str):
    try:
        DAILY_REPORT_STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "last_report_date": date_str,
            "last_report_timestamp": int(time.time() * 1000),
        }
        with open(DAILY_REPORT_STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
    except Exception as e:
        logger.error(f"Error guardando daily_report_state: {e}")


# =============================================================================
# REPORTE DIARIO — Funciones auxiliares de carga
# =============================================================================
def _load_closures_since(cutoff_ms: int) -> List[dict]:
    """Carga cierres desde un timestamp en ms."""
    if not AUDIT_LOG_FILE.exists():
        return []
    closures = []
    try:
        with open(AUDIT_LOG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if rec.get("category") != "CLOSURE":
                    continue
                if rec.get("pnl_usd") is None:
                    continue
                if rec.get("timestamp", 0) < cutoff_ms:
                    continue
                closures.append(rec)
    except Exception as e:
        logger.error(f"Error cargando cierres para reporte: {e}")
    closures.sort(key=lambda r: r.get("timestamp", 0))
    return closures


def _load_all_closures() -> List[dict]:
    """Carga TODOS los cierres (para contar progreso hacia 30)."""
    if not AUDIT_LOG_FILE.exists():
        return []
    closures = []
    try:
        with open(AUDIT_LOG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if rec.get("category") == "CLOSURE" and rec.get("pnl_usd") is not None:
                    closures.append(rec)
    except Exception:
        pass
    return closures


def _count_events_since(cutoff_ms: int) -> dict:
    """Cuenta eventos ORDER_FILLED, OPEN_POSITION_DETECTED y rechazos."""
    result = {"orders_filled": 0, "positions_opened": 0, "rejections": 0}
    if not AUDIT_LOG_FILE.exists():
        return result
    try:
        with open(AUDIT_LOG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if rec.get("timestamp", 0) < cutoff_ms:
                    continue
                event = rec.get("event_type", "")
                cat = rec.get("category", "")
                if event == "ORDER_FILLED":
                    result["orders_filled"] += 1
                elif event == "OPEN_POSITION_DETECTED":
                    result["positions_opened"] += 1
                elif cat == "REJECTION":
                    result["rejections"] += 1
    except Exception:
        pass
    return result


def _get_mt5_snapshot() -> dict:
    """Estado actual de MT5."""
    try:
        acc = mt5.account_info()
        positions = mt5.positions_get() or []
        if acc is None:
            return {}
        return {
            "balance": round(acc.balance, 2),
            "equity": round(acc.equity, 2),
            "margin_free": round(acc.margin_free, 2),
            "positions_count": len(positions),
            "floating_pnl": round(sum(p.profit for p in positions), 2),
        }
    except Exception:
        return {}


def read_optimized_config() -> dict:
    if CONFIG_OPTIMIZED_FILE.exists():
        try:
            with open(CONFIG_OPTIMIZED_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def _format_pnl(value: float) -> str:
    emoji = "🟢" if value > 0 else ("🔴" if value < 0 else "⚪")
    return f"{emoji} `${value:+,.2f}`"


# =============================================================================
# REPORTE DIARIO — Generación de recomendaciones
# =============================================================================
def _generate_recommendations(by_symbol_data: dict) -> list:
    """Genera recomendaciones automáticas según performance de cada activo."""
    recs = []
    MIN_TRADES_TO_EVALUATE = int(os.getenv("ANALYSIS_MIN_TRADES", "5"))

    for sym, d in by_symbol_data.items():
        if d["count"] < MIN_TRADES_TO_EVALUATE:
            continue

        wr = (d["wins"] / d["count"]) * 100 if d["count"] > 0 else 0
        sym_pf = (d["gross_profit"] / d["gross_loss"]) if d["gross_loss"] > 0 else 999.0

        if sym_pf < 0.7:
            recs.append(f"🔴 *{sym}*: PF={sym_pf:.2f} muy bajo. Considerar desactivar.")
        elif sym_pf < 1.0:
            recs.append(f"🟡 *{sym}*: PF={sym_pf:.2f}. Revisar parámetros.")
        elif sym_pf > 2.0:
            recs.append(f"🟢 *{sym}*: PF={sym_pf:.2f} excelente. Mantener configuración.")

        if wr < 40 and d["count"] >= MIN_TRADES_TO_EVALUATE:
            recs.append(f"⚠️ *{sym}*: win rate {wr:.0f}% bajo. Ampliar SL o aumentar confianza mínima.")

    return recs[:5]


# =============================================================================
# REPORTE DIARIO — Construcción del mensaje
# =============================================================================
def build_daily_report(days: int = 1) -> str:
    """Construye el mensaje del reporte diario con desglose por activo."""
    now_ms = int(time.time() * 1000)
    cutoff_ms = now_ms - (days * 86400 * 1000)

    closures = _load_closures_since(cutoff_ms)
    all_closures = _load_all_closures()
    orders = _count_events_since(cutoff_ms)
    mt5_snap = _get_mt5_snapshot()
    ctrl = read_control_state()
    config = read_optimized_config()

    # ─── Estadísticas globales ───────────────────────────────────────
    total = len(closures)
    if total > 0:
        pnls = [float(r.get("pnl_usd", 0)) for r in closures]
        wins = [p for p in pnls if p > 0]
        losses = [p for p in pnls if p <= 0]
        total_pnl = sum(pnls)
        win_rate = (len(wins) / total) * 100
        avg_win = sum(wins) / len(wins) if wins else 0
        avg_loss = abs(sum(losses) / len(losses)) if losses else 0
        gross_profit = sum(wins)
        gross_loss = abs(sum(losses))
        pf = (gross_profit / gross_loss) if gross_loss > 0 else 999.0
        best = max(pnls)
        worst = min(pnls)
    else:
        total_pnl = win_rate = avg_win = avg_loss = pf = best = worst = 0

    # ─── Desglose por activo ─────────────────────────────────────────
    by_symbol_data = defaultdict(lambda: {
        "count": 0, "wins": 0, "losses": 0,
        "pnl": 0.0, "gross_profit": 0.0, "gross_loss": 0.0,
    })
    for r in closures:
        sym = str(r.get("symbol", "UNKNOWN")).upper()
        pnl = float(r.get("pnl_usd", 0))
        by_symbol_data[sym]["count"] += 1
        by_symbol_data[sym]["pnl"] += pnl
        if pnl > 0:
            by_symbol_data[sym]["wins"] += 1
            by_symbol_data[sym]["gross_profit"] += pnl
        else:
            by_symbol_data[sym]["losses"] += 1
            by_symbol_data[sym]["gross_loss"] += abs(pnl)

    # ─── Encabezado ──────────────────────────────────────────────────
    day_label = "HOY" if days == 1 else f"ÚLTIMOS {days} DÍAS"
    date_str = datetime.now(TZ_MT5).strftime("%Y-%m-%d")

    lines = [
        "📊 *QUANTEDGE AI — REPORTE DIARIO*",
        f"_{date_str} ({day_label})_",
        "",
    ]

    paused = ctrl.get("paused", False)
    bot_status = "⏸️ PAUSADO" if paused else "▶️ ACTIVO"
    lines.append(f"*Estado del bot:* {bot_status}")

    # ─── Estado MT5 ──────────────────────────────────────────────────
    if mt5_snap:
        lines.append(f"*MT5:*")
        lines.append(f"  • Balance: `${mt5_snap['balance']:,.2f}`")
        lines.append(f"  • Equidad: `${mt5_snap['equity']:,.2f}`")
        lines.append(f"  • Posiciones abiertas: `{mt5_snap['positions_count']}`")
        if mt5_snap['positions_count'] > 0:
            lines.append(f"  • PnL flotante: {_format_pnl(mt5_snap['floating_pnl'])}")

    # ─── Actividad ───────────────────────────────────────────────────
    lines.append("")
    lines.append(f"*Actividad:*")
    lines.append(f"  • Órdenes ejecutadas: `{orders['orders_filled']}`")
    lines.append(f"  • Posiciones cerradas: `{total}`")
    lines.append(f"  • Rechazos: `{orders['rejections']}`")

    # ─── Resultados globales ─────────────────────────────────────────
    lines.append("")
    if total > 0:
        lines.append(f"*Resultados globales:*")
        lines.append(f"  • PnL: {_format_pnl(total_pnl)}")
        lines.append(f"  • Wins / Losses: `{len(wins)}` / `{len(losses)}`")
        lines.append(f"  • Win rate: `{win_rate:.1f}%`")
        lines.append(f"  • Profit Factor: `{pf:.2f}`")
        lines.append(f"  • Mejor / Peor: `+${best:,.2f}` / `${worst:,.2f}`")
    else:
        lines.append(f"*Resultados:* _sin trades cerrados en el período_")

    # ─── Desglose por activo ─────────────────────────────────────────
    if by_symbol_data:
        lines.append("")
        lines.append(f"*📈 Desglose por activo:*")
        lines.append("")

        sorted_symbols = sorted(
            by_symbol_data.items(),
            key=lambda x: x[1]["pnl"],
            reverse=True
        )

        for sym, d in sorted_symbols:
            if d["count"] == 0:
                continue

            wr = (d["wins"] / d["count"]) * 100 if d["count"] > 0 else 0
            sym_pf = (d["gross_profit"] / d["gross_loss"]) if d["gross_loss"] > 0 else 999.0

            if d["pnl"] > 0:
                emoji = "🟢"
            elif d["pnl"] < 0:
                emoji = "🔴"
            else:
                emoji = "⚪"

            warning = ""
            if d["count"] >= 5 and d["pnl"] < -20:
                warning = " ⚠️"
            elif d["count"] >= 5 and sym_pf < 0.8:
                warning = " ⚠️"

            lines.append(
                f"{emoji} *{sym}*{warning}\n"
                f"    `{d['count']}` trades | WR `{wr:.0f}%` | PF `{sym_pf:.2f}` | PnL {_format_pnl(d['pnl'])}"
            )

    # ─── Agente 5 (Learner) ──────────────────────────────────────────
    lines.append("")
    lines.append(f"*🧠 Agente 5 (Learner):*")
    lines.append(f"  • Cierres totales: `{len(all_closures)}` / `30`")
    if config:
        lines.append(f"  • Confianza: `{config.get('min_confidence_threshold', 'N/D')}%`")
        lines.append(f"  • SL ATR: `{config.get('atr_stop_multiplier', 'N/D')}×`")
        lines.append(f"  • TP ATR: `{config.get('atr_profit_multiplier', 'N/D')}×`")

    # ─── Recomendaciones automáticas ─────────────────────────────────
    if total >= 5:
        recs = _generate_recommendations(by_symbol_data)
        if recs:
            lines.append("")
            lines.append(f"*💡 Recomendaciones:*")
            for rec in recs:
                lines.append(f"  {rec}")

    lines.append("")
    lines.append(f"_Generado a las {datetime.now(TZ_MT5).strftime('%H:%M:%S')}_")

    return "\n".join(lines)


# =============================================================================
# REPORTE DIARIO — Disparo automático
# =============================================================================
def should_send_daily_report() -> bool:
    """Determina si es momento de enviar el reporte."""
    now_mt5 = datetime.now(TZ_MT5)
    today_str = now_mt5.strftime("%Y-%m-%d")

    report_time_reached = (
        now_mt5.hour > DAILY_REPORT_HOUR or
        (now_mt5.hour == DAILY_REPORT_HOUR and now_mt5.minute >= DAILY_REPORT_MINUTE)
    )
    if not report_time_reached:
        return False

    state = read_daily_report_state()
    if state.get("last_report_date") == today_str:
        return False

    return True


async def send_daily_report_if_needed():
    """Envía el reporte diario si es momento y no se ha enviado aún."""
    if not should_send_daily_report():
        return

    now_mt5 = datetime.now(TZ_MT5)
    today_str = now_mt5.strftime("%Y-%m-%d")

    logger.info("=" * 70)
    logger.info(f"📊 [DAILY REPORT] Disparando reporte diario para {today_str}")
    logger.info("=" * 70)

    try:
        report = build_daily_report(days=1)
        sent = send_telegram_alert(report)

        if sent:
            write_daily_report_state(today_str)
            logger.info(f"✅ [DAILY REPORT] Enviado correctamente para {today_str}")
        else:
            logger.warning("⚠️ [DAILY REPORT] No se pudo enviar. Se reintentará en el próximo ciclo.")
    except Exception as e:
        logger.error(f"❌ [DAILY REPORT] Error generando/enviando reporte: {e}")


# =============================================================================
# CLOSE ALL
# =============================================================================
def close_all_positions() -> int:
    closed = 0
    try:
        positions = mt5.positions_get()
        if not positions:
            return 0
        for p in positions:
            tick = mt5.symbol_info_tick(p.symbol)
            if not tick:
                continue
            close_type = mt5.ORDER_TYPE_SELL if p.type == mt5.ORDER_TYPE_BUY else mt5.ORDER_TYPE_BUY
            price = tick.bid if p.type == mt5.ORDER_TYPE_BUY else tick.ask
            req = {
                "action": mt5.TRADE_ACTION_DEAL,
                "position": p.ticket,
                "symbol": p.symbol,
                "volume": p.volume,
                "type": close_type,
                "price": price,
                "deviation": 30,
                "magic": int(os.getenv("MAGIC_NUMBER", "992026")),
                "comment": "QuantEdge-CloseAll-TG",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_IOC,
            }
            res = mt5.order_send(req)
            if res and res.retcode == mt5.TRADE_RETCODE_DONE:
                closed += 1
                logger.info(f"🔴 Cerrada posición #{p.ticket} {p.symbol}")
            else:
                logger.error(f"Fallo cerrando #{p.ticket}: {res.comment if res else 'sin respuesta'}")
    except Exception as e:
        logger.error(f"Error en close_all_positions: {e}")
    return closed


# =============================================================================
# CONFIGURACIÓN / LOGGING
# =============================================================================
TZ_MT5 = timezone(timedelta(hours=3))


class MT5TimeFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        dt = datetime.fromtimestamp(record.created, tz=TZ_MT5)
        return dt.strftime(datefmt) if datefmt else dt.isoformat()


handler = logging.StreamHandler()
handler.setFormatter(MT5TimeFormatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))

logger = logging.getLogger("QuantEdgeSniper")
logger.addHandler(handler)
logger.setLevel(logging.INFO)
logger.propagate = False

MT5_ACCOUNT = int(os.getenv("MT5_ACCOUNT", "52974519"))
MT5_PASSWORD = os.getenv("MT5_PASSWORD", "")
MT5_SERVER = os.getenv("MT5_SERVER", "ICMarketsSC-Demo")

DEFAULT_SYMBOLS = "XAUUSD,WTI,BRENT,EURUSD,GBPUSD,BTCUSD,ETHUSD,SOLUSD"
TRADING_SYMBOLS_RAW = os.getenv("TRADING_SYMBOLS", DEFAULT_SYMBOLS)
SYMBOLS_LIST = [s.strip() for s in TRADING_SYMBOLS_RAW.split(",") if s.strip()]

DECISION_THROTTLE_SECONDS = float(os.getenv("DECISION_THROTTLE_SECONDS", "0.5"))
HEARTBEAT_INTERVAL_SECONDS = float(os.getenv("HEARTBEAT_INTERVAL_SECONDS", "900.0"))
FAILED_ORDER_COOLDOWN_SEC = float(os.getenv("FAILED_ORDER_COOLDOWN_SEC", "300.0"))
MARKET_CLOSED_COOLDOWN_SEC = float(os.getenv("MARKET_CLOSED_COOLDOWN_SEC", "1800.0"))


def get_mt5_timestamp_ms() -> int:
    return int(datetime.now(TZ_MT5).timestamp() * 1000)


def connect_mt5() -> bool:
    if not mt5.initialize():
        logger.error(f"Error inicializando MT5: {mt5.last_error()}")
        return False

    if MT5_PASSWORD:
        login_res = mt5.login(login=MT5_ACCOUNT, password=MT5_PASSWORD, server=MT5_SERVER)
    else:
        login_res = mt5.login(login=MT5_ACCOUNT, server=MT5_SERVER)

    if not login_res:
        logger.warning(f"Aviso de login en MT5: {mt5.last_error()}")

    info = mt5.account_info()
    if info is None:
        logger.error("No se pudo leer la información de cuenta en MT5.")
        return False

    logger.info("=" * 70)
    logger.info("✅ CONECTADO DIRECTAMENTE A METATRADER 5 (IC MARKETS)")
    logger.info(f"  • Cuenta:       #{info.login} ({info.server})")
    logger.info(f"  • Capital Base: ${info.balance:,.2f} {info.currency}")
    logger.info(f"  • Equidad:      ${info.equity:,.2f} {info.currency}")
    logger.info("=" * 70)
    return True


def resolve_mt5_symbol(symbol: str) -> str:
    aliases = [symbol, f"{symbol}.raw", f"{symbol}m", f"{symbol}_raw"]
    s_upper = symbol.upper()

    if s_upper in ["XAUUSD", "GOLD"]:
        aliases.extend(["GOLD", "XAUUSD", "XAUUSD.raw", "GOLD.raw"])
    elif s_upper in ["XTIUSD", "WTI", "USOIL"]:
        aliases.extend(["XTIUSD", "WTI", "USOIL", "XTIUSD.raw", "WTI.raw"])
    elif s_upper in ["XBRUSD", "BRENT", "UKOIL"]:
        aliases.extend(["XBRUSD", "BRENT", "UKOIL", "XBRUSD.raw", "BRENT.raw"])
    elif "BTC" in s_upper:
        aliases.extend(["BTCUSD", "BTCUSDT", "BTCUSD.raw", "BTCUSDT.raw"])
    elif "ETH" in s_upper:
        aliases.extend(["ETHUSD", "ETHUSDT", "ETHUSD.raw", "ETHUSDT.raw"])
    elif "SOL" in s_upper:
        aliases.extend(["SOLUSD", "SOLUSDT", "SOLUSD.raw", "SOLUSDT.raw"])

    for a in aliases:
        if mt5.symbol_info(a):
            mt5.symbol_select(a, True)
            return a
    return symbol


async def send_order_async(req: dict):
    return await asyncio.to_thread(mt5.order_send, req)


def normalize_side(side) -> str:
    if hasattr(side, "value"):
        return side.value
    return str(side)


# =============================================================================
# MAIN
# =============================================================================
async def main():
    logger.info("Iniciando pipeline Sniper Cuantitativo Multi-Activo...")

    has_mt5 = connect_mt5()

    # 🔧 Capital se lee EN VIVO desde MT5
    capital_base = None
    if has_mt5:
        acc = mt5.account_info()
        if acc and acc.balance > 0:
            capital_base = acc.balance
            logger.info(f"💰 Capital Base leído desde MT5: ${capital_base:,.2f} (cuenta #{acc.login})")
        else:
            logger.warning("⚠️  MT5 no devolvió información de cuenta. Usando fallback.")
    else:
        logger.warning("⚠️  MT5 no disponible. Usando fallback.")

    if capital_base is None:
        capital_base = float(os.getenv("CAPITAL_BASE_USD", "1500.0"))
        logger.warning(f"⚠️  Usando CAPITAL_BASE_USD del .env como fallback: ${capital_base:,.2f}")
        
    learning_agent = ContinuousLearningAgent(evaluation_interval_sec=300.0)
    initial_learned_config = learning_agent.analyze_and_optimize()

    feature_agents = {s: IngestionFeatureAgent(symbol=s, candle_period_ms=60000, history_length=200) for s in SYMBOLS_LIST}
    signal_agents = {
        s: StrategySignalAgent(
            symbol=s,
            min_confidence_threshold=initial_learned_config.get("min_confidence_threshold", 86.0),
            atr_stop_multiplier=initial_learned_config.get("atr_stop_multiplier", 1.8),
            atr_profit_multiplier=initial_learned_config.get("atr_profit_multiplier", 3.0)
        )
        for s in SYMBOLS_LIST
    }

    risk_guardian = InstitutionalRiskGuardian(
        initial_capital=capital_base,
        max_risk_per_trade_pct=float(os.getenv("MAX_RISK_PER_TRADE_PCT", "1.0")),
        daily_drawdown_limit_pct=float(os.getenv("DAILY_DRAWDOWN_LIMIT_PCT", "3.0")),
        max_concurrent_positions=int(os.getenv("MAX_CONCURRENT_POSITIONS", "3")),
        max_daily_trades=int(os.getenv("MAX_DAILY_TRADES", "6")),
        cooldown_seconds=int(os.getenv("COOLDOWN_SECONDS", "180")),
        max_allowed_spread_bps=float(os.getenv("MAX_ALLOWED_SPREAD_BPS", "5.0"))
    )

    execution_oms = ExecutionOMSAgent()
    resolved_symbols = {s: (resolve_mt5_symbol(s) if has_mt5 else s) for s in SYMBOLS_LIST}

    logger.info("🎯 Escáner Multi-Activo cargado:")
    logger.info(f"  • Activos ({len(SYMBOLS_LIST)}): {', '.join(SYMBOLS_LIST)}")
    logger.info(f"  • Resueltos: {resolved_symbols}")
    logger.info(f"  • Control remoto: ACTIVO ({CONTROL_STATE_FILE})")
    logger.info(f"  • Reporte diario: {DAILY_REPORT_HOUR:02d}:{DAILY_REPORT_MINUTE:02d} (hora MT5 UTC+3)")
    logger.info("=" * 70)

    last_heartbeat_timestamp = datetime.now(TZ_MT5).timestamp()
    last_paused_log = 0.0
    last_report_check = 0.0

    # 🔧 Cooldowns por símbolo
    failed_orders_cooldown: Dict[str, float] = {}
    market_closed_cooldown: Dict[str, float] = {}

    while True:
        try:
            await asyncio.sleep(DECISION_THROTTLE_SECONDS)
            now_wall = datetime.now(TZ_MT5).timestamp()

            # ---------------------------------------------------------------
            # 📊 REPORTE DIARIO
            # ---------------------------------------------------------------
            if time.time() - last_report_check > 30:
                last_report_check = time.time()
                try:
                    await send_daily_report_if_needed()
                except Exception as e:
                    logger.error(f"Error en reporte diario: {e}")

            # ---------------------------------------------------------------
            # 🎮 CONTROL REMOTO
            # ---------------------------------------------------------------
            ctrl = read_control_state()

            if ctrl.get("close_all_requested"):
                logger.warning("🚨 [TELEGRAM] Ejecutando CLOSE ALL...")
                n = close_all_positions()
                logger.warning(f"🚨 [TELEGRAM] {n} posiciones cerradas.")
                send_telegram_alert(f"🚨 *CIERRE TOTAL ejecutado.*\n`{n}` posiciones cerradas.")
                reset_close_all_flag()

            if ctrl.get("paused"):
                now_ts = time.time()
                if now_ts - last_paused_log > 60:
                    logger.info("⏸️  [TELEGRAM] Bot PAUSADO. No se abrirán nuevas órdenes.")
                    last_paused_log = now_ts
                if has_mt5:
                    acc = mt5.account_info()
                    if acc:
                        risk_guardian.sync_capital_from_mt5(acc.balance, acc.equity)
                    positions = mt5.positions_get()
                    if positions is not None:
                        risk_guardian.sync_active_positions([p.symbol for p in positions])
                        execution_oms.sync_mt5_positions(positions, risk_guardian)
                        for sym in SYMBOLS_LIST:
                            resolved_sym = resolved_symbols[sym]
                            tick_info = mt5.symbol_info_tick(resolved_sym)
                            if not tick_info or tick_info.bid <= 0:
                                continue
                            feat = feature_agents[sym].last_feature_vector
                            if feat:
                                for order_id in list(execution_oms.active_orders.keys()):
                                    execution_oms.update_tick_price(order_id, sym, tick_info.bid, feat.atr14)
                continue

            # ---------------------------------------------------------------
            # 🧠 FEEDBACK LEARNER
            # ---------------------------------------------------------------
            try:
                learned_cfg = learning_agent.auto_evaluate_if_needed()
                if learned_cfg:
                    for sig_agent in signal_agents.values():
                        sig_agent.min_confidence = learned_cfg.get("min_confidence_threshold", sig_agent.min_confidence)
            except Exception as e:
                logger.debug(f"Aviso evaluando feedback learner: {e}")

            # ---------------------------------------------------------------
            # 📈 PIPELINE PRINCIPAL
            # ---------------------------------------------------------------
            if has_mt5:
                acc = mt5.account_info()
                if acc:
                    risk_guardian.sync_capital_from_mt5(acc.balance, acc.equity)

                positions = mt5.positions_get()
                if positions is not None:
                    risk_guardian.sync_active_positions([p.symbol for p in positions])
                    execution_oms.sync_mt5_positions(positions, risk_guardian)

                for sym in SYMBOLS_LIST:
                    now_ts = time.time()

                    if sym in failed_orders_cooldown:
                        if now_ts - failed_orders_cooldown[sym] < FAILED_ORDER_COOLDOWN_SEC:
                            continue

                    if sym in market_closed_cooldown:
                        if now_ts - market_closed_cooldown[sym] < MARKET_CLOSED_COOLDOWN_SEC:
                            continue

                    resolved_sym = resolved_symbols[sym]
                    tick_info = mt5.symbol_info_tick(resolved_sym)
                    if not tick_info or tick_info.bid <= 0:
                        continue

                    price = tick_info.bid
                    spread = tick_info.ask - tick_info.bid
                    spread_bps = (spread / price) * 10000.0 if price > 0 else 0.0

                    is_buyer_maker = tick_info.last < tick_info.ask if tick_info.last > 0 else False
                    qty = float(tick_info.volume_real) if hasattr(tick_info, 'volume_real') and tick_info.volume_real > 0 else 1.0

                    tick_obj = Tick(
                        timestamp_ms=get_mt5_timestamp_ms(),
                        symbol=sym,
                        price=price,
                        quantity=qty,
                        is_buyer_maker=is_buyer_maker
                    )

                    feat = feature_agents[sym].process_tick(tick_obj)

                    for order_id in list(execution_oms.active_orders.keys()):
                        execution_oms.update_tick_price(order_id, sym, price, feat.atr14)

                    signal = signal_agents[sym].evaluate(feat)
                    if signal and signal.signal_type in ["BUY", "SELL"]:
                        verdict = risk_guardian.evaluate_order_risk(signal, spread_bps)
                        if verdict.authorized:
                            side_str = normalize_side(signal.signal_type)
                            logger.info(f"🚀 EJECUTANDO ORDEN SNIPER: {side_str} {verdict.authorized_size_units} lotes {sym} ({resolved_sym})")

                            start_time_ms = get_mt5_timestamp_ms()
                            order_type = mt5.ORDER_TYPE_BUY if signal.signal_type == "BUY" else mt5.ORDER_TYPE_SELL
                            req = {
                                "action": mt5.TRADE_ACTION_DEAL,
                                "symbol": resolved_sym,
                                "volume": verdict.authorized_size_units,
                                "type": order_type,
                                "price": tick_info.ask if signal.signal_type == "BUY" else tick_info.bid,
                                "sl": signal.suggested_stop_loss,
                                "tp": signal.suggested_take_profit,
                                "deviation": 20,
                                "magic": int(os.getenv("MAGIC_NUMBER", "992026")),
                                "comment": "QuantEdge-Multi-Py",
                                "type_time": mt5.ORDER_TIME_GTC,
                                "type_filling": mt5.ORDER_FILLING_IOC,
                            }

                            res = None
                            try:
                                res = await send_order_async(req)
                            except Exception as e:
                                logger.error(f"Excepción enviando orden ({sym}): {e}")
                            finally:
                                if not (res and res.retcode == mt5.TRADE_RETCODE_DONE):
                                    risk_guardian.release_pending_lock(sym)

                            execution_latency_ms = round(get_mt5_timestamp_ms() - start_time_ms, 2)

                            if res and res.retcode == mt5.TRADE_RETCODE_DONE:
                                risk_guardian.register_trade_executed(sym)
                                slippage_usd = round(abs(res.price - price) * verdict.authorized_size_units * 100.0, 2)

                                await execution_oms.place_bracket_order(
                                    symbol=sym,
                                    side=side_str,
                                    quantity=verdict.authorized_size_units,
                                    current_market_price=res.price,
                                    stop_loss=signal.suggested_stop_loss,
                                    take_profit=signal.suggested_take_profit
                                )

                                log_order_filled(
                                    symbol=sym,
                                    side=side_str,
                                    volume=verdict.authorized_size_units,
                                    fill_price=res.price,
                                    sl=signal.suggested_stop_loss,
                                    tp=signal.suggested_take_profit,
                                    ticket=res.order,
                                    metadata={
                                        "execution_latency_ms": execution_latency_ms,
                                        "slippage_usd": slippage_usd,
                                        "confidence_percent": signal.confidence_percent
                                    }
                                )

                                send_telegram_alert(
                                    "🎯 *ORDEN SNIPER EJECUTADA*\n"
                                    f"• Activo: `{sym}` (`{resolved_sym}`)\n"
                                    f"• Lado: `{side_str}`\n"
                                    f"• Precio: `{res.price}`\n"
                                    f"• Ticket: `#{res.order}`\n"
                                    f"• Latencia: `{execution_latency_ms} ms`\n"
                                    f"• SL: `{signal.suggested_stop_loss}` | TP: `{signal.suggested_take_profit}`\n"
                                    f"• Confianza: `{signal.confidence_percent}%`"
                                )
                            else:
                                comment_str = res.comment if res else "Respuesta nula de MT5"
                                retcode = res.retcode if res else -1
                                logger.error(f"Fallo al ejecutar en MT5 ({sym}): {comment_str} (retcode={retcode})")

                                comment_lower = str(comment_str).lower()

                                if retcode == 10018 or "market closed" in comment_lower:
                                    market_closed_cooldown[sym] = time.time()
                                    logger.warning(
                                        f"⏸️ Mercado cerrado en {sym}. Cooldown {int(MARKET_CLOSED_COOLDOWN_SEC/60)} min."
                                    )
                                elif "invalid stops" in comment_lower:
                                    failed_orders_cooldown[sym] = time.time()
                                    logger.warning(
                                        f"⏸️ Cooldown de {int(FAILED_ORDER_COOLDOWN_SEC/60)} min en {sym} tras 'Invalid stops'."
                                    )
                                elif "volume" in comment_lower:
                                    failed_orders_cooldown[sym] = time.time()
                                    logger.warning(
                                        f"⏸️ Cooldown de {int(FAILED_ORDER_COOLDOWN_SEC/60)} min en {sym} tras error de volumen."
                                    )

                                log_rejection(
                                    symbol=sym,
                                    reason=f"Rechazo de ejecución en MT5: {comment_str}",
                                    details=f"Retcode: {retcode} | SL: {signal.suggested_stop_loss} TP: {signal.suggested_take_profit}",
                                    side=side_str,
                                    price=price,
                                    volume=verdict.authorized_size_units
                                )

            # ---------------------------------------------------------------
            # 💓 HEARTBEAT CADA 15 MIN
            # ---------------------------------------------------------------
            if now_wall - last_heartbeat_timestamp >= HEARTBEAT_INTERVAL_SECONDS:
                last_heartbeat_timestamp = now_wall
                logger.info("=" * 70)
                logger.info("🔍 [ESCÁNER MULTI-ACTIVO] Diagnóstico (Cada 15 Minutos):")
                for sym in SYMBOLS_LIST:
                    res_s = resolved_symbols[sym]
                    if has_mt5:
                        t_info = mt5.symbol_info_tick(res_s)
                        if t_info and t_info.bid > 0:
                            p_curr = t_info.bid
                            feat_diag = feature_agents[sym].last_feature_vector
                            if feat_diag:
                                trend_str = "ALCISTA" if feat_diag.ema9 > feat_diag.ema21 else "BAJISTA"
                                vwap_str = "SOBRE VWAP" if feat_diag.price > feat_diag.vwap else "BAJO VWAP"
                                rsi_val = f"{feat_diag.rsi14:.1f}"
                                atr_val = f"{feat_diag.atr14:.5f}"
                            else:
                                trend_str = vwap_str = rsi_val = atr_val = "N/D"

                            block_info = ""
                            if sym in market_closed_cooldown:
                                elapsed = time.time() - market_closed_cooldown[sym]
                                if elapsed < MARKET_CLOSED_COOLDOWN_SEC:
                                    remaining = int(MARKET_CLOSED_COOLDOWN_SEC - elapsed)
                                    block_info = f" | 🔒 CLOSED: {remaining}s"
                            elif sym in failed_orders_cooldown:
                                elapsed = time.time() - failed_orders_cooldown[sym]
                                if elapsed < FAILED_ORDER_COOLDOWN_SEC:
                                    remaining = int(FAILED_ORDER_COOLDOWN_SEC - elapsed)
                                    block_info = f" | ⏸️ CD: {remaining}s"

                            logger.info(
                                f"  • {sym:<7} ({res_s:<8}) | ${p_curr:<10.5f} | "
                                f"{trend_str:<7} | {vwap_str:<10} | RSI: {rsi_val:<6} | ATR: {atr_val}{block_info}"
                            )
                logger.info("=" * 70)

        except Exception as loop_err:
            logger.error(f"Error en bucle multi-activo: {loop_err}")
            await asyncio.sleep(1.0)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("🛑 Bot detenido por el usuario (Ctrl+C).")
    finally:
        try:
            mt5.shutdown()
        except Exception:
            pass