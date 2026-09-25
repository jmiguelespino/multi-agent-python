# Changelog — QuantEdge AI

## [2026-09-24]
### Corregido
- **`.env`**: Eliminado `CAPITAL_BASE_USD` hardcodeado.
  El capital ahora se lee EN VIVO desde MT5 en todos los scripts.
- **`check_lots.py`**: Ahora lee el balance de MT5 como fuente principal.
- **`diagnostico_proyecto.py`**: Idem.

### Cambiado
- `MAX_DAILY_TRADES`: 6 → 25
- `MAX_CONCURRENT_POSITIONS`: 3 → 4
- `COOLDOWN_SECONDS`: 180 → 60
- `STOP_LOSS_CUARENTENA_SECONDS`: 600 → 300
- `CRUDE_MAX_LOT_SIZE`: 0.10 → 0.50
- `GOLD_MAX_LOT_SIZE`: 0.03 → 0.02
- `GOLD_ATR_STOP_MULTIPLIER`: 3.5 → 4.5
- `GOLD_ATR_PROFIT_MULTIPLIER`: 6.0 → 7.0
- `MAX_ALLOWED_SPREAD_BPS`: 5.0 → 15.0

### Añadido
- `check_lots.py` — Análisis de riesgo por activo con capital dinámico.
- `diagnostico_proyecto.py` — Estado del bot en un vistazo.

### Métricas
- Balance inicial: $1,733.99
- Balance actual: $1,875.82 (+8.18%)
- Órdenes ejecutadas hoy: 52
- Posiciones cerradas hoy: 28


# CHANGELOG — QuantEdge AI

Todos los cambios notables del proyecto se documentan en este archivo.
El formato sigue [Keep a Changelog](https://keepachangelog.com/es/1.1.0/)
y el versionado [SemVer](https://semver.org/lang/es/).

---

## [1.7.0] — 2026-09-24

### 🚨 CRÍTICO — FIX #1: Unificar WTI y BRENT como "OIL"

**Problema:**
El bot estaba expuesto al doble en petróleo: podía tener abierta una posición
en `XTIUSD` (WTI) y aceptar simultáneamente una señal de `XBRUSD` (BRENT),
acumulando riesgo duplicado en el mismo subyacente (crudo).

**Solución:**
Unificar ambos símbolos bajo el activo canónico `"OIL"` en las funciones
`get_canonical_asset()`.

**Archivos modificados:**
- `risk_guardian.py` → `get_canonical_asset()` + `elif canonical_sym == "OIL"`
- `execution_agent.py` → `get_canonical_asset()`

**Antes:**
```python
if "WTI" in s or "XTI" in s or ...:
    return "WTI"
if "BRENT" in s or "XBR" in s or "UKO" in s:
    return "BRENT"