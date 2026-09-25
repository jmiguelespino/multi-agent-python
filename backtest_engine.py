"""
=============================================================================
MOTOR DE BACKTEST — QuantEdge AI v2
=============================================================================
🔧 v2:
  • Filtro de fechas (start_date / end_date)
  • Filtro M15 real (agrupa M1 → M15, EMA20 M15)
  • Risk Guardian real con límites del .env:
      - MAX_CONCURRENT_POSITIONS
      - MAX_DAILY_TRADES
      - COOLDOWN_SECONDS
      - STOP_LOSS_CUARENTENA_SECONDS
      - MAX_ALLOWED_SPREAD_BPS
      - DAILY_DRAWDOWN_LIMIT_PCT
  • ATR se calcula en M1 (feature_agent)
  • SL/TP se calcula con ATR M1 (signal_agent)
=============================================================================
"""
import os
import math
import csv
import glob
from dataclasses import dataclass, field
from collections import deque, defaultdict
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timezone, timedelta


TZ_MT5 = timezone(timedelta(hours=3))


# =============================================================================
# Clasificación de activos
# =============================================================================
def get_canonical_asset(symbol: str) -> str:
    if not symbol:
        return ""
    s = symbol.upper().replace(".RAW", "").replace("_RAW", "").strip()
    if "BTC" in s: return "BTC"
    if "ETH" in s: return "ETH"
    if "SOL" in s: return "SOL"
    if "XAU" in s or "GOLD" in s: return "XAU"
    if "XAG" in s or "SILVER" in s: return "XAG"
    if any(k in s for k in ("WTI", "XTI", "BRENT", "XBR", "OIL")): return "OIL"
    if "US500" in s or "SP500" in s or "SPX" in s: return "US500"
    if any(fx in s for fx in ("EUR", "GBP", "JPY", "AUD", "NZD")): return "FOREX"
    return s


# =============================================================================
# Dataclasses
# =============================================================================
@dataclass(slots=True)
class Candle:
    time_ms: int
    open: float
    high: float
    low: float
    close: float
    tick_volume: int
    spread_points: int


@dataclass
class Position:
    symbol: str
    side: str
    volume: float
    entry_price: float
    stop_loss: float
    take_profit: float
    entry_time_ms: int

    break_even_activated: bool = False
    trailing_active: bool = False
    trailing_price: Optional[float] = None

    exit_price: Optional[float] = None
    exit_time_ms: Optional[int] = None
    exit_reason: Optional[str] = None
    pnl_usd: float = 0.0
    pnl_pct: float = 0.0


@dataclass
class FeatureVector:
    timestamp_ms: int
    price: float
    ema9: float
    ema21: float
    vwap: float
    rsi14: float
    atr14: float
    cvd: float
    candle_delta: float
    is_ready: bool


@dataclass
class BacktestStats:
    version: str
    total_trades: int = 0
    wins: int = 0
    losses: int = 0
    breakeven: int = 0
    gross_profit: float = 0.0
    gross_loss: float = 0.0
    total_pnl: float = 0.0
    max_dd: float = 0.0
    max_dd_pct: float = 0.0
    rejected_by_risk: Dict[str, int] = field(default_factory=lambda: defaultdict(int))
    equity_curve: List[float] = field(default_factory=list)

    @property
    def win_rate_pct(self) -> float:
        return (self.wins / self.total_trades * 100.0) if self.total_trades > 0 else 0.0

    @property
    def profit_factor(self) -> float:
        if self.gross_loss > 0:
            return self.gross_profit / self.gross_loss
        return 999.0 if self.gross_profit > 0 else 0.0

    @property
    def avg_win(self) -> float:
        return (self.gross_profit / self.wins) if self.wins > 0 else 0.0

    @property
    def avg_loss(self) -> float:
        return (-self.gross_loss / self.losses) if self.losses > 0 else 0.0


# =============================================================================
# Feature Calculator (M1)
# =============================================================================
class FeatureCalculator:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.ema9: Optional[float] = None
        self.ema21: Optional[float] = None
        self.avg_gain: Optional[float] = None
        self.avg_loss: Optional[float] = None
        self.prev_close: Optional[float] = None
        self.atr14: Optional[float] = None
        self.cvd: float = 0.0
        self.candles_closed: int = 0
        self.prev_candle: Optional[Candle] = None
        self.cum_pv: float = 0.0
        self.cum_vol: float = 0.0

    def _update_ema(self, prev, price, period):
        k = 2.0 / (period + 1)
        return price if prev is None else price * k + prev * (1 - k)

    def _update_rsi(self, price):
        if self.prev_close is None:
            self.prev_close = price
            return 50.0
        diff = price - self.prev_close
        self.prev_close = price
        gain = max(0.0, diff)
        loss = max(0.0, -diff)
        if self.avg_gain is None:
            self.avg_gain, self.avg_loss = gain, loss
            return 50.0
        self.avg_gain = (self.avg_gain * 13 + gain) / 14
        self.avg_loss = (self.avg_loss * 13 + loss) / 14
        if self.avg_gain == 0 and self.avg_loss == 0: return 50.0
        if self.avg_loss == 0: return 100.0
        rs = self.avg_gain / self.avg_loss
        return 100.0 - 100.0 / (1.0 + rs)

    def _update_atr_on_close(self, closed: Candle):
        if self.prev_candle is None:
            self.prev_candle = closed
            return
        h, l, pc = closed.high, closed.low, self.prev_candle.close
        tr = max(h - l, abs(h - pc), abs(l - pc))
        if tr <= 0:
            self.prev_candle = closed
            return
        if self.atr14 is None:
            self.atr14 = tr
        else:
            self.atr14 = (self.atr14 * 13 + tr) / 14
        self.prev_candle = closed

    def on_candle_close(self, c: Candle) -> FeatureVector:
        self.ema9 = self._update_ema(self.ema9, c.close, 9)
        self.ema21 = self._update_ema(self.ema21, c.close, 21)
        rsi = self._update_rsi(c.close)

        body_delta = c.close - c.open
        self.cvd += (1 if body_delta > 0 else -1) * c.tick_volume

        tp = (c.high + c.low + c.close) / 3.0
        self.cum_pv += tp * c.tick_volume
        self.cum_vol += c.tick_volume
        vwap = (self.cum_pv / self.cum_vol) if self.cum_vol > 0 else c.close

        self._update_atr_on_close(c)
        self.candles_closed += 1

        atr = self.atr14 if self.atr14 else 0.0

        return FeatureVector(
            timestamp_ms=c.time_ms,
            price=c.close,
            ema9=self.ema9 or c.close,
            ema21=self.ema21 or c.close,
            vwap=vwap,
            rsi14=rsi,
            atr14=atr,
            cvd=self.cvd,
            candle_delta=body_delta,
            is_ready=(self.candles_closed >= 20 and atr > 0),
        )


# =============================================================================
# M15 Aggregator
# =============================================================================
class M15Aggregator:
    """Agrupa velas M1 en M15 y calcula EMA20 M15."""

    def __init__(self):
        self.bucket_ms: Optional[int] = None
        self.current_candle: Optional[Candle] = None
        self.ema20: Optional[float] = None
        self.closes: deque = deque(maxlen=200)

    @staticmethod
    def _bucket(time_ms: int) -> int:
        """Retorna el inicio del bucket M15 al que pertenece time_ms."""
        return (time_ms // (15 * 60 * 1000)) * (15 * 60 * 1000)

    def on_candle_close(self, c: Candle) -> Optional[float]:
        """
        Procesa una vela M1 cerrada.
        Devuelve la EMA20 M15 más reciente (o None si no hay suficiente data).
        """
        bucket = self._bucket(c.time_ms)

        if self.bucket_ms is None:
            self.bucket_ms = bucket
            self.current_candle = Candle(
                time_ms=bucket,
                open=c.open, high=c.high, low=c.low, close=c.close,
                tick_volume=c.tick_volume, spread_points=c.spread_points,
            )
            return None

        if bucket > self.bucket_ms:
            # Cerró un M15 → procesar
            if self.current_candle is not None:
                self.closes.append(self.current_candle.close)
                self.ema20 = self._update_ema(self.ema20, self.current_candle.close, 20)

            self.bucket_ms = bucket
            self.current_candle = Candle(
                time_ms=bucket,
                open=c.open, high=c.high, low=c.low, close=c.close,
                tick_volume=c.tick_volume, spread_points=c.spread_points,
            )
        else:
            # Mismo bucket → actualizar high/low/close/volumen
            cc = self.current_candle
            cc.high = max(cc.high, c.high)
            cc.low = min(cc.low, c.low)
            cc.close = c.close
            cc.tick_volume += c.tick_volume

        return self.ema20

    @staticmethod
    def _update_ema(prev, price, period):
        k = 2.0 / (period + 1)
        return price if prev is None else price * k + prev * (1 - k)


# =============================================================================
# Signal Logic
# =============================================================================
class SignalLogic:
    W_TREND = 0.35
    W_MOMENTUM = 0.30
    W_ORDER_FLOW = 0.20
    W_VOLATILITY = 0.15

    def __init__(self, symbol, min_confidence, atr_stop_mult, atr_profit_mult):
        self.symbol = symbol
        self.min_confidence = min_confidence
        self.atr_stop_mult = atr_stop_mult
        self.atr_profit_mult = atr_profit_mult
        sym = symbol.upper()
        self.is_oil = any(k in sym for k in ("WTI", "XTI", "BRENT", "XBR", "OIL"))

    def evaluate(self, f: FeatureVector, m15_ema20: Optional[float]) -> Optional[Tuple]:
        if not f.is_ready or f.atr14 <= 0:
            return None

        is_bull = (f.ema9 > f.ema21) and (f.price > f.vwap)
        is_bear = (f.ema9 < f.ema21) and (f.price < f.vwap)
        trend_score = 1.0 if is_bull else (-1.0 if is_bear else 0.0)

        if self.is_oil:
            rsi_buy = (45.0, 72.0)
            rsi_sell = (28.0, 55.0)
        else:
            rsi_buy = (50.0, 66.0)
            rsi_sell = (34.0, 50.0)

        if rsi_buy[0] <= f.rsi14 <= rsi_buy[1]:
            momentum_score = 1.0
        elif rsi_sell[0] <= f.rsi14 <= rsi_sell[1]:
            momentum_score = -1.0
        else:
            momentum_score = 0.0

        of_score = 0.0
        if f.candle_delta > 0 and f.cvd > 0: of_score = 1.0
        elif f.candle_delta < 0 and f.cvd < 0: of_score = -1.0

        min_atr = f.price * 0.0001
        max_atr = f.price * 0.0100
        vol_score = 1.0 if (min_atr <= f.atr14 <= max_atr) else 0.2

        max_possible = self.W_TREND + self.W_MOMENTUM + self.W_ORDER_FLOW + self.W_VOLATILITY
        bull_raw = ((self.W_TREND if trend_score > 0 else 0)
                    + (self.W_MOMENTUM if momentum_score > 0 else 0)
                    + (self.W_ORDER_FLOW if of_score > 0 else 0)
                    + self.W_VOLATILITY * vol_score)
        bear_raw = ((self.W_TREND if trend_score < 0 else 0)
                    + (self.W_MOMENTUM if momentum_score < 0 else 0)
                    + (self.W_ORDER_FLOW if of_score < 0 else 0)
                    + self.W_VOLATILITY * vol_score)

        bull_conf = bull_raw / max_possible * 100
        bear_conf = bear_raw / max_possible * 100

        if bull_conf >= self.min_confidence and trend_score > 0 and momentum_score > 0:
            side, conf = "BUY", bull_conf
        elif bear_conf >= self.min_confidence and trend_score < 0 and momentum_score < 0:
            side, conf = "SELL", bear_conf
        else:
            return None

        # Filtro M15
        if m15_ema20 is not None:
            if side == "BUY" and f.price < m15_ema20:
                return None
            if side == "SELL" and f.price > m15_ema20:
                return None

        sl_dist = max(f.atr14 * self.atr_stop_mult, f.price * 0.0005)
        tp_dist = max(f.atr14 * self.atr_profit_mult, f.price * 0.0008)

        if side == "BUY":
            sl = f.price - sl_dist
            tp = f.price + tp_dist
        else:
            sl = f.price + sl_dist
            tp = f.price - tp_dist

        return (side, conf, sl, tp, f.atr14)


# =============================================================================
# Sizing
# =============================================================================
def contract_size(symbol):
    s = symbol.upper()
    if "XAU" in s: return 100.0
    if "XAG" in s: return 1000.0
    if any(k in s for k in ("BTC", "ETH", "SOL")): return 1.0
    if any(k in s for k in ("WTI", "XTI", "BRENT", "XBR", "OIL")): return 100.0
    if "US500" in s or "SP500" in s: return 1.0
    return 100000.0


def max_lot(canonical):
    if canonical == "XAU": return 0.02
    if canonical == "XAG": return 0.05
    if canonical == "OIL": return 0.50
    if canonical == "US500": return 0.50
    if canonical in ("BTC", "ETH", "SOL"): return 0.10
    return 0.10


def risk_pct(canonical):
    if canonical == "XAU": return 0.3
    return 0.5


# =============================================================================
# Load CSV
# =============================================================================
def load_candles_from_csv(filepath, start_date=None, end_date=None):
    candles = []
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader)
        for row in reader:
            if len(row) < 9:
                continue
            try:
                date_str = row[0].strip().replace(".", "-")
                time_str = row[1].strip()
                dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M:%S").replace(tzinfo=TZ_MT5)

                if start_date and dt.strftime("%Y-%m-%d") < start_date:
                    continue
                if end_date and dt.strftime("%Y-%m-%d") > end_date:
                    continue

                candles.append(Candle(
                    time_ms=int(dt.timestamp() * 1000),
                    open=float(row[2]), high=float(row[3]), low=float(row[4]), close=float(row[5]),
                    tick_volume=int(row[6]), spread_points=int(row[8]),
                ))
            except (ValueError, IndexError):
                continue
    return candles


# =============================================================================
# Risk Guardian (simplificado, con límites reales)
# =============================================================================
class RiskGuardian:
    def __init__(self, cfg):
        self.max_concurrent = cfg.get("max_concurrent_positions", 3)
        self.max_daily_trades = cfg.get("max_daily_trades", 20)
        self.cooldown_seconds = cfg.get("cooldown_seconds", 60)
        self.sl_quarantine_seconds = cfg.get("stop_loss_cuarentena_seconds", 300)
        self.max_spread_bps = cfg.get("max_allowed_spread_bps", 15.0)
        self.crypto_offhours_max_bps = cfg.get("crypto_offhours_max_spread_bps", 20.0)
        self.daily_dd_limit_pct = cfg.get("daily_drawdown_limit_pct", 3.0)

        self.active_count = 0
        self.active_symbols = set()
        self.last_trade_ts = 0.0
        self.last_sl_by_symbol = {}
        self.trades_today = 0
        self.current_day = None
        self.day_start_equity = 0.0
        self.cb_active = False

    def _check_daily_reset(self, day_key, equity):
        if self.current_day != day_key:
            self.current_day = day_key
            self.trades_today = 0
            self.day_start_equity = equity
            self.cb_active = False

    def evaluate(self, symbol, side, price, spread_bps, equity, day_key):
        canonical = get_canonical_asset(symbol)
        now = 0.0  # timestamp actual (no real en backtest)

        self._check_daily_reset(day_key, equity)

        # Circuit breaker
        if self.day_start_equity > 0:
            dd_pct = (self.day_start_equity - equity) / self.day_start_equity * 100
            if dd_pct >= self.daily_dd_limit_pct:
                self.cb_active = True
                return False, "CIRCUIT_BREAKER"

        if self.cb_active:
            return False, "CIRCUIT_BREAKER"

        # Cuota diaria
        if self.trades_today >= self.max_daily_trades:
            return False, "QUOTA_REACHED"

        # Doble exposición
        if canonical in self.active_symbols:
            return False, "MAX_POSITIONS_BLOCKED"

        # Concurrent positions
        if self.active_count >= self.max_concurrent:
            return False, "MAX_CONCURRENT"

        # Spread
        max_spread = self.max_spread_bps
        if canonical in ("BTC", "ETH", "SOL"):
            # En crypto, permitir más spread fuera de horario US (no modelado exacto aquí)
            max_spread = max(self.max_spread_bps, self.crypto_offhours_max_bps)
        if spread_bps > max_spread:
            return False, "SPREAD_TOO_HIGH"

        return True, None

    def register_open(self, symbol):
        canonical = get_canonical_asset(symbol)
        self.active_count += 1
        self.active_symbols.add(canonical)
        self.trades_today += 1

    def register_close(self, symbol, pnl, ts):
        canonical = get_canonical_asset(symbol)
        self.active_count = max(0, self.active_count - 1)
        self.active_symbols.discard(canonical)
        if pnl < 0:
            self.last_sl_by_symbol[canonical] = ts


# =============================================================================
# Motor principal
# =============================================================================
def run_backtest(version_name, config, datasets_dir, initial_capital=1750.0,
                 start_date=None, end_date=None):
    symbols = config.get("symbols", [])
    disabled = set(s.upper() for s in config.get("disabled_symbols", []))
    min_conf = config.get("min_confidence", 92.0)
    sl_by_class = config.get("atr_stop_multiplier_by_class", {})
    tp_by_class = config.get("atr_profit_multiplier_by_class", {})
    use_m15 = config.get("use_m15_filter", False)

    stats = BacktestStats(version=version_name)
    all_trades: List[Position] = []

    capital = initial_capital
    equity = initial_capital
    peak_equity = initial_capital

    # Localizar archivos
    files_by_sym = {}
    for sym in symbols:
        matches = glob.glob(os.path.join(datasets_dir, f"{sym}_M1_*.csv"))
        if matches:
            files_by_sym[sym] = matches[0]

    # Cargar features + M15 aggregators
    candles_by_sym = {}
    feature_calcs = {}
    m15_aggs = {}
    signal_logics = {}

    for sym, path in files_by_sym.items():
        candles = load_candles_from_csv(path, start_date, end_date)
        if not candles:
            continue
        candles_by_sym[sym] = candles
        feature_calcs[sym] = FeatureCalculator(sym)
        m15_aggs[sym] = M15Aggregator()
        canonical = get_canonical_asset(sym)
        signal_logics[sym] = SignalLogic(
            symbol=sym, min_confidence=min_conf,
            atr_stop_mult=sl_by_class.get(canonical, 1.8),
            atr_profit_mult=tp_by_class.get(canonical, 3.0),
        )

    # Índice unificado de tiempos
    all_times = set()
    for candles in candles_by_sym.values():
        for c in candles:
            all_times.add(c.time_ms)
    sorted_times = sorted(all_times)

    candles_index = {sym: {c.time_ms: c for c in candles} for sym, candles in candles_by_sym.items()}

    # Risk Guardian
    risk_cfg = {
        "max_concurrent_positions": config.get("max_concurrent_positions", 3),
        "max_daily_trades": config.get("max_daily_trades", 20),
        "cooldown_seconds": config.get("cooldown_seconds", 60),
        "stop_loss_cuarentena_seconds": config.get("stop_loss_cuarentena_seconds", 300),
        "max_allowed_spread_bps": config.get("max_allowed_spread_bps", 15.0),
        "crypto_offhours_max_spread_bps": config.get("crypto_offhours_max_spread_bps", 20.0),
        "daily_drawdown_limit_pct": config.get("daily_drawdown_limit_pct", 3.0),
    }
    risk = RiskGuardian(risk_cfg)

    active_positions: Dict[str, Position] = {}
    last_trade_ts_by_sym: Dict[str, int] = {}
    m15_ema20_by_sym: Dict[str, Optional[float]] = {s: None for s in candles_by_sym.keys()}

    for ts in sorted_times:
        day_key = datetime.fromtimestamp(ts / 1000, tz=TZ_MT5).strftime("%Y-%m-%d")

        for sym in list(feature_calcs.keys()):
            if sym.upper() in disabled:
                continue

            candle = candles_index[sym].get(ts)
            if candle is None:
                continue

            canonical = get_canonical_asset(sym)

            # Actualizar M15 (opcional)
            if use_m15:
                ema = m15_aggs[sym].on_candle_close(candle)
                if ema is not None:
                    m15_ema20_by_sym[sym] = ema

            # Actualizar features M1
            feat = feature_calcs[sym].on_candle_close(candle)

            # Gestionar posición abierta
            if sym in active_positions:
                pos = active_positions[sym]

                # BE
                if not pos.break_even_activated:
                    if pos.side == "BUY" and candle.high >= pos.entry_price + feat.atr14 * 1.2:
                        be_price = pos.entry_price + feat.atr14 * 0.10
                        if pos.stop_loss < be_price:
                            pos.stop_loss = be_price
                            pos.break_even_activated = True
                    elif pos.side == "SELL" and candle.low <= pos.entry_price - feat.atr14 * 1.2:
                        be_price = pos.entry_price - feat.atr14 * 0.10
                        if pos.stop_loss > be_price:
                            pos.stop_loss = be_price
                            pos.break_even_activated = True

                # Trailing
                if not pos.trailing_active:
                    if pos.side == "BUY" and candle.high >= pos.entry_price + feat.atr14 * 2.0:
                        pos.trailing_active = True
                        pos.trailing_price = candle.high - feat.atr14 * 1.8
                    elif pos.side == "SELL" and candle.low <= pos.entry_price - feat.atr14 * 2.0:
                        pos.trailing_active = True
                        pos.trailing_price = candle.low + feat.atr14 * 1.8
                elif pos.trailing_active:
                    if pos.side == "BUY":
                        new_trail = candle.high - feat.atr14 * 1.8
                        if new_trail > (pos.trailing_price or 0):
                            pos.trailing_price = new_trail
                            pos.stop_loss = max(pos.stop_loss, new_trail)
                    else:
                        new_trail = candle.low + feat.atr14 * 1.8
                        if new_trail < (pos.trailing_price or float("inf")):
                            pos.trailing_price = new_trail
                            pos.stop_loss = min(pos.stop_loss, new_trail)

                # SL/TP
                if pos.side == "BUY":
                    if candle.low <= pos.stop_loss:
                        pos.exit_price = pos.stop_loss
                        pos.exit_reason = "STOP_LOSS"
                    elif candle.high >= pos.take_profit:
                        pos.exit_price = pos.take_profit
                        pos.exit_reason = "TAKE_PROFIT"
                else:
                    if candle.high >= pos.stop_loss:
                        pos.exit_price = pos.stop_loss
                        pos.exit_reason = "STOP_LOSS"
                    elif candle.low <= pos.take_profit:
                        pos.exit_price = pos.take_profit
                        pos.exit_reason = "TAKE_PROFIT"

                if pos.exit_price is not None:
                    pos.exit_time_ms = ts
                    cs = contract_size(sym)
                    if pos.side == "BUY":
                        pnl = (pos.exit_price - pos.entry_price) * pos.volume * cs
                    else:
                        pnl = (pos.entry_price - pos.exit_price) * pos.volume * cs
                    pos.pnl_usd = round(pnl, 2)
                    notional = pos.entry_price * pos.volume * cs
                    pos.pnl_pct = round((pnl / notional) * 100, 4) if notional > 0 else 0.0

                    stats.total_trades += 1
                    if pnl > 0:
                        stats.wins += 1
                        stats.gross_profit += pnl
                    elif pnl < 0:
                        stats.losses += 1
                        stats.gross_loss += abs(pnl)
                    else:
                        stats.breakeven += 1

                    stats.total_pnl += pnl
                    equity += pnl
                    if equity > peak_equity:
                        peak_equity = equity
                    dd = peak_equity - equity
                    if dd > stats.max_dd:
                        stats.max_dd = dd
                        stats.max_dd_pct = (dd / peak_equity * 100) if peak_equity > 0 else 0

                    all_trades.append(pos)
                    del active_positions[sym]
                    risk.register_close(sym, pnl, ts)
                    continue

            # Nueva señal
            if sym in active_positions:
                continue

            # Cooldown por símbolo
            if ts - last_trade_ts_by_sym.get(sym, 0) < 60_000:
                continue

            # Cuarentena
            last_sl = risk.last_sl_by_symbol.get(canonical, 0)
            if (ts - last_sl) < risk.sl_quarantine_seconds * 1000:
                continue

            # Spread
            spread_bps = candle.spread_points / candle.close * 10000 if candle.close > 0 else 0

            # Risk Guardian
            allowed, reason = risk.evaluate(sym, None, candle.close, spread_bps, equity, day_key)
            if not allowed:
                stats.rejected_by_risk[reason] += 1
                continue

            # Señal
            m15_ema = m15_ema20_by_sym.get(sym) if use_m15 else None
            sig = signal_logics[sym].evaluate(feat, m15_ema)
            if sig is None:
                continue

            side, conf, sl, tp, atr = sig

            # Sizing
            risk_usd = equity * (risk_pct(canonical) / 100.0)
            stop_dist = abs(feat.price - sl)
            cs = contract_size(sym)
            size = round(risk_usd / (stop_dist * cs), 2) if stop_dist > 0 else 0.0
            size = min(size, max_lot(canonical))
            size = max(0.01, size)

            if size <= 0:
                continue

            pos = Position(
                symbol=sym, side=side, volume=size,
                entry_price=candle.close, stop_loss=sl, take_profit=tp,
                entry_time_ms=ts,
            )
            active_positions[sym] = pos
            last_trade_ts_by_sym[sym] = ts
            risk.register_open(sym)

        stats.equity_curve.append(equity)

    # Cerrar posiciones abiertas al final
    for sym, pos in active_positions.items():
        last_candle = candles_by_sym[sym][-1] if candles_by_sym.get(sym) else None
        if last_candle is None:
            continue
        pos.exit_price = last_candle.close
        pos.exit_reason = "END"
        pos.exit_time_ms = last_candle.time_ms
        cs = contract_size(sym)
        if pos.side == "BUY":
            pnl = (pos.exit_price - pos.entry_price) * pos.volume * cs
        else:
            pnl = (pos.entry_price - pos.exit_price) * pos.volume * cs
        pos.pnl_usd = round(pnl, 2)
        stats.total_trades += 1
        if pnl > 0:
            stats.wins += 1; stats.gross_profit += pnl
        elif pnl < 0:
            stats.losses += 1; stats.gross_loss += abs(pnl)
        stats.total_pnl += pnl
        all_trades.append(pos)

    return stats, all_trades