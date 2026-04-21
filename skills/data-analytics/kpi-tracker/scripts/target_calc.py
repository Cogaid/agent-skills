#!/usr/bin/env python3
"""Calculate KPI targets based on historical data and growth assumptions.

Usage:
    python target_calc.py --kpi "mrr" --method historical --growth-rate 10
    python target_calc.py --kpi "win_rate" --method benchmark --output targets.json
"""

import argparse
import json
import random
import sys
from datetime import datetime

# Sample historical data
SAMPLE_HISTORY = {
    "mrr": {
        "name": "Monthly Recurring Revenue",
        "unit": "$",
        "history": [
            {"period": "2024-Q1", "value": 380000},
            {"period": "2024-Q2", "value": 410000},
            {"period": "2024-Q3", "value": 435000},
            {"period": "2024-Q4", "value": 470000},
        ],
    },
    "win_rate": {
        "name": "Win Rate",
        "unit": "%",
        "history": [
            {"period": "2024-Q1", "value": 26},
            {"period": "2024-Q2", "value": 28},
            {"period": "2024-Q3", "value": 27},
            {"period": "2024-Q4", "value": 30},
        ],
    },
    "nps": {
        "name": "Net Promoter Score",
        "unit": "",
        "history": [
            {"period": "2024-Q1", "value": 42},
            {"period": "2024-Q2", "value": 45},
            {"period": "2024-Q3", "value": 43},
            {"period": "2024-Q4", "value": 48},
        ],
    },
    "churn_rate": {
        "name": "Churn Rate",
        "unit": "%",
        "history": [
            {"period": "2024-Q1", "value": 3.2},
            {"period": "2024-Q2", "value": 2.9},
            {"period": "2024-Q3", "value": 3.1},
            {"period": "2024-Q4", "value": 2.7},
        ],
    },
}

BENCHMARKS = {
    "mrr": {"industry_median": 500000, "top_quartile": 750000, "source": "SaaS benchmarks report"},
    "win_rate": {"industry_median": 25, "top_quartile": 35, "source": "Sales benchmark report"},
    "nps": {"industry_median": 40, "top_quartile": 60, "source": "Customer experience benchmarks"},
    "churn_rate": {"industry_median": 5.0, "top_quartile": 2.5, "source": "SaaS churn benchmarks"},
}

METHODS = {
    "historical": "Project forward using historical trend and specified growth rate",
    "benchmark": "Set target relative to industry benchmarks",
    "stretch": "Apply stretch factor (20-30%) above historical projection",
}


def calculate_historical_target(kpi_data, growth_rate):
    """Calculate target using historical baseline + growth rate."""
    history = kpi_data["history"]
    values = [h["value"] for h in history]

    avg = sum(values) / len(values)
    latest = values[-1]

    # Simple linear trend
    n = len(values)
    x_mean = (n - 1) / 2
    y_mean = avg
    numerator = sum((i - x_mean) * (v - y_mean) for i, v in enumerate(values))
    denominator = sum((i - x_mean) ** 2 for i in range(n))
    slope = numerator / denominator if denominator else 0

    projected = latest + slope
    target = projected * (1 + growth_rate / 100)

    return {
        "method": "Historical Baseline",
        "latest_value": latest,
        "average": round(avg, 2),
        "trend_slope": round(slope, 2),
        "projected_next_period": round(projected, 2),
        "growth_rate_applied": f"{growth_rate}%",
        "recommended_target": round(target, 2),
        "milestones": {
            "month_1": round(latest + (target - latest) * 0.33, 2),
            "month_2": round(latest + (target - latest) * 0.66, 2),
            "month_3": round(target, 2),
        },
    }


def calculate_benchmark_target(kpi_name, kpi_data):
    """Calculate target relative to industry benchmarks."""
    bench = BENCHMARKS.get(kpi_name)
    if not bench:
        return {"error": f"No benchmarks available for {kpi_name}"}

    latest = kpi_data["history"][-1]["value"]

    return {
        "method": "Benchmark",
        "latest_value": latest,
        "industry_median": bench["industry_median"],
        "top_quartile": bench["top_quartile"],
        "source": bench["source"],
        "recommended_target": bench["industry_median"] if latest < bench["industry_median"] else bench["top_quartile"],
        "gap_to_median": round(bench["industry_median"] - latest, 2),
        "gap_to_top_quartile": round(bench["top_quartile"] - latest, 2),
        "positioning": (
            "Above top quartile" if latest >= bench["top_quartile"] else
            "Above median" if latest >= bench["industry_median"] else
            "Below median"
        ),
    }


def calculate_stretch_target(kpi_data, growth_rate):
    """Calculate stretch target with aggressive growth assumption."""
    base = calculate_historical_target(kpi_data, growth_rate)
    stretch_factor = 1.25  # 25% stretch

    return {
        "method": "Stretch Target",
        "base_target": base["recommended_target"],
        "stretch_factor": f"{int((stretch_factor - 1) * 100)}%",
        "recommended_target": round(base["recommended_target"] * stretch_factor, 2),
        "note": "Stretch targets should be aspirational. Expect 70% achievement rate.",
    }


def main():
    parser = argparse.ArgumentParser(
        description="Calculate KPI targets based on historical data and growth assumptions."
    )
    parser.add_argument(
        "--kpi",
        choices=list(SAMPLE_HISTORY.keys()),
        default="mrr",
        help="KPI to calculate target for (default: mrr)",
    )
    parser.add_argument(
        "--method",
        choices=list(METHODS.keys()),
        default="historical",
        help="Target setting method (default: historical)",
    )
    parser.add_argument(
        "--growth-rate",
        type=float,
        default=10,
        help="Expected growth rate in percent (default: 10)",
    )
    parser.add_argument(
        "--output",
        help="Output file path (default: stdout)",
    )

    args = parser.parse_args()

    kpi_data = SAMPLE_HISTORY[args.kpi]

    if args.method == "historical":
        target_info = calculate_historical_target(kpi_data, args.growth_rate)
    elif args.method == "benchmark":
        target_info = calculate_benchmark_target(args.kpi, kpi_data)
    elif args.method == "stretch":
        target_info = calculate_stretch_target(kpi_data, args.growth_rate)

    result = {
        "kpi": kpi_data["name"],
        "unit": kpi_data["unit"],
        "history": kpi_data["history"],
        "target_calculation": target_info,
        "generated_date": datetime.now().strftime("%Y-%m-%d"),
        "note": "Using sample historical data -- replace with actual KPI history",
    }

    output = json.dumps(result, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Target calculation written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
