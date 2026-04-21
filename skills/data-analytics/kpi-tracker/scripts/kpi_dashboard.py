#!/usr/bin/env python3
"""Generate a KPI dashboard with sample data and traffic light scoring.

Usage:
    python kpi_dashboard.py --department sales --period "2025-Q1"
    python kpi_dashboard.py --department engineering --output dashboard.json
"""

import argparse
import json
import random
import sys
from datetime import datetime

DEPARTMENT_KPIS = {
    "sales": {
        "name": "Sales",
        "kpis": [
            {"name": "Monthly Recurring Revenue", "unit": "$", "target": 500000, "direction": "higher_better"},
            {"name": "Win Rate", "unit": "%", "target": 30, "direction": "higher_better"},
            {"name": "Average Deal Size", "unit": "$", "target": 15000, "direction": "higher_better"},
            {"name": "Sales Cycle Length", "unit": "days", "target": 35, "direction": "lower_better"},
            {"name": "Pipeline Coverage", "unit": "x", "target": 3.5, "direction": "higher_better"},
            {"name": "Quota Attainment", "unit": "%", "target": 100, "direction": "higher_better"},
        ],
    },
    "marketing": {
        "name": "Marketing",
        "kpis": [
            {"name": "Marketing Qualified Leads", "unit": "", "target": 500, "direction": "higher_better"},
            {"name": "Cost per Lead", "unit": "$", "target": 45, "direction": "lower_better"},
            {"name": "Conversion Rate", "unit": "%", "target": 3.5, "direction": "higher_better"},
            {"name": "Organic Traffic", "unit": "", "target": 50000, "direction": "higher_better"},
            {"name": "Email Open Rate", "unit": "%", "target": 22, "direction": "higher_better"},
            {"name": "Return on Ad Spend", "unit": "x", "target": 4.0, "direction": "higher_better"},
        ],
    },
    "engineering": {
        "name": "Engineering",
        "kpis": [
            {"name": "Deployment Frequency", "unit": "/week", "target": 10, "direction": "higher_better"},
            {"name": "Lead Time for Changes", "unit": "hours", "target": 24, "direction": "lower_better"},
            {"name": "Change Failure Rate", "unit": "%", "target": 10, "direction": "lower_better"},
            {"name": "Mean Time to Recovery", "unit": "minutes", "target": 60, "direction": "lower_better"},
            {"name": "Sprint Velocity", "unit": "points", "target": 45, "direction": "higher_better"},
            {"name": "Test Coverage", "unit": "%", "target": 80, "direction": "higher_better"},
        ],
    },
    "support": {
        "name": "Customer Support",
        "kpis": [
            {"name": "First Response Time", "unit": "hours", "target": 2, "direction": "lower_better"},
            {"name": "Resolution Time", "unit": "hours", "target": 24, "direction": "lower_better"},
            {"name": "First Contact Resolution", "unit": "%", "target": 70, "direction": "higher_better"},
            {"name": "Customer Satisfaction", "unit": "/5", "target": 4.2, "direction": "higher_better"},
            {"name": "Net Promoter Score", "unit": "", "target": 50, "direction": "higher_better"},
            {"name": "Escalation Rate", "unit": "%", "target": 10, "direction": "lower_better"},
        ],
    },
    "product": {
        "name": "Product",
        "kpis": [
            {"name": "Daily Active Users", "unit": "", "target": 5000, "direction": "higher_better"},
            {"name": "Monthly Active Users", "unit": "", "target": 25000, "direction": "higher_better"},
            {"name": "Feature Adoption Rate", "unit": "%", "target": 30, "direction": "higher_better"},
            {"name": "Retention Rate (D30)", "unit": "%", "target": 40, "direction": "higher_better"},
            {"name": "Churn Rate", "unit": "%", "target": 3, "direction": "lower_better"},
            {"name": "Time to Value", "unit": "minutes", "target": 15, "direction": "lower_better"},
        ],
    },
}


def generate_kpi_value(kpi):
    """Generate a realistic KPI value near the target."""
    target = kpi["target"]
    variance = target * random.uniform(0.15, 0.35)
    actual = target + random.uniform(-variance, variance * 0.8)
    prior = target + random.uniform(-variance, variance * 0.5)
    return round(max(0, actual), 2), round(max(0, prior), 2)


def score_kpi(actual, target, direction):
    """Calculate traffic light score."""
    if direction == "higher_better":
        ratio = actual / target if target else 1
    else:
        ratio = target / actual if actual else 1

    if ratio >= 1.2:
        return "Blue"
    elif ratio >= 0.9:
        return "Green"
    elif ratio >= 0.7:
        return "Yellow"
    else:
        return "Red"


def generate_dashboard(department, period):
    """Generate a KPI dashboard."""
    dept = DEPARTMENT_KPIS.get(department, DEPARTMENT_KPIS["sales"])

    kpi_results = []
    for kpi in dept["kpis"]:
        actual, prior = generate_kpi_value(kpi)
        target = kpi["target"]
        status = score_kpi(actual, target, kpi["direction"])

        attainment = round((actual / target * 100), 1) if kpi["direction"] == "higher_better" else round((target / actual * 100), 1) if actual else 0

        change_pct = round(((actual - prior) / prior * 100), 1) if prior else 0

        kpi_results.append({
            "name": kpi["name"],
            "actual": actual,
            "target": target,
            "unit": kpi["unit"],
            "attainment_pct": attainment,
            "prior_period": prior,
            "change_pct": change_pct,
            "trend": "up" if change_pct > 2 else "down" if change_pct < -2 else "flat",
            "status": status,
            "direction": kpi["direction"],
        })

    green = sum(1 for k in kpi_results if k["status"] in ("Green", "Blue"))
    total = len(kpi_results)

    dashboard = {
        "metadata": {
            "department": dept["name"],
            "period": period,
            "generated_date": datetime.now().strftime("%Y-%m-%d"),
            "total_kpis": total,
        },
        "summary": {
            "on_track": green,
            "at_risk": sum(1 for k in kpi_results if k["status"] == "Yellow"),
            "off_track": sum(1 for k in kpi_results if k["status"] == "Red"),
            "exceeding": sum(1 for k in kpi_results if k["status"] == "Blue"),
            "overall_health": "On Track" if green / total >= 0.7 else "At Risk" if green / total >= 0.5 else "Off Track",
        },
        "kpis": kpi_results,
        "note": "Sample data -- replace with actual KPI values from your data sources",
    }

    return dashboard


def main():
    parser = argparse.ArgumentParser(
        description="Generate a KPI dashboard with traffic light scoring."
    )
    parser.add_argument(
        "--department",
        choices=list(DEPARTMENT_KPIS.keys()),
        default="sales",
        help="Department (default: sales)",
    )
    parser.add_argument(
        "--period",
        default=datetime.now().strftime("%Y-Q%q" if False else "%Y-Q1"),
        help="Report period (e.g., 2025-Q1)",
    )
    parser.add_argument(
        "--output",
        help="Output file path (default: stdout)",
    )

    args = parser.parse_args()

    dashboard = generate_dashboard(department=args.department, period=args.period)
    output = json.dumps(dashboard, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"KPI dashboard written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
