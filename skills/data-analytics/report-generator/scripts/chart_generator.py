#!/usr/bin/env python3
"""Generate chart specifications and data for report visualizations.

Usage:
    python chart_generator.py --type line --metric revenue --periods 12
    python chart_generator.py --type bar --metric users --periods 6 --output chart.json
    python chart_generator.py --type scorecard --metrics "Revenue,Users,NPS" --output scorecard.json
"""

import argparse
import json
import random
import sys
from datetime import datetime, timedelta

CHART_TYPES = {
    "line": {
        "name": "Line Chart",
        "best_for": "Trends over time",
        "config": {
            "type": "line",
            "options": {
                "y_axis_start_at_zero": False,
                "show_data_labels": False,
                "show_trend_line": True,
                "smooth_lines": True,
            },
        },
    },
    "bar": {
        "name": "Bar Chart",
        "best_for": "Comparing values across categories",
        "config": {
            "type": "bar",
            "options": {
                "y_axis_start_at_zero": True,
                "show_data_labels": True,
                "horizontal": False,
                "stacked": False,
            },
        },
    },
    "pie": {
        "name": "Pie Chart",
        "best_for": "Part of whole (5 or fewer categories)",
        "config": {
            "type": "pie",
            "options": {
                "show_percentages": True,
                "show_legend": True,
                "max_slices": 5,
            },
        },
    },
    "scorecard": {
        "name": "Scorecard",
        "best_for": "KPI status overview",
        "config": {
            "type": "scorecard",
            "options": {
                "show_trend_arrow": True,
                "show_target": True,
                "color_code": True,
            },
        },
    },
    "scatter": {
        "name": "Scatter Plot",
        "best_for": "Correlation between two variables",
        "config": {
            "type": "scatter",
            "options": {
                "show_trend_line": True,
                "show_correlation": True,
            },
        },
    },
}


def generate_time_series(metric, periods):
    """Generate sample time series data."""
    base_value = random.uniform(100, 10000)
    growth_rate = random.uniform(-0.02, 0.05)
    noise = random.uniform(0.05, 0.15)

    data = []
    current = base_value
    now = datetime.now()

    for i in range(periods - 1, -1, -1):
        date = now - timedelta(days=30 * i)
        current = current * (1 + growth_rate + random.uniform(-noise, noise))
        data.append({
            "date": date.strftime("%Y-%m"),
            "value": round(current, 2),
        })

    return {
        "metric": metric,
        "data": data,
        "summary": {
            "latest": data[-1]["value"],
            "earliest": data[0]["value"],
            "min": round(min(d["value"] for d in data), 2),
            "max": round(max(d["value"] for d in data), 2),
            "avg": round(sum(d["value"] for d in data) / len(data), 2),
            "total_change_pct": round(((data[-1]["value"] - data[0]["value"]) / data[0]["value"]) * 100, 1),
        },
    }


def generate_comparison_data(metric, periods):
    """Generate comparison data for bar charts."""
    data = []
    now = datetime.now()
    for i in range(periods - 1, -1, -1):
        date = now - timedelta(days=30 * i)
        actual = round(random.uniform(100, 1000), 2)
        target = round(actual * random.uniform(0.9, 1.1), 2)
        data.append({
            "period": date.strftime("%Y-%m"),
            "actual": actual,
            "target": target,
            "variance_pct": round(((actual - target) / target) * 100, 1),
        })
    return {"metric": metric, "data": data}


def generate_scorecard(metrics_str):
    """Generate scorecard data for multiple metrics."""
    metrics = [m.strip() for m in metrics_str.split(",")]
    cards = []
    for metric in metrics:
        current = round(random.uniform(50, 500), 1)
        prior = round(current * random.uniform(0.85, 1.15), 1)
        target = round(current * random.uniform(0.9, 1.1), 1)
        change = round(((current - prior) / prior) * 100, 1) if prior else 0
        status = "Green" if current >= target * 0.9 else "Yellow" if current >= target * 0.7 else "Red"
        cards.append({
            "metric": metric,
            "value": current,
            "prior": prior,
            "change_pct": change,
            "target": target,
            "trend": "up" if change > 0 else "down" if change < 0 else "flat",
            "status": status,
        })
    return {"type": "scorecard", "cards": cards}


def main():
    parser = argparse.ArgumentParser(
        description="Generate chart specifications and sample data for report visualizations."
    )
    parser.add_argument(
        "--type",
        choices=list(CHART_TYPES.keys()),
        default="line",
        help="Chart type (default: line)",
    )
    parser.add_argument(
        "--metric",
        default="Revenue",
        help="Metric name (default: Revenue)",
    )
    parser.add_argument(
        "--metrics",
        help="Comma-separated metric names (for scorecard type)",
    )
    parser.add_argument(
        "--periods",
        type=int,
        default=12,
        help="Number of periods to generate (default: 12)",
    )
    parser.add_argument(
        "--output",
        help="Output file path (default: stdout)",
    )

    args = parser.parse_args()

    chart_info = CHART_TYPES[args.type]

    if args.type == "scorecard":
        metrics_str = args.metrics or "Revenue,Users,NPS,Churn Rate"
        data = generate_scorecard(metrics_str)
    elif args.type == "bar":
        data = generate_comparison_data(args.metric, args.periods)
    else:
        data = generate_time_series(args.metric, args.periods)

    result = {
        "chart": chart_info,
        "data": data,
        "generated_date": datetime.now().strftime("%Y-%m-%d"),
    }

    output = json.dumps(result, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Chart data written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
