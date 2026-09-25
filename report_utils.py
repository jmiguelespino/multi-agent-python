"""
=============================================================================
QUANTEDGE AI — UTILIDADES DE REPORTES (unificación B12)
=============================================================================
🔧 v1.0.0 — LOTE FUSIONADO 2.6+3:
  • 🐛 B12 CORREGIDO: elimina la duplicación de build_daily_report()
    entre main.py y daily_report.py.
  • Ambas partes ahora importan de aquí.
  • Incluye _generate_recommendations() que antes solo estaba en main.py.
=============================================================================
"""
import os
import json
import time
import logging
from pathlib import Path
from datetime import datetime, timezone, timedelta
from collections import defaultdict
from typing import List, Dict, Any, Optional

logger = logging.getLogger("ReportUtils")
logger.propagate = False

TZ_MT5 = timezone(timedelta(hours=3))

BASE_DIR = Path(__file__).resolve().parent
AUDIT_LOG_FILE = BASE_DIR / "logs" / "trade_audit_history.jsonl"
CONTROL_STATE_FILE = BASE_DIR / "control_state.json"
CONFIG_OPTIMIZED_FILE = BASE_DIR / "config_optimized.json"


# =============================================================================
# CARGA DE DATOS
# =============================================================================
def load_closures_since(cutoff_ms: int, include_tests: bool = False) -> List[dict]:
    """Carga cierres desde un timestamp en ms."""
    if not AUDIT_LOG_FILE.exists():
        return []

    closures = []
    try:
        with open(AUDIT_LOG_FILE, "r", encoding="utf-8") as f:
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
                if not include_tests and rec.get("is_test") is True:
                    continue
                closures.append(rec)
    except Exception as e:
        logger.error(f"Error cargando cierres: {e}")

    closures.sort(key=lambda r: r.get("timestamp", 0))
    return closures


def load_all_closures(include_tests: bool = False) -> List[dict]:
    """Carga TODOS los cierres (para progreso del learner)."""
    if not AUDIT_LOG_FILE.exists():
        return []
    closures = []
    try:
        with open(AUDIT_LOG_FILE, "r", encoding="utf-8") as f:
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
                if not include_tests and rec.get("is_test") is True:
                    continue
                closures.append(rec)
    except Exception:
        pass
    return closures


def count_events_since(cutoff_ms: int) -> dict:
    """Cuenta ORDER_FILLED, OPEN_POSITION_DETECTED y REJECTION desde cutoff."""
    result = {"orders_filled": 0, "positions_opened": 0, "rejections": 0}
    if not AUDIT_LOG_FILE.exists():
        return result

    try:
        with open(AUDIT_LOG_FILE, "r", encoding="utf-8") as f:
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
        acc = mt5.account_info()
        positions = mt5.positions_get() or []
        if acc is None:
            return {}
        return {
            "balance": round(acc.balance, 2),
            "equity": round(acc.equity, 2),
            "margin_free": round(acc.margin_free, 2),
            "positions_count": len(positions),
            "floating_pnl": round(sum(p.profit for p in positions), 2),
        }
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


# =============================================================================
# FORMATEO
# =============================================================================
def format_pnl(value: float) -> str:
    emoji = "🟢" if value > 0 else ("🔴" if value < 0 else "⚪")
    return f"{emoji} `${value:+,.2f}`"


def generate_recommendations(by_symbol_data: dict) -> list:
    recs = []
    MIN_TRADES_TO_EVALUATE = int(os.getenv("ANALYSIS_MIN_TRADES", "5"))

    for sym, d in by_symbol_data.items():
        if d["count"] < MIN_TRADES_TO_EVALUATE:
            continue

        wr = (d["wins"] / d["count"]) * 100 if d["count"] > 0 else 0
        sym_pf = (d["gross_profit"] / d["gross_loss"]) if d["gross_loss"] > 0 else 999.0

        if sym_pf < 0.5:
            recs.append(f"🔴 *{sym}*: PF={sym_pf:.2f} MUY BAJO. Considerar deshabilitar.")
        elif sym_pf < 0.7:
            recs.append(f"🔴 *{sym}*: PF={sym_pf:.2f} muy bajo. Revisar parámetros.")
        elif sym_pf < 1.0:
            recs.append(f"🟡 *{sym}*: PF={sym_pf:.2f}. Revisar parámetros.")
        elif sym_pf > 2.0:
            recs.append(f"🟢 *{sym}*: PF={sym_pf:.2f} excelente. Mantener configuración.")

        if wr < 40 and d["count"] >= MIN_TRADES_TO_EVALUATE:
            recs.append(f"⚠️ *{sym}*: win rate {wr:.0f}% bajo. Ampliar SL o aumentar confianza mínima.")

    return recs[:5]


# =============================================================================
# REPORTE PRINCIPAL
# =============================================================================
def build_daily_report(days: int = 1, include_tests: bool = False) -> str:
    """Construye el mensaje de reporte diario."""
    now_ms = int(time.time() * 1000)
    cutoff_ms = now_ms - (days * 86400 * 1000)

    closures = load_closures_since(cutoff_ms, include_tests=include_tests)
    all_closures = load_all_closures(include_tests=include_tests)
    orders = count_events_since(cutoff_ms)
    mt5_snap = get_mt5_snapshot()
    ctrl = read_control_state()
    config = read_config_optimized()

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

    by_symbol_data = defaultdict(lambda: {
        "count": 0, "wins": 0, "losses": 0,
        "pnl": 0.0, "gross_profit": 0.0, "gross_loss": 0.0,
    })
    for r in closures:
        sym = str(r.get("symbol", "UNKNOWN")).upper()
        pnl = float(r.get("pnl_usd", 0))
        by_symbol_data[sym]["count"] += 1
        by_symbol_data[sym]["pnl"] += pnl
        if pnl > 0:
            by_symbol_data[sym]["wins"] += 1
            by_symbol_data[sym]["gross_profit"] += pnl
        else:
            by_symbol_data[sym]["losses"] += 1
            by_symbol_data[sym]["gross_loss"] += abs(pnl)

    day_label = "HOY" if days == 1 else f"ÚLTIMOS {days} DÍAS"
    date_str = datetime.now(TZ_MT5).strftime("%Y-%m-%d")

    lines = [
        "📊 *QUANTEDGE AI — REPORTE DIARIO*",
        f"_{date_str} ({day_label})_",
        "",
    ]

    paused = ctrl.get("paused", False)
    bot_status = "⏸️ PAUSADO" if paused else "▶️ ACTIVO"
    lines.append(f"*Estado del bot:* {bot_status}")

    if mt5_snap:
        lines.append(f"*MT5:*")
        lines.append(f"  • Balance: `${mt5_snap['balance']:,.2f}`")
        lines.append(f"  • Equidad: `${mt5_snap['equity']:,.2f}`")
        lines.append(f"  • Posiciones abiertas: `{mt5_snap['positions_count']}`")
        if mt5_snap['positions_count'] > 0:
            lines.append(f"  • PnL flotante: {format_pnl(mt5_snap['floating_pnl'])}")

    lines.append("")
    lines.append(f"*Actividad:*")
    lines.append(f"  • Órdenes ejecutadas: `{orders['orders_filled']}`")
    lines.append(f"  • Posiciones cerradas: `{total}`")
    lines.append(f"  • Rechazos: `{orders['rejections']}`")

    lines.append("")
    if total > 0:
        lines.append(f"*Resultados globales:*")
        lines.append(f"  • PnL: {format_pnl(total_pnl)}")
        lines.append(f"  • Wins / Losses: `{len(wins)}` / `{len(losses)}`")
        lines.append(f"  • Win rate: `{win_rate:.1f}%`")
        lines.append(f"  • Profit Factor: `{pf:.2f}`")
        lines.append(f"  • Avg Win: `${avg_win:,.2f}` | Avg Loss: `${avg_loss:,.2f}`")
        lines.append(f"  • Mejor / Peor: `+${best:,.2f}` / `${worst:,.2f}`")
    else:
        lines.append(f"*Resultados:* _sin trades cerrados en el período_")

    if by_symbol_data:
        lines.append("")
        lines.append(f"*📈 Desglose por activo:*")
        lines.append("")

        sorted_symbols = sorted(
            by_symbol_data.items(),
            key=lambda x: x[1]["pnl"],
            reverse=True
        )

        for sym, d in sorted_symbols:
            if d["count"] == 0:
                continue

            wr = (d["wins"] / d["count"]) * 100 if d["count"] > 0 else 0
            sym_pf = (d["gross_profit"] / d["gross_loss"]) if d["gross_loss"] > 0 else 999.0

            if d["pnl"] > 0:
                emoji = "🟢"
            elif d["pnl"] < 0:
                emoji = "🔴"
            else:
                emoji = "⚪"

            warning = ""
            if d["count"] >= 5 and d["pnl"] < -20:
                warning = " ⚠️"
            elif d["count"] >= 5 and sym_pf < 0.8:
                warning = " ⚠️"

            lines.append(
                f"{emoji} *{sym}*{warning}\n"
                f"    `{d['count']}` trades | WR `{wr:.0f}%` | PF `{sym_pf:.2f}` | PnL {format_pnl(d['pnl'])}"
            )

    lines.append("")
    lines.append(f"*🧠 Agente 5 (Learner):*")
    lines.append(f"  • Cierres totales: `{len(all_closures)}` / `30`")
    if config:
        lines.append(f"  • Confianza: `{config.get('min_confidence_threshold', 'N/D')}%`")
        lines.append(f"  • SL ATR: `{config.get('atr_stop_multiplier', 'N/D')}×`")
        lines.append(f"  • TP ATR: `{config.get('atr_profit_multiplier', 'N/D')}×`")
        if config.get("disabled_symbols"):
            lines.append(f"  • ⛔ Deshabilitados: `{', '.join(config['disabled_symbols'])}`")

    if total >= 5:
        recs = generate_recommendations(by_symbol_data)
        if recs:
            lines.append("")
            lines.append(f"*💡 Recomendaciones:*")
            for rec in recs:
                lines.append(f"  {rec}")

    lines.append("")
    lines.append(f"_Generado a las {datetime.now(TZ_MT5).strftime('%H:%M:%S')}_")

    return "\n".join(lines)