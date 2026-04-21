#!/usr/bin/env python3
"""Generate a personalized morning briefing from connected sources.

Usage:
    python generate_briefing.py --user user123 --format markdown
    python generate_briefing.py --user user123 --format json --components calendar,tasks,email
"""

import argparse
import json
import sys
from datetime import datetime, timedelta

# Sample data simulating connected sources
SAMPLE_CALENDAR = [
    {"time": "09:00 AM", "event": "Team Standup", "duration": "30m", "location": "Zoom", "prep": "Review sprint board"},
    {"time": "11:00 AM", "event": "Product Review", "duration": "60m", "location": "Conf Room B", "prep": "Prepare demo slides"},
    {"time": "01:00 PM", "event": "1:1 with Manager", "duration": "30m", "location": "Zoom", "prep": "Update on project status"},
    {"time": "03:00 PM", "event": "Client Call - Acme", "duration": "45m", "location": "Teams", "prep": "Review proposal draft"},
]

SAMPLE_TASKS = [
    {"title": "Submit Q2 budget proposal", "priority": "P0", "due": "today", "context": "Finance needs by EOD"},
    {"title": "Review PR #342 - auth refactor", "priority": "P0", "due": "today", "context": "Blocking deployment"},
    {"title": "Update project roadmap", "priority": "P1", "due": "Wed", "context": "For leadership sync"},
    {"title": "Write API documentation", "priority": "P1", "due": "Thu", "context": "Sprint commitment"},
    {"title": "Organize shared drive folders", "priority": "P2", "due": "Fri", "context": "Team cleanup"},
]

SAMPLE_OVERDUE = [
    {"title": "Send vendor contract feedback", "original_due": "yesterday", "rollover_count": 1},
    {"title": "Complete compliance training", "original_due": "2 days ago", "rollover_count": 2},
]

SAMPLE_EMAILS = [
    {"sender": "CEO", "subject": "Q2 Strategy Update - Input Needed", "urgency": "high", "action": True},
    {"sender": "Client (Acme)", "subject": "Re: Proposal Questions", "urgency": "high", "action": True},
    {"sender": "HR", "subject": "Benefits Enrollment Reminder", "urgency": "low", "action": False},
]

SAMPLE_WEATHER = {"summary": "Partly cloudy", "high": "72F", "low": "58F"}
SAMPLE_COMMUTE = {"time": "25 min", "status": "normal traffic"}

SAMPLE_NEWS = [
    {"headline": "Fed signals interest rate pause through summer", "source": "Reuters"},
    {"headline": "New AI coding assistant benchmarks released", "source": "TechCrunch"},
    {"headline": "Global supply chain disruptions easing", "source": "Bloomberg"},
]


def generate_markdown_briefing(user: str, components: list[str], date_str: str) -> str:
    """Generate a formatted markdown briefing."""
    lines = []
    lines.append("=" * 60)
    lines.append("              DAILY BRIEFING")
    lines.append(f"              {date_str}")
    lines.append(f"              Good morning, {user}!")
    lines.append("=" * 60)
    lines.append("")

    lines.append("TODAY'S FOCUS (pick your top 3):")
    lines.append("  1. Complete Q2 budget proposal")
    lines.append("  2. Prepare for client call")
    lines.append("  3. Clear code review backlog")
    lines.append("")

    if "calendar" in components:
        lines.append("-" * 60)
        lines.append(f"CALENDAR ({len(SAMPLE_CALENDAR)} events today)")
        lines.append("")
        for event in SAMPLE_CALENDAR:
            lines.append(f"  {event['time']}  {event['event']} ({event['duration']})")
            lines.append(f"              Location: {event['location']}")
            if event.get("prep"):
                lines.append(f"              Prep: {event['prep']}")
            lines.append("")
        meeting_hours = 2.75
        focus_hours = 8 - meeting_hours - 1  # subtract lunch
        lines.append(f"  Total meeting time: {meeting_hours}h")
        lines.append(f"  Focus time available: {focus_hours}h")
        lines.append(f"  Free blocks: 10:00-11:00 AM, 1:30-3:00 PM, 3:45-5:00 PM")
        lines.append("")

    if "tasks" in components:
        lines.append("-" * 60)
        lines.append("PRIORITY TASKS")
        lines.append("")
        for task in SAMPLE_TASKS:
            lines.append(f"  [{task['priority']}] {task['title']} -- Due: {task['due']} -- {task['context']}")
        lines.append("")
        if SAMPLE_OVERDUE:
            lines.append("OVERDUE / ROLLED OVER (from yesterday):")
            for task in SAMPLE_OVERDUE:
                lines.append(f"  [!] {task['title']} -- Originally due: {task['original_due']} (rolled {task['rollover_count']}x)")
            lines.append("  Decision needed: Reschedule, delegate, or drop?")
            lines.append("")

    if "email" in components:
        lines.append("-" * 60)
        unread = len(SAMPLE_EMAILS)
        lines.append(f"EMAIL HIGHLIGHTS ({unread} flagged)")
        lines.append("")
        action_emails = [e for e in SAMPLE_EMAILS if e["action"]]
        fyi_emails = [e for e in SAMPLE_EMAILS if not e["action"]]
        if action_emails:
            lines.append("  Action Required:")
            for e in action_emails:
                lines.append(f"    - {e['sender']}: {e['subject']} ({e['urgency']})")
        if fyi_emails:
            lines.append("  FYI:")
            for e in fyi_emails:
                lines.append(f"    - {e['sender']}: {e['subject']}")
        lines.append("")

    if "weather" in components:
        lines.append("-" * 60)
        lines.append("CONDITIONS")
        lines.append(f"  Weather: {SAMPLE_WEATHER['summary']} | High: {SAMPLE_WEATHER['high']} Low: {SAMPLE_WEATHER['low']}")
        lines.append(f"  Commute: {SAMPLE_COMMUTE['time']} ({SAMPLE_COMMUTE['status']})")
        lines.append("")

    if "news" in components:
        lines.append("-" * 60)
        lines.append("NEWS DIGEST (top 3 relevant):")
        for i, item in enumerate(SAMPLE_NEWS, 1):
            lines.append(f"  {i}. {item['headline']} -- {item['source']}")
        lines.append("")

    lines.append("=" * 60)
    return "\n".join(lines)


def generate_json_briefing(user: str, components: list[str], date_str: str) -> dict:
    """Generate briefing data as structured JSON."""
    briefing = {
        "user": user,
        "date": date_str,
        "generated_at": datetime.now().isoformat(),
        "focus_goals": [
            "Complete Q2 budget proposal",
            "Prepare for client call",
            "Clear code review backlog",
        ],
    }

    if "calendar" in components:
        briefing["calendar"] = {
            "events": SAMPLE_CALENDAR,
            "event_count": len(SAMPLE_CALENDAR),
            "meeting_hours": 2.75,
            "focus_hours": 4.25,
            "free_blocks": ["10:00-11:00 AM", "1:30-3:00 PM", "3:45-5:00 PM"],
        }

    if "tasks" in components:
        briefing["tasks"] = {
            "priority_tasks": SAMPLE_TASKS,
            "overdue": SAMPLE_OVERDUE,
            "total_count": len(SAMPLE_TASKS) + len(SAMPLE_OVERDUE),
        }

    if "email" in components:
        briefing["email"] = {
            "highlights": SAMPLE_EMAILS,
            "unread_count": len(SAMPLE_EMAILS),
            "action_required": len([e for e in SAMPLE_EMAILS if e["action"]]),
        }

    if "weather" in components:
        briefing["weather"] = SAMPLE_WEATHER
        briefing["commute"] = SAMPLE_COMMUTE

    if "news" in components:
        briefing["news"] = SAMPLE_NEWS

    return briefing


def main():
    parser = argparse.ArgumentParser(
        description="Generate a personalized daily briefing from connected sources."
    )
    parser.add_argument("--user", required=True, help="User ID or name for personalization")
    parser.add_argument(
        "--format",
        choices=["markdown", "json"],
        default="markdown",
        help="Output format (default: markdown)",
    )
    parser.add_argument(
        "--components",
        default="calendar,tasks,email,weather,news",
        help="Comma-separated list of components to include (default: all)",
    )
    parser.add_argument(
        "--date",
        default=None,
        help="Date for briefing (default: today, format: YYYY-MM-DD)",
    )

    args = parser.parse_args()
    components = [c.strip() for c in args.components.split(",")]

    if args.date:
        date_obj = datetime.strptime(args.date, "%Y-%m-%d")
    else:
        date_obj = datetime.now()

    date_str = date_obj.strftime("%A, %B %d, %Y")

    if args.format == "json":
        result = generate_json_briefing(args.user, components, date_str)
        print(json.dumps(result, indent=2))
    else:
        result = generate_markdown_briefing(args.user, components, date_str)
        print(result)


if __name__ == "__main__":
    main()
