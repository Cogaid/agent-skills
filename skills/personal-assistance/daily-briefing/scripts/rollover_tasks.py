#!/usr/bin/env python3
"""Process task rollovers automatically based on priority rules.

Usage:
    python rollover_tasks.py --user user123 --apply-rules
    python rollover_tasks.py --user user123 --dry-run --format json
"""

import argparse
import json
import sys
from datetime import datetime, timedelta

SAMPLE_INCOMPLETE_TASKS = [
    {"id": "T001", "title": "Submit quarterly report", "priority": "P0", "due": "2025-01-15", "rollover_count": 0},
    {"id": "T002", "title": "Update project roadmap", "priority": "P1", "due": "2025-01-14", "rollover_count": 1},
    {"id": "T003", "title": "Organize shared drive", "priority": "P2", "due": "2025-01-12", "rollover_count": 3},
    {"id": "T004", "title": "Read industry newsletter", "priority": "P3", "due": "2025-01-10", "rollover_count": 4},
    {"id": "T005", "title": "Update LinkedIn profile", "priority": "P4", "due": "2025-01-13", "rollover_count": 0},
    {"id": "T006", "title": "Review vendor contract", "priority": "P1", "due": "2025-01-13", "rollover_count": 2},
]

ROLLOVER_RULES = {
    "P0": {"action": "auto_roll", "escalate_after": 2, "max_rollovers": 5, "alert_at": 1},
    "P1": {"action": "auto_roll", "escalate_after": 2, "max_rollovers": 5, "alert_at": 2},
    "P2": {"action": "auto_roll", "escalate_after": 3, "max_rollovers": 5, "alert_at": 3},
    "P3": {"action": "no_auto_roll", "move_to_someday_after": 5},
    "P4": {"action": "drop", "drop_immediately": True},
}

PRIORITY_ESCALATION = {"P0": "P0", "P1": "P0", "P2": "P1", "P3": "P3", "P4": "P4"}


def process_rollover(task: dict, apply: bool) -> dict:
    """Process a single task through rollover rules."""
    priority = task["priority"]
    rules = ROLLOVER_RULES[priority]
    rollover_count = task["rollover_count"] + 1
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

    result = {
        "task_id": task["id"],
        "title": task["title"],
        "original_priority": priority,
        "original_due": task["due"],
        "rollover_count": rollover_count,
    }

    if rules["action"] == "drop":
        result["action"] = "DROP"
        result["new_priority"] = None
        result["new_due"] = None
        result["message"] = "P4 task dropped (informational only, no auto-roll)"

    elif rules["action"] == "no_auto_roll":
        if rollover_count >= rules.get("move_to_someday_after", 5):
            result["action"] = "MOVE_TO_SOMEDAY"
            result["new_priority"] = None
            result["new_due"] = None
            result["message"] = f"Moved to someday/maybe after {rollover_count} deferrals"
        else:
            result["action"] = "SKIP"
            result["new_priority"] = priority
            result["new_due"] = None
            result["message"] = f"Low priority, not auto-rolled ({rollover_count} deferrals)"

    elif rules["action"] == "auto_roll":
        escalate_after = rules.get("escalate_after", 2)
        max_rollovers = rules.get("max_rollovers", 5)

        if rollover_count >= max_rollovers:
            result["action"] = "STUCK_REVIEW"
            result["new_priority"] = "P0"
            result["new_due"] = tomorrow
            result["message"] = f"STUCK: Rolled {rollover_count} times. Mandatory review required."
            result["alert"] = True
        elif rollover_count >= escalate_after:
            new_priority = PRIORITY_ESCALATION[priority]
            result["action"] = "ROLL_AND_ESCALATE"
            result["new_priority"] = new_priority
            result["new_due"] = tomorrow
            result["message"] = f"Escalated from {priority} to {new_priority} after {rollover_count} rollovers"
            result["alert"] = True
        else:
            result["action"] = "ROLL"
            result["new_priority"] = priority
            result["new_due"] = tomorrow
            result["message"] = f"Rolled to tomorrow as {priority} (rollover #{rollover_count})"
            result["alert"] = rollover_count >= rules.get("alert_at", 999)

    result["applied"] = apply
    return result


def main():
    parser = argparse.ArgumentParser(description="Process task rollovers based on priority rules.")
    parser.add_argument("--user", required=True, help="User ID or name")
    parser.add_argument("--apply-rules", action="store_true", help="Apply rollover rules (default: dry run)")
    parser.add_argument("--dry-run", action="store_true", help="Preview rollover actions without applying")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format")

    args = parser.parse_args()
    apply = args.apply_rules and not args.dry_run

    results = []
    for task in SAMPLE_INCOMPLETE_TASKS:
        result = process_rollover(task, apply)
        results.append(result)

    if args.format == "json":
        output = {
            "user": args.user,
            "processed_at": datetime.now().isoformat(),
            "dry_run": not apply,
            "tasks_processed": len(results),
            "results": results,
            "summary": {
                "rolled": len([r for r in results if r["action"] == "ROLL"]),
                "escalated": len([r for r in results if r["action"] == "ROLL_AND_ESCALATE"]),
                "stuck": len([r for r in results if r["action"] == "STUCK_REVIEW"]),
                "dropped": len([r for r in results if r["action"] == "DROP"]),
                "skipped": len([r for r in results if r["action"] == "SKIP"]),
                "someday": len([r for r in results if r["action"] == "MOVE_TO_SOMEDAY"]),
            },
        }
        print(json.dumps(output, indent=2))
    else:
        mode = "DRY RUN" if not apply else "APPLIED"
        print(f"Task Rollover Processing [{mode}]")
        print(f"User: {args.user}")
        print(f"Date: {datetime.now().strftime('%Y-%m-%d')}")
        print("=" * 60)
        for r in results:
            alert_marker = " [ALERT]" if r.get("alert") else ""
            print(f"\n  [{r['action']}]{alert_marker} {r['title']}")
            print(f"    {r['original_priority']} -> {r.get('new_priority', 'N/A')} | Due: {r.get('new_due', 'N/A')}")
            print(f"    {r['message']}")
        print("\n" + "=" * 60)
        summary_actions = {}
        for r in results:
            summary_actions[r["action"]] = summary_actions.get(r["action"], 0) + 1
        print("Summary:", ", ".join(f"{k}: {v}" for k, v in summary_actions.items()))


if __name__ == "__main__":
    main()
