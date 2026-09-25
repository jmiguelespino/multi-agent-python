"""
Diagnóstico específico para Forex (EURUSD, GBPUSD).
"""
import MetaTrader5 as mt5
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

mt5.initialize()

print("=" * 70)
print("  DIAGNÓSTICO FOREX (EURUSD, GBPUSD)")
print("=" * 70)

for sym in ["EURUSD", "GBPUSD"]:
    info = mt5.symbol_info(sym)
    tick = mt5.symbol_info_tick(sym)

    if not info or not tick:
        print(f"\n❌ {sym}: no disponible")
        continue

    spread_bps = ((tick.ask - tick.bid) / tick.bid) * 10000

    # ATR teórico con las últimas 14 velas de 1 minuto
    rates = mt5.copy_rates_from_pos(sym, mt5.TIMEFRAME_M1, 0, 20)
    if rates is not None and len(rates) >= 14:
        trs = []
        for i in range(1, len(rates)):
            h, l, pc = rates[i]['high'], rates[i]['low'], rates[i-1]['close']
            tr = max(h - l, abs(h - pc), abs(l - pc))
            trs.append(tr)
        atr = sum(trs[-14:]) / 14
    else:
        atr = 0

    sl_mult = float(os.getenv("FOREX_ATR_STOP_MULTIPLIER", "1.2"))
    sl_pips = atr * sl_mult * 10000  # convertir a pips
    min_atr = tick.bid * 0.0001
    max_atr = tick.bid * 0.01

    print(f"\n📊 {sym}:")
    print(f"  Precio:            {tick.bid}")
    print(f"  Spread:            {spread_bps:.2f} bps")
    print(f"  ATR(14) M1:        {atr:.6f} ({atr * 10000:.1f} pips)")
    print(f"  SL multiplier:     {sl_mult}")
    print(f"  SL calculado:      {sl_pips:.1f} pips")
    print(f"  Rango ATR válido:  {min_atr:.6f} - {max_atr:.6f}")
    print(f"  ATR en rango:      {'✅ Sí' if min_atr <= atr <= max_atr else '❌ No'}")

    # Volumen calculado
    capital = 1875.82
    risk_pct = float(os.getenv("MAX_RISK_PER_TRADE_PCT", "1.0"))
    risk_usd = capital * (risk_pct / 100)
    contract = info.trade_contract_size
    if atr > 0:
        lot_calc = risk_usd / (atr * sl_mult * contract)
    else:
        lot_calc = 0
    max_lot = float(os.getenv("FOREX_MAX_LOT_SIZE", "0.10"))
    final_lot = min(lot_calc, max_lot)
    real_risk = final_lot * atr * sl_mult * contract

    print(f"  Lotaje calculado:  {lot_calc:.4f}")
    print(f"  Cap max lot:       {max_lot}")
    print(f"  Lotaje final:      {final_lot:.4f}")
    print(f"  Riesgo real:       ${real_risk:.2f} ({(real_risk/capital)*100:.2f}%)")

mt5.shutdown()