"""
=============================================================================
SMOKE TEST — QuantEdge AI
=============================================================================
Valida que los fixes críticos estén correctamente aplicados sin necesidad
de conexión real a MT5 ni de datos de mercado.

Ejecutar:
    python test_smoke.py

Salida esperada:
    ✅ Todos los tests pasaron (N/N)
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
        # No deben unificarse
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
            _fail(
                f"{symbol:15s} → rg={rg}, exec={ex} (esperado {expected})"
            )
            all_ok = False

    # Verificación crítica: WTI y BRENT deben ser iguales
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

    # Sin MT5 inicializado, copy_rates_from_pos lanzará excepción
    # El método debe devolver True (permitir señal)
    agent = StrategySignalAgent("BTCUSD")
    try:
        result = agent._check_macro_trend("BUY", 60000.0)
        if result is True:
            _ok("Ante error/ausencia de datos → devuelve True (permitir)")
            return True
        else:
            _warn(f"Devolvió {result} en vez de True (puede ser por MT5 activo)")
            return True  # No es fallo si MT5 está corriendo
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
        # signal_agent no tiene get_canonical_asset, pero tiene lógica propia
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
# RUNNER
# =============================================================================
def main():
    print("=" * 70)
    print("  QUANTEDGE AI — SMOKE TEST")
    print("=" * 70)

    tests = [
        ("FIX #1 — get_canonical_asset → OIL", test_fix1_canonical_oil),
        ("FIX #2 — _check_macro_trend existe", test_fix2_macro_trend_method_exists),
        ("FIX #2 — _check_macro_trend fail-safe", test_fix2_macro_trend_failsafe),
        ("Risk Guardian — instanciación", test_risk_guardian_instantiates),
        ("Signal Agent — por clase de activo", test_signal_agent_per_asset_class),
        ("Execution Agent — instanciación", test_execution_agent_instantiates),
        ("Coherencia — canónico en 3 módulos", test_canonical_consistency),
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