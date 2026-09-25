import MetaTrader5 as mt5

mt5.initialize()
acc = mt5.account_info()
positions = mt5.positions_get() or []

if acc is None:
    print("❌ No hay cuenta conectada")
    exit(1)

print("=" * 70)
print("  ESTADO ACTUAL DE LA CUENTA")
print("=" * 70)
print(f"  Login:         #{acc.login} ({acc.server})")
print(f"  Balance:       ${acc.balance:,.2f}")
print(f"  Equity:        ${acc.equity:,.2f}")
print(f"  Margen usado:  ${acc.margin:,.2f}")
print(f"  Margen libre:  ${acc.margin_free:,.2f}")
print(f"  Nivel margen:  {acc.margin_level:.2f}%" if acc.margin_level else "  Nivel margen:  N/D")
print()
print(f"  Posiciones abiertas: {len(positions)}")
print("-" * 70)
total_pnl = 0.0
for p in positions:
    side = "BUY" if p.type == mt5.ORDER_TYPE_BUY else "SELL"
    total_pnl += p.profit
    print(f"  #{p.ticket} {p.symbol:<10} {side:<5} {p.volume:>5} lots @ ${p.price_open:>10.2f} | PnL: ${p.profit:>+8.2f}")
print("-" * 70)
print(f"  PnL total flotante: ${total_pnl:>+8.2f}")
print()

if total_pnl > 0:
    print(f"  🟢 En verde")
elif total_pnl < 0:
    print(f"  🔴 En rojo")
else:
    print(f"  ⚪ Neutro")

mt5.shutdown()