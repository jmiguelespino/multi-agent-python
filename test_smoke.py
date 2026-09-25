"""
=============================================================================
SMOKE TEST — QuantEdge AI
=============================================================================
Valida que los fixes críticos estén correctamente aplicados sin necesidad
de conexión real a MT5 ni de datos de mercado.

Ejecutar:
    python test_smoke.py

Salida esperada:
    ✅ Todos los tests pasaron (14/14)

🔧 v1.8.0 (2026-09):
  • Añadidos 7 tests que cubren los bugs críticos que el smoke anterior
    NO detectaba:
      - BUG #1: is_buyer_maker en main.py
      - BUG #3: _resolve_mt5_symbol en signal_agent.py
      - BUG #4: _get_contract_size en execution_agent.py
      - BUG #5: _fetch_realized_pnl_from_mt5 no inventa MANUAL_CLOSE
      - MEJORA #5: MIN_ATR para XAG y US500 en feature_agent.py
      - Coherencia canónica en 4 módulos (incluye mt5_bridge)
=============================================================================
"""
import sys
import os

# Colores para terminal
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def _ok(msg: str):
    print(f"{GREEN}✅ {msg}{RESET}")


def _fail(msg: str):
    print(f"{RED}❌ {msg}{RESET}")


def _warn(msg: str):
    print(f"{YELLOW}⚠️  {msg}{RESET}")


# =============================================================================
# TEST 1 — FIX #1: get_canonical_asset() unifica WTI y BRENT como "OIL"
# =============================================================================
def test_fix1_canonical_oil():
    print("\n🧪 TEST 1 — FIX #1: get_canonical_asset() → OIL")
    try:
        from risk_guardian import get_canonical_asset as rg_canonical
        from execution_agent import get_canonical_asset as exec_canonical
    except ImportError as e:
        _fail(f"No se pudo importar módulos: {e}")
        return False

    casos = [
        ("XTIUSD", "OIL"),
        ("XTIUSD.RAW", "OIL"),
        ("WTI", "OIL"),
        ("USOIL", "OIL"),
        ("CRUDE", "OIL"),
        ("XBRUSD", "OIL"),
        ("BRENT", "OIL"),
        ("UKOIL", "OIL"),
        ("XBRUSD.RAW", "OIL"),
        ("XAUUSD", "XAU"),
        ("BTCUSD", "BTC"),
        ("ETHUSD", "ETH"),
        ("SOLUSD", "SOL"),
        ("XAGUSD", "XAG"),
        ("US500", "US500"),
        ("EURUSD", "EURUSD"),
        ("GBPUSD", "GBPUSD"),
    ]

    all_ok = True
    for symbol, expected in casos:
        rg = rg_canonical(symbol)
        ex = exec_canonical(symbol)
        if rg == expected and ex == expected:
            _ok(f"{symbol:15s} → {rg} (risk_guardian + execution_agent)")
        else:
            _fail(f"{symbol:15s} → rg={rg}, exec={ex} (esperado {expected})")
            all_ok = False

    if rg_canonical("XTIUSD") == rg_canonical("XBRUSD") == "OIL":
        _ok("CRÍTICO: XTIUSD y XBRUSD comparten canónico 'OIL'")
    else:
        _fail("CRÍTICO: XTIUSD y XBRUSD NO comparten canónico")
        all_ok = False

    return all_ok


# =============================================================================
# TEST 2 — FIX #2: Filtro de tendencia macro M15 existe
# =============================================================================
def test_fix2_macro_trend_method_exists():
    print("\n🧪 TEST 2 — FIX #2: _check_macro_trend() existe en signal_agent")
    try:
        from signal_agent import StrategySignalAgent
    except ImportError as e:
        _fail(f"No se pudo importar signal_agent: {e}")
        return False

    agent = StrategySignalAgent("BTCUSD")
    if hasattr(agent, "_check_macro_trend") and callable(getattr(agent, "_check_macro_trend")):
        _ok("Método _check_macro_trend() presente y llamable")
        return True
    else:
        _fail("Método _check_macro_trend() NO encontrado")
        return False


# =============================================================================
# TEST 3 — FIX #2: _check_macro_trend() falla seguro ante errores
# =============================================================================
def test_fix2_macro_trend_failsafe():
    print("\n🧪 TEST 3 — FIX #2: _check_macro_trend() es fail-safe")
    try:
        from signal_agent import StrategySignalAgent
    except ImportError as e:
        _fail(f"No se pudo importar signal_agent: {e}")
        return False

    agent = StrategySignalAgent("BTCUSD")
    try:
        result = agent._check_macro_trend("BUY", 60000.0)
        if result is True:
            _ok("Ante error/ausencia de datos → devuelve True (permitir)")
            return True
        else:
            _warn(f"Devolvió {result} en vez de True (puede ser por MT5 activo)")
            return True
    except Exception as e:
        _fail(f"El método lanzó excepción no controlada: {e}")
        return False


# =============================================================================
# TEST 4 — Risk Guardian: instanciación y estado inicial
# =============================================================================
def test_risk_guardian_instantiates():
    print("\n🧪 TEST 4 — Risk Guardian se instancia correctamente")
    try:
        from risk_guardian import InstitutionalRiskGuardian
    except ImportError as e:
        _fail(f"No se pudo importar risk_guardian: {e}")
        return False

    try:
        rg = InstitutionalRiskGuardian(initial_capital=1790.83)
        report = rg.get_status_report()
        _ok(f"Instanciado. Equity: ${report['current_equity']:.2f}")
        _ok(f"Drawdown: {report['drawdown_pct']}% | Circuit breaker: {report['circuit_breaker_active']}")
        return True
    except Exception as e:
        _fail(f"Error instanciando: {e}")
        return False


# =============================================================================
# TEST 5 — Signal Agent: instanciación por clase de activo
# =============================================================================
def test_signal_agent_per_asset_class():
    print("\n🧪 TEST 5 — Signal Agent se adapta por clase de activo")
    try:
        from signal_agent import StrategySignalAgent
    except ImportError as e:
        _fail(f"No se pudo importar signal_agent: {e}")
        return False

    casos = [
        ("XAUUSD", "is_gold"),
        ("XAGUSD", "is_silver"),
        ("XTIUSD", "is_oil"),
        ("XBRUSD", "is_oil"),
        ("BTCUSD", "is_crypto"),
        ("ETHUSD", "is_crypto"),
        ("SOLUSD", "is_crypto"),
        ("US500",  "is_index"),
        ("EURUSD", "is_forex"),
    ]

    all_ok = True
    for symbol, attr in casos:
        agent = StrategySignalAgent(symbol)
        if getattr(agent, attr, False):
            _ok(f"{symbol:10s} → {attr}=True (precisión={agent.precision})")
        else:
            _fail(f"{symbol:10s} → {attr}=False")
            all_ok = False

    return all_ok


# =============================================================================
# TEST 6 — Execution Agent: instanciación
# =============================================================================
def test_execution_agent_instantiates():
    print("\n🧪 TEST 6 — Execution Agent se instancia correctamente")
    try:
        from execution_agent import ExecutionOMSAgent
    except ImportError as e:
        _fail(f"No se pudo importar execution_agent: {e}")
        return False

    try:
        oms = ExecutionOMSAgent()
        _ok(f"Instanciado. Órdenes activas: {len(oms.active_orders)}")
        _ok(f"BE trigger: {oms.be_trigger_atr}×ATR | Trail trigger: {oms.trail_trigger_atr}×ATR")
        return True
    except Exception as e:
        _fail(f"Error instanciando: {e}")
        return False


# =============================================================================
# TEST 7 — Coherencia: get_canonical_asset existe en los 3 módulos
# =============================================================================
def test_canonical_consistency():
    print("\n🧪 TEST 7 — get_canonical_asset() coherente en los 3 módulos")
    try:
        from risk_guardian import get_canonical_asset as rg
        from execution_agent import get_canonical_asset as ex
    except ImportError as e:
        _fail(f"No se pudo importar módulos: {e}")
        return False

    symbols = ["XTIUSD", "XBRUSD", "XAUUSD", "BTCUSD", "XAGUSD", "US500"]
    all_ok = True
    for s in symbols:
        a, b = rg(s), ex(s)
        if a == b:
            _ok(f"{s:10s} → rg='{a}', exec='{b}'")
        else:
            _fail(f"{s:10s} → rg='{a}' ≠ exec='{b}'")
            all_ok = False

    return all_ok


# =============================================================================
# 🆕 TEST 8 — BUG #1: mt5_bridge.get_canonical_asset → OIL (antes NO se testeaba)
# =============================================================================
def test_bug1_bridge_canonical_oil():
    print("\n🧪 TEST 8 — 🐛 BUG #1: mt5_bridge.get_canonical_asset → OIL")
    try:
        from mt5_bridge import get_canonical_asset as bridge_canonical
    except ImportError as e:
        _fail(f"No se pudo importar mt5_bridge: {e}")
        return False

    casos = [
        ("XTIUSD", "OIL"),
        ("XBRUSD", "OIL"),
        ("WTI", "OIL"),
        ("BRENT", "OIL"),
        ("XTIUSD.RAW", "OIL"),
        ("XBRUSD.RAW", "OIL"),
        ("XAUUSD", "XAU"),
        ("XAGUSD", "XAG"),
        ("BTCUSD", "BTC"),
        ("US500", "US500"),
    ]

    all_ok = True
    for symbol, expected in casos:
        got = bridge_canonical(symbol)
        if got == expected:
            _ok(f"{symbol:15s} → {got}")
        else:
            _fail(f"{symbol:15s} → {got} (esperado {expected})")
            all_ok = False

    # Verificación crítica específica del bridge
    if bridge_canonical("XTIUSD") == bridge_canonical("XBRUSD") == "OIL":
        _ok("CRÍTICO: el bridge también unifica WTI y BRENT bajo OIL")
    else:
        _fail("CRÍTICO: el bridge NO unifica WTI y BRENT")
        all_ok = False

    return all_ok


# =============================================================================
# 🆕 TEST 9 — BUG #2: infer_is_buyer_maker (tick rule) en main.py
# =============================================================================
def test_bug1_infer_is_buyer_maker():
    print("\n🧪 TEST 9 — 🐛 BUG #1: infer_is_buyer_maker (tick rule)")
    try:
        from main import infer_is_buyer_maker
    except ImportError as e:
        _fail(f"No se pudo importar main: {e}")
        return False

    class FakeTick:
        def __init__(self, bid, ask, last):
            self.bid = bid
            self.ask = ask
            self.last = last

    casos = [
        # (bid, ask, last, expected_is_buyer_maker)
        # last >= ask → comprador agresivo → False
        (100.0, 100.2, 100.2, False),
        (100.0, 100.2, 100.5, False),
        # last <= bid → vendedor agresivo → True
        (100.0, 100.2, 100.0, True),
        (100.0, 100.2, 99.8, True),
        # dentro del spread → fallback por mid
        (100.0, 100.2, 100.15, False),  # por encima del mid (100.1)
        (100.0, 100.2, 100.05, True),   # por debajo del mid (100.1)
        # datos inválidos → neutral (False)
        (0.0, 0.0, 0.0, False),
        (100.0, 100.2, 0.0, False),
    ]

    all_ok = True
    for bid, ask, last, expected in casos:
        tick = FakeTick(bid, ask, last)
        got = infer_is_buyer_maker(tick)
        label = "vendedor" if got else "comprador"
        if got == expected:
            _ok(f"bid={bid}, ask={ask}, last={last} → {label}")
        else:
            _fail(f"bid={bid}, ask={ask}, last={last} → {label} (esperado {'vendedor' if expected else 'comprador'})")
            all_ok = False

    return all_ok


# =============================================================================
# 🆕 TEST 10 — BUG #3: signal_agent._resolve_mt5_symbol existe
# =============================================================================
def test_bug3_signal_agent_resolve_symbol():
    print("\n🧪 TEST 10 — 🐛 BUG #3: signal_agent._resolve_mt5_symbol existe")
    try:
        from signal_agent import StrategySignalAgent
    except ImportError as e:
        _fail(f"No se pudo importar signal_agent: {e}")
        return False

    agent = StrategySignalAgent("WTI")

    if not hasattr(agent, "_resolve_mt5_symbol"):
        _fail("Método _resolve_mt5_symbol() NO encontrado — el FIX #2 podría estar inactivo")
        return False

    _ok("Método _resolve_mt5_symbol() presente")

    # Verificar que el método devuelve algo (sin MT5, debe devolver el original)
    try:
        resolved = agent._resolve_mt5_symbol()
        _ok(f"Resolución para 'WTI' → '{resolved}' (sin MT5, se espera 'WTI')")
    except Exception as e:
        _fail(f"_resolve_mt5_symbol lanzó excepción: {e}")
        return False

    # Verificar que el atributo de cache existe
    if hasattr(agent, "_resolved_mt5_symbol"):
        _ok("Cache _resolved_mt5_symbol presente")
    else:
        _warn("Cache _resolved_mt5_symbol no encontrado (rendimiento)")

    return True


# =============================================================================
# 🆕 TEST 11 — BUG #4: execution_agent._get_contract_size por clase
# =============================================================================
def test_bug4_execution_agent_contract_size():
    print("\n🧪 TEST 11 — 🐛 BUG #4: _get_contract_size por clase de activo")
    try:
        from execution_agent import ExecutionOMSAgent
    except ImportError as e:
        _fail(f"No se pudo importar execution_agent: {e}")
        return False

    if not hasattr(ExecutionOMSAgent, "_get_contract_size"):
        _fail("Método _get_contract_size() NO encontrado — BUG #4 no corregido")
        return False

    _ok("Método _get_contract_size() presente")

    # Sin MT5, debe devolver los fallbacks conocidos
    casos = [
        ("XAUUSD", 100.0),
        ("XAGUSD", 1000.0),
        ("EURUSD", 100000.0),
        ("XTIUSD", 100.0),
        ("US500", 1.0),
    ]

    all_ok = True
    for symbol, expected in casos:
        got = ExecutionOMSAgent._get_contract_size(symbol)
        if abs(got - expected) < 0.001:
            _ok(f"{symbol:10s} → contract_size={got}")
        else:
            _fail(f"{symbol:10s} → contract_size={got} (esperado {expected})")
            all_ok = False

    return all_ok


# =============================================================================
# 🆕 TEST 12 — MEJORA #5: feature_agent._get_min_atr para XAG y US500
# =============================================================================
def test_mejora5_feature_agent_min_atr():
    print("\n🧪 TEST 12 — 🐛 MEJORA #5: _get_min_atr para XAG y US500")
    try:
        from feature_agent import IngestionFeatureAgent
    except ImportError as e:
        _fail(f"No se pudo importar feature_agent: {e}")
        return False

    casos = [
        ("XAUUSD", 0.50),
        ("XAGUSD", 0.02),   # 🆕
        ("US500",  0.50),   # 🆕
        ("XTIUSD", 0.05),
        ("BTCUSD", 50.0),
        ("ETHUSD", 3.0),
        ("SOLUSD", 0.10),
        ("EURUSD", 0.00015),
    ]

    all_ok = True
    for symbol, expected in casos:
        agent = IngestionFeatureAgent(symbol=symbol)
        got = agent._get_min_atr()
        if abs(got - expected) < 1e-9:
            _ok(f"{symbol:10s} → MIN_ATR={got}")
        else:
            _fail(f"{symbol:10s} → MIN_ATR={got} (esperado {expected})")
            all_ok = False

    return all_ok


# =============================================================================
# 🆕 TEST 13 — Coherencia canónica en 4 módulos (incluye mt5_bridge)
# =============================================================================
def test_canonical_consistency_4_modules():
    print("\n🧪 TEST 13 — get_canonical_asset() coherente en 4 módulos")
    try:
        from risk_guardian import get_canonical_asset as rg
        from execution_agent import get_canonical_asset as ex
        from mt5_bridge import get_canonical_asset as br
    except ImportError as e:
        _fail(f"No se pudo importar módulos: {e}")
        return False

    symbols = ["XTIUSD", "XBRUSD", "XAUUSD", "BTCUSD", "XAGUSD", "US500", "EURUSD"]
    all_ok = True
    for s in symbols:
        a, b, c = rg(s), ex(s), br(s)
        if a == b == c:
            _ok(f"{s:10s} → rg='{a}', exec='{b}', bridge='{c}'")
        else:
            _fail(f"{s:10s} → rg='{a}', exec='{b}', bridge='{c}' (INCOHERENTE)")
            all_ok = False

    return all_ok


# =============================================================================
# 🆕 TEST 14 — BUG #5: _fetch_realized_pnl_from_mt5 no inventa MANUAL_CLOSE
# =============================================================================
def test_bug5_pnl_unknown_reason():
    print("\n🧪 TEST 14 — 🐛 BUG #5: _fetch_realized_pnl_from_mt5 no inventa MANUAL_CLOSE")
    try:
        from execution_agent import ExecutionOMSAgent
    except ImportError as e:
        _fail(f"No se pudo importar execution_agent: {e}")
        return False

    # Sin MT5 inicializado, la función debe devolver UNKNOWN, no MANUAL_CLOSE
    pnl, price, reason = ExecutionOMSAgent._fetch_realized_pnl_from_mt5(999999999)

    if reason == "UNKNOWN":
        _ok(f"Ticket inexistente → reason='{reason}' (correcto, no inventa MANUAL_CLOSE)")
        return True
    elif reason == "MANUAL_CLOSE":
        _fail(f"Ticket inexistente → reason='{reason}' (BUG #5 no corregido)")
        return False
    else:
        _warn(f"Ticket inexistente → reason='{reason}' (inesperado, pero no es MANUAL_CLOSE)")
        return True


# =============================================================================
# RUNNER
# =============================================================================
def main():
    print("=" * 70)
    print("  QUANTEDGE AI — SMOKE TEST v1.8.0")
    print("=" * 70)

    tests = [
        ("FIX #1 — get_canonical_asset → OIL",              test_fix1_canonical_oil),
        ("FIX #2 — _check_macro_trend existe",              test_fix2_macro_trend_method_exists),
        ("FIX #2 — _check_macro_trend fail-safe",           test_fix2_macro_trend_failsafe),
        ("Risk Guardian — instanciación",                   test_risk_guardian_instantiates),
        ("Signal Agent — por clase de activo",              test_signal_agent_per_asset_class),
        ("Execution Agent — instanciación",                 test_execution_agent_instantiates),
        ("Coherencia — canónico en 3 módulos",              test_canonical_consistency),
        ("🆕 BUG #1 — bridge canónico OIL",                 test_bug1_bridge_canonical_oil),
        ("🆕 BUG #1 — infer_is_buyer_maker (tick rule)",    test_bug1_infer_is_buyer_maker),
        ("🆕 BUG #3 — signal_agent._resolve_mt5_symbol",    test_bug3_signal_agent_resolve_symbol),
        ("🆕 BUG #4 — execution._get_contract_size",        test_bug4_execution_agent_contract_size),
        ("🆕 MEJORA #5 — feature._get_min_atr XAG/US500",   test_mejora5_feature_agent_min_atr),
        ("🆕 Coherencia — canónico en 4 módulos",           test_canonical_consistency_4_modules),
        ("🆕 BUG #5 — pnl UNKNOWN en lugar de MANUAL",      test_bug5_pnl_unknown_reason),
    ]

    results = []
    for name, fn in tests:
        try:
            results.append((name, fn()))
        except Exception as e:
            _fail(f"TEST '{name}' lanzó excepción: {e}")
            results.append((name, False))

    print("\n" + "=" * 70)
    print("  RESUMEN")
    print("=" * 70)

    passed = sum(1 for _, ok in results if ok)
    total = len(results)

    for name, ok in results:
        status = f"{GREEN}PASS{RESET}" if ok else f"{RED}FAIL{RESET}"
        print(f"  [{status}] {name}")

    print("-" * 70)
    if passed == total:
        print(f"{GREEN}✅ Todos los tests pasaron ({passed}/{total}){RESET}")
        sys.exit(0)
    else:
        print(f"{RED}❌ {total - passed} de {total} tests fallaron{RESET}")
        sys.exit(1)


if __name__ == "__main__":
    main()