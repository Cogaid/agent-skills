#!/usr/bin/env python3
"""Async standup message collector and summarizer.

Parses standup messages in the Done/Doing/Blockers format, generates
a structured summary with blocker tracking and participation metrics.

Usage:
    python standup_collector.py --file standups.txt
    python standup_collector.py --demo
    python standup_collector.py --demo --json
"""

import argparse
import json
import sys
from datetime import date


def parse_standup(message, author="Unknown"):
    """Parse a standup message into structured sections."""
    sections = {"done": [], "doing": [], "blockers": [], "fyi": []}
    current = None

    for line in message.strip().split("\n"):
        lower = line.lower().strip()
        if lower.startswith("done") or lower.startswith("**done"):
            current = "done"
            continue
        elif lower.startswith("doing") or lower.startswith("**doing"):
            current = "doing"
            continue
        elif lower.startswith("blocker") or lower.startswith("**blocker"):
            current = "blockers"
            continue
        elif lower.startswith("fyi") or lower.startswith("**fyi"):
            current = "fyi"
            continue

        if current and line.strip().startswith("- "):
            item = line.strip()[2:].strip()
            if item:
                sections[current].append(item)

    return {"author": author, **sections}


def generate_summary(updates, team_size=None, sprint_info=None):
    """Generate a formatted summary from parsed standup updates."""
    today = date.today().isoformat()
    reporters = [u["author"] for u in updates]
    effective_team_size = team_size or len(updates)

    # Collect all blockers
    all_blockers = []
    for u in updates:
        for b in u.get("blockers", []):
            if b.lower() not in ("none", "n/a", "no blockers", ""):
                all_blockers.append({"person": u["author"], "blocker": b})

    # Collect highlights
    all_done = []
    for u in updates:
        for d in u.get("done", []):
            all_done.append({"person": u["author"], "item": d})

    all_doing = []
    for u in updates:
        for d in u.get("doing", []):
            all_doing.append({"person": u["author"], "item": d})

    all_fyi = []
    for u in updates:
        for f in u.get("fyi", []):
            all_fyi.append({"person": u["author"], "item": f})

    summary = {
        "date": today,
        "reporters": reporters,
        "reporting_count": len(reporters),
        "team_size": effective_team_size,
        "participation_rate": round(len(reporters) / effective_team_size * 100, 1),
        "completed_items": all_done,
        "in_progress_items": all_doing,
        "blockers": all_blockers,
        "blocker_count": len(all_blockers),
        "fyi_items": all_fyi,
    }

    if sprint_info:
        summary["sprint"] = sprint_info

    return summary


def format_summary_text(summary):
    """Format summary as readable text."""
    lines = []
    lines.append("=" * 60)
    lines.append(f"DAILY STANDUP SUMMARY - {summary['date']}")
    lines.append("=" * 60)
    lines.append("")
    lines.append(f"Reporting: {summary['reporting_count']}/{summary['team_size']} "
                 f"({summary['participation_rate']}%)")
    lines.append("")

    lines.append("PROGRESS HIGHLIGHTS")
    lines.append("-" * 40)
    for item in summary["completed_items"]:
        lines.append(f"  [{item['person']}] {item['item']}")
    if not summary["completed_items"]:
        lines.append("  (no completed items reported)")
    lines.append("")

    lines.append("IN PROGRESS TODAY")
    lines.append("-" * 40)
    for item in summary["in_progress_items"]:
        lines.append(f"  [{item['person']}] {item['item']}")
    if not summary["in_progress_items"]:
        lines.append("  (no in-progress items reported)")
    lines.append("")

    lines.append("BLOCKERS")
    lines.append("-" * 40)
    if summary["blockers"]:
        for i, b in enumerate(summary["blockers"], 1):
            lines.append(f"  {i}. [{b['person']}] {b['blocker']}")
    else:
        lines.append("  No blockers reported")
    lines.append("")

    if summary["fyi_items"]:
        lines.append("FYI")
        lines.append("-" * 40)
        for item in summary["fyi_items"]:
            lines.append(f"  [{item['person']}] {item['item']}")
        lines.append("")

    return "\n".join(lines)


DEMO_UPDATES = [
    {
        "author": "Alice",
        "message": """**Done:**
- Completed US-101: user authentication flow - ready for QA
- Reviewed PR #234 for Bob

**Doing:**
- Starting US-103: password reset flow
- Expected completion: tomorrow

**Blockers:**
- None

**FYI:**
- OOO Friday afternoon
""",
    },
    {
        "author": "Bob",
        "message": """**Done:**
- Merged PR #234 for payment integration
- Fixed BUG-89: incorrect tax calculation

**Doing:**
- US-105: invoice generation (50% complete)

**Blockers:**
- Waiting for staging DB credentials from DevOps (since Apr 18)

**FYI:**
- None
""",
    },
    {
        "author": "Carol",
        "message": """**Done:**
- Finished API endpoint for search feature
- Deployed search to staging environment

**Doing:**
- US-107: search results pagination
- Writing integration tests for search

**Blockers:**
- Design spec unclear for settings page - waiting on @designer

**FYI:**
- Will be late to standup tomorrow (dentist appointment)
""",
    },
]


def main():
    parser = argparse.ArgumentParser(
        description="Collect and summarize async standup updates",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run with demo data
  %(prog)s --demo

  # Parse a file of standup messages
  %(prog)s --file standups.txt --team-size 7

  # JSON output
  %(prog)s --demo --json
        """,
    )
    parser.add_argument("--file", type=str, help="File containing standup messages")
    parser.add_argument("--team-size", type=int, help="Total team size for participation rate")
    parser.add_argument("--sprint", type=str, help="Sprint identifier (e.g., 'Sprint 14, Day 5/10')")
    parser.add_argument("--demo", action="store_true", help="Run with sample data")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.demo:
        updates = []
        for entry in DEMO_UPDATES:
            parsed = parse_standup(entry["message"], author=entry["author"])
            updates.append(parsed)
        team_size = args.team_size or 5
    elif args.file:
        try:
            with open(args.file, "r") as f:
                content = f.read()
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found", file=sys.stderr)
            sys.exit(1)

        # Split by author headers (e.g., "## Alice" or "**Alice**")
        import re
        blocks = re.split(r'\n(?=##\s|\*\*\w)', content)
        updates = []
        for block in blocks:
            block = block.strip()
            if not block:
                continue
            # Try to extract author name
            author_match = re.match(r'(?:##\s*|\*\*)(\w+)', block)
            author = author_match.group(1) if author_match else "Unknown"
            parsed = parse_standup(block, author=author)
            updates.append(parsed)
        team_size = args.team_size or len(updates)
    else:
        print("No input provided. Use --demo for sample data or --file to parse a file.")
        print("Run with --help for usage information.")
        sys.exit(1)

    sprint_info = args.sprint if args.sprint else None
    summary = generate_summary(updates, team_size=team_size, sprint_info=sprint_info)

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_summary_text(summary))


if __name__ == "__main__":
    main()
