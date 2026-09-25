"""
=============================================================================
QUANTEDGE AI — ANÁLISIS POR ACTIVO
=============================================================================
Analiza el historial de trades (JSONL) y genera un reporte detallado por
símbolo con recomendaciones automáticas de ajuste.

Uso:
    python analyze_by_symbol.py
    python analyze_by_symbol.py --days 7
    python analyze_by_symbol.py --min-trades 5
    python analyze_by_symbol.py --export report.csv

Salida:
  • Tabla con métricas por activo (trades, WR, PF, PnL, expectancy)
  • Ranking de activos por rentabilidad
  • Recomendaciones automáticas (activar/desactivar/ajustar)
=============================================================================
"""

import os
import sys
import json
import argparse
from collections import defaultdict
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional

LOGS_DIR = os.path.join(os.path.dirname(__file__), "logs")
AUDIT_LOG_FILE = os.path.join(LOGS_DIR, "trade_audit_history.jsonl")

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"


# =============================================================================
# CARGA DE DATOS
# =============================================================================
def load_closures(log_path: str, days: Optional[int] = None) -> List[Dict[str, Any]]:
    """Carga cierres (category='CLOSURE') del JSONL."""
    if not os.path.exists(log_path):
        print(f"{RED}❌ Archivo no encontrado: {log_path}{RESET}")
        return []

    cutoff_ms = 0
    if days:
        cutoff_ms = int((datetime.now(timezone.utc).timestamp() - days * 86400) * 1000)

    closures = []
    with open(log_path, "r", encoding="utf-8") as f:
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
            if cutoff_ms and rec.get("timestamp", 0) < cutoff_ms:
                continue
            closures.append(rec)

    closures.sort(key=lambda r: r.get("timestamp", 0))
    return closures


# =============================================================================
# ESTADÍSTICAS POR SÍMBOLO
# =============================================================================
def compute_symbol_stats(closures: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """Agrupa cierres por símbolo y calcula métricas."""
    by_symbol = defaultdict(lambda: {
        "trades": 0,
        "wins": 0,
        "losses": 0,
        "pnl_total": 0.0,
        "gross_profit": 0.0,
        "gross_loss": 0.0,
        "pnls": [],
        "best": 0.0,
        "worst": 0.0,
        "max_win_streak": 0,
        "max_loss_streak": 0,
        "current_streak": 0,
        "last_streak_type": None,
    })

    for r in closures:
        sym = str(r.get("symbol", "UNKNOWN")).upper()
        pnl = float(r.get("pnl_usd", 0.0))
        d = by_symbol[sym]

        d["trades"] += 1
        d["pnl_total"] += pnl
        d["pnls"].append(pnl)

        if pnl > 0:
            d["wins"] += 1
            d["gross_profit"] += pnl
            if pnl > d["best"]:
                d["best"] = pnl
            # Racha
            if d["last_streak_type"] == "win":
                d["current_streak"] += 1
            else:
                d["current_streak"] = 1
                d["last_streak_type"] = "win"
            d["max_win_streak"] = max(d["max_win_streak"], d["current_streak"])
        else:
            d["losses"] += 1
            d["gross_loss"] += abs(pnl)
            if pnl < d["worst"]:
                d["worst"] = pnl
            if d["last_streak_type"] == "loss":
                d["current_streak"] += 1
            else:
                d["current_streak"] = 1
                d["last_streak_type"] = "loss"
            d["max_loss_streak"] = max(d["max_loss_streak"], d["current_streak"])

    # Calcular métricas derivadas
    for sym, d in by_symbol.items():
        if d["trades"] == 0:
            continue
        d["win_rate_pct"] = round((d["wins"] / d["trades"]) * 100, 2)
        d["profit_factor"] = round(
            (d["gross_profit"] / d["gross_loss"]) if d["gross_loss"] > 0 else 999.0, 2
        )
        d["avg_win"] = round(d["gross_profit"] / d["wins"], 2) if d["wins"] > 0 else 0.0
        d["avg_loss"] = round(d["gross_loss"] / d["losses"], 2) if d["losses"] > 0 else 0.0
        d["expectancy"] = round(
            (d["win_rate_pct"] / 100.0) * d["avg_win"]
            - ((1 - d["win_rate_pct"] / 100.0) * d["avg_loss"]),
            2
        )

    return dict(by_symbol)


# =============================================================================
# RECOMENDACIONES
# =============================================================================
def generate_recommendations(stats: Dict[str, Dict[str, Any]], min_trades: int = 5) -> List[str]:
    """Genera recomendaciones basadas en las estadísticas."""
    recs = []

    # Ordenar por PnL
    sorted_syms = sorted(stats.items(), key=lambda x: x[1]["pnl_total"], reverse=True)

    winners = []
    losers = []
    neutral = []

    for sym, d in sorted_syms:
        if d["trades"] < min_trades:
            continue

        pf = d["profit_factor"]
        wr = d["win_rate_pct"]
        pnl = d["pnl_total"]

        if pf >= 1.5 and wr >= 55:
            winners.append((sym, d))
        elif pf < 1.0 or pnl < -20:
            losers.append((sym, d))
        else:
            neutral.append((sym, d))

    # Recomendaciones para ganadores
    if winners:
        recs.append(f"{GREEN}✅ ACTIVOS RENTABLES (mantener):{RESET}")
        for sym, d in winners:
            recs.append(
                f"   • {BOLD}{sym}{RESET}: PF={d['profit_factor']}, "
                f"WR={d['win_rate_pct']}%, PnL=${d['pnl_total']:.2f}, "
                f"expectancy=${d['expectancy']:.2f}"
            )
        recs.append("")

    # Recomendaciones para perdedores
    if losers:
        recs.append(f"{RED}🔴 ACTIVOS A REVISAR:{RESET}")
        for sym, d in losers:
            recs.append(
                f"   • {BOLD}{sym}{RESET}: PF={d['profit_factor']}, "
                f"WR={d['win_rate_pct']}%, PnL=${d['pnl_total']:.2f}"
            )

            # Sugerencia específica
            if d["profit_factor"] < 0.5:
                recs.append(f"     💡 Sugerencia: DESACTIVAR {sym} (PF crítico)")
            elif d["profit_factor"] < 0.8:
                recs.append(f"     💡 Sugerencia: Ampliar SL en 30-50% o subir confianza mínima para {sym}")
            elif d["win_rate_pct"] < 40:
                recs.append(f"     💡 Sugerencia: Ampliar SL (win rate bajo indica stops muy ajustados)")
            elif d["avg_loss"] > d["avg_win"] * 1.5:
                recs.append(f"     💡 Sugerencia: Reducir TP o aumentar SL (avg loss >> avg win)")
        recs.append("")

    # Neutrales
    if neutral:
        recs.append(f"{YELLOW}⚪ ACTIVOS NEUTRALES (observar):{RESET}")
        for sym, d in neutral:
            recs.append(
                f"   • {BOLD}{sym}{RESET}: PF={d['profit_factor']}, "
                f"WR={d['win_rate_pct']}%, PnL=${d['pnl_total']:.2f} "
                f"({d['trades']} trades)"
            )
        recs.append("")

    # Activos con pocos trades
    low_data = [(sym, d) for sym, d in sorted_syms if d["trades"] < min_trades]
    if low_data:
        recs.append(f"{BLUE}ℹ️  ACTIVOS CON POCOS DATOS (< {min_trades} trades):{RESET}")
        for sym, d in low_data:
            recs.append(
                f"   • {BOLD}{sym}{RESET}: {d['trades']} trades, PnL=${d['pnl_total']:.2f} "
                f"(insuficiente para evaluar)"
            )

    return recs


# =============================================================================
# IMPRESIÓN
# =============================================================================
def print_header(title: str):
    print(f"\n{BOLD}{CYAN}{'═' * 90}{RESET}")
    print(f"{BOLD}{CYAN}  {title}{RESET}")
    print(f"{BOLD}{CYAN}{'═' * 90}{RESET}")


def print_symbol_table(stats: Dict[str, Dict[str, Any]], min_trades: int):
    """Imprime la tabla principal de símbolos."""
    print_header("📊 ANÁLISIS POR ACTIVO")

    if not stats:
        print(f"  {YELLOW}Sin datos de cierres disponibles.{RESET}")
        return

    # Encabezado
    header = (
        f"  {'SÍMBOLO':<10} {'TRADES':>7} {'WR%':>7} {'PF':>6} "
        f"{'PnL':>12} {'EXPECT':>10} {'MAX DD':>10} {'RACHA':>10}"
    )
    print(header)
    print(f"  {'-' * 86}")

    # Ordenar por PnL descendente
    sorted_syms = sorted(stats.items(), key=lambda x: x[1]["pnl_total"], reverse=True)

    for sym, d in sorted_syms:
        if d["trades"] == 0:
            continue

        pnl_color = GREEN if d["pnl_total"] >= 0 else RED
        wr_color = GREEN if d["win_rate_pct"] >= 50 else (YELLOW if d["win_rate_pct"] >= 40 else RED)
        pf_color = GREEN if d["profit_factor"] >= 1.5 else (YELLOW if d["profit_factor"] >= 1.0 else RED)

        warning = ""
        if d["trades"] < min_trades:
            warning = f" {BLUE}(pocos datos){RESET}"

        racha_str = f"{d['max_win_streak']}W/{d['max_loss_streak']}L"

        print(
            f"  {BOLD}{sym:<10}{RESET} "
            f"{d['trades']:>7} "
            f"{wr_color}{d['win_rate_pct']:>6.1f}%{RESET} "
            f"{pf_color}{d['profit_factor']:>6.2f}{RESET} "
            f"{pnl_color}${d['pnl_total']:>10,.2f}{RESET} "
            f"${d['expectancy']:>8,.2f} "
            f"{d['worst']:>10,.2f} "
            f"{racha_str:>10}{warning}"
        )


def print_ranking(stats: Dict[str, Dict[str, Any]]):
    """Imprime ranking visual por PnL."""
    print_header("🏆 RANKING POR RENTABILIDAD")

    if not stats:
        return

    sorted_syms = sorted(stats.items(), key=lambda x: x[1]["pnl_total"], reverse=True)
    max_abs_pnl = max(abs(d["pnl_total"]) for _, d in sorted_syms) or 1.0

    for i, (sym, d) in enumerate(sorted_syms, 1):
        if d["trades"] == 0:
            continue

        bar_len = int((abs(d["pnl_total"]) / max_abs_pnl) * 40)
        bar = "█" * bar_len

        if d["pnl_total"] >= 0:
            color = GREEN
            sign = "+"
        else:
            color = RED
            sign = ""

        medal = "🥇" if i == 1 else ("🥈" if i == 2 else ("🥉" if i == 3 else "  "))

        print(f"  {medal} {BOLD}{sym:<10}{RESET} {color}{bar} {sign}${d['pnl_total']:,.2f}{RESET}")


def print_recommendations(recs: List[str]):
    print_header("💡 RECOMENDACIONES AUTOMÁTICAS")
    if not recs:
        print(f"  {YELLOW}Sin datos suficientes para generar recomendaciones.{RESET}")
        return
    for line in recs:
        print(f"  {line}")


def export_csv(stats: Dict[str, Dict[str, Any]], path: str):
    """Exporta las estadísticas a CSV."""
    import csv

    fields = [
        "symbol", "trades", "wins", "losses", "win_rate_pct",
        "profit_factor", "pnl_total", "expectancy",
        "avg_win", "avg_loss", "best", "worst",
        "max_win_streak", "max_loss_streak",
    ]

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for sym, d in sorted(stats.items(), key=lambda x: x[1]["pnl_total"], reverse=True):
            row = {"symbol": sym, **{k: d.get(k, 0) for k in fields if k != "symbol"}}
            writer.writerow(row)

    print(f"\n{GREEN}✅ Reporte exportado: {path}{RESET}")


# =============================================================================
# MAIN
# =============================================================================
def main():
    parser = argparse.ArgumentParser(description="Análisis de performance por activo")
    parser.add_argument("--days", type=int, default=None,
                        help="Filtrar últimos N días (default: todos)")
    parser.add_argument("--min-trades", type=int, default=5,
                        help="Mínimo de trades para evaluar un activo (default: 5)")
    parser.add_argument("--log", type=str, default=AUDIT_LOG_FILE,
                        help="Ruta del JSONL")
    parser.add_argument("--export", type=str, default=None,
                        help="Exportar a CSV")
    args = parser.parse_args()

    # Cargar datos
    print(f"\n{BOLD}{CYAN}🎯 QUANTEDGE AI — ANÁLISIS POR ACTIVO{RESET}")
    print(f"  Archivo:       {args.log}")
    print(f"  Días:          {args.days if args.days else 'Todos'}")
    print(f"  Mín. trades:   {args.min_trades}")

    closures = load_closures(args.log, days=args.days)

    if not closures:
        print(f"\n{YELLOW}⚠️  No hay cierres registrados con los filtros aplicados.{RESET}")
        sys.exit(0)

    print(f"  Cierres:       {len(closures)}")

    # Calcular estadísticas
    stats = compute_symbol_stats(closures)

    # Imprimir reportes
    print_symbol_table(stats, args.min_trades)
    print_ranking(stats)
    recs = generate_recommendations(stats, min_trades=args.min_trades)
    print_recommendations(recs)

    # Exportar
    if args.export:
        export_csv(stats, args.export)

    print(f"\n{CYAN}{'═' * 90}{RESET}\n")


if __name__ == "__main__":
    main()