"""
MÓDULO DE EJECUCIÓN INSTITUCIONAL Y OMS (AGENTE 4)

🔧 v1.7.0 — LOTE 2.5 (fixes post-reporte real):
  • 🐛 B15 CORREGIDO: nuevo método _scan_recent_deals_for_closures() que
    escanea history_deals_get cada 30s buscando cierres huérfanos
    (posiciones abiertas y cerradas entre ciclos con throttle de 1s).
    Se registran como cierres con reason="MANUAL_CLOSE" si no se detectan
    por sync_mt5_positions.
  • Lote 2 mantenido (B4: freeze_level + min_stop_distance).
  • Lote 1 mantenido (B2: sin place_bracket_order; B11: PENDING_PNL).
  • logger.propagate = False.
"""
import os
import asyncio
import logging
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Optional, List, Any
import MetaTrader5 as mt5
from dotenv import load_dotenv

from audit_logger import (
    log_order_filled,
    log_break_even,
    log_trailing_stop,
    log_position_closed,
    log_audit_event
)
from time_utils import mt5_ms_to_epoch

load_dotenv()
logger = logging.getLogger("ExecutionOMS")
logger.propagate = False


def get_canonical_asset(symbol: str) -> str:
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


class OrderStatus(str, Enum):
    PENDING = "PENDING"
    FILLED = "FILLED"
    CANCELED = "CANCELED"
    REJECTED = "REJECTED"
    PENDING_PNL = "PENDING_PNL"


@dataclass
class BracketOrder:
    order_id: str
    symbol: str
    side: str
    quantity: float
    entry_price: float
    stop_loss: float
    take_profit: float
    break_even_activated: bool = False
    trailing_stop_active: bool = False
    trailing_stop_price: Optional[float] = None
    status: OrderStatus = OrderStatus.PENDING
    slippage_usd: float = 0.0
    commission_usd: float = 0.0
    entry_timestamp: float = 0.0
    pnl_usd: float = 0.0
    close_price: float = 0.0
    pnl_fetch_attempts: int = 0
    pnl_fetch_last_attempt_ts: float = 0.0
    close_reason_pending: str = "UNKNOWN"


class ExecutionOMSAgent:
    PNL_MAX_FETCH_ATTEMPTS = 6
    PNL_RETRY_BACKOFF_BASE_SEC = 2.0

    # 🆕 B15: cada cuántos segundos escanear deals en busca de cierres huérfanos
    DEALS_SCAN_INTERVAL_SEC = 30.0
    # 🆕 B15: ventana de tiempo hacia atrás para buscar deals
    DEALS_SCAN_LOOKBACK_MIN = 5

    def __init__(self, taker_fee_pct: float = 0.0004, maker_fee_pct: float = 0.0002):
        self.taker_fee_pct = taker_fee_pct
        self.maker_fee_pct = maker_fee_pct
        self.active_orders: Dict[str, BracketOrder] = {}
        self.closed_orders: List[BracketOrder] = []
        self._reported_tickets: set = set()
        self._sl_warning_shown: set = set()

        # 🆕 B15: estado del escaneo de deals
        self._last_deals_scan_ts: float = 0.0
        self._processed_deal_tickets: set = set()

        self.be_trigger_atr = float(os.getenv("BREAK_EVEN_ATR_TRIGGER", "1.2"))
        self.be_lock_atr = float(os.getenv("BREAK_EVEN_LOCK_ATR", "0.10"))
        self.trail_trigger_atr = float(os.getenv("TRAILING_STOP_ATR_TRIGGER", "2.0"))
        self.trail_dist_atr = float(os.getenv("TRAILING_STOP_ATR_DISTANCE", "1.8"))
        self.magic_number = int(os.getenv("MAGIC_NUMBER", "992026"))

    # -------------------------------------------------------------------------
    # Helpers
    # -------------------------------------------------------------------------
    @staticmethod
    def _get_contract_size(symbol: str) -> float:
        try:
            info = mt5.symbol_info(symbol)
            if info and getattr(info, "trade_contract_size", 0) > 0:
                return float(info.trade_contract_size)
        except Exception:
            pass

        s = symbol.upper()
        if "XAU" in s or "GOLD" in s:
            return 100.0
        if "XAG" in s or "SILVER" in s:
            return 1000.0
        if any(fx in s for fx in ["EUR", "GBP", "AUD", "NZD", "USDJPY", "CHF", "CAD"]):
            return 100000.0
        if any(o in s for o in ["WTI", "XTI", "BRENT", "XBR", "OIL"]):
            return 100.0
        if "US500" in s or "SP500" in s:
            return 1.0
        return 1.0

    @staticmethod
    def _get_min_stop_distance(symbol: str) -> tuple[float, float]:
        """
        🐛 B4: devuelve (min_distance_sl_tp, freeze_distance) en unidades de
        precio leyendo TODOS los campos relevantes del broker.
        """
        try:
            info = mt5.symbol_info(symbol)
            if not info:
                return 0.0, 0.0

            point = info.point

            stops_level = max(
                float(getattr(info, "trade_stops_level", 0) or 0),
                float(getattr(info, "stops_level", 0) or 0),
            )
            freeze_level = max(
                float(getattr(info, "trade_freeze_level", 0) or 0),
                float(getattr(info, "freeze_level", 0) or 0),
            )

            if stops_level <= 0 and freeze_level <= 0:
                stops_level = 50.0

            min_distance = stops_level * point
            freeze_distance = freeze_level * point

            return min_distance, freeze_distance
        except Exception:
            return 0.0, 0.0

    @staticmethod
    def _fetch_realized_pnl_from_mt5(
        ticket: int,
        max_retries: int = 3,
        retry_delay: float = 0.5
    ) -> tuple[float, float, str]:
        try:
            from datetime import datetime, timedelta, timezone as _tz
            tz_mt5 = _tz(timedelta(hours=3))
            from_date = datetime.now(tz_mt5) - timedelta(days=7)
            to_date = datetime.now(tz_mt5) + timedelta(days=1)

            deals = None
            for attempt in range(max_retries):
                deals = mt5.history_deals_get(from_date, to_date, position=ticket)

                if not deals or len(deals) == 0:
                    all_deals = mt5.history_deals_get(from_date, to_date)
                    if all_deals:
                        deals = [d for d in all_deals
                                 if (getattr(d, "position_id", None) or getattr(d, "position", None)) == ticket]

                if deals and len(deals) > 0:
                    break

                if attempt < max_retries - 1:
                    logger.debug(
                        f"⏳ Reintentando fetch de deals para ticket #{ticket} "
                        f"(intento {attempt+1}/{max_retries}, esperando {retry_delay:.1f}s)"
                    )
                    time.sleep(retry_delay)
                    retry_delay *= 2

            if not deals:
                logger.warning(
                    f"⚠️ No se encontraron deals en MT5 para el ticket #{ticket} "
                    f"tras {max_retries} intentos. PnL se registrará como 0.0 con reason=UNKNOWN."
                )
                return 0.0, 0.0, "UNKNOWN"

            total_profit = 0.0
            total_commission = 0.0
            total_swap = 0.0
            close_price = 0.0
            reason = "UNKNOWN"

            for d in deals:
                pid = getattr(d, "position_id", None) or getattr(d, "position", None)
                if pid != ticket:
                    continue

                total_profit += getattr(d, "profit", 0.0)
                total_commission += getattr(d, "commission", 0.0)
                total_swap += getattr(d, "swap", 0.0)

                if getattr(d, "entry", None) == mt5.DEAL_ENTRY_OUT:
                    close_price = d.price
                    comment = (d.comment or "").lower()
                    if "tp" in comment or "take" in comment:
                        reason = "TAKE_PROFIT"
                    elif "sl" in comment or "stop" in comment:
                        reason = "STOP_LOSS"
                    elif "trail" in comment:
                        reason = "TRAILING_STOP"
                    else:
                        reason = "MANUAL_CLOSE"

            total_pnl = total_profit + total_commission + total_swap

            if reason == "UNKNOWN" and close_price > 0:
                reason = "MANUAL_CLOSE"

            return round(total_pnl, 2), close_price, reason
        except Exception as e:
            logger.error(f"Error obteniendo PnL real del ticket #{ticket}: {e}")
            return 0.0, 0.0, "UNKNOWN"

    # -------------------------------------------------------------------------
    # 🆕 B15: escaneo de deals para detectar cierres huérfanos
    # -------------------------------------------------------------------------
    def _scan_recent_deals_for_closures(self, risk_guardian: Optional[Any] = None):
        """
        🆕 B15: escanea los deals recientes de MT5 y detecta cierres que
        sync_mt5_positions() pudo haber perdido (posiciones abiertas y
        cerradas entre ciclos con throttle de 1s).

        Cada DEALS_SCAN_INTERVAL_SEC:
          - Consulta history_deals_get de los últimos DEALS_SCAN_LOOKBACK_MIN min.
          - Filtra DEAL_ENTRY_OUT.
          - Para cada uno, si su position_id NO está en closed_orders ni
            active_orders → registrar como cierre huérfano.
        """
        now = time.time()
        if now - self._last_deals_scan_ts < self.DEALS_SCAN_INTERVAL_SEC:
            return
        self._last_deals_scan_ts = now

        try:
            from datetime import datetime, timedelta, timezone as _tz
            tz_mt5 = _tz(timedelta(hours=3))
            from_date = datetime.now(tz_mt5) - timedelta(minutes=self.DEALS_SCAN_LOOKBACK_MIN)
            to_date = datetime.now(tz_mt5) + timedelta(minutes=1)

            deals = mt5.history_deals_get(from_date, to_date)
            if not deals:
                return

            # Tickets ya conocidos (en active_orders o closed_orders)
            known_tickets: set = set()
            for o in self.closed_orders:
                if o.order_id and o.order_id.isdigit():
                    known_tickets.add(int(o.order_id))
            for oid in self.active_orders.keys():
                if oid.isdigit():
                    known_tickets.add(int(oid))

            orphan_closures = []
            for d in deals:
                if getattr(d, "entry", None) != mt5.DEAL_ENTRY_OUT:
                    continue
                pid = getattr(d, "position_id", None) or getattr(d, "position", None)
                if not pid or pid in known_tickets:
                    continue
                if d.ticket in self._processed_deal_tickets:
                    continue
                orphan_closures.append(d)

            if not orphan_closures:
                return

            logger.info(f"🩹 B15: {len(orphan_closures)} cierre(s) huérfano(s) detectado(s). Procesando...")

            for d in orphan_closures:
                pid = getattr(d, "position_id", None) or getattr(d, "position", None)
                self._processed_deal_tickets.add(d.ticket)

                # Reconstruir info del cierre
                pnl_usd, close_price, close_reason = self._fetch_realized_pnl_from_mt5(
                    pid, max_retries=1, retry_delay=0.0
                )
                if close_reason == "UNKNOWN":
                    close_reason = "MANUAL_CLOSE"

                symbol = getattr(d, "symbol", "UNKNOWN")
                volume = getattr(d, "volume", 0.0)

                # DEAL_TYPE_BUY en un cierre significa que la posición era SELL
                deal_type = getattr(d, "type", None)
                if deal_type == mt5.DEAL_TYPE_BUY:
                    side = "SELL"
                elif deal_type == mt5.DEAL_TYPE_SELL:
                    side = "BUY"
                else:
                    side = "UNKNOWN"

                logger.warning(
                    f"🩹 B15: cierre huérfano #{pid} {symbol} {side} {volume} | "
                    f"PnL=${pnl_usd:.2f} | reason={close_reason} | "
                    f"(no estaba en active_orders ni closed_orders)"
                )

                log_position_closed(
                    symbol=symbol,
                    side=side,
                    volume=volume,
                    entry_price=0.0,   # desconocido
                    exit_price=close_price,
                    pnl_usd=pnl_usd,
                    pnl_percent=0.0,
                    reason=close_reason,
                    ticket=pid,
                    order_id=str(pid),
                    duration_sec=0,
                    is_test=False
                )

                if risk_guardian:
                    risk_guardian.register_trade_closed(pnl_usd=pnl_usd, symbol=symbol)

        except Exception as e:
            logger.debug(f"B15: error escaneando deals: {e}")

    # -------------------------------------------------------------------------
    # Sincronización con MT5
    # -------------------------------------------------------------------------
    def sync_mt5_positions(self, raw_positions, risk_guardian: Optional[Any] = None):
        if raw_positions is None:
            raw_positions = []

        # 🆕 B15: escanear deals primero (por si hay cierres huérfanos)
        self._scan_recent_deals_for_closures(risk_guardian)

        current_tickets = {str(p.ticket) for p in raw_positions}

        # 1. Detectar ABIERTAS
        for p in raw_positions:
            order_key = str(p.ticket)
            side = "BUY" if p.type == mt5.ORDER_TYPE_BUY else "SELL"

            if order_key not in self.active_orders:
                entry_time = mt5_ms_to_epoch(p.time_msc) if hasattr(p, 'time_msc') and p.time_msc else time.time()

                order = BracketOrder(
                    order_id=order_key,
                    symbol=p.symbol,
                    side=side,
                    quantity=p.volume,
                    entry_price=p.price_open,
                    stop_loss=p.sl,
                    take_profit=p.tp,
                    status=OrderStatus.FILLED,
                    entry_timestamp=entry_time
                )
                self.active_orders[order_key] = order

                # 🆕 B10: notificar al RiskGuardian que la posición fue confirmada
                if risk_guardian and hasattr(risk_guardian, "notify_position_confirmed"):
                    risk_guardian.notify_position_confirmed(p.symbol)

            if order_key not in self._reported_tickets:
                self._reported_tickets.add(order_key)
                log_audit_event(
                    event_type="OPEN_POSITION_DETECTED",
                    category="ORDER",
                    symbol=p.symbol,
                    reason="Posición abierta detectada en MT5 y vinculada al motor de blindaje OMS.",
                    details=f"Ticket #{p.ticket} | {side} {p.volume} {p.symbol} @ ${p.price_open:.2f} | PnL Flotante: ${p.profit:,.2f} USD",
                    side=side,
                    price=p.price_open,
                    volume=p.volume,
                    stop_loss=p.sl,
                    take_profit=p.tp,
                    ticket=p.ticket,
                    order_id=order_key
                )

        # 2. Detectar CERRADAS
        now = time.time()
        for order_id in list(self.active_orders.keys()):
            if not order_id.isdigit():
                continue

            if order_id in current_tickets:
                continue

            closed_order = self.active_orders[order_id]
            ticket_int = int(order_id)

            if closed_order.status == OrderStatus.PENDING_PNL:
                elapsed = now - closed_order.pnl_fetch_last_attempt_ts
                backoff = self.PNL_RETRY_BACKOFF_BASE_SEC * (2 ** closed_order.pnl_fetch_attempts)
                if elapsed < backoff:
                    continue

                if closed_order.pnl_fetch_attempts >= self.PNL_MAX_FETCH_ATTEMPTS:
                    logger.error(
                        f"❌ Ticket #{ticket_int}: no se pudo obtener PnL tras "
                        f"{self.PNL_MAX_FETCH_ATTEMPTS} intentos. Se registra como 0.0/UNKNOWN."
                    )
                    pnl_usd, close_price, close_reason = 0.0, closed_order.close_price, "UNKNOWN"
                else:
                    pnl_usd, close_price, close_reason = self._fetch_realized_pnl_from_mt5(
                        ticket_int, max_retries=1, retry_delay=0.0
                    )
                    closed_order.pnl_fetch_attempts += 1
                    closed_order.pnl_fetch_last_attempt_ts = now

                    if close_reason == "UNKNOWN":
                        logger.info(
                            f"⏳ Ticket #{ticket_int}: PnL aún no disponible en MT5 "
                            f"(intento {closed_order.pnl_fetch_attempts}/{self.PNL_MAX_FETCH_ATTEMPTS})."
                        )
                        continue
            else:
                pnl_usd, close_price, close_reason = self._fetch_realized_pnl_from_mt5(ticket_int)

                if close_reason == "UNKNOWN":
                    closed_order.status = OrderStatus.PENDING_PNL
                    closed_order.pnl_fetch_attempts = 1
                    closed_order.pnl_fetch_last_attempt_ts = now
                    closed_order.close_price = close_price
                    closed_order.close_reason_pending = "UNKNOWN"
                    logger.info(
                        f"⏳ Ticket #{ticket_int}: cerrado pero PnL no disponible. "
                        f"Marcado como PENDING_PNL (intento 1/{self.PNL_MAX_FETCH_ATTEMPTS})."
                    )
                    continue

            # PnL confirmado
            closed_order = self.active_orders.pop(order_id)
            closed_order.pnl_usd = pnl_usd
            closed_order.close_price = close_price
            closed_order.status = OrderStatus.CANCELED
            closed_order.close_reason_pending = close_reason
            self.closed_orders.append(closed_order)

            if order_id in self._reported_tickets:
                self._reported_tickets.remove(order_id)

            if risk_guardian:
                risk_guardian.register_trade_closed(pnl_usd=pnl_usd, symbol=closed_order.symbol)

            contract_size = self._get_contract_size(closed_order.symbol)
            notional = closed_order.entry_price * closed_order.quantity * contract_size
            pnl_percent = (pnl_usd / notional) * 100.0 if notional > 0 else 0.0

            duration_sec = int(time.time() - closed_order.entry_timestamp) if closed_order.entry_timestamp else 0

            log_position_closed(
                symbol=closed_order.symbol,
                side=closed_order.side,
                volume=closed_order.quantity,
                entry_price=closed_order.entry_price,
                exit_price=close_price,
                pnl_usd=pnl_usd,
                pnl_percent=round(pnl_percent, 2),
                reason=close_reason,
                ticket=ticket_int,
                order_id=order_id,
                duration_sec=duration_sec
            )
            logger.info(
                f"📉 Posición cerrada #{ticket_int} {closed_order.symbol} | "
                f"PnL: ${pnl_usd:.2f} | Razón: {close_reason} | Duración: {duration_sec}s"
            )

    # -------------------------------------------------------------------------
    # Modificación de SL en MT5
    # -------------------------------------------------------------------------
    def _update_mt5_sl(self, ticket_id: str, symbol: str, new_sl: float, current_tp: float):
        """
        🐛 B4: usa _get_min_stop_distance() que lee trade_stops_level Y
        trade_freeze_level. Respeta el freeze_level.
        """
        if not ticket_id.isdigit():
            return

        try:
            ticket = int(ticket_id)

            positions = mt5.positions_get(ticket=ticket)
            if not positions:
                return

            pos = positions[0]
            tick = mt5.symbol_info_tick(symbol)
            info = mt5.symbol_info(symbol)

            if not tick or not info:
                return

            min_distance, freeze_distance = self._get_min_stop_distance(symbol)

            # 🆕 B4: verificar freeze_level ANTES de intentar modificar
            if freeze_distance > 0:
                if pos.type == mt5.ORDER_TYPE_BUY:
                    distance_to_freeze = abs(tick.bid - pos.price_open)
                else:
                    distance_to_freeze = abs(tick.ask - pos.price_open)

                if distance_to_freeze < freeze_distance:
                    logger.debug(
                        f"🧊 Ticket #{ticket}: precio dentro del freeze_level "
                        f"({distance_to_freeze:.5f} < {freeze_distance:.5f}). "
                        f"Modificación de SL pospuesta."
                    )
                    return

            # Ajustar SL para respetar la distancia mínima
            if pos.type == mt5.ORDER_TYPE_BUY:
                if new_sl >= tick.bid - min_distance:
                    adjusted_sl = round(tick.bid - min_distance, info.digits)
                    logger.debug(
                        f"SL ajustado para ticket #{ticket}: {new_sl} → {adjusted_sl} "
                        f"(bid={tick.bid}, min_dist={min_distance:.5f})"
                    )
                    new_sl = adjusted_sl
            else:
                if new_sl <= tick.ask + min_distance:
                    adjusted_sl = round(tick.ask + min_distance, info.digits)
                    logger.debug(
                        f"SL ajustado para ticket #{ticket}: {new_sl} → {adjusted_sl} "
                        f"(ask={tick.ask}, min_dist={min_distance:.5f})"
                    )
                    new_sl = adjusted_sl

            req = {
                "action": mt5.TRADE_ACTION_SLTP,
                "position": ticket,
                "symbol": symbol,
                "sl": new_sl,
                "tp": current_tp,
            }
            res = mt5.order_send(req)

            if not (res and res.retcode == mt5.TRADE_RETCODE_DONE):
                comment = res.comment if res else "Error de envío"
                if ticket not in self._sl_warning_shown:
                    logger.warning(f"⚠️ No se pudo modificar SL (Ticket #{ticket}): {comment}")
                    self._sl_warning_shown.add(ticket)
        except Exception as e:
            logger.error(f"Error modificando SL en MT5: {e}")

    async def place_bracket_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
        current_market_price: float,
        stop_loss: float,
        take_profit: float
    ) -> None:
        """🐛 B2: stub deprecado. La posición se detecta en sync_mt5_positions."""
        logger.debug(
            f"ℹ️ place_bracket_order llamado para {symbol} {side} {quantity} "
            f"(deprecado — sync_mt5_positions gestionará la posición)"
        )
        return None

    def update_tick_price(self, order_id: str, tick_symbol: str, current_price: float, atr: float) -> Optional[str]:
        if order_id not in self.active_orders:
            return None

        order = self.active_orders[order_id]

        if order.status == OrderStatus.PENDING_PNL:
            return None

        if order.symbol != tick_symbol and get_canonical_asset(order.symbol) != get_canonical_asset(tick_symbol):
            return None

        if order.side == "BUY":
            if not order.break_even_activated and current_price >= order.entry_price + (atr * self.be_trigger_atr):
                old_sl = order.stop_loss
                be_price = round(order.entry_price + (atr * self.be_lock_atr), 2)
                if order.stop_loss < be_price:
                    order.stop_loss = be_price
                    order.break_even_activated = True
                    self._update_mt5_sl(order_id, order.symbol, be_price, order.take_profit)
                    log_break_even(
                        symbol=order.symbol,
                        ticket=int(order_id) if order_id.isdigit() else None,
                        old_sl=old_sl,
                        new_sl=order.stop_loss,
                        current_price=current_price,
                        profit_locked_usd=round((be_price - order.entry_price) * order.quantity, 2),
                        order_id=order_id
                    )

            if not order.trailing_stop_active and current_price >= order.entry_price + (atr * self.trail_trigger_atr):
                order.trailing_stop_active = True
                order.trailing_stop_price = round(current_price - (atr * self.trail_dist_atr), 2)
                self._update_mt5_sl(order_id, order.symbol, order.trailing_stop_price, order.take_profit)
                log_trailing_stop(
                    symbol=order.symbol,
                    ticket=int(order_id) if order_id.isdigit() else None,
                    old_sl=order.stop_loss,
                    new_sl=order.trailing_stop_price,
                    current_price=current_price,
                    order_id=order_id
                )
            elif order.trailing_stop_active and order.trailing_stop_price:
                new_trail = round(current_price - (atr * self.trail_dist_atr), 2)
                if new_trail > order.trailing_stop_price:
                    old_trail = order.trailing_stop_price
                    order.trailing_stop_price = new_trail
                    self._update_mt5_sl(order_id, order.symbol, new_trail, order.take_profit)
                    log_trailing_stop(
                        symbol=order.symbol,
                        ticket=int(order_id) if order_id.isdigit() else None,
                        old_sl=old_trail,
                        new_sl=new_trail,
                        current_price=current_price,
                        order_id=order_id
                    )

        elif order.side == "SELL":
            if not order.break_even_activated and current_price <= order.entry_price - (atr * self.be_trigger_atr):
                old_sl = order.stop_loss
                be_price = round(order.entry_price - (atr * self.be_lock_atr), 2)
                if order.stop_loss == 0 or order.stop_loss > be_price:
                    order.stop_loss = be_price
                    order.break_even_activated = True
                    self._update_mt5_sl(order_id, order.symbol, be_price, order.take_profit)
                    log_break_even(
                        symbol=order.symbol,
                        ticket=int(order_id) if order_id.isdigit() else None,
                        old_sl=old_sl,
                        new_sl=order.stop_loss,
                        current_price=current_price,
                        profit_locked_usd=round((order.entry_price - be_price) * order.quantity, 2),
                        order_id=order_id
                    )

            if not order.trailing_stop_active and current_price <= order.entry_price - (atr * self.trail_trigger_atr):
                order.trailing_stop_active = True
                order.trailing_stop_price = round(current_price + (atr * self.trail_dist_atr), 2)
                self._update_mt5_sl(order_id, order.symbol, order.trailing_stop_price, order.take_profit)
                log_trailing_stop(
                    symbol=order.symbol,
                    ticket=int(order_id) if order_id.isdigit() else None,
                    old_sl=order.stop_loss,
                    new_sl=order.trailing_stop_price,
                    current_price=current_price,
                    order_id=order_id
                )
            elif order.trailing_stop_active and order.trailing_stop_price:
                new_trail = round(current_price + (atr * self.trail_dist_atr), 2)
                if new_trail < order.trailing_stop_price:
                    old_trail = order.trailing_stop_price
                    order.trailing_stop_price = new_trail
                    self._update_mt5_sl(order_id, order.symbol, new_trail, order.take_profit)
                    log_trailing_stop(
                        symbol=order.symbol,
                        ticket=int(order_id) if order_id.isdigit() else None,
                        old_sl=old_trail,
                        new_sl=new_trail,
                        current_price=current_price,
                        order_id=order_id
                    )

        return None