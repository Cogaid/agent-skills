#!/usr/bin/env python3
"""Create and manage reminders with smart scheduling.

Usage:
    python reminder_manager.py --create --title "Follow up with John" --when "2025-01-20 10:00"
    python reminder_manager.py --list --status pending
    python reminder_manager.py --due-today
    python reminder_manager.py --example --format json
"""

import argparse
import json
import sys
from datetime import datetime, timedelta

SAMPLE_REMINDERS = [
    {
        "id": "R001",
        "title": "Follow up with John re: proposal",
        "type": "follow-up",
        "priority": "high",
        "status": "pending",
        "trigger": "2025-01-20T10:00:00",
        "context": "Sent proposal on Jan 15. No response yet after 5 days.",
        "category": "work",
        "snooze_count": 0,
        "created_at": "2025-01-15T09:00:00",
    },
    {
        "id": "R002",
        "title": "Submit expense report",
        "type": "time-based",
        "priority": "normal",
        "status": "due",
        "trigger": "2025-01-17T17:00:00",
        "context": "Monthly expense report due by end of business Friday.",
        "category": "work",
        "snooze_count": 1,
        "created_at": "2025-01-14T08:00:00",
    },
    {
        "id": "R003",
        "title": "Take daily vitamin",
        "type": "recurring",
        "priority": "normal",
        "status": "pending",
        "trigger": "daily at 08:00",
        "context": "Morning vitamin routine with breakfast.",
        "category": "health",
        "snooze_count": 0,
        "created_at": "2025-01-01T08:00:00",
    },
    {
        "id": "R004",
        "title": "Prepare slides for client presentation",
        "type": "event-based",
        "priority": "high",
        "status": "pending",
        "trigger": "2025-01-21T09:00:00 (1 day before meeting)",
        "context": "Client presentation on Jan 22 at 2 PM. Need 10-slide deck.",
        "category": "work",
        "snooze_count": 0,
        "created_at": "2025-01-15T10:00:00",
    },
    {
        "id": "R005",
        "title": "Pay electricity bill",
        "type": "time-based",
        "priority": "normal",
        "status": "overdue",
        "trigger": "2025-01-15T12:00:00",
        "context": "Monthly electricity bill. Amount: $145. Auto-pay not set up.",
        "category": "finance",
        "snooze_count": 2,
        "created_at": "2025-01-12T08:00:00",
    },
    {
        "id": "R006",
        "title": "Call Mom for birthday",
        "type": "time-based",
        "priority": "high",
        "status": "pending",
        "trigger": "2025-01-25T10:00:00",
        "context": "Mom's birthday is Jan 25. Call in the morning.",
        "category": "social",
        "snooze_count": 0,
        "created_at": "2025-01-18T08:00:00",
    },
]


def create_reminder(title: str, when: str, priority: str, category: str, context: str) -> dict:
    """Create a new reminder."""
    reminder = {
        "id": f"R{datetime.now().strftime('%H%M%S')}",
        "title": title,
        "type": "time-based",
        "priority": priority,
        "status": "pending",
        "trigger": when,
        "context": context or f"Created on {datetime.now().strftime('%Y-%m-%d')}",
        "category": category,
        "snooze_count": 0,
        "created_at": datetime.now().isoformat(),
    }
    return reminder


def filter_reminders(reminders: list, status: str = None, category: str = None, due_today: bool = False) -> list:
    """Filter reminders by criteria."""
    filtered = reminders

    if status:
        filtered = [r for r in filtered if r["status"] == status]

    if category:
        filtered = [r for r in filtered if r["category"] == category]

    if due_today:
        today = datetime.now().strftime("%Y-%m-%d")
        filtered = [r for r in filtered if today in r.get("trigger", "") or r["status"] in ("due", "overdue")]

    return filtered


def get_statistics(reminders: list) -> dict:
    """Compute reminder statistics."""
    status_counts = {}
    category_counts = {}
    priority_counts = {}

    for r in reminders:
        status_counts[r["status"]] = status_counts.get(r["status"], 0) + 1
        category_counts[r["category"]] = category_counts.get(r["category"], 0) + 1
        priority_counts[r["priority"]] = priority_counts.get(r["priority"], 0) + 1

    overdue = [r for r in reminders if r["status"] == "overdue"]
    high_snooze = [r for r in reminders if r["snooze_count"] >= 3]

    return {
        "total": len(reminders),
        "by_status": status_counts,
        "by_category": category_counts,
        "by_priority": priority_counts,
        "overdue_count": len(overdue),
        "high_snooze_count": len(high_snooze),
        "health_score": "good" if len(overdue) < 3 and len(high_snooze) == 0 else "needs attention",
    }


def main():
    parser = argparse.ArgumentParser(description="Create and manage reminders.")
    parser.add_argument("--create", action="store_true", help="Create a new reminder")
    parser.add_argument("--title", help="Reminder title (for --create)")
    parser.add_argument("--when", help="When to trigger (for --create, ISO datetime or relative)")
    parser.add_argument("--priority", choices=["urgent", "high", "normal", "low"], default="normal", help="Priority level")
    parser.add_argument("--category", choices=["work", "personal", "health", "finance", "social"], default="work", help="Category")
    parser.add_argument("--context", help="Additional context for the reminder")
    parser.add_argument("--list", action="store_true", help="List reminders")
    parser.add_argument("--status", choices=["pending", "due", "overdue", "snoozed", "complete"], help="Filter by status")
    parser.add_argument("--due-today", action="store_true", help="Show reminders due today")
    parser.add_argument("--stats", action="store_true", help="Show reminder statistics")
    parser.add_argument("--example", action="store_true", help="Run with example data")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format")

    args = parser.parse_args()

    if args.create and args.title and args.when:
        reminder = create_reminder(args.title, args.when, args.priority, args.category, args.context)
        if args.format == "json":
            print(json.dumps({"created": reminder}, indent=2))
        else:
            print(f"Reminder created:")
            print(f"  ID: {reminder['id']}")
            print(f"  Title: {reminder['title']}")
            print(f"  When: {reminder['trigger']}")
            print(f"  Priority: {reminder['priority']}")
            print(f"  Category: {reminder['category']}")
        return

    reminders = SAMPLE_REMINDERS

    if args.stats:
        stats = get_statistics(reminders)
        if args.format == "json":
            print(json.dumps(stats, indent=2))
        else:
            print("Reminder Statistics")
            print("=" * 40)
            print(f"  Total: {stats['total']}")
            print(f"  Health: {stats['health_score']}")
            print(f"  Overdue: {stats['overdue_count']}")
            print(f"\n  By Status:")
            for k, v in stats["by_status"].items():
                print(f"    {k}: {v}")
            print(f"\n  By Category:")
            for k, v in stats["by_category"].items():
                print(f"    {k}: {v}")
        return

    filtered = filter_reminders(reminders, status=args.status, due_today=args.due_today)

    if args.format == "json":
        output = {
            "generated_at": datetime.now().isoformat(),
            "filter": {"status": args.status, "due_today": args.due_today},
            "count": len(filtered),
            "reminders": filtered,
        }
        print(json.dumps(output, indent=2))
    else:
        title = "Reminders"
        if args.due_today:
            title = "Reminders Due Today"
        elif args.status:
            title = f"Reminders ({args.status})"
        print(f"{title}")
        print("=" * 50)
        for r in filtered:
            priority_marker = {"urgent": "!!!", "high": "!!", "normal": "!", "low": "."}
            marker = priority_marker.get(r["priority"], "!")
            snooze = f" (snoozed {r['snooze_count']}x)" if r["snooze_count"] > 0 else ""
            print(f"\n  [{r['status'].upper()}] {marker} {r['title']}{snooze}")
            print(f"    When: {r['trigger']}")
            print(f"    Category: {r['category']} | Priority: {r['priority']}")
            if r.get("context"):
                print(f"    Context: {r['context']}")
        print(f"\n{'=' * 50}")
        print(f"Total: {len(filtered)} reminder(s)")


if __name__ == "__main__":
    main()
