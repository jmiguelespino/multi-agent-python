"""
MÓDULO DE CONECTIVIDAD Y DATA STREAMING EN TIEMPO REAL (L1/L2)
Arquitectura: Asyncio WebSocket Manager con Backpressure & Exponential Backoff
"""
import asyncio
import json
import logging
import time
from dataclasses import dataclass
from typing import AsyncGenerator, Dict, List, Optional
import aiohttp

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("DataStreamer")

@dataclass(slots=True)
class Tick:
    timestamp_ms: int
    symbol: str
    price: float
    quantity: float
    is_buyer_maker: bool  # True = Sell aggressor, False = Buy aggressor

@dataclass(slots=True)
class OrderBookL2:
    timestamp_ms: int
    symbol: str
    bids: List[tuple[float, float]]  # (price, quantity)
    asks: List[tuple[float, float]]  # (price, quantity)
    spread: float
    spread_bps: float
    mid_price: float

class WebSocketManager:
    """
    Gestor de WebSocket institucional para streaming L1/L2.
    Implementa reconexión automática con jitter y backpressure buffer.
    """
    def __init__(self, symbol: str = "BTCUSDT", max_queue_size: int = 10000):
        self.symbol = symbol.lower()
        self.base_ws_url = "wss://stream.binance.com:9443/ws"
        self.tick_queue: asyncio.Queue[Tick] = asyncio.Queue(maxsize=max_queue_size)
        self.is_running: bool = False
        self._reconnect_delay: float = 1.0
        self._max_reconnect_delay: float = 30.0

    async def start(self):
        self.is_running = True
        while self.is_running:
            try:
                stream_url = f"{self.base_ws_url}/{self.symbol}@trade"
                logger.info(f"Conectando a stream de mercado: {stream_url}")
                
                async with aiohttp.ClientSession() as session:
                    async with session.ws_connect(stream_url, heartbeat=20.0) as ws:
                        logger.info(f"Stream L1 conectado exitosamente para {self.symbol.upper()}")
                        self._reconnect_delay = 1.0  # Reset backoff tras éxito
                        
                        async for msg in ws:
                            if not self.is_running:
                                break
                            if msg.type == aiohttp.WSMsgType.TEXT:
                                data = json.loads(msg.data)
                                if data.get("e") == "trade":
                                    tick = Tick(
                                        timestamp_ms=data["T"],
                                        symbol=data["s"],
                                        price=float(data["p"]),
                                        quantity=float(data["q"]),
                                        is_buyer_maker=data["m"]
                                    )
                                    # Manejo de backpressure
                                    if self.tick_queue.full():
                                        try:
                                            self.tick_queue.get_nowait()
                                        except asyncio.QueueEmpty:
                                            pass
                                    await self.tick_queue.put(tick)
                            elif msg.type in (aiohttp.WSMsgType.CLOSED, aiohttp.WSMsgType.ERROR):
                                logger.warning("WebSocket desconectado. Iniciando ciclo de recuperación...")
                                break
            except Exception as exc:
                logger.error(f"Excepción en socket stream: {exc}. Reintentando en {self._reconnect_delay:.1f}s")
                await asyncio.sleep(self._reconnect_delay)
                self._reconnect_delay = min(self._max_reconnect_delay, self._reconnect_delay * 1.8)

    async def get_tick_stream(self) -> AsyncGenerator[Tick, None]:
        """Generador asíncrono para consumir ticks sin bloqueo de event loop."""
        while self.is_running or not self.tick_queue.empty():
            tick = await self.tick_queue.get()
            yield tick
            self.tick_queue.task_done()

    def stop(self):
        self.is_running = False
        logger.info("Deteniendo WebSocketManager...")