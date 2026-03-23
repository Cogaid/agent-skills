#!/usr/bin/env python3
"""
Track and analyze demo performance metrics.

Usage:
    python demo_analyzer.py demos.json
    python demo_analyzer.py --report weekly demos.json
    python demo_analyzer.py --sample

Output: Demo performance analysis and improvement recommendations
"""

import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime


# Benchmarks
BENCHMARKS = {
    "show_rate": {"good": 0.85, "great": 0.95},
    "demo_to_opportunity": {"good": 0.60, "great": 0.75},
    "demo_to_close": {"good": 0.25, "great": 0.40},
    "average_duration": {"target": 30, "max": 45},
    "follow_up_same_day": {"good": 0.90, "great": 1.0}
}


def load_data(file_path):
    """Load demo data from JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)


def calculate_metrics(demos):
    """Calculate overall demo metrics."""

    total_scheduled = len(demos)
    total_completed = sum(1 for d in demos if d.get("status") == "completed")
    total_no_show = sum(1 for d in demos if d.get("status") == "no_show")

    # Outcome tracking
    opportunities = sum(1 for d in demos if d.get("outcome") == "opportunity")
    closed_won = sum(1 for d in demos if d.get("outcome") == "closed_won")
    closed_lost = sum(1 for d in demos if d.get("outcome") == "closed_lost")

    # Duration analysis
    durations = [d.get("duration_minutes", 0) for d in demos if d.get("duration_minutes")]
    avg_duration = sum(durations) / len(durations) if durations else 0

    # Follow-up tracking
    same_day_followup = sum(1 for d in demos if d.get("follow_up_same_day", False))

    return {
        "summary": {
            "total_scheduled": total_scheduled,
            "total_completed": total_completed,
            "total_no_show": total_no_show
        },
        "rates": {
            "show_rate": round(total_completed / total_scheduled, 4) if total_scheduled else 0,
            "demo_to_opportunity": round(opportunities / total_completed, 4) if total_completed else 0,
            "demo_to_close": round(closed_won / total_completed, 4) if total_completed else 0,
            "win_rate": round(closed_won / (closed_won + closed_lost), 4) if (closed_won + closed_lost) else 0
        },
        "outcomes": {
            "opportunities": opportunities,
            "closed_won": closed_won,
            "closed_lost": closed_lost,
            "pending": total_completed - opportunities - closed_won - closed_lost
        },
        "efficiency": {
            "average_duration": round(avg_duration, 1),
            "follow_up_same_day_rate": round(same_day_followup / total_completed, 4) if total_completed else 0
        }
    }


def analyze_by_audience(demos):
    """Analyze performance by audience type."""

    audience_data = defaultdict(lambda: {
        "count": 0, "completed": 0, "opportunities": 0, "won": 0, "duration": []
    })

    for demo in demos:
        audience = demo.get("audience_type", "unknown")
        audience_data[audience]["count"] += 1

        if demo.get("status") == "completed":
            audience_data[audience]["completed"] += 1
            if demo.get("duration_minutes"):
                audience_data[audience]["duration"].append(demo["duration_minutes"])

        if demo.get("outcome") == "opportunity":
            audience_data[audience]["opportunities"] += 1
        if demo.get("outcome") == "closed_won":
            audience_data[audience]["won"] += 1

    results = {}
    for audience, data in audience_data.items():
        durations = data["duration"]
        results[audience] = {
            "demos": data["count"],
            "completed": data["completed"],
            "show_rate": round(data["completed"] / data["count"], 4) if data["count"] else 0,
            "opportunity_rate": round(data["opportunities"] / data["completed"], 4) if data["completed"] else 0,
            "win_rate": round(data["won"] / data["completed"], 4) if data["completed"] else 0,
            "avg_duration": round(sum(durations) / len(durations), 1) if durations else 0
        }

    return results


def analyze_by_rep(demos):
    """Analyze performance by sales rep."""

    rep_data = defaultdict(lambda: {
        "count": 0, "completed": 0, "opportunities": 0, "won": 0
    })

    for demo in demos:
        rep = demo.get("rep_name", "unknown")
        rep_data[rep]["count"] += 1

        if demo.get("status") == "completed":
            rep_data[rep]["completed"] += 1
        if demo.get("outcome") == "opportunity":
            rep_data[rep]["opportunities"] += 1
        if demo.get("outcome") == "closed_won":
            rep_data[rep]["won"] += 1

    results = {}
    for rep, data in rep_data.items():
        results[rep] = {
            "demos": data["count"],
            "completed": data["completed"],
            "opportunity_rate": round(data["opportunities"] / data["completed"], 4) if data["completed"] else 0,
            "win_rate": round(data["won"] / data["completed"], 4) if data["completed"] else 0
        }

    return dict(sorted(results.items(), key=lambda x: -x[1]["opportunity_rate"]))


def analyze_objections(demos):
    """Analyze common objections encountered."""

    objection_counts = defaultdict(int)
    objection_outcomes = defaultdict(lambda: {"overcome": 0, "lost": 0})

    for demo in demos:
        for objection in demo.get("objections", []):
            objection_type = objection.get("type", "other")
            objection_counts[objection_type] += 1

            if objection.get("overcome", False):
                objection_outcomes[objection_type]["overcome"] += 1
            else:
                objection_outcomes[objection_type]["lost"] += 1

    results = []
    for objection, count in sorted(objection_counts.items(), key=lambda x: -x[1]):
        outcomes = objection_outcomes[objection]
        total = outcomes["overcome"] + outcomes["lost"]
        results.append({
            "objection": objection,
            "count": count,
            "overcome_rate": round(outcomes["overcome"] / total, 4) if total else 0
        })

    return results


def compare_to_benchmarks(metrics):
    """Compare metrics to benchmarks."""

    comparison = {}

    for metric, thresholds in BENCHMARKS.items():
        if metric in metrics.get("rates", {}):
            value = metrics["rates"][metric]
            if "good" in thresholds:
                if value >= thresholds.get("great", 1):
                    status = "great"
                elif value >= thresholds["good"]:
                    status = "good"
                else:
                    status = "needs_improvement"
            else:
                status = "on_track" if value <= thresholds.get("max", 100) else "over_target"

            comparison[metric] = {
                "value": value,
                "status": status,
                "benchmark": thresholds
            }

    return comparison


def generate_recommendations(metrics, audience_analysis, objection_analysis):
    """Generate improvement recommendations."""

    recommendations = []

    # Show rate recommendations
    show_rate = metrics["rates"].get("show_rate", 0)
    if show_rate < 0.85:
        recommendations.append({
            "priority": "high",
            "area": "Show Rate",
            "issue": f"Show rate ({show_rate:.0%}) below 85%",
            "actions": [
                "Confirm meetings 24h and 1h before",
                "Send calendar invite with clear agenda",
                "Include video/dial-in details prominently",
                "Consider shorter demo duration"
            ]
        })

    # Demo-to-opportunity recommendations
    opp_rate = metrics["rates"].get("demo_to_opportunity", 0)
    if opp_rate < 0.60:
        recommendations.append({
            "priority": "high",
            "area": "Demo Effectiveness",
            "issue": f"Demo-to-opportunity rate ({opp_rate:.0%}) below 60%",
            "actions": [
                "Better qualify leads before demo",
                "More discovery during demo opening",
                "Focus on relevant use cases only",
                "End with clear next step"
            ]
        })

    # Duration recommendations
    avg_duration = metrics["efficiency"].get("average_duration", 0)
    if avg_duration > 45:
        recommendations.append({
            "priority": "medium",
            "area": "Demo Duration",
            "issue": f"Average duration ({avg_duration:.0f} min) exceeds 45 minutes",
            "actions": [
                "Tighten agenda and focus",
                "Cut less relevant features",
                "Use more concise explanations",
                "Ask more questions, talk less"
            ]
        })

    # Follow-up recommendations
    followup_rate = metrics["efficiency"].get("follow_up_same_day_rate", 0)
    if followup_rate < 0.90:
        recommendations.append({
            "priority": "medium",
            "area": "Follow-Up",
            "issue": f"Same-day follow-up rate ({followup_rate:.0%}) below 90%",
            "actions": [
                "Prepare follow-up template in advance",
                "Block 15 min after each demo for follow-up",
                "Use CRM automation for reminders"
            ]
        })

    # Objection handling
    if objection_analysis:
        lowest = min(objection_analysis, key=lambda x: x["overcome_rate"])
        if lowest["overcome_rate"] < 0.50 and lowest["count"] >= 5:
            recommendations.append({
                "priority": "high",
                "area": "Objection Handling",
                "issue": f"'{lowest['objection']}' overcome rate only {lowest['overcome_rate']:.0%}",
                "actions": [
                    "Develop better response to this objection",
                    "Proactively address in demo",
                    "Create supporting materials",
                    "Practice with team"
                ]
            })

    return recommendations


def generate_report(analysis, format_type="text"):
    """Generate formatted analysis report."""

    if format_type == "json":
        return json.dumps(analysis, indent=2)

    lines = []
    lines.append("\n" + "=" * 60)
    lines.append("DEMO PERFORMANCE ANALYSIS")
    lines.append("=" * 60)

    # Summary
    if "metrics" in analysis:
        m = analysis["metrics"]
        lines.append("\n--- SUMMARY ---")
        lines.append(f"Demos Scheduled: {m['summary']['total_scheduled']}")
        lines.append(f"Demos Completed: {m['summary']['total_completed']}")
        lines.append(f"No Shows: {m['summary']['total_no_show']}")

        lines.append("\n--- KEY RATES ---")
        lines.append(f"Show Rate: {m['rates']['show_rate']:.1%}")
        lines.append(f"Demo → Opportunity: {m['rates']['demo_to_opportunity']:.1%}")
        lines.append(f"Demo → Close: {m['rates']['demo_to_close']:.1%}")

        lines.append("\n--- OUTCOMES ---")
        lines.append(f"Opportunities: {m['outcomes']['opportunities']}")
        lines.append(f"Closed Won: {m['outcomes']['closed_won']}")
        lines.append(f"Closed Lost: {m['outcomes']['closed_lost']}")

    # Benchmark comparison
    if "benchmarks" in analysis:
        lines.append("\n--- VS BENCHMARKS ---")
        for metric, data in analysis["benchmarks"].items():
            icon = "✓" if data["status"] in ["good", "great", "on_track"] else "✗"
            lines.append(f"{icon} {metric}: {data['value']:.1%} ({data['status']})")

    # By audience
    if "by_audience" in analysis:
        lines.append("\n--- BY AUDIENCE TYPE ---")
        for audience, data in analysis["by_audience"].items():
            lines.append(f"\n  {audience.upper()}:")
            lines.append(f"    Demos: {data['demos']}")
            lines.append(f"    Opportunity Rate: {data['opportunity_rate']:.1%}")
            lines.append(f"    Avg Duration: {data['avg_duration']:.0f} min")

    # Top objections
    if "objections" in analysis and analysis["objections"]:
        lines.append("\n--- TOP OBJECTIONS ---")
        for obj in analysis["objections"][:5]:
            lines.append(f"  {obj['objection']}: {obj['count']}x (overcome {obj['overcome_rate']:.0%})")

    # Recommendations
    if "recommendations" in analysis:
        lines.append("\n--- RECOMMENDATIONS ---")
        for rec in sorted(analysis["recommendations"], key=lambda x: x["priority"]):
            lines.append(f"\n[{rec['priority'].upper()}] {rec['area']}")
            lines.append(f"  Issue: {rec['issue']}")
            for action in rec["actions"][:2]:
                lines.append(f"  → {action}")

    lines.append("\n" + "=" * 60)
    return "\n".join(lines)


def generate_sample_data():
    """Generate sample demo data."""

    return [
        {
            "date": "2025-01-15",
            "company": "Acme Corp",
            "rep_name": "Sarah Chen",
            "audience_type": "executive",
            "status": "completed",
            "duration_minutes": 25,
            "outcome": "opportunity",
            "follow_up_same_day": True,
            "objections": []
        },
        {
            "date": "2025-01-16",
            "company": "TechStart Inc",
            "rep_name": "Mike Johnson",
            "audience_type": "technical",
            "status": "completed",
            "duration_minutes": 55,
            "outcome": "closed_won",
            "follow_up_same_day": True,
            "objections": [{"type": "integration", "overcome": True}]
        },
        {
            "date": "2025-01-17",
            "company": "BigCo Ltd",
            "rep_name": "Sarah Chen",
            "audience_type": "committee",
            "status": "completed",
            "duration_minutes": 45,
            "outcome": "closed_lost",
            "follow_up_same_day": False,
            "objections": [{"type": "pricing", "overcome": False}, {"type": "timing", "overcome": False}]
        },
        {
            "date": "2025-01-18",
            "company": "StartupXYZ",
            "rep_name": "Mike Johnson",
            "audience_type": "manager",
            "status": "no_show",
            "duration_minutes": None,
            "outcome": None,
            "follow_up_same_day": False,
            "objections": []
        },
        {
            "date": "2025-01-19",
            "company": "Enterprise Co",
            "rep_name": "Sarah Chen",
            "audience_type": "executive",
            "status": "completed",
            "duration_minutes": 22,
            "outcome": "opportunity",
            "follow_up_same_day": True,
            "objections": [{"type": "competitor", "overcome": True}]
        }
    ]


def main():
    parser = argparse.ArgumentParser(description='Analyze demo performance')
    parser.add_argument('file', nargs='?', help='Demo data file (JSON)')
    parser.add_argument('--report', '-r', choices=['summary', 'detailed', 'weekly'],
                        default='summary', help='Report type')
    parser.add_argument('--format', '-f', choices=['json', 'text'],
                        default='text', help='Output format')
    parser.add_argument('--sample', '-s', action='store_true',
                        help='Generate sample data')

    args = parser.parse_args()

    if args.sample:
        print(json.dumps(generate_sample_data(), indent=2))
        return

    if not args.file:
        parser.print_help()
        return

    try:
        demos = load_data(args.file)
    except FileNotFoundError:
        print(json.dumps({"error": f"File not found: {args.file}"}))
        sys.exit(1)

    # Run analysis
    metrics = calculate_metrics(demos)
    audience_analysis = analyze_by_audience(demos)
    rep_analysis = analyze_by_rep(demos)
    objection_analysis = analyze_objections(demos)
    benchmark_comparison = compare_to_benchmarks(metrics)
    recommendations = generate_recommendations(metrics, audience_analysis, objection_analysis)

    analysis = {
        "metrics": metrics,
        "by_audience": audience_analysis,
        "by_rep": rep_analysis,
        "objections": objection_analysis,
        "benchmarks": benchmark_comparison,
        "recommendations": recommendations
    }

    print(generate_report(analysis, args.format))


if __name__ == '__main__':
    main()
