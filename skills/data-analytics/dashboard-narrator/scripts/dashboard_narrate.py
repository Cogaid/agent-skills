#!/usr/bin/env python3
"""Generate narrative commentary from dashboard metrics data.

Usage:
    python dashboard_narrate.py --period "2025-03"
    python dashboard_narrate.py --period "2025-03" --format detailed --output narrative.json
"""

import argparse
import json
import random
import sys
from datetime import datetime

# Sample dashboard data
SAMPLE_METRICS = [
    {"name": "Revenue", "current": 1250000, "prior": 1180000, "target": 1200000, "unit": "$", "direction": "higher_better"},
    {"name": "Active Users", "current": 45200, "prior": 42800, "target": 44000, "unit": "", "direction": "higher_better"},
    {"name": "NPS", "current": 48, "prior": 52, "target": 50, "unit": "", "direction": "higher_better"},
    {"name": "Churn Rate", "current": 2.8, "prior": 2.5, "target": 2.5, "unit": "%", "direction": "lower_better"},
    {"name": "CAC", "current": 58, "prior": 45, "target": 50, "unit": "$", "direction": "lower_better"},
    {"name": "CSAT", "current": 4.3, "prior": 4.1, "target": 4.2, "unit": "/5", "direction": "higher_better"},
]

MAGNITUDE_LANGUAGE = {
    "flat": {"positive": "remained stable", "negative": "stagnated", "neutral": "held steady"},
    "slight": {"positive": "edged up", "negative": "dipped slightly", "neutral": "moved marginally"},
    "moderate": {"positive": "grew", "negative": "declined", "neutral": "changed"},
    "notable": {"positive": "rose significantly", "negative": "fell notably", "neutral": "shifted"},
    "strong": {"positive": "surged", "negative": "dropped sharply", "neutral": "swung"},
    "dramatic": {"positive": "skyrocketed", "negative": "plummeted", "neutral": "moved dramatically"},
}


def classify_magnitude(pct_change):
    """Classify the magnitude of a percentage change."""
    abs_change = abs(pct_change)
    if abs_change < 2:
        return "flat"
    elif abs_change < 5:
        return "slight"
    elif abs_change < 10:
        return "moderate"
    elif abs_change < 20:
        return "notable"
    elif abs_change < 50:
        return "strong"
    else:
        return "dramatic"


def determine_status(metric):
    """Determine traffic light status."""
    if metric["direction"] == "higher_better":
        ratio = metric["current"] / metric["target"] if metric["target"] else 1
    else:
        ratio = metric["target"] / metric["current"] if metric["current"] else 1

    if ratio >= 0.9:
        return "Green"
    elif ratio >= 0.7:
        return "Yellow"
    else:
        return "Red"


def generate_narrative(metric):
    """Generate narrative for a single metric."""
    current = metric["current"]
    prior = metric["prior"]
    target = metric["target"]
    direction = metric["direction"]

    pct_change = ((current - prior) / prior * 100) if prior else 0
    vs_target_pct = ((current - target) / target * 100) if target else 0

    magnitude = classify_magnitude(pct_change)

    if direction == "higher_better":
        tone = "positive" if pct_change > 0 else "negative" if pct_change < 0 else "neutral"
    else:
        tone = "positive" if pct_change < 0 else "negative" if pct_change > 0 else "neutral"

    language = MAGNITUDE_LANGUAGE[magnitude][tone]

    unit = metric["unit"]
    if unit == "$":
        current_fmt = f"${current:,.0f}"
        prior_fmt = f"${prior:,.0f}"
        target_fmt = f"${target:,.0f}"
    elif unit == "%":
        current_fmt = f"{current}%"
        prior_fmt = f"{prior}%"
        target_fmt = f"{target}%"
    else:
        current_fmt = f"{current:,.0f}{unit}" if isinstance(current, (int, float)) and current > 100 else f"{current}{unit}"
        prior_fmt = f"{prior:,.0f}{unit}" if isinstance(prior, (int, float)) and prior > 100 else f"{prior}{unit}"
        target_fmt = f"{target:,.0f}{unit}" if isinstance(target, (int, float)) and target > 100 else f"{target}{unit}"

    narrative = f"{metric['name']} {language} to {current_fmt}, {'+' if pct_change >= 0 else ''}{pct_change:.1f}% from {prior_fmt} in the prior period."

    if vs_target_pct >= 0 and direction == "higher_better":
        narrative += f" This exceeds the target of {target_fmt} by {vs_target_pct:.1f}%."
    elif vs_target_pct < 0 and direction == "higher_better":
        narrative += f" This falls short of the target of {target_fmt} by {abs(vs_target_pct):.1f}%."
    elif vs_target_pct <= 0 and direction == "lower_better":
        narrative += f" This is within the target of {target_fmt}."
    else:
        narrative += f" This exceeds the target ceiling of {target_fmt} by {vs_target_pct:.1f}%."

    return {
        "metric": metric["name"],
        "narrative": narrative,
        "status": determine_status(metric),
        "change_pct": round(pct_change, 1),
        "vs_target_pct": round(vs_target_pct, 1),
        "magnitude": magnitude,
        "tone": tone,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Generate narrative commentary from dashboard metrics."
    )
    parser.add_argument(
        "--period",
        default=datetime.now().strftime("%Y-%m"),
        help="Report period (e.g., 2025-03)",
    )
    parser.add_argument(
        "--format",
        choices=["summary", "detailed"],
        default="summary",
        help="Output format (default: summary)",
    )
    parser.add_argument(
        "--output",
        help="Output file path (default: stdout)",
    )

    args = parser.parse_args()

    narratives = [generate_narrative(m) for m in SAMPLE_METRICS]

    green = sum(1 for n in narratives if n["status"] == "Green")
    total = len(narratives)

    result = {
        "period": args.period,
        "generated_date": datetime.now().strftime("%Y-%m-%d"),
        "overall_status": "On Track" if green / total >= 0.7 else "At Risk" if green / total >= 0.5 else "Off Track",
        "summary": f"{green} of {total} metrics are on track.",
        "narratives": narratives,
        "note": "Using sample data -- replace SAMPLE_METRICS with actual dashboard data",
    }

    if args.format == "summary":
        result = {
            "period": result["period"],
            "overall_status": result["overall_status"],
            "summary": result["summary"],
            "metrics": [{
                "metric": n["metric"],
                "status": n["status"],
                "narrative": n["narrative"],
            } for n in narratives],
        }

    output = json.dumps(result, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Narrative written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
