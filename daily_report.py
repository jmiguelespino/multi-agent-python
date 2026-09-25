"""
=============================================================================
QUANTEDGE AI — REPORTE DIARIO POR TELEGRAM (CLI WRAPPER)
=============================================================================
🔧 v1.1.0 — LOTE FUSIONADO 2.6+3:
  • 🐛 B12 CORREGIDO: la lógica de build_daily_report ahora está en
    report_utils.py. Este archivo es solo un wrapper CLI.

Ejecución manual:
    python daily_report.py
    python daily_report.py --days 7
    python daily_report.py --no-send
=============================================================================
"""

import os
import sys
import argparse
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

try:
    from report_utils import build_daily_report
except ImportError as e:
    print(f"❌ No se pudo importar report_utils: {e}")
    sys.exit(1)

try:
    from telegram_notifier import send_telegram_alert
except ImportError:
    print("❌ No se pudo importar telegram_notifier")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Reporte diario QuantEdge AI")
    parser.add_argument("--days", type=int, default=int(os.getenv("REPORT_DAYS", "1")),
                        help="Cuántos días analizar (default: 1)")
    parser.add_argument("--no-send", action="store_true",
                        help="Solo imprimir, no enviar a Telegram")
    parser.add_argument("--include-tests", action="store_true",
                        help="Incluir trades de test en el reporte")
    args = parser.parse_args()

    report = build_daily_report(days=args.days, include_tests=args.include_tests)

    if args.no_send:
        print(report)
        return

    if send_telegram_alert(report):
        print("✅ Reporte enviado a Telegram")
        print(report)
    else:
        print("❌ No se pudo enviar el reporte")
        print(report)
        sys.exit(1)


if __name__ == "__main__":
    main()