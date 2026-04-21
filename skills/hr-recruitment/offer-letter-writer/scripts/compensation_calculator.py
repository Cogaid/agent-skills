#!/usr/bin/env python3
"""
Compensation Calculator

Calculates total compensation packages, compares offers side-by-side,
and models negotiation scenarios. Outputs structured JSON with total comp
breakdowns.

Usage:
    python compensation_calculator.py --demo
    python compensation_calculator.py --base 180000 --bonus-pct 15 --equity-value 200000 --signing 25000
    python compensation_calculator.py --compare offer1.json offer2.json
"""

import argparse
import json
import sys


def calculate_total_comp(
    base_salary,
    bonus_pct=0,
    equity_total_value=0,
    equity_vest_years=4,
    signing_bonus=0,
    benefits_value=25000,
    other_annual=0,
):
    """Calculate total compensation over 1 year and 4 years."""
    annual_bonus = base_salary * (bonus_pct / 100)
    annual_equity = equity_total_value / equity_vest_years if equity_vest_years > 0 else 0

    year1_total = base_salary + annual_bonus + annual_equity + signing_bonus + benefits_value + other_annual
    annual_ongoing = base_salary + annual_bonus + annual_equity + benefits_value + other_annual
    four_year_total = (base_salary * 4) + (annual_bonus * 4) + equity_total_value + signing_bonus + (benefits_value * 4) + (other_annual * 4)

    return {
        "components": {
            "base_salary": base_salary,
            "annual_bonus_target": round(annual_bonus),
            "bonus_percentage": bonus_pct,
            "equity_total_value": equity_total_value,
            "equity_annual_value": round(annual_equity),
            "equity_vest_years": equity_vest_years,
            "signing_bonus": signing_bonus,
            "benefits_value": benefits_value,
            "other_annual": other_annual,
        },
        "totals": {
            "year_1_total": round(year1_total),
            "annual_ongoing": round(annual_ongoing),
            "four_year_total": round(four_year_total),
        },
        "breakdown_year_1": {
            "base_salary": base_salary,
            "bonus": round(annual_bonus),
            "equity": round(annual_equity),
            "signing_bonus": signing_bonus,
            "benefits": benefits_value,
            "other": other_annual,
            "total": round(year1_total),
        },
    }


def compare_offers(offer_a, offer_b):
    """Compare two compensation packages side by side."""
    comp_a = calculate_total_comp(**offer_a["compensation"])
    comp_b = calculate_total_comp(**offer_b["compensation"])

    comparison = {
        "offer_a": {
            "name": offer_a.get("name", "Offer A"),
            "role": offer_a.get("role", "Unknown"),
            "compensation": comp_a,
        },
        "offer_b": {
            "name": offer_b.get("name", "Offer B"),
            "role": offer_b.get("role", "Unknown"),
            "compensation": comp_b,
        },
        "gaps": {
            "year_1": comp_a["totals"]["year_1_total"] - comp_b["totals"]["year_1_total"],
            "annual_ongoing": comp_a["totals"]["annual_ongoing"] - comp_b["totals"]["annual_ongoing"],
            "four_year": comp_a["totals"]["four_year_total"] - comp_b["totals"]["four_year_total"],
            "base_salary": offer_a["compensation"]["base_salary"] - offer_b["compensation"]["base_salary"],
        },
        "winner": {},
    }

    for metric in ["year_1", "annual_ongoing", "four_year"]:
        gap = comparison["gaps"][metric]
        if gap > 0:
            comparison["winner"][metric] = offer_a.get("name", "Offer A")
        elif gap < 0:
            comparison["winner"][metric] = offer_b.get("name", "Offer B")
        else:
            comparison["winner"][metric] = "Tie"

    return comparison


def model_negotiation(base_offer, scenarios):
    """Model different negotiation scenarios."""
    base_comp = calculate_total_comp(**base_offer)
    results = {
        "base_offer": base_comp,
        "scenarios": [],
    }

    for scenario in scenarios:
        adjusted = base_offer.copy()
        adjusted.update(scenario.get("adjustments", {}))
        adjusted_comp = calculate_total_comp(**adjusted)

        delta_year1 = adjusted_comp["totals"]["year_1_total"] - base_comp["totals"]["year_1_total"]
        delta_4year = adjusted_comp["totals"]["four_year_total"] - base_comp["totals"]["four_year_total"]

        results["scenarios"].append({
            "name": scenario.get("name", "Scenario"),
            "adjustments": scenario.get("adjustments", {}),
            "result": adjusted_comp,
            "delta_year_1": delta_year1,
            "delta_four_year": delta_4year,
            "delta_year_1_pct": round(delta_year1 / base_comp["totals"]["year_1_total"] * 100, 1) if base_comp["totals"]["year_1_total"] > 0 else 0,
        })

    return results


# --- Demo Data ---

DEMO_OFFER_A = {
    "name": "Our Offer",
    "role": "Senior Software Engineer",
    "compensation": {
        "base_salary": 185000,
        "bonus_pct": 15,
        "equity_total_value": 200000,
        "equity_vest_years": 4,
        "signing_bonus": 25000,
        "benefits_value": 28000,
        "other_annual": 2000,
    },
}

DEMO_OFFER_B = {
    "name": "Competing Offer (BigTech Corp)",
    "role": "Senior Software Engineer",
    "compensation": {
        "base_salary": 200000,
        "bonus_pct": 15,
        "equity_total_value": 300000,
        "equity_vest_years": 4,
        "signing_bonus": 50000,
        "benefits_value": 25000,
        "other_annual": 0,
    },
}

DEMO_SCENARIOS = [
    {
        "name": "Increase base by 10%",
        "adjustments": {"base_salary": 203500},
    },
    {
        "name": "Match signing bonus",
        "adjustments": {"signing_bonus": 50000},
    },
    {
        "name": "Increase equity by 50%",
        "adjustments": {"equity_total_value": 300000},
    },
    {
        "name": "Combined: base +5%, signing match, equity +25%",
        "adjustments": {
            "base_salary": 194250,
            "signing_bonus": 50000,
            "equity_total_value": 250000,
        },
    },
]


def print_summary(data, mode):
    """Print human-readable summary."""
    if mode == "calculate":
        comp = data
        print("=== TOTAL COMPENSATION SUMMARY ===")
        print(f"")
        print(f"{'Component':<30} {'Annual':<15} {'4-Year':<15}")
        print(f"{'-'*60}")
        b = comp["components"]
        print(f"{'Base Salary':<30} ${b['base_salary']:>12,}  ${b['base_salary']*4:>12,}")
        print(f"{'Annual Bonus ({b[\"bonus_percentage\"]}%)':<30} ${b['annual_bonus_target']:>12,}  ${b['annual_bonus_target']*4:>12,}")
        print(f"{'Equity':<30} ${b['equity_annual_value']:>12,}  ${b['equity_total_value']:>12,}")
        print(f"{'Signing Bonus':<30} ${b['signing_bonus']:>12,}  ${b['signing_bonus']:>12,}")
        print(f"{'Benefits':<30} ${b['benefits_value']:>12,}  ${b['benefits_value']*4:>12,}")
        if b["other_annual"]:
            print(f"{'Other':<30} ${b['other_annual']:>12,}  ${b['other_annual']*4:>12,}")
        print(f"{'-'*60}")
        t = comp["totals"]
        print(f"{'YEAR 1 TOTAL':<30} ${t['year_1_total']:>12,}")
        print(f"{'ANNUAL ONGOING':<30} ${t['annual_ongoing']:>12,}")
        print(f"{'4-YEAR TOTAL':<30} {'':>15}${t['four_year_total']:>12,}")

    elif mode == "compare":
        a = data["offer_a"]
        b = data["offer_b"]
        gaps = data["gaps"]
        print("=== OFFER COMPARISON ===")
        print(f"")
        print(f"{'Metric':<25} {a['name']:<18} {b['name']:<18} {'Gap':<15}")
        print(f"{'-'*76}")
        print(f"{'Base Salary':<25} ${a['compensation']['components']['base_salary']:>15,} ${b['compensation']['components']['base_salary']:>15,} ${gaps['base_salary']:>+12,}")
        print(f"{'Year 1 Total':<25} ${a['compensation']['totals']['year_1_total']:>15,} ${b['compensation']['totals']['year_1_total']:>15,} ${gaps['year_1']:>+12,}")
        print(f"{'Annual Ongoing':<25} ${a['compensation']['totals']['annual_ongoing']:>15,} ${b['compensation']['totals']['annual_ongoing']:>15,} ${gaps['annual_ongoing']:>+12,}")
        print(f"{'4-Year Total':<25} ${a['compensation']['totals']['four_year_total']:>15,} ${b['compensation']['totals']['four_year_total']:>15,} ${gaps['four_year']:>+12,}")
        print(f"")
        print(f"Winner by Year 1: {data['winner']['year_1']}")
        print(f"Winner by 4-Year: {data['winner']['four_year']}")

    elif mode == "negotiate":
        print("=== NEGOTIATION SCENARIOS ===")
        base_y1 = data["base_offer"]["totals"]["year_1_total"]
        print(f"Base Offer Year 1: ${base_y1:,}")
        print()
        for s in data["scenarios"]:
            print(f"  {s['name']}:")
            print(f"    Year 1: ${s['result']['totals']['year_1_total']:,} ({s['delta_year_1_pct']:+.1f}%)")
            print(f"    4-Year: ${s['result']['totals']['four_year_total']:,} (delta: ${s['delta_four_year']:+,})")
            print()


def main():
    parser = argparse.ArgumentParser(
        description="Calculate and compare compensation packages."
    )
    subparsers = parser.add_subparsers(dest="command")

    # Calculate subcommand
    calc_parser = subparsers.add_parser("calculate", help="Calculate total compensation")
    calc_parser.add_argument("--base", type=int, required=True, help="Base salary")
    calc_parser.add_argument("--bonus-pct", type=float, default=0, help="Annual bonus as % of base")
    calc_parser.add_argument("--equity-value", type=int, default=0, help="Total equity value over vest period")
    calc_parser.add_argument("--equity-years", type=int, default=4, help="Equity vesting period in years")
    calc_parser.add_argument("--signing", type=int, default=0, help="Signing bonus")
    calc_parser.add_argument("--benefits", type=int, default=25000, help="Annual benefits value")
    calc_parser.add_argument("--other", type=int, default=0, help="Other annual compensation")

    # Compare subcommand
    compare_parser = subparsers.add_parser("compare", help="Compare two offers")
    compare_parser.add_argument("offer_a", help="Path to first offer JSON")
    compare_parser.add_argument("offer_b", help="Path to second offer JSON")

    # Demo subcommand
    subparsers.add_parser("demo", help="Run demo with sample data")

    parser.add_argument("--format", choices=["json", "summary"], default="json", help="Output format")
    # Also support --demo at top level for convenience
    parser.add_argument("--demo", action="store_true", help="Run demo with sample data")

    args = parser.parse_args()

    if args.demo or args.command == "demo":
        # Run all three demo modes
        print("--- Offer Calculation ---") if args.format == "summary" else None
        comp = calculate_total_comp(**DEMO_OFFER_A["compensation"])

        comparison = compare_offers(DEMO_OFFER_A, DEMO_OFFER_B)

        negotiation = model_negotiation(DEMO_OFFER_A["compensation"], DEMO_SCENARIOS)

        if args.format == "summary":
            print_summary(comp, "calculate")
            print("\n")
            print_summary(comparison, "compare")
            print("\n")
            print_summary(negotiation, "negotiate")
        else:
            output = {
                "calculation": comp,
                "comparison": comparison,
                "negotiation_scenarios": negotiation,
            }
            print(json.dumps(output, indent=2))

    elif args.command == "calculate":
        comp = calculate_total_comp(
            base_salary=args.base,
            bonus_pct=args.bonus_pct,
            equity_total_value=args.equity_value,
            equity_vest_years=args.equity_years,
            signing_bonus=args.signing,
            benefits_value=args.benefits,
            other_annual=args.other,
        )
        if args.format == "summary":
            print_summary(comp, "calculate")
        else:
            print(json.dumps(comp, indent=2))

    elif args.command == "compare":
        try:
            with open(args.offer_a) as f:
                offer_a = json.load(f)
            with open(args.offer_b) as f:
                offer_b = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(json.dumps({"error": str(e)}))
            sys.exit(1)

        result = compare_offers(offer_a, offer_b)
        if args.format == "summary":
            print_summary(result, "compare")
        else:
            print(json.dumps(result, indent=2))

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
