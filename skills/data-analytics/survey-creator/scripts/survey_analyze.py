#!/usr/bin/env python3
"""Analyze survey responses and generate summary statistics.

Usage:
    python survey_analyze.py --type nps
    python survey_analyze.py --type csat --output analysis.json
    python survey_analyze.py --type engagement --output analysis.json
"""

import argparse
import json
import random
import sys
from datetime import datetime

SAMPLE_DATA = {
    "nps": {
        "responses": [random.randint(0, 10) for _ in range(200)],
        "metric_name": "Net Promoter Score",
    },
    "csat": {
        "responses": [random.randint(1, 5) for _ in range(200)],
        "metric_name": "Customer Satisfaction Score",
    },
    "engagement": {
        "dimensions": {
            "Engagement & Motivation": [round(random.uniform(2.5, 5.0), 1) for _ in range(100)],
            "Management & Leadership": [round(random.uniform(2.5, 5.0), 1) for _ in range(100)],
            "Growth & Development": [round(random.uniform(2.0, 5.0), 1) for _ in range(100)],
            "Work Environment": [round(random.uniform(3.0, 5.0), 1) for _ in range(100)],
            "Recognition & Compensation": [round(random.uniform(2.0, 4.5), 1) for _ in range(100)],
        },
        "metric_name": "Employee Engagement Index",
    },
}


def analyze_nps(responses):
    """Calculate NPS from a list of 0-10 scores."""
    total = len(responses)
    promoters = sum(1 for r in responses if r >= 9)
    passives = sum(1 for r in responses if 7 <= r <= 8)
    detractors = sum(1 for r in responses if r <= 6)

    nps_score = round(((promoters - detractors) / total) * 100)

    distribution = {}
    for i in range(11):
        distribution[str(i)] = sum(1 for r in responses if r == i)

    return {
        "metric": "Net Promoter Score",
        "nps_score": nps_score,
        "total_responses": total,
        "breakdown": {
            "promoters": {"count": promoters, "percentage": round(100 * promoters / total, 1)},
            "passives": {"count": passives, "percentage": round(100 * passives / total, 1)},
            "detractors": {"count": detractors, "percentage": round(100 * detractors / total, 1)},
        },
        "distribution": distribution,
        "interpretation": (
            "Excellent" if nps_score >= 50 else
            "Good" if nps_score >= 30 else
            "Average" if nps_score >= 0 else
            "Needs Improvement"
        ),
        "benchmark": {"excellent": ">50", "good": "30-50", "average": "0-30", "poor": "<0"},
    }


def analyze_csat(responses):
    """Calculate CSAT from a list of 1-5 scores."""
    total = len(responses)
    satisfied = sum(1 for r in responses if r >= 4)
    avg = round(sum(responses) / total, 2)

    distribution = {}
    for i in range(1, 6):
        distribution[str(i)] = sum(1 for r in responses if r == i)

    return {
        "metric": "Customer Satisfaction Score",
        "csat_percentage": round(100 * satisfied / total, 1),
        "average_score": avg,
        "total_responses": total,
        "distribution": distribution,
        "interpretation": (
            "Excellent" if satisfied / total >= 0.9 else
            "Good" if satisfied / total >= 0.8 else
            "Average" if satisfied / total >= 0.7 else
            "Needs Improvement"
        ),
        "benchmark": {"excellent": ">90%", "good": "80-90%", "average": "70-80%", "poor": "<70%"},
    }


def analyze_engagement(dimensions):
    """Analyze employee engagement across dimensions."""
    results = {}
    overall_scores = []

    for dim, scores in dimensions.items():
        avg = round(sum(scores) / len(scores), 2)
        overall_scores.append(avg)
        results[dim] = {
            "average": avg,
            "responses": len(scores),
            "min": min(scores),
            "max": max(scores),
            "status": "Healthy" if avg >= 3.8 else "Attention Needed" if avg >= 3.0 else "Critical",
        }

    overall = round(sum(overall_scores) / len(overall_scores), 2)

    return {
        "metric": "Employee Engagement Index",
        "overall_index": overall,
        "interpretation": "Healthy" if overall >= 3.8 else "Attention Needed" if overall >= 3.0 else "Critical",
        "dimensions": results,
        "top_strength": max(results, key=lambda k: results[k]["average"]),
        "top_concern": min(results, key=lambda k: results[k]["average"]),
        "benchmark": {"healthy": ">3.8/5.0", "attention": "3.0-3.8", "critical": "<3.0"},
    }


def main():
    parser = argparse.ArgumentParser(
        description="Analyze survey responses and generate summary statistics."
    )
    parser.add_argument(
        "--type",
        choices=["nps", "csat", "engagement"],
        default="nps",
        help="Survey analysis type (default: nps)",
    )
    parser.add_argument(
        "--output",
        help="Output file path (default: stdout)",
    )

    args = parser.parse_args()

    data = SAMPLE_DATA[args.type]

    if args.type == "nps":
        analysis = analyze_nps(data["responses"])
    elif args.type == "csat":
        analysis = analyze_csat(data["responses"])
    elif args.type == "engagement":
        analysis = analyze_engagement(data["dimensions"])

    result = {
        "analysis_date": datetime.now().strftime("%Y-%m-%d"),
        "analysis_type": args.type,
        "note": "Using sample data -- replace with actual survey responses",
        "results": analysis,
    }

    output = json.dumps(result, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Analysis written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
