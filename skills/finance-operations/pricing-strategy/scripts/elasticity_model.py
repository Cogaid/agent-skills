#!/usr/bin/env python3
"""
Estimate price sensitivity and model revenue at different price points.

Usage:
    python elasticity_model.py --current-price 49 --test-range "29,39,59,79"
    python elasticity_model.py --current-price 49 --current-volume 1000 --elasticity -1.5
"""

import argparse
import json
from datetime import datetime


def estimate_demand(current_price, current_volume, new_price, elasticity):
    """Estimate demand at a new price point using price elasticity."""
    pct_price_change = (new_price - current_price) / current_price
    pct_volume_change = elasticity * pct_price_change
    new_volume = current_volume * (1 + pct_volume_change)
    return max(0, round(new_volume))


def model_elasticity(current_price, current_volume, test_prices, elasticity, cost_per_unit=0):
    """Model revenue and profit at multiple price points."""
    results = []
    current_revenue = current_price * current_volume
    current_profit = (current_price - cost_per_unit) * current_volume

    for price in test_prices:
        volume = estimate_demand(current_price, current_volume, price, elasticity)
        revenue = price * volume
        profit = (price - cost_per_unit) * volume
        revenue_change = (revenue - current_revenue) / current_revenue * 100 if current_revenue else 0
        profit_change = (profit - current_profit) / current_profit * 100 if current_profit else 0

        results.append({
            "price": price,
            "estimated_volume": volume,
            "volume_change_pct": round((volume - current_volume) / current_volume * 100, 1),
            "revenue": round(revenue),
            "revenue_change_pct": round(revenue_change, 1),
            "profit": round(profit),
            "profit_change_pct": round(profit_change, 1),
            "margin_pct": round((price - cost_per_unit) / price * 100, 1) if price > 0 else 0,
        })

    return results


def classify_elasticity(elasticity):
    """Classify the elasticity value."""
    e = abs(elasticity)
    if e < 0.5:
        return "Highly inelastic - strong pricing power, raise prices"
    elif e < 1.0:
        return "Inelastic - moderate pricing power, test higher prices"
    elif e == 1.0:
        return "Unit elastic - price changes offset by volume changes"
    elif e < 2.0:
        return "Elastic - price sensitive market, be cautious with increases"
    else:
        return "Highly elastic - very price sensitive, compete on value not price"


def print_model(results, current_price, current_volume, elasticity, cost_per_unit):
    """Print formatted elasticity model."""
    print("=" * 80)
    print(f"  PRICE ELASTICITY MODEL")
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d')}")
    print("=" * 80)

    print(f"\n  PARAMETERS:")
    print(f"    Current price:    ${current_price:.2f}")
    print(f"    Current volume:   {current_volume:,}/month")
    print(f"    Current revenue:  ${current_price * current_volume:,.0f}/month")
    print(f"    Elasticity:       {elasticity}")
    print(f"    Classification:   {classify_elasticity(elasticity)}")
    if cost_per_unit > 0:
        print(f"    Unit cost:        ${cost_per_unit:.2f}")
        print(f"    Current margin:   {(current_price - cost_per_unit) / current_price * 100:.1f}%")

    print(f"\n  SCENARIO ANALYSIS:")
    print(f"  {'Price':>8} {'Volume':>8} {'Vol %':>8} {'Revenue':>12} {'Rev %':>8} {'Profit':>12} {'Prof %':>8} {'Margin':>8}")
    print(f"  {'─'*8} {'─'*8} {'─'*8} {'─'*12} {'─'*8} {'─'*12} {'─'*8} {'─'*8}")

    best_revenue = max(results, key=lambda r: r["revenue"])
    best_profit = max(results, key=lambda r: r["profit"])

    for r in results:
        rev_marker = " <-R" if r["price"] == best_revenue["price"] else ""
        prof_marker = " <-P" if r["price"] == best_profit["price"] else ""
        current = " (now)" if r["price"] == current_price else ""
        marker = rev_marker or prof_marker or current

        print(f"  ${r['price']:>7} {r['estimated_volume']:>7,} {r['volume_change_pct']:>+7.1f}% ${r['revenue']:>11,} {r['revenue_change_pct']:>+7.1f}% ${r['profit']:>11,} {r['profit_change_pct']:>+7.1f}% {r['margin_pct']:>7.1f}%{marker}")

    print(f"\n  LEGEND: <-R = Max Revenue, <-P = Max Profit")

    print(f"\n  RECOMMENDATIONS:")
    if best_revenue["price"] != current_price:
        print(f"    Revenue-optimal price: ${best_revenue['price']} (${best_revenue['revenue']:,}/mo, {best_revenue['revenue_change_pct']:+.1f}% vs current)")
    if best_profit["price"] != current_price:
        print(f"    Profit-optimal price:  ${best_profit['price']} (${best_profit['profit']:,}/mo, {best_profit['profit_change_pct']:+.1f}% vs current)")

    # Sensitivity warning
    if abs(elasticity) > 1.5:
        print(f"\n  WARNING: High elasticity ({elasticity}) means the market is very price-sensitive.")
        print(f"  Consider investing in differentiation before raising prices.")
    elif abs(elasticity) < 0.8:
        print(f"\n  OPPORTUNITY: Low elasticity ({elasticity}) suggests you have pricing power.")
        print(f"  Test a 10-20% price increase with new customers.")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Model price sensitivity and revenue impact.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --current-price 49 --test-range "29,39,59,79"
  %(prog)s --current-price 49 --current-volume 1000 --elasticity -1.5
  %(prog)s --current-price 99 --test-range "79,89,109,129" --cost 20
        """,
    )
    parser.add_argument("--current-price", type=float, required=True, help="Current price per unit")
    parser.add_argument("--current-volume", type=int, default=1000, help="Current monthly volume (default: 1000)")
    parser.add_argument("--elasticity", type=float, default=-1.2,
                        help="Price elasticity of demand (negative number, default: -1.2)")
    parser.add_argument("--test-range", default=None,
                        help="Comma-separated price points to test")
    parser.add_argument("--cost", type=float, default=0, help="Cost per unit (default: 0)")
    parser.add_argument("--format", choices=["text", "json"], default="text")

    args = parser.parse_args()

    if args.test_range:
        test_prices = sorted([float(p.strip()) for p in args.test_range.split(",")])
    else:
        # Auto-generate test range
        base = args.current_price
        test_prices = sorted([
            round(base * 0.6), round(base * 0.8), round(base * 0.9),
            round(base), round(base * 1.1), round(base * 1.25),
            round(base * 1.5), round(base * 2.0),
        ])

    # Ensure current price is in the list
    if args.current_price not in test_prices:
        test_prices.append(args.current_price)
        test_prices.sort()

    results = model_elasticity(args.current_price, args.current_volume,
                                test_prices, args.elasticity, args.cost)

    if args.format == "json":
        output = {
            "current_price": args.current_price,
            "current_volume": args.current_volume,
            "elasticity": args.elasticity,
            "classification": classify_elasticity(args.elasticity),
            "scenarios": results,
        }
        print(json.dumps(output, indent=2))
    else:
        print_model(results, args.current_price, args.current_volume,
                    args.elasticity, args.cost)


if __name__ == "__main__":
    main()
