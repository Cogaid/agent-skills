#!/usr/bin/env python3
"""
Generate a financial KPI dashboard with trend data.

Usage:
    python financial_dashboard.py --metrics revenue,margin,runway --format text
    python financial_dashboard.py --metrics all --format json
"""

import argparse
import json
from datetime import datetime

# Sample dashboard data (6 months)
MONTHLY_DATA = [
    {"month": "2025-11", "mrr": 180000, "arr": 2160000, "gross_margin": 72.3, "net_margin": 12.1,
     "cash": 2800000, "burn": 158000, "customers": 245, "new_customers": 18, "churn_pct": 2.1,
     "cac": 3200, "ltv": 14500, "nrr": 108, "headcount": 42, "revenue_per_emp": 4286},
    {"month": "2025-12", "mrr": 188000, "arr": 2256000, "gross_margin": 73.1, "net_margin": 13.5,
     "cash": 2650000, "burn": 152000, "customers": 258, "new_customers": 22, "churn_pct": 1.9,
     "cac": 2900, "ltv": 15100, "nrr": 110, "headcount": 44, "revenue_per_emp": 4273},
    {"month": "2026-01", "mrr": 198000, "arr": 2376000, "gross_margin": 74.0, "net_margin": 14.2,
     "cash": 2510000, "burn": 148000, "customers": 275, "new_customers": 25, "churn_pct": 1.8,
     "cac": 2750, "ltv": 15800, "nrr": 112, "headcount": 45, "revenue_per_emp": 4400},
    {"month": "2026-02", "mrr": 205000, "arr": 2460000, "gross_margin": 74.5, "net_margin": 14.8,
     "cash": 2380000, "burn": 142000, "customers": 290, "new_customers": 20, "churn_pct": 1.7,
     "cac": 3100, "ltv": 16200, "nrr": 113, "headcount": 46, "revenue_per_emp": 4457},
    {"month": "2026-03", "mrr": 215000, "arr": 2580000, "gross_margin": 75.2, "net_margin": 15.5,
     "cash": 2270000, "burn": 138000, "customers": 308, "new_customers": 24, "churn_pct": 1.5,
     "cac": 2600, "ltv": 16800, "nrr": 115, "headcount": 47, "revenue_per_emp": 4574},
    {"month": "2026-04", "mrr": 228000, "arr": 2736000, "gross_margin": 75.8, "net_margin": 16.1,
     "cash": 2180000, "burn": 132000, "customers": 325, "new_customers": 26, "churn_pct": 1.4,
     "cac": 2450, "ltv": 17500, "nrr": 116, "headcount": 48, "revenue_per_emp": 4750},
]

METRIC_GROUPS = {
    "revenue": ["mrr", "arr"],
    "margin": ["gross_margin", "net_margin"],
    "cash": ["cash", "burn"],
    "runway": ["cash", "burn"],
    "customers": ["customers", "new_customers", "churn_pct"],
    "efficiency": ["cac", "ltv", "nrr", "ltv_cac"],
    "team": ["headcount", "revenue_per_emp"],
}


def format_currency(val):
    if val >= 1000000:
        return f"${val / 1000000:.1f}M"
    elif val >= 1000:
        return f"${val / 1000:.0f}K"
    return f"${val:,.0f}"


def print_dashboard(data, metrics):
    current = data[-1]
    prev = data[-2] if len(data) > 1 else current

    print("=" * 70)
    print(f"  FINANCIAL DASHBOARD - {current['month']}")
    print(f"  Last Updated: {datetime.now().strftime('%Y-%m-%d')}")
    print("=" * 70)

    if "revenue" in metrics or "all" in metrics:
        mrr_chg = (current["mrr"] - prev["mrr"]) / prev["mrr"] * 100
        print(f"\n  REVENUE")
        print(f"  {'─' * 50}")
        print(f"    MRR:          {format_currency(current['mrr']):>12}   ({mrr_chg:+.1f}% MoM)")
        print(f"    ARR:          {format_currency(current['arr']):>12}")
        six_mo = data[0] if len(data) >= 6 else data[0]
        six_mo_growth = (current["mrr"] - six_mo["mrr"]) / six_mo["mrr"] * 100
        print(f"    6-mo growth:  {six_mo_growth:>11.1f}%")

    if "margin" in metrics or "all" in metrics:
        gm_chg = current["gross_margin"] - prev["gross_margin"]
        nm_chg = current["net_margin"] - prev["net_margin"]
        print(f"\n  PROFITABILITY")
        print(f"  {'─' * 50}")
        print(f"    Gross Margin: {current['gross_margin']:>11.1f}%   ({gm_chg:+.1f}pp MoM)")
        print(f"    Net Margin:   {current['net_margin']:>11.1f}%   ({nm_chg:+.1f}pp MoM)")

    if "cash" in metrics or "runway" in metrics or "all" in metrics:
        runway = current["cash"] / current["burn"] if current["burn"] else float("inf")
        print(f"\n  CASH")
        print(f"  {'─' * 50}")
        print(f"    Cash:         {format_currency(current['cash']):>12}")
        print(f"    Burn Rate:    {format_currency(current['burn']):>12}/mo")
        print(f"    Runway:       {runway:>11.1f} months")

    if "customers" in metrics or "all" in metrics:
        print(f"\n  CUSTOMERS")
        print(f"  {'─' * 50}")
        print(f"    Total:        {current['customers']:>12,}")
        print(f"    New (month):  {current['new_customers']:>12}")
        print(f"    Churn Rate:   {current['churn_pct']:>11.1f}%")

    if "efficiency" in metrics or "all" in metrics:
        ltv_cac = current["ltv"] / current["cac"] if current["cac"] else 0
        print(f"\n  EFFICIENCY")
        print(f"  {'─' * 50}")
        print(f"    CAC:          {format_currency(current['cac']):>12}")
        print(f"    LTV:          {format_currency(current['ltv']):>12}")
        print(f"    LTV:CAC:      {ltv_cac:>11.1f}:1")
        print(f"    NRR:          {current['nrr']:>11}%")

    if "team" in metrics or "all" in metrics:
        print(f"\n  TEAM")
        print(f"  {'─' * 50}")
        print(f"    Headcount:    {current['headcount']:>12}")
        print(f"    Rev/Employee: {format_currency(current['revenue_per_emp']):>12}")

    # Trend table
    print(f"\n  MONTHLY TREND")
    print(f"  {'─' * 66}")
    print(f"    {'Month':<10} {'MRR':>10} {'GM%':>8} {'Cash':>10} {'Customers':>10} {'Burn':>10}")
    print(f"    {'─'*10} {'─'*10} {'─'*8} {'─'*10} {'─'*10} {'─'*10}")
    for d in data:
        print(f"    {d['month']:<10} {format_currency(d['mrr']):>10} {d['gross_margin']:>7.1f}% {format_currency(d['cash']):>10} {d['customers']:>10} {format_currency(d['burn']):>10}")
    print("=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="Generate financial KPI dashboard with trends.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --metrics revenue,margin,runway
  %(prog)s --metrics all
  %(prog)s --metrics all --format json
        """,
    )
    parser.add_argument("--metrics", default="all",
                        help="Metric groups: revenue,margin,cash,runway,customers,efficiency,team,all (default: all)")
    parser.add_argument("--months", type=int, default=6, help="Number of months to show (default: 6)")
    parser.add_argument("--format", choices=["text", "json", "html"], default="text",
                        help="Output format (default: text)")

    args = parser.parse_args()
    metrics = [m.strip() for m in args.metrics.split(",")]
    data = MONTHLY_DATA[-args.months:]

    if args.format == "json":
        current = data[-1]
        ltv_cac = current["ltv"] / current["cac"] if current["cac"] else 0
        runway = current["cash"] / current["burn"] if current["burn"] else 0
        result = {
            "period": current["month"],
            "generated": datetime.now().strftime("%Y-%m-%d"),
            "current": {**current, "ltv_cac": round(ltv_cac, 1), "runway_months": round(runway, 1)},
            "trend": data,
        }
        print(json.dumps(result, indent=2))
    else:
        print_dashboard(data, metrics)


if __name__ == "__main__":
    main()
