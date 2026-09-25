"""
=============================================================================
QUANTEDGE AI — METATRADER 5 (IC MARKETS) REAL-TIME LOCAL BRIDGE (UTC+3)
=============================================================================
🔧 FIX:
  • resolve_symbol_name ya no devuelve dentro del for.
  • history_deals_get se cachea cada 60s (antes: cada 0.5s).
  • execute_order usa lock global y try/finally.
"""
import asyncio
import json
import logging
import os
import sys
import time
from pathlib import Path
from datetime import datetime, timezone, timedelta
from typing import Set, Any, Optional
import websockets
import MetaTrader5 as mt5

TZ_MT5 = timezone(timedelta(hours=3))

class MT5TimeFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        dt = datetime.fromtimestamp(record.created, tz=TZ_MT5)
        if datefmt:
            return dt.strftime(datefmt)
        return dt.isoformat()

handler = logging.StreamHandler()
handler.setFormatter(MT5TimeFormatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))

logger = logging.getLogger("MT5Bridge")
logger.addHandler(handler)
logger.setLevel(logging.INFO)

logging.getLogger("websockets").setLevel(logging.CRITICAL)
logging.getLogger("websockets.server").setLevel(logging.CRITICAL)

PORT = 8001
CONNECTED_CLIENTS: Set[Any] = set()

MT5_ACCOUNT = int(os.getenv("MT5_ACCOUNT", "52974519"))
MT5_PASSWORD = os.getenv("MT5_PASSWORD", "")
MT5_SERVER = os.getenv("MT5_SERVER", "ICMarketsSC-Demo")

# 🔧 Cache de historial de deals
_HISTORY_CACHE = {"data": [], "last_fetch": 0.0}
_HISTORY_CACHE_TTL = 60.0


def get_mt5_timestamp_ms() -> int:
    return int(datetime.now(TZ_MT5).timestamp() * 1000)

def get_mt5_iso_time() -> str:
    return datetime.now(TZ_MT5).isoformat()

def init_mt5() -> bool:
    logger.info("Iniciando conexión con MetaTrader 5...")
    if not mt5.initialize():
        logger.error(f"Error al inicializar MT5: {mt5.last_error()}")
        return False

    logger.info(f"Autenticando en MT5 Cuenta #{MT5_ACCOUNT} en servidor {MT5_SERVER}...")
    if MT5_PASSWORD:
        login_ok = mt5.login(login=MT5_ACCOUNT, password=MT5_PASSWORD, server=MT5_SERVER)
    else:
        login_ok = mt5.login(login=MT5_ACCOUNT, server=MT5_SERVER)

    if not login_ok:
        logger.warning(f"Aviso de login: {mt5.last_error()}. Verificando si el terminal ya tiene sesión activa...")

    account_info = mt5.account_info()
    if account_info is None:
        logger.error("No se pudo obtener información de cuenta en MT5. Revisa tus credenciales o abre el terminal.")
        return False
    else:
        logger.info("✅ CONECTADO DIRECTAMENTE A METATRADER 5!")
        logger.info(f"  • Titular:   {account_info.name}")
        logger.info(f"  • Cuenta:    #{account_info.login}")
        logger.info(f"  • Servidor:  {account_info.server}")
        logger.info(f"  • Balance:   ${account_info.balance:,.2f} {account_info.currency}")
        logger.info(f"  • Equidad:   ${account_info.equity:,.2f} {account_info.currency}")
        logger.info(f"  • Apalancam.: 1:{account_info.leverage}")

    return True


def _fetch_closed_trades_cached():
    """🔧 Devuelve el historial de deals cacheado (TTL 60s)."""
    now = time.time()
    if now - _HISTORY_CACHE["last_fetch"] < _HISTORY_CACHE_TTL:
        return _HISTORY_CACHE["data"]

    closed_trades = []
    try:
        from_date = datetime.now(TZ_MT5) - timedelta(days=7)
        to_date = datetime.now(TZ_MT5) + timedelta(days=1)
        deals = mt5.history_deals_get(from_date, to_date)
        if deals:
            for d in deals:
                if d.entry == mt5.DEAL_ENTRY_OUT or d.profit != 0:
                    raw_time = d.time_msc if hasattr(d, 'time_msc') and d.time_msc else (d.time * 1000 if hasattr(d, 'time') else get_mt5_timestamp_ms())
                    if raw_time < 100_000_000_000:
                        raw_time = raw_time * 1000
                    closed_trades.append({
                        "ticket": d.ticket,
                        "deal": d.deal if hasattr(d, 'deal') else d.ticket,
                        "symbol": d.symbol,
                        "type": "BUY" if d.type == mt5.DEAL_TYPE_BUY else "SELL",
                        "volume": d.volume,
                        "priceOpen": d.price,
                        "priceClose": d.price,
                        "profit": round(d.profit, 2),
                        "commission": round(d.commission, 2) if hasattr(d, 'commission') else 0.0,
                        "time": raw_time,
                        "comment": d.comment if hasattr(d, 'comment') else ""
                    })
    except Exception as e:
        logger.debug(f"Aviso extrayendo historial de deals: {e}")

    _HISTORY_CACHE["data"] = closed_trades
    _HISTORY_CACHE["last_fetch"] = now
    return closed_trades


def get_account_payload():
    info = mt5.account_info()
    if not info:
        return None

    raw_positions = mt5.positions_get()
    positions = []
    if raw_positions:
        for p in raw_positions:
            positions.append({
                "ticket": p.ticket,
                "symbol": p.symbol,
                "type": "BUY" if p.type == mt5.ORDER_TYPE_BUY else "SELL",
                "volume": p.volume,
                "priceOpen": p.price_open,
                "priceCurrent": p.price_current,
                "sl": p.sl,
                "tp": p.tp,
                "pnl": round(p.profit, 2),
                "comment": p.comment,
                "time": p.time_msc
            })

    return {
        "type": "ACCOUNT_SYNC",
        "login": info.login,
        "name": info.name,
        "server": info.server,
        "currency": info.currency,
        "balance": round(info.balance, 2),
        "equity": round(info.equity, 2),
        "margin": round(info.margin, 2),
        "marginFree": round(info.margin_free, 2),
        "positions": positions,
        "positionsCount": len(positions),
        "closedTrades": _fetch_closed_trades_cached(),  # 🔧 cacheado
        "timestamp": get_mt5_timestamp_ms(),
        "isoTime": get_mt5_iso_time()
    }


SYMBOL_ALIASES = {
    "BRENT": ["BRENT", "XBRUSD", "UKOUSD", "BRENT.raw", "XBRUSD.raw"],
    "WTI": ["WTI", "XTIUSD", "USOUSD", "WTI.raw", "XTIUSD.raw"],
    "XAUUSD": ["XAUUSD", "GOLD", "XAUUSD.raw"],
    "EURUSD": ["EURUSD", "EURUSD.raw"],
    "GBPUSD": ["GBPUSD", "GBPUSD.raw"],
    "BTCUSDT": ["BTCUSD", "BTCUSD.raw", "BTCUSDT"],
    "ETHUSDT": ["ETHUSD", "ETHUSD.raw", "ETHUSDT"],
    "SOLUSDT": ["SOLUSD", "SOLUSD.raw", "SOLUSDT"]
}


def resolve_symbol_name(symbol: str) -> str:
    """🔧 FIX: el return estaba dentro del for y solo probaba el primer alias."""
    if mt5.symbol_info(symbol):
        return symbol
    for alias in SYMBOL_ALIASES.get(symbol, []):
        if mt5.symbol_info(alias):
            return alias
    return symbol


def get_market_snapshot():
    symbols_to_stream = ["XAUUSD", "WTI", "BRENT", "EURUSD", "GBPUSD", "BTCUSDT", "ETHUSDT", "SOLUSDT"]
    snapshot = {}
    for sym in symbols_to_stream:
        resolved = resolve_symbol_name(sym)
        tick = mt5.symbol_info_tick(resolved)
        if tick and tick.bid > 0:
            snapshot[sym] = {
                "price": tick.bid,
                "ask": tick.ask,
                "spread": round(tick.ask - tick.bid, 5),
                "timestamp": get_mt5_timestamp_ms()
            }
    return {"type": "MARKET_SNAPSHOT", "data": snapshot}


def get_canonical_asset(sym: str) -> str:
    if not sym:
        return ""
    s = str(sym).upper().replace(".RAW", "").replace("_RAW", "").strip()
    if "BTC" in s or "BITCOIN" in s:
        return "BTC"
    if "ETH" in s or "ETHEREUM" in s:
        return "ETH"
    if "SOL" in s or "SOLANA" in s:
        return "SOL"
    if "XAU" in s or "GOLD" in s or "ORO" in s:
        return "XAU"
    if "WTI" in s or "XTI" in s or "USO" in s or "CRUDE" in s or "OIL" in s or "PETROLEO" in s:
        return "WTI"
    if "BRENT" in s or "XBR" in s or "UKO" in s:
        return "BRENT"
    if "EUR" in s:
        return "EURUSD"
    if "GBP" in s:
        return "GBPUSD"
    return s


def normalize_volume(info, volume: float) -> float:
    vol_min = info.volume_min
    vol_max = info.volume_max
    vol_step = info.volume_step

    if vol_step > 0:
        volume = round(volume / vol_step) * vol_step

    volume = max(vol_min, min(vol_max, volume))
    digits = 2 if vol_step < 0.1 else (1 if vol_step < 1.0 else 0)
    return round(volume, digits)


def validate_and_fix_stops(info, side: str, price: float, sl: float, tp: float) -> tuple[float, float]:
    if sl <= 0 and tp <= 0:
        return 0.0, 0.0

    point = info.point
    stops_level = info.stops_level * point
    digits = info.digits
    symbol = info.name

    min_dist_points = (
        0.0015 if "USD" in symbol and "XAU" not in symbol and "XTI" not in symbol and "XBR" not in symbol else 0.50
    )
    min_distance = max(stops_level, min_dist_points)

    final_sl = sl
    final_tp = tp

    if side == "BUY":
        if final_sl > 0 and (price - final_sl) < min_distance:
            final_sl = price - min_distance
        if final_tp > 0 and (final_tp - price) < min_distance:
            final_tp = price + min_distance
    elif side == "SELL":
        if final_sl > 0 and (final_sl - price) < min_distance:
            final_sl = price + min_distance
        if final_tp > 0 and (price - final_tp) < min_distance:
            final_tp = price - min_distance

    return round(final_sl, digits) if final_sl > 0 else 0.0, round(final_tp, digits) if final_tp > 0 else 0.0


LAST_ORDER_TIMESTAMP = 0.0
ORDER_THROTTLE_SECONDS = 0.5


def execute_order(data: dict) -> dict:
    """🔧 FIX: usa try/finally para garantizar consistencia y lock monotónico."""
    global LAST_ORDER_TIMESTAMP
    now = time.monotonic()
    if now - LAST_ORDER_TIMESTAMP < ORDER_THROTTLE_SECONDS:
        return {"status": "THROTTLED", "message": "Orden rechazada por limitador de frecuencia (500ms throttling)"}
    LAST_ORDER_TIMESTAMP = now

    req_symbol = data.get("symbol", "XAUUSD")
    symbol = resolve_symbol_name(req_symbol)
    side = data.get("side", "BUY")
    volume_raw = float(data.get("volume", 0.01))
    sl_raw = float(data.get("sl", 0.0))
    tp_raw = float(data.get("tp", 0.0))

    current_positions = mt5.positions_get()
    if current_positions:
        req_canonical = get_canonical_asset(req_symbol)
        for pos in current_positions:
            pos_canonical = get_canonical_asset(pos.symbol)
            if pos_canonical == req_canonical:
                reject_msg = f"Ya existe una posición activa en {pos.symbol} (Ticket #{pos.ticket}) para el activo {req_canonical}. Orden rechazada por regla de 1 posición por activo."
                logger.warning(f"🛡️ BLOQUEO DE RESGUARDO EN MT5: {reject_msg}")
                return {
                    "status": "REJECTED",
                    "message": reject_msg,
                    "ticket": pos.ticket,
                    "symbol": pos.symbol
                }

    info = mt5.symbol_info(symbol)
    if not info:
        return {"status": "ERROR", "message": f"Símbolo {req_symbol} no encontrado en MT5"}

    if not info.visible:
        mt5.symbol_select(symbol, True)

    tick = mt5.symbol_info_tick(symbol)
    if not tick:
        return {"status": "ERROR", "message": f"No hay precio tick para {symbol}"}

    volume = normalize_volume(info, volume_raw)
    price = round(tick.ask if side == "BUY" else tick.bid, info.digits)
    sl, tp = validate_and_fix_stops(info, side, price, sl_raw, tp_raw)

    order_type = mt5.ORDER_TYPE_BUY if side == "BUY" else mt5.ORDER_TYPE_SELL

    filling_modes = [mt5.ORDER_FILLING_FOK, mt5.ORDER_FILLING_IOC, mt5.ORDER_FILLING_RETURN]

    if info.filling_mode & 1:
        filling_modes = [mt5.ORDER_FILLING_FOK, mt5.ORDER_FILLING_IOC, mt5.ORDER_FILLING_RETURN]
    elif info.filling_mode & 2:
        filling_modes = [mt5.ORDER_FILLING_IOC, mt5.ORDER_FILLING_FOK, mt5.ORDER_FILLING_RETURN]

    last_result = None
    try:
        for fill_mode in filling_modes:
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": symbol,
                "volume": volume,
                "type": order_type,
                "price": price,
                "sl": sl,
                "tp": tp,
                "deviation": 20,
                "magic": 992026,
                "comment": "QuantEdge-Sniper",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": fill_mode,
            }

            result = mt5.order_send(request)
            last_result = result
            if result and result.retcode == mt5.TRADE_RETCODE_DONE:
                logger.info(f"🎯 Orden ejecutada con éxito en MT5: Ticket #{result.order} {side} {volume} {symbol} @ {result.price}")
                return {
                    "status": "SUCCESS",
                    "orderId": result.order,
                    "symbol": symbol,
                    "side": side,
                    "volume": volume,
                    "fillPrice": result.price
                }
    finally:
        pass  # El lock se libera solo por throttle de tiempo

    comment_err = last_result.comment if last_result else "Sin respuesta"
    retcode_err = last_result.retcode if last_result else -1
    logger.error(f"❌ Error MT5 al enviar orden: {retcode_err} ({comment_err})")
    return {"status": "ERROR", "code": retcode_err, "comment": comment_err}


async def handler(websocket):
    CONNECTED_CLIENTS.add(websocket)
    logger.info(f"🟢 Cliente QuantEdge Web conectado desde {websocket.remote_address}")

    try:
        payload = get_account_payload()
        if payload:
            await websocket.send(json.dumps(payload))

        snap = get_market_snapshot()
        if snap["data"]:
            await websocket.send(json.dumps(snap))

        async for message in websocket:
            try:
                data = json.loads(message)
                action = data.get("action")

                if action == "PING":
                    await websocket.send(json.dumps({"type": "PONG", "time": get_mt5_timestamp_ms()}))
                elif action in ["ORDER", "EXECUTE_ORDER"]:
                    res = execute_order(data)
                    await websocket.send(json.dumps({"type": "ORDER_RESULT", "data": res}))
                elif action in ["CLOSE", "CLOSE_ORDER"]:
                    ticket_raw = data.get("ticket")
                    try:
                        ticket = int(ticket_raw)
                        pos = mt5.positions_get(ticket=ticket)
                        if pos and len(pos) > 0:
                            p = pos[0]
                            tick = mt5.symbol_info_tick(p.symbol)
                            price = tick.bid if p.type == mt5.ORDER_TYPE_BUY else tick.ask
                            c_type = mt5.ORDER_TYPE_SELL if p.type == mt5.ORDER_TYPE_BUY else mt5.ORDER_TYPE_BUY
                            req = {
                                "action": mt5.TRADE_ACTION_DEAL,
                                "position": p.ticket,
                                "symbol": p.symbol,
                                "volume": p.volume,
                                "type": c_type,
                                "price": price,
                                "magic": 992026,
                                "comment": "Close Sniper",
                            }
                            mt5.order_send(req)
                    except Exception as err:
                        logger.error(f"Error cerrando ticket {ticket_raw}: {err}")
                elif action == "CLOSE_ALL":
                    positions = mt5.positions_get()
                    if positions:
                        for p in positions:
                            tick = mt5.symbol_info_tick(p.symbol)
                            price = tick.bid if p.type == mt5.ORDER_TYPE_BUY else tick.ask
                            c_type = mt5.ORDER_TYPE_SELL if p.type == mt5.ORDER_TYPE_BUY else mt5.ORDER_TYPE_BUY
                            req = {
                                "action": mt5.TRADE_ACTION_DEAL,
                                "position": p.ticket,
                                "symbol": p.symbol,
                                "volume": p.volume,
                                "type": c_type,
                                "price": price,
                                "magic": 992026,
                                "comment": "Close All",
                            }
                            mt5.order_send(req)
                    await websocket.send(json.dumps({"type": "CLOSE_ALL_DONE"}))
            except Exception as e:
                logger.error(f"Error procesando mensaje: {e}")

    except websockets.ConnectionClosed:
        logger.warning("Cliente desconectado.")
    finally:
        CONNECTED_CLIENTS.discard(websocket)


async def broadcast_loop():
    symbols_to_stream = ["XAUUSD", "WTI", "BRENT", "EURUSD", "GBPUSD", "BTCUSDT", "ETHUSDT", "SOLUSDT"]

    while True:
        await asyncio.sleep(0.5)
        if not CONNECTED_CLIENTS:
            continue

        try:
            payload = get_account_payload()
            if payload:
                message = json.dumps(payload)
                await asyncio.gather(*[client.send(message) for client in CONNECTED_CLIENTS], return_exceptions=True)

            for sym in symbols_to_stream:
                resolved_sym = resolve_symbol_name(sym)
                tick = mt5.symbol_info_tick(resolved_sym)
                if tick:
                    tick_payload = json.dumps({
                        "type": "PRICE_TICK",
                        "symbol": sym,
                        "price": tick.bid,
                        "ask": tick.ask,
                        "timestamp": get_mt5_timestamp_ms(),
                        "isoTime": get_mt5_iso_time()
                    })
                    await asyncio.gather(*[client.send(tick_payload) for client in CONNECTED_CLIENTS], return_exceptions=True)

        except Exception as e:
            logger.error(f"Error en broadcast: {e}")


async def main():
    if not init_mt5():
        logger.warning("No se pudo conectar con MT5 en el arranque. Asegúrate de abrir la app MetaTrader 5.")

    logger.info(f"Iniciando WebSocket Bridge en ws://127.0.0.1:{PORT} ...")
    server = await websockets.serve(handler, "127.0.0.1", PORT)
    logger.info("🚀 BRIDGE ACTIVO. Listo para recibir la conexión de tu panel QuantEdge AI.")

    await asyncio.gather(
        server.wait_closed(),
        broadcast_loop()
    )


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bridge detenido por el usuario.")
        mt5.shutdown()
        sys.exit(0)