"""
Diagnóstico rápido del estado del bot.
"""
import MetaTrader5 as mt5
from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

print("=" * 70)
print("🔍 QUANTEDGE AI — DIAGNÓSTICO")
print("=" * 70)

# --- MT5 ---
if not mt5.initialize():
    print(f"❌ Error inicializando MT5: {mt5.last_error()}")
    exit(1)

acc = mt5.account_info()
if acc is None:
    print("❌ No hay cuenta conectada en MT5")
    exit(1)

print(f"\n📊 CUENTA MT5:")
print(f"  • Login:   #{acc.login}")
print(f"  • Balance: ${acc.balance:,.2f}")
print(f"  • Equity:  ${acc.equity:,.2f}")
print(f"  • Margen libre: ${acc.margin_free:,.2f}")

# --- Posiciones ---
positions = mt5.positions_get() or []
print(f"\n📈 POSICIONES ABIERTAS: {len(positions)}")
for p in positions:
    side = "BUY" if p.type == mt5.ORDER_TYPE_BUY else "SELL"
    print(f"  • #{p.ticket} {p.symbol} {side} {p.volume} lots @ ${p.price_open} | PnL: ${p.profit:+.2f}")

# --- Config ---
print(f"\n⚙️  CONFIGURACIÓN (.env):")
print(f"  • MAX_DAILY_TRADES:           {os.getenv('MAX_DAILY_TRADES', 'N/D')}")
print(f"  • MAX_CONCURRENT_POSITIONS:   {os.getenv('MAX_CONCURRENT_POSITIONS', 'N/D')}")
print(f"  • COOLDOWN_SECONDS:           {os.getenv('COOLDOWN_SECONDS', 'N/D')}")
print(f"  • STOP_LOSS_CUARENTENA_SEC:   {os.getenv('STOP_LOSS_CUARENTENA_SECONDS', 'N/D')}")
print(f"  • MAX_RISK_PER_TRADE_PCT:     {os.getenv('MAX_RISK_PER_TRADE_PCT', 'N/D')}")
print(f"  • MIN_CONFIDENCE_THRESHOLD:   {os.getenv('MIN_CONFIDENCE_THRESHOLD', 'N/D')}")

# --- Auditoría del día ---
audit_file = BASE_DIR / "logs" / "trade_audit_history.jsonl"
if audit_file.exists():
    import json
    from datetime import datetime, timezone, timedelta
    TZ_MT5 = timezone(timedelta(hours=3))
    today = datetime.now(TZ_MT5).strftime("%Y-%m-%d")

    orders_today = 0
    closures_today = 0
    rejections_by_type = {}

    with open(audit_file, "r", encoding="utf-8") as f:
        for line in f:
            try:
                rec = json.loads(line)
            except:
                continue
            # Filtrar solo hoy (comparando fecha ISO en UTC+3)
            ts_ms = rec.get("timestamp", 0)
            dt = datetime.fromtimestamp(ts_ms / 1000, tz=TZ_MT5)
            if dt.strftime("%Y-%m-%d") != today:
                continue

            evt = rec.get("event_type", "")
            cat = rec.get("category", "")
            if evt == "ORDER_FILLED":
                orders_today += 1
            elif cat == "CLOSURE":
                closures_today += 1
            elif cat == "REJECTION":
                rejections_by_type[evt] = rejections_by_type.get(evt, 0) + 1

    print(f"\n📅 ACTIVIDAD DE HOY ({today}):")
    print(f"  • Órdenes ejecutadas: {orders_today}")
    print(f"  • Posiciones cerradas: {closures_today}")
    print(f"  • Rechazos:")
    for evt, count in sorted(rejections_by_type.items(), key=lambda x: -x[1])[:10]:
        print(f"      - {evt}: {count}")

mt5.shutdown()
print("\n" + "=" * 70)