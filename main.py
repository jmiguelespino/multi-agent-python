"""
=============================================================================
QUANTEDGE AI — MOTOR AUTÓNOMO DE TRADING INSTITUCIONAL MULTI-ACTIVO (UTC+3)
=============================================================================
🔧 v1.9.0 — LOTE FUSIONADO 2.6+3:
  • 🐛 B20: consulta `disabled_symbols` del learner y salta esos símbolos.
  • 🐛 B12: importa build_daily_report de report_utils.py (sin duplicación).
  • 🐛 O2: bucle órdenes×símbolos invertido a símbolo→órdenes (más eficiente).
  • 🐛 O3: flush periódico del audit_logger.
  • v1.8.0 heredado: B2 (sin place_bracket_order), B14 (learner completo).
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

TZ_MT5 = timezone(timedelta(hours=3))


class MT5TimeFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        dt = datetime.fromtimestamp(record.created, tz=TZ_MT5)
        return dt.strftime(datefmt) if datefmt else dt.isoformat()


for h in logging.root.handlers[:]:
    logging.root.removeHandler(h)

handler = logging.StreamHandler()
handler.setFormatter(MT5TimeFormatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))

logger = logging.getLogger("QuantEdgeSniper")
logger.addHandler(handler)
logger.setLevel(logging.INFO)
logger.propagate = False

BASE_DIR = Path(__file__).resolve().parent

env_file = BASE_DIR.parent / '.env'
if not env_file.exists():
    env_file = BASE_DIR / '.env'
load_dotenv(dotenv_path=env_file)

logging.getLogger("SignalAgent").setLevel(logging.DEBUG)

import MetaTrader5 as mt5
from signal_agent import StrategySignalAgent
from risk_guardian import InstitutionalRiskGuardian
from execution_agent import ExecutionOMSAgent
from feature_agent import IngestionFeatureAgent
from feedback_learner import ContinuousLearningAgent
from data_streamer import Tick
from telegram_notifier import send_telegram_alert
from audit_logger import (
    log_order_filled,
    log_rejection,
    log_audit_event,
    flush_audit_log,
)

# 🐛 B12: importar utilidades unificadas
from report_utils import (
    build_daily_report,
    read_control_state,
    read_config_optimized,
)

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


def reset_close_all_flag():
    try:
        state = read_control_state()
        state["close_all_requested"] = False
        with open(CONTROL_STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2)
    except Exception:
        pass


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


def should_send_daily_report() -> bool:
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
    if not should_send_daily_report():
        return

    now_mt5 = datetime.now(TZ_MT5)
    today_str = now_mt5.strftime("%Y-%m-%d")

    logger.info("=" * 70)
    logger.info(f"📊 [DAILY REPORT] Disparando reporte para {today_str}")
    logger.info("=" * 70)

    try:
        report = build_daily_report(days=1, include_tests=False)
        sent = send_telegram_alert(report)

        if sent:
            write_daily_report_state(today_str)
            logger.info(f"✅ [DAILY REPORT] Enviado para {today_str}")
        else:
            logger.warning("⚠️ [DAILY REPORT] No se pudo enviar.")
    except Exception as e:
        logger.error(f"❌ [DAILY REPORT] Error: {e}")


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


def infer_is_buyer_maker(tick_info) -> bool:
    try:
        bid = float(getattr(tick_info, "bid", 0.0) or 0.0)
        ask = float(getattr(tick_info, "ask", 0.0) or 0.0)
        last = float(getattr(tick_info, "last", 0.0) or 0.0)
    except Exception:
        return False

    if last <= 0 or bid <= 0 or ask <= 0:
        return False

    if last >= ask:
        return False
    if last <= bid:
        return True

    mid = (bid + ask) / 2.0
    return last < mid


# =============================================================================
# CONFIGURACIÓN
# =============================================================================
MT5_ACCOUNT = int(os.getenv("MT5_ACCOUNT", "52974519"))
MT5_PASSWORD = os.getenv("MT5_PASSWORD", "")
MT5_SERVER = os.getenv("MT5_SERVER", "ICMarketsSC-Demo")

DEFAULT_SYMBOLS = "XAUUSD,WTI,BRENT,EURUSD,GBPUSD,BTCUSD,ETHUSD,SOLUSD"
TRADING_SYMBOLS_RAW = os.getenv("TRADING_SYMBOLS", DEFAULT_SYMBOLS)
SYMBOLS_LIST = [s.strip() for s in TRADING_SYMBOLS_RAW.split(",") if s.strip()]

DECISION_THROTTLE_SECONDS = float(os.getenv("DECISION_THROTTLE_SECONDS", "1.0"))
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
        logger.warning(f"Aviso de login MT5: {mt5.last_error()}")

    info = mt5.account_info()
    if info is None:
        logger.error("No se pudo leer info de cuenta MT5.")
        return False

    logger.info("=" * 70)
    logger.info("✅ CONECTADO A METATRADER 5 (IC MARKETS)")
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
    elif s_upper in ["XAGUSD", "SILVER"]:
        aliases.extend(["SILVER", "XAGUSD", "XAGUSD.raw", "SILVER.raw"])
    elif s_upper in ["US500", "SP500", "SPX"]:
        aliases.extend(["US500", "SP500", "SPX500", "US500.raw", "SP500.raw"])
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
# 🐛 B14: propagación de parámetros del learner a signal agents
# =============================================================================
def apply_learned_config_to_signal_agents(signal_agents: dict, learned_cfg: dict):
    if not learned_cfg:
        return

    new_conf = learned_cfg.get("min_confidence_threshold")
    new_sl = learned_cfg.get("atr_stop_multiplier")
    new_tp = learned_cfg.get("atr_profit_multiplier")

    for sym, sig_agent in signal_agents.items():
        if new_conf is not None:
            sig_agent.min_confidence = new_conf
        # 🐛 B19: delegar en método del agente que respeta límites por clase
        sig_agent.apply_learned_params(atr_sl=new_sl, atr_tp=new_tp)

    if new_conf is not None or new_sl is not None or new_tp is not None:
        logger.debug(
            f"🧠 Learner → SignalAgents: conf={new_conf}% | SL={new_sl}× | TP={new_tp}×"
        )


# =============================================================================
# MAIN
# =============================================================================
async def main():
    logger.info("Iniciando pipeline Sniper Cuantitativo Multi-Activo...")

    has_mt5 = connect_mt5()

    capital_base = None
    if has_mt5:
        acc = mt5.account_info()
        if acc and acc.balance > 0:
            capital_base = acc.balance
            logger.info(f"💰 Capital Base desde MT5: ${capital_base:,.2f}")
        else:
            logger.warning("⚠️ MT5 sin info de cuenta. Fallback.")
    else:
        logger.warning("⚠️ MT5 no disponible. Fallback.")

    if capital_base is None:
        capital_base = float(os.getenv("CAPITAL_BASE_USD", "1500.0"))
        logger.warning(f"⚠️ CAPITAL_BASE_USD fallback: ${capital_base:,.2f}")

    learning_agent = ContinuousLearningAgent(evaluation_interval_sec=300.0)
    initial_learned_config = learning_agent.analyze_and_optimize()

    feature_agents = {s: IngestionFeatureAgent(symbol=s, candle_period_ms=60000, history_length=200) for s in SYMBOLS_LIST}
    signal_agents = {
        s: StrategySignalAgent(
            symbol=s,
            min_confidence_threshold=initial_learned_config.get("min_confidence_threshold", 90.0),
            atr_stop_multiplier=initial_learned_config.get("atr_stop_multiplier", 2.0),
            atr_profit_multiplier=initial_learned_config.get("atr_profit_multiplier", 3.0)
        )
        for s in SYMBOLS_LIST
    }

    risk_guardian = InstitutionalRiskGuardian(
        initial_capital=capital_base,
        max_risk_per_trade_pct=float(os.getenv("MAX_RISK_PER_TRADE_PCT", "0.5")),
        daily_drawdown_limit_pct=float(os.getenv("DAILY_DRAWDOWN_LIMIT_PCT", "3.0")),
        max_concurrent_positions=int(os.getenv("MAX_CONCURRENT_POSITIONS", "3")),
        max_daily_trades=int(os.getenv("MAX_DAILY_TRADES", "20")),
        cooldown_seconds=int(os.getenv("COOLDOWN_SECONDS", "60")),
        max_allowed_spread_bps=float(os.getenv("MAX_ALLOWED_SPREAD_BPS", "15.0"))
    )

    execution_oms = ExecutionOMSAgent()
    resolved_symbols = {s: (resolve_mt5_symbol(s) if has_mt5 else s) for s in SYMBOLS_LIST}

    # 🐛 B20: caché de símbolos deshabilitados
    disabled_now = initial_learned_config.get("disabled_symbols", [])

    logger.info("🎯 Escáner Multi-Activo cargado:")
    logger.info(f"  • Activos ({len(SYMBOLS_LIST)}): {', '.join(SYMBOLS_LIST)}")
    logger.info(f"  • Resueltos: {resolved_symbols}")
    if disabled_now:
        logger.info(f"  • ⛔ Deshabilitados por learner: {', '.join(disabled_now)}")
    logger.info(f"  • Control remoto: ACTIVO ({CONTROL_STATE_FILE})")
    logger.info(f"  • Reporte diario: {DAILY_REPORT_HOUR:02d}:{DAILY_REPORT_MINUTE:02d} (MT5 UTC+3)")
    logger.info(f"  • Warmup mínimo: 20 velas cerradas por símbolo (~20 min)")
    logger.info("=" * 70)

    log_audit_event(
        event_type="BOT_STARTED",
        category="SYSTEM",
        symbol="SYSTEM",
        reason="QuantEdge AI v1.9.0 arrancado",
        details=f"MT5 #{MT5_ACCOUNT} | {len(SYMBOLS_LIST)} símbolos | capital ${capital_base:,.2f}",
        metadata={
            "version": "1.9.0",
            "phase": "LOTE_FUSIONADO_2.6+3",
            "warmup_min_candles": 20,
            "symbols": SYMBOLS_LIST,
            "disabled_symbols": disabled_now,
            "capital_base": round(capital_base, 2),
        }
    )
    logger.info("📝 BOT_STARTED registrado en JSONL")

    last_heartbeat_timestamp = datetime.now(TZ_MT5).timestamp()
    last_paused_log = 0.0
    last_report_check = 0.0
    last_warmup_log = 0.0
    last_disabled_refresh = 0.0

    failed_orders_cooldown: Dict[str, float] = {}
    market_closed_cooldown: Dict[str, float] = {}

    while True:
        try:
            await asyncio.sleep(DECISION_THROTTLE_SECONDS)
            now_wall = datetime.now(TZ_MT5).timestamp()

            # 🐛 O3: flush periódico del audit log
            try:
                from audit_logger import _writer
                _writer.maybe_flush_periodic()
            except Exception:
                pass

            if time.time() - last_report_check > 30:
                last_report_check = time.time()
                try:
                    await send_daily_report_if_needed()
                except Exception as e:
                    logger.error(f"Error en reporte diario: {e}")

            # 🐛 B20: refrescar disabled_symbols cada 5 min
            if time.time() - last_disabled_refresh > 300:
                last_disabled_refresh = time.time()
                try:
                    cfg_now = read_config_optimized()
                    disabled_now = cfg_now.get("disabled_symbols", [])
                except Exception:
                    pass

            ctrl = read_control_state()

            if ctrl.get("close_all_requested"):
                logger.warning("🚨 [TELEGRAM] CLOSE ALL...")
                n = close_all_positions()
                logger.warning(f"🚨 [TELEGRAM] {n} posiciones cerradas.")
                send_telegram_alert(f"🚨 *CIERRE TOTAL ejecutado.*\n`{n}` posiciones cerradas.")
                reset_close_all_flag()

            if ctrl.get("paused"):
                now_ts = time.time()
                if now_ts - last_paused_log > 60:
                    logger.info("⏸️  [TELEGRAM] Bot PAUSADO.")
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

            try:
                learned_cfg = learning_agent.auto_evaluate_if_needed()
                apply_learned_config_to_signal_agents(signal_agents, learned_cfg)
            except Exception as e:
                logger.debug(f"Aviso feedback learner: {e}")

            if has_mt5:
                acc = mt5.account_info()
                if acc:
                    risk_guardian.sync_capital_from_mt5(acc.balance, acc.equity)

                positions = mt5.positions_get()
                if positions is not None:
                    risk_guardian.sync_active_positions([p.symbol for p in positions])
                    execution_oms.sync_mt5_positions(positions, risk_guardian)

                if now_wall - last_warmup_log > 300:
                    last_warmup_log = now_wall
                    warmup_status = []
                    for sym in SYMBOLS_LIST:
                        fa = feature_agents[sym]
                        if not fa.is_ready():
                            warmup_status.append(f"{sym}({fa.candles_closed_count}/20)")
                    if warmup_status:
                        logger.info(f"⏳ WARMUP en curso: {', '.join(warmup_status)}")

                # 🐛 O2: iterar símbolos, y dentro cada símbolo, sus órdenes
                for sym in SYMBOLS_LIST:
                    # 🐛 B20: saltar símbolos deshabilitados
                    if sym.upper() in [s.upper() for s in disabled_now]:
                        continue

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

                    is_buyer_maker = infer_is_buyer_maker(tick_info)
                    qty = float(tick_info.volume_real) if hasattr(tick_info, 'volume_real') and tick_info.volume_real > 0 else 1.0

                    tick_obj = Tick(
                        timestamp_ms=get_mt5_timestamp_ms(),
                        symbol=sym,
                        price=price,
                        quantity=qty,
                        is_buyer_maker=is_buyer_maker
                    )

                    feat = feature_agents[sym].process_tick(tick_obj)

                    # 🐛 O2: solo actualizar órdenes del símbolo actual
                    for order_id, order in list(execution_oms.active_orders.items()):
                        if order.symbol == sym or order.symbol == resolved_sym:
                            execution_oms.update_tick_price(order_id, sym, price, feat.atr14)

                    signal = signal_agents[sym].evaluate(feat)
                    if signal and signal.signal_type in ["BUY", "SELL"]:
                        verdict = risk_guardian.evaluate_order_risk(signal, spread_bps)
                        if verdict.authorized:
                            side_str = normalize_side(signal.signal_type)
                            logger.info(f"🚀 EJECUTANDO: {side_str} {verdict.authorized_size_units} lotes {sym} ({resolved_sym})")

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

                                log_order_filled(
                                    symbol=sym,
                                    side=side_str,
                                    volume=verdict.authorized_size_units,
                                    fill_price=res.price,
                                    sl=signal.suggested_stop_loss,
                                    tp=signal.suggested_take_profit,
                                    ticket=res.order,
                                    order_id=str(res.order),
                                    metadata={
                                        "latency_ms": execution_latency_ms,
                                        "requested_price": price,
                                        "confidence": signal.confidence_percent,
                                    }
                                )

                                send_telegram_alert(
                                    "🎯 *ORDEN SNIPER EJECUTADA*\n"
                                    f"• Activo: `{sym}` (`{resolved_sym}`)\n"
                                    f"• Lado: `{side_str}`\n"
                                    f"• Precio: `{res.price}`\n"
                                    f"• Ticket: `#{res.order}`\n"
                                    f"• SL: `{signal.suggested_stop_loss}` | TP: `{signal.suggested_take_profit}`\n"
                                    f"• Confianza: `{signal.confidence_percent}%`"
                                )
                            else:
                                comment_str = res.comment if res else "Respuesta nula"
                                retcode = res.retcode if res else -1
                                logger.error(f"Fallo MT5 ({sym}): {comment_str} (retcode={retcode})")

                                comment_lower = str(comment_str).lower()

                                if retcode == 10018 or "market closed" in comment_lower:
                                    market_closed_cooldown[sym] = time.time()
                                    logger.warning(f"⏸️ Mercado cerrado {sym}. Cooldown {int(MARKET_CLOSED_COOLDOWN_SEC/60)} min.")
                                elif "invalid stops" in comment_lower:
                                    failed_orders_cooldown[sym] = time.time()
                                    logger.warning(f"⏸️ Cooldown {int(FAILED_ORDER_COOLDOWN_SEC/60)} min en {sym} tras 'Invalid stops'.")
                                elif "volume" in comment_lower:
                                    failed_orders_cooldown[sym] = time.time()
                                    logger.warning(f"⏸️ Cooldown {int(FAILED_ORDER_COOLDOWN_SEC/60)} min en {sym} tras error de volumen.")

                                log_rejection(
                                    symbol=sym,
                                    reason=f"Rechazo de ejecución MT5: {comment_str}",
                                    details=f"Retcode: {retcode}",
                                    side=side_str,
                                    price=price,
                                    volume=verdict.authorized_size_units
                                )

            if now_wall - last_heartbeat_timestamp >= HEARTBEAT_INTERVAL_SECONDS:
                last_heartbeat_timestamp = now_wall
                logger.info("=" * 70)
                logger.info("🔍 [ESCÁNER MULTI-ACTIVO] Diagnóstico (Cada 15 Min):")
                for sym in SYMBOLS_LIST:
                    res_s = resolved_symbols[sym]
                    is_disabled = sym.upper() in [s.upper() for s in disabled_now]
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
                                ready_str = "READY" if feat_diag.is_ready else f"WARMUP {feat_diag.candles_closed}/20"
                            else:
                                trend_str = vwap_str = rsi_val = atr_val = "N/D"
                                ready_str = "WARMUP 0/20"

                            block_info = ""
                            if is_disabled:
                                block_info = " | ⛔ DISABLED (B20)"
                            elif sym in market_closed_cooldown:
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
                                f"{trend_str:<7} | {vwap_str:<10} | RSI: {rsi_val:<6} | ATR: {atr_val} | {ready_str}{block_info}"
                            )
                logger.info("=" * 70)

                positions_now = mt5.positions_get() if has_mt5 else None
                log_audit_event(
                    event_type="HEARTBEAT",
                    category="SYSTEM",
                    symbol="SYSTEM",
                    reason="Diagnóstico periódico multi-activo",
                    details=f"Posiciones: {len(positions_now) if positions_now else 0} | Capital: ${capital_base:,.2f}",
                    metadata={
                        "symbols_count": len(SYMBOLS_LIST),
                        "disabled_count": len(disabled_now),
                        "positions_count": len(positions_now) if positions_now else 0,
                        "capital": round(capital_base, 2),
                        "bot_alive": True,
                    }
                )

        except Exception as loop_err:
            logger.error(f"Error en bucle: {loop_err}")
            await asyncio.sleep(1.0)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("🛑 Bot detenido por el usuario (Ctrl+C).")
    finally:
        try:
            flush_audit_log()
        except Exception:
            pass
        try:
            mt5.shutdown()
        except Exception:
            pass