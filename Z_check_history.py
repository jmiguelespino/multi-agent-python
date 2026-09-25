# check_history.py
import MetaTrader5 as mt5
from datetime import datetime, timezone, timedelta

mt5.initialize()

tz_mt5 = timezone(timedelta(hours=3))
end = datetime.now(tz_mt5)
start = end - timedelta(days=180)  # 6 meses

SIMBOLOS = ["XAUUSD", "XTIUSD", "XBRUSD", "XAGUSD", "BTCUSD", "ETHUSD", "SOLUSD", "US500"]

print("=" * 80)
print(f"VERIFICACIÓN DE HISTÓRICO MT5 — {start.date()} → {end.date()}")
print("=" * 80)

for sym in SIMBOLOS:
    resolved = sym
    if not mt5.symbol_info(sym):
        for alt in [f"{sym}.raw", f"{sym}m", f"{sym}_raw"]:
            if mt5.symbol_info(alt):
                resolved = alt
                break

    if not mt5.symbol_info(resolved):
        print(f"❌ {sym:8s} — NO disponible en MT5")
        continue

    mt5.symbol_select(resolved, True)
    rates = mt5.copy_rates_range(resolved, mt5.TIMEFRAME_M1, start, end)

    if rates is None or len(rates) == 0:
        print(f"⚠️  {sym:8s} ({resolved:12s}) — 0 velas M1 en el rango")
        continue

    first_dt = datetime.fromtimestamp(rates[0]['time'], tz=tz_mt5)
    last_dt = datetime.fromtimestamp(rates[-1]['time'], tz=tz_mt5)
    dias = (last_dt - first_dt).days

    print(
        f"✅ {sym:8s} ({resolved:12s}) — {len(rates):>7,} velas M1 | "
        f"{first_dt.date()} → {last_dt.date()} ({dias} días)"
    )

mt5.shutdown()
print("=" * 80)