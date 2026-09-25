"""
AGENTE 1: INGESTION & FEATURE ENGINEERING AGENT

🔧 v1.4.1:
  • 🐛 MIN_ATR recalibrados para el mercado actual.
    Antes: BTC=50, ETH=3.0, SOL=0.10 (demasiado altos, forzaban SL/TP
    desproporcionados en cripto cuando el ATR real era menor).
    Ahora: BTC=20, ETH=1.0, SOL=0.03.
  • 🆕 WARMUP: el FeatureVector expone `is_ready` que solo es True cuando
    hay ≥20 velas cerradas y el ATR14 está calculado con Wilder real.
  • 🐛 MEJORA #5: MIN_ATR para XAG (Plata) y US500 (S&P 500).
  • VWAP O(1) + ATR Wilder.
"""
import math
from collections import deque
from dataclasses import dataclass
from typing import Optional
from data_streamer import Tick


# =============================================================================
# CONSTANTE DE WARMUP
# =============================================================================
MIN_CANDLES_FOR_READY = 20


@dataclass(slots=True)
class Candle:
    timestamp_ms: int
    open: float
    high: float
    low: float
    close: float
    volume: float
    buy_volume: float
    sell_volume: float
    trades_count: int
    closed: bool = False


@dataclass(slots=True)
class FeatureVector:
    timestamp_ms: int
    price: float
    ema9: float
    ema21: float
    vwap: float
    vwap_upper_1: float
    vwap_lower_1: float
    vwap_upper_2: float
    vwap_lower_2: float
    rsi14: float
    atr14: float
    cvd: float
    candle_delta: float
    # 🆕 v1.4.0: flag de warmup
    is_ready: bool = False
    candles_closed: int = 0


class IngestionFeatureAgent:
    # 🐛 v1.4.1: MIN_ATR recalibrados
    MIN_ATR_BY_CLASS = {
        "XAU": 0.50,       # Oro: $0.50
        "XAG": 0.02,       # Plata: $0.02
        "WTI": 0.05,       # Petróleo: $0.05
        "BRENT": 0.05,
        "BTC": 20.0,       # 🆕 BTC: $20 (antes 50)
        "ETH": 1.0,        # 🆕 ETH: $1 (antes 3)
        "SOL": 0.03,       # 🆕 SOL: $0.03 (antes 0.10)
        "US500": 0.50,     # S&P 500: 0.50 puntos
        "FOREX": 0.00015,  # Forex: 1.5 pips
    }

    def __init__(self, symbol: str = "XAUUSD", candle_period_ms: int = 60000, history_length: int = 200):
        self.symbol = symbol
        self.candle_period_ms = candle_period_ms
        self.candles: deque[Candle] = deque(maxlen=history_length)
        self.current_candle: Optional[Candle] = None

        self.ema9: Optional[float] = None
        self.ema21: Optional[float] = None
        self.cvd: float = 0.0

        self.rsi_period = 14
        self.avg_gain: Optional[float] = None
        self.avg_loss: Optional[float] = None
        self.prev_close: Optional[float] = None

        self.atr14: Optional[float] = None

        self._sum_pv: float = 0.0
        self._sum_v: float = 0.0
        self._sum_pv2: float = 0.0
        self._vwap: float = 0.0
        self._vwap_stdev: float = 0.0

        self.last_feature_vector: Optional[FeatureVector] = None
        self.candles_closed_count: int = 0

    # -------------------------------------------------------------------------
    # WARMUP
    # -------------------------------------------------------------------------
    def is_ready(self) -> bool:
        """
        Indica si el agente tiene datos suficientes para generar señales fiables.
        Requiere:
          • ≥20 velas cerradas (MIN_CANDLES_FOR_READY).
          • ATR14 calculado con Wilder real (self.atr14 is not None).
        """
        return (
            self.candles_closed_count >= MIN_CANDLES_FOR_READY
            and self.atr14 is not None
            and self.atr14 > 0
        )

    # -------------------------------------------------------------------------
    # ATR mínimo según clase de activo
    # -------------------------------------------------------------------------
    def _get_min_atr(self) -> float:
        s = self.symbol.upper()
        if "XAU" in s or "GOLD" in s:
            return self.MIN_ATR_BY_CLASS["XAU"]
        if "XAG" in s or "SILVER" in s:
            return self.MIN_ATR_BY_CLASS["XAG"]
        if "WTI" in s or "XTI" in s or "OIL" in s:
            return self.MIN_ATR_BY_CLASS["WTI"]
        if "BRENT" in s or "XBR" in s:
            return self.MIN_ATR_BY_CLASS["BRENT"]
        if "BTC" in s:
            return self.MIN_ATR_BY_CLASS["BTC"]
        if "ETH" in s:
            return self.MIN_ATR_BY_CLASS["ETH"]
        if "SOL" in s:
            return self.MIN_ATR_BY_CLASS["SOL"]
        if "US500" in s or "SP500" in s or "SPX" in s:
            return self.MIN_ATR_BY_CLASS["US500"]
        if any(fx in s for fx in ["EUR", "GBP", "JPY", "AUD", "NZD"]):
            return self.MIN_ATR_BY_CLASS["FOREX"]
        return 0.001

    # -------------------------------------------------------------------------
    # Helpers VWAP
    # -------------------------------------------------------------------------
    @staticmethod
    def _typical_price(c: Candle) -> float:
        return (c.high + c.low + c.close) / 3.0

    def _add_candle_to_vwap_accumulators(self, c: Candle):
        tp = self._typical_price(c)
        self._sum_pv += tp * c.volume
        self._sum_v += c.volume
        self._sum_pv2 += (tp * tp) * c.volume

    def _rebuild_vwap_accumulators(self):
        self._sum_pv = 0.0
        self._sum_v = 0.0
        self._sum_pv2 = 0.0
        for c in self.candles:
            self._add_candle_to_vwap_accumulators(c)
        if self.current_candle is not None:
            self._add_candle_to_vwap_accumulators(self.current_candle)

    def _recompute_vwap(self):
        if self._sum_v <= 0:
            ref_price = self.current_candle.close if self.current_candle else 0.0
            self._vwap = ref_price
            self._vwap_stdev = 0.0
            return
        self._vwap = self._sum_pv / self._sum_v
        variance = (self._sum_pv2 / self._sum_v) - (self._vwap ** 2)
        self._vwap_stdev = math.sqrt(variance) if variance > 0 else 0.0

    # -------------------------------------------------------------------------
    # Procesamiento principal
    # -------------------------------------------------------------------------
    def process_tick(self, tick: Tick) -> FeatureVector:
        candle_open_time = (tick.timestamp_ms // self.candle_period_ms) * self.candle_period_ms

        tick_delta = -tick.quantity if tick.is_buyer_maker else tick.quantity
        self.cvd += tick_delta

        if self.current_candle is None:
            self.current_candle = Candle(
                timestamp_ms=candle_open_time,
                open=tick.price, high=tick.price, low=tick.price, close=tick.price,
                volume=tick.quantity,
                buy_volume=0.0 if tick.is_buyer_maker else tick.quantity,
                sell_volume=tick.quantity if tick.is_buyer_maker else 0.0,
                trades_count=1
            )
            self._add_candle_to_vwap_accumulators(self.current_candle)

        elif candle_open_time > self.current_candle.timestamp_ms:
            # Cerrar vela anterior
            self.current_candle.closed = True
            self.candles.append(self.current_candle)
            self._update_atr_on_candle_close(self.current_candle)
            self._rebuild_vwap_accumulators()
            self.candles_closed_count += 1

            self.current_candle = Candle(
                timestamp_ms=candle_open_time,
                open=tick.price, high=tick.price, low=tick.price, close=tick.price,
                volume=tick.quantity,
                buy_volume=0.0 if tick.is_buyer_maker else tick.quantity,
                sell_volume=tick.quantity if tick.is_buyer_maker else 0.0,
                trades_count=1
            )
        else:
            c = self.current_candle
            c.close = tick.price
            if tick.price > c.high: c.high = tick.price
            if tick.price < c.low: c.low = tick.price
            c.volume += tick.quantity
            c.trades_count += 1
            if tick.is_buyer_maker:
                c.sell_volume += tick.quantity
            else:
                c.buy_volume += tick.quantity

        price = tick.price
        self.ema9 = self._update_ema(self.ema9, price, 9)
        self.ema21 = self._update_ema(self.ema21, price, 21)
        self._recompute_vwap()

        rsi = self._calculate_rsi(price)

        atr_raw = self.atr14 if self.atr14 is not None else self._default_atr()
        atr = max(atr_raw, self._get_min_atr())

        candle_delta = self.current_candle.buy_volume - self.current_candle.sell_volume
        ready = self.is_ready()

        feat = FeatureVector(
            timestamp_ms=tick.timestamp_ms,
            price=price,
            ema9=self.ema9 or price,
            ema21=self.ema21 or price,
            vwap=self._vwap,
            vwap_upper_1=self._vwap + self._vwap_stdev,
            vwap_lower_1=self._vwap - self._vwap_stdev,
            vwap_upper_2=self._vwap + (2.0 * self._vwap_stdev),
            vwap_lower_2=self._vwap - (2.0 * self._vwap_stdev),
            rsi14=rsi,
            atr14=atr,
            cvd=self.cvd,
            candle_delta=candle_delta,
            is_ready=ready,
            candles_closed=self.candles_closed_count,
        )
        self.last_feature_vector = feat
        return feat

    def _update_atr_on_candle_close(self, closed_candle: Candle):
        if len(self.candles) < 2:
            return
        prev = self.candles[-2]
        h = closed_candle.high
        l = closed_candle.low
        prev_c = prev.close
        tr = max(h - l, abs(h - prev_c), abs(l - prev_c))

        if tr <= 0:
            return

        if self.atr14 is None:
            self.atr14 = tr
        else:
            self.atr14 = ((self.atr14 * (self.rsi_period - 1)) + tr) / self.rsi_period

    def _default_atr(self) -> float:
        s = self.symbol.upper()
        if "XAU" in s or "GOLD" in s:
            return 2.50
        if "XAG" in s or "SILVER" in s:
            return 0.05
        if "BTC" in s:
            return 500.0     # 🆕 antes 150, más realista
        if "ETH" in s:
            return 15.0      # 🆕 antes 10
        if "SOL" in s:
            return 0.30      # 🆕 antes 0.50
        if "WTI" in s or "XTI" in s:
            return 0.30
        if "BRENT" in s or "XBR" in s:
            return 0.30
        if "US500" in s or "SP500" in s:
            return 5.0
        if any(fx in s for fx in ["EUR", "GBP"]):
            return 0.0015
        return 1.50

    def _update_ema(self, prev_ema: Optional[float], price: float, period: int) -> float:
        k = 2.0 / (period + 1)
        return price if prev_ema is None else (price * k) + (prev_ema * (1.0 - k))

    def _calculate_rsi(self, current_price: float) -> float:
        if self.prev_close is None:
            self.prev_close = current_price
            return 50.0

        diff = current_price - self.prev_close
        self.prev_close = current_price
        gain = max(0.0, diff)
        loss = max(0.0, -diff)

        if self.avg_gain is None:
            self.avg_gain = gain
            self.avg_loss = loss
            return 50.0

        self.avg_gain = (self.avg_gain * 13 + gain) / 14
        self.avg_loss = (self.avg_loss * 13 + loss) / 14

        if self.avg_gain == 0.0 and self.avg_loss == 0.0:
            return 50.0
        if self.avg_loss == 0.0:
            return 100.0
        rs = self.avg_gain / self.avg_loss
        return 100.0 - (100.0 / (1.0 + rs))