#!/usr/bin/env python3
"""
Monitor and compare competitor pricing with change tracking.

Usage:
    python competitor_tracker.py --competitors "compA,compB,compC"
    python competitor_tracker.py --all --format json
"""

import argparse
import json
from datetime import datetime

COMPETITOR_DATA = {
    "Competitor A": {
        "company": "Competitor A",
        "url": "competitora.com",
        "last_checked": "2026-04-15",
        "plans": [
            {"name": "Starter", "price": 29, "billing": "monthly", "annual_price": 24},
            {"name": "Professional", "price": 79, "billing": "monthly", "annual_price": 65},
            {"name": "Enterprise", "price": None, "billing": "custom", "annual_price": None},
        ],
        "free_tier": True,
        "free_trial_days": 14,
        "model": "per-seat",
        "target": "SMB",
        "recent_changes": [
            {"date": "2026-03-01", "change": "Raised Starter from $25 to $29 (+16%)"},
            {"date": "2025-09-15", "change": "Added free tier (previously trial-only)"},
        ],
    },
    "Competitor B": {
        "company": "Competitor B",
        "url": "competitorb.com",
        "last_checked": "2026-04-12",
        "plans": [
            {"name": "Basic", "price": 19, "billing": "monthly", "annual_price": 15},
            {"name": "Plus", "price": 49, "billing": "monthly", "annual_price": 39},
            {"name": "Business", "price": 99, "billing": "monthly", "annual_price": 79},
        ],
        "free_tier": False,
        "free_trial_days": 30,
        "model": "flat-rate",
        "target": "SMB-Mid",
        "recent_changes": [
            {"date": "2026-01-10", "change": "Introduced Business tier (new)"},
            {"date": "2025-11-01", "change": "Reduced trial from 30 to 14 days, then reverted"},
        ],
    },
    "Competitor C": {
        "company": "Competitor C",
        "url": "competitorc.com",
        "last_checked": "2026-04-10",
        "plans": [
            {"name": "Team", "price": 12, "billing": "per-user/month", "annual_price": 10},
            {"name": "Business", "price": 25, "billing": "per-user/month", "annual_price": 20},
            {"name": "Enterprise", "price": None, "billing": "custom", "annual_price": None},
        ],
        "free_tier": True,
        "free_trial_days": 14,
        "model": "per-seat",
        "target": "Mid-Enterprise",
        "recent_changes": [
            {"date": "2026-02-20", "change": "Added usage-based add-on for API calls ($0.01/call)"},
        ],
    },
}


def print_comparison(competitors):
    """Print formatted competitor comparison."""
    print("=" * 80)
    print(f"  COMPETITOR PRICING TRACKER")
    print(f"  As of: {datetime.now().strftime('%Y-%m-%d')}")
    print("=" * 80)

    for name, data in competitors.items():
        print(f"\n  {data['company']} ({data['url']})")
        print(f"  Last checked: {data['last_checked']} | Model: {data['model']} | Target: {data['target']}")
        print(f"  Free tier: {'Yes' if data['free_tier'] else 'No'} | Trial: {data['free_trial_days']} days")
        print(f"  {'─'*72}")
        print(f"  {'Plan':<20} {'Monthly':>10} {'Annual':>10} {'Annual Discount':>16}")
        print(f"  {'─'*20} {'─'*10} {'─'*10} {'─'*16}")
        for plan in data["plans"]:
            monthly = f"${plan['price']}/mo" if plan["price"] else "Custom"
            annual = f"${plan['annual_price']}/mo" if plan["annual_price"] else "Custom"
            if plan["price"] and plan["annual_price"]:
                discount = round((1 - plan["annual_price"] / plan["price"]) * 100)
                discount_str = f"{discount}%"
            else:
                discount_str = "--"
            print(f"  {plan['name']:<20} {monthly:>10} {annual:>10} {discount_str:>16}")

        if data["recent_changes"]:
            print(f"\n  Recent changes:")
            for change in data["recent_changes"]:
                print(f"    [{change['date']}] {change['change']}")

    # Summary comparison table
    print(f"\n{'=' * 80}")
    print(f"  PRICE COMPARISON MATRIX (monthly, lowest tier)")
    print(f"  {'─'*72}")
    print(f"  {'Competitor':<20} {'Entry Price':>12} {'Mid Price':>12} {'Top Price':>12} {'Model':<12}")
    print(f"  {'─'*20} {'─'*12} {'─'*12} {'─'*12} {'─'*12}")
    for name, data in competitors.items():
        plans = data["plans"]
        prices = [p["price"] for p in plans if p["price"]]
        entry = f"${min(prices)}" if prices else "Custom"
        top = f"${max(prices)}" if prices else "Custom"
        mid = f"${prices[len(prices)//2]}" if len(prices) > 1 else entry
        print(f"  {data['company']:<20} {entry:>12} {mid:>12} {top:>12} {data['model']:<12}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Monitor and compare competitor pricing.",
    )
    parser.add_argument("--competitors", default=None,
                        help="Comma-separated competitor names to show")
    parser.add_argument("--all", action="store_true", help="Show all tracked competitors")
    parser.add_argument("--format", choices=["text", "json"], default="text")

    args = parser.parse_args()

    if args.competitors:
        names = [n.strip() for n in args.competitors.split(",")]
        selected = {k: v for k, v in COMPETITOR_DATA.items()
                    if any(n.lower() in k.lower() for n in names)}
    else:
        selected = COMPETITOR_DATA

    if not selected:
        selected = COMPETITOR_DATA

    if args.format == "json":
        print(json.dumps(selected, indent=2))
    else:
        print_comparison(selected)


if __name__ == "__main__":
    main()
