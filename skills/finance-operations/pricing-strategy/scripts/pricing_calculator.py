#!/usr/bin/env python3
"""
Model pricing scenarios with cost, value, and competitive analysis.

Usage:
    python pricing_calculator.py --cost 15 --target-margin 70 --volume 1000
    python pricing_calculator.py --cost 15 --target-margin 70 --volume 1000 --value-delivered 200
    python pricing_calculator.py --scenarios
"""

import argparse
import json
from datetime import datetime

SAMPLE_SCENARIOS = [
    {"name": "Conservative", "price": 29, "volume": 1200, "churn": 5.0},
    {"name": "Base", "price": 49, "volume": 1000, "churn": 3.5},
    {"name": "Premium", "price": 79, "volume": 700, "churn": 2.5},
    {"name": "Enterprise", "price": 149, "volume": 350, "churn": 1.5},
]


def calculate_pricing(cost, target_margin, volume, value_delivered=None, competitor_avg=None):
    """Calculate pricing recommendations from multiple angles."""
    # Cost-based pricing
    cost_price = cost / (1 - target_margin / 100)

    # Value-based pricing (if value provided)
    value_price_low = value_delivered * 0.10 if value_delivered else None
    value_price_high = value_delivered * 0.30 if value_delivered else None

    # Revenue projections at different price points
    price_points = [
        round(cost_price * 0.8),
        round(cost_price),
        round(cost_price * 1.2),
        round(cost_price * 1.5),
        round(cost_price * 2.0),
    ]

    if value_delivered:
        price_points.extend([round(value_price_low), round(value_price_high)])
    if competitor_avg:
        price_points.extend([round(competitor_avg * 0.9), round(competitor_avg), round(competitor_avg * 1.1)])

    price_points = sorted(set(price_points))

    projections = []
    for price in price_points:
        margin = (price - cost) / price * 100 if price > 0 else 0
        # Simple elasticity model: volume decreases as price increases
        base_price = cost_price
        elasticity = -1.2  # moderate elasticity
        volume_adj = volume * (1 + elasticity * (price - base_price) / base_price)
        volume_adj = max(volume_adj, volume * 0.2)  # floor at 20% of base volume

        revenue = price * volume_adj
        gross_profit = (price - cost) * volume_adj

        projections.append({
            "price": price,
            "margin_pct": round(margin, 1),
            "est_volume": round(volume_adj),
            "monthly_revenue": round(revenue),
            "monthly_profit": round(gross_profit),
            "annual_revenue": round(revenue * 12),
            "annual_profit": round(gross_profit * 12),
        })

    result = {
        "inputs": {
            "unit_cost": cost,
            "target_margin": target_margin,
            "base_volume": volume,
            "value_delivered": value_delivered,
            "competitor_avg": competitor_avg,
        },
        "cost_based_price": round(cost_price, 2),
        "value_based_range": {
            "low": round(value_price_low, 2) if value_price_low else None,
            "high": round(value_price_high, 2) if value_price_high else None,
        },
        "projections": projections,
        "recommendation": None,
    }

    # Find optimal (max profit)
    best = max(projections, key=lambda p: p["monthly_profit"])
    result["recommendation"] = {
        "price": best["price"],
        "rationale": f"Maximizes monthly profit at ${best['monthly_profit']:,.0f}/mo with {best['margin_pct']}% margin",
    }

    return result


def print_analysis(result):
    """Print formatted pricing analysis."""
    inp = result["inputs"]
    print("=" * 75)
    print(f"  PRICING ANALYSIS")
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d')}")
    print("=" * 75)

    print(f"\n  INPUTS:")
    print(f"    Unit cost:           ${inp['unit_cost']:.2f}")
    print(f"    Target margin:       {inp['target_margin']}%")
    print(f"    Base volume:         {inp['base_volume']:,} units/month")
    if inp["value_delivered"]:
        print(f"    Value delivered:     ${inp['value_delivered']:.2f}/user/month")
    if inp["competitor_avg"]:
        print(f"    Competitor avg:      ${inp['competitor_avg']:.2f}")

    print(f"\n  PRICE ANCHORS:")
    print(f"    Cost-based (floor):  ${result['cost_based_price']:.2f}")
    if result["value_based_range"]["low"]:
        print(f"    Value-based range:   ${result['value_based_range']['low']:.2f} - ${result['value_based_range']['high']:.2f}")

    print(f"\n  SCENARIO PROJECTIONS:")
    print(f"  {'Price':>8} {'Margin':>8} {'Volume':>8} {'Mo Revenue':>12} {'Mo Profit':>12} {'Annual Rev':>12}")
    print(f"  {'─'*8} {'─'*8} {'─'*8} {'─'*12} {'─'*12} {'─'*12}")

    for p in result["projections"]:
        marker = " <-- OPTIMAL" if p["price"] == result["recommendation"]["price"] else ""
        print(f"  ${p['price']:>7} {p['margin_pct']:>7.1f}% {p['est_volume']:>7,} ${p['monthly_revenue']:>11,} ${p['monthly_profit']:>11,} ${p['annual_revenue']:>11,}{marker}")

    rec = result["recommendation"]
    print(f"\n  RECOMMENDATION: ${rec['price']}/unit")
    print(f"  {rec['rationale']}")
    print()


def print_scenarios():
    """Print scenario comparison."""
    print("=" * 70)
    print(f"  PRICING SCENARIO COMPARISON")
    print("=" * 70)
    print(f"\n  {'Scenario':<15} {'Price':>8} {'Volume':>8} {'MRR':>12} {'ARR':>12} {'Churn':>8}")
    print(f"  {'─'*15} {'─'*8} {'─'*8} {'─'*12} {'─'*12} {'─'*8}")

    for s in SAMPLE_SCENARIOS:
        mrr = s["price"] * s["volume"]
        arr = mrr * 12
        print(f"  {s['name']:<15} ${s['price']:>7} {s['volume']:>7,} ${mrr:>11,} ${arr:>11,} {s['churn']:>7.1f}%")

    # LTV comparison
    print(f"\n  LIFETIME VALUE ANALYSIS (at 70% gross margin):")
    print(f"  {'Scenario':<15} {'Monthly Rev':>12} {'Avg Life':>10} {'LTV':>10} {'LTV/Price':>10}")
    print(f"  {'─'*15} {'─'*12} {'─'*10} {'─'*10} {'─'*10}")
    for s in SAMPLE_SCENARIOS:
        avg_life = 1 / (s["churn"] / 100) if s["churn"] > 0 else 120  # months
        ltv = s["price"] * 0.70 * avg_life
        ratio = ltv / s["price"]
        print(f"  {s['name']:<15} ${s['price']:>11} {avg_life:>9.1f}mo ${ltv:>9,.0f} {ratio:>9.1f}x")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Model pricing scenarios with revenue projections.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --cost 15 --target-margin 70 --volume 1000
  %(prog)s --cost 15 --target-margin 70 --volume 1000 --value-delivered 200
  %(prog)s --scenarios
        """,
    )
    parser.add_argument("--cost", type=float, help="Unit cost")
    parser.add_argument("--target-margin", type=float, help="Target margin percentage")
    parser.add_argument("--volume", type=int, help="Expected monthly volume")
    parser.add_argument("--value-delivered", type=float, default=None,
                        help="Economic value delivered to customer per unit/month")
    parser.add_argument("--competitor-avg", type=float, default=None,
                        help="Average competitor price")
    parser.add_argument("--scenarios", action="store_true", help="Show sample scenario comparison")
    parser.add_argument("--format", choices=["text", "json"], default="text")

    args = parser.parse_args()

    if args.scenarios:
        if args.format == "json":
            print(json.dumps(SAMPLE_SCENARIOS, indent=2))
        else:
            print_scenarios()
        return

    if not all([args.cost, args.target_margin, args.volume]):
        parser.error("--cost, --target-margin, and --volume are required (or use --scenarios)")

    result = calculate_pricing(args.cost, args.target_margin, args.volume,
                                args.value_delivered, args.competitor_avg)

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print_analysis(result)


if __name__ == "__main__":
    main()
