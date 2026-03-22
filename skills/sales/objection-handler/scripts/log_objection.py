#!/usr/bin/env python3
"""
Log sales objections and outcomes for pattern analysis.

Usage:
    python log_objection.py --interactive
    python log_objection.py --type price --outcome resolved --deal "Acme Corp"

Output: JSON record of objection
"""

import argparse
import json
import sys
from datetime import datetime


OBJECTION_TYPES = [
    "price",
    "timing",
    "authority",
    "need",
    "trust",
    "competition",
    "other"
]

OUTCOMES = [
    "resolved",      # Objection handled, deal advancing
    "deferred",      # Need to address later
    "escalated",     # Brought in help (manager, SE, etc.)
    "lost"           # Deal lost due to objection
]


def interactive_log():
    """Interactive mode for logging objections."""

    print("=== Objection Logger ===\n")

    # Basic info
    deal = input("Deal/Company name: ").strip()
    contact = input("Contact name: ").strip()
    stage = input("Deal stage: ").strip()

    # Objection details
    print(f"\nObjection types: {', '.join(OBJECTION_TYPES)}")
    obj_type = input("Objection type: ").strip().lower()
    if obj_type not in OBJECTION_TYPES:
        obj_type = "other"

    exact_words = input("Their exact words: ").strip()
    root_cause = input("Root cause (what you discovered): ").strip()

    # Response
    response_used = input("Response/approach you used: ").strip()

    print(f"\nOutcomes: {', '.join(OUTCOMES)}")
    outcome = input("Outcome: ").strip().lower()
    if outcome not in OUTCOMES:
        outcome = "deferred"

    # Learnings
    worked = input("What worked well: ").strip()
    improve = input("What to do differently: ").strip()
    next_step = input("Next step: ").strip()

    return {
        "timestamp": datetime.now().isoformat(),
        "deal": deal,
        "contact": contact,
        "stage": stage,
        "objection": {
            "type": obj_type,
            "exact_words": exact_words,
            "root_cause": root_cause
        },
        "response": response_used,
        "outcome": outcome,
        "learnings": {
            "worked": worked,
            "improve": improve
        },
        "next_step": next_step
    }


def quick_log(obj_type, outcome, deal, words=None):
    """Quick log without full interactive mode."""
    return {
        "timestamp": datetime.now().isoformat(),
        "deal": deal,
        "objection": {
            "type": obj_type,
            "exact_words": words or ""
        },
        "outcome": outcome
    }


def main():
    parser = argparse.ArgumentParser(description="Log sales objection")
    parser.add_argument("--interactive", "-i", action="store_true",
                        help="Interactive mode")
    parser.add_argument("--type", "-t", choices=OBJECTION_TYPES,
                        help="Objection type")
    parser.add_argument("--outcome", "-o", choices=OUTCOMES,
                        help="Outcome")
    parser.add_argument("--deal", "-d", help="Deal/company name")
    parser.add_argument("--words", "-w", help="Their exact words")
    parser.add_argument("--output", help="Append to JSON file")

    args = parser.parse_args()

    if args.interactive:
        record = interactive_log()
    elif args.type and args.outcome and args.deal:
        record = quick_log(args.type, args.outcome, args.deal, args.words)
    else:
        parser.print_help()
        sys.exit(1)

    # Output
    if args.output:
        # Append to existing file or create new
        try:
            with open(args.output, 'r') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(record)

        with open(args.output, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Saved to {args.output}")
    else:
        print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
