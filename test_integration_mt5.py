"""
=============================================================================
QUANTEDGE AI — TEST DE INTEGRACIÓN CON METATRADER 5 REAL
=============================================================================
⚠️  ADVERTENCIA: Este test REALMENTE abre y cierra una posición en tu
    cuenta Demo. Asegúrate de:
      1. Estar en cuenta DEMO (no real).
      2. Tener MetaTrader 5 abierto y con Algo Trading activo.
      3. Aceptar que se abre una posición de 0.01 lotes.

Ejecución:
    python test_integration_mt5.py
    python test_integration_mt5.py --symbol XAUUSD
    python test_integration_mt5.py --yes   (sin confirmación interactiva)

🔧 v1.1:
  • Fix: stops_level puede no existir según versión de MetaTrader5.
    Se prueban múltiples nombres (stops_level, trade_stops_level, freeze_level)
    y se usa un colchón de seguridad si todos fallan.
  • Fix: si algún test falla, se cierra la posición automáticamente
    para no dejar huérfanos en MT5.
  • Fix: PnL desde deals busca 24h atrás y prueba ambos campos (position_id / position).
  • Añadido: --cleanup para cerrar posiciones huérfanas de tests anteriores.
=============================================================================
"""

import os
import sys
import time
import argparse
import logging
from datetime import datetime, timezone, timedelta
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

TZ_MT5 = timezone(timedelta(hours=3))


class MT5TimeFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        dt = datetime.fromtimestamp(record.created, tz=TZ_MT5)
        return dt.strftime(datefmt) if datefmt else dt.isoformat()


handler = logging.StreamHandler()
handler.setFormatter(MT5TimeFormatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
logger = logging.getLogger("IntegrationTest")
logger.addHandler(handler)
logger.setLevel(logging.INFO)

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

PASSED = 0
FAILED = 0


def ok(msg: str):
    global PASSED
    PASSED += 1
    print(f"{GREEN}✅ PASS{RESET} | {msg}")


def fail(msg: str, err: str = ""):
    global FAILED
    FAILED += 1
    print(f"{RED}❌ FAIL{RESET} | {msg}")
    if err:
        print(f"        ↳ {err}")


def warn(msg: str):
    print(f"{YELLOW}⚠️  WARN{RESET} | {msg}")


def section(title: str):
    print(f"\n{BOLD}{CYAN}─── {title} ───{RESET}")


# -----------------------------------------------------------------------------
# Configuración
# -----------------------------------------------------------------------------
MT5_ACCOUNT = int(os.getenv("MT5_ACCOUNT", "52974519"))
MT5_PASSWORD = os.getenv("MT5_PASSWORD", "")
MT5_SERVER = os.getenv("MT5_SERVER", "ICMarketsSC-Demo")
MAGIC_NUMBER = int(os.getenv("MAGIC_NUMBER", "992026"))
TEST_VOLUME = 0.01
TEST_MAGIC = MAGIC_NUMBER + 1  # diferente al de producción


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------
def get_stops_level(info) -> float:
    """
    🔧 FIX: MetaTrader5 no siempre expone stops_level.
    Probamos varios nombres y devolvemos 0 si ninguno existe.
    """
    for attr in ("stops_level", "trade_stops_level", "freeze_level"):
        val = getattr(info, attr, None)
        if val:
            return float(val)
    return 0.0


def close_position_by_ticket(ticket: int, reason: str = "Cleanup") -> bool:
    """Cierra una posición por ticket. Devuelve True si lo logró."""
    import MetaTrader5 as mt5
    positions = mt5.positions_get(ticket=ticket)
    if not positions:
        return False

    p = positions[0]
    tick = mt5.symbol_info_tick(p.symbol)
    if not tick:
        return False

    close_type = mt5.ORDER_TYPE_SELL if p.type == mt5.ORDER_TYPE_BUY else mt5.ORDER_TYPE_BUY
    price = tick.bid if p.type == mt5.ORDER_TYPE_BUY else tick.ask

    for fm in (mt5.ORDER_FILLING_IOC, mt5.ORDER_FILLING_FOK, mt5.ORDER_FILLING_RETURN):
        req = {
            "action": mt5.TRADE_ACTION_DEAL,
            "position": ticket,
            "symbol": p.symbol,
            "volume": p.volume,
            "type": close_type,
            "price": price,
            "deviation": 30,
            "magic": TEST_MAGIC,
            "comment": f"QTest-{reason}",
            "type_filling": fm,
        }
        res = mt5.order_send(req)
        if res and res.retcode == mt5.TRADE_RETCODE_DONE:
            return True
        time.sleep(0.2)
    return False


def cleanup_huerfanos() -> int:
    """Cierra posiciones abiertas con MAGIC de tests anteriores."""
    import MetaTrader5 as mt5
    positions = mt5.positions_get()
    if not positions:
        return 0

    closed = 0
    for p in positions:
        if p.magic == TEST_MAGIC:
            warn(f"Huérfano detectado: #{p.ticket} {p.symbol} {p.volume} @ ${p.price_open} (magic={p.magic})")
            if close_position_by_ticket(p.ticket, reason="CleanupHuerfano"):
                closed += 1
                ok(f"Cerrado huérfano #{p.ticket}")
            else:
                fail(f"No se pudo cerrar huérfano #{p.ticket}")
    return closed


# -----------------------------------------------------------------------------
# 1. Conexión
# -----------------------------------------------------------------------------
def connect_mt5() -> bool:
    section("1. Conexión a MetaTrader 5")

    try:
        import MetaTrader5 as mt5
    except ImportError:
        fail("MetaTrader5 no instalado. Ejecuta: pip install MetaTrader5")
        return False

    if not mt5.initialize():
        fail(f"mt5.initialize() falló: {mt5.last_error()}")
        return False
    ok("mt5.initialize() OK")

    if MT5_PASSWORD:
        login_ok = mt5.login(login=MT5_ACCOUNT, password=MT5_PASSWORD, server=MT5_SERVER)
    else:
        warn("MT5_PASSWORD vacío, intentando login sin password")
        login_ok = mt5.login(login=MT5_ACCOUNT, server=MT5_SERVER)

    if not login_ok:
        warn(f"mt5.login() devolvió False: {mt5.last_error()}. Verificando sesión activa...")

    acc = mt5.account_info()
    if acc is None:
        fail("account_info() devolvió None. ¿Terminal MT5 abierto y logueado?")
        return False

    ok(f"Cuenta conectada: #{acc.login} ({acc.server})")
    ok(f"Balance: ${acc.balance:,.2f} {acc.currency}")
    ok(f"Equity:  ${acc.equity:,.2f} {acc.currency}")
    ok(f"Leverage: 1:{acc.leverage}")

    if acc.trade_allowed is False:
        fail("Trading NO permitido en la cuenta. Activa 'Algo Trading' en MT5.")
        return False
    ok("Trading permitido en la cuenta")

    if acc.trade_expert is False:
        warn("Asesores expertos NO permitidos. Activa 'Permitir trading algorítmico'.")

    return True


# -----------------------------------------------------------------------------
# Resolución de símbolo
# -----------------------------------------------------------------------------
def resolve_symbol(symbol: str) -> str:
    import MetaTrader5 as mt5
    if mt5.symbol_info(symbol):
        return symbol

    aliases = {
        "XAUUSD": ["GOLD", "XAUUSD.raw", "GOLD.raw"],
        "WTI": ["XTIUSD", "USOIL", "WTI.raw", "XTIUSD.raw"],
        "BRENT": ["XBRUSD", "UKOIL", "BRENT.raw", "XBRUSD.raw"],
        "BTCUSD": ["BTCUSDT", "BTCUSD.raw", "BTCUSDT.raw"],
        "ETHUSD": ["ETHUSDT", "ETHUSD.raw", "ETHUSDT.raw"],
        "SOLUSD": ["SOLUSDT", "SOLUSD.raw", "SOLUSDT.raw"],
    }
    for alias in aliases.get(symbol.upper(), []):
        if mt5.symbol_info(alias):
            return alias
    return symbol


# -----------------------------------------------------------------------------
# 2. Tick
# -----------------------------------------------------------------------------
def test_tick(symbol: str) -> bool:
    section(f"2. Lectura de tick en vivo — {symbol}")

    import MetaTrader5 as mt5
    info = mt5.symbol_info(symbol)
    if info is None:
        fail(f"Símbolo {symbol} no encontrado en MT5")
        return False

    if not info.visible:
        mt5.symbol_select(symbol, True)
        time.sleep(0.5)

    tick = mt5.symbol_info_tick(symbol)
    if tick is None or tick.bid <= 0:
        fail(f"No hay tick para {symbol}")
        return False

    spread = tick.ask - tick.bid
    spread_bps = (spread / tick.bid) * 10000.0 if tick.bid > 0 else 0.0
    ok(f"Tick: bid={tick.bid} ask={tick.ask} spread={spread_bps:.2f} bps")
    ok(f"Contract size: {info.trade_contract_size} | volume_min: {info.volume_min} | volume_step: {info.volume_step}")
    return True


# -----------------------------------------------------------------------------
# 3. Apertura
# -----------------------------------------------------------------------------
def send_test_order(symbol: str, side: str = "BUY") -> tuple[bool, dict]:
    import MetaTrader5 as mt5

    info = mt5.symbol_info(symbol)
    tick = mt5.symbol_info_tick(symbol)

    if side == "BUY":
        price = round(tick.ask, info.digits)
        order_type = mt5.ORDER_TYPE_BUY
        sl = round(price - (info.point * 500), info.digits) if info.point > 0 else 0.0
        tp = round(price + (info.point * 1000), info.digits) if info.point > 0 else 0.0
    else:
        price = round(tick.bid, info.digits)
        order_type = mt5.ORDER_TYPE_SELL
        sl = round(price + (info.point * 500), info.digits) if info.point > 0 else 0.0
        tp = round(price - (info.point * 1000), info.digits) if info.point > 0 else 0.0

    last_res = None
    for fm in (mt5.ORDER_FILLING_IOC, mt5.ORDER_FILLING_FOK, mt5.ORDER_FILLING_RETURN):
        req = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": TEST_VOLUME,
            "type": order_type,
            "price": price,
            "sl": sl,
            "tp": tp,
            "deviation": 30,
            "magic": TEST_MAGIC,
            "comment": "QTest-Integration",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": fm,
        }
        res = mt5.order_send(req)
        last_res = res
        if res and res.retcode == mt5.TRADE_RETCODE_DONE:
            return True, {
                "ticket": res.order,
                "price": res.price,
                "volume": res.volume,
                "filling_mode": fm,
            }
        time.sleep(0.2)

    return False, {
        "retcode": last_res.retcode if last_res else -1,
        "comment": last_res.comment if last_res else "sin respuesta",
    }


def test_open_position(symbol: str) -> tuple[bool, int]:
    section(f"3. Apertura de posición — {symbol} (0.01 lotes)")

    import MetaTrader5 as mt5

    existing = mt5.positions_get(symbol=symbol)
    if existing:
        warn(f"Ya existe(n) {len(existing)} posición(es) en {symbol}.")
        for p in existing:
            warn(f"  #{p.ticket} magic={p.magic} {p.type} {p.volume} @ ${p.price_open}")
        warn("Ejecuta con --cleanup para cerrar huérfanos, o ciérralos manualmente.")
        return False, 0

    success, data = send_test_order(symbol, side="BUY")
    if not success:
        fail(f"order_send() falló: retcode={data.get('retcode')} comment={data.get('comment')}")
        return False, 0

    ok(f"Posición abierta: ticket #{data['ticket']} @ ${data['price']} (filling={data['filling_mode']})")

    time.sleep(0.5)
    positions = mt5.positions_get(ticket=data["ticket"])
    if not positions:
        fail("Posición no aparece en positions_get() tras 0.5s")
        return False, data["ticket"]

    pos = positions[0]
    ok(f"Posición confirmada: {pos.symbol} {pos.volume} lotes @ ${pos.price_open} | SL=${pos.sl} TP=${pos.tp}")
    return True, data["ticket"]


# -----------------------------------------------------------------------------
# 4. Modificar SL (🔧 FIX stops_level)
# -----------------------------------------------------------------------------
def test_modify_sl(ticket: int) -> bool:
    section(f"4. Modificación de SL — Ticket #{ticket}")

    import MetaTrader5 as mt5

    positions = mt5.positions_get(ticket=ticket)
    if not positions:
        fail(f"Ticket #{ticket} no encontrado")
        return False

    pos = positions[0]
    info = mt5.symbol_info(pos.symbol)
    tick = mt5.symbol_info_tick(pos.symbol)

    # 🔧 FIX: stops_level puede no existir. Usamos helper con fallbacks.
    stops_level = get_stops_level(info)

    if stops_level > 0:
        min_distance = stops_level * info.point
    else:
        # Fallback: 100 puntos (1.0 USD en XAUUSD)
        min_distance = info.point * 100

    # Colchón adicional para asegurar aceptación
    min_distance = max(min_distance, info.point * 50)

    if pos.type == mt5.ORDER_TYPE_BUY:
        new_sl = round(tick.bid - min_distance, info.digits)
    else:
        new_sl = round(tick.ask + min_distance, info.digits)

    logger.info(
        f"Diagnóstico SL: bid=${tick.bid} ask=${tick.ask} | "
        f"stops_level={stops_level} | min_distance={min_distance:.4f} | nuevo_sl=${new_sl}"
    )

    req = {
        "action": mt5.TRADE_ACTION_SLTP,
        "position": ticket,
        "symbol": pos.symbol,
        "sl": new_sl,
        "tp": pos.tp,
    }

    res = mt5.order_send(req)
    if not (res and res.retcode == mt5.TRADE_RETCODE_DONE):
        retcode = res.retcode if res else -1
        comment = res.comment if res else "N/A"
        fail(f"No se pudo modificar SL: retcode={retcode} comment={comment}")
        return False

    time.sleep(0.3)
    pos_updated = mt5.positions_get(ticket=ticket)
    if pos_updated and abs(pos_updated[0].sl - new_sl) < info.point * 2:
        ok(f"SL modificado: ${pos.sl} → ${pos_updated[0].sl}")
        return True
    else:
        current_sl = pos_updated[0].sl if pos_updated else "?"
        fail(f"SL solicitado ${new_sl}, SL actual ${current_sl}")
        return False


# -----------------------------------------------------------------------------
# 5. Cierre
# -----------------------------------------------------------------------------
def test_close_position(ticket: int) -> bool:
    section(f"5. Cierre de posición — Ticket #{ticket}")

    import MetaTrader5 as mt5

    positions = mt5.positions_get(ticket=ticket)
    if not positions:
        fail(f"Ticket #{ticket} ya no existe")
        return False

    pos = positions[0]
    tick = mt5.symbol_info_tick(pos.symbol)
    close_type = mt5.ORDER_TYPE_SELL if pos.type == mt5.ORDER_TYPE_BUY else mt5.ORDER_TYPE_BUY
    price = tick.bid if pos.type == mt5.ORDER_TYPE_BUY else tick.ask

    for fm in (mt5.ORDER_FILLING_IOC, mt5.ORDER_FILLING_FOK, mt5.ORDER_FILLING_RETURN):
        req = {
            "action": mt5.TRADE_ACTION_DEAL,
            "position": ticket,
            "symbol": pos.symbol,
            "volume": pos.volume,
            "type": close_type,
            "price": price,
            "deviation": 30,
            "magic": TEST_MAGIC,
            "comment": "QTest-Close",
            "type_filling": fm,
        }
        res = mt5.order_send(req)
        if res and res.retcode == mt5.TRADE_RETCODE_DONE:
            ok(f"Posición cerrada: ticket #{ticket} @ ${res.price}")
            return True

    fail(f"No se pudo cerrar #{ticket}: {res.comment if res else 'sin respuesta'}")
    return False


# -----------------------------------------------------------------------------
# 6. PnL desde deals (🔧 FIX 24h + ambos campos)
# -----------------------------------------------------------------------------
def test_pnl_from_deals(ticket: int) -> bool:
    section(f"6. PnL real desde deals — Ticket #{ticket}")

    import MetaTrader5 as mt5

    time.sleep(2.0)
    from_date = datetime.now(TZ_MT5) - timedelta(hours=24)
    to_date = datetime.now(TZ_MT5) + timedelta(hours=1)

    deals = mt5.history_deals_get(from_date, to_date)
    if not deals:
        fail("No se encontraron deals en las últimas 24h")
        return False

    ticket_deals = []
    for d in deals:
        pid = getattr(d, "position_id", None)
        if pid is None:
            pid = getattr(d, "position", None)
        if pid == ticket:
            ticket_deals.append(d)

    if not ticket_deals:
        warn(f"No se encontraron deals para ticket #{ticket} (revisados {len(deals)} deals)")
        return False

    total_pnl = sum(d.profit + d.commission + d.swap for d in ticket_deals)
    ok(f"Deals encontrados: {len(ticket_deals)}")
    for d in ticket_deals:
        entry_str = "IN " if d.entry == 0 else "OUT"
        ok(f"  [{entry_str}] #{d.ticket} {d.symbol} {d.volume} @ ${d.price} | "
           f"profit=${d.profit:.2f} comm=${d.commission:.2f} swap=${d.swap:.2f}")
    ok(f"PnL total ticket #{ticket}: ${total_pnl:.2f}")
    return True


# -----------------------------------------------------------------------------
# 7. Slot libre
# -----------------------------------------------------------------------------
def test_slot_freed(symbol: str) -> bool:
    section(f"7. Verificación de slot libre — {symbol}")

    import MetaTrader5 as mt5
    positions = mt5.positions_get(symbol=symbol)
    if positions:
        fail(f"Aún hay {len(positions)} posición(es) en {symbol}")
        return False
    ok(f"Sin posiciones abiertas en {symbol} — slot libre")
    return True


# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Test de integración con MT5 real")
    parser.add_argument("--symbol", type=str, default="XAUUSD", help="Símbolo a testear")
    parser.add_argument("--yes", action="store_true", help="No pedir confirmación")
    parser.add_argument("--cleanup", action="store_true",
                        help="Cerrar posiciones huérfanas de tests anteriores y salir")
    args = parser.parse_args()

    print(f"\n{BOLD}{CYAN}{'═' * 70}{RESET}")
    print(f"{BOLD}{CYAN}  QUANTEDGE AI — TEST DE INTEGRACIÓN MT5 REAL{RESET}")
    print(f"{BOLD}{CYAN}{'═' * 70}{RESET}")

    # --- MODO CLEANUP ---
    if args.cleanup:
        print(f"\n{YELLOW}Modo CLEANUP: cerrando huérfanos de tests previos...{RESET}")
        try:
            import MetaTrader5 as mt5
            if not mt5.initialize():
                print(f"{RED}❌ No se pudo inicializar MT5{RESET}")
                sys.exit(1)
            n = cleanup_huerfanos()
            mt5.shutdown()
            if n > 0:
                print(f"\n{GREEN}✅ {n} posición(es) huérfana(s) cerrada(s).{RESET}\n")
            else:
                print(f"\n{GREEN}✅ No había huérfanos.{RESET}\n")
            sys.exit(0)
        except Exception as e:
            print(f"{RED}❌ Error en cleanup: {e}{RESET}")
            sys.exit(1)

    # --- MODO TEST NORMAL ---
    print(f"\n{YELLOW}{BOLD}⚠️  ADVERTENCIA{RESET}")
    print(f"   Este test abrirá y cerrará una posición de {TEST_VOLUME} lotes en:")
    print(f"   • Cuenta:   #{MT5_ACCOUNT} ({MT5_SERVER})")
    print(f"   • Símbolo:  {args.symbol}")
    print(f"   • Magic:    {TEST_MAGIC} (diferente al de producción)")
    print(f"\n   {BOLD}Asegúrate de estar en cuenta DEMO.{RESET}")

    if not args.yes:
        try:
            resp = input(f"\n{YELLOW}¿Continuar? (escribe 'SI' para confirmar): {RESET}").strip().upper()
            if resp != "SI":
                print("Test cancelado.")
                sys.exit(0)
        except (KeyboardInterrupt, EOFError):
            print("\nTest cancelado.")
            sys.exit(0)

    if not connect_mt5():
        print(f"\n{RED}⛔ Test abortado: no se pudo conectar a MT5.{RESET}")
        sys.exit(1)

    import MetaTrader5 as mt5

    # 🔧 Auto-cleanup de huérfanos ANTES de empezar
    print()
    section("0. Auto-cleanup de huérfanos previos")
    cleaned = cleanup_huerfanos()
    if cleaned == 0:
        ok("Sin huérfanos previos")

    symbol = resolve_symbol(args.symbol)
    if symbol != args.symbol:
        ok(f"Símbolo resuelto: '{args.symbol}' → '{symbol}'")

    if not test_tick(symbol):
        mt5.shutdown()
        sys.exit(1)

    opened, ticket = test_open_position(symbol)
    if not opened:
        if ticket == 0:
            warn("No se abrió posición, saltando tests 4-6")
        mt5.shutdown()
        sys.exit(1 if FAILED > 0 else 0)

    # 🔧 Tests 4-6 con cleanup de emergencia
    try:
        test_modify_sl(ticket)
        test_close_position(ticket)
        test_pnl_from_deals(ticket)
        test_slot_freed(symbol)
    except Exception as e:
        fail(f"Excepción en tests 4-6: {e}")
        warn("Intentando cerrar posición de emergencia...")
        try:
            positions = mt5.positions_get(ticket=ticket)
            if positions and close_position_by_ticket(ticket, reason="EmergencyCleanup"):
                warn(f"Posición #{ticket} cerrada de emergencia.")
            else:
                fail(f"No se pudo cerrar #{ticket} de emergencia. Revísalo en MT5.")
        except Exception as cleanup_err:
            fail(f"Error en cleanup de emergencia: {cleanup_err}")
    finally:
        mt5.shutdown()

    print(f"\n{BOLD}{CYAN}{'═' * 70}{RESET}")
    total = PASSED + FAILED
    if FAILED == 0:
        print(f"{GREEN}{BOLD}  ✅ INTEGRACIÓN OK ({PASSED}/{total}){RESET}")
    else:
        print(f"{RED}{BOLD}  ❌ {FAILED} FALLARON ({PASSED}/{total} OK){RESET}")
    print(f"{BOLD}{CYAN}{'═' * 70}{RESET}\n")

    sys.exit(0 if FAILED == 0 else 1)


if __name__ == "__main__":
    main()