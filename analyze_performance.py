"""
=============================================================================
QUANTEDGE AI — ANALIZADOR DE PERFORMANCE v1.1
=============================================================================
🔧 v1.1:
  • Max DD % ahora se calcula sobre el capital base (no sobre el peak del PnL).
  • Si se pasa --capital-base, se usa ese valor para el % de drawdown.
  • Por defecto asume $1500 (o lo lee de .env CAPITAL_BASE_USD).
=============================================================================
"""

import os
import sys
import json
import math
import argparse
from collections import defaultdict
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional

LOGS_DIR = os.path.join(os.path.dirname(__file__), "logs")
AUDIT_LOG_FILE = os.path.join(LOGS_DIR, "trade_audit_history.jsonl")

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"


def load_env_capital_base() -> float:
    """Lee CAPITAL_BASE_USD del .env si existe."""
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    if not os.path.exists(env_path):
        return 1500.0
    try:
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("CAPITAL_BASE_USD="):
                    return float(line.split("=", 1)[1].strip())
    except Exception:
        pass
    return 1500.0


def load_closures(log_path: str, days: Optional[int] = None, symbol_filter: Optional[str] = None) -> List[Dict[str, Any]]:
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
            if symbol_filter and symbol_filter.upper() not in str(rec.get("symbol", "")).upper():
                continue
            closures.append(rec)

    closures.sort(key=lambda r: r.get("timestamp", 0))
    return closures


def compute_basic_stats(closures: List[Dict[str, Any]]) -> Dict[str, Any]:
    pnls = [float(r.get("pnl_usd", 0.0)) for r in closures]
    total = len(pnls)
    if total == 0:
        return {}

    wins = [p for p in pnls if p > 0]
    losses = [p for p in pnls if p <= 0]

    total_pnl = sum(pnls)
    gross_profit = sum(wins)
    gross_loss = abs(sum(losses))

    win_rate = (len(wins) / total) * 100.0
    avg_win = (gross_profit / len(wins)) if wins else 0.0
    avg_loss = (gross_loss / len(losses)) if losses else 0.0
    profit_factor = (gross_profit / gross_loss) if gross_loss > 0 else 999.0

    expectancy = (win_rate / 100.0) * avg_win - ((1 - win_rate / 100.0) * avg_loss)

    return {
        "total_trades": total,
        "wins": len(wins),
        "losses": len(losses),
        "win_rate_pct": round(win_rate, 2),
        "total_pnl": round(total_pnl, 2),
        "gross_profit": round(gross_profit, 2),
        "gross_loss": round(gross_loss, 2),
        "profit_factor": round(profit_factor, 2),
        "avg_win": round(avg_win, 2),
        "avg_loss": round(avg_loss, 2),
        "expectancy": round(expectancy, 2),
        "best_trade": round(max(pnls), 2),
        "worst_trade": round(min(pnls), 2),
    }


def compute_sharpe(pnls: List[float], periods_per_year: int = 252) -> float:
    if len(pnls) < 2:
        return 0.0
    mean = sum(pnls) / len(pnls)
    variance = sum((p - mean) ** 2 for p in pnls) / (len(pnls) - 1)
    std = math.sqrt(variance)
    if std == 0:
        return 0.0
    return (mean / std) * math.sqrt(periods_per_year)


def compute_sortino(pnls: List[float], periods_per_year: int = 252) -> float:
    if len(pnls) < 2:
        return 0.0
    mean = sum(pnls) / len(pnls)
    downside = [p for p in pnls if p < 0]
    if not downside:
        return 999.0
    downside_mean_sq = sum(p ** 2 for p in downside) / len(pnls)
    downside_dev = math.sqrt(downside_mean_sq)
    if downside_dev == 0:
        return 0.0
    return (mean / downside_dev) * math.sqrt(periods_per_year)


def compute_max_drawdown(equity_curve: List[float], capital_base: float) -> Dict[str, float]:
    """
    🔧 FIX: el % se calcula sobre el capital base (o el peak real de la cuenta),
    no sobre el peak del PnL acumulado (que puede ser ~0 al inicio).
    """
    if not equity_curve:
        return {"max_dd_usd": 0.0, "max_dd_pct": 0.0, "peak": 0.0, "trough": 0.0}

    peak = equity_curve[0]
    max_dd_usd = 0.0
    peak_val = equity_curve[0]
    trough_val = equity_curve[0]

    for value in equity_curve:
        if value > peak:
            peak = value
        dd_usd = peak - value
        if dd_usd > max_dd_usd:
            max_dd_usd = dd_usd
            peak_val = peak
            trough_val = value

    # 🔧 % sobre el capital base (equity inicial real)
    ref_capital = max(capital_base, capital_base + peak_val, 1.0)
    max_dd_pct = (max_dd_usd / ref_capital) * 100.0 if ref_capital > 0 else 0.0

    return {
        "max_dd_usd": round(max_dd_usd, 2),
        "max_dd_pct": round(max_dd_pct, 2),
        "peak": round(peak_val, 2),
        "trough": round(trough_val, 2),
    }


def compute_streaks(pnls: List[float]) -> Dict[str, int]:
    max_wins = max_losses = 0
    cur_wins = cur_losses = 0
    for p in pnls:
        if p > 0:
            cur_wins += 1
            cur_losses = 0
            max_wins = max(max_wins, cur_wins)
        else:
            cur_losses += 1
            cur_wins = 0
            max_losses = max(max_losses, cur_losses)
    return {"max_win_streak": max_wins, "max_loss_streak": max_losses}


def group_by_symbol(closures: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    groups = defaultdict(list)
    for r in closures:
        sym = str(r.get("symbol", "UNKNOWN")).upper()
        groups[sym].append(r)
    return dict(groups)


def group_by_hour(closures: List[Dict[str, Any]]) -> Dict[int, float]:
    hourly = defaultdict(float)
    for r in closures:
        ts = r.get("timestamp", 0) / 1000.0
        try:
            hour = datetime.fromtimestamp(ts, tz=timezone.utc).hour
        except Exception:
            continue
        hourly[hour] += float(r.get("pnl_usd", 0.0))
    return dict(sorted(hourly.items()))


def print_header(title: str):
    print(f"\n{BOLD}{CYAN}{'═' * 70}{RESET}")
    print(f"{BOLD}{CYAN}  {title}{RESET}")
    print(f"{BOLD}{CYAN}{'═' * 70}{RESET}")


def print_basic_report(stats: Dict[str, Any]):
    print_header("📊 RESUMEN GLOBAL")
    print(f"  Total trades:      {BOLD}{stats['total_trades']}{RESET}")
    print(f"  Wins / Losses:     {GREEN}{stats['wins']}{RESET} / {RED}{stats['losses']}{RESET}")
    print(f"  Win rate:          {BOLD}{stats['win_rate_pct']}%{RESET}")
    print(f"  Total PnL:         {GREEN if stats['total_pnl'] >= 0 else RED}${stats['total_pnl']:,.2f}{RESET}")
    print(f"  Gross profit:      {GREEN}${stats['gross_profit']:,.2f}{RESET}")
    print(f"  Gross loss:        {RED}${stats['gross_loss']:,.2f}{RESET}")
    print(f"  Profit Factor:     {BOLD}{stats['profit_factor']}{RESET}")
    print(f"  Avg Win:           ${stats['avg_win']:,.2f}")
    print(f"  Avg Loss:          ${stats['avg_loss']:,.2f}")
    print(f"  Expectancy:        ${stats['expectancy']:,.2f} por trade")
    print(f"  Best trade:        {GREEN}${stats['best_trade']:,.2f}{RESET}")
    print(f"  Worst trade:       {RED}${stats['worst_trade']:,.2f}{RESET}")


def print_risk_report(sharpe: float, sortino: float, dd: Dict[str, float], streaks: Dict[str, int], capital_base: float):
    print_header("⚖️  MÉTRICAS DE RIESGO")
    print(f"  Capital base:      ${capital_base:,.2f}")
    print(f"  Sharpe Ratio:      {BOLD}{sharpe:.2f}{RESET}")
    print(f"  Sortino Ratio:     {BOLD}{sortino:.2f}{RESET}")
    print(f"  Max Drawdown:      {RED}${dd['max_dd_usd']:,.2f} ({dd['max_dd_pct']:.2f}%){RESET}")
    print(f"  Peak → Trough:     ${dd['peak']:,.2f} → ${dd['trough']:,.2f}")
    print(f"  Max win streak:    {GREEN}{streaks['max_win_streak']}{RESET}")
    print(f"  Max loss streak:   {RED}{streaks['max_loss_streak']}{RESET}")


def print_symbol_report(groups: Dict[str, List[Dict[str, Any]]]):
    print_header("💼 DESGLOSE POR ACTIVO")
    rows = []
    for sym, items in groups.items():
        stats = compute_basic_stats(items)
        if stats:
            rows.append((sym, stats))
    rows.sort(key=lambda x: x[1]["total_pnl"], reverse=True)

    print(f"  {'SÍMBOLO':<12} {'TRADES':>7} {'WIN%':>7} {'PF':>6} {'PnL':>12} {'EXPECT':>10}")
    print(f"  {'-' * 60}")
    for sym, stats in rows:
        pnl_color = GREEN if stats["total_pnl"] >= 0 else RED
        print(
            f"  {sym:<12} {stats['total_trades']:>7} "
            f"{stats['win_rate_pct']:>6.1f}% "
            f"{stats['profit_factor']:>6.2f} "
            f"{pnl_color}${stats['total_pnl']:>10,.2f}{RESET} "
            f"${stats['expectancy']:>8,.2f}"
        )


def print_hourly_report(hourly: Dict[int, float]):
    print_header("🕐 PnL POR HORA (UTC)")
    if not hourly:
        print("  (sin datos)")
        return
    max_abs = max(abs(v) for v in hourly.values()) or 1.0
    for hour, pnl in hourly.items():
        bar_len = int((abs(pnl) / max_abs) * 30)
        color = GREEN if pnl >= 0 else RED
        bar = "█" * bar_len
        print(f"  {hour:02d}:00  {color}{bar} ${pnl:,.2f}{RESET}")


def export_csv(closures: List[Dict[str, Any]], path: str):
    import csv
    fields = ["timestamp", "iso_time", "symbol", "side", "volume", "price",
              "pnl_usd", "pnl_percent", "ticket", "event_type", "reason"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for r in closures:
            writer.writerow(r)
    print(f"\n{GREEN}✅ Reporte exportado: {path}{RESET}")


def main():
    parser = argparse.ArgumentParser(description="Analizador de performance QuantEdge AI")
    parser.add_argument("--days", type=int, default=None, help="Filtrar últimos N días")
    parser.add_argument("--symbol", type=str, default=None, help="Filtrar por símbolo")
    parser.add_argument("--log", type=str, default=AUDIT_LOG_FILE, help="Ruta del JSONL")
    parser.add_argument("--export", type=str, default=None, help="Exportar CSV")
    parser.add_argument("--capital-base", type=float, default=None,
                        help="Capital base para el %% de Drawdown (default: lee .env)")
    args = parser.parse_args()

    capital_base = args.capital_base if args.capital_base else load_env_capital_base()

    closures = load_closures(args.log, days=args.days, symbol_filter=args.symbol)

    if not closures:
        print(f"{YELLOW}⚠️  No hay cierres registrados con los filtros aplicados.{RESET}")
        print(f"   Archivo: {args.log}")
        sys.exit(0)

    pnls = [float(r.get("pnl_usd", 0.0)) for r in closures]
    equity_curve = []
    running = 0.0
    for p in pnls:
        running += p
        equity_curve.append(running)

    stats = compute_basic_stats(closures)
    sharpe = compute_sharpe(pnls)
    sortino = compute_sortino(pnls)
    dd = compute_max_drawdown(equity_curve, capital_base)
    streaks = compute_streaks(pnls)

    print_header("🎯 QUANTEDGE AI — ANÁLISIS DE PERFORMANCE")
    print(f"  Archivo:           {args.log}")
    print(f"  Cierres cargados:  {len(closures)}")
    if args.days:
        print(f"  Ventana:           Últimos {args.days} días")
    if args.symbol:
        print(f"  Filtro símbolo:    {args.symbol}")

    print_basic_report(stats)
    print_risk_report(sharpe, sortino, dd, streaks, capital_base)
    print_symbol_report(group_by_symbol(closures))
    print_hourly_report(group_by_hour(closures))

    if args.export:
        export_csv(closures, args.export)

    print(f"\n{CYAN}{'═' * 70}{RESET}\n")


if __name__ == "__main__":
    main()