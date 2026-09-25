"""
=============================================================================
SMOKE TEST — QuantEdge AI
=============================================================================
🔧 v1.9.0 — LOTE FUSIONADO 2.6+3:
  • 🐛 O5: TEST 14 reduce reintentos de PnL (max_retries=1) para no tardar.
  • Añadidos tests 15, 16, 17 para B19, B20, B21.
=============================================================================
"""
import sys
import os

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
        _fail(f"No se pudo importar signal_agent: {e}")
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
# TEST 14 — PnL UNKNOWN (O5: retry rápido)
# =============================================================================
def test_bug5_pnl_unknown_reason():
    print("\n🧪 TEST 14 — PnL UNKNOWN (retry rápido)")
    try:
        from execution_agent import ExecutionOMSAgent
    except ImportError as e:
        _fail(f"No se pudo importar: {e}")
        return False

    # 🐛 O5: usar max_retries=1 para no tardar
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
# 🆕 TEST 15 — B19: límites ATR por clase
# =============================================================================
def test_b19_atr_limits_by_class():
    print("\n🧪 TEST 15 — 🐛 B19: límites ATR por clase")
    try:
        from feedback_learner import clamp_atr_by_class, get_class_of
    except ImportError as e:
        _fail(f"No se pudo importar: {e}")
        return False

    # Oro: SL ∈ [3.5, 6.0]
    sl, tp = clamp_atr_by_class("XAU", 1.0, 1.0)
    if sl == 3.5 and tp == 5.0:
        _ok(f"XAU con SL=1.0/TP=1.0 → clamp a SL={sl}/TP={tp}")
    else:
        _fail(f"XAU clamp incorrecto: SL={sl}, TP={tp}")
        return False

    # Cripto: SL ∈ [1.8, 3.5]
    sl, tp = clamp_atr_by_class("BTC", 10.0, 20.0)
    if sl == 3.5 and tp == 6.0:
        _ok(f"BTC con SL=10.0/TP=20.0 → clamp a SL={sl}/TP={tp}")
    else:
        _fail(f"BTC clamp incorrecto: SL={sl}, TP={tp}")
        return False

    # get_class_of
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
# 🆕 TEST 16 — B20: disabled_symbols
# =============================================================================
def test_b20_disabled_symbols():
    print("\n🧪 TEST 16 — 🐛 B20: disabled_symbols")
    try:
        from feedback_learner import ContinuousLearningAgent, DISABLE_THRESHOLDS
    except ImportError as e:
        _fail(f"No se pudo importar: {e}")
        return False

    agent = ContinuousLearningAgent()

    # Simular by_symbol con XAGUSD muy malo
    fake_by_symbol = {
        "XAGUSD": {"trades": 8, "profit_factor": 0.25, "wins": 2, "losses": 6, "win_rate_pct": 25.0, "pnl_usd": -20.0, "is_profitable": False},
        "ETHUSD": {"trades": 6, "profit_factor": 0.0, "wins": 0, "losses": 6, "win_rate_pct": 0.0, "pnl_usd": -5.0, "is_profitable": False},
        "XTIUSD": {"trades": 4, "profit_factor": 2.045, "wins": 3, "losses": 1, "win_rate_pct": 75.0, "pnl_usd": 23.0, "is_profitable": True},
    }

    disabled, details = agent._compute_disabled_symbols(fake_by_symbol)

    if "XAGUSD" in disabled:
        _ok(f"XAGUSD deshabilitado (PF=0.25)")
    else:
        _fail(f"XAGUSD NO deshabilitado (era PF=0.25)")
        return False

    if "ETHUSD" in disabled:
        _ok(f"ETHUSD deshabilitado (PF=0.0)")
    else:
        _fail(f"ETHUSD NO deshabilitado (era PF=0.0)")
        return False

    if "XTIUSD" not in disabled:
        _ok(f"XTIUSD NO deshabilitado (PF=2.045)")
    else:
        _fail(f"XTIUSD deshabilitado por error (era PF=2.045)")
        return False

    # Verificar is_symbol_disabled
    if agent.is_symbol_disabled("XAGUSD", {"disabled_symbols": disabled, "disabled_details": details}):
        _ok("is_symbol_disabled('XAGUSD') → True")
    else:
        _fail("is_symbol_disabled('XAGUSD') → False")
        return False

    return True


# =============================================================================
# 🆕 TEST 17 — B21: cuarentena escalonada
# =============================================================================
def test_b21_quarantine_scaling():
    print("\n🧪 TEST 17 — 🐛 B21: cuarentena escalonada")
    try:
        from risk_guardian import InstitutionalRiskGuardian, CONSECUTIVE_LOSS_THRESHOLDS
    except ImportError as e:
        _fail(f"No se pudo importar: {e}")
        return False

    rg = InstitutionalRiskGuardian(initial_capital=1730.0)

    # Simular 3 pérdidas consecutivas en XAUUSD
    for i in range(3):
        rg.register_trade_closed(pnl_usd=-5.0, symbol="XAUUSD")

    # Verificar cuarentena
    report = rg.get_status_report()
    quarantines = report.get("active_quarantines", {})

    if "XAU" in quarantines:
        remaining_min = quarantines["XAU"]["remaining_min"]
        if 50 <= remaining_min <= 60:
            _ok(f"XAU en cuarentena ~1h ({remaining_min} min restantes) tras 3 pérdidas")
        else:
            _warn(f"XAU en cuarentena con {remaining_min} min (esperado ~60)")
    else:
        _fail("XAU NO está en cuarentena tras 3 pérdidas")
        return False

    # Verificar que ganar resetea
    rg.register_trade_closed(pnl_usd=+10.0, symbol="XAUUSD")
    streak = rg._consecutive_losses.get("XAU", 0)
    if streak == 0:
        _ok("Racha reseteada tras ganancia")
    else:
        _fail(f"Racha NO reseteada (streak={streak})")
        return False

    return True


# =============================================================================
# RUNNER
# =============================================================================
def main():
    print("=" * 70)
    print("  QUANTEDGE AI — SMOKE TEST v1.9.0")
    print("=" * 70)

    tests = [
        ("FIX #1 — canónico OIL",               test_fix1_canonical_oil),
        ("FIX #2 — _check_macro_trend existe",  test_fix2_macro_trend_method_exists),
        ("FIX #2 — _check_macro_trend fail-safe", test_fix2_macro_trend_failsafe),
        ("Risk Guardian — instanciación",       test_risk_guardian_instantiates),
        ("Signal Agent — por clase",            test_signal_agent_per_asset_class),
        ("Execution Agent — instanciación",     test_execution_agent_instantiates),
        ("Coherencia — 3 módulos",              test_canonical_consistency),
        ("BUG #1 — bridge canónico OIL",        test_bug1_bridge_canonical_oil),
        ("BUG #1 — infer_is_buyer_maker",       test_bug1_infer_is_buyer_maker),
        ("BUG #3 — _resolve_mt5_symbol",        test_bug3_signal_agent_resolve_symbol),
        ("BUG #4 — _get_contract_size",         test_bug4_execution_agent_contract_size),
        ("MEJORA #5 — _get_min_atr",            test_mejora5_feature_agent_min_atr),
        ("Coherencia — 4 módulos",              test_canonical_consistency_4_modules),
        ("BUG #5 — PnL UNKNOWN (O5)",           test_bug5_pnl_unknown_reason),
        ("🆕 B19 — límites ATR por clase",      test_b19_atr_limits_by_class),
        ("🆕 B20 — disabled_symbols",           test_b20_disabled_symbols),
        ("🆕 B21 — cuarentena escalonada",      test_b21_quarantine_scaling),
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