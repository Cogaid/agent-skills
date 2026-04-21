#!/usr/bin/env python3
"""Predict SLA compliance based on current trends.

Usage:
    python scripts/forecast_compliance.py --period next-week --confidence 0.9
    python scripts/forecast_compliance.py --period next-month --tier enterprise
    python scripts/forecast_compliance.py --period next-week --metric frt
"""

import argparse
import json
import math
import random
import sys
from datetime import datetime, timedelta

random.seed(42)

# Simulated historical weekly compliance data (last 8 weeks)
HISTORICAL_DATA = {
    "frt": [94.2, 93.8, 95.1, 94.5, 96.0, 95.3, 95.8, 96.2],
    "rt": [91.5, 92.0, 91.8, 93.2, 92.5, 94.0, 93.5, 94.1],
    "uptime": [99.92, 99.95, 99.88, 99.93, 99.96, 99.91, 99.94, 99.97],
    "fcr": [73.5, 74.0, 73.8, 75.2, 74.5, 76.0, 75.5, 76.2],
}

TARGETS = {"frt": 95.0, "rt": 95.0, "uptime": 99.9, "fcr": 75.0}


def simple_linear_forecast(data, periods_ahead=1):
    """Simple linear regression forecast."""
    n = len(data)
    x = list(range(n))
    x_mean = sum(x) / n
    y_mean = sum(data) / n

    numerator = sum((x[i] - x_mean) * (data[i] - y_mean) for i in range(n))
    denominator = sum((x[i] - x_mean) ** 2 for i in range(n))

    if denominator == 0:
        slope = 0
    else:
        slope = numerator / denominator

    intercept = y_mean - slope * x_mean

    forecasts = []
    for p in range(1, periods_ahead + 1):
        forecast_x = n - 1 + p
        forecast_y = intercept + slope * forecast_x
        forecasts.append(round(forecast_y, 2))

    # Calculate residual standard error for confidence intervals
    predictions = [intercept + slope * xi for xi in x]
    residuals = [data[i] - predictions[i] for i in range(n)]
    sse = sum(r ** 2 for r in residuals)
    se = math.sqrt(sse / max(1, n - 2))

    return forecasts, slope, se


def compute_confidence_interval(forecast, se, confidence_level, n):
    """Compute confidence interval using t-distribution approximation."""
    # Approximate z-scores for common confidence levels
    z_scores = {0.8: 1.282, 0.85: 1.44, 0.9: 1.645, 0.95: 1.96, 0.99: 2.576}
    z = z_scores.get(confidence_level, 1.645)

    margin = z * se * math.sqrt(1 + 1 / n)
    return {
        "lower": round(forecast - margin, 2),
        "upper": round(min(100, forecast + margin), 2),
        "margin": round(margin, 2),
    }


def assess_risk(forecast, target, ci_lower):
    """Assess risk of SLA breach."""
    if ci_lower >= target:
        return {"level": "low", "description": "Forecast confidently above target"}
    elif forecast >= target:
        return {"level": "medium", "description": "Forecast above target but lower bound is below"}
    else:
        return {"level": "high", "description": "Forecast below target -- intervention recommended"}


def main():
    parser = argparse.ArgumentParser(
        description="Predict SLA compliance based on current trends"
    )
    parser.add_argument(
        "--period",
        default="next-week",
        help="Forecast period: next-week, next-month (default: next-week)",
    )
    parser.add_argument(
        "--confidence",
        type=float,
        default=0.9,
        help="Confidence level for intervals: 0.8, 0.85, 0.9, 0.95, 0.99 (default: 0.9)",
    )
    parser.add_argument(
        "--metric",
        choices=["frt", "rt", "uptime", "fcr", "all"],
        default="all",
        help="Metric to forecast (default: all)",
    )
    parser.add_argument(
        "--tier",
        choices=["enterprise", "premium", "standard", "basic", "all"],
        default="all",
        help="Tier to forecast (default: all)",
    )

    args = parser.parse_args()

    periods_ahead = 1 if args.period == "next-week" else 4
    metrics = list(HISTORICAL_DATA.keys()) if args.metric == "all" else [args.metric]

    forecasts = {}
    overall_risk = "low"

    for metric in metrics:
        data = HISTORICAL_DATA[metric]
        target = TARGETS[metric]
        forecast_values, slope, se = simple_linear_forecast(data, periods_ahead)

        point_forecast = forecast_values[-1]
        ci = compute_confidence_interval(point_forecast, se, args.confidence, len(data))
        risk = assess_risk(point_forecast, target, ci["lower"])

        if risk["level"] == "high":
            overall_risk = "high"
        elif risk["level"] == "medium" and overall_risk != "high":
            overall_risk = "medium"

        trend_direction = "improving" if slope > 0.1 else ("declining" if slope < -0.1 else "stable")

        forecasts[metric] = {
            "current_value": data[-1],
            "target": target,
            "forecast": point_forecast,
            "confidence_interval": ci,
            "trend": {
                "direction": trend_direction,
                "slope_per_week": round(slope, 3),
                "last_8_weeks": data,
            },
            "risk": risk,
        }

    recommendations = []
    for metric, f in forecasts.items():
        if f["risk"]["level"] == "high":
            recommendations.append(
                f"URGENT: {metric.upper()} forecast ({f['forecast']}%) is below target ({f['target']}%). "
                f"Increase staffing or review process bottlenecks."
            )
        elif f["risk"]["level"] == "medium":
            recommendations.append(
                f"WATCH: {metric.upper()} forecast ({f['forecast']}%) is near target. "
                f"Monitor closely and prepare contingency plan."
            )

    if not recommendations:
        recommendations.append("All metrics are forecast to meet targets. Continue current operations.")

    output = {
        "forecast_period": args.period,
        "confidence_level": args.confidence,
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "overall_risk": overall_risk,
        "metrics": forecasts,
        "recommendations": recommendations,
    }

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
