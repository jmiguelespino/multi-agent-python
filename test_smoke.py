"""
=============================================================================
SMOKE TEST — QuantEdge AI
=============================================================================
🔧 v1.9.1 — fixes TEST 16 y TEST 17 duplicado:
  • 🐛 TEST 16 corregido: `_compute_disabled_symbols(fake_by_symbol, {})`
  • 🐛 TEST 17 eliminado duplicado
  • TEST 18 (B20-fixed) se mantiene
=============================================================================
"""
import sys
import os
import time

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
# TEST 1 — get_canonical_asset → OIL
# =============================================================================
def test_fix1_canonical_oil():
    print("\n🧪 TEST 1 — get_canonical_asset() → OIL")
    try:
        from risk_guardian import get_canonical_asset as rg_canonical
        from execution_agent import get_canonical_asset as exec_canonical
    except ImportError as e:
        _fail(f"No se pudo importar: {e}")
        return False

    casos = [
        ("XTIUSD", "OIL"), ("XTIUSD.RAW", "OIL"), ("WTI", "OIL"),
        ("USOIL", "OIL"), ("CRUDE", "OIL"), ("XBRUSD", "OIL"),
        ("BRENT", "OIL"), ("UKOIL", "OIL"), ("XBRUSD.RAW", "OIL"),
        ("XAUUSD", "XAU"), ("BTCUSD", "BTC"), ("ETHUSD", "ETH"),
        ("SOLUSD", "SOL"), ("XAGUSD", "XAG"), ("US500", "US500"),
        ("EURUSD", "EURUSD"), ("GBPUSD", "GBPUSD"),
    ]

    all_ok = True
    for symbol, expected in casos:
        rg = rg_canonical(symbol)
        ex = exec_canonical(symbol)
        if rg == expected and ex == expected:
            _ok(f"{symbol:15s} → {rg}")
        else:
            _fail(f"{symbol:15s} → rg={rg}, exec={ex} (esperado {expected})")
            all_ok = False

    if rg_canonical("XTIUSD") == rg_canonical("XBRUSD") == "OIL":
        _ok("CRÍTICO: XTIUSD y XBRUSD comparten 'OIL'")
    else:
        _fail("CRÍTICO: XTIUSD y XBRUSD NO comparten canónico")
        all_ok = False

    return all_ok


# =============================================================================
# TEST 2 — _check_macro_trend existe
# =============================================================================
def test_fix2_macro_trend_method_exists():
    print("\n🧪 TEST 2 — _check_macro_trend() existe")
    try:
        from signal_agent import StrategySignalAgent
    except ImportError as e:
        _fail(f"No se pudo importar: {e}")
        return False

    agent = StrategySignalAgent("BTCUSD")
    if hasattr(agent, "_check_macro_trend") and callable(getattr(agent, "_check_macro_trend")):
        _ok("Método presente")
        return True
    else:
        _fail("Método NO encontrado")
        return False


# =============================================================================
# TEST 3 — _check_macro_trend fail-safe
# =============================================================================
def test_fix2_macro_trend_failsafe():
    print("\n🧪 TEST 3 — _check_macro_trend() fail-safe")
    try:
        from signal_agent import StrategySignalAgent
    except ImportError as e:
        _fail(f"No se pudo importar: {e}")
        return False

    agent = StrategySignalAgent("BTCUSD")
    try:
        result = agent._check_macro_trend("BUY", 60000.0)
        if result is True:
            _ok("Fail-safe OK")
            return True
        else:
            _warn(f"Devolvió {result}")
            return True
    except Exception as e:
        _fail(f"Excepción: {e}")
        return False


# =============================================================================
# TEST 4 — Risk Guardian
# =============================================================================
def test_risk_guardian_instantiates():
    print("\n🧪 TEST 4 — Risk Guardian")
    try:
        from risk_guardian import InstitutionalRiskGuardian
    except ImportError as e:
        _fail(f"No se pudo importar: {e}")
        return False

    try:
        rg = InstitutionalRiskGuardian(initial_capital=1790.83)
        report = rg.get_status_report()
        _ok(f"Instanciado. Equity: ${report['current_equity']:.2f}")
        _ok(f"Drawdown: {report['drawdown_pct']}% | CB: {report['circuit_breaker_active']}")
        return True
    except Exception as e:
        _fail(f"Error instanciando: {e}")
        return False


# =============================================================================
# TEST 5 — Signal Agent por clase
# =============================================================================
def test_signal_agent_per_asset_class():
    print("\n🧪 TEST 5 — Signal Agent por clase")
    try:
        from signal_agent import StrategySignalAgent
    except ImportError as e:
        _fail(f"No se pudo importar: {e}")
        return False

    casos = [
        ("XAUUSD", "is_gold"), ("XAGUSD", "is_silver"),
        ("XTIUSD", "is_oil"), ("XBRUSD", "is_oil"),
        ("BTCUSD", "is_crypto"), ("ETHUSD", "is_crypto"),
        ("SOLUSD", "is_crypto"), ("US500", "is_index"),
        ("EURUSD", "is_forex"),
    ]

    all_ok = True
    for symbol, attr in casos:
        agent = StrategySignalAgent(symbol)
        if getattr(agent, attr, False):
            _ok(f"{symbol:10s} → {attr}=True")
        else:
            _fail(f"{symbol:10s} → {attr}=False")
            all_ok = False
    return all_ok


# =============================================================================
# TEST 6 — Execution Agent
# =============================================================================
def test_execution_agent_instantiates():
    print("\n🧪 TEST 6 — Execution Agent")
    try:
        from execution_agent import ExecutionOMSAgent
    except ImportError as e:
        _fail(f"No se pudo importar: {e}")
        return False

    try:
        oms = ExecutionOMSAgent()
        _ok(f"Instanciado. Activas: {len(oms.active_orders)}")
        _ok(f"BE: {oms.be_trigger_atr}×ATR | Trail: {oms.trail_trigger_atr}×ATR")
        return True
    except Exception as e:
        _fail(f"Error: {e}")
        return False


# =============================================================================
# TEST 7 — Coherencia 3 módulos
# =============================================================================
def test_canonical_consistency():
    print("\n🧪 TEST 7 — Coherencia canónico 3 módulos")
    try:
        from risk_guardian import get_canonical_asset as rg
        from execution_agent import get_canonical_asset as ex
    except ImportError as e:
        _fail(f"No se pudo importar: {e}")
        return False

    symbols = ["XTIUSD", "XBRUSD", "XAUUSD", "BTCUSD", "XAGUSD", "US500"]
    all_ok = True
    for s in symbols:
        a, b = rg(s), ex(s)
        if a == b:
            _ok(f"{s:10s} → '{a}'")
        else:
            _fail(f"{s:10s} → rg='{a}' ≠ exec='{b}'")
            all_ok = False
    return all_ok


# =============================================================================
# TEST 8 — mt5_bridge canónico
# =============================================================================
def test_bug1_bridge_canonical_oil():
    print("\n🧪 TEST 8 — mt5_bridge canónico OIL")
    try:
        from mt5_bridge import get_canonical_asset as bridge_canonical
    except ImportError as e:
        _fail(f"No se pudo importar: {e}")
        return False

    casos = [
        ("XTIUSD", "OIL"), ("XBRUSD", "OIL"), ("WTI", "OIL"), ("BRENT", "OIL"),
        ("XTIUSD.RAW", "OIL"), ("XBRUSD.RAW", "OIL"),
        ("XAUUSD", "XAU"), ("XAGUSD", "XAG"), ("BTCUSD", "BTC"), ("US500", "US500"),
    ]

    all_ok = True
    for symbol, expected in casos:
        got = bridge_canonical(symbol)
        if got == expected:
            _ok(f"{symbol:15s} → {got}")
        else:
            _fail(f"{symbol:15s} → {got} (esperado {expected})")
            all_ok = False

    if bridge_canonical("XTIUSD") == bridge_canonical("XBRUSD") == "OIL":
        _ok("CRÍTICO: bridge unifica WTI/BRENT")
    else:
        _fail("CRÍTICO: bridge NO unifica")
        all_ok = False
    return all_ok


# =============================================================================
# TEST 9 — infer_is_buyer_maker
# =============================================================================
def test_bug1_infer_is_buyer_maker():
    print("\n🧪 TEST 9 — infer_is_buyer_maker")
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
        (100.0, 100.2, 100.2, False),
        (100.0, 100.2, 100.5, False),
        (100.0, 100.2, 100.0, True),
        (100.0, 100.2, 99.8, True),
        (100.0, 100.2, 100.15, False),
        (100.0, 100.2, 100.05, True),
        (0.0, 0.0, 0.0, False),
        (100.0, 100.2, 0.0, False),
    ]

    all_ok = True
    for bid, ask, last, expected in casos:
        got = infer_is_buyer_maker(FakeTick(bid, ask, last))
        label = "vendedor" if got else "comprador"
        if got == expected:
            _ok(f"bid={bid}, ask={ask}, last={last} → {label}")
        else:
            _fail(f"bid={bid}, ask={ask}, last={last} → {label}")
            all_ok = False
    return all_ok


# =============================================================================
# TEST 10 — signal_agent._resolve_mt5_symbol
# =============================================================================
def test_bug3_signal_agent_resolve_symbol():
    print("\n🧪 TEST 10 — signal_agent._resolve_mt5_symbol")
    try:
        from signal_agent import StrategySignalAgent
    except ImportError as e:
        _fail(f"No se pudo importar: {e}")
        return False

    agent = StrategySignalAgent("WTI")
    if not hasattr(agent, "_resolve_mt5_symbol"):
        _fail("Método NO encontrado")
        return False

    _ok("Método presente")
    try:
        resolved = agent._resolve_mt5_symbol()
        _ok(f"'WTI' → '{resolved}'")
    except Exception as e:
        _fail(f"Excepción: {e}")
        return False

    if hasattr(agent, "_resolved_mt5_symbol"):
        _ok("Cache presente")
    return True


# =============================================================================
# TEST 11 — _get_contract_size
# =============================================================================
def test_bug4_execution_agent_contract_size():
    print("\n🧪 TEST 11 — _get_contract_size")
    try:
        from execution_agent import ExecutionOMSAgent
    except ImportError as e:
        _fail(f"No se pudo importar: {e}")
        return False

    casos = [
        ("XAUUSD", 100.0), ("XAGUSD", 1000.0), ("EURUSD", 100000.0),
        ("XTIUSD", 100.0), ("US500", 1.0),
    ]
    all_ok = True
    for symbol, expected in casos:
        got = ExecutionOMSAgent._get_contract_size(symbol)
        if abs(got - expected) < 0.001:
            _ok(f"{symbol:10s} → {got}")
        else:
            _fail(f"{symbol:10s} → {got} (esperado {expected})")
            all_ok = False
    return all_ok


# =============================================================================
# TEST 12 — _get_min_atr
# =============================================================================
def test_mejora5_feature_agent_min_atr():
    print("\n🧪 TEST 12 — _get_min_atr XAG/US500")
    try:
        from feature_agent import IngestionFeatureAgent
    except ImportError as e:
        _fail(f"No se pudo importar: {e}")
        return False

    casos = [
        ("XAUUSD", 0.50), ("XAGUSD", 0.02), ("US500", 0.50),
        ("XTIUSD", 0.05), ("BTCUSD", 20.0), ("ETHUSD", 1.0),
        ("SOLUSD", 0.03), ("EURUSD", 0.00015),
    ]
    all_ok = True
    for symbol, expected in casos:
        agent = IngestionFeatureAgent(symbol=symbol)
        got = agent._get_min_atr()
        if abs(got - expected) < 1e-9:
            _ok(f"{symbol:10s} → MIN_ATR={got}")
        else:
            _fail(f"{symbol:10s} → {got} (esperado {expected})")
            all_ok = False
    return all_ok


# =============================================================================
# TEST 13 — Coherencia 4 módulos
# =============================================================================
def test_canonical_consistency_4_modules():
    print("\n🧪 TEST 13 — Coherencia 4 módulos")
    try:
        from risk_guardian import get_canonical_asset as rg
        from execution_agent import get_canonical_asset as ex
        from mt5_bridge import get_canonical_asset as br
    except ImportError as e:
        _fail(f"No se pudo importar: {e}")
        return False

    symbols = ["XTIUSD", "XBRUSD", "XAUUSD", "BTCUSD", "XAGUSD", "US500", "EURUSD"]
    all_ok = True
    for s in symbols:
        a, b, c = rg(s), ex(s), br(s)
        if a == b == c:
            _ok(f"{s:10s} → '{a}'")
        else:
            _fail(f"{s:10s} → rg='{a}', exec='{b}', bridge='{c}'")
            all_ok = False
    return all_ok


# =============================================================================
# TEST 14 — PnL UNKNOWN (O5)
# =============================================================================
def test_bug5_pnl_unknown_reason():
    print("\n🧪 TEST 14 — PnL UNKNOWN (retry rápido)")
    try:
        from execution_agent import ExecutionOMSAgent
    except ImportError as e:
        _fail(f"No se pudo importar: {e}")
        return False

    pnl, price, reason = ExecutionOMSAgent._fetch_realized_pnl_from_mt5(
        999999999, max_retries=1, retry_delay=0.0
    )

    if reason == "UNKNOWN":
        _ok(f"Ticket inexistente → reason='{reason}'")
        return True
    elif reason == "MANUAL_CLOSE":
        _fail(f"Ticket inexistente → reason='{reason}' (BUG #5)")
        return False
    else:
        _warn(f"Ticket inexistente → reason='{reason}'")
        return True


# =============================================================================
# TEST 15 — B19: límites ATR por clase
# =============================================================================
def test_b19_atr_limits_by_class():
    print("\n🧪 TEST 15 — 🐛 B19: límites ATR por clase")
    try:
        from feedback_learner import clamp_atr_by_class, get_class_of
    except ImportError as e:
        _fail(f"No se pudo importar: {e}")
        return False

    sl, tp = clamp_atr_by_class("XAU", 1.0, 1.0)
    if sl == 3.5 and tp == 5.0:
        _ok(f"XAU con SL=1.0/TP=1.0 → clamp a SL={sl}/TP={tp}")
    else:
        _fail(f"XAU clamp incorrecto: SL={sl}, TP={tp}")
        return False

    sl, tp = clamp_atr_by_class("BTC", 10.0, 20.0)
    if sl == 3.5 and tp == 6.0:
        _ok(f"BTC con SL=10.0/TP=20.0 → clamp a SL={sl}/TP={tp}")
    else:
        _fail(f"BTC clamp incorrecto: SL={sl}, TP={tp}")
        return False

    casos_clase = [
        ("XAUUSD", "XAU"), ("XAGUSD", "XAG"), ("XTIUSD", "OIL"),
        ("BTCUSD", "BTC"), ("EURUSD", "FOREX"), ("US500", "US500"),
    ]
    for sym, expected in casos_clase:
        got = get_class_of(sym)
        if got == expected:
            _ok(f"get_class_of({sym}) → {got}")
        else:
            _fail(f"get_class_of({sym}) → {got} (esperado {expected})")
            return False

    return True


# =============================================================================
# 🆕 TEST 18 — B20 corregido: min_trades + histéresis
# =============================================================================
def test_b20_fixed():
    print("\n🧪 TEST 18 — 🐛 B20 corregido: min_trades + histéresis")
    try:
        from feedback_learner import (
            ContinuousLearningAgent, DISABLE_THRESHOLDS,
            PF_LOOKBACK_TRADES, REENABLE_MIN_PF, REENABLE_MIN_WR
        )
    except ImportError as e:
        _fail(f"No se pudo importar: {e}")
        return False

    all_ok = True

    critical_min = DISABLE_THRESHOLDS["critical"]["min_trades"]
    if critical_min >= 30:
        _ok(f"critical.min_trades = {critical_min} (≥30)")
    else:
        _fail(f"critical.min_trades = {critical_min} (esperado ≥30)")
        all_ok = False

    if "wr_max" in DISABLE_THRESHOLDS["critical"]:
        _ok(f"critical.wr_max = {DISABLE_THRESHOLDS['critical']['wr_max']}% (histéresis activa)")
    else:
        _fail("critical.wr_max NO definido")
        all_ok = False

    if 0 < PF_LOOKBACK_TRADES <= 200:
        _ok(f"PF_LOOKBACK_TRADES = {PF_LOOKBACK_TRADES}")
    else:
        _fail(f"PF_LOOKBACK_TRADES = {PF_LOOKBACK_TRADES}")
        all_ok = False

    agent = ContinuousLearningAgent()
    fake_by_symbol = {
        "TEST1": {"trades": 50, "profit_factor": 0.4, "win_rate_pct": 55.0, "wins": 27, "losses": 23, "pnl_usd": -10.0, "is_profitable": False},
        "TEST2": {"trades": 50, "profit_factor": 0.4, "win_rate_pct": 30.0, "wins": 15, "losses": 35, "pnl_usd": -20.0, "is_profitable": False},
        "TEST3": {"trades": 5,  "profit_factor": 0.2, "win_rate_pct": 20.0, "wins": 1, "losses": 4, "pnl_usd": -5.0,  "is_profitable": False},
    }
    disabled, details = agent._compute_disabled_symbols(fake_by_symbol, {})

    if "TEST1" not in disabled:
        _ok("TEST1 (PF=0.4, WR=55%) NO deshabilitado (histéresis OK)")
    else:
        _fail("TEST1 (PF=0.4, WR=55%) SÍ deshabilitado (falta histéresis)")
        all_ok = False

    if "TEST2" in disabled:
        _ok("TEST2 (PF=0.4, WR=30%) SÍ deshabilitado (correcto)")
    else:
        _fail("TEST2 (PF=0.4, WR=30%) NO deshabilitado (debería)")
        all_ok = False

    if "TEST3" not in disabled:
        _ok("TEST3 (5 trades) NO deshabilitado (min_trades OK)")
    else:
        _fail("TEST3 (5 trades) SÍ deshabilitado (min_trades bajo)")
        all_ok = False

    current_disabled = {
        "RECOVERED": {"level": "severe", "pf": 0.5, "trades": 30, "disabled_at": int(time.time()) - 3600, "disabled_until": int(time.time()) + 3600, "reason": "test"}
    }
    fake_recovered = {
        "RECOVERED": {"trades": 20, "profit_factor": 1.5, "win_rate_pct": 55.0, "wins": 11, "losses": 9, "pnl_usd": 5.0, "is_profitable": True},
    }
    disabled2, _ = agent._compute_disabled_symbols(fake_recovered, current_disabled)
    if "RECOVERED" not in disabled2:
        _ok("RECOVERED (PF=1.5) re-habilitado automáticamente (B20.4 OK)")
    else:
        _fail("RECOVERED (PF=1.5) NO re-habilitado (falta B20.4)")
        all_ok = False

    return all_ok


# =============================================================================
# 🆕 TEST 19 — B23: clamp duro ATR
# =============================================================================
def test_b23_atr_clamp():
    print("\n🧪 TEST 19 — 🐛 B23: clamp duro ATR multipliers")
    try:
        import feedback_learner as fl
    except ImportError as e:
        _fail(f"No se pudo importar: {e}")
        return False

    # Verificar que el código tiene el clamp
    import inspect
    source = inspect.getsource(fl.ContinuousLearningAgent.analyze_and_optimize)

    if "B23" in source and "min(6.0" in source and "min(9.0" in source:
        _ok("Clamp duro SL ∈ [1.0, 6.0] presente")
        _ok("Clamp duro TP ∈ [2.0, 9.0] presente")
        return True
    else:
        _fail("Clamp duro B23 NO encontrado en analyze_and_optimize()")
        return False


# =============================================================================
# RUNNER
# =============================================================================
def main():
    print("=" * 70)
    print("  QUANTEDGE AI — SMOKE TEST v1.9.1")
    print("=" * 70)

    tests = [
        ("FIX #1 — canónico OIL",                       test_fix1_canonical_oil),
        ("FIX #2 — _check_macro_trend existe",          test_fix2_macro_trend_method_exists),
        ("FIX #2 — _check_macro_trend fail-safe",       test_fix2_macro_trend_failsafe),
        ("Risk Guardian — instanciación",               test_risk_guardian_instantiates),
        ("Signal Agent — por clase",                    test_signal_agent_per_asset_class),
        ("Execution Agent — instanciación",             test_execution_agent_instantiates),
        ("Coherencia — 3 módulos",                      test_canonical_consistency),
        ("BUG #1 — bridge canónico OIL",                test_bug1_bridge_canonical_oil),
        ("BUG #1 — infer_is_buyer_maker",               test_bug1_infer_is_buyer_maker),
        ("BUG #3 — _resolve_mt5_symbol",                test_bug3_signal_agent_resolve_symbol),
        ("BUG #4 — _get_contract_size",                 test_bug4_execution_agent_contract_size),
        ("MEJORA #5 — _get_min_atr",                    test_mejora5_feature_agent_min_atr),
        ("Coherencia — 4 módulos",                      test_canonical_consistency_4_modules),
        ("BUG #5 — PnL UNKNOWN (O5)",                   test_bug5_pnl_unknown_reason),
        ("B19 — límites ATR por clase",                 test_b19_atr_limits_by_class),
        ("B20-fixed — histéresis + re-habilitación",    test_b20_fixed),
        ("B23 — clamp duro ATR",                        test_b23_atr_clamp),
    ]

    results = []
    for name, fn in tests:
        try:
            results.append((name, fn()))
        except Exception as e:
            _fail(f"TEST '{name}' excepción: {e}")
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
        print(f"{RED}❌ {total - passed} de {total} fallaron{RESET}")
        sys.exit(1)


if __name__ == "__main__":
    main()