"""
Verifica los límites de lotaje configurados y el riesgo real estimado por activo.
El capital se lee EN VIVO desde MT5 (con fallback al .env si MT5 no está disponible).
"""
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

# --- Leer capital EN VIVO desde MT5 ---
CAPITAL = None
CAPITAL_SOURCE = "unknown"
try:
    import MetaTrader5 as mt5
    if mt5.initialize():
        acc = mt5.account_info()
        if acc:
            CAPITAL = acc.balance
            CAPITAL_SOURCE = f"MT5 (cuenta #{acc.login})"
        else:
            CAPITAL = float(os.getenv("CAPITAL_BASE_USD", "1500.0"))
            CAPITAL_SOURCE = "FALLBACK .env (MT5 sin cuenta)"
        mt5.shutdown()
    else:
        CAPITAL = float(os.getenv("CAPITAL_BASE_USD", "1500.0"))
        CAPITAL_SOURCE = "FALLBACK .env (MT5 init falló)"
except ImportError:
    CAPITAL = float(os.getenv("CAPITAL_BASE_USD", "1500.0"))
    CAPITAL_SOURCE = "FALLBACK .env (MetaTrader5 no instalado)"

# Contract sizes reales de IC Markets (obtenidos con mt5.symbol_info)
CONTRACT_SIZES = {
    "XAUUSD": 100.0, "XTIUSD": 100.0, "XBRUSD": 100.0,
    "EURUSD": 100000.0, "GBPUSD": 100000.0,
    "BTCUSD": 1.0, "ETHUSD": 1.0, "SOLUSD": 1.0,
}

# ATR típicos observados (aproximados)
ATR_TIPICOS = {
    "XAUUSD": 2.50, "XTIUSD": 0.30, "XBRUSD": 0.30,
    "EURUSD": 0.00020, "GBPUSD": 0.00025,
    "BTCUSD": 50.0, "ETHUSD": 3.0, "SOLUSD": 0.10,
}

SL_MULTS = {
    "XAUUSD": float(os.getenv("GOLD_ATR_STOP_MULTIPLIER", "4.5")),
    "XTIUSD": float(os.getenv("OIL_ATR_STOP_MULTIPLIER", "1.8")),
    "XBRUSD": float(os.getenv("OIL_ATR_STOP_MULTIPLIER", "1.8")),
    "EURUSD": float(os.getenv("FOREX_ATR_STOP_MULTIPLIER", "1.2")),
    "GBPUSD": float(os.getenv("FOREX_ATR_STOP_MULTIPLIER", "1.2")),
    "BTCUSD": float(os.getenv("CRYPTO_ATR_STOP_MULTIPLIER", "2.2")),
    "ETHUSD": float(os.getenv("CRYPTO_ATR_STOP_MULTIPLIER", "2.2")),
    "SOLUSD": float(os.getenv("CRYPTO_ATR_STOP_MULTIPLIER", "2.2")),
}

MAX_LOTS = {
    "XAUUSD": float(os.getenv("GOLD_MAX_LOT_SIZE", "0.03")),
    "XTIUSD": float(os.getenv("CRUDE_MAX_LOT_SIZE", "0.50")),
    "XBRUSD": float(os.getenv("CRUDE_MAX_LOT_SIZE", "0.50")),
    "EURUSD": float(os.getenv("FOREX_MAX_LOT_SIZE", "0.10")),
    "GBPUSD": float(os.getenv("FOREX_MAX_LOT_SIZE", "0.10")),
    "BTCUSD": float(os.getenv("CRYPTO_MAX_LOT_SIZE", "0.05")),
    "ETHUSD": float(os.getenv("CRYPTO_MAX_LOT_SIZE", "0.05")),
    "SOLUSD": float(os.getenv("CRYPTO_MAX_LOT_SIZE", "0.05")),
}

VOL_MIN = {
    "XAUUSD": 0.01, "XTIUSD": 0.50, "XBRUSD": 0.50,
    "EURUSD": 0.01, "GBPUSD": 0.01,
    "BTCUSD": 0.01, "ETHUSD": 0.01, "SOLUSD": 1.00,
}

TARGET_RISK_PCT = float(os.getenv("MAX_RISK_PER_TRADE_PCT", "1.0"))
TARGET_RISK_USD = CAPITAL * (TARGET_RISK_PCT / 100.0)

print("=" * 90)
print(f"  ANÁLISIS DE RIESGO POR ACTIVO")
print(f"  Capital: ${CAPITAL:,.2f}  (fuente: {CAPITAL_SOURCE})")
print(f"  Objetivo de riesgo por trade: ${TARGET_RISK_USD:.2f} ({TARGET_RISK_PCT:.2f}%)")
print("=" * 90)
print(f"\n{'Activo':<10} {'SL_ATR':>7} {'SL_$':>11} {'LotMax':>7} {'Risk_$':>10} {'Risk_%':>8} {'Estado':<20}")
print("-" * 90)

max_positions = int(os.getenv("MAX_CONCURRENT_POSITIONS", "5"))
active_symbols = [s.strip() for s in os.getenv("TRADING_SYMBOLS", "").split(",") if s.strip()]

for sym in CONTRACT_SIZES:
    if sym not in active_symbols and sym not in ["XTIUSD", "XBRUSD", "XAUUSD"]:
        # Solo mostramos los activos activos + los 3 principales
        if sym not in active_symbols:
            continue

    atr = ATR_TIPICOS[sym]
    sl_mult = SL_MULTS[sym]
    sl_usd = atr * sl_mult
    lot = MAX_LOTS[sym]
    contract = CONTRACT_SIZES[sym]
    risk_usd = lot * sl_usd * contract
    risk_pct = (risk_usd / CAPITAL) * 100.0

    if risk_pct <= 1.0:
        estado = "✅ OK"
    elif risk_pct <= 1.5:
        estado = "🟡 ACEPTABLE"
    elif risk_pct <= 2.0:
        estado = "🟠 ALTO"
    else:
        estado = "🔴 CRÍTICO"

    if VOL_MIN[sym] > lot:
        estado += " (vol_min)"

    print(f"{sym:<10} {sl_mult:>7.1f} {sl_usd:>11.5f} {lot:>7.2f} {risk_usd:>10.2f} {risk_pct:>7.2f}% {estado:<20}")

print("-" * 90)

# Riesgo agregado
total_risk_single = 0.0
for sym in active_symbols:
    if sym in CONTRACT_SIZES:
        risk = MAX_LOTS[sym] * (ATR_TIPICOS[sym] * SL_MULTS[sym]) * CONTRACT_SIZES[sym]
        total_risk_single += risk

worst_case = total_risk_single  # Si el bot tomara todos los activos al máximo
realistic_case = (total_risk_single / len(active_symbols)) * max_positions if active_symbols else 0

print()
print(f"Riesgo si TODOS los activos operaran al máximo: ${worst_case:.2f} ({worst_case / CAPITAL * 100:.2f}%)")
print(f"Riesgo agregado con {max_positions} posiciones simultáneas: ${realistic_case:.2f} ({realistic_case / CAPITAL * 100:.2f}%)")
print(f"Circuit breaker activa si: -${CAPITAL * float(os.getenv('DAILY_DRAWDOWN_LIMIT_PCT', '3.0')) / 100:.2f}")
print()