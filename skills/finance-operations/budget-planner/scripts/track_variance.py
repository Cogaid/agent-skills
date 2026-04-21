#!/usr/bin/env python3
"""
Monthly budget variance tracking with threshold flagging.

Usage:
    python track_variance.py --period 2026-03 --threshold 10
    python track_variance.py --period 2026-03 --department engineering --format json
"""

import argparse
import json
from datetime import datetime

SAMPLE_VARIANCE_DATA = {
    "2026-03": {
        "engineering": [
            {"category": "Salaries & Wages", "budget": 100000, "actual": 98500},
            {"category": "Benefits", "budget": 28000, "actual": 28200},
            {"category": "Contractors", "budget": 15000, "actual": 22000},
            {"category": "Cloud Infrastructure", "budget": 10000, "actual": 13500},
            {"category": "SaaS Tools", "budget": 4000, "actual": 4200},
            {"category": "Hardware", "budget": 3000, "actual": 0},
            {"category": "Training", "budget": 2000, "actual": 1500},
        ],
        "marketing": [
            {"category": "Salaries & Wages", "budget": 50000, "actual": 50000},
            {"category": "Paid Advertising", "budget": 20000, "actual": 26500},
            {"category": "Content & Creative", "budget": 8000, "actual": 7200},
            {"category": "Events", "budget": 6000, "actual": 12000},
            {"category": "Tools", "budget": 3000, "actual": 3100},
        ],
        "sales": [
            {"category": "Salaries & Wages", "budget": 40000, "actual": 40000},
            {"category": "Commissions", "budget": 18000, "actual": 24500},
            {"category": "Travel", "budget": 4000, "actual": 5200},
            {"category": "CRM & Tools", "budget": 3000, "actual": 3000},
        ],
    },
}


def analyze(data, threshold):
    results = []
    for item in data:
        variance = item["actual"] - item["budget"]
        var_pct = (variance / item["budget"] * 100) if item["budget"] else 0

        if abs(var_pct) <= 5:
            status = "on_track"
        elif abs(var_pct) <= threshold:
            status = "watch"
        else:
            status = "alert"

        results.append({
            "category": item["category"],
            "budget": item["budget"],
            "actual": item["actual"],
            "variance": variance,
            "variance_pct": round(var_pct, 1),
            "status": status,
            "flagged": abs(var_pct) > threshold,
        })
    return results


def print_report(department, results, period, threshold):
    status_icons = {"on_track": "OK", "watch": "WATCH", "alert": "ALERT"}

    print(f"\n  VARIANCE REPORT: {department.upper()}")
    print(f"  Period: {period} | Threshold: {threshold}%")
    print(f"  {'─'*70}")
    print(f"  {'Category':<24} {'Budget':>10} {'Actual':>10} {'Variance':>10} {'Var%':>8} {'Status':>8}")
    print(f"  {'─'*24} {'─'*10} {'─'*10} {'─'*10} {'─'*8} {'─'*8}")

    total_budget = 0
    total_actual = 0
    for r in results:
        flag = " *" if r["flagged"] else ""
        print(f"  {r['category']:<24} ${r['budget']:>9,.0f} ${r['actual']:>9,.0f} ${r['variance']:>+9,.0f} {r['variance_pct']:>+7.1f}% {status_icons[r['status']]:>6}{flag}")
        total_budget += r["budget"]
        total_actual += r["actual"]

    total_var = total_actual - total_budget
    total_pct = (total_var / total_budget * 100) if total_budget else 0
    print(f"  {'─'*24} {'─'*10} {'─'*10} {'─'*10} {'─'*8}")
    print(f"  {'TOTAL':<24} ${total_budget:>9,.0f} ${total_actual:>9,.0f} ${total_var:>+9,.0f} {total_pct:>+7.1f}%")

    flagged = [r for r in results if r["flagged"]]
    if flagged:
        print(f"\n  ACTION ITEMS:")
        for r in flagged:
            print(f"    - {r['category']}: {r['variance_pct']:+.1f}% (${abs(r['variance']):,.0f} {'over' if r['variance'] > 0 else 'under'}) -> Investigate and document")


def main():
    parser = argparse.ArgumentParser(
        description="Monthly budget variance tracking.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--period", required=True, help="Period (e.g., 2026-03)")
    parser.add_argument("--department", default=None, help="Filter by department")
    parser.add_argument("--threshold", type=float, default=10, help="Variance threshold % (default: 10)")
    parser.add_argument("--format", choices=["text", "json"], default="text")

    args = parser.parse_args()
    period_key = args.period if args.period in SAMPLE_VARIANCE_DATA else "2026-03"
    period_data = SAMPLE_VARIANCE_DATA[period_key]

    departments = [args.department] if args.department and args.department in period_data else list(period_data.keys())

    all_results = {}
    for dept in departments:
        all_results[dept] = analyze(period_data[dept], args.threshold)

    if args.format == "json":
        print(json.dumps({"period": args.period, "threshold": args.threshold, "departments": all_results}, indent=2))
    else:
        print("=" * 75)
        print(f"  BUDGET VARIANCE TRACKING - {args.period}")
        print("=" * 75)
        for dept, results in all_results.items():
            print_report(dept, results, args.period, args.threshold)
        print()


if __name__ == "__main__":
    main()
