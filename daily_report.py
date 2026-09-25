"""
=============================================================================
QUANTEDGE AI — REPORTE DIARIO POR TELEGRAM
=============================================================================
Envía un resumen del día por Telegram:
  • PnL del día (realizado + flotante)
  • Trades del día (wins / losses / win rate)
  • Mejor y peor trade
  • Estado del bot y MT5
  • Progreso hacia el mínimo de 30 trades para el learner

Ejecución manual:
    python daily_report.py

Ejecución automática (Programador de Tareas de Windows):
    Programa:  pythonw.exe (o python.exe)
    Argumentos: daily_report.py
    Hora:       23:59 diariamente

Configuración vía .env (opcional):
    REPORT_HOUR=23                        # Hora del reporte (no aplica si se ejecuta desde Task Scheduler)
    REPORT_DAYS=1                         # Cuántos días analizar (default: 1 = hoy)
=============================================================================
"""

import os
import sys
import json
import time
import argparse
from pathlib import Path
from datetime import datetime, timezone, timedelta
from collections import defaultdict
from dotenv import load_dotenv

load_dotenv()

TZ_MT5 = timezone(timedelta(hours=3))

BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "logs" / "trade_audit_history.jsonl"
CONTROL_STATE_FILE = BASE_DIR / "control_state.json"
CONFIG_OPTIMIZED_FILE = BASE_DIR / "config_optimized.json"

# -----------------------------------------------------------------------------
# Alertas Telegram
# -----------------------------------------------------------------------------
try:
    from telegram_notifier import send_telegram_alert
except ImportError:
    print("❌ No se pudo importar telegram_notifier")
    sys.exit(1)


# -----------------------------------------------------------------------------
# Carga de datos
# -----------------------------------------------------------------------------
def load_closures_since(cutoff_ms: int) -> list:
    """Carga cierres desde un timestamp en ms."""
    if not LOG_FILE.exists():
        return []

    closures = []
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if rec.get("category") != "CLOSURE":
                    continue
                if rec.get("pnl_usd") is None:
                    continue
                if rec.get("timestamp", 0) < cutoff_ms:
                    continue
                closures.append(rec)
    except Exception as e:
        print(f"Error leyendo log: {e}")

    closures.sort(key=lambda r: r.get("timestamp", 0))
    return closures


def load_all_closures() -> list:
    """Carga TODOS los cierres (para contar progreso hacia 30)."""
    if not LOG_FILE.exists():
        return []
    closures = []
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if rec.get("category") == "CLOSURE" and rec.get("pnl_usd") is not None:
                    closures.append(rec)
    except Exception:
        pass
    return closures


def count_orders_today(cutoff_ms: int) -> dict:
    """Cuenta eventos ORDER_FILLED y OPEN_POSITION_DETECTED desde cutoff."""
    result = {"orders_filled": 0, "positions_opened": 0, "rejections": 0}
    if not LOG_FILE.exists():
        return result

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if rec.get("timestamp", 0) < cutoff_ms:
                    continue
                event = rec.get("event_type", "")
                cat = rec.get("category", "")

                if event == "ORDER_FILLED":
                    result["orders_filled"] += 1
                elif event == "OPEN_POSITION_DETECTED":
                    result["positions_opened"] += 1
                elif cat == "REJECTION":
                    result["rejections"] += 1
    except Exception:
        pass
    return result


def get_mt5_snapshot() -> dict:
    """Estado actual de MT5 (si está disponible)."""
    try:
        import MetaTrader5 as mt5
        if not mt5.initialize():
            return {}
        acc = mt5.account_info()
        positions = mt5.positions_get() or []
        if acc is None:
            mt5.shutdown()
            return {}

        result = {
            "balance": round(acc.balance, 2),
            "equity": round(acc.equity, 2),
            "margin_free": round(acc.margin_free, 2),
            "positions_count": len(positions),
            "floating_pnl": round(sum(p.profit for p in positions), 2),
            "positions": [
                {
                    "ticket": p.ticket,
                    "symbol": p.symbol,
                    "type": "BUY" if p.type == mt5.ORDER_TYPE_BUY else "SELL",
                    "volume": p.volume,
                    "profit": round(p.profit, 2),
                }
                for p in positions
            ],
        }
        mt5.shutdown()
        return result
    except Exception:
        return {}


def read_control_state() -> dict:
    if not CONTROL_STATE_FILE.exists():
        return {}
    try:
        with open(CONTROL_STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def read_config_optimized() -> dict:
    if not CONFIG_OPTIMIZED_FILE.exists():
        return {}
    try:
        with open(CONFIG_OPTIMIZED_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


# -----------------------------------------------------------------------------
# Formateo
# -----------------------------------------------------------------------------
def format_pnl(value: float) -> str:
    emoji = "🟢" if value > 0 else ("🔴" if value < 0 else "⚪")
    return f"{emoji} `${value:+,.2f}`"


def build_daily_report(days: int = 1) -> str:
    """Construye el mensaje de reporte."""

    # Rango temporal
    now_ms = int(time.time() * 1000)
    cutoff_ms = now_ms - (days * 86400 * 1000)

    # Datos
    closures = load_closures_since(cutoff_ms)
    all_closures = load_all_closures()
    orders = count_orders_today(cutoff_ms)
    mt5_snap = get_mt5_snapshot()
    ctrl = read_control_state()
    config = read_config_optimized()

    # Estadísticas del período
    total = len(closures)
    if total > 0:
        pnls = [float(r.get("pnl_usd", 0)) for r in closures]
        wins = [p for p in pnls if p > 0]
        losses = [p for p in pnls if p <= 0]
        total_pnl = sum(pnls)
        win_rate = (len(wins) / total) * 100
        avg_win = sum(wins) / len(wins) if wins else 0
        avg_loss = abs(sum(losses) / len(losses)) if losses else 0
        gross_profit = sum(wins)
        gross_loss = abs(sum(losses))
        pf = (gross_profit / gross_loss) if gross_loss > 0 else 999.0
        best = max(pnls)
        worst = min(pnls)
    else:
        total_pnl = win_rate = avg_win = avg_loss = pf = best = worst = 0

    # Desglose por activo
    by_symbol = defaultdict(lambda: {"count": 0, "pnl": 0.0})
    for r in closures:
        sym = str(r.get("symbol", "UNKNOWN")).upper()
        by_symbol[sym]["count"] += 1
        by_symbol[sym]["pnl"] += float(r.get("pnl_usd", 0))

    # Encabezado
    day_label = "HOY" if days == 1 else f"ÚLTIMOS {days} DÍAS"
    date_str = datetime.now(TZ_MT5).strftime("%Y-%m-%d")

    lines = [
        f"📊 *QUANTEDGE AI — REPORTE DIARIO*",
        f"_{date_str} ({day_label})_",
        "",
    ]

    # Estado del bot
    paused = ctrl.get("paused", False)
    bot_status = "⏸️ PAUSADO" if paused else "▶️ ACTIVO"
    lines.append(f"*Estado del bot:* {bot_status}")

    # MT5
    if mt5_snap:
        lines.append(f"*MT5:*")
        lines.append(f"  • Balance: `${mt5_snap['balance']:,.2f}`")
        lines.append(f"  • Equidad: `${mt5_snap['equity']:,.2f}`")
        lines.append(f"  • Margen libre: `${mt5_snap['margin_free']:,.2f}`")
        lines.append(f"  • Posiciones abiertas: `{mt5_snap['positions_count']}`")
        if mt5_snap['positions_count'] > 0:
            lines.append(f"  • PnL flotante: {format_pnl(mt5_snap['floating_pnl'])}")
    else:
        lines.append("*MT5:* _no disponible_")

    lines.append("")

    # Actividad del día
    lines.append(f"*Actividad:*")
    lines.append(f"  • Órdenes ejecutadas: `{orders['orders_filled']}`")
    lines.append(f"  • Posiciones cerradas: `{total}`")
    lines.append(f"  • Rechazos: `{orders['rejections']}`")

    lines.append("")

    # Resultados
    if total > 0:
        lines.append(f"*Resultados:*")
        lines.append(f"  • PnL: {format_pnl(total_pnl)}")
        lines.append(f"  • Wins / Losses: `{len(wins)}` / `{len(losses)}`")
        lines.append(f"  • Win rate: `{win_rate:.1f}%`")
        lines.append(f"  • Profit Factor: `{pf:.2f}`")
        lines.append(f"  • Avg Win: `${avg_win:,.2f}` | Avg Loss: `${avg_loss:,.2f}`")
        lines.append(f"  • Mejor trade: `+${best:,.2f}`")
        lines.append(f"  • Peor trade: `${worst:,.2f}`")
    else:
        lines.append(f"*Resultados:* _sin trades cerrados en el período_")

    # Desglose por activo
    if by_symbol:
        lines.append("")
        lines.append(f"*Por activo:*")
        for sym in sorted(by_symbol.keys()):
            data = by_symbol[sym]
            lines.append(f"  • `{sym}`: {data['count']} trades | {format_pnl(data['pnl'])}")

    # Progreso del learner
    lines.append("")
    lines.append(f"*Agente 5 (Learner):*")
    lines.append(f"  • Cierres totales: `{len(all_closures)}` / `30` (mínimo para optimizar)")
    if config:
        lines.append(f"  • Confianza: `{config.get('min_confidence_threshold', 'N/D')}%`")
        lines.append(f"  • SL ATR: `{config.get('atr_stop_multiplier', 'N/D')}×`")
        lines.append(f"  • TP ATR: `{config.get('atr_profit_multiplier', 'N/D')}×`")

    # Pie
    lines.append("")
    lines.append(f"_Reporte generado a las {datetime.now(TZ_MT5).strftime('%H:%M:%S')}_")

    return "\n".join(lines)


# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Reporte diario QuantEdge AI")
    parser.add_argument("--days", type=int, default=int(os.getenv("REPORT_DAYS", "1")),
                        help="Cuántos días analizar (default: 1)")
    parser.add_argument("--no-send", action="store_true",
                        help="Solo imprimir, no enviar a Telegram")
    args = parser.parse_args()

    report = build_daily_report(days=args.days)

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