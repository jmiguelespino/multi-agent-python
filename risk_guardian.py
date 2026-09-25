"""
=============================================================================
QUANTEDGE AI — MÓDULO DE GESTIÓN DE RIESGO INSTITUCIONAL Y CIRCUIT BREAKERS
=============================================================================
🔧 v1.7:
  • FIX: WTI y BRENT unificados como "OIL" (evita doble exposición a petróleo).
  • Añadido soporte para XAGUSD (Plata) y US500 (S&P 500).
  • CRYPTO_MAX_RISK_PCT ahora se aplica correctamente antes del sizing.
  • Acepta volume_min del broker si el riesgo resultante es <= 3x el límite.
  • Bloqueo PERMANENTE solo si el volume_min implica riesgo excesivo.
  • Rate limiter para logs de spread (60s por símbolo).
  • Lock con TTL.
=============================================================================
"""
import os
import time
import logging
from dataclasses import dataclass
from typing import Optional, Set, Dict
from datetime import datetime, timezone
import MetaTrader5 as mt5
from dotenv import load_dotenv
from audit_logger import log_rejection

load_dotenv()
logger = logging.getLogger("RiskGuardian")
logger.propagate = False


@dataclass(slots=True)
class RiskVerdict:
    authorized: bool
    rejection_reason: Optional[str]
    authorized_size_units: float
    risk_amount_usd: float
    stop_distance_usd: float
    circuit_breaker_tripped: bool


def is_us_market_hours() -> bool:
    now_utc = datetime.now(timezone.utc)
    if now_utc.weekday() >= 5:
        return False
    return 13 <= now_utc.hour < 21


def get_canonical_asset(symbol: str) -> str:
    """
    🔧 v1.7: WTI y BRENT devuelven "OIL" para unificar exposición.
    """
    if not symbol:
        return ""
    s = symbol.upper().replace(".RAW", "").replace("_RAW", "").strip()
    if "BTC" in s or "BITCOIN" in s:
        return "BTC"
    if "ETH" in s or "ETHEREUM" in s:
        return "ETH"
    if "SOL" in s or "SOLANA" in s:
        return "SOL"
    if "XAU" in s or "GOLD" in s or "ORO" in s:
        return "XAU"
    if "XAG" in s or "SILVER" in s or "PLATA" in s:
        return "XAG"
    # 🔧 FIX: WTI y BRENT → "OIL" (mismo activo subyacente)
    if "WTI" in s or "XTI" in s or "USO" in s or "CRUDE" in s or "OIL" in s or "PETROLEO" in s:
        return "OIL"
    if "BRENT" in s or "XBR" in s or "UKO" in s:
        return "OIL"
    if "US500" in s or "SP500" in s or "SPX" in s:
        return "US500"
    if "EUR" in s:
        return "EURUSD"
    if "GBP" in s:
        return "GBPUSD"
    return s


class InstitutionalRiskGuardian:
    PENDING_LOCK_TTL_SECONDS = 30.0
    SPREAD_LOG_COOLDOWN_SEC = 60.0
    BROKER_MIN_TOLERANCE_MULT = 3.0

    def __init__(
        self,
        initial_capital: Optional[float] = None,
        max_risk_per_trade_pct: Optional[float] = None,
        daily_drawdown_limit_pct: Optional[float] = None,
        max_concurrent_positions: Optional[int] = None,
        max_daily_trades: Optional[int] = None,
        cooldown_seconds: Optional[int] = None,
        max_allowed_spread_bps: Optional[float] = None
    ):
        self.initial_capital = initial_capital or float(os.getenv("CAPITAL_BASE_USD", "1500.0"))
        self.current_equity = self.initial_capital
        self.daily_peak_equity = self.initial_capital
        self.max_risk_per_trade_pct = max_risk_per_trade_pct or float(os.getenv("MAX_RISK_PER_TRADE_PCT", "1.0"))
        self.daily_drawdown_limit_pct = daily_drawdown_limit_pct or float(os.getenv("DAILY_DRAWDOWN_LIMIT_PCT", "3.0"))
        self.max_concurrent_positions = max_concurrent_positions or int(os.getenv("MAX_CONCURRENT_POSITIONS", "5"))
        self.max_daily_trades = max_daily_trades or int(os.getenv("MAX_DAILY_TRADES", "25"))
        self.cooldown_seconds = cooldown_seconds or int(os.getenv("COOLDOWN_SECONDS", "60"))
        self.max_allowed_spread_bps = max_allowed_spread_bps or float(os.getenv("MAX_ALLOWED_SPREAD_BPS", "15.0"))

        self.trades_executed_today: int = 0
        self.last_trade_timestamp: float = 0.0
        self.circuit_breaker_active: bool = False
        self.active_positions_count: int = 0
        self.active_symbols: Set[str] = set()
        self.last_stop_loss_by_symbol: Dict[str, float] = {}
        self._pending_orders_lock: Dict[str, float] = {}
        self._last_spread_log: Dict[str, float] = {}
        self._blocked_assets: Dict[str, str] = {}
        self._forced_min_volume: Dict[str, float] = {}

    def _prune_expired_locks(self):
        now = time.time()
        expired = [k for k, ts in self._pending_orders_lock.items() if now - ts > self.PENDING_LOCK_TTL_SECONDS]
        for k in expired:
            logger.warning(f"🔓 Lock expirado liberado automáticamente: {k}")
            self._pending_orders_lock.pop(k, None)

    def sync_capital_from_mt5(self, mt5_balance: float, mt5_equity: float):
        if mt5_balance > 0:
            self.initial_capital = mt5_balance
        if mt5_equity > 0:
            self.current_equity = mt5_equity
            if mt5_equity > self.daily_peak_equity:
                self.daily_peak_equity = mt5_equity

    def sync_active_positions(self, symbols: list[str]):
        self.active_symbols = set(symbols)
        self.active_positions_count = len(symbols)

    def evaluate_order_risk(self, signal, current_market_spread_bps: float) -> RiskVerdict:
        self._prune_expired_locks()

        now = time.time()
        symbol = getattr(signal, 'symbol', 'UNKNOWN')
        side = getattr(signal, 'signal_type', 'UNKNOWN')
        price = getattr(signal, 'price', 0.0)
        canonical_sym = get_canonical_asset(symbol)

        # 0. Anti-Duplicación en tránsito
        if canonical_sym in self._pending_orders_lock:
            msg = f"ORDEN BLOQUEADA: Solicitud en tránsito activa para {symbol} ({canonical_sym})."
            logger.debug(msg)
            return RiskVerdict(False, msg, 0.0, 0.0, 0.0, False)

        # 0.1 Activo bloqueado permanentemente
        if canonical_sym in self._blocked_assets:
            return RiskVerdict(False, self._blocked_assets[canonical_sym], 0.0, 0.0, 0.0, False)

        # 1. Circuit Breaker Diario
        current_drawdown_usd = self.daily_peak_equity - self.current_equity
        drawdown_pct = (current_drawdown_usd / self.daily_peak_equity) * 100.0 if self.daily_peak_equity > 0 else 0.0

        if drawdown_pct >= self.daily_drawdown_limit_pct or self.circuit_breaker_active:
            self.circuit_breaker_active = True
            msg = f"CIRCUIT BREAKER TRIPPED! Drawdown ({drawdown_pct:.2f}%) >= límite ({self.daily_drawdown_limit_pct}%)."
            logger.critical(msg)
            log_rejection(
                symbol=symbol,
                reason=msg,
                event_type="CIRCUIT_BREAKER_TRIGGERED",
                details=f"Pico: ${self.daily_peak_equity:.2f} | Equity: ${self.current_equity:.2f} | Drawdown: {drawdown_pct:.2f}%",
                side=side,
                price=price
            )
            return RiskVerdict(False, msg, 0.0, 0.0, 0.0, True)

        # 2. Cuota Diaria
        if self.trades_executed_today >= self.max_daily_trades:
            msg = f"CUOTA DIARIA CUMPLIDA ({self.trades_executed_today}/{self.max_daily_trades} trades)."
            logger.debug(msg)
            log_rejection(
                symbol=symbol,
                reason=msg,
                event_type="QUOTA_REACHED",
                details=f"Trades ejecutados hoy: {self.trades_executed_today}/{self.max_daily_trades}",
                side=side,
                price=price
            )
            return RiskVerdict(False, msg, 0.0, 0.0, 0.0, False)

        # 3. Cooldown global
        time_since_last = now - self.last_trade_timestamp
        if time_since_last < self.cooldown_seconds:
            remaining = int(self.cooldown_seconds - time_since_last)
            msg = f"COOLDOWN ACTIVO ({remaining}s restantes)."
            logger.debug(msg)
            log_rejection(
                symbol=symbol,
                reason=msg,
                event_type="COOLDOWN_BLOCKED",
                details=f"Tiempo restante de cooldown: {remaining}s",
                side=side,
                price=price
            )
            return RiskVerdict(False, msg, 0.0, 0.0, 0.0, False)

        # 3.1 Cuarentena tras Stop Loss
        sl_quarantine_sec = float(os.getenv("STOP_LOSS_CUARENTENA_SECONDS", "300"))
        last_loss = max(
            self.last_stop_loss_by_symbol.get(symbol, 0.0),
            self.last_stop_loss_by_symbol.get(canonical_sym, 0.0)
        )
        if now - last_loss < sl_quarantine_sec:
            remaining = int(sl_quarantine_sec - (now - last_loss))
            msg = f"RESGUARDO PATRIMONIAL: Pausa de {int(sl_quarantine_sec/60)} min activa en {symbol} ({canonical_sym}) tras Stop Loss."
            logger.debug(msg)
            log_rejection(
                symbol=symbol,
                reason=msg,
                event_type="COOLDOWN_BLOCKED",
                details=f"Pausa anti-reincidencia activa: {remaining}s restantes.",
                side=side,
                price=price
            )
            return RiskVerdict(False, msg, 0.0, 0.0, 0.0, False)

        # 4. Doble exposición por activo canónico (ahora WTI y BRENT son "OIL")
        has_same_asset = any(get_canonical_asset(s) == canonical_sym for s in self.active_symbols)
        if has_same_asset:
            msg = f"Ya existe una posición activa en {symbol} ({canonical_sym})."
            logger.debug(msg)
            log_rejection(
                symbol=symbol,
                reason=msg,
                event_type="MAX_POSITIONS_BLOCKED",
                details=f"Máx 1 posición por activo ({canonical_sym}).",
                side=side,
                price=price
            )
            return RiskVerdict(False, msg, 0.0, 0.0, 0.0, False)

        # 5. Límite del portafolio global
        if self.active_positions_count >= self.max_concurrent_positions:
            msg = f"Límite de posiciones simultáneas alcanzado ({self.active_positions_count}/{self.max_concurrent_positions})."
            logger.debug(msg)
            log_rejection(
                symbol=symbol,
                reason=msg,
                event_type="MAX_POSITIONS_BLOCKED",
                details=f"Portafolio al límite configurado ({self.max_concurrent_positions}).",
                side=side,
                price=price
            )
            return RiskVerdict(False, msg, 0.0, 0.0, 0.0, False)

        # 6. Filtro de Spread Adaptativo
        max_spread_limit = self.max_allowed_spread_bps
        crypto_offhours_max = float(os.getenv("CRYPTO_OFFHOURS_MAX_SPREAD_BPS", "20.0"))
        if canonical_sym in ["BTC", "ETH", "SOL"] and not is_us_market_hours():
            max_spread_limit = max(self.max_allowed_spread_bps, crypto_offhours_max)

        if current_market_spread_bps > max_spread_limit:
            msg = f"Spread elevado ({current_market_spread_bps:.1f} bps > {max_spread_limit:.1f} bps)."

            now_ts = time.time()
            last_log = self._last_spread_log.get(canonical_sym, 0.0)
            if now_ts - last_log > self.SPREAD_LOG_COOLDOWN_SEC:
                logger.warning(msg)
                self._last_spread_log[canonical_sym] = now_ts

            log_rejection(
                symbol=symbol,
                reason=msg,
                event_type="ORDER_REJECTED",
                details=f"Spread actual {current_market_spread_bps:.1f} bps supera el límite dinámico de {max_spread_limit:.1f} bps",
                side=side,
                price=price,
                metadata={"spread_bps": current_market_spread_bps, "max_allowed_bps": max_spread_limit}
            )
            return RiskVerdict(False, msg, 0.0, 0.0, 0.0, False)

        # 7. Sizing dinámico
        # 🔧 Calcular risk_pct específico por activo ANTES del sizing
        risk_pct = self.max_risk_per_trade_pct

        if canonical_sym == "XAU":
            risk_pct = float(os.getenv("GOLD_MAX_RISK_PCT", "0.3"))
        elif canonical_sym in ["BTC", "ETH", "SOL"]:
            risk_pct = float(os.getenv("CRYPTO_MAX_RISK_PCT", "1.0"))

        risk_usd = self.current_equity * (risk_pct / 100.0)
        stop_distance = abs(signal.price - signal.suggested_stop_loss)

        if stop_distance <= 0:
            err_msg = "Distancia de stop loss inválida"
            log_rejection(symbol=symbol, reason=err_msg, side=side, price=price)
            return RiskVerdict(False, err_msg, 0.0, 0.0, 0.0, False)

        point_multiplier = 1.0
        sym_upper = symbol.upper()

        s_info = mt5.symbol_info(symbol) if hasattr(mt5, 'symbol_info') else None
        if s_info and hasattr(s_info, 'trade_contract_size') and s_info.trade_contract_size > 0:
            point_multiplier = float(s_info.trade_contract_size)
        else:
            if "XAU" in sym_upper or "GOLD" in sym_upper or "XAG" in sym_upper or "SILVER" in sym_upper:
                point_multiplier = 100.0 if "XAU" in sym_upper or "GOLD" in sym_upper else 1000.0
            elif "WTI" in sym_upper or "BRENT" in sym_upper or "OIL" in sym_upper or "XTI" in sym_upper or "XBR" in sym_upper:
                point_multiplier = 100.0
            elif any(fx in sym_upper for fx in ["EUR", "GBP", "AUD", "NZD", "USDJPY"]):
                point_multiplier = 100000.0
            elif "US500" in sym_upper or "SP500" in sym_upper:
                point_multiplier = 1.0
            else:
                point_multiplier = 1.0

        calculated_size = round(risk_usd / (stop_distance * point_multiplier), 2)

        # 🔧 Tope por clase de activo (WTI y BRENT ahora usan "OIL")
        if canonical_sym == "XAU":
            max_lot = float(os.getenv("GOLD_MAX_LOT_SIZE", "0.02"))
        elif canonical_sym == "XAG":
            max_lot = float(os.getenv("XAG_MAX_LOT_SIZE", "0.05"))
        elif canonical_sym == "OIL":
            max_lot = float(os.getenv("CRUDE_MAX_LOT_SIZE", "0.50"))
        elif canonical_sym == "US500":
            max_lot = float(os.getenv("US500_MAX_LOT_SIZE", "1.0"))
        elif canonical_sym in ["BTC", "ETH", "SOL"]:
            max_lot = float(os.getenv("CRYPTO_MAX_LOT_SIZE", "0.10"))
        else:
            max_lot = float(os.getenv("FOREX_MAX_LOT_SIZE", "0.10"))

        calculated_size = min(calculated_size, max_lot)

        # Ajuste a volume_min/step de MT5
        if s_info:
            vol_step = getattr(s_info, 'volume_step', 0.01)
            vol_min = getattr(s_info, 'volume_min', 0.01)
            if vol_step > 0:
                calculated_size = round(calculated_size / vol_step) * vol_step
            calculated_size = max(vol_min, calculated_size)

        calculated_size = max(0.01, round(calculated_size, 2))

        # FIX: si volume_min del broker > cap, comprobar viabilidad
        if s_info:
            broker_min = getattr(s_info, 'volume_min', 0.01)
            if broker_min > max_lot:
                risk_with_broker_min_usd = broker_min * stop_distance * point_multiplier
                risk_with_broker_min_pct = (risk_with_broker_min_usd / self.current_equity) * 100.0

                if canonical_sym == "XAU":
                    base_risk_pct = float(os.getenv("GOLD_MAX_RISK_PCT", "0.3"))
                elif canonical_sym in ["BTC", "ETH", "SOL"]:
                    base_risk_pct = float(os.getenv("CRYPTO_MAX_RISK_PCT", "1.0"))
                else:
                    base_risk_pct = self.max_risk_per_trade_pct
                max_acceptable_pct = base_risk_pct * self.BROKER_MIN_TOLERANCE_MULT

                if risk_with_broker_min_pct <= max_acceptable_pct:
                    if canonical_sym not in self._forced_min_volume:
                        self._forced_min_volume[canonical_sym] = broker_min
                        logger.info(
                            f"✅ AJUSTE POR VOLUME_MIN: Broker exige {broker_min} lotes para {canonical_sym} "
                            f"(cap={max_lot}). Riesgo real: {risk_with_broker_min_pct:.2f}% "
                            f"(aceptable ≤ {max_acceptable_pct:.2f}%). Usando {broker_min} lotes."
                        )
                    calculated_size = broker_min
                else:
                    msg = (
                        f"ACTIVO BLOQUEADO: volume_min del broker ({broker_min}) "
                        f"implica riesgo de {risk_with_broker_min_pct:.2f}% "
                        f"(> {max_acceptable_pct:.2f}% aceptable) para {canonical_sym}."
                    )
                    if canonical_sym not in self._blocked_assets:
                        logger.error(f"🛡️ {msg}")
                        self._blocked_assets[canonical_sym] = msg
                        log_rejection(
                            symbol=symbol,
                            reason=msg,
                            event_type="ASSET_BLOCKED",
                            details=(
                                f"volume_min={broker_min}, cap={max_lot}, "
                                f"stop_distance={stop_distance:.5f}, "
                                f"contract_size={point_multiplier}, "
                                f"riesgo_real={risk_with_broker_min_pct:.2f}%"
                            ),
                            side=side,
                            price=price
                        )
                    return RiskVerdict(False, msg, 0.0, 0.0, 0.0, False)

        self._pending_orders_lock[canonical_sym] = time.time()

        final_risk_usd = calculated_size * stop_distance * point_multiplier

        logger.info(
            f"🎯 Señal {side} APROBADA por Risk Guardian. "
            f"Size: {calculated_size} lotes (Máx: {max_lot}) | "
            f"Riesgo: ${final_risk_usd:.2f} ({risk_pct:.2f}%) | "
            f"Contract Size: {point_multiplier} | Stop: ${stop_distance:.5f}"
        )

        return RiskVerdict(
            authorized=True,
            rejection_reason=None,
            authorized_size_units=calculated_size,
            risk_amount_usd=round(final_risk_usd, 2),
            stop_distance_usd=stop_distance,
            circuit_breaker_tripped=False
        )

    def release_pending_lock(self, symbol: str):
        canonical_sym = get_canonical_asset(symbol)
        self._pending_orders_lock.pop(canonical_sym, None)

    def register_trade_executed(self, symbol: Optional[str] = None):
        self.trades_executed_today += 1
        self.last_trade_timestamp = time.time()
        self.active_positions_count += 1
        if symbol:
            canonical_sym = get_canonical_asset(symbol)
            self.active_symbols.add(symbol)
            self.active_symbols.add(canonical_sym)
            self.release_pending_lock(symbol)
        logger.info(f"Trade registrado. Cuota de hoy: {self.trades_executed_today}/{self.max_daily_trades}")

    def register_trade_closed(self, pnl_usd: float = 0.0, symbol: Optional[str] = None):
        if self.active_positions_count > 0:
            self.active_positions_count -= 1
        if symbol:
            canonical_sym = get_canonical_asset(symbol)
            self.active_symbols.discard(symbol)
            self.active_symbols.discard(canonical_sym)
            if pnl_usd < 0:
                now_ts = time.time()
                self.last_stop_loss_by_symbol[symbol] = now_ts
                self.last_stop_loss_by_symbol[canonical_sym] = now_ts
                sl_min = int(float(os.getenv("STOP_LOSS_CUARENTENA_SECONDS", "300")) / 60)
                logger.info(f"🛡️ Resguardo patrimonial activado: Cuarentena de {sl_min} min en {symbol} ({canonical_sym}) tras Stop Loss. PnL: ${pnl_usd:.2f}")
        self.current_equity += pnl_usd
        if self.current_equity > self.daily_peak_equity:
            self.daily_peak_equity = self.current_equity

    def get_status_report(self) -> dict:
        return {
            "initial_capital": round(self.initial_capital, 2),
            "current_equity": round(self.current_equity, 2),
            "daily_peak_equity": round(self.daily_peak_equity, 2),
            "drawdown_pct": round(
                ((self.daily_peak_equity - self.current_equity) / self.daily_peak_equity) * 100.0
                if self.daily_peak_equity > 0 else 0.0, 2
            ),
            "trades_executed_today": self.trades_executed_today,
            "max_daily_trades": self.max_daily_trades,
            "active_positions_count": self.active_positions_count,
            "max_concurrent_positions": self.max_concurrent_positions,
            "circuit_breaker_active": self.circuit_breaker_active,
            "blocked_assets": dict(self._blocked_assets),
            "forced_min_volume": dict(self._forced_min_volume),
            "pending_locks": list(self._pending_orders_lock.keys()),
        }