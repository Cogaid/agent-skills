#!/usr/bin/env python3
"""Track follow-up sequences and escalation chains.

Usage:
    python followup_tracker.py --list --status active
    python followup_tracker.py --create --to "John Smith" --topic "Proposal review" --sent-date 2025-01-15
    python followup_tracker.py --due --format json
    python followup_tracker.py --example
"""

import argparse
import json
import sys
from datetime import datetime, timedelta

SAMPLE_FOLLOWUPS = [
    {
        "id": "FU001",
        "to": "John Smith (Acme Corp)",
        "topic": "Q2 Proposal Review",
        "original_date": "2025-01-10",
        "channel": "email",
        "status": "active",
        "follow_ups": [
            {"date": "2025-01-13", "type": "gentle", "response": None},
        ],
        "next_action": {"type": "direct", "due": "2025-01-17"},
        "max_attempts": 3,
        "escalation": "CC account manager after 3rd attempt",
    },
    {
        "id": "FU002",
        "to": "Sarah Lee (Internal - Design)",
        "topic": "Design token export",
        "original_date": "2025-01-12",
        "channel": "slack",
        "status": "active",
        "follow_ups": [],
        "next_action": {"type": "gentle", "due": "2025-01-15"},
        "max_attempts": 2,
        "escalation": "Mention in standup",
    },
    {
        "id": "FU003",
        "to": "Mike Chen (Manager)",
        "topic": "Budget approval for new tool",
        "original_date": "2025-01-08",
        "channel": "email",
        "status": "active",
        "follow_ups": [
            {"date": "2025-01-11", "type": "gentle", "response": "Will review this week"},
            {"date": "2025-01-15", "type": "direct", "response": None},
        ],
        "next_action": {"type": "final", "due": "2025-01-20"},
        "max_attempts": 3,
        "escalation": "Bring up in 1:1",
    },
    {
        "id": "FU004",
        "to": "HR Department",
        "topic": "Benefits enrollment confirmation",
        "original_date": "2025-01-05",
        "channel": "email",
        "status": "resolved",
        "follow_ups": [
            {"date": "2025-01-08", "type": "gentle", "response": None},
            {"date": "2025-01-12", "type": "direct", "response": "Confirmed, you're enrolled"},
        ],
        "next_action": None,
        "max_attempts": 3,
        "escalation": None,
    },
    {
        "id": "FU005",
        "to": "Vendor Support (SaaS Tool)",
        "topic": "License key not working",
        "original_date": "2025-01-14",
        "channel": "support ticket",
        "status": "overdue",
        "follow_ups": [
            {"date": "2025-01-17", "type": "gentle", "response": None},
            {"date": "2025-01-22", "type": "direct", "response": None},
            {"date": "2025-01-28", "type": "final", "response": None},
        ],
        "next_action": {"type": "escalate", "due": "2025-01-30"},
        "max_attempts": 4,
        "escalation": "Request manager escalation via alternate email",
    },
]

FOLLOWUP_TEMPLATES = {
    "gentle": {
        "subject": "Following up - {topic}",
        "body": "Hi {name},\n\nJust following up on {topic} from {date}. Let me know if you have any questions.\n\nBest,\n{your_name}",
    },
    "direct": {
        "subject": "Re: {topic} - checking in",
        "body": "Hi {name},\n\nWanted to check in again on {topic}. This is important for {reason}.\n\nCould you let me know the status by {deadline}?\n\nThanks,\n{your_name}",
    },
    "final": {
        "subject": "Should I close this out? - {topic}",
        "body": "Hi {name},\n\nI've followed up a few times on {topic} but haven't heard back. I'll close this out by {deadline} unless I hear otherwise.\n\nBest,\n{your_name}",
    },
    "escalate": {
        "subject": "{topic} - escalation",
        "body": "Hi {escalation_contact},\n\nI've been trying to reach {name} about {topic} since {date} without success. Could you help connect us or provide an update?\n\nThanks,\n{your_name}",
    },
}


def calculate_days_waiting(original_date: str) -> int:
    orig = datetime.strptime(original_date, "%Y-%m-%d")
    return (datetime.now() - orig).days


def get_due_followups(followups: list) -> list:
    """Get follow-ups that need action today or are overdue."""
    today = datetime.now().strftime("%Y-%m-%d")
    due = []
    for fu in followups:
        if fu["status"] != "active":
            continue
        if fu.get("next_action") and fu["next_action"].get("due", "") <= today:
            fu["days_waiting"] = calculate_days_waiting(fu["original_date"])
            fu["attempts_made"] = len(fu["follow_ups"])
            due.append(fu)
    return due


def main():
    parser = argparse.ArgumentParser(description="Track follow-up sequences and escalation.")
    parser.add_argument("--list", action="store_true", help="List all follow-ups")
    parser.add_argument("--status", choices=["active", "resolved", "overdue", "all"], default="all", help="Filter by status")
    parser.add_argument("--due", action="store_true", help="Show follow-ups due today or overdue")
    parser.add_argument("--create", action="store_true", help="Create new follow-up tracker")
    parser.add_argument("--to", help="Person/entity to follow up with")
    parser.add_argument("--topic", help="Topic of follow-up")
    parser.add_argument("--sent-date", help="Date original message was sent (YYYY-MM-DD)")
    parser.add_argument("--example", action="store_true", help="Run with example data")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format")

    args = parser.parse_args()

    if args.create and args.to and args.topic:
        sent = args.sent_date or datetime.now().strftime("%Y-%m-%d")
        first_followup = (datetime.strptime(sent, "%Y-%m-%d") + timedelta(days=3)).strftime("%Y-%m-%d")
        new_fu = {
            "id": f"FU{datetime.now().strftime('%H%M%S')}",
            "to": args.to,
            "topic": args.topic,
            "original_date": sent,
            "channel": "email",
            "status": "active",
            "follow_ups": [],
            "next_action": {"type": "gentle", "due": first_followup},
            "max_attempts": 3,
        }
        if args.format == "json":
            print(json.dumps({"created": new_fu}, indent=2))
        else:
            print(f"Follow-up tracker created:")
            print(f"  To: {new_fu['to']}")
            print(f"  Topic: {new_fu['topic']}")
            print(f"  Original date: {new_fu['original_date']}")
            print(f"  First follow-up due: {first_followup}")
        return

    followups = SAMPLE_FOLLOWUPS

    if args.due:
        due_items = get_due_followups(followups)
        if args.format == "json":
            print(json.dumps({"due_followups": due_items, "count": len(due_items)}, indent=2))
        else:
            print("Follow-ups Due Today")
            print("=" * 50)
            if not due_items:
                print("  No follow-ups due today.")
            for fu in due_items:
                print(f"\n  [{fu['next_action']['type'].upper()}] {fu['to']}")
                print(f"    Topic: {fu['topic']}")
                print(f"    Waiting: {fu.get('days_waiting', '?')} days")
                print(f"    Attempts: {fu.get('attempts_made', 0)}/{fu['max_attempts']}")
                if fu.get("escalation"):
                    print(f"    Escalation: {fu['escalation']}")
        return

    # List all
    if args.status != "all":
        followups = [f for f in followups if f["status"] == args.status]

    if args.format == "json":
        output = {
            "generated_at": datetime.now().isoformat(),
            "filter": args.status,
            "count": len(followups),
            "followups": followups,
        }
        print(json.dumps(output, indent=2))
    else:
        print(f"Follow-up Tracker ({args.status})")
        print("=" * 50)
        for fu in followups:
            days = calculate_days_waiting(fu["original_date"])
            attempts = len(fu["follow_ups"])
            status_icon = {"active": "->", "resolved": "OK", "overdue": "!!"}
            icon = status_icon.get(fu["status"], "?")
            print(f"\n  [{icon}] {fu['to']}")
            print(f"    Topic: {fu['topic']}")
            print(f"    Status: {fu['status']} | Waiting: {days} days | Attempts: {attempts}/{fu['max_attempts']}")
            if fu.get("next_action"):
                print(f"    Next: {fu['next_action']['type']} follow-up due {fu['next_action']['due']}")
            if fu["follow_ups"]:
                last = fu["follow_ups"][-1]
                response = last.get("response") or "No response"
                print(f"    Last contact: {last['date']} ({last['type']}) - {response}")
        print(f"\n{'=' * 50}")
        print(f"Total: {len(followups)} | Active: {len([f for f in followups if f['status'] == 'active'])}")


if __name__ == "__main__":
    main()
