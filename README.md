# 🚀 QuantEdge AI — Motor Autónomo de Trading Algorítmico Institucional

**QuantEdge AI** es un sistema autónomo de trading cuantitativo de alta precisión
desarrollado en Python y diseñado para operar directamente en **MetaTrader 5**
(IC Markets SC Demo).

A diferencia de los asesores expertos (EAs) tradicionales basados en indicadores
rezagados o cuadrículas de alto riesgo (Grid/Martingala), QuantEdge AI emplea una
**arquitectura multi-agente en tiempo real** que evalúa confluencias matemáticas
avanzadas, controla el riesgo de forma estricta y adapta sus parámetros mediante
aprendizaje continuo.

> 📌 **Versión:** 1.7.0 — Ver [CHANGELOG.md](./CHANGELOG.md) para los últimos fixes.

---

## 🌟 Arquitectura Multi-Agente (5 Agentes Especializados)
┌───────────────────────────────────────────────────────────────────────┐
│ main.py — Orquestador │
│ (asyncio event loop multi-activo) │
└───────────────┬───────────────────────────────────────────────────────┘
│
┌───────────┼────────────┬─────────────┬──────────────┐
▼ ▼ ▼ ▼ ▼
┌────────┐ ┌─────────┐ ┌──────────┐ ┌───────────┐ ┌──────────────┐
│Agente 1│ │Agente 2 │ │ Agente 3 │ │ Agente 4 │ │ Agente 5 │
│Feature │ │Signal │ │ Risk │ │ Execution │ │ Feedback │
│ Agent │ │ Agent │ │ Guardian │ │ OMS │ │ Learner │
└────┬───┘ └────┬────┘ └─────┬────┘ └─────┬─────┘ └──────┬───────┘
│ │ │ │ │
│ EMA9/21 │ Conf≥86% │ 1% riesgo │ Bracket │ Lee logs
│ VWAP │ SL/TP │ 3% DD │ Break-Even │ Ajusta
│ RSI/ATR │ ATR-based │ 25 trades │ Trailing │ umbral
│ CVD │ M15 filter │ 60s cool │ │
└──────────┴────────────┴────────────┴──────────────┘
│
▼
┌──────────────────────┐
│ MetaTrader 5 (IPC) │
│ IC Markets SC Demo │
└──────────────────────┘
│
┌───────────────┼──────────────┐
▼ ▼ ▼
┌──────────┐ ┌────────────┐ ┌────────────┐
│ audit_ │ │ telegram_ │ │ mt5_ │
│ logger │ │ notifier │ │ bridge │
│ (JSONL) │ │ │ │ (WS :8001) │
└──────────┘ └────────────┘ └────────────┘


### Agentes

| # | Archivo | Rol |
|---|---------|-----|
| 1 | `feature_agent.py` | Ingesta de ticks, cálculo **O(1)** de EMA 9/21, VWAP + bandas, RSI 14, ATR 14 (Wilder), CVD |
| 2 | `signal_agent.py` | Estrategia de **Confluencia Sniper** ≥ 86% (tendencia, momentum, order flow, volatilidad) + **filtro de tendencia macro M15 (EMA20)** |
| 3 | `risk_guardian.py` | Guardián institucional: **1% riesgo/trade** (0.3% en Oro), 3% DD diario, 25 trades/día, 60s cooldown, cuarentena 300s tras SL |
| 4 | `execution_agent.py` | OMS con **Break-Even +1.2×ATR**, **Trailing +2.0×ATR**, gestión de SL en MT5 |
| 5 | `feedback_learner.py` | Aprendizaje continuo: lee `trade_audit_history.jsonl`, ajusta umbral de confluencia según win rate y profit factor |

### Módulos de soporte

| Archivo | Rol |
|---------|-----|
| `main.py` | Orquestador asyncio multi-activo |
| `mt5_bridge.py` | Puente WebSocket puerto `8001` para panel web |
| `data_streamer.py` | Manager WebSocket Binance (L1) con reconexión exponencial |
| `audit_logger.py` | Registro inmutable JSONL + salida limpia en consola |
| `telegram_notifier.py` | Alertas Telegram con anti-spam (1 msg / 5s, máx 5 / 10 min) |
| `test_smoke.py` | Validación automática de fixes (7 tests, no requiere MT5) |

---

## 🌍 Operativa Multi-Activo Dinámica

Un solo motor monitorea y opera simultáneamente una cartera diversificada
configurada desde `.env`:

- **Materias Primas:** Oro (`XAUUSD`), Plata (`XAGUSD`), Petróleo (`XTIUSD` / WTI, `XBRUSD` / BRENT)
- **Divisas / Forex:** `EURUSD`, `GBPUSD`
- **Criptomonedas:** `BTCUSD`, `ETHUSD`, `SOLUSD` (con tolerancia adaptativa de spread fuera de horario bancario)
- **Índices:** `US500` (S&P 500)

> ⚠️ **Nota crítica (v1.7.0):** WTI y BRENT comparten el activo canónico **`OIL`**
> para evitar doble exposición al mismo subyacente (crudo). Si tienes `XTIUSD`
> abierto y llega señal de `XBRUSD`, **se rechaza automáticamente**.
>
> 🔧 **Aplicado en:** `risk_guardian.py`, `execution_agent.py` y **`mt5_bridge.py`**
> (los 3 módulos que gestionan exposición).

---

## 🛡️ Protección de Capital — Valores Reales en Código v1.7.0

| Parámetro | Valor real | Fuente (`.env`) |
|-----------|------------|-----------------|
| Riesgo por operación (general) | 1.0% | `MAX_RISK_PER_TRADE_PCT` |
| Riesgo por operación (Oro) | 0.3% | `GOLD_MAX_RISK_PCT` |
| Riesgo por operación (Cripto) | 1.0% | `CRYPTO_MAX_RISK_PCT` |
| Drawdown diario máximo | 3.0% | `DAILY_DRAWDOWN_LIMIT_PCT` |
| Máx. trades por día | 25 | `MAX_DAILY_TRADES` |
| Máx. posiciones simultáneas | 5 | `MAX_CONCURRENT_POSITIONS` |
| Cooldown entre trades | 60 s | `COOLDOWN_SECONDS` |
| Cuarentena tras Stop Loss | 300 s (5 min) | `STOP_LOSS_CUARENTENA_SECONDS` |
| Spread máximo (general) | 15.0 bps | `MAX_ALLOWED_SPREAD_BPS` |
| Spread máximo (cripto off-hours) | 20.0 bps | `CRYPTO_OFFHOURS_MAX_SPREAD_BPS` |
| Tope de lotes OIL (WTI+BRENT) | 0.50 | `CRUDE_MAX_LOT_SIZE` |
| Tope de lotes Oro | 0.02 | `GOLD_MAX_LOT_SIZE` |
| Tope de lotes Cripto | 0.10 | `CRYPTO_MAX_LOT_SIZE` |

### Multiplicadores ATR reales (v1.7.0)

| Activo | Stop Loss | Take Profit | R:R |
|--------|-----------|-------------|-----|
| **Oro** (XAUUSD) | 4.5× ATR | 7.0× ATR | 1:1.56 |
| **Plata** (XAGUSD) | 2.5× ATR | 4.0× ATR | 1:1.60 |
| **Petróleo** (WTI/BRENT) | 1.8× ATR | 3.0× ATR | 1:1.67 |
| **Forex** (EURUSD/GBPUSD) | 1.2× ATR | 2.0× ATR | 1:1.67 |
| **Cripto** (BTC/ETH/SOL) | 2.2× ATR | 3.8× ATR | 1:1.73 |
| **Índices** (US500) | 2.0× ATR | 3.5× ATR | 1:1.75 |
| **General** (fallback) | 1.8× ATR | 3.0× ATR | 1:1.67 |

### Blindaje dinámico (Agente 4)

| Evento | Trigger | Acción |
|--------|---------|--------|
| **Break-Even** | Precio ≥ entrada + 1.2× ATR | SL → entrada + 0.10× ATR |
| **Trailing Stop** | Precio ≥ entrada + 2.0× ATR | SL → precio − 1.8× ATR (y se actualiza) |
| **Cuarentena** | Cierre con PnL < 0 | Bloqueo del activo 300 s (5 min) |
| **Circuit Breaker** | DD diario ≥ 3% | Bloqueo total de nuevas órdenes |
| **Anti-Doble-Exposición** | `OIL` ya activo (WTI o BRENT) | Rechazo de nueva señal en `OIL` |

### Filtro de tendencia macro (Agente 2 — v1.7.0)

| Timeframe | Indicador | Regla |
|-----------|-----------|-------|
| **M15** | EMA 20 | BUY solo si `precio > EMA20_M15` |
| **M15** | EMA 20 | SELL solo si `precio < EMA20_M15` |
| — | Fail-safe | Si no hay datos o error → permite (no bloquea) |

**Ejemplo:**
- BTCUSD bajando en M15 → señal BUY **rechazada** ✅
- XBRUSD subiendo en M15 → señal BUY **aceptada** ✅

---

## 📋 Requisitos Previos

1. **Windows 10/11 o Windows Server** (64-bit).
   La librería nativa `MetaTrader5` requiere `terminal64.exe` vía IPC.
   **No funciona en Linux/macOS** sin Wine o VPS Windows.

2. **Python 3.10, 3.11 o 3.12** (64-bit). Marcar *"Add Python to PATH"*.

3. **MetaTrader 5 instalado** (versión de IC Markets recomendada), con sesión
   iniciada en la cuenta Demo.
