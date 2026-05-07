#!/usr/bin/env python3
"""
Generate a Profit & Loss report with variance analysis.

Usage:
    python generate_pnl.py --period Q1-2026 --compare budget,prior
    python generate_pnl.py --period 2026-03 --compare budget --format json
"""

import argparse
import json
from datetime import datetime

# Sample financial data
SAMPLE_DATA = {
    "Q1-2026": {
        "actual": {
            "product_revenue": 850000,
            "service_revenue": 320000,
            "other_revenue": 15000,
            "direct_costs": 195000,
            "hosting_infra": 42000,
            "salaries_benefits": 480000,
            "sales_marketing": 125000,
            "rd_engineering": 95000,
            "general_admin": 65000,
        },
        "budget": {
            "product_revenue": 800000,
            "service_revenue": 350000,
            "other_revenue": 10000,
            "direct_costs": 180000,
            "hosting_infra": 38000,
            "salaries_benefits": 475000,
            "sales_marketing": 110000,
            "rd_engineering": 100000,
            "general_admin": 60000,
        },
        "prior": {
            "product_revenue": 720000,
            "service_revenue": 295000,
            "other_revenue": 12000,
            "direct_costs": 170000,
            "hosting_infra": 35000,
            "salaries_benefits": 450000,
            "sales_marketing": 105000,
            "rd_engineering": 85000,
            "general_admin": 58000,
        },
    },
}

PERIOD_LABELS = {
    "Q1-2026": {"start": "Jan 1, 2026", "end": "Mar 31, 2026"},
    "2026-03": {"start": "Mar 1, 2026", "end": "Mar 31, 2026"},
}


def compute_pnl(data):
    """Compute derived P&L values from raw data."""
    revenue = data["product_revenue"] + data["service_revenue"] + data["other_revenue"]
    cogs = data["direct_costs"] + data["hosting_infra"]
    gross_profit = revenue - cogs
    gross_margin = (gross_profit / revenue * 100) if revenue else 0
    opex = data["salaries_benefits"] + data["sales_marketing"] + data["rd_engineering"] + data["general_admin"]
    net_income = gross_profit - opex
    net_margin = (net_income / revenue * 100) if revenue else 0
    return {
        "total_revenue": revenue,
        "total_cogs": cogs,
        "gross_profit": gross_profit,
        "gross_margin": round(gross_margin, 1),
        "total_opex": opex,
        "net_income": net_income,
        "net_margin": round(net_margin, 1),
        **data,
    }


def compute_variance(actual, compare, label):
    """Compute variance between actual and comparison data."""
    variances = []
    for key in actual:
        if key in compare and isinstance(actual[key], (int, float)):
            diff = actual[key] - compare[key]
            pct = (diff / compare[key] * 100) if compare[key] else 0
            # For expense items, over budget is negative (bad)
            is_revenue = "revenue" in key or key in ("total_revenue", "gross_profit", "net_income")
            favorable = diff > 0 if is_revenue else diff < 0
            variances.append({
                "item": key,
                "actual": actual[key],
                f"{label}": compare[key],
                "variance": diff,
                "variance_pct": round(pct, 1),
                "favorable": favorable,
            })
    return variances


def format_currency(amount):
    if amount < 0:
        return f"(${abs(amount):,.0f})"
    return f"${amount:,.0f}"


def print_pnl(actual_pnl, comparisons, period):
    """Print formatted P&L report."""
    labels = PERIOD_LABELS.get(period, {"start": period, "end": period})

    print("=" * 80)
    print(f"  PROFIT & LOSS STATEMENT")
    print(f"  Period: {labels['start']} to {labels['end']}")
    comp_labels = ", ".join(f"vs. {c}" for c in comparisons.keys())
    print(f"  Comparison: {comp_labels}")
    print("=" * 80)

    def row(label, key, indent=2):
        parts = [f"{'  ' * indent}{label:<28}"]
        parts.append(f"{format_currency(actual_pnl[key]):>12}")
        for comp_name, comp_pnl in comparisons.items():
            diff = actual_pnl[key] - comp_pnl[key]
            parts.append(f"{format_currency(comp_pnl[key]):>12}")
            parts.append(f"{format_currency(diff):>12}")
        print("".join(parts))

    header = f"{'':28}{'Actual':>14}"
    for comp_name in comparisons:
        header += f"{comp_name.capitalize():>14}{'Variance':>12}"
    print(f"  {header}")
    print(f"  {'─' * (len(header))}")

    print("  REVENUE")
    row("Product Revenue", "product_revenue")
    row("Service Revenue", "service_revenue")
    row("Other Revenue", "other_revenue")
    print(f"  {'─' * 60}")
    row("TOTAL REVENUE", "total_revenue", 1)
    print()

    print("  COST OF GOODS SOLD")
    row("Direct Costs", "direct_costs")
    row("Hosting / Infra", "hosting_infra")
    print(f"  {'─' * 60}")
    row("TOTAL COGS", "total_cogs", 1)
    print()

    row("GROSS PROFIT", "gross_profit", 1)
    print(f"    Gross Margin: {actual_pnl['gross_margin']}%")
    print()

    print("  OPERATING EXPENSES")
    row("Salaries & Benefits", "salaries_benefits")
    row("Sales & Marketing", "sales_marketing")
    row("R&D / Engineering", "rd_engineering")
    row("General & Admin", "general_admin")
    print(f"  {'─' * 60}")
    row("TOTAL OpEx", "total_opex", 1)
    print()

    row("NET INCOME (LOSS)", "net_income", 1)
    print(f"    Net Margin: {actual_pnl['net_margin']}%")
    print("=" * 80)

    # Flag material variances
    print("\nMATERIAL VARIANCES (>10%):")
    for comp_name, comp_pnl in comparisons.items():
        variances = compute_variance(actual_pnl, comp_pnl, comp_name)
        flagged = [v for v in variances if abs(v["variance_pct"]) > 10 and v["item"] not in ("gross_margin", "net_margin")]
        if flagged:
            print(f"\n  vs. {comp_name.capitalize()}:")
            for v in flagged:
                direction = "OVER" if not v["favorable"] else "UNDER" if "revenue" not in v["item"] else "ABOVE"
                print(f"    {v['item']:<28} {format_currency(v['variance']):>12} ({v['variance_pct']:+.1f}%) {direction}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate P&L report with variance analysis.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --period Q1-2026 --compare budget,prior
  %(prog)s --period Q1-2026 --compare budget --format json
        """,
    )
    parser.add_argument("--period", required=True, help="Reporting period (e.g., Q1-2026, 2026-03)")
    parser.add_argument("--compare", default="budget,prior",
                        help="Comparison datasets, comma-separated (default: budget,prior)")
    parser.add_argument("--format", choices=["text", "json"], default="text",
                        help="Output format (default: text)")

    args = parser.parse_args()
    period = args.period
    compare_types = [c.strip() for c in args.compare.split(",")]

    # Use sample data, default to Q1-2026
    data_key = period if period in SAMPLE_DATA else "Q1-2026"
    period_data = SAMPLE_DATA[data_key]

    actual_pnl = compute_pnl(period_data["actual"])
    comparisons = {}
    for ct in compare_types:
        if ct in period_data:
            comparisons[ct] = compute_pnl(period_data[ct])

    if args.format == "json":
        result = {
            "period": period,
            "actual": actual_pnl,
            "comparisons": comparisons,
        }
        print(json.dumps(result, indent=2))
    else:
        print_pnl(actual_pnl, comparisons, period)


if __name__ == "__main__":
    main()
