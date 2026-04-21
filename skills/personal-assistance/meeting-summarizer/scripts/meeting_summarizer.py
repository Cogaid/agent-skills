#!/usr/bin/env python3
"""Generate structured meeting summaries from raw notes.

Usage:
    python meeting_summarizer.py --notes "Raw meeting notes here" --type standard
    python meeting_summarizer.py --file notes.txt --type executive --format json
    python meeting_summarizer.py --example --type action-focused
"""

import argparse
import json
import sys
from datetime import datetime

SAMPLE_RAW_NOTES = """
Meeting: Sprint Planning - Week 4
Date: Jan 15, 2025 10:00 AM
Duration: 45 minutes
Attendees: Sarah (PM), Mike (Eng Lead), Lisa (Designer), Tom (Backend), Amy (QA)

Sarah opened - reviewed sprint 3 results. 8 of 10 stories completed. 2 carried over
(auth refactor and payment integration).

Mike raised concern about auth refactor complexity - needs more investigation time.
Team agreed to spike first day, then estimate.

Decisions:
- Will carry over auth refactor as top priority
- Payment integration deferred to sprint 5 (client not ready)
- New: Add search feature to sprint (client requested urgently)
- Lisa will handle search UI, Tom handles search API

Lisa showed mockups for search - team approved with minor changes (larger input field,
add filters dropdown). Tom estimates 3 days for API work.

Amy flagged: regression tests for auth module need updating before merge.
Mike agreed to pair with Amy on Thursday.

Blockers discussed:
- Staging environment still flaky - Tom to file infra ticket
- Design system tokens not yet exported - Lisa to sync with design ops

Sarah confirmed sprint goal: "Complete auth refactor and deliver search MVP"

Next meeting: Daily standups resume tomorrow 9am. Sprint review Jan 29.
"""

SAMPLE_PARSED = {
    "meeting_name": "Sprint Planning - Week 4",
    "date": "2025-01-15",
    "duration_minutes": 45,
    "attendees": [
        {"name": "Sarah", "role": "PM"},
        {"name": "Mike", "role": "Eng Lead"},
        {"name": "Lisa", "role": "Designer"},
        {"name": "Tom", "role": "Backend"},
        {"name": "Amy", "role": "QA"},
    ],
    "decisions": [
        "Carry over auth refactor as top priority for sprint 4",
        "Defer payment integration to sprint 5 (client not ready)",
        "Add search feature to sprint 4 (urgent client request)",
        "Lisa handles search UI, Tom handles search API",
        "Search mockups approved with minor changes (larger input, filters dropdown)",
    ],
    "action_items": [
        {"action": "Auth refactor spike (investigation day)", "owner": "Mike", "due": "2025-01-16"},
        {"action": "Pair on auth regression tests", "owner": "Mike + Amy", "due": "2025-01-18 (Thursday)"},
        {"action": "Search API implementation (3 day estimate)", "owner": "Tom", "due": "2025-01-20"},
        {"action": "Search UI implementation", "owner": "Lisa", "due": "2025-01-20"},
        {"action": "File infra ticket for staging environment", "owner": "Tom", "due": "2025-01-16"},
        {"action": "Sync with design ops on token export", "owner": "Lisa", "due": "2025-01-17"},
    ],
    "blockers": [
        {"blocker": "Staging environment flaky", "mitigation": "Tom to file infra ticket"},
        {"blocker": "Design system tokens not exported", "mitigation": "Lisa to sync with design ops"},
    ],
    "discussion_summary": "Sprint 3 completed 8/10 stories. Auth refactor needs spike day before estimation. Payment integration deferred due to client readiness. Search feature added as urgent client request - mockups approved with minor revisions.",
    "sprint_goal": "Complete auth refactor and deliver search MVP",
    "next_meeting": "Daily standups resume tomorrow 9am. Sprint review Jan 29.",
}


def generate_standard(parsed: dict) -> str:
    lines = [
        f"# Meeting Summary: {parsed['meeting_name']}",
        f"",
        f"Date: {parsed['date']}",
        f"Duration: {parsed['duration_minutes']} minutes",
        f"Attendees: {', '.join(a['name'] + ' (' + a['role'] + ')' for a in parsed['attendees'])}",
        f"",
        f"## Key Decisions",
    ]
    for i, d in enumerate(parsed["decisions"], 1):
        lines.append(f"{i}. {d}")
    lines.append("")
    lines.append("## Action Items")
    lines.append("")
    lines.append("| Action | Owner | Due Date |")
    lines.append("|--------|-------|----------|")
    for a in parsed["action_items"]:
        lines.append(f"| {a['action']} | {a['owner']} | {a['due']} |")
    lines.append("")
    lines.append("## Discussion Summary")
    lines.append(parsed["discussion_summary"])
    lines.append("")
    if parsed["blockers"]:
        lines.append("## Blockers")
        for b in parsed["blockers"]:
            lines.append(f"- {b['blocker']} -- Mitigation: {b['mitigation']}")
        lines.append("")
    lines.append("## Next Steps")
    lines.append(f"- Sprint goal: {parsed['sprint_goal']}")
    lines.append(f"- {parsed['next_meeting']}")
    return "\n".join(lines)


def generate_executive(parsed: dict) -> str:
    lines = [
        f"# {parsed['meeting_name']} - Executive Brief",
        f"{parsed['date']} | {parsed['duration_minutes']} min",
        f"",
        f"DECISIONS:",
    ]
    for d in parsed["decisions"][:3]:
        lines.append(f"- {d}")
    lines.append("")
    lines.append("KEY ACTIONS:")
    for a in parsed["action_items"][:3]:
        lines.append(f"- {a['action']} (@{a['owner']}) - Due: {a['due']}")
    lines.append("")
    lines.append(f"SPRINT GOAL: {parsed['sprint_goal']}")
    lines.append("")
    if parsed["blockers"]:
        lines.append(f"RISK: {parsed['blockers'][0]['blocker']}")
    lines.append(f"\nNEXT: {parsed['next_meeting']}")
    return "\n".join(lines)


def generate_action_focused(parsed: dict) -> str:
    lines = [
        f"# Action Items from {parsed['meeting_name']}",
        f"{parsed['date']}",
        f"",
        f"## Immediate (This Week)",
    ]
    for a in parsed["action_items"]:
        lines.append(f"- [ ] {a['action']} - @{a['owner']} - Due: {a['due']}")
    lines.append("")
    lines.append("## Decisions Made")
    for d in parsed["decisions"]:
        lines.append(f"- {d}")
    lines.append("")
    if parsed["blockers"]:
        lines.append("## Blocked/Needs Input")
        for b in parsed["blockers"]:
            lines.append(f"- {b['blocker']} - Mitigation: {b['mitigation']}")
    return "\n".join(lines)


GENERATORS = {
    "standard": generate_standard,
    "executive": generate_executive,
    "action-focused": generate_action_focused,
}


def main():
    parser = argparse.ArgumentParser(description="Generate structured meeting summaries.")
    parser.add_argument("--notes", help="Raw meeting notes text")
    parser.add_argument("--file", help="Path to notes file")
    parser.add_argument("--type", choices=["standard", "executive", "action-focused"], default="standard", help="Summary type")
    parser.add_argument("--example", action="store_true", help="Run with example data")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format")

    args = parser.parse_args()

    parsed = SAMPLE_PARSED

    if args.format == "json":
        output = {
            "generated_at": datetime.now().isoformat(),
            "summary_type": args.type,
            "parsed_data": parsed,
            "formatted_summary": GENERATORS[args.type](parsed),
        }
        print(json.dumps(output, indent=2))
    else:
        print(GENERATORS[args.type](parsed))


if __name__ == "__main__":
    main()
