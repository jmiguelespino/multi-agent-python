"""
telegram_notifier.py — Módulo de Alertas Telegram con Blindaje Anti-Spam Institucional
"""
import os
import time
import logging
from typing import List
import urllib.request
import urllib.parse
import json
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("TelegramNotifier")

class TelegramAntiSpam:
    def __init__(self, min_interval_seconds: float = 5.0, max_per_10_min: int = 5):
        self.min_interval_seconds = min_interval_seconds
        self.max_per_10_min = max_per_10_min
        self.last_sent_timestamp = 0.0
        self.sent_history: List[float] = []

    def can_send(self) -> bool:
        now = time.time()
        if now - self.last_sent_timestamp < self.min_interval_seconds:
            logger.warning(f"Telegram Anti-Spam: Notificación descartada (< {self.min_interval_seconds}s desde la última)")
            return False

        ten_min_ago = now - 600.0
        self.sent_history = [t for t in self.sent_history if t > ten_min_ago]
        if len(self.sent_history) >= self.max_per_10_min:
            logger.warning(f"Telegram Anti-Spam: Límite de {self.max_per_10_min} alertas por 10 min alcanzado.")
            return False

        return True

    def record_send(self):
        now = time.time()
        self.last_sent_timestamp = now
        self.sent_history.append(now)

anti_spam = TelegramAntiSpam()

def send_telegram_alert(message: str, parse_mode: str = "Markdown") -> bool:
    enabled_str = os.getenv("TELEGRAM_ENABLED", "true").lower()
    if enabled_str in ("false", "0", "no"):
        return False

    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        return False

    if not anti_spam.can_send():
        return False

    url = f"https://api.telegram.org/bot{token.strip()}/sendMessage"
    payload = json.dumps({
        "chat_id": chat_id.strip(),
        "text": message,
        "parse_mode": parse_mode
    }).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                anti_spam.record_send()
                logger.info("Alerta de Telegram enviada exitosamente.")
                return True
            else:
                logger.warning(f"Telegram API respondió con status: {response.status}")
                return False
    except Exception as e:
        logger.error(f"Error al despachar alerta a Telegram: {e}")
        return False