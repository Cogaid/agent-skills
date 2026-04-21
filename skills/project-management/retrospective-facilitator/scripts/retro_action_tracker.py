#!/usr/bin/env python3
"""Retrospective action item tracker.

Tracks action item completion across retrospectives, calculates
completion rates, identifies recurring themes, and reports on
improvement trends.

Usage:
    python retro_action_tracker.py --demo
    python retro_action_tracker.py --demo --json
    python retro_action_tracker.py --demo --sprint "Sprint 14"
"""

import argparse
import json
import sys
from datetime import date


SAMPLE_ACTIONS = [
    {"sprint": "Sprint 10", "description": "Set up CI/CD pipeline for automated deploys", "owner": "Alice", "status": "done", "created": "2026-02-01", "completed": "2026-02-14"},
    {"sprint": "Sprint 10", "description": "Create onboarding doc for new team members", "owner": "Bob", "status": "done", "created": "2026-02-01", "completed": "2026-02-10"},
    {"sprint": "Sprint 10", "description": "Reduce standup duration to 15 min", "owner": "Carol", "status": "in_progress", "created": "2026-02-01", "completed": ""},
    {"sprint": "Sprint 11", "description": "Implement WIP limits on board", "owner": "Alice", "status": "done", "created": "2026-02-15", "completed": "2026-02-28"},
    {"sprint": "Sprint 11", "description": "Add acceptance criteria to all stories before planning", "owner": "Dave", "status": "done", "created": "2026-02-15", "completed": "2026-03-01"},
    {"sprint": "Sprint 11", "description": "Schedule weekly design sync", "owner": "Eve", "status": "done", "created": "2026-02-15", "completed": "2026-02-20"},
    {"sprint": "Sprint 11", "description": "Investigate flaky test failures", "owner": "Bob", "status": "not_started", "created": "2026-02-15", "completed": ""},
    {"sprint": "Sprint 12", "description": "Pair programming on complex bugs", "owner": "Carol", "status": "done", "created": "2026-03-01", "completed": "2026-03-14"},
    {"sprint": "Sprint 12", "description": "Set up monitoring dashboard", "owner": "Alice", "status": "done", "created": "2026-03-01", "completed": "2026-03-10"},
    {"sprint": "Sprint 12", "description": "Document architecture decisions in ADRs", "owner": "Dave", "status": "done", "created": "2026-03-01", "completed": "2026-03-14"},
    {"sprint": "Sprint 13", "description": "Reduce context switching by batching meetings", "owner": "Eve", "status": "in_progress", "created": "2026-03-15", "completed": ""},
    {"sprint": "Sprint 13", "description": "Improve PR review turnaround to < 4 hours", "owner": "Bob", "status": "done", "created": "2026-03-15", "completed": "2026-03-25"},
    {"sprint": "Sprint 14", "description": "Add load testing to the CI pipeline", "owner": "Alice", "status": "in_progress", "created": "2026-03-29", "completed": ""},
    {"sprint": "Sprint 14", "description": "Create runbook for production incidents", "owner": "Carol", "status": "not_started", "created": "2026-03-29", "completed": ""},
    {"sprint": "Sprint 14", "description": "Cross-train on payment module", "owner": "Dave", "status": "done", "created": "2026-03-29", "completed": "2026-04-10"},
]

SAMPLE_THEMES = [
    {"theme": "Deployment friction", "sprints_raised": ["Sprint 10", "Sprint 11", "Sprint 12", "Sprint 13"], "status": "resolved", "resolution": "CI/CD pipeline implemented in Sprint 12"},
    {"theme": "Unclear requirements", "sprints_raised": ["Sprint 11", "Sprint 12", "Sprint 14"], "status": "in_progress", "resolution": "Added grooming session, PO writing ACs"},
    {"theme": "Context switching", "sprints_raised": ["Sprint 13", "Sprint 14"], "status": "monitoring", "resolution": "WIP limits introduced, meeting batching in progress"},
    {"theme": "Flaky tests", "sprints_raised": ["Sprint 11"], "status": "open", "resolution": "Investigation not started"},
]

SAMPLE_MOODS = [
    {"sprint": "Sprint 10", "average": 3.2, "event": "Team member left"},
    {"sprint": "Sprint 11", "average": 3.5, "event": "New hire onboarded"},
    {"sprint": "Sprint 12", "average": 4.0, "event": "Successful release"},
    {"sprint": "Sprint 13", "average": 3.8, "event": "Scope change mid-sprint"},
    {"sprint": "Sprint 14", "average": 4.1, "event": "Completed CI/CD improvement"},
]


def completion_rate(actions):
    """Calculate completion rate for a set of actions."""
    if not actions:
        return 0.0
    done = sum(1 for a in actions if a["status"] == "done")
    return round((done / len(actions)) * 100, 1)


def analyze_sprints(actions):
    """Analyze action items by sprint."""
    sprints = {}
    for a in actions:
        sprint = a["sprint"]
        if sprint not in sprints:
            sprints[sprint] = []
        sprints[sprint].append(a)

    results = []
    for sprint in sorted(sprints.keys()):
        items = sprints[sprint]
        done = sum(1 for i in items if i["status"] == "done")
        in_progress = sum(1 for i in items if i["status"] == "in_progress")
        not_started = sum(1 for i in items if i["status"] == "not_started")
        dropped = sum(1 for i in items if i["status"] == "dropped")

        results.append({
            "sprint": sprint,
            "total": len(items),
            "done": done,
            "in_progress": in_progress,
            "not_started": not_started,
            "dropped": dropped,
            "completion_rate": completion_rate(items),
        })
    return results


def analyze_themes(themes):
    """Analyze recurring themes."""
    analysis = []
    for t in themes:
        count = len(t["sprints_raised"])
        analysis.append({
            "theme": t["theme"],
            "times_raised": count,
            "status": t["status"],
            "resolution": t["resolution"],
            "persistent": count >= 3,
            "needs_escalation": count >= 3 and t["status"] not in ("resolved",),
        })
    return sorted(analysis, key=lambda x: x["times_raised"], reverse=True)


def analyze_moods(moods):
    """Analyze team mood trends."""
    if len(moods) < 2:
        return {"trend": "insufficient data", "moods": moods}

    values = [m["average"] for m in moods]
    first_half = sum(values[:len(values)//2]) / (len(values)//2)
    second_half = sum(values[len(values)//2:]) / (len(values) - len(values)//2)

    if second_half - first_half > 0.3:
        trend = "improving"
    elif first_half - second_half > 0.3:
        trend = "declining"
    else:
        trend = "stable"

    return {
        "trend": trend,
        "current": moods[-1]["average"] if moods else 0,
        "average": round(sum(values) / len(values), 1),
        "moods": moods,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Track retro action items and improvement trends",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Full demo report
  %(prog)s --demo

  # Filter by sprint
  %(prog)s --demo --sprint "Sprint 14"

  # JSON output
  %(prog)s --demo --json
        """,
    )
    parser.add_argument("--demo", action="store_true", help="Use sample retro data")
    parser.add_argument("--sprint", type=str, help="Filter to a specific sprint")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if not args.demo:
        print("Use --demo to run with sample data.")
        sys.exit(0)

    actions = SAMPLE_ACTIONS
    if args.sprint:
        actions = [a for a in actions if a["sprint"] == args.sprint]

    sprint_analysis = analyze_sprints(actions)
    theme_analysis = analyze_themes(SAMPLE_THEMES)
    mood_analysis = analyze_moods(SAMPLE_MOODS)

    overall_rate = completion_rate(actions)

    result = {
        "report_date": date.today().isoformat(),
        "overall_completion_rate": overall_rate,
        "total_actions": len(actions),
        "sprints": sprint_analysis,
        "themes": theme_analysis,
        "mood": mood_analysis,
    }

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("=" * 65)
        print("RETROSPECTIVE IMPROVEMENT REPORT")
        print("=" * 65)
        print()
        print(f"Overall completion rate: {overall_rate}%")
        print(f"Total actions tracked: {len(actions)}")
        print()

        print("ACTION ITEMS BY SPRINT")
        print("-" * 65)
        print(f"  {'Sprint':<14} {'Total':>6} {'Done':>6} {'In Prog':>8} {'Rate':>8}")
        for s in sprint_analysis:
            print(f"  {s['sprint']:<14} {s['total']:>6} {s['done']:>6} "
                  f"{s['in_progress']:>8} {s['completion_rate']:>7.0f}%")
        print()

        print("RECURRING THEMES")
        print("-" * 65)
        for t in theme_analysis:
            flag = " ** ESCALATE **" if t["needs_escalation"] else ""
            print(f"  {t['theme']:<30} Raised: {t['times_raised']}x | "
                  f"Status: {t['status']}{flag}")
        print()

        print("TEAM MOOD")
        print("-" * 65)
        print(f"  Trend: {mood_analysis['trend']}")
        print(f"  Current: {mood_analysis['current']} | Average: {mood_analysis['average']}")
        for m in mood_analysis["moods"]:
            bar = "#" * int(m["average"] * 4) + "." * (20 - int(m["average"] * 4))
            print(f"  {m['sprint']:<14} [{bar}] {m['average']:.1f}  {m['event']}")
        print()


if __name__ == "__main__":
    main()
