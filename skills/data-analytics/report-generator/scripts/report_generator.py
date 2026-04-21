#!/usr/bin/env python3
"""Generate a data report skeleton with sample metrics and structure.

Usage:
    python report_generator.py --type monthly --period "2025-03"
    python report_generator.py --type weekly --period "2025-W12" --output report.json
    python report_generator.py --type quarterly --period "2025-Q1" --department sales
"""

import argparse
import json
import random
import sys
from datetime import datetime

REPORT_TYPES = {
    "weekly": {
        "name": "Weekly Operations Report",
        "sections": ["tldr", "metrics_dashboard", "completed", "blockers", "priorities_next_week"],
        "typical_metrics": ["Revenue", "Active Users", "Support Tickets", "Deployments", "Uptime %"],
    },
    "monthly": {
        "name": "Monthly Business Review",
        "sections": [
            "executive_summary", "financial_summary", "revenue_deep_dive",
            "customer_metrics", "product_metrics", "department_updates",
            "risks_and_issues", "outlook",
        ],
        "typical_metrics": [
            "Revenue", "Gross Margin", "EBITDA", "New Customers",
            "Churn Rate", "NPS", "CAC", "LTV", "DAU", "MAU",
        ],
    },
    "quarterly": {
        "name": "Quarterly Board Report",
        "sections": [
            "strategic_overview", "financial_performance", "growth_metrics",
            "product_and_technology", "team_and_organization",
            "competitive_landscape", "risk_register", "board_ask",
        ],
        "typical_metrics": [
            "ARR", "Revenue Growth %", "Gross Margin", "Cash Runway",
            "Customer Count", "Net Revenue Retention", "Employee Count",
            "Quota Attainment",
        ],
    },
    "adhoc": {
        "name": "Ad-Hoc Analysis Report",
        "sections": [
            "executive_summary", "background_and_objective",
            "methodology", "findings", "recommendations", "appendix",
        ],
        "typical_metrics": [],
    },
}

SAMPLE_DEPARTMENTS = {
    "sales": {
        "metrics": ["MRR", "Pipeline Value", "Win Rate", "Avg Deal Size", "Sales Cycle Days", "Quota Attainment"],
    },
    "marketing": {
        "metrics": ["MQLs", "Cost per Lead", "Conversion Rate", "Organic Traffic", "Email Open Rate", "ROAS"],
    },
    "engineering": {
        "metrics": ["Deploy Frequency", "Lead Time", "Change Failure Rate", "MTTR", "Sprint Velocity", "Test Coverage"],
    },
    "support": {
        "metrics": ["First Response Time", "Resolution Time", "CSAT", "FCR Rate", "Ticket Volume", "Escalation Rate"],
    },
}


def generate_sample_metric(name):
    """Generate a sample metric with realistic values."""
    current = round(random.uniform(50, 500), 1)
    prior = round(current * random.uniform(0.85, 1.15), 1)
    target = round(current * random.uniform(0.95, 1.1), 1)
    change_pct = round(((current - prior) / prior) * 100, 1) if prior != 0 else 0

    if current >= target * 0.9:
        status = "Green"
    elif current >= target * 0.7:
        status = "Yellow"
    else:
        status = "Red"

    return {
        "name": name,
        "current": current,
        "prior_period": prior,
        "change_pct": change_pct,
        "target": target,
        "status": status,
    }


def generate_report(report_type, period, department=None):
    """Generate a report skeleton with sample data."""
    rtype = REPORT_TYPES.get(report_type, REPORT_TYPES["monthly"])

    metrics = rtype["typical_metrics"]
    if department and department in SAMPLE_DEPARTMENTS:
        metrics = SAMPLE_DEPARTMENTS[department]["metrics"]

    sample_metrics = [generate_sample_metric(m) for m in metrics]

    green_count = sum(1 for m in sample_metrics if m["status"] == "Green")
    total = len(sample_metrics)

    report = {
        "metadata": {
            "report_type": rtype["name"],
            "period": period,
            "department": department or "All",
            "generated_date": datetime.now().strftime("%Y-%m-%d"),
            "author": "[AUTHOR NAME]",
            "status": "DRAFT",
        },
        "sections": rtype["sections"],
        "metrics": sample_metrics,
        "summary": {
            "total_metrics": total,
            "on_track": green_count,
            "at_risk": sum(1 for m in sample_metrics if m["status"] == "Yellow"),
            "off_track": sum(1 for m in sample_metrics if m["status"] == "Red"),
            "overall_health": "On Track" if green_count / max(total, 1) >= 0.7 else "At Risk" if green_count / max(total, 1) >= 0.5 else "Off Track",
        },
        "visualization_suggestions": [
            {"metric": metrics[0] if metrics else "Revenue", "chart_type": "line", "reason": "Show trend over time"},
            {"metric": metrics[1] if len(metrics) > 1 else "Users", "chart_type": "bar", "reason": "Compare across periods"},
            {"metric": "Overall Health", "chart_type": "scorecard", "reason": "Executive snapshot"},
        ],
    }

    return report


def main():
    parser = argparse.ArgumentParser(
        description="Generate a data report skeleton with sample metrics and structure."
    )
    parser.add_argument(
        "--type",
        choices=list(REPORT_TYPES.keys()),
        default="monthly",
        help="Report type (default: monthly)",
    )
    parser.add_argument(
        "--period",
        default=datetime.now().strftime("%Y-%m"),
        help="Report period (e.g., 2025-03, 2025-W12, 2025-Q1)",
    )
    parser.add_argument(
        "--department",
        choices=list(SAMPLE_DEPARTMENTS.keys()),
        help="Filter to specific department",
    )
    parser.add_argument(
        "--output",
        help="Output file path (default: stdout)",
    )

    args = parser.parse_args()

    report = generate_report(report_type=args.type, period=args.period, department=args.department)
    output = json.dumps(report, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Report skeleton written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
