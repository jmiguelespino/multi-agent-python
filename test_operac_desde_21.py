"""
Análisis detallado de operaciones desde las 21:00 de hoy.
"""
import MetaTrader5 as mt5
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta
from collections import defaultdict

TZ_MT5 = timezone(timedelta(hours=3))
BASE_DIR = Path(__file__).resolve().parent
AUDIT_FILE = BASE_DIR / "logs" / "trade_audit_history.jsonl"

# Fecha/hora de corte: hoy a las 21:00 MT5
now_mt5 = datetime.now(TZ_MT5)
cutoff = now_mt5.replace(hour=21, minute=0, second=0, microsecond=0)
cutoff_ms = int(cutoff.timestamp() * 1000)

print("=" * 90)
print(f"  ANÁLISIS DE OPERACIONES DESDE LAS {cutoff.strftime('%Y-%m-%d %H:%M')} (MT5)")
print(f"  Hora actual: {now_mt5.strftime('%Y-%m-%d %H:%M:%S')} MT5")
print("=" * 90)

# --- Leer audit log ---
if not AUDIT_FILE.exists():
    print(f"❌ No existe {AUDIT_FILE}")
    exit(1)

orders = []
closures = []
rejections = defaultdict(int)

with open(AUDIT_FILE, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except:
            continue
        ts = rec.get("timestamp", 0)
        if ts < cutoff_ms:
            continue

        cat = rec.get("category", "")
        evt = rec.get("event_type", "")

        if evt == "ORDER_FILLED":
            orders.append(rec)
        elif cat == "CLOSURE":
            closures.append(rec)
        elif cat == "REJECTION":
            rejections[evt] += 1

print(f"\n📊 RESUMEN DEL PERÍODO:")
print(f"  Órdenes ejecutadas:    {len(orders)}")
print(f"  Posiciones cerradas:   {len(closures)}")
print(f"  Rechazos:              {sum(rejections.values())}")

if rejections:
    print(f"\n  Desglose de rechazos:")
    for evt, cnt in sorted(rejections.items(), key=lambda x: -x[1])[:10]:
        print(f"    {evt}: {cnt}")

# --- Análisis de cierres ---
print("\n" + "=" * 90)
print("  DETALLE DE CIERRES")
print("=" * 90)

if not closures:
    print("  (No hay cierres en este período)")
else:
    print(f"  {'HORA':<8} {'SÍMBOLO':<10} {'LADO':<5} {'LOTES':>7} {'PnL':>10} {'DUR':>8} {'RAZÓN':<15}")
    print("  " + "-" * 80)

    total_pnl = 0
    by_symbol = defaultdict(lambda: {"count": 0, "pnl": 0.0, "wins": 0, "losses": 0})

    for c in sorted(closures, key=lambda x: x.get("timestamp", 0)):
        ts = c.get("timestamp", 0) / 1000
        dt = datetime.fromtimestamp(ts, tz=TZ_MT5)
        hora = dt.strftime("%H:%M:%S")
        sym = c.get("symbol", "?")
        side = c.get("side", "?")
        vol = c.get("volume", 0)
        pnl = float(c.get("pnl_usd", 0) or 0)
        reason = c.get("event_type", "?").replace("_HIT", "").replace("_CLOSE", "")
        meta = c.get("metadata", {})
        dur = meta.get("duration_sec", 0)

        total_pnl += pnl
        by_symbol[sym]["count"] += 1
        by_symbol[sym]["pnl"] += pnl
        if pnl > 0:
            by_symbol[sym]["wins"] += 1
        else:
            by_symbol[sym]["losses"] += 1

        emoji = "🟢" if pnl > 0 else "🔴"
        print(f"  {hora:<8} {sym:<10} {side:<5} {vol:>7.2f} {emoji} ${pnl:>+8.2f} {dur:>7}s {reason:<15}")

    print("  " + "-" * 80)
    print(f"  PnL TOTAL: ${total_pnl:>+8.2f}")

    # Desglose por símbolo
    print("\n  📊 DESGLOSE POR SÍMBOLO:")
    print(f"  {'SÍMBOLO':<10} {'TRADES':>7} {'W/L':>8} {'WR%':>7} {'PnL':>12}")
    print("  " + "-" * 55)
    for sym, d in sorted(by_symbol.items(), key=lambda x: x[1]["pnl"], reverse=True):
        wr = (d["wins"] / d["count"] * 100) if d["count"] > 0 else 0
        emoji = "🟢" if d["pnl"] > 0 else "🔴"
        print(f"  {sym:<10} {d['count']:>7} {d['wins']}/{d['losses']:<6} {wr:>6.1f}% {emoji} ${d['pnl']:>+9.2f}")

# --- Órdenes abiertas actuales en MT5 ---
print("\n" + "=" * 90)
print("  POSICIONES ABIERTAS ACTUALMENTE")
print("=" * 90)

mt5.initialize()
acc = mt5.account_info()
positions = mt5.positions_get() or []

if acc:
    print(f"  Balance:  ${acc.balance:,.2f}")
    print(f"  Equity:   ${acc.equity:,.2f}")
    print(f"  Margen:   ${acc.margin:,.2f}")
    print()

total_float = 0
for p in positions:
    side = "BUY" if p.type == mt5.ORDER_TYPE_BUY else "SELL"
    total_float += p.profit
    emoji = "🟢" if p.profit > 0 else "🔴"
    open_time = datetime.fromtimestamp(p.time, tz=TZ_MT5)
    print(f"  #{p.ticket} {p.symbol:<10} {side:<5} {p.volume:>5.2f} @ ${p.price_open:>10.2f} | "
          f"Open: {open_time.strftime('%H:%M')} | PnL: {emoji} ${p.profit:>+7.2f}")

print()
print(f"  PnL flotante total: ${total_float:>+8.2f}")

mt5.shutdown()
print("\n" + "=" * 90)