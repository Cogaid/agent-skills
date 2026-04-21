#!/usr/bin/env python3
"""
Run weighted vendor scoring analysis with rankings.

Usage:
    python evaluate_vendor.py --vendors "vendorA,vendorB,vendorC" --criteria criteria.json
    python evaluate_vendor.py --demo
    python evaluate_vendor.py --demo --format json
"""

import argparse
import json
from datetime import datetime
from pathlib import Path

DEFAULT_CRITERIA = [
    {"name": "Feature coverage", "weight": 20},
    {"name": "Integration", "weight": 10},
    {"name": "Ease of use", "weight": 10},
    {"name": "Implementation effort", "weight": 5},
    {"name": "Uptime / SLA", "weight": 10},
    {"name": "Security & compliance", "weight": 10},
    {"name": "Support quality", "weight": 5},
    {"name": "Documentation", "weight": 5},
    {"name": "Price / value", "weight": 15},
    {"name": "Financial stability", "weight": 5},
    {"name": "Roadmap alignment", "weight": 5},
]

SAMPLE_SCORES = {
    "CloudPlatform Pro": {
        "Feature coverage": 5, "Integration": 4, "Ease of use": 4,
        "Implementation effort": 3, "Uptime / SLA": 5, "Security & compliance": 5,
        "Support quality": 4, "Documentation": 4, "Price / value": 3,
        "Financial stability": 5, "Roadmap alignment": 4,
        "deal_breakers": {"SOC 2": True, "SSO": True, "API": True, "Data residency": True},
    },
    "AgileTools Inc": {
        "Feature coverage": 4, "Integration": 5, "Ease of use": 5,
        "Implementation effort": 4, "Uptime / SLA": 4, "Security & compliance": 3,
        "Support quality": 5, "Documentation": 5, "Price / value": 4,
        "Financial stability": 3, "Roadmap alignment": 4,
        "deal_breakers": {"SOC 2": True, "SSO": False, "API": True, "Data residency": True},
    },
    "BudgetSoft": {
        "Feature coverage": 3, "Integration": 3, "Ease of use": 4,
        "Implementation effort": 5, "Uptime / SLA": 3, "Security & compliance": 2,
        "Support quality": 3, "Documentation": 3, "Price / value": 5,
        "Financial stability": 2, "Roadmap alignment": 3,
        "deal_breakers": {"SOC 2": False, "SSO": False, "API": True, "Data residency": False},
    },
}


def calculate_weighted_scores(criteria, vendor_scores):
    """Calculate weighted scores for all vendors."""
    results = {}
    for vendor, scores in vendor_scores.items():
        weighted_total = 0
        total_weight = 0
        details = []
        for criterion in criteria:
            name = criterion["name"]
            weight = criterion["weight"]
            score = scores.get(name, 0)
            weighted = score * weight / 100
            weighted_total += weighted
            total_weight += weight
            details.append({
                "criterion": name,
                "weight": weight,
                "score": score,
                "weighted": round(weighted, 2),
            })

        # Check deal-breakers
        deal_breakers = scores.get("deal_breakers", {})
        failed_dbs = [k for k, v in deal_breakers.items() if not v]

        results[vendor] = {
            "weighted_score": round(weighted_total, 2),
            "max_score": 5.0,
            "details": details,
            "deal_breakers": deal_breakers,
            "failed_deal_breakers": failed_dbs,
            "eliminated": len(failed_dbs) > 0,
        }

    return results


def print_evaluation(results, criteria):
    """Print formatted evaluation."""
    print("=" * 85)
    print(f"  VENDOR EVALUATION SCORECARD")
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d')}")
    print("=" * 85)

    vendors = list(results.keys())

    # Header
    header = f"  {'Criteria':<24} {'Wt':>4}"
    for v in vendors:
        short = v[:15]
        header += f"  {'Score':>5} {'Wtd':>5}"
    print(f"\n{header}")

    separator = f"  {'─'*24} {'─'*4}"
    for _ in vendors:
        separator += f"  {'─'*5} {'─'*5}"
    print(separator)

    # Rows
    for criterion in criteria:
        row = f"  {criterion['name']:<24} {criterion['weight']:>3}%"
        for v in vendors:
            detail = next(d for d in results[v]["details"] if d["criterion"] == criterion["name"])
            row += f"  {detail['score']:>5} {detail['weighted']:>5.2f}"
        print(row)

    # Totals
    print(separator)
    total_row = f"  {'WEIGHTED TOTAL':<24} {'100':>4}"
    for v in vendors:
        total_row += f"        {results[v]['weighted_score']:>5.2f}"
    print(total_row)

    # Deal-breaker check
    print(f"\n  DEAL-BREAKER CHECK:")
    all_dbs = set()
    for v in vendors:
        all_dbs.update(results[v]["deal_breakers"].keys())

    for db in sorted(all_dbs):
        row = f"    {db:<24}"
        for v in vendors:
            passed = results[v]["deal_breakers"].get(db)
            row += f"  {'PASS' if passed else 'FAIL':>8}"
        print(row)

    # Rankings
    ranked = sorted(vendors, key=lambda v: (not results[v]["eliminated"], results[v]["weighted_score"]), reverse=True)

    print(f"\n  RANKINGS:")
    print(f"  {'─'*60}")
    for i, v in enumerate(ranked, 1):
        r = results[v]
        status = "ELIMINATED (deal-breaker)" if r["eliminated"] else ""
        if r["eliminated"]:
            status += f" [{', '.join(r['failed_deal_breakers'])}]"
        print(f"  #{i}  {v:<25} {r['weighted_score']:.2f}/5.00  {status}")

    # Recommendation
    eligible = [v for v in ranked if not results[v]["eliminated"]]
    if eligible:
        winner = eligible[0]
        print(f"\n  RECOMMENDATION: {winner}")
        print(f"  Score: {results[winner]['weighted_score']:.2f}/5.00")
        if len(eligible) > 1:
            runner = eligible[1]
            gap = results[winner]["weighted_score"] - results[runner]["weighted_score"]
            print(f"  Lead over runner-up ({runner}): {gap:.2f} points")
    else:
        print(f"\n  WARNING: All vendors failed at least one deal-breaker requirement.")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Run weighted vendor scoring analysis.",
    )
    parser.add_argument("--vendors", default=None, help="Comma-separated vendor names")
    parser.add_argument("--criteria", default=None, help="Criteria JSON file path")
    parser.add_argument("--demo", action="store_true", help="Use sample data")
    parser.add_argument("--format", choices=["text", "json"], default="text")

    args = parser.parse_args()

    if args.criteria and Path(args.criteria).exists():
        with open(args.criteria) as f:
            criteria = json.load(f)
    else:
        criteria = DEFAULT_CRITERIA

    if args.demo or not args.vendors:
        vendor_scores = SAMPLE_SCORES
    else:
        # In production, would load scores from a file or database
        vendor_scores = SAMPLE_SCORES

    results = calculate_weighted_scores(criteria, vendor_scores)

    if args.format == "json":
        print(json.dumps(results, indent=2))
    else:
        print_evaluation(results, criteria)


if __name__ == "__main__":
    main()
