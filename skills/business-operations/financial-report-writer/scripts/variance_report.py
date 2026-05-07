#!/usr/bin/env python3
"""
Generate budget variance analysis with flagging for material variances.

Usage:
    python variance_report.py --period 2026-03 --threshold 10
    python variance_report.py --period 2026-03 --threshold 5 --format json
"""

import argparse
import json
from datetime import datetime

# Sample budget vs actual data
SAMPLE_DATA = {
    "2026-03": {
        "period": "March 2026",
        "categories": [
            {"name": "Product Revenue", "type": "revenue", "budget": 290000, "actual": 310000},
            {"name": "Service Revenue", "type": "revenue", "budget": 115000, "actual": 102000},
            {"name": "Other Revenue", "type": "revenue", "budget": 5000, "actual": 6500},
            {"name": "Direct Costs", "type": "expense", "budget": 62000, "actual": 67000},
            {"name": "Hosting / Infra", "type": "expense", "budget": 13000, "actual": 16200},
            {"name": "Salaries & Benefits", "type": "expense", "budget": 158000, "actual": 156500},
            {"name": "Sales & Marketing", "type": "expense", "budget": 38000, "actual": 45200},
            {"name": "R&D / Engineering", "type": "expense", "budget": 33000, "actual": 31000},
            {"name": "General & Admin", "type": "expense", "budget": 20000, "actual": 22800},
            {"name": "Travel & Meals", "type": "expense", "budget": 5000, "actual": 2100},
            {"name": "Software Licenses", "type": "expense", "budget": 8000, "actual": 8400},
            {"name": "Professional Fees", "type": "expense", "budget": 12000, "actual": 9500},
        ],
    },
}


def analyze_variance(categories, threshold):
    """Analyze variances and flag items above threshold."""
    results = []
    for cat in categories:
        budget = cat["budget"]
        actual = cat["actual"]
        variance = actual - budget
        variance_pct = (variance / budget * 100) if budget else 0

        # Determine if favorable
        if cat["type"] == "revenue":
            favorable = variance >= 0
        else:
            favorable = variance <= 0

        status = "on_track"
        if abs(variance_pct) > threshold * 1.5:
            status = "alert"
        elif abs(variance_pct) > threshold:
            status = "over" if not favorable else "under_budget"

        results.append({
            "name": cat["name"],
            "type": cat["type"],
            "budget": budget,
            "actual": actual,
            "variance": variance,
            "variance_pct": round(variance_pct, 1),
            "favorable": favorable,
            "status": status,
            "flagged": abs(variance_pct) > threshold,
        })
    return results


def print_variance_report(results, period_label, threshold):
    """Print formatted variance report."""
    status_icons = {"on_track": "OK", "over": "WARN", "under_budget": "OK", "alert": "ALERT"}

    print("=" * 85)
    print(f"  BUDGET VARIANCE REPORT")
    print(f"  Period: {period_label}")
    print(f"  Threshold: {threshold}%")
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d')}")
    print("=" * 85)

    # Revenue section
    rev_items = [r for r in results if r["type"] == "revenue"]
    exp_items = [r for r in results if r["type"] == "expense"]

    print(f"\n  {'Category':<24} {'Budget':>12} {'Actual':>12} {'Variance':>12} {'Var %':>8} {'Status':>8}")
    print(f"  {'─'*24} {'─'*12} {'─'*12} {'─'*12} {'─'*8} {'─'*8}")

    print("  REVENUE")
    total_rev_budget = 0
    total_rev_actual = 0
    for item in rev_items:
        flag = " *" if item["flagged"] else ""
        var_str = f"${item['variance']:+,.0f}"
        print(f"    {item['name']:<22} ${item['budget']:>11,.0f} ${item['actual']:>11,.0f} {var_str:>12} {item['variance_pct']:>+7.1f}% {status_icons[item['status']]:>6}{flag}")
        total_rev_budget += item["budget"]
        total_rev_actual += item["actual"]

    print(f"  {'─'*24} {'─'*12} {'─'*12} {'─'*12}")
    rev_var = total_rev_actual - total_rev_budget
    rev_var_pct = (rev_var / total_rev_budget * 100) if total_rev_budget else 0
    print(f"    {'TOTAL REVENUE':<22} ${total_rev_budget:>11,.0f} ${total_rev_actual:>11,.0f} ${rev_var:>+11,.0f} {rev_var_pct:>+7.1f}%")

    print("\n  EXPENSES")
    total_exp_budget = 0
    total_exp_actual = 0
    for item in exp_items:
        flag = " *" if item["flagged"] else ""
        var_str = f"${item['variance']:+,.0f}"
        print(f"    {item['name']:<22} ${item['budget']:>11,.0f} ${item['actual']:>11,.0f} {var_str:>12} {item['variance_pct']:>+7.1f}% {status_icons[item['status']]:>6}{flag}")
        total_exp_budget += item["budget"]
        total_exp_actual += item["actual"]

    print(f"  {'─'*24} {'─'*12} {'─'*12} {'─'*12}")
    exp_var = total_exp_actual - total_exp_budget
    exp_var_pct = (exp_var / total_exp_budget * 100) if total_exp_budget else 0
    print(f"    {'TOTAL EXPENSES':<22} ${total_exp_budget:>11,.0f} ${total_exp_actual:>11,.0f} ${exp_var:>+11,.0f} {exp_var_pct:>+7.1f}%")

    net_budget = total_rev_budget - total_exp_budget
    net_actual = total_rev_actual - total_exp_actual
    print(f"\n    {'NET INCOME':<22} ${net_budget:>11,.0f} ${net_actual:>11,.0f} ${net_actual - net_budget:>+11,.0f}")

    # Flagged items summary
    flagged = [r for r in results if r["flagged"]]
    if flagged:
        print(f"\n  FLAGGED ITEMS (>{threshold}% variance):")
        print(f"  {'─'*60}")
        for item in sorted(flagged, key=lambda x: abs(x["variance_pct"]), reverse=True):
            direction = "over budget" if not item["favorable"] else "under budget" if item["type"] == "expense" else "above target"
            print(f"    {item['name']:<24} {item['variance_pct']:+.1f}% ({direction}) -> ${abs(item['variance']):,.0f}")

    print()


def main():
    parser = argparse.ArgumentParser(
        description="Generate budget variance analysis with flagging.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --period 2026-03 --threshold 10
  %(prog)s --period 2026-03 --threshold 5 --format json
        """,
    )
    parser.add_argument("--period", required=True, help="Reporting period (e.g., 2026-03)")
    parser.add_argument("--threshold", type=float, default=10,
                        help="Variance threshold percentage to flag (default: 10)")
    parser.add_argument("--format", choices=["text", "json"], default="text",
                        help="Output format (default: text)")

    args = parser.parse_args()
    data_key = args.period if args.period in SAMPLE_DATA else "2026-03"
    period_data = SAMPLE_DATA[data_key]

    results = analyze_variance(period_data["categories"], args.threshold)

    if args.format == "json":
        output = {
            "period": args.period,
            "period_label": period_data["period"],
            "threshold": args.threshold,
            "generated": datetime.now().strftime("%Y-%m-%d"),
            "items": results,
            "flagged_count": sum(1 for r in results if r["flagged"]),
        }
        print(json.dumps(output, indent=2))
    else:
        print_variance_report(results, period_data["period"], args.threshold)


if __name__ == "__main__":
    main()
