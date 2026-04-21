#!/usr/bin/env python3
"""
Initialize a new budget from template with pre-populated categories.

Usage:
    python create_budget.py --department engineering --year 2026 --approach zero-based
    python create_budget.py --department marketing --year 2026 --approach incremental --base-year 2025
"""

import argparse
import json
from datetime import datetime

# Department budget templates with typical allocations
DEPARTMENT_TEMPLATES = {
    "engineering": {
        "categories": [
            {"name": "Salaries & Wages", "annual_base": 1200000, "growth": 0.08},
            {"name": "Benefits & Insurance", "annual_base": 336000, "growth": 0.05},
            {"name": "Contractors & Freelancers", "annual_base": 180000, "growth": 0.10},
            {"name": "Cloud Infrastructure", "annual_base": 120000, "growth": 0.15},
            {"name": "SaaS & Subscriptions", "annual_base": 48000, "growth": 0.10},
            {"name": "Hardware & Equipment", "annual_base": 36000, "growth": 0.0},
            {"name": "Training & Development", "annual_base": 24000, "growth": 0.05},
            {"name": "Software Licenses", "annual_base": 18000, "growth": 0.08},
            {"name": "Travel", "annual_base": 12000, "growth": 0.0},
            {"name": "Miscellaneous", "annual_base": 6000, "growth": 0.0},
        ],
        "headcount": {"current": 12, "planned_hires": 3, "avg_salary": 130000},
    },
    "marketing": {
        "categories": [
            {"name": "Salaries & Wages", "annual_base": 600000, "growth": 0.06},
            {"name": "Benefits & Insurance", "annual_base": 168000, "growth": 0.05},
            {"name": "Advertising & Paid Media", "annual_base": 240000, "growth": 0.20},
            {"name": "Content & Creative", "annual_base": 96000, "growth": 0.10},
            {"name": "Events & Conferences", "annual_base": 72000, "growth": 0.05},
            {"name": "SaaS & Tools", "annual_base": 36000, "growth": 0.10},
            {"name": "Contractors & Agencies", "annual_base": 60000, "growth": 0.15},
            {"name": "Travel", "annual_base": 18000, "growth": 0.0},
            {"name": "Miscellaneous", "annual_base": 6000, "growth": 0.0},
        ],
        "headcount": {"current": 6, "planned_hires": 2, "avg_salary": 95000},
    },
    "sales": {
        "categories": [
            {"name": "Salaries & Wages", "annual_base": 480000, "growth": 0.10},
            {"name": "Benefits & Insurance", "annual_base": 134000, "growth": 0.05},
            {"name": "Commissions & Bonuses", "annual_base": 200000, "growth": 0.15},
            {"name": "Sales Tools & CRM", "annual_base": 36000, "growth": 0.08},
            {"name": "Travel & Entertainment", "annual_base": 48000, "growth": 0.05},
            {"name": "Training", "annual_base": 12000, "growth": 0.0},
            {"name": "Contractors", "annual_base": 24000, "growth": 0.10},
            {"name": "Miscellaneous", "annual_base": 6000, "growth": 0.0},
        ],
        "headcount": {"current": 5, "planned_hires": 3, "avg_salary": 85000},
    },
    "general": {
        "categories": [
            {"name": "Salaries & Wages", "annual_base": 360000, "growth": 0.05},
            {"name": "Benefits & Insurance", "annual_base": 100000, "growth": 0.05},
            {"name": "Office / Rent", "annual_base": 120000, "growth": 0.03},
            {"name": "Legal & Accounting", "annual_base": 60000, "growth": 0.05},
            {"name": "Insurance (D&O, E&O, GL)", "annual_base": 24000, "growth": 0.03},
            {"name": "Technology & IT", "annual_base": 18000, "growth": 0.08},
            {"name": "Travel & Meals", "annual_base": 12000, "growth": 0.0},
            {"name": "Professional Development", "annual_base": 8000, "growth": 0.0},
            {"name": "Miscellaneous", "annual_base": 6000, "growth": 0.0},
        ],
        "headcount": {"current": 4, "planned_hires": 1, "avg_salary": 90000},
    },
}

# Quarterly distribution (seasonality)
QUARTERLY_DISTRIBUTION = {
    "engineering": [0.24, 0.25, 0.25, 0.26],
    "marketing": [0.22, 0.26, 0.24, 0.28],
    "sales": [0.23, 0.25, 0.25, 0.27],
    "general": [0.25, 0.25, 0.25, 0.25],
}


def build_budget(department, year, approach, contingency_pct=7.0):
    """Build a budget for the given department and year."""
    template = DEPARTMENT_TEMPLATES.get(department, DEPARTMENT_TEMPLATES["general"])
    distribution = QUARTERLY_DISTRIBUTION.get(department, [0.25, 0.25, 0.25, 0.25])

    categories = []
    total_annual = 0

    for cat in template["categories"]:
        if approach == "zero-based":
            annual = cat["annual_base"]
        else:  # incremental
            annual = cat["annual_base"] * (1 + cat["growth"])

        annual = round(annual, -2)  # Round to nearest hundred
        quarterly = [round(annual * d, -2) for d in distribution]
        # Adjust Q4 to make sure sum matches
        quarterly[3] = annual - sum(quarterly[:3])

        categories.append({
            "name": cat["name"],
            "annual": annual,
            "quarterly": quarterly,
        })
        total_annual += annual

    contingency = round(total_annual * (contingency_pct / 100), -2)

    budget = {
        "department": department,
        "fiscal_year": year,
        "approach": approach,
        "created": datetime.now().strftime("%Y-%m-%d"),
        "headcount": template["headcount"],
        "categories": categories,
        "contingency": contingency,
        "contingency_pct": contingency_pct,
        "total_annual": total_annual + contingency,
    }
    return budget


def print_budget(budget):
    """Print formatted budget."""
    print("=" * 80)
    print(f"  BUDGET: {budget['department'].upper()} DEPARTMENT")
    print(f"  Fiscal Year: {budget['fiscal_year']}")
    print(f"  Approach: {budget['approach'].replace('-', ' ').title()}")
    print(f"  Created: {budget['created']}")
    print("=" * 80)

    hc = budget["headcount"]
    print(f"\n  HEADCOUNT PLAN")
    print(f"    Current FTEs:     {hc['current']}")
    print(f"    Planned Hires:    {hc['planned_hires']}")
    print(f"    Year-end FTEs:    {hc['current'] + hc['planned_hires']}")
    print(f"    Avg Salary:       ${hc['avg_salary']:,.0f}")

    print(f"\n  {'Category':<28} {'Q1':>10} {'Q2':>10} {'Q3':>10} {'Q4':>10} {'Annual':>12}")
    print(f"  {'─'*28} {'─'*10} {'─'*10} {'─'*10} {'─'*10} {'─'*12}")

    subtotal_q = [0, 0, 0, 0]
    for cat in budget["categories"]:
        q = cat["quarterly"]
        print(f"  {cat['name']:<28} ${q[0]:>9,.0f} ${q[1]:>9,.0f} ${q[2]:>9,.0f} ${q[3]:>9,.0f} ${cat['annual']:>11,.0f}")
        for i in range(4):
            subtotal_q[i] += q[i]

    print(f"  {'─'*28} {'─'*10} {'─'*10} {'─'*10} {'─'*10} {'─'*12}")
    subtotal = sum(cat["annual"] for cat in budget["categories"])
    print(f"  {'Subtotal':<28} ${subtotal_q[0]:>9,.0f} ${subtotal_q[1]:>9,.0f} ${subtotal_q[2]:>9,.0f} ${subtotal_q[3]:>9,.0f} ${subtotal:>11,.0f}")

    cont_q = round(budget["contingency"] / 4, -2)
    print(f"  {'Contingency (' + str(budget['contingency_pct']) + '%)':<28} ${cont_q:>9,.0f} ${cont_q:>9,.0f} ${cont_q:>9,.0f} ${cont_q:>9,.0f} ${budget['contingency']:>11,.0f}")

    print(f"  {'═'*28} {'═'*10} {'═'*10} {'═'*10} {'═'*10} {'═'*12}")
    total_q = [sq + cont_q for sq in subtotal_q]
    print(f"  {'TOTAL':<28} ${total_q[0]:>9,.0f} ${total_q[1]:>9,.0f} ${total_q[2]:>9,.0f} ${total_q[3]:>9,.0f} ${budget['total_annual']:>11,.0f}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Initialize a new department budget from template.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --department engineering --year 2026 --approach zero-based
  %(prog)s --department marketing --year 2026 --approach incremental
  %(prog)s --department sales --year 2026 --approach zero-based --contingency 10
        """,
    )
    parser.add_argument("--department", required=True,
                        choices=list(DEPARTMENT_TEMPLATES.keys()),
                        help="Department name")
    parser.add_argument("--year", type=int, required=True, help="Fiscal year")
    parser.add_argument("--approach", required=True,
                        choices=["zero-based", "incremental"],
                        help="Budgeting approach")
    parser.add_argument("--contingency", type=float, default=7.0,
                        help="Contingency percentage (default: 7)")
    parser.add_argument("--format", choices=["text", "json"], default="text",
                        help="Output format (default: text)")

    args = parser.parse_args()
    budget = build_budget(args.department, args.year, args.approach, args.contingency)

    if args.format == "json":
        print(json.dumps(budget, indent=2))
    else:
        print_budget(budget)


if __name__ == "__main__":
    main()
