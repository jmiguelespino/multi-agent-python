"""
check_deals.py — Diagnóstico de cómo MT5 reporta los deals.
"""
import MetaTrader5 as mt5
from datetime import datetime, timedelta, timezone

TZ_MT5 = timezone(timedelta(hours=3))

mt5.initialize()

# Rango amplio
from_date = datetime.now(TZ_MT5) - timedelta(days=2)
to_date = datetime.now(TZ_MT5) + timedelta(days=1)

print("=" * 80)
print(f"DEALS EN MT5 ({from_date.date()} → {to_date.date()})")
print("=" * 80)

# Todos los deals
all_deals = mt5.history_deals_get(from_date, to_date)
print(f"\nTotal deals en el rango: {len(all_deals) if all_deals else 0}")

if all_deals:
    print(f"\nPrimeros 5 deals — INSPECCIÓN DE CAMPOS:")
    for i, d in enumerate(all_deals[:5]):
        print(f"\n  Deal #{i+1}:")
        print(f"    ticket:       {d.ticket}")
        print(f"    order:        {d.order}")
        print(f"    position_id:  {getattr(d, 'position_id', 'NO EXISTE')}")
        print(f"    position:     {getattr(d, 'position', 'NO EXISTE')}")
        print(f"    symbol:       {d.symbol}")
        print(f"    type:         {d.type}")
        print(f"    entry:        {d.entry}  (0=IN, 1=OUT, 2=INOUT, 3=OUT_BY)")
        print(f"    profit:       {d.profit}")
        print(f"    volume:       {d.volume}")
        print(f"    price:        {d.price}")
        print(f"    time:         {d.time}")
        print(f"    time_msc:     {d.time_msc}")

    # Tickets únicos de position_id
    pos_ids = set()
    for d in all_deals:
        pid = getattr(d, "position_id", None) or getattr(d, "position", None)
        if pid:
            pos_ids.add(pid)
    print(f"\n\nPosition IDs únicos: {len(pos_ids)}")
    print(f"Primeros 10: {sorted(pos_ids)[:10]}")

    # Tickets de deals
    deal_tickets = [d.ticket for d in all_deals]
    print(f"\nDeal tickets únicos: {len(set(deal_tickets))}")
    print(f"Primeros 10: {sorted(set(deal_tickets))[:10]}")

    # Orders
    order_tickets = [d.order for d in all_deals]
    print(f"\nOrder tickets únicos: {len(set(order_tickets))}")
    print(f"Primeros 10: {sorted(set(order_tickets))[:10]}")

# Buscar específicamente el ticket del test de integración
target_ticket = 1963800008
print(f"\n\n{'=' * 80}")
print(f"BUSCANDO TICKET {target_ticket} (test de integración)")
print(f"{'=' * 80}")

found_in_position = False
found_in_ticket = False
found_in_order = False

for d in all_deals or []:
    if getattr(d, 'position_id', None) == target_ticket:
        print(f"✅ Encontrado en position_id: {d}")
        found_in_position = True
    if d.ticket == target_ticket:
        print(f"✅ Encontrado en ticket: {d}")
        found_in_ticket = True
    if d.order == target_ticket:
        print(f"✅ Encontrado en order: {d}")
        found_in_order = True

if not (found_in_position or found_in_ticket or found_in_order):
    print(f"❌ NO se encontró el ticket {target_ticket} en ningún campo")

mt5.shutdown()