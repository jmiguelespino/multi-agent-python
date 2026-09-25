# check_timeline.py
import json
import os
from datetime import datetime

print("=" * 80)
print("TIMELINE DEL PROYECTO")
print("=" * 80)

# 1. Rango temporal del JSONL
jsonl = 'logs/trade_audit_history.jsonl'
if os.path.exists(jsonl):
    timestamps = []
    with open(jsonl, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
                ts = r.get('timestamp')
                if ts:
                    timestamps.append(ts)
            except json.JSONDecodeError:
                continue

    if timestamps:
        timestamps.sort()
        first = datetime.fromtimestamp(timestamps[0] / 1000)
        last = datetime.fromtimestamp(timestamps[-1] / 1000)
        print(f"\nJSONL — trade_audit_history.jsonl:")
        print(f"  Primer evento: {first.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  Último evento: {last.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  Total eventos: {len(timestamps)}")

# 2. Última modificación de archivos clave
print(f"\nÚLTIMA MODIFICACIÓN DE ARCHIVOS:")
files = [
    'main.py',
    'signal_agent.py',
    'execution_agent.py',
    'feature_agent.py',
    'risk_guardian.py',
    'mt5_bridge.py',
    'test_smoke.py',
    'config_optimized.json',
    'logs/trade_audit_history.jsonl',
]

for f in files:
    if os.path.exists(f):
        mtime = datetime.fromtimestamp(os.path.getmtime(f))
        print(f"  {f:45s} → {mtime.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print(f"  {f:45s} → NO EXISTE")

# 3. Comparar
print()
print("=" * 80)
print("COMPARACIÓN CLAVE")
print("=" * 80)

main_mtime = datetime.fromtimestamp(os.path.getmtime('main.py'))
jsonl_mtime = datetime.fromtimestamp(os.path.getmtime(jsonl))

with open(jsonl, 'r', encoding='utf-8') as f:
    last_ts = None
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            r = json.loads(line)
            ts = r.get('timestamp')
            if ts:
                last_ts = ts
        except json.JSONDecodeError:
            continue

if last_ts:
    last_event = datetime.fromtimestamp(last_ts / 1000)
    print(f"\nÚltimo evento en JSONL:   {last_event.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Última modificación main.py: {main_mtime.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Última modificación JSONL:   {jsonl_mtime.strftime('%Y-%m-%d %H:%M:%S')}")

    if main_mtime > last_event:
        delta = (main_mtime - last_event).total_seconds() / 60
        print(f"\n✅ FASE 1 (main.py) fue modificado DESPUÉS del último trade.")
        print(f"   Diferencia: {delta:.1f} minutos tras el último trade.")
        print(f"   → Los trades del JSONL son ANTERIORES al fix.")
    else:
        delta = (last_event - main_mtime).total_seconds() / 60
        print(f"\n⚠️  Hay trades POSTERIORES a la modificación de main.py.")
        print(f"   Último trade fue {delta:.1f} minutos después del fix.")
        print(f"   → Hay que revisar si el fix se aplicó correctamente.")