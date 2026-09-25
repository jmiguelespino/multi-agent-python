# check_us500.py
import MetaTrader5 as mt5
from datetime import datetime, timedelta, timezone

mt5.initialize()
tz = timezone(timedelta(hours=3))
f = datetime.now(tz) - timedelta(hours=6)
t = datetime.now(tz) + timedelta(hours=1)

print("=" * 70)
print("DEALS US500 — últimas 6h")
print("=" * 70)

deals = mt5.history_deals_get(f, t)
if not deals:
    print("No hay deals.")
else:
    for d in deals:
        if d.symbol != "US500":
            continue
        pid = getattr(d, "position_id", None) or getattr(d, "position", None)
        entry_str = {0: "IN", 1: "OUT", 2: "INOUT", 3: "OUT_BY"}.get(d.entry, "?")
        print(
            f"#{d.ticket} pos_id={pid} "
            f"entry={entry_str} "
            f"price={d.price} "
            f"profit={d.profit} "
            f"commission={d.commission} "
            f"swap={d.swap} "
            f"comment='{d.comment}'"
        )

print()
print("=" * 70)
print("POSICIONES ABIERTAS AHORA")
print("=" * 70)
positions = mt5.positions_get() or []
if not positions:
    print("No hay posiciones abiertas.")
else:
    for p in positions:
        side = "BUY" if p.type == mt5.ORDER_TYPE_BUY else "SELL"
        print(
            f"#{p.ticket} {p.symbol} {side} {p.volume} "
            f"entry={p.price_open} current={p.price_current} "
            f"SL={p.sl} TP={p.tp} PnL={p.profit}"
        )

mt5.shutdown()