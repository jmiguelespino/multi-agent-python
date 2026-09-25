"""
Test rápido de un activo candidato: spread, ATR, y volumen mínimo.
NO opera, solo lee datos de MT5.
"""
import MetaTrader5 as mt5
import sys

if len(sys.argv) < 2:
    print("Uso: python test_candidate.py <SIMBOLO>")
    print("Ejemplo: python test_candidate.py NAS100")
    sys.exit(1)

symbol = sys.argv[1].upper()

mt5.initialize()

info = mt5.symbol_info(symbol)
if not info:
    print(f"❌ {symbol} no encontrado en MT5")
    mt5.shutdown()
    sys.exit(1)

tick = mt5.symbol_info_tick(symbol)
if not tick:
    print(f"❌ No hay tick para {symbol}")
    mt5.shutdown()
    sys.exit(1)

spread_bps = ((tick.ask - tick.bid) / tick.bid) * 10000

# ATR de las últimas 20 velas de 1 minuto
rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M1, 0, 20)
atr = 0
if rates is not None and len(rates) >= 14:
    trs = [max(rates[i]['high']-rates[i]['low'],
               abs(rates[i]['high']-rates[i-1]['close']),
               abs(rates[i]['low']-rates[i-1]['close']))
           for i in range(1, len(rates))]
    atr = sum(trs[-14:]) / 14

print()
print("=" * 60)
print(f"  TEST RÁPIDO: {symbol}")
print("=" * 60)
print(f"  Precio:            {tick.bid}")
print(f"  Spread:            {spread_bps:.2f} bps")
print(f"  ATR(14) M1:        {atr:.6f}")
print(f"  Contract size:     {info.trade_contract_size}")
print(f"  Volume min:        {info.volume_min}")
print(f"  Volume step:       {info.volume_step}")
print(f"  Volume max:        {info.volume_max}")
print()

# Diagnóstico rápido
if spread_bps > 15:
    print(f"  ⚠️  Spread ALTO (>{15} bps). Podría ser rechazado.")
elif spread_bps > 8:
    print(f"  🟡 Spread medio. Aceptable si el ATR es amplio.")
else:
    print(f"  ✅ Spread bajo. Buen candidato.")

if info.volume_min > 0.5:
    print(f"  ⚠️  Volume min alto ({info.volume_min}). Podría necesitar cap especial.")

print()
mt5.shutdown()