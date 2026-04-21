#!/usr/bin/env python3
"""RAG status calculator for project reporting.

Assesses RAG (Red/Amber/Green) status across multiple project dimensions
using configurable thresholds. Outputs a structured assessment with
trend analysis and recommendations.

Usage:
    python rag_calculator.py --demo
    python rag_calculator.py --schedule-variance 8 --budget-variance 12 --defect-rate 3
    python rag_calculator.py --demo --json
"""

import argparse
import json
import sys
from datetime import date


DEFAULT_THRESHOLDS = {
    "schedule": {"green_max": 5, "amber_max": 15, "unit": "%"},
    "budget": {"green_max": 5, "amber_max": 15, "unit": "%"},
    "scope": {"green_max": 5, "amber_max": 15, "unit": "% change"},
    "quality": {"green_max": 5, "amber_max": 15, "unit": "% defect rate"},
    "resources": {"green_max": 0, "amber_max": 1, "unit": "open positions"},
}


def assess_dimension(name, actual, planned, thresholds=None):
    """Assess RAG status for a single dimension."""
    if thresholds is None:
        thresholds = DEFAULT_THRESHOLDS.get(name, DEFAULT_THRESHOLDS["schedule"])

    if planned == 0:
        variance_pct = 0
    else:
        variance_pct = abs((actual - planned) / planned) * 100

    if variance_pct <= thresholds["green_max"]:
        status = "GREEN"
    elif variance_pct <= thresholds["amber_max"]:
        status = "AMBER"
    else:
        status = "RED"

    return {
        "dimension": name,
        "actual": actual,
        "planned": planned,
        "variance": round(actual - planned, 2),
        "variance_pct": round(variance_pct, 1),
        "status": status,
        "threshold_unit": thresholds["unit"],
    }


def determine_overall_status(assessments):
    """Determine overall project RAG from dimension assessments."""
    statuses = [a["status"] for a in assessments]
    red_count = statuses.count("RED")
    amber_count = statuses.count("AMBER")

    if red_count > 0:
        overall = "RED"
        rationale = f"{red_count} dimension(s) at RED status"
    elif amber_count >= 2:
        overall = "AMBER"
        rationale = f"{amber_count} dimensions at AMBER - trending toward RED"
    elif amber_count == 1:
        overall = "AMBER"
        rationale = "1 dimension at AMBER - monitoring required"
    else:
        overall = "GREEN"
        rationale = "All dimensions within acceptable thresholds"

    return {
        "status": overall,
        "rationale": rationale,
        "red_count": red_count,
        "amber_count": amber_count,
        "green_count": statuses.count("GREEN"),
    }


def add_trend(current_status, previous_status=None):
    """Calculate trend arrow based on status change."""
    if previous_status is None:
        return "--"
    status_order = {"GREEN": 0, "AMBER": 1, "RED": 2}
    current_val = status_order.get(current_status, 0)
    previous_val = status_order.get(previous_status, 0)
    if current_val < previous_val:
        return "IMPROVING"
    elif current_val > previous_val:
        return "DECLINING"
    return "STABLE"


def generate_recommendations(assessments, overall):
    """Generate actionable recommendations based on assessment."""
    recommendations = []
    for a in assessments:
        if a["status"] == "RED":
            recommendations.append({
                "priority": "HIGH",
                "dimension": a["dimension"],
                "action": f"Immediate recovery plan needed for {a['dimension']} "
                          f"(variance: {a['variance_pct']}%)",
            })
        elif a["status"] == "AMBER":
            recommendations.append({
                "priority": "MEDIUM",
                "dimension": a["dimension"],
                "action": f"Monitor {a['dimension']} closely; prepare contingency "
                          f"(variance: {a['variance_pct']}%)",
            })
    if not recommendations:
        recommendations.append({
            "priority": "LOW",
            "dimension": "all",
            "action": "Continue as planned; all dimensions within thresholds",
        })
    return recommendations


DEMO_DATA = {
    "schedule": {"actual": 42, "planned": 40, "previous_status": "GREEN"},
    "budget": {"actual": 283000, "planned": 270000, "previous_status": "GREEN"},
    "scope": {"actual": 52, "planned": 50, "previous_status": "GREEN"},
    "quality": {"actual": 3, "planned": 2, "previous_status": "GREEN"},
    "resources": {"actual": 4, "planned": 5, "previous_status": "AMBER"},
}


def main():
    parser = argparse.ArgumentParser(
        description="RAG status calculator for project reporting",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run with demo data
  %(prog)s --demo

  # Custom assessment
  %(prog)s --schedule-actual 42 --schedule-planned 40 \\
           --budget-actual 283000 --budget-planned 270000

  # JSON output
  %(prog)s --demo --json
        """,
    )
    parser.add_argument("--demo", action="store_true", help="Run with sample project data")
    parser.add_argument("--schedule-actual", type=float, help="Schedule actual (days elapsed)")
    parser.add_argument("--schedule-planned", type=float, help="Schedule planned (days)")
    parser.add_argument("--budget-actual", type=float, help="Budget actual spend")
    parser.add_argument("--budget-planned", type=float, help="Budget planned")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.demo:
        data = DEMO_DATA
    elif args.schedule_actual and args.schedule_planned:
        data = {
            "schedule": {"actual": args.schedule_actual, "planned": args.schedule_planned},
            "budget": {"actual": args.budget_actual or 0, "planned": args.budget_planned or 1},
        }
    else:
        print("Use --demo for sample data or provide --schedule-actual and --schedule-planned.")
        sys.exit(1)

    assessments = []
    for dim_name, dim_data in data.items():
        assessment = assess_dimension(dim_name, dim_data["actual"], dim_data["planned"])
        assessment["trend"] = add_trend(
            assessment["status"], dim_data.get("previous_status")
        )
        assessments.append(assessment)

    overall = determine_overall_status(assessments)
    recommendations = generate_recommendations(assessments, overall)

    result = {
        "report_date": date.today().isoformat(),
        "overall": overall,
        "dimensions": assessments,
        "recommendations": recommendations,
    }

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("=" * 65)
        print(f"PROJECT RAG ASSESSMENT - {result['report_date']}")
        print("=" * 65)
        print()
        print(f"OVERALL STATUS: {overall['status']}")
        print(f"Rationale: {overall['rationale']}")
        print()
        print(f"{'Dimension':<12} {'Status':<8} {'Actual':>10} {'Planned':>10} {'Variance':>10} {'Trend':<12}")
        print("-" * 65)
        for a in assessments:
            print(
                f"{a['dimension']:<12} {a['status']:<8} {a['actual']:>10.0f} "
                f"{a['planned']:>10.0f} {a['variance_pct']:>9.1f}% {a['trend']:<12}"
            )
        print()
        print("RECOMMENDATIONS")
        print("-" * 65)
        for r in recommendations:
            print(f"  [{r['priority']}] {r['action']}")
        print()


if __name__ == "__main__":
    main()
