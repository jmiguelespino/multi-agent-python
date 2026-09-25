"""
MÓDULO DE ESTRATEGIA CUANTITATIVA Y GENERACIÓN DE SEÑALES SNIPER (AGENTE 2)

🔧 v1.4:
  • Añadido soporte para XAGUSD (Plata) y US500 (S&P 500).
  • Precisión decimal correcta por clase de activo.
  • Confianza normalizada.
  • Validación de stops coherentes.
🔧 v1.5:
  • FIX #2: Filtro de tendencia macro M15 (EMA20) para evitar comprar en
    tendencia bajista o vender en tendencia alcista.
"""
import os
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from dotenv import load_dotenv

load_dotenv()


class SignalType(str, Enum):
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"


@dataclass(slots=True)
class ConfluenceScore:
    trend_score: float
    momentum_score: float
    order_flow_score: float
    volatility_score: float
    overall_confidence: float
    reasons: List[str] = field(default_factory=list)


@dataclass(slots=True)
class TradeSignal:
    id: str
    timestamp_ms: int
    symbol: str
    signal_type: SignalType
    price: float
    confidence_percent: float
    suggested_stop_loss: float
    suggested_take_profit: float
    confluence: ConfluenceScore


class StrategySignalAgent:
    W_TREND = 0.35
    W_MOMENTUM = 0.30
    W_ORDER_FLOW = 0.20
    W_VOLATILITY = 0.15

    PRECISION_BY_CLASS = {
        "XAU": 2,
        "XAG": 3,
        "WTI": 2,
        "BRENT": 2,
        "BTC": 2,
        "ETH": 2,
        "SOL": 2,
        "US500": 1,
        "FOREX": 5,
    }

    def __init__(
        self,
        symbol: str = "XAUUSD",
        min_confidence_threshold: Optional[float] = None,
        atr_stop_multiplier: Optional[float] = None,
        atr_profit_multiplier: Optional[float] = None
    ):
        self.symbol = symbol
        self.min_confidence = min_confidence_threshold or float(os.getenv("MIN_CONFIDENCE_THRESHOLD", "86.0"))

        sym_upper = symbol.upper()
        self.is_gold = any(k in sym_upper for k in ["XAU", "GOLD"])
        self.is_silver = any(k in sym_upper for k in ["XAG", "SILVER"])
        self.is_oil = any(k in sym_upper for k in ["WTI", "BRENT", "OIL", "XTI", "XBR"])
        self.is_forex = any(fx in sym_upper for fx in ["EUR", "GBP", "JPY", "AUD", "NZD"])
        self.is_crypto = any(c in sym_upper for c in ["BTC", "ETH", "SOL"])
        self.is_index = any(idx in sym_upper for idx in ["US500", "SP500", "SPX", "NAS100", "US30", "GER40", "UK100"])

        self.precision = self._get_precision()

        if self.is_gold:
            default_sl = float(os.getenv("GOLD_ATR_STOP_MULTIPLIER", "4.5"))
            default_tp = float(os.getenv("GOLD_ATR_PROFIT_MULTIPLIER", "7.0"))
        elif self.is_silver:
            default_sl = float(os.getenv("XAG_ATR_STOP_MULTIPLIER", "2.5"))
            default_tp = float(os.getenv("XAG_ATR_PROFIT_MULTIPLIER", "4.0"))
        elif self.is_oil:
            default_sl = float(os.getenv("OIL_ATR_STOP_MULTIPLIER", "1.8"))
            default_tp = float(os.getenv("OIL_ATR_PROFIT_MULTIPLIER", "3.0"))
        elif self.is_index:
            default_sl = float(os.getenv("US500_ATR_STOP_MULTIPLIER", "2.0"))
            default_tp = float(os.getenv("US500_ATR_PROFIT_MULTIPLIER", "3.5"))
        elif self.is_forex:
            default_sl = float(os.getenv("FOREX_ATR_STOP_MULTIPLIER", "1.2"))
            default_tp = float(os.getenv("FOREX_ATR_PROFIT_MULTIPLIER", "2.0"))
        elif self.is_crypto:
            default_sl = float(os.getenv("CRYPTO_ATR_STOP_MULTIPLIER", "2.2"))
            default_tp = float(os.getenv("CRYPTO_ATR_PROFIT_MULTIPLIER", "3.8"))
        else:
            default_sl = float(os.getenv("ATR_STOP_MULTIPLIER", "1.8"))
            default_tp = float(os.getenv("ATR_PROFIT_MULTIPLIER", "3.0"))

        self.atr_stop_multiplier = atr_stop_multiplier or default_sl
        self.atr_profit_multiplier = atr_profit_multiplier or default_tp

    def _get_precision(self) -> int:
        s = self.symbol.upper()
        if any(fx in s for fx in ["EUR", "GBP", "JPY", "AUD", "NZD", "CHF", "CAD"]):
            return self.PRECISION_BY_CLASS["FOREX"]
        if "XAU" in s or "GOLD" in s:
            return self.PRECISION_BY_CLASS["XAU"]
        if "XAG" in s or "SILVER" in s:
            return self.PRECISION_BY_CLASS["XAG"]
        if "US500" in s or "SP500" in s or "SPX" in s:
            return self.PRECISION_BY_CLASS["US500"]
        if "XTI" in s or "WTI" in s or "OIL" in s:
            return self.PRECISION_BY_CLASS["WTI"]
        if "XBR" in s or "BRENT" in s:
            return self.PRECISION_BY_CLASS["BRENT"]
        if "BTC" in s:
            return self.PRECISION_BY_CLASS["BTC"]
        if "ETH" in s:
            return self.PRECISION_BY_CLASS["ETH"]
        if "SOL" in s:
            return self.PRECISION_BY_CLASS["SOL"]
        return 2

    def _check_macro_trend(self, signal_type_str: str, current_price: float) -> bool:
        """
        🔧 FIX #2: Verifica que la tendencia de 15min esté alineada con la señal.
        Retorna True si está alineada, False si no.
        """
        try:
            import MetaTrader5 as mt5
            rates = mt5.copy_rates_from_pos(self.symbol, mt5.TIMEFRAME_M15, 0, 30)
            if rates is None or len(rates) < 20:
                return True  # No hay datos suficientes, permitir

            # Calcular EMA 20 en M15
            closes = [r['close'] for r in rates[-20:]]
            k = 2.0 / (20 + 1)
            ema20 = closes[0]
            for c in closes[1:]:
                ema20 = c * k + ema20 * (1 - k)

            # BUY solo si precio > EMA20_M15
            if signal_type_str == "BUY" and current_price < ema20:
                return False

            # SELL solo si precio < EMA20_M15
            if signal_type_str == "SELL" and current_price > ema20:
                return False

            return True
        except Exception:
            return True  # En caso de error, no bloquear

    def evaluate(self, f) -> Optional[TradeSignal]:
        reasons: List[str] = []
        trend_score = 0.0
        momentum_score = 0.0
        order_flow_score = 0.0
        volatility_score = 0.0

        # 1. Tendencia
        is_bull_trend = (f.ema9 > f.ema21) and (f.price > f.vwap)
        is_bear_trend = (f.ema9 < f.ema21) and (f.price < f.vwap)

        if is_bull_trend:
            trend_score = 1.0
            reasons.append("EMA9 > EMA21 y Precio > VWAP")
        elif is_bear_trend:
            trend_score = -1.0
            reasons.append("EMA9 < EMA21 y Precio < VWAP")

        # 2. Momentum (RSI)
        if self.is_oil:
            rsi_buy_min = float(os.getenv("RSI_BUY_MIN_OIL", "45.0"))
            rsi_buy_max = float(os.getenv("RSI_BUY_MAX_OIL", "72.0"))
            rsi_sell_min = float(os.getenv("RSI_SELL_MIN_OIL", "28.0"))
            rsi_sell_max = float(os.getenv("RSI_SELL_MAX_OIL", "55.0"))
        else:
            rsi_buy_min = float(os.getenv("RSI_BUY_MIN_GENERAL", "50.0"))
            rsi_buy_max = float(os.getenv("RSI_BUY_MAX_GENERAL", "66.0"))
            rsi_sell_min = float(os.getenv("RSI_SELL_MIN_GENERAL", "34.0"))
            rsi_sell_max = float(os.getenv("RSI_SELL_MAX_GENERAL", "50.0"))

        if rsi_buy_min <= f.rsi14 <= rsi_buy_max:
            momentum_score = 1.0
            reasons.append(f"RSI en expansión ({f.rsi14:.1f})")
        elif rsi_sell_min <= f.rsi14 <= rsi_sell_max:
            momentum_score = -1.0
            reasons.append(f"RSI en compresión ({f.rsi14:.1f})")

        # 3. Order Flow
        if f.candle_delta > 0 and f.cvd > 0:
            order_flow_score = 1.0
            reasons.append("CVD y delta positivos")
        elif f.candle_delta < 0 and f.cvd < 0:
            order_flow_score = -1.0
            reasons.append("CVD y delta negativos")

        # 4. Volatilidad
        min_atr = f.price * 0.0001
        max_atr = f.price * 0.0100
        if min_atr <= f.atr14 <= max_atr:
            volatility_score = 1.0
        else:
            volatility_score = 0.2
            reasons.append(f"ATR fuera de rango")

        # Confluencia normalizada
        raw_bull = (
            (self.W_TREND if trend_score > 0 else 0.0) +
            (self.W_MOMENTUM if momentum_score > 0 else 0.0) +
            (self.W_ORDER_FLOW if order_flow_score > 0 else 0.0) +
            (self.W_VOLATILITY * volatility_score)
        )
        raw_bear = (
            (self.W_TREND if trend_score < 0 else 0.0) +
            (self.W_MOMENTUM if momentum_score < 0 else 0.0) +
            (self.W_ORDER_FLOW if order_flow_score < 0 else 0.0) +
            (self.W_VOLATILITY * volatility_score)
        )

        max_possible = self.W_TREND + self.W_MOMENTUM + self.W_ORDER_FLOW + self.W_VOLATILITY
        bull_conf = raw_bull / max_possible
        bear_conf = raw_bear / max_possible

        signal_type = SignalType.HOLD
        confidence = 0.0

        if bull_conf * 100 >= self.min_confidence and trend_score > 0 and momentum_score > 0:
            signal_type = SignalType.BUY
            confidence = round(bull_conf * 100, 1)
        elif bear_conf * 100 >= self.min_confidence and trend_score < 0 and momentum_score < 0:
            signal_type = SignalType.SELL
            confidence = round(bear_conf * 100, 1)
        else:
            return None

        # 🔧 FIX #2: Verificar tendencia macro M15 antes de aceptar la señal
        signal_type_str = signal_type.value if hasattr(signal_type, 'value') else str(signal_type)
        if not self._check_macro_trend(signal_type_str, f.price):
            return None  # Rechazar señal contraria a tendencia macro

        sl_distance = f.atr14 * self.atr_stop_multiplier
        tp_distance = f.atr14 * self.atr_profit_multiplier

        min_distance_pct = 0.00005 if self.is_forex else 0.0005
        min_distance = f.price * min_distance_pct

        if sl_distance < min_distance or tp_distance < min_distance:
            return None

        if signal_type == SignalType.BUY:
            stop_loss = round(f.price - sl_distance, self.precision)
            take_profit = round(f.price + tp_distance, self.precision)
        else:
            stop_loss = round(f.price + sl_distance, self.precision)
            take_profit = round(f.price - tp_distance, self.precision)

        if stop_loss == round(f.price, self.precision) or take_profit == round(f.price, self.precision):
            return None

        if signal_type == SignalType.BUY:
            if stop_loss >= f.price or take_profit <= f.price:
                return None
        else:
            if stop_loss <= f.price or take_profit >= f.price:
                return None

        confluence_obj = ConfluenceScore(
            trend_score=trend_score,
            momentum_score=momentum_score,
            order_flow_score=order_flow_score,
            volatility_score=volatility_score,
            overall_confidence=confidence,
            reasons=reasons
        )

        return TradeSignal(
            id=f"SIG-SNIPER-{int(time.time()*1000)}",
            timestamp_ms=int(time.time()*1000),
            symbol=self.symbol,
            signal_type=signal_type,
            price=f.price,
            confidence_percent=confidence,
            suggested_stop_loss=stop_loss,
            suggested_take_profit=take_profit,
            confluence=confluence_obj
        )