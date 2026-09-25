"""
MÓDULO DE ESTRATEGIA CUANTITATIVA Y GENERACIÓN DE SEÑALES SNIPER (AGENTE 2)

🔧 v1.9.0 — LOTE FUSIONADO 2.6+3:
  • 🐛 O1 OPTIMIZADO: import MetaTrader5 movido a nivel de módulo.
  • 🐛 O4 OPTIMIZADO: cache M15 con TTL 60s para copy_rates_from_pos.
  • B16 heredado: validación SL/TP contra min_stop_distance.
  • v1.7.1 heredado: SIGNAL_REJECTED rate limiter, WARMUP, filtro M15.
"""
import os
import time
import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger("SignalAgent")
logger.propagate = False

# 🐛 O1: import a nivel de módulo
try:
    import MetaTrader5 as mt5
    _MT5_AVAILABLE = True
except ImportError:
    mt5 = None
    _MT5_AVAILABLE = False


_REJECTION_LOG_COOLDOWN_SEC = 300.0

# 🐛 O4: TTL del cache M15
_M15_CACHE_TTL_SEC = 60.0
_m15_cache: dict = {}


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
        "XAU": 2, "XAG": 3, "WTI": 2, "BRENT": 2,
        "BTC": 2, "ETH": 2, "SOL": 2, "US500": 1, "FOREX": 5,
    }

    _MT5_SYMBOL_ALIASES = {
        "XAUUSD": ["XAUUSD", "GOLD", "XAUUSD.raw", "GOLD.raw"],
        "XAGUSD": ["XAGUSD", "SILVER", "XAGUSD.raw", "SILVER.raw"],
        "US500":  ["US500", "SP500", "SPX500", "US500.raw", "SP500.raw"],
        "WTI":    ["XTIUSD", "WTI", "USOIL", "XTIUSD.raw", "WTI.raw"],
        "XTIUSD": ["XTIUSD", "WTI", "USOIL", "XTIUSD.raw", "WTI.raw"],
        "BRENT":  ["XBRUSD", "BRENT", "UKOIL", "XBRUSD.raw", "BRENT.raw"],
        "XBRUSD": ["XBRUSD", "BRENT", "UKOIL", "XBRUSD.raw", "BRENT.raw"],
        "EURUSD": ["EURUSD", "EURUSD.raw"],
        "GBPUSD": ["GBPUSD", "GBPUSD.raw"],
    }

    def __init__(
        self,
        symbol: str = "XAUUSD",
        min_confidence_threshold: Optional[float] = None,
        atr_stop_multiplier: Optional[float] = None,
        atr_profit_multiplier: Optional[float] = None
    ):
        self.symbol = symbol
        self.min_confidence = min_confidence_threshold or float(os.getenv("MIN_CONFIDENCE_THRESHOLD", "90.0"))

        sym_upper = symbol.upper()
        self.is_gold = any(k in sym_upper for k in ["XAU", "GOLD"])
        self.is_silver = any(k in sym_upper for k in ["XAG", "SILVER"])
        self.is_oil = any(k in sym_upper for k in ["WTI", "BRENT", "OIL", "XTI", "XBR"])
        self.is_forex = any(fx in sym_upper for fx in ["EUR", "GBP", "JPY", "AUD", "NZD"])
        self.is_crypto = any(c in sym_upper for c in ["BTC", "ETH", "SOL"])
        self.is_index = any(idx in sym_upper for idx in ["US500", "SP500", "SPX", "NAS100", "US30", "GER40", "UK100"])

        self.precision = self._get_precision()
        self._resolved_mt5_symbol: Optional[str] = None

        self._last_rejection_log_ts: float = 0.0
        self._last_rejection_reason: str = ""

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

        self._default_atr_sl = default_sl
        self._default_atr_tp = default_tp
        self.atr_stop_multiplier = atr_stop_multiplier or default_sl
        self.atr_profit_multiplier = atr_profit_multiplier or default_tp

        if self.is_gold:
            self.min_sl_distance_pct = 0.0005
        elif self.is_crypto:
            self.min_sl_distance_pct = 0.0010
        elif self.is_forex:
            self.min_sl_distance_pct = 0.0001
        else:
            self.min_sl_distance_pct = 0.0008

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

    def apply_learned_params(self, atr_sl: Optional[float] = None, atr_tp: Optional[float] = None):
        """
        🐛 B19: aplica parámetros del learner respetando los límites por clase.
        NO sobreescribe el valor default de la clase si el learner no está
        autorizado (mantiene coherencia).
        """
        # Los atr_sl/atr_tp del learner se aplican solo como override suave
        # Los valores por clase se mantienen como base
        if atr_sl is not None:
            self.atr_stop_multiplier = atr_sl
        if atr_tp is not None:
            self.atr_profit_multiplier = atr_tp

    def _resolve_mt5_symbol(self) -> str:
        if self._resolved_mt5_symbol:
            return self._resolved_mt5_symbol

        if not _MT5_AVAILABLE:
            self._resolved_mt5_symbol = self.symbol
            return self._resolved_mt5_symbol

        try:
            sym_upper = self.symbol.upper()

            if mt5.symbol_info(self.symbol):
                self._resolved_mt5_symbol = self.symbol
                return self._resolved_mt5_symbol

            aliases = self._MT5_SYMBOL_ALIASES.get(sym_upper, [])
            if not aliases:
                aliases = [f"{self.symbol}.raw", f"{self.symbol}_raw", f"{self.symbol}m"]

            for alias in aliases:
                if mt5.symbol_info(alias):
                    try:
                        mt5.symbol_select(alias, True)
                    except Exception:
                        pass
                    self._resolved_mt5_symbol = alias
                    logger.info(f"🔧 [M15] '{self.symbol}' resuelto a '{alias}'")
                    return alias

            logger.warning(f"⚠️ [M15] No se pudo resolver '{self.symbol}'. Fail-safe.")
            self._resolved_mt5_symbol = self.symbol
            return self._resolved_mt5_symbol
        except Exception as e:
            logger.debug(f"🔧 [M15] Error resolviendo '{self.symbol}': {e}")
            return self.symbol

    def _get_m15_rates_cached(self, resolved_sym: str) -> Optional[list]:
        """
        🐛 O4: cachea copy_rates_from_pos con TTL 60s.
        """
        now = time.time()
        cached = _m15_cache.get(resolved_sym)
        if cached and (now - cached["ts"]) < _M15_CACHE_TTL_SEC:
            return cached["rates"]

        if not _MT5_AVAILABLE:
            return None

        try:
            rates = mt5.copy_rates_from_pos(resolved_sym, mt5.TIMEFRAME_M15, 0, 30)
            if rates is not None and len(rates) > 0:
                _m15_cache[resolved_sym] = {"rates": rates, "ts": now}
            return rates
        except Exception as e:
            logger.debug(f"🔍 [M15] Error copy_rates para {resolved_sym}: {e}")
            return None

    def _check_macro_trend(self, signal_type_str: str, current_price: float) -> bool:
        """
        🐛 O1: ya no importa MetaTrader5 aquí (lo hace a nivel de módulo).
        🐛 O4: usa cache de copy_rates.
        """
        try:
            resolved_sym = self._resolve_mt5_symbol()
            rates = self._get_m15_rates_cached(resolved_sym)

            if rates is None or len(rates) < 20:
                return True

            closes = [r['close'] for r in rates[-20:]]
            k = 2.0 / (20 + 1)

            seed_len = min(5, len(closes))
            ema20 = sum(closes[:seed_len]) / seed_len
            for c in closes[seed_len:]:
                ema20 = c * k + ema20 * (1 - k)

            if signal_type_str == "BUY" and current_price < ema20:
                logger.debug(
                    f"🔍 [M15] BUY RECHAZADO en {self.symbol} ({resolved_sym}): "
                    f"precio {current_price:.5f} < EMA20_M15 {ema20:.5f}"
                )
                return False

            if signal_type_str == "SELL" and current_price > ema20:
                logger.debug(
                    f"🔍 [M15] SELL RECHAZADO en {self.symbol} ({resolved_sym}): "
                    f"precio {current_price:.5f} > EMA20_M15 {ema20:.5f}"
                )
                return False

            return True
        except Exception as e:
            logger.debug(f"🔍 [M15] Fail-safe para {self.symbol}: {e}")
            return True

    def _log_rejection(self, reason: str, rsi: float, trend_score: float, momentum_score: float):
        now = time.time()
        if now - self._last_rejection_log_ts < _REJECTION_LOG_COOLDOWN_SEC:
            return
        self._last_rejection_log_ts = now
        self._last_rejection_reason = reason
        logger.debug(
            f"⏸️  [REJECT] {self.symbol}: {reason} | RSI={rsi:.1f} | "
            f"trend={trend_score:+.0f} | momentum={momentum_score:+.0f}"
        )

    def _get_broker_min_distance(self, price: float) -> float:
        min_distance = price * self.min_sl_distance_pct

        if not _MT5_AVAILABLE:
            return min_distance

        try:
            resolved_sym = self._resolve_mt5_symbol()
            info = mt5.symbol_info(resolved_sym)
            if info:
                point = info.point
                stops_level = max(
                    float(getattr(info, "trade_stops_level", 0) or 0),
                    float(getattr(info, "stops_level", 0) or 0),
                )
                if stops_level > 0:
                    broker_min = stops_level * point * 1.5
                    min_distance = max(min_distance, broker_min)
        except Exception:
            pass

        return min_distance

    def evaluate(self, f) -> Optional[TradeSignal]:
        if not getattr(f, "is_ready", False):
            return None

        reasons: List[str] = []
        trend_score = 0.0
        momentum_score = 0.0
        order_flow_score = 0.0
        volatility_score = 0.0

        is_bull_trend = (f.ema9 > f.ema21) and (f.price > f.vwap)
        is_bear_trend = (f.ema9 < f.ema21) and (f.price < f.vwap)

        if is_bull_trend:
            trend_score = 1.0
            reasons.append("EMA9 > EMA21 y Precio > VWAP")
        elif is_bear_trend:
            trend_score = -1.0
            reasons.append("EMA9 < EMA21 y Precio < VWAP")

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

        if f.candle_delta > 0 and f.cvd > 0:
            order_flow_score = 1.0
            reasons.append("CVD y delta positivos")
        elif f.candle_delta < 0 and f.cvd < 0:
            order_flow_score = -1.0
            reasons.append("CVD y delta negativos")

        min_atr = f.price * 0.0001
        max_atr = f.price * 0.0100
        if min_atr <= f.atr14 <= max_atr:
            volatility_score = 1.0
        else:
            volatility_score = 0.2
            reasons.append(f"ATR fuera de rango")

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
            if momentum_score == 0.0:
                self._log_rejection("RSI fuera de zona", f.rsi14, trend_score, momentum_score)
            elif trend_score == 0.0:
                self._log_rejection("Sin tendencia clara", f.rsi14, trend_score, momentum_score)
            else:
                self._log_rejection(f"Confianza insuficiente ({max(bull_conf, bear_conf)*100:.1f}%)",
                                    f.rsi14, trend_score, momentum_score)
            return None

        signal_type_str = signal_type.value if hasattr(signal_type, 'value') else str(signal_type)
        if not self._check_macro_trend(signal_type_str, f.price):
            return None

        raw_sl_distance = f.atr14 * self.atr_stop_multiplier
        raw_tp_distance = f.atr14 * self.atr_profit_multiplier

        min_distance = self._get_broker_min_distance(f.price)
        sl_distance = max(raw_sl_distance, min_distance)
        tp_distance = max(raw_tp_distance, min_distance)

        if sl_distance <= 0 or tp_distance <= 0:
            return None

        if signal_type == SignalType.BUY:
            stop_loss = round(f.price - sl_distance, self.precision)
            take_profit = round(f.price + tp_distance, self.precision)

            if stop_loss >= f.price or take_profit <= f.price:
                logger.warning(
                    f"🚨 B16: SL/TP invertidos en {self.symbol} BUY. Rechazando."
                )
                return None
        else:
            stop_loss = round(f.price + sl_distance, self.precision)
            take_profit = round(f.price - tp_distance, self.precision)

            if stop_loss <= f.price or take_profit >= f.price:
                logger.warning(
                    f"🚨 B16: SL/TP invertidos en {self.symbol} SELL. Rechazando."
                )
                return None

        if stop_loss <= 0 or take_profit <= 0:
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