#!/usr/bin/env python3
"""Analyze A/B test results for canned response templates.

Usage:
    python scripts/ab_test_report.py --test-id ABT-042 --metric csat
    python scripts/ab_test_report.py --test-id ABT-042 --metric resolution_rate --confidence 0.95
    python scripts/ab_test_report.py --list-active
"""

import argparse
import json
import math
import random
import sys
from datetime import datetime, timedelta

random.seed(42)

# Sample active A/B tests
ACTIVE_TESTS = [
    {
        "test_id": "ABT-042",
        "template_id": "GREET-001",
        "name": "Empathy-first vs Action-first Opening",
        "hypothesis": "Leading with empathy before action will increase CSAT",
        "started": "2024-02-01",
        "status": "running",
        "variant_a": "Standard greeting (action-first)",
        "variant_b": "Empathy-first greeting",
        "change_tested": "Added 'I understand how frustrating this must be' before stating next steps",
    },
    {
        "test_id": "ABT-043",
        "template_id": "TRBL-001",
        "name": "Numbered Steps vs Bullet Points",
        "hypothesis": "Numbered steps will reduce follow-up questions",
        "started": "2024-02-10",
        "status": "running",
        "variant_a": "Bullet point format",
        "variant_b": "Numbered steps with bold actions",
        "change_tested": "Changed formatting from bullets to numbered steps with bold action verbs",
    },
    {
        "test_id": "ABT-044",
        "template_id": "CLOS-001",
        "name": "Question Close vs Statement Close",
        "hypothesis": "Ending with a question reduces ticket reopen rate",
        "started": "2024-02-15",
        "status": "complete",
        "variant_a": "Statement close ('Have a great day!')",
        "variant_b": "Question close ('Is there anything else I can help with?')",
        "change_tested": "Changed closing from statement to open-ended question",
    },
]


def simulate_test_results(test_id, primary_metric):
    """Simulate A/B test results with realistic data."""
    test = next((t for t in ACTIVE_TESTS if t["test_id"] == test_id), None)
    if not test:
        return {"error": f"Test {test_id} not found"}

    # Simulate results based on metric
    n_a = random.randint(200, 500)
    n_b = random.randint(200, 500)

    metric_configs = {
        "csat": {"base_a": 4.2, "lift": 0.15, "std": 0.8, "scale": "1-5"},
        "resolution_rate": {"base_a": 0.78, "lift": 0.04, "std": 0.12, "scale": "0-1"},
        "reopen_rate": {"base_a": 0.12, "lift": -0.03, "std": 0.08, "scale": "0-1"},
        "reply_rate": {"base_a": 0.65, "lift": 0.05, "std": 0.15, "scale": "0-1"},
        "handle_time": {"base_a": 8.5, "lift": -0.8, "std": 3.2, "scale": "minutes"},
    }

    config = metric_configs.get(primary_metric, metric_configs["csat"])

    # Generate variant A results
    mean_a = config["base_a"]
    mean_b = config["base_a"] + config["lift"]
    std = config["std"]

    # Simulate means with some randomness
    observed_a = mean_a + random.uniform(-0.05, 0.05)
    observed_b = mean_b + random.uniform(-0.08, 0.08)

    return {
        "test_info": test,
        "primary_metric": primary_metric,
        "variant_a": {
            "label": "Control",
            "description": test["variant_a"],
            "sample_size": n_a,
            "metric_value": round(observed_a, 3),
            "std_dev": round(std + random.uniform(-0.05, 0.05), 3),
        },
        "variant_b": {
            "label": "Test",
            "description": test["variant_b"],
            "sample_size": n_b,
            "metric_value": round(observed_b, 3),
            "std_dev": round(std + random.uniform(-0.05, 0.05), 3),
        },
    }


def compute_statistical_significance(results, confidence_level=0.95):
    """Compute statistical significance of A/B test results."""
    a = results["variant_a"]
    b = results["variant_b"]

    mean_diff = b["metric_value"] - a["metric_value"]
    se = math.sqrt((a["std_dev"] ** 2 / a["sample_size"]) + (b["std_dev"] ** 2 / b["sample_size"]))

    if se == 0:
        z_score = 0
    else:
        z_score = mean_diff / se

    # Two-tailed test
    z_critical = {0.90: 1.645, 0.95: 1.96, 0.99: 2.576}.get(confidence_level, 1.96)
    is_significant = abs(z_score) > z_critical

    # Effect size (Cohen's d approximation)
    pooled_std = math.sqrt((a["std_dev"] ** 2 + b["std_dev"] ** 2) / 2)
    cohens_d = mean_diff / pooled_std if pooled_std > 0 else 0

    effect_label = "negligible"
    if abs(cohens_d) >= 0.8:
        effect_label = "large"
    elif abs(cohens_d) >= 0.5:
        effect_label = "medium"
    elif abs(cohens_d) >= 0.2:
        effect_label = "small"

    # Determine winner
    if not is_significant:
        winner = "none (not statistically significant)"
        recommendation = "Continue test for more data, or keep control (no meaningful difference detected)"
    elif mean_diff > 0:
        winner = "Variant B (Test)"
        recommendation = f"Replace control with Variant B. Expected {results['primary_metric']} improvement: {round(mean_diff, 3)}"
    else:
        winner = "Variant A (Control)"
        recommendation = "Keep current control. Test variant performed worse."

    return {
        "mean_difference": round(mean_diff, 4),
        "standard_error": round(se, 4),
        "z_score": round(z_score, 3),
        "z_critical": z_critical,
        "confidence_level": confidence_level,
        "is_significant": is_significant,
        "effect_size": {
            "cohens_d": round(cohens_d, 3),
            "interpretation": effect_label,
        },
        "relative_improvement_pct": round(mean_diff / a["metric_value"] * 100, 2) if a["metric_value"] != 0 else 0,
        "winner": winner,
        "recommendation": recommendation,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Analyze A/B test results for canned response templates"
    )
    parser.add_argument(
        "--test-id",
        help="A/B test identifier (e.g., ABT-042)",
    )
    parser.add_argument(
        "--metric",
        choices=["csat", "resolution_rate", "reopen_rate", "reply_rate", "handle_time"],
        default="csat",
        help="Primary metric to analyze (default: csat)",
    )
    parser.add_argument(
        "--confidence",
        type=float,
        default=0.95,
        help="Confidence level: 0.90, 0.95, or 0.99 (default: 0.95)",
    )
    parser.add_argument(
        "--list-active",
        action="store_true",
        help="List all active A/B tests",
    )

    args = parser.parse_args()

    if args.list_active:
        output = {
            "active_tests": ACTIVE_TESTS,
            "total_active": sum(1 for t in ACTIVE_TESTS if t["status"] == "running"),
            "total_complete": sum(1 for t in ACTIVE_TESTS if t["status"] == "complete"),
        }
        print(json.dumps(output, indent=2))
        return

    if not args.test_id:
        parser.error("--test-id is required (or use --list-active)")

    results = simulate_test_results(args.test_id, args.metric)
    if "error" in results:
        print(json.dumps(results, indent=2), file=sys.stderr)
        sys.exit(1)

    analysis = compute_statistical_significance(results, args.confidence)

    output = {
        "test_id": args.test_id,
        "analysis_date": datetime.utcnow().isoformat() + "Z",
        "test_info": results["test_info"],
        "primary_metric": args.metric,
        "results": {
            "variant_a": results["variant_a"],
            "variant_b": results["variant_b"],
        },
        "statistical_analysis": analysis,
        "next_steps": [
            analysis["recommendation"],
            "Monitor secondary metrics for 2 weeks after implementing winner",
            "Document learnings for future test design",
        ],
    }

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
