#!/usr/bin/env python3
"""Blocker tracker for standup workflows.

Tracks blockers across standups, calculates aging, identifies
escalation needs, and reports on resolution metrics.

Usage:
    python blocker_tracker.py --demo
    python blocker_tracker.py --demo --json
    python blocker_tracker.py --add "Waiting for API credentials" --owner alice --severity P1
    python blocker_tracker.py --resolve 1
    python blocker_tracker.py --report
"""

import argparse
import json
import sys
from datetime import date, timedelta


# Sample blocker data for demo mode
SAMPLE_BLOCKERS = [
    {
        "id": 1,
        "description": "Waiting for staging DB credentials from DevOps",
        "blocked_person": "Bob",
        "owner": "DevOps",
        "severity": "P1",
        "raised_date": (date.today() - timedelta(days=2)).isoformat(),
        "resolved_date": None,
        "status": "open",
    },
    {
        "id": 2,
        "description": "Design spec unclear for settings page",
        "blocked_person": "Carol",
        "owner": "Designer",
        "severity": "P2",
        "raised_date": (date.today() - timedelta(days=1)).isoformat(),
        "resolved_date": None,
        "status": "open",
    },
    {
        "id": 3,
        "description": "API rate limit hit during load testing",
        "blocked_person": "Dave",
        "owner": "Dave",
        "severity": "P2",
        "raised_date": (date.today() - timedelta(days=3)).isoformat(),
        "resolved_date": (date.today() - timedelta(days=1)).isoformat(),
        "status": "resolved",
    },
    {
        "id": 4,
        "description": "CI/CD pipeline failing on integration tests",
        "blocked_person": "Alice",
        "owner": "Alice",
        "severity": "P1",
        "raised_date": (date.today() - timedelta(days=4)).isoformat(),
        "resolved_date": (date.today() - timedelta(days=3)).isoformat(),
        "status": "resolved",
    },
    {
        "id": 5,
        "description": "Third-party payment sandbox is down",
        "blocked_person": "Eve",
        "owner": "Vendor",
        "severity": "P0",
        "raised_date": date.today().isoformat(),
        "status": "open",
        "resolved_date": None,
    },
]


def calculate_age(raised_date_str, resolved_date_str=None):
    """Calculate blocker age in days."""
    raised = date.fromisoformat(raised_date_str)
    end = date.fromisoformat(resolved_date_str) if resolved_date_str else date.today()
    return (end - raised).days


def assess_escalation(blocker):
    """Determine if a blocker needs escalation."""
    if blocker["status"] == "resolved":
        return {"needs_escalation": False, "reason": "Already resolved"}

    age = calculate_age(blocker["raised_date"])
    severity = blocker["severity"]

    # Escalation rules
    if severity == "P0":
        return {
            "needs_escalation": True,
            "urgency": "IMMEDIATE",
            "target": "Engineering Manager + dependent team leads",
            "reason": f"P0 blocker: {blocker['description'][:50]}",
        }
    elif severity == "P1" and age >= 1:
        return {
            "needs_escalation": True,
            "urgency": "SAME DAY",
            "target": "Scrum Master + Product Owner",
            "reason": f"P1 blocker aged {age} day(s)",
        }
    elif severity == "P2" and age >= 2:
        return {
            "needs_escalation": True,
            "urgency": "WITHIN 48H",
            "target": "Scrum Master",
            "reason": f"P2 blocker aged {age} day(s)",
        }
    elif age >= 3:
        return {
            "needs_escalation": True,
            "urgency": "REVIEW",
            "target": "Scrum Master",
            "reason": f"Blocker aged {age} day(s) regardless of severity",
        }

    return {"needs_escalation": False, "reason": "Within SLA"}


def generate_report(blockers):
    """Generate a blocker status report."""
    open_blockers = [b for b in blockers if b["status"] == "open"]
    resolved_blockers = [b for b in blockers if b["status"] == "resolved"]

    # Calculate metrics
    resolution_times = []
    for b in resolved_blockers:
        if b.get("resolved_date"):
            resolution_times.append(calculate_age(b["raised_date"], b["resolved_date"]))

    avg_resolution = (
        round(sum(resolution_times) / len(resolution_times), 1)
        if resolution_times
        else 0
    )

    # Severity breakdown
    severity_counts = {}
    for b in open_blockers:
        sev = b["severity"]
        severity_counts[sev] = severity_counts.get(sev, 0) + 1

    # Escalation needs
    escalations = []
    for b in open_blockers:
        esc = assess_escalation(b)
        if esc["needs_escalation"]:
            escalations.append({**esc, "blocker_id": b["id"], "description": b["description"]})

    report = {
        "date": date.today().isoformat(),
        "total_blockers": len(blockers),
        "open": len(open_blockers),
        "resolved": len(resolved_blockers),
        "avg_resolution_days": avg_resolution,
        "severity_breakdown": severity_counts,
        "escalations_needed": escalations,
        "open_blockers": [
            {
                **b,
                "age_days": calculate_age(b["raised_date"]),
                "escalation": assess_escalation(b),
            }
            for b in open_blockers
        ],
    }
    return report


def format_report_text(report):
    """Format report as readable text."""
    lines = []
    lines.append("=" * 60)
    lines.append(f"BLOCKER STATUS REPORT - {report['date']}")
    lines.append("=" * 60)
    lines.append("")
    lines.append(f"Total: {report['total_blockers']} | Open: {report['open']} | "
                 f"Resolved: {report['resolved']}")
    lines.append(f"Avg resolution time: {report['avg_resolution_days']} days")
    lines.append("")

    if report["severity_breakdown"]:
        lines.append("SEVERITY BREAKDOWN (Open)")
        lines.append("-" * 30)
        for sev, count in sorted(report["severity_breakdown"].items()):
            lines.append(f"  {sev}: {count}")
        lines.append("")

    lines.append("OPEN BLOCKERS")
    lines.append("-" * 60)
    for b in report["open_blockers"]:
        lines.append(f"  #{b['id']} [{b['severity']}] {b['description']}")
        lines.append(f"     Blocked: {b['blocked_person']} | Owner: {b['owner']} | "
                     f"Age: {b['age_days']}d")
        esc = b["escalation"]
        if esc["needs_escalation"]:
            lines.append(f"     ESCALATION: {esc['urgency']} -> {esc['target']}")
        lines.append("")

    if report["escalations_needed"]:
        lines.append("ESCALATION ACTIONS NEEDED")
        lines.append("-" * 60)
        for e in report["escalations_needed"]:
            lines.append(f"  #{e['blocker_id']}: {e['urgency']} -> {e['target']}")
            lines.append(f"    Reason: {e['reason']}")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Track and report on standup blockers",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run demo report
  %(prog)s --demo

  # JSON output
  %(prog)s --demo --json

  # Generate report from demo data
  %(prog)s --demo --report
        """,
    )
    parser.add_argument("--demo", action="store_true", help="Use sample blocker data")
    parser.add_argument("--report", action="store_true", help="Generate full report")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if not args.demo:
        print("Use --demo flag to run with sample data.")
        print("Run with --help for usage information.")
        sys.exit(0)

    blockers = SAMPLE_BLOCKERS
    report = generate_report(blockers)

    if args.json:
        print(json.dumps(report, indent=2, default=str))
    else:
        print(format_report_text(report))


if __name__ == "__main__":
    main()
