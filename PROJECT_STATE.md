# 📋 QUANTEDGE AI — ESTADO DEL PROYECTO

**Última actualización**: 2026-09-26 00:15 (UTC+3)
**Cuenta MT5**: 52974519 (ICMarketsSC-Demo)
**Capital base**: $1,731.03
**Estado del bot**: 🟢 CORRIENDO (solo cripto hasta domingo 18:00 UTC-3)

---

## 🎯 Historial de versiones

| Versión | Comentario en órdenes | Fecha | Estado |
|---|---|---|---|
| v1.x | `QuantEdge-Agente4`, `Comite AI` | 17-18/09 | Obsoleta |
| v2.x | `QuantEdge-Sniper` | 20-21/09 | Obsoleta |
| v3.x | `QuantEdge-Multi-Py` | 22-25/09 | Actual en uso |

**Rendimiento histórico real** (cuenta demo):
- 17-25/09: **+174 USD**, PF=1.235, Sharpe=0.075

---

## 🐛 Bugs corregidos (Lotes 1, 2, 2.5, 2.6+3, 3.5)

| ID | Bug | Fix | Archivo |
|---|---|---|---|
| B2 | Doble registro de posición | Eliminado `place_bracket_order` | `execution_agent.py`, `main.py` |
| B3 | Race en `active_positions_count` | Solo `sync_active_positions` controla | `risk_guardian.py` |
| B4 | `_update_mt5_sl` ignora `freeze_level` | `_get_min_stop_distance` | `execution_agent.py` |
| B5 | `UNKNOWN` → `MANUAL_CLOSE` | Añadido `CLOSE_UNKNOWN` | `audit_logger.py` |
| B6 | Learner NO filtra tests | Campo `is_test` en metadata | `audit_logger.py`, `feedback_learner.py` |
| B10 | TTL de locks 30s → 120s | +`notify_position_confirmed` | `risk_guardian.py` |
| B11 | PnL perdido si fetch falla | Estado `PENDING_PNL` con reintentos | `execution_agent.py` |
| B12 | `build_daily_report` duplicado | Nuevo `report_utils.py` | `main.py`, `daily_report.py` |
| B13 | Triple inconsistencia `min_confidence` | Unificado a 90.0 | `feedback_learner.py` |
| B14 | `atr_*_multiplier` no se propagan | `apply_learned_config_to_signal_agents` | `main.py` |
| B15 | Cierres huérfanos no detectados | `_scan_recent_deals_for_closures` | `execution_agent.py` |
| B16 | SL/TP invertidos | `_get_broker_min_distance` + validación | `signal_agent.py` |
| B17 | `MAX_CONCURRENT_POSITIONS` no respetado | Lock síncrono | `risk_guardian.py` |
| B18 | `unprofitable_symbols` no usado | Análisis por símbolo | `feedback_learner.py` |
| B19 | Learner pisa multiplicadores ATR | `clamp_atr_by_class` | `feedback_learner.py`, `signal_agent.py` |
| **B20** | **`disabled_symbols` con min_trades=5** | **min_trades=30 + histéresis + re-habilitación** | **`feedback_learner.py` v1.5.1** |
| B21 | Cuarentena por racha de pérdidas | Escalonada 1h/6h/24h | `risk_guardian.py` |
| **B23** | **`atr_profit_mult` acumulaba hasta 13.65** | **Clamp duro SL∈[1,6], TP∈[2,9]** | **`feedback_learner.py` v1.5.1** |
| O1 | `import MT5` dentro de `_check_macro_trend` | A nivel módulo | `signal_agent.py` |
| O2 | Bucle `orders × symbols` ineficiente | Invertido | `main.py` |
| O3 | Buffer + flush en `audit_logger` | `_BufferedWriter` | `audit_logger.py` |
| O4 | Cache M15 con TTL | `_get_m15_rates_cached` | `signal_agent.py` |
| O5 | Test 14 PnL retry lento | `max_retries=1` | `test_smoke.py` |

---

## 🚨 PENDIENTE: Backtest con 4 bugs críticos

**Estado**: el motor de backtest existe pero sus resultados NO son válidos.

### Bugs identificados

| # | Bug | Evidencia | Fix pendiente |
|---|---|---|---|
| **BT-1** | `spread_bps` mal calculado (falta `point_size`) | `SPREAD_TOO_HIGH: 593,582 rechazos` | Multiplicar `spread_points × point_size` antes de dividir por precio |
| **BT-2** | `QUOTA_REACHED` mal contado | `144,947 rechazos` | El contador diario se resetea mal |
| **BT-3** | `CIRCUIT_BREAKER` no se resetea diario | `4,641 rechazos` + CB queda activo siempre | Resetear CB cada día UTC |
| **BT-4** | Solo opera XAUUSD y BTCUSD | 8 símbolos → solo 2 operan | Combinación de BT-1, BT-2, BT-3 |
| **BT-5** | BE demasiado agresivo | avg win +1.67 vs avg loss -8.18 | Subir `be_trigger_atr` de 1.2 a 2.5 |

### Diagnóstico

**El bot REAL es rentable (+174 USD en 9 días). El backtest dice -285 USD.**
**La discrepancia es por los 5 bugs del motor de backtest.**

### Archivos del backtest

- `backtest_engine.py` — motor v3 (con bugs parcialmente arreglados, pendiente de testear)
- `backtest.py` — runner
- `backtest_config.json` — config (start_date/end_date/nulled)
- `datasets/` — 8 CSVs M1 + 8 M5 + 8 M15

---

## 📂 Estructura actual del proyecto
