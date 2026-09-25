"""
Reporte de operaciones y PnL por activo.
"""
import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime, timezone, timedelta

TZ_MT5 = timezone(timedelta(hours=3))
BASE_DIR = Path(__file__).resolve().parent
AUDIT_FILE = BASE_DIR / "logs" / "trade_audit_history.jsonl"

counts_orders = defaultdict(int)
counts_closures = defaultdict(int)
pnls = defaultdict(float)
wins = defaultdict(int)
losses = defaultdict(int)

if not AUDIT_FILE.exists():
    print(f"❌ No existe {AUDIT_FILE}")
    exit(1)

for line in AUDIT_FILE.read_text(encoding="utf-8").splitlines():
    try:
        r = json.loads(line)
    except Exception:
        continue

    sym = r.get("symbol", "UNKNOWN")
    evt = r.get("event_type", "")
    cat = r.get("category", "")

    if evt == "ORDER_FILLED":
        counts_orders[sym] += 1
    elif cat == "CLOSURE":
        pnl = float(r.get("pnl_usd") or 0)
        counts_closures[sym] += 1
        pnls[sym] += pnl
        if pnl > 0:
            wins[sym] += 1
        else:
            losses[sym] += 1

all_syms = sorted(set(list(counts_orders.keys()) + list(counts_closures.keys())))

print()
print("=" * 90)
print("  OPERACIONES TOTALES Y PnL POR ACTIVO")
print("=" * 90)
print(f"{'SÍMBOLO':<10} {'ÓRDENES':>9} {'CIERRES':>9} {'W/L':>10} {'WR%':>7} {'PnL Total':>13} {'PnL/Op':>10}")
print("-" * 90)

total_orders = 0
total_closures = 0
total_pnl = 0.0

for sym in all_syms:
    o = counts_orders[sym]
    c = counts_closures[sym]
    p = pnls[sym]
    w = wins[sym]
    l = losses[sym]
    wr = (w / c * 100) if c > 0 else 0
    pnl_per = (p / c) if c > 0 else 0

    total_orders += o
    total_closures += c
    total_pnl += p

    pnl_emoji = "🟢" if p > 0 else ("🔴" if p < 0 else "⚪")
    print(f"{sym:<10} {o:>9} {c:>9} {w:>4}/{l:<5} {wr:>6.1f}% {pnl_emoji} ${p:>+10.2f} ${pnl_per:>+8.2f}")

print("-" * 90)
print(f"{'TOTAL':<10} {total_orders:>9} {total_closures:>9} {'':>10} {'':>7} 🟢 ${total_pnl:>+10.2f}")

# Ranking por PnL
print()
print("=" * 90)
print("  RANKING POR PnL")
print("=" * 90)

sorted_syms = sorted(all_syms, key=lambda s: pnls[s], reverse=True)
for i, sym in enumerate(sorted_syms, 1):
    p = pnls[sym]
    bar_len = int(abs(p) / 5) if p != 0 else 0
    bar = "█" * min(bar_len, 40)
    color = "🟢" if p > 0 else "🔴"
    medal = "🥇" if i == 1 else ("🥈" if i == 2 else ("🥉" if i == 3 else "  "))
    print(f"{medal} {sym:<10} {color} {bar} ${p:>+10.2f}")

print()