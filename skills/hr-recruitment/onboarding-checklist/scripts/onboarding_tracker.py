#!/usr/bin/env python3
"""
Onboarding Health Tracker

Tracks onboarding progress, calculates completion rates, identifies
overdue items, and generates health reports with risk indicators.

Usage:
    python onboarding_tracker.py --demo
    python onboarding_tracker.py --data onboarding_data.json
    python onboarding_tracker.py --data onboarding_data.json --format summary
"""

import argparse
import json
import sys
from datetime import datetime, timedelta

# --- Sample Data ---

SAMPLE_DATA = {
    "employee": {
        "name": "Alex Rivera",
        "role": "Senior Software Engineer",
        "department": "Engineering",
        "manager": "Sarah Chen",
        "buddy": "Jamie Park",
        "start_date": "2026-04-06",
        "work_arrangement": "hybrid",
    },
    "current_date": "2026-04-20",
    "tasks": {
        "pre_boarding": [
            {"task": "Send welcome email", "owner": "HR", "due": "2026-03-27", "status": "complete", "completed_date": "2026-03-25"},
            {"task": "Ship equipment", "owner": "IT", "due": "2026-04-01", "status": "complete", "completed_date": "2026-03-30"},
            {"task": "Create accounts and access", "owner": "IT", "due": "2026-04-03", "status": "complete", "completed_date": "2026-04-03"},
            {"task": "Send personal welcome from manager", "owner": "Manager", "due": "2026-03-30", "status": "complete", "completed_date": "2026-04-02"},
            {"task": "Assign onboarding buddy", "owner": "Manager", "due": "2026-03-30", "status": "complete", "completed_date": "2026-03-28"},
            {"task": "Draft 30-60-90 day plan", "owner": "Manager", "due": "2026-04-03", "status": "complete", "completed_date": "2026-04-05"},
        ],
        "week_1": [
            {"task": "Complete HR paperwork", "owner": "New Hire", "due": "2026-04-10", "status": "complete", "completed_date": "2026-04-07"},
            {"task": "Access all required tools", "owner": "IT", "due": "2026-04-08", "status": "complete", "completed_date": "2026-04-08"},
            {"task": "Meet all team members", "owner": "New Hire", "due": "2026-04-10", "status": "complete", "completed_date": "2026-04-09"},
            {"task": "First 1:1 with manager", "owner": "Manager", "due": "2026-04-10", "status": "complete", "completed_date": "2026-04-08"},
            {"task": "Buddy introduction and tour", "owner": "Buddy", "due": "2026-04-07", "status": "complete", "completed_date": "2026-04-06"},
            {"task": "Complete security training", "owner": "New Hire", "due": "2026-04-10", "status": "complete", "completed_date": "2026-04-10"},
            {"task": "Review team OKRs", "owner": "New Hire", "due": "2026-04-10", "status": "complete", "completed_date": "2026-04-09"},
        ],
        "month_1": [
            {"task": "Complete all training modules", "owner": "New Hire", "due": "2026-04-30", "status": "in_progress", "completed_date": None},
            {"task": "Ship first deliverable / quick win", "owner": "New Hire", "due": "2026-04-30", "status": "in_progress", "completed_date": None},
            {"task": "Attend cross-functional meetings", "owner": "New Hire", "due": "2026-04-25", "status": "complete", "completed_date": "2026-04-15"},
            {"task": "Build relationships outside team (5+)", "owner": "New Hire", "due": "2026-04-30", "status": "in_progress", "completed_date": None},
            {"task": "Week 1 feedback survey completed", "owner": "New Hire", "due": "2026-04-13", "status": "complete", "completed_date": "2026-04-12"},
            {"task": "Receive first informal feedback", "owner": "Manager", "due": "2026-04-20", "status": "overdue", "completed_date": None},
            {"task": "Set up dev environment", "owner": "New Hire", "due": "2026-04-13", "status": "complete", "completed_date": "2026-04-11"},
            {"task": "Submit first PR", "owner": "New Hire", "due": "2026-04-20", "status": "complete", "completed_date": "2026-04-16"},
        ],
        "month_2": [
            {"task": "Own a meaningful project", "owner": "New Hire", "due": "2026-05-15", "status": "not_started", "completed_date": None},
            {"task": "Present work to team", "owner": "New Hire", "due": "2026-05-31", "status": "not_started", "completed_date": None},
            {"task": "Midpoint check-in with manager", "owner": "Manager", "due": "2026-05-15", "status": "not_started", "completed_date": None},
            {"task": "Reduce dependency on buddy", "owner": "New Hire", "due": "2026-05-31", "status": "not_started", "completed_date": None},
        ],
        "month_3": [
            {"task": "Operate independently", "owner": "New Hire", "due": "2026-06-30", "status": "not_started", "completed_date": None},
            {"task": "Deliver measurable outcome", "owner": "New Hire", "due": "2026-06-30", "status": "not_started", "completed_date": None},
            {"task": "90-day review with manager", "owner": "Manager", "due": "2026-07-03", "status": "not_started", "completed_date": None},
            {"task": "Complete 90-day feedback survey", "owner": "New Hire", "due": "2026-07-03", "status": "not_started", "completed_date": None},
            {"task": "Set next quarter goals", "owner": "Manager", "due": "2026-07-03", "status": "not_started", "completed_date": None},
        ],
    },
    "check_ins": {
        "manager_1on1s": [
            {"date": "2026-04-08", "occurred": True, "notes": "Great first week energy"},
            {"date": "2026-04-15", "occurred": True, "notes": "Making good progress on codebase ramp"},
            {"date": "2026-04-22", "occurred": False, "notes": ""},
        ],
        "buddy_checkins": [
            {"date": "2026-04-06", "occurred": True},
            {"date": "2026-04-07", "occurred": True},
            {"date": "2026-04-08", "occurred": True},
            {"date": "2026-04-09", "occurred": True},
            {"date": "2026-04-10", "occurred": True},
            {"date": "2026-04-14", "occurred": True},
            {"date": "2026-04-17", "occurred": False},
        ],
    },
    "survey_responses": {
        "week_1": {
            "welcome_feeling": 5,
            "equipment_ready": "yes",
            "tools_access": "mostly",
            "role_clarity": 4,
            "buddy_helpfulness": 5,
            "overall_quality": 4,
            "best_part": "Team lunch and buddy pairing were great",
            "improvement": "Some tools took until Day 3 to get access",
        },
    },
}


def calculate_phase_stats(tasks, current_date_str):
    """Calculate completion stats for a phase."""
    current_date = datetime.strptime(current_date_str, "%Y-%m-%d")
    total = len(tasks)
    complete = sum(1 for t in tasks if t["status"] == "complete")
    in_progress = sum(1 for t in tasks if t["status"] == "in_progress")
    overdue = sum(1 for t in tasks if t["status"] in ("in_progress", "not_started", "overdue")
                  and datetime.strptime(t["due"], "%Y-%m-%d") < current_date)
    not_started = sum(1 for t in tasks if t["status"] == "not_started")

    return {
        "total": total,
        "complete": complete,
        "in_progress": in_progress,
        "overdue": overdue,
        "not_started": not_started,
        "completion_rate": round(complete / total * 100, 1) if total > 0 else 0,
    }


def identify_overdue_items(all_tasks, current_date_str):
    """Find all overdue tasks across phases."""
    current_date = datetime.strptime(current_date_str, "%Y-%m-%d")
    overdue = []
    for phase, tasks in all_tasks.items():
        for task in tasks:
            due_date = datetime.strptime(task["due"], "%Y-%m-%d")
            if task["status"] in ("in_progress", "not_started", "overdue") and due_date < current_date:
                days_overdue = (current_date - due_date).days
                overdue.append({
                    "phase": phase,
                    "task": task["task"],
                    "owner": task["owner"],
                    "due": task["due"],
                    "days_overdue": days_overdue,
                    "severity": "high" if days_overdue > 7 else "medium" if days_overdue > 3 else "low",
                })
    overdue.sort(key=lambda x: x["days_overdue"], reverse=True)
    return overdue


def check_in_health(check_ins):
    """Analyze check-in frequency and consistency."""
    results = {}

    for check_type, meetings in check_ins.items():
        total = len(meetings)
        occurred = sum(1 for m in meetings if m["occurred"])
        missed = total - occurred
        consecutive_missed = 0
        max_consecutive = 0
        for m in reversed(meetings):
            if not m["occurred"]:
                consecutive_missed += 1
                max_consecutive = max(max_consecutive, consecutive_missed)
            else:
                consecutive_missed = 0

        results[check_type] = {
            "total_scheduled": total,
            "occurred": occurred,
            "missed": missed,
            "attendance_rate": round(occurred / total * 100, 1) if total > 0 else 0,
            "consecutive_missed_recent": consecutive_missed,
            "max_consecutive_missed": max_consecutive,
            "status": "healthy" if consecutive_missed == 0 else "at_risk" if consecutive_missed == 1 else "critical",
        }

    return results


def calculate_days_since_start(start_date_str, current_date_str):
    """Calculate calendar days since start."""
    start = datetime.strptime(start_date_str, "%Y-%m-%d")
    current = datetime.strptime(current_date_str, "%Y-%m-%d")
    return (current - start).days


def generate_health_report(data):
    """Generate a comprehensive onboarding health report."""
    employee = data["employee"]
    current_date = data["current_date"]
    tasks = data["tasks"]

    days_since_start = calculate_days_since_start(employee["start_date"], current_date)

    # Phase stats
    phase_stats = {}
    for phase, phase_tasks in tasks.items():
        phase_stats[phase] = calculate_phase_stats(phase_tasks, current_date)

    # Overall stats
    all_tasks_flat = [t for phase_tasks in tasks.values() for t in phase_tasks]
    overall_stats = calculate_phase_stats(all_tasks_flat, current_date)

    # Overdue items
    overdue_items = identify_overdue_items(tasks, current_date)

    # Check-in health
    checkin_health = check_in_health(data.get("check_ins", {}))

    # Risk assessment
    risks = []
    if overall_stats["overdue"] > 0:
        risks.append({
            "level": "medium" if overall_stats["overdue"] <= 2 else "high",
            "category": "task_completion",
            "message": f"{overall_stats['overdue']} task(s) overdue",
        })

    for check_type, health in checkin_health.items():
        if health["status"] == "critical":
            risks.append({
                "level": "high",
                "category": "engagement",
                "message": f"{check_type}: {health['consecutive_missed_recent']} consecutive missed check-ins",
            })
        elif health["status"] == "at_risk":
            risks.append({
                "level": "medium",
                "category": "engagement",
                "message": f"{check_type}: missed most recent check-in",
            })

    survey = data.get("survey_responses", {})
    if "week_1" in survey:
        w1 = survey["week_1"]
        low_scores = []
        for key, val in w1.items():
            if isinstance(val, int) and val < 3:
                low_scores.append(key)
        if low_scores:
            risks.append({
                "level": "high",
                "category": "satisfaction",
                "message": f"Low Week 1 survey scores in: {', '.join(low_scores)}",
            })

    # Determine current phase
    if days_since_start <= 7:
        current_phase = "week_1"
    elif days_since_start <= 30:
        current_phase = "month_1"
    elif days_since_start <= 60:
        current_phase = "month_2"
    else:
        current_phase = "month_3"

    # Overall health score (0-100)
    health_score = 100
    health_score -= overall_stats["overdue"] * 10
    for check_type, health in checkin_health.items():
        if health["status"] == "critical":
            health_score -= 20
        elif health["status"] == "at_risk":
            health_score -= 10
    health_score = max(0, min(100, health_score))

    return {
        "report_date": current_date,
        "employee": employee,
        "days_since_start": days_since_start,
        "current_phase": current_phase,
        "health_score": health_score,
        "health_status": "healthy" if health_score >= 80 else "at_risk" if health_score >= 60 else "critical",
        "overall_stats": overall_stats,
        "phase_stats": phase_stats,
        "overdue_items": overdue_items,
        "check_in_health": checkin_health,
        "survey_responses": survey,
        "risks": risks,
        "recommendations": generate_recommendations(risks, overdue_items, checkin_health, days_since_start),
    }


def generate_recommendations(risks, overdue_items, checkin_health, days_since_start):
    """Generate actionable recommendations based on health data."""
    recommendations = []

    for item in overdue_items:
        recommendations.append({
            "priority": "high" if item["days_overdue"] > 5 else "medium",
            "action": f"Complete overdue task: '{item['task']}' (owner: {item['owner']}, {item['days_overdue']} days overdue)",
        })

    for check_type, health in checkin_health.items():
        if health["consecutive_missed_recent"] > 0:
            recommendations.append({
                "priority": "high",
                "action": f"Resume {check_type.replace('_', ' ')} immediately. Missed {health['consecutive_missed_recent']} recent session(s).",
            })

    if days_since_start > 14 and days_since_start <= 30:
        recommendations.append({
            "priority": "medium",
            "action": "Ensure first informal feedback has been delivered to new hire.",
        })

    if days_since_start > 25:
        recommendations.append({
            "priority": "low",
            "action": "Prepare for 30-day check-in. Gather feedback from buddy and cross-functional contacts.",
        })

    recommendations.sort(key=lambda x: {"high": 0, "medium": 1, "low": 2}.get(x["priority"], 3))
    return recommendations


def print_summary(report):
    """Print a human-readable health report."""
    e = report["employee"]
    print(f"=== ONBOARDING HEALTH REPORT ===")
    print(f"Employee: {e['name']} ({e['role']})")
    print(f"Manager: {e['manager']} | Buddy: {e['buddy']}")
    print(f"Start Date: {e['start_date']} | Day {report['days_since_start']}")
    print(f"Current Phase: {report['current_phase']}")
    print(f"")
    print(f"HEALTH SCORE: {report['health_score']}/100 ({report['health_status'].upper()})")
    print(f"")

    print(f"Task Completion:")
    for phase, stats in report["phase_stats"].items():
        bar = "#" * int(stats["completion_rate"] / 5) + "." * (20 - int(stats["completion_rate"] / 5))
        print(f"  {phase:<15} [{bar}] {stats['completion_rate']:>5.1f}% ({stats['complete']}/{stats['total']})")
    print(f"  {'OVERALL':<15} {report['overall_stats']['completion_rate']:>28.1f}% ({report['overall_stats']['complete']}/{report['overall_stats']['total']})")

    if report["overdue_items"]:
        print(f"\nOverdue Items ({len(report['overdue_items'])}):")
        for item in report["overdue_items"]:
            print(f"  [{item['severity'].upper()}] {item['task']} (owner: {item['owner']}, {item['days_overdue']} days late)")

    print(f"\nCheck-in Health:")
    for check_type, health in report["check_in_health"].items():
        print(f"  {check_type}: {health['attendance_rate']:.0f}% attendance ({health['occurred']}/{health['total_scheduled']}) - {health['status'].upper()}")

    if report["risks"]:
        print(f"\nRisks ({len(report['risks'])}):")
        for risk in report["risks"]:
            print(f"  [{risk['level'].upper()}] {risk['message']}")

    if report["recommendations"]:
        print(f"\nRecommendations:")
        for i, rec in enumerate(report["recommendations"], 1):
            print(f"  {i}. [{rec['priority'].upper()}] {rec['action']}")


def main():
    parser = argparse.ArgumentParser(
        description="Track onboarding progress and generate health reports."
    )
    parser.add_argument("--data", help="Path to JSON file with onboarding data")
    parser.add_argument("--demo", action="store_true", help="Run with sample data")
    parser.add_argument("--format", choices=["json", "summary"], default="json", help="Output format")

    args = parser.parse_args()

    if args.demo:
        data = SAMPLE_DATA
    elif args.data:
        try:
            with open(args.data, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(json.dumps({"error": str(e)}))
            sys.exit(1)
    else:
        parser.error("Either --demo or --data is required")
        sys.exit(1)

    report = generate_health_report(data)

    if args.format == "summary":
        print_summary(report)
    else:
        print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
