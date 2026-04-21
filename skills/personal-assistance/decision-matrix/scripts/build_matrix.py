#!/usr/bin/env python3
"""Create and calculate a weighted decision matrix.

Usage:
    python build_matrix.py --criteria 5 --options 3 --interactive
    python build_matrix.py --example --format json
    python build_matrix.py --from-file matrix.json
"""

import argparse
import json
import sys
from datetime import datetime

SAMPLE_MATRIX = {
    "decision": "Which project management tool should we adopt?",
    "date": "2025-01-15",
    "decision_maker": "Engineering Team",
    "criteria": [
        {"name": "Ease of use", "weight": 25, "rationale": "Team adoption depends on low friction"},
        {"name": "Integration", "weight": 20, "rationale": "Must connect with GitHub, Slack, CI/CD"},
        {"name": "Cost", "weight": 20, "rationale": "Budget constraint of $50/user/month"},
        {"name": "Customization", "weight": 20, "rationale": "Need custom workflows for our process"},
        {"name": "Support/Docs", "weight": 15, "rationale": "Small team, need good self-service resources"},
    ],
    "options": [
        {
            "name": "Tool A (Jira)",
            "scores": [3, 5, 3, 5, 4],
        },
        {
            "name": "Tool B (Linear)",
            "scores": [5, 4, 4, 3, 3],
        },
        {
            "name": "Tool C (Asana)",
            "scores": [4, 3, 4, 4, 5],
        },
    ],
}


def calculate_matrix(matrix: dict) -> dict:
    """Calculate weighted scores and rankings."""
    criteria = matrix["criteria"]
    options = matrix["options"]
    results = []

    for option in options:
        weighted_scores = []
        total = 0.0
        for i, criterion in enumerate(criteria):
            raw = option["scores"][i]
            weight = criterion["weight"] / 100.0
            weighted = round(raw * weight, 2)
            weighted_scores.append({
                "criterion": criterion["name"],
                "weight": criterion["weight"],
                "raw_score": raw,
                "weighted_score": weighted,
            })
            total += weighted
        results.append({
            "option": option["name"],
            "weighted_scores": weighted_scores,
            "total": round(total, 2),
        })

    results.sort(key=lambda x: x["total"], reverse=True)
    for rank, r in enumerate(results, 1):
        r["rank"] = rank

    winner = results[0]
    runner_up = results[1] if len(results) > 1 else None
    margin = round(winner["total"] - runner_up["total"], 2) if runner_up else 0

    if margin > 0.5:
        confidence = "High"
    elif margin > 0.2:
        confidence = "Medium"
    else:
        confidence = "Low"

    return {
        "decision": matrix["decision"],
        "date": matrix["date"],
        "calculated_at": datetime.now().isoformat(),
        "criteria": criteria,
        "results": results,
        "recommendation": {
            "winner": winner["option"],
            "score": winner["total"],
            "runner_up": runner_up["option"] if runner_up else None,
            "runner_up_score": runner_up["total"] if runner_up else None,
            "margin": margin,
            "confidence": confidence,
        },
    }


def display_text(result: dict) -> None:
    """Display matrix results in text format."""
    print(f"Decision Matrix: {result['decision']}")
    print(f"Date: {result['date']}")
    print("=" * 70)

    criteria = result["criteria"]
    print(f"\nCriteria and Weights:")
    for c in criteria:
        print(f"  {c['name']:20s} {c['weight']:3d}%  ({c['rationale']})")

    print(f"\nScores and Rankings:")
    print("-" * 70)

    header = f"  {'Criterion':20s} {'Weight':>6s}"
    for r in result["results"]:
        header += f"  {r['option'][:15]:>15s}"
    print(header)
    print("-" * 70)

    for i, c in enumerate(criteria):
        row = f"  {c['name']:20s} {c['weight']:5d}%"
        for r in result["results"]:
            ws = r["weighted_scores"][i]
            row += f"  {ws['raw_score']}x{ws['weight']}%={ws['weighted_score']:5.2f}"
        print(row)

    print("-" * 70)
    total_row = f"  {'TOTAL':20s} {'':>6s}"
    for r in result["results"]:
        total_row += f"        {r['total']:>7.2f}"
    print(total_row)

    rank_row = f"  {'RANK':20s} {'':>6s}"
    for r in result["results"]:
        rank_row += f"        #{r['rank']:>5d}"
    print(rank_row)

    rec = result["recommendation"]
    print(f"\nRecommendation: {rec['winner']}")
    print(f"  Score: {rec['score']} (vs. {rec['runner_up']}: {rec['runner_up_score']})")
    print(f"  Margin: {rec['margin']} points")
    print(f"  Confidence: {rec['confidence']}")
    print("=" * 70)


def main():
    parser = argparse.ArgumentParser(description="Create and calculate a weighted decision matrix.")
    parser.add_argument("--criteria", type=int, help="Number of criteria")
    parser.add_argument("--options", type=int, help="Number of options")
    parser.add_argument("--interactive", action="store_true", help="Interactive guided mode (uses sample for demo)")
    parser.add_argument("--example", action="store_true", help="Run with example data")
    parser.add_argument("--from-file", help="Load matrix from JSON file")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format")

    args = parser.parse_args()

    if args.from_file:
        with open(args.from_file) as f:
            matrix = json.load(f)
    else:
        matrix = SAMPLE_MATRIX

    result = calculate_matrix(matrix)

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        display_text(result)


if __name__ == "__main__":
    main()
