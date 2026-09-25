"""
=============================================================================
RUNNER DE BACKTEST — QuantEdge AI v2
=============================================================================
🔧 v2: soporta filtro de fechas (start_date / end_date en config) y M15.
=============================================================================
"""
import os
import json
import time
import argparse
from collections import defaultdict

from backtest_engine import run_backtest, BacktestStats, Position


def format_pf(pf):
    if pf >= 2.0: return f"🟢 {pf:.2f}"
    if pf >= 1.2: return f"🟡 {pf:.2f}"
    if pf >= 1.0: return f"⚪ {pf:.2f}"
    return f"🔴 {pf:.2f}"


def format_pnl(v):
    emoji = "🟢" if v > 0 else ("🔴" if v < 0 else "⚪")
    return f"{emoji} ${v:+,.2f}"


def print_stats(stats, trades, start_date, end_date):
    print(f"\n{'=' * 78}")
    print(f"  RESULTADOS — Versión: {stats.version.upper()}")
    print(f"  Período: {start_date or 'inicio'} → {end_date or 'fin'}")
    print(f"{'=' * 78}")
    print(f"  Total trades:       {stats.total_trades}")
    print(f"  Wins / Losses / BE: {stats.wins} / {stats.losses} / {stats.breakeven}")
    print(f"  Win Rate:           {stats.win_rate_pct:.2f}%")
    print(f"  Profit Factor:      {format_pf(stats.profit_factor)}")
    print(f"  PnL total:          {format_pnl(stats.total_pnl)}")
    print(f"  Avg Win / Loss:     ${stats.avg_win:,.2f} / ${stats.avg_loss:,.2f}")
    print(f"  Max Drawdown:       ${stats.max_dd:,.2f} ({stats.max_dd_pct:.2f}%)")

    if stats.rejected_by_risk:
        print(f"\n  🚫 Rechazos por RiskGuardian:")
        for reason, count in sorted(stats.rejected_by_risk.items(), key=lambda x: -x[1]):
            print(f"    {reason:25s}: {count}")

    by_sym = defaultdict(lambda: {"trades": 0, "wins": 0, "losses": 0, "pnl": 0.0, "gp": 0.0, "gl": 0.0})
    for t in trades:
        s = by_sym[t.symbol]
        s["trades"] += 1
        s["pnl"] += t.pnl_usd
        if t.pnl_usd > 0:
            s["wins"] += 1; s["gp"] += t.pnl_usd
        elif t.pnl_usd < 0:
            s["losses"] += 1; s["gl"] += abs(t.pnl_usd)

    print(f"\n  📊 Desglose por símbolo:")
    for sym, d in sorted(by_sym.items(), key=lambda x: x[1]["pnl"], reverse=True):
        wr = (d["wins"] / d["trades"] * 100) if d["trades"] > 0 else 0
        pf = (d["gp"] / d["gl"]) if d["gl"] > 0 else (999 if d["gp"] > 0 else 0)
        print(f"    {sym:8s} | {d['trades']:>4} trades | WR {wr:>5.1f}% | PF {format_pf(pf)} | PnL {format_pnl(d['pnl'])}")

    print(f"\n  📈 Razones de cierre:")
    by_reason = defaultdict(int)
    for t in trades:
        by_reason[t.exit_reason or "UNKNOWN"] += 1
    for reason, count in sorted(by_reason.items(), key=lambda x: -x[1]):
        print(f"    {reason:15s}: {count}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--version", type=str)
    parser.add_argument("--export", action="store_true")
    args = parser.parse_args()

    with open("backtest_config.json", "r", encoding="utf-8") as f:
        cfg = json.load(f)

    datasets_dir = cfg.get("datasets_dir", "datasets")
    initial_capital = cfg.get("initial_capital", 1750.0)
    start_date = cfg.get("start_date")
    end_date = cfg.get("end_date")

    if args.version:
        versions_to_run = [args.version]
    elif args.all:
        versions_to_run = list(cfg["versions"].keys())
    else:
        versions_to_run = ["fixes"]

    all_results = {}

    for v_name in versions_to_run:
        if v_name not in cfg["versions"]:
            print(f"❌ Versión '{v_name}' no encontrada")
            continue

        v_cfg = dict(cfg["versions"][v_name])
        v_cfg["symbols"] = cfg["symbols"]

        print(f"\n{'=' * 78}")
        print(f"  ▶️  Ejecutando: {v_name.upper()}")
        print(f"  Período: {start_date or 'inicio'} → {end_date or 'fin'}")
        print(f"{'=' * 78}")

        t0 = time.time()
        stats, trades = run_backtest(v_name, v_cfg, datasets_dir, initial_capital, start_date, end_date)
        elapsed = time.time() - t0

        print_stats(stats, trades, start_date, end_date)
        print(f"\n  ⏱️  Tiempo: {elapsed:.1f}s")

        all_results[v_name] = (stats, trades)

        if args.export:
            out_file = f"backtest_trades_{v_name}.csv"
            with open(out_file, "w", encoding="utf-8") as f:
                f.write("symbol,side,volume,entry_price,entry_time,exit_price,exit_time,reason,pnl_usd,pnl_pct\n")
                for t in trades:
                    f.write(f"{t.symbol},{t.side},{t.volume},{t.entry_price},{t.entry_time_ms},"
                            f"{t.exit_price},{t.exit_time_ms},{t.exit_reason},{t.pnl_usd},{t.pnl_pct}\n")
            print(f"  💾 Exportado a {out_file}")

    if len(all_results) > 1:
        print(f"\n{'=' * 78}")
        print(f"  🏆 COMPARACIÓN")
        print(f"  Período: {start_date or 'inicio'} → {end_date or 'fin'}")
        print(f"{'=' * 78}")
        print(f"  {'Versión':<10} {'Trades':>7} {'WR':>7} {'PF':>7} {'PnL':>12} {'MaxDD':>10}")
        print(f"  {'-' * 65}")
        for v_name, (stats, _) in all_results.items():
            print(f"  {v_name:<10} {stats.total_trades:>7} {stats.win_rate_pct:>6.1f}% "
                  f"{stats.profit_factor:>7.2f} {stats.total_pnl:>+11.2f} {stats.max_dd:>9.2f}")


if __name__ == "__main__":
    main()