#!/usr/bin/env python3
"""Run sensitivity analysis on a completed decision matrix.

Usage:
    python sensitivity_check.py --matrix matrix.json --scenarios all
    python sensitivity_check.py --example --format json
"""

import argparse
import json
import sys
from datetime import datetime

SAMPLE_MATRIX = {
    "decision": "Which project management tool should we adopt?",
    "criteria": [
        {"name": "Ease of use", "weight": 25},
        {"name": "Integration", "weight": 20},
        {"name": "Cost", "weight": 20},
        {"name": "Customization", "weight": 20},
        {"name": "Support/Docs", "weight": 15},
    ],
    "options": [
        {"name": "Jira", "scores": [3, 5, 3, 5, 4]},
        {"name": "Linear", "scores": [5, 4, 4, 3, 3]},
        {"name": "Asana", "scores": [4, 3, 4, 4, 5]},
    ],
}


def calc_total(scores: list, weights: list) -> float:
    return round(sum(s * (w / 100.0) for s, w in zip(scores, weights)), 2)


def get_winner(matrix: dict, weights: list = None) -> tuple:
    if weights is None:
        weights = [c["weight"] for c in matrix["criteria"]]
    totals = []
    for opt in matrix["options"]:
        totals.append((opt["name"], calc_total(opt["scores"], weights)))
    totals.sort(key=lambda x: x[1], reverse=True)
    return totals


def weight_sensitivity(matrix: dict, shift: int = 10) -> list:
    """Test decision robustness by shifting each criterion's weight."""
    base_weights = [c["weight"] for c in matrix["criteria"]]
    base_ranking = get_winner(matrix)
    base_winner = base_ranking[0][0]
    scenarios = []

    for i, criterion in enumerate(matrix["criteria"]):
        for direction in [+shift, -shift]:
            new_weights = base_weights.copy()
            new_weights[i] = max(0, new_weights[i] + direction)
            # Redistribute the shift proportionally among other criteria
            diff = sum(new_weights) - 100
            if diff != 0:
                others = [j for j in range(len(new_weights)) if j != i and new_weights[j] > 0]
                per_other = diff / len(others) if others else 0
                for j in others:
                    new_weights[j] = max(0, round(new_weights[j] - per_other, 1))

            ranking = get_winner(matrix, new_weights)
            winner = ranking[0][0]
            gap = round(ranking[0][1] - ranking[1][1], 2)

            scenarios.append({
                "criterion": criterion["name"],
                "direction": f"+{direction}" if direction > 0 else str(direction),
                "new_weight": new_weights[i],
                "winner": winner,
                "gap": gap,
                "winner_changed": winner != base_winner,
            })

    return scenarios


def score_sensitivity(matrix: dict) -> list:
    """Test if runner-up could win with +1 on its weakest criterion."""
    base_ranking = get_winner(matrix)
    base_winner_name = base_ranking[0][0]
    runner_up_name = base_ranking[1][0]

    runner_up = next(o for o in matrix["options"] if o["name"] == runner_up_name)
    winner = next(o for o in matrix["options"] if o["name"] == base_winner_name)
    weights = [c["weight"] for c in matrix["criteria"]]

    scenarios = []

    # Runner-up improves weakest score
    weakest_idx = runner_up["scores"].index(min(runner_up["scores"]))
    new_scores = runner_up["scores"].copy()
    new_scores[weakest_idx] = min(5, new_scores[weakest_idx] + 1)
    new_total = calc_total(new_scores, weights)
    winner_total = calc_total(winner["scores"], weights)

    scenarios.append({
        "scenario": f"{runner_up_name} improves '{matrix['criteria'][weakest_idx]['name']}' by +1",
        "original_score": runner_up["scores"][weakest_idx],
        "new_score": new_scores[weakest_idx],
        "new_total": new_total,
        "winner_total": winner_total,
        "winner_changed": new_total > winner_total,
    })

    # Winner's weakest score drops by 1
    weakest_idx_w = winner["scores"].index(min(winner["scores"]))
    new_scores_w = winner["scores"].copy()
    new_scores_w[weakest_idx_w] = max(1, new_scores_w[weakest_idx_w] - 1)
    new_total_w = calc_total(new_scores_w, weights)
    runner_total = calc_total(runner_up["scores"], weights)

    scenarios.append({
        "scenario": f"{base_winner_name} drops '{matrix['criteria'][weakest_idx_w]['name']}' by -1",
        "original_score": winner["scores"][weakest_idx_w],
        "new_score": new_scores_w[weakest_idx_w],
        "new_total": new_total_w,
        "runner_up_total": runner_total,
        "winner_changed": new_total_w < runner_total,
    })

    return scenarios


def main():
    parser = argparse.ArgumentParser(description="Run sensitivity analysis on a decision matrix.")
    parser.add_argument("--matrix", help="Path to matrix JSON file")
    parser.add_argument("--scenarios", choices=["weight", "score", "all"], default="all", help="Which scenarios to run")
    parser.add_argument("--shift", type=int, default=10, help="Weight shift percentage for sensitivity (default: 10)")
    parser.add_argument("--example", action="store_true", help="Run with example data")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format")

    args = parser.parse_args()

    if args.matrix:
        with open(args.matrix) as f:
            matrix = json.load(f)
    else:
        matrix = SAMPLE_MATRIX

    results = {"decision": matrix["decision"], "analyzed_at": datetime.now().isoformat()}

    base_ranking = get_winner(matrix)
    results["base_case"] = {
        "winner": base_ranking[0][0],
        "score": base_ranking[0][1],
        "runner_up": base_ranking[1][0],
        "runner_up_score": base_ranking[1][1],
        "gap": round(base_ranking[0][1] - base_ranking[1][1], 2),
    }

    if args.scenarios in ("weight", "all"):
        results["weight_sensitivity"] = weight_sensitivity(matrix, args.shift)
    if args.scenarios in ("score", "all"):
        results["score_sensitivity"] = score_sensitivity(matrix)

    # Overall assessment
    any_weight_flip = any(s.get("winner_changed") for s in results.get("weight_sensitivity", []))
    any_score_flip = any(s.get("winner_changed") for s in results.get("score_sensitivity", []))

    if not any_weight_flip and not any_score_flip:
        results["overall"] = "ROBUST - Decision holds across all tested scenarios"
    elif any_weight_flip and any_score_flip:
        results["overall"] = "SENSITIVE - Decision changes under weight AND score variations. Gather more evidence."
    else:
        results["overall"] = "MODERATELY ROBUST - Decision changes under some scenarios. Review flagged cases."

    if args.format == "json":
        print(json.dumps(results, indent=2))
    else:
        print(f"Sensitivity Analysis: {results['decision']}")
        print("=" * 60)
        bc = results["base_case"]
        print(f"\nBase Case: {bc['winner']} ({bc['score']}) vs {bc['runner_up']} ({bc['runner_up_score']})")
        print(f"Gap: {bc['gap']} points")

        if "weight_sensitivity" in results:
            print(f"\nWeight Sensitivity (+/- {args.shift}%):")
            print("-" * 60)
            for s in results["weight_sensitivity"]:
                flag = " *** FLIP ***" if s["winner_changed"] else ""
                print(f"  {s['criterion']} {s['direction']}% -> Winner: {s['winner']} (gap: {s['gap']}){flag}")

        if "score_sensitivity" in results:
            print(f"\nScore Sensitivity:")
            print("-" * 60)
            for s in results["score_sensitivity"]:
                flag = " *** FLIP ***" if s["winner_changed"] else ""
                print(f"  {s['scenario']}{flag}")

        print(f"\nOverall: {results['overall']}")
        print("=" * 60)


if __name__ == "__main__":
    main()
