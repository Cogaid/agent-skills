#!/usr/bin/env python3
"""Extract action items from meeting notes using pattern matching.

Usage:
    python action_extractor.py --notes "Meeting notes text here"
    python action_extractor.py --file notes.txt --format json
    python action_extractor.py --example
"""

import argparse
import json
import re
import sys
from datetime import datetime

SAMPLE_NOTES = """
Sprint Planning Meeting - Jan 15, 2025

Sarah mentioned that Mike should investigate the auth refactor by end of day tomorrow.
Tom agreed to file the infra ticket for staging environment today.
Lisa will sync with design ops on the token export by Friday.

We decided that the search feature needs to be done by Jan 20.
Mike and Amy will pair on regression tests Thursday.

Action: Tom to implement search API (3 day estimate, due Monday)
TODO: Lisa - update search mockups with larger input field
Follow-up: Sarah to send sprint 4 goals to stakeholders by EOD

Amy raised that she needs access to the test environment - Mike to set that up.

Next steps:
- Mike: complete spike investigation
- Tom: staging fix + search API
- Lisa: mockup revisions + design ops sync
"""

# Patterns that indicate action items
ACTION_PATTERNS = [
    r"(?P<owner>[A-Z][a-z]+)\s+(?:should|will|needs to|to|agreed to|is going to)\s+(?P<action>[^.!?\n]+)",
    r"(?:Action|TODO|Follow-up):\s*(?P<owner>[A-Z][a-z]+)\s*[-:to]*\s*(?P<action>[^.!?\n]+)",
    r"(?P<owner>[A-Z][a-z]+)\s+to\s+(?P<action>[^.!?\n]+)",
    r"-\s*(?P<owner>[A-Z][a-z]+):\s*(?P<action>[^.!?\n]+)",
]

# Patterns for due dates
DUE_PATTERNS = [
    (r"by\s+(end of day|EOD|today|tomorrow|Friday|Monday|Tuesday|Wednesday|Thursday)", "relative"),
    (r"due\s+(\w+day|\w+\s+\d+)", "relative"),
    (r"by\s+(Jan(?:uary)?\s+\d+|Feb(?:ruary)?\s+\d+|Mar(?:ch)?\s+\d+)", "absolute"),
    (r"(\d{4}-\d{2}-\d{2})", "iso"),
]


def extract_actions(text: str) -> list:
    """Extract action items from text using pattern matching."""
    actions = []
    seen = set()

    for pattern in ACTION_PATTERNS:
        matches = re.finditer(pattern, text, re.MULTILINE)
        for match in matches:
            owner = match.group("owner")
            action = match.group("action").strip().rstrip(".,;")

            # Skip very short or very long matches (likely false positives)
            if len(action) < 10 or len(action) > 150:
                continue

            # Deduplicate
            key = f"{owner}:{action[:30]}"
            if key in seen:
                continue
            seen.add(key)

            # Try to find due date in the action text or surrounding context
            due_date = None
            for due_pattern, date_type in DUE_PATTERNS:
                due_match = re.search(due_pattern, action, re.IGNORECASE)
                if due_match:
                    due_date = due_match.group(1)
                    break

            # If not in action text, check the full sentence
            if not due_date:
                sentence_start = max(0, match.start() - 50)
                sentence_end = min(len(text), match.end() + 100)
                context = text[sentence_start:sentence_end]
                for due_pattern, date_type in DUE_PATTERNS:
                    due_match = re.search(due_pattern, context, re.IGNORECASE)
                    if due_match:
                        due_date = due_match.group(1)
                        break

            actions.append({
                "owner": owner,
                "action": action,
                "due_date": due_date,
                "has_due_date": due_date is not None,
                "confidence": "high" if any(kw in match.group(0).lower() for kw in ["action:", "todo:", "follow-up:"]) else "medium",
            })

    return actions


def main():
    parser = argparse.ArgumentParser(description="Extract action items from meeting notes.")
    parser.add_argument("--notes", help="Meeting notes text")
    parser.add_argument("--file", help="Path to notes file")
    parser.add_argument("--example", action="store_true", help="Run with example data")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format")

    args = parser.parse_args()

    if args.file:
        with open(args.file) as f:
            text = f.read()
    elif args.notes:
        text = args.notes
    else:
        text = SAMPLE_NOTES

    actions = extract_actions(text)

    if args.format == "json":
        output = {
            "extracted_at": datetime.now().isoformat(),
            "total_actions": len(actions),
            "with_due_dates": len([a for a in actions if a["has_due_date"]]),
            "without_due_dates": len([a for a in actions if not a["has_due_date"]]),
            "actions": actions,
        }
        print(json.dumps(output, indent=2))
    else:
        print("Action Items Extracted")
        print("=" * 60)
        print(f"  Total found: {len(actions)}")
        print(f"  With due dates: {len([a for a in actions if a['has_due_date']])}")
        print(f"  Without due dates: {len([a for a in actions if not a['has_due_date']])}")
        print()

        for i, a in enumerate(actions, 1):
            due = f" -- Due: {a['due_date']}" if a["due_date"] else " -- Due: [NOT SET]"
            conf = f" [{a['confidence']}]"
            print(f"  {i}. @{a['owner']}: {a['action']}{due}{conf}")

        # Flag issues
        no_date = [a for a in actions if not a["has_due_date"]]
        if no_date:
            print(f"\n  WARNING: {len(no_date)} action(s) missing due dates:")
            for a in no_date:
                print(f"    - @{a['owner']}: {a['action'][:50]}...")

        print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
