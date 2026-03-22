#!/usr/bin/env python3
"""
Calculate ROI metrics for sales proposals.

Usage:
    python calculate_roi.py --current-cost 50000 --savings 30000 --investment 25000
    python calculate_roi.py --interactive

Output: JSON with ROI metrics
"""

import argparse
import json
import sys


def calculate_roi_metrics(current_cost, annual_savings, investment, years=3):
    """Calculate ROI metrics."""

    # Basic calculations
    net_annual_benefit = annual_savings
    payback_months = (investment / net_annual_benefit) * 12 if net_annual_benefit > 0 else float('inf')

    # Year 1 ROI
    year1_net = net_annual_benefit - investment
    year1_roi = (year1_net / investment) * 100 if investment > 0 else 0

    # Multi-year calculations
    cumulative_benefits = []
    cumulative_net = []

    for year in range(1, years + 1):
        total_benefit = net_annual_benefit * year
        net_value = total_benefit - investment
        cumulative_benefits.append({
            "year": year,
            "cumulative_benefit": round(total_benefit, 2),
            "cumulative_net": round(net_value, 2),
            "roi_percent": round((net_value / investment) * 100, 1) if investment > 0 else 0
        })

    # Calculate break-even point
    if payback_months <= years * 12:
        break_even = f"{int(payback_months)} months"
    else:
        break_even = f">{years} years"

    return {
        "inputs": {
            "current_annual_cost": current_cost,
            "annual_savings": annual_savings,
            "investment": investment,
            "analysis_period_years": years
        },
        "metrics": {
            "payback_period_months": round(payback_months, 1),
            "break_even": break_even,
            "year1_net_value": round(year1_net, 2),
            "year1_roi_percent": round(year1_roi, 1),
            f"year{years}_total_benefit": round(net_annual_benefit * years, 2),
            f"year{years}_net_value": round((net_annual_benefit * years) - investment, 2),
            f"year{years}_roi_percent": round(((net_annual_benefit * years - investment) / investment) * 100, 1) if investment > 0 else 0
        },
        "yearly_breakdown": cumulative_benefits,
        "summary": {
            "investment_per_dollar_return": round(investment / (net_annual_benefit * years), 2) if net_annual_benefit > 0 else None,
            "return_per_dollar_invested": round((net_annual_benefit * years) / investment, 2) if investment > 0 else 0
        }
    }


def interactive_mode():
    """Interactive ROI calculation."""
    print("=== ROI Calculator ===\n")

    print("--- CURRENT COSTS ---")
    current_cost = float(input("Current annual cost of problem: $").replace(",", ""))

    print("\n--- EXPECTED BENEFITS ---")
    annual_savings = float(input("Expected annual savings/benefit: $").replace(",", ""))

    print("\n--- INVESTMENT ---")
    investment = float(input("Total investment required: $").replace(",", ""))

    print("\n--- ANALYSIS PERIOD ---")
    years_input = input("Years to analyze (default 3): ").strip()
    years = int(years_input) if years_input else 3

    return current_cost, annual_savings, investment, years


def format_currency(amount):
    """Format number as currency."""
    return f"${amount:,.2f}"


def print_summary(result):
    """Print formatted summary."""
    metrics = result["metrics"]

    print("\n" + "=" * 50)
    print("ROI SUMMARY")
    print("=" * 50)
    print(f"Investment:          {format_currency(result['inputs']['investment'])}")
    print(f"Annual Benefit:      {format_currency(result['inputs']['annual_savings'])}")
    print(f"Payback Period:      {metrics['break_even']}")
    print(f"Year 1 ROI:          {metrics['year1_roi_percent']}%")
    print(f"Year 1 Net Value:    {format_currency(metrics['year1_net_value'])}")

    years = result['inputs']['analysis_period_years']
    print(f"\n{years}-Year Analysis:")
    print(f"  Total Benefit:     {format_currency(metrics[f'year{years}_total_benefit'])}")
    print(f"  Net Value:         {format_currency(metrics[f'year{years}_net_value'])}")
    print(f"  ROI:               {metrics[f'year{years}_roi_percent']}%")

    print(f"\nFor every $1 invested: ${result['summary']['return_per_dollar_invested']} return")
    print("=" * 50)


def main():
    parser = argparse.ArgumentParser(description="Calculate ROI metrics")
    parser.add_argument("--current-cost", type=float, help="Current annual cost")
    parser.add_argument("--savings", type=float, help="Annual savings/benefit")
    parser.add_argument("--investment", type=float, help="Total investment")
    parser.add_argument("--years", type=int, default=3, help="Analysis period")
    parser.add_argument("--interactive", "-i", action="store_true", help="Interactive mode")
    parser.add_argument("--json", action="store_true", help="Output as JSON only")

    args = parser.parse_args()

    if args.interactive:
        current_cost, savings, investment, years = interactive_mode()
    elif args.current_cost and args.savings and args.investment:
        current_cost = args.current_cost
        savings = args.savings
        investment = args.investment
        years = args.years
    else:
        parser.print_help()
        sys.exit(1)

    result = calculate_roi_metrics(current_cost, savings, investment, years)

    if args.json or not args.interactive:
        print(json.dumps(result, indent=2))
    else:
        print_summary(result)
        print("\nFull JSON output:")
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
