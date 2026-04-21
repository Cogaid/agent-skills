#!/usr/bin/env python3
"""Generate an end-of-day review summary.

Usage:
    python end_of_day_review.py --user user123 --date today
    python end_of_day_review.py --user user123 --date 2025-01-15 --format json
"""

import argparse
import json
import sys
from datetime import datetime

SAMPLE_COMPLETED = [
    {"title": "Submit Q2 budget proposal", "priority": "P0", "completed_at": "10:30 AM"},
    {"title": "Review PR #342 - auth refactor", "priority": "P0", "completed_at": "11:45 AM"},
    {"title": "1:1 with Manager", "priority": "P1", "completed_at": "01:30 PM"},
    {"title": "Client Call - Acme", "priority": "P1", "completed_at": "03:45 PM"},
]

SAMPLE_INCOMPLETE = [
    {"title": "Update project roadmap", "priority": "P1", "reason": "Blocked by missing data from analytics team", "new_due": "tomorrow", "rollover_count": 1},
    {"title": "Write API documentation", "priority": "P1", "reason": "Ran out of time after client call", "new_due": "tomorrow", "rollover_count": 0},
]

SAMPLE_WINS = [
    "Budget proposal approved on first submission",
    "Client expressed interest in expanding scope for Q3",
]

SAMPLE_BLOCKERS = [
    {"blocker": "Analytics team hasn't shared Q1 data", "action": "Ping analytics lead tomorrow AM"},
    {"blocker": "Staging environment down since 2 PM", "action": "IT ticket #4521 filed, awaiting fix"},
]

FOCUS_GOALS = [
    {"goal": "Complete Q2 budget proposal", "completed": True},
    {"goal": "Prepare for client call", "completed": True},
    {"goal": "Clear code review backlog", "completed": False},
]


def generate_markdown_review(user: str, date_str: str) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append("              END-OF-DAY REVIEW")
    lines.append(f"              {date_str}")
    lines.append("=" * 60)
    lines.append("")

    goals_done = sum(1 for g in FOCUS_GOALS if g["completed"])
    tasks_done = len(SAMPLE_COMPLETED)
    tasks_total = tasks_done + len(SAMPLE_INCOMPLETE)

    lines.append("TODAY'S SCORECARD:")
    lines.append(f"  Focus Goals Completed: {goals_done}/3")
    lines.append(f"  Tasks Completed: {tasks_done}/{tasks_total}")
    lines.append(f"  Meetings Attended: 3/3")
    lines.append("")

    lines.append("-" * 60)
    lines.append("COMPLETED:")
    for task in SAMPLE_COMPLETED:
        lines.append(f"  [x] {task['title']} (completed {task['completed_at']})")
    lines.append("")

    lines.append("NOT COMPLETED (rolling to tomorrow):")
    for task in SAMPLE_INCOMPLETE:
        lines.append(f"  [ ] {task['title']} -- Reason: {task['reason']}")
        lines.append(f"      New priority: {task['priority']} | Rollover #{task['rollover_count'] + 1}")
    lines.append("")

    lines.append("-" * 60)
    lines.append("WINS:")
    for win in SAMPLE_WINS:
        lines.append(f"  - {win}")
    lines.append("")

    lines.append("BLOCKERS:")
    for b in SAMPLE_BLOCKERS:
        lines.append(f"  - {b['blocker']}")
        lines.append(f"    Action: {b['action']}")
    lines.append("")

    lines.append("-" * 60)
    lines.append("TOMORROW'S TOP PRIORITIES:")
    lines.append("  1. Update project roadmap (rolled over)")
    lines.append("  2. Write API documentation (rolled over)")
    lines.append("  3. Prepare weekly status report")
    lines.append("")

    lines.append("=" * 60)
    return "\n".join(lines)


def generate_json_review(user: str, date_str: str) -> dict:
    goals_done = sum(1 for g in FOCUS_GOALS if g["completed"])
    return {
        "user": user,
        "date": date_str,
        "generated_at": datetime.now().isoformat(),
        "scorecard": {
            "focus_goals_completed": goals_done,
            "focus_goals_total": len(FOCUS_GOALS),
            "tasks_completed": len(SAMPLE_COMPLETED),
            "tasks_total": len(SAMPLE_COMPLETED) + len(SAMPLE_INCOMPLETE),
            "meetings_attended": 3,
            "meetings_total": 3,
        },
        "completed_tasks": SAMPLE_COMPLETED,
        "incomplete_tasks": SAMPLE_INCOMPLETE,
        "wins": SAMPLE_WINS,
        "blockers": SAMPLE_BLOCKERS,
        "focus_goals": FOCUS_GOALS,
        "tomorrow_priorities": [
            "Update project roadmap (rolled over)",
            "Write API documentation (rolled over)",
            "Prepare weekly status report",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description="Generate end-of-day review summary.")
    parser.add_argument("--user", required=True, help="User ID or name")
    parser.add_argument("--date", default="today", help="Date for review (default: today)")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown", help="Output format")

    args = parser.parse_args()

    if args.date == "today":
        date_obj = datetime.now()
    else:
        date_obj = datetime.strptime(args.date, "%Y-%m-%d")

    date_str = date_obj.strftime("%A, %B %d, %Y")

    if args.format == "json":
        print(json.dumps(generate_json_review(args.user, date_str), indent=2))
    else:
        print(generate_markdown_review(args.user, date_str))


if __name__ == "__main__":
    main()
