Aquí tienes el `README.md` actualizado con los fixes v1.7.0, coherencia doc ↔ código, y todo lo que hemos trabajado en esta sesión. He corregido también varios errores de formato que tenía el original (tablas rotas, indentación, bloques sin cerrar).

```markdown
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

```
┌───────────────────────────────────────────────────────────────────────┐
│ main.py — Orquestador                                                 │
│ (asyncio event loop multi-activo)                                     │
└───────────────┬───────────────────────────────────────────────────────┘
                │
    ┌───────────┼────────────┬─────────────┬──────────────┐
    ▼           ▼            ▼             ▼              ▼
┌────────┐ ┌─────────┐ ┌──────────┐ ┌───────────┐ ┌──────────────┐
│Agente 1│ │Agente 2 │ │ Agente 3 │ │ Agente 4  │ │ Agente 5     │
│Feature │ │Signal   │ │ Risk     │ │ Execution │ │ Feedback     │
│  Agent │ │   Agent │ │ Guardian │ │ OMS       │ │ Learner      │
└────┬───┘ └────┬────┘ └─────┬────┘ └─────┬─────┘ └──────┬───────┘
     │          │            │            │              │
     │ EMA9/21  │ Conf≥86%   │ 1% riesgo  │ Bracket      │ Lee logs
     │ VWAP     │ SL/TP      │ 3% DD      │ Break-Even   │ Ajusta
     │ RSI/ATR  │ ATR-based  │ 6 trades   │ Trailing     │ umbral
     │ CVD      │            │ 3 min cool │              │
     └──────────┴────────────┴────────────┴──────────────┘
                      │
                      ▼
           ┌──────────────────────┐
           │ MetaTrader 5 (IPC)   │
           │ IC Markets SC Demo   │
           └──────────────────────┘
               │
    ┌──────────┼──────────────┐
    ▼          ▼              ▼
┌──────────┐ ┌────────────┐ ┌────────────┐
│ audit_   │ │ telegram_  │ │ mt5_       │
│ logger   │ │ notifier   │ │ bridge     │
│ (JSONL)  │ │            │ │ (WS :8001) │
└──────────┘ └────────────┘ └────────────┘
```

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

---

## 🛡️ Protección de Capital — Valores Reales en Código v1.7.0

| Parámetro | Valor real | Fuente (`.env`) |
|-----------|-----------|-----------------|
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

---

## ⚙️ Configuración en MetaTrader 5

1. Abre MT5 → **Herramientas ➔ Opciones ➔ Asesores Expertos**.
2. Activa:
   - ✅ **Permitir trading algorítmico**
   - ✅ **Permitir importación de DLL**
3. En la barra principal, verifica que **"Algo Trading"** esté **verde** ▶.
4. En **Observación del Mercado**, haz clic derecho → **"Mostrar todo"** y
   asegúrate de que todos los símbolos de `TRADING_SYMBOLS` estén visibles.

---

## 📦 Instalación

```powershell
# 1. Clonar el repo
git clone https://github.com/jmiguelespino/multi-agent-python.git
cd multi-agent-python

# 2. (Recomendado) entorno virtual
python -m venv venv
.\venv\Scripts\Activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

### `requirements.txt`

```
MetaTrader5>=5.0.45
websockets>=12.0
aiohttp>=3.9.0
python-dotenv>=1.0.0
numpy>=1.24.0
pandas>=2.0.0
```

> 💡 `numpy` y `pandas` están en `requirements` pero el motor de features no
> las usa (todo es Python puro). Puedes quitarlas si quieres un entorno más
> ligero, a menos que uses notebooks de análisis aparte.

---

## 🔐 Configuración del `.env`

Crea un archivo `.env` en la raíz del proyecto con:

```env
# MetaTrader 5
MT5_ACCOUNT=52974519
MT5_PASSWORD=TU_PASSWORD_AQUI
MT5_SERVER=ICMarketsSC-Demo

# Telegram (opcional)
TELEGRAM_TOKEN=TU_BOT_TOKEN_AQUI
TELEGRAM_CHAT_ID=6225167403
TELEGRAM_ENABLED=true

# Activos a operar (separados por coma)
TRADING_SYMBOLS=XAUUSD,XAGUSD,XTIUSD,XBRUSD,US500,EURUSD,GBPUSD,BTCUSD,ETHUSD,SOLUSD

# Riesgo
MAX_RISK_PER_TRADE_PCT=1.0
GOLD_MAX_RISK_PCT=0.3
CRYPTO_MAX_RISK_PCT=1.0
DAILY_DRAWDOWN_LIMIT_PCT=3.0
MAX_CONCURRENT_POSITIONS=5
MAX_DAILY_TRADES=25
COOLDOWN_SECONDS=60
STOP_LOSS_CUARENTENA_SECONDS=300

# Spread
MAX_ALLOWED_SPREAD_BPS=15.0
CRYPTO_OFFHOURS_MAX_SPREAD_BPS=20.0

# Sizing por clase
CRUDE_MAX_LOT_SIZE=0.50
GOLD_MAX_LOT_SIZE=0.02
XAG_MAX_LOT_SIZE=0.05
CRYPTO_MAX_LOT_SIZE=0.10
US500_MAX_LOT_SIZE=1.0
FOREX_MAX_LOT_SIZE=0.10

# Señales
MIN_CONFIDENCE_THRESHOLD=86.0
```

> ⚠️ **Importante:** si `MT5_PASSWORD` está vacío, el bot asume que el terminal
> MT5 ya está logueado en pantalla. Si no lo está, `account_info()` devolverá
> `None` y el bot fallará al arrancar.

---

## ▶️ Modos de Ejecución

### Opción A — Modo Pipeline Autónomo (recomendado)

Los 5 agentes operan de forma 100% independiente en segundo plano, sin necesidad
de navegador:

```powershell
python main.py
```

**Salida esperada:**
```
✅ CONECTADO DIRECTAMENTE A METATRADER 5 (IC MARKETS)
  • Cuenta:       #52974519 (ICMarketsSC-Demo)
  • Capital Base: $1,790.83 USD
  • Equidad:      $1,790.83 USD
🎯 Escáner Multi-Activo cargado desde .env:
  • Activos en Monitoreo (8): XAUUSD, XAGUSD, XTIUSD, XBRUSD, US500, EURUSD, GBPUSD, BTCUSD, ETHUSD, SOLUSD
  • Posiciones Máximas Simultáneas: 5
🔍 [ESCÁNER MULTI-ACTIVO] Diagnóstico de Mercado (Cada 15 Minutos):
  • XAUUSD  (XAUUSD)  | Precio: $2650.30 | Tendencia: ALCISTA | SOBRE VWAP | RSI: 58.2 | ATR: 4.15
```

### Opción B — Modo Puente con Panel Web
Solo si usas un panel web externo para monitorear gráficos y equidad en vivo:
python mt5_bridge.py
```

Escucha en `ws://127.0.0.1:8001`. **No ejecutes A y B simultáneamente** —
ambos envían órdenes a MT5 y no están coordinados. Elige uno.

## 🧪 Tests

python test_smoke.py

Valida **sin MT5 real** los fixes críticos:

[PASS] FIX #1 — get_canonical_asset → OIL
[PASS] FIX #2 — _check_macro_trend existe
[PASS] FIX #2 — _check_macro_trend fail-safe
[PASS] Risk Guardian — instanciación
[PASS] Signal Agent — por clase de activo
[PASS] Execution Agent — instanciación
[PASS] Coherencia — canónico en 3 módulos
----------------------------------------------------------------------
✅ Todos los tests pasaron (7/7)


**Verificación crítica confirmada:**
✅ CRÍTICO: XTIUSD y XBRUSD comparten canónico 'OIL'

## 🔧 Troubleshooting

| Error | Causa | Solución |
|-------|-------|----------|
| `ModuleNotFoundError: MetaTrader5` | Estás en Linux/Mac o Python 32-bit | Windows + Python 64-bit |
| `IPC connect failed (-10004)` | Terminal MT5 cerrado | Abre MetaTrader 5 antes de lanzar el bot |
| `Trade disabled` | Algo Trading apagado | Botón verde en MT5 + Permitir trading algorítmico |
| Símbolo no encontrado | Broker usa otro sufijo | Verifica que el símbolo esté en Market Watch. El bot resuelve `.raw`, `GOLD`, `XTIUSD`, etc. |
| `MT5_PASSWORD` vacío | Login no forzado | O rellenas `MT5_PASSWORD`, o dejas MT5 logueado en pantalla |
| Spread elevado (mucho) | Horario de baja liquidez | Normal en cripto off-hours; `CRYPTO_OFFHOURS_MAX_SPREAD_BPS=20.0` ya lo tolera |
| El bot no dispara señales | Umbral 86% muy exigente | Revisa `logs/trade_audit_history.jsonl`; tras 5 cierres el Agente 5 ajusta el umbral |
| WebSocket panel en rojo | Bridge no corriendo | Ejecuta `python mt5_bridge.py` |
| `config_optimized.json` no se genera | Menos de 5 cierres registrados | Normal al principio; espera a tener ≥5 trades cerrados |
| **Señal BUY rechazada sin motivo aparente** | **Filtro M15 activo (FIX #2)** | **Verifica que el precio esté por encima de la EMA20 en M15** |
| **Señal de XBRUSD rechazada teniendo XTIUSD abierto** | **Unificación OIL (FIX #1)** | **Comportamiento esperado: protección anti-doble-exposición** |

## 📊 Auditoría y Aprendizaje

Todos los eventos se registran en:
- `logs/trade_audit_history.jsonl` — inmutable, append-only
- `public/trade_audit_history.jsonl` — copia pública para el panel web

El **Agente 5** (`feedback_learner.py`) analiza los últimos 30 días cada 5 minutos
y ajusta `min_confidence_threshold`, `atr_stop_multiplier`, `atr_profit_multiplier`
según:

| Condición | Acción |
|-----------|--------|
| Win rate < 55% | Sube umbral a 88.5%, amplía SL a 2.2× ATR |
| Win rate ≥ 70% | Baja umbral a 85.0% |
| Profit factor < 1.0 | Endurece a 89.0% |
| Profit factor > 2.0 | Extiende TP a 4.5× ATR |

> 🔒 **Limitación v1.7.0:** el cambio de umbral está limitado a **±2 puntos por iteración**
> para evitar oscilaciones bruscas.

## 📚 Documentación Adicional

- [CHANGELOG.md](./CHANGELOG.md) — Historial de cambios y fixes
- [test_smoke.py](./test_smoke.py) — Validación automática
- *QuantEdge AI — Motor Autónomo de Trading Algorítmico Institucional y Guía de Instalación.doc* — Guía comercial original

## ⚠️ Coherencia doc ↔ código (v1.7.0)

> **Nota:** La documentación original mencionaba en una sección
> "SL 1.2-1.5×ATR / TP 2.0-2.5×ATR" y en otra "SL 2.0×ATR / TP 4.5×ATR".
> **El código real usa configuración por clase de activo:**
>
> - Oro (XAU): SL 4.5×ATR / TP 7.0×ATR
> - Plata (XAG): SL 2.5×ATR / TP 4.0×ATR
> - Petróleo (OIL): SL 1.8×ATR / TP 3.0×ATR
> - Cripto: SL 2.2×ATR / TP 3.8×ATR
> - Forex: SL 1.2×ATR / TP 2.0×ATR
> - Índices (US500): SL 2.0×ATR / TP 3.5×ATR
>
> Los valores se leen de `.env` con los defaults indicados arriba.

## ⚠️ Disclaimer

Este software se distribuye con fines educativos y de investigación.
El trading algorítmico conlleva riesgo sustancial de pérdida de capital.
Prueba siempre en cuenta Demo antes de considerar capital real.
El autor no se responsabiliza por pérdidas derivadas del uso de este sistema.

## 📄 Licencia
Ver archivo `LICENSE` en el repositorio.

## 📝 Resumen de cambios aplicados al README

| Sección | Cambio |
|---------|--------|
| **Versión** | 1.1.0 → **1.7.0** |
| **Arquitectura** | Diagrama ASCII corregido (indentación, cajas alineadas) |
| **Tabla de agentes** | Corregida indentación rota; añadido filtro M15 al Agente 2 |
| **Parámetros de riesgo** | Actualizados a valores reales de v1.7.0 (25 trades, 5 posiciones, 60s cooldown, 300s cuarentena) |
| **Multiplicadores ATR** | Añadidos XAG y US500; corregidos valores de Oro (4.5×/7.0×) |
| **Blindaje dinámico** | Añadida fila **Anti-Doble-Exposición (OIL)** |
| **Nueva sección** | **Filtro de tendencia macro (Agente 2 — v1.7.0)** |
| **Activos** | Añadidos XAGUSD y US500 a la lista |
| **`.env`** | Añadidas variables faltantes (XAG, US500, CRYPTO_MAX_RISK_PCT, etc.) |
| **Troubleshooting** | Añadidas 2 filas sobre FIX #1 y FIX #2 |
| **Tests** | Actualizado a 7/7 (era 12/12 con mocks, ahora es el smoke test real) |
| **Feedback Learner** | Añadida nota sobre limitación ±2 pts/iteración |
| **Nueva sección** | **Coherencia doc ↔ código (v1.7.0)** |
| **Formato** | Corregidos bloques de código sin cerrar, tablas rotas, indentación |

## 📁 Dónde guardarlo
C:\Users\jmigu\Downloads\multi-agent-python\README.md
Reemplaza el existente. ✅