#!/usr/bin/env python3
"""
Log escalation details for tracking and analysis.

Usage:
    python log_escalation.py --ticket 12345 --level 2 --resolution "credit applied"
    python log_escalation.py --interactive

Output: JSON escalation record with timestamp
"""

import argparse
import json
import sys
from datetime import datetime


def create_escalation_log(
    ticket_id: str,
    level: int,
    resolution: str = "",
    customer: str = "",
    tier: str = "",
    root_cause: str = "",
    compensation: str = "",
    follow_up_required: bool = False,
    sentiment_at_close: str = "neutral"
) -> dict:
    """Create an escalation log entry."""

    level_names = {
        1: "frustrated",
        2: "angry",
        3: "critical"
    }

    log_entry = {
        "escalation_id": f"ESC-{datetime.now().strftime('%Y%m%d%H%M%S')}-{ticket_id}",
        "ticket_id": ticket_id,
        "timestamp": datetime.now().isoformat(),
        "escalation_level": level,
        "level_name": level_names.get(level, "unknown"),
        "customer": customer,
        "tier": tier,
        "root_cause": root_cause,
        "resolution": resolution,
        "compensation_provided": compensation,
        "follow_up_required": follow_up_required,
        "sentiment_at_close": sentiment_at_close,
        "status": "resolved" if resolution else "open"
    }

    return log_entry


def interactive_log():
    """Interactive mode for creating escalation log."""

    print("=== Escalation Log Entry ===\n")

    ticket_id = input("Ticket ID: ").strip()
    level = int(input("Escalation Level (1-3): ").strip())
    customer = input("Customer Name/Account: ").strip()
    tier = input("Customer Tier (free/pro/enterprise): ").strip()
    root_cause = input("Root Cause: ").strip()
    resolution = input("Resolution Provided: ").strip()
    compensation = input("Compensation (if any): ").strip()
    follow_up = input("Follow-up Required? (y/n): ").strip().lower() == 'y'
    sentiment = input("Sentiment at Close (satisfied/neutral/unsatisfied): ").strip()

    log_entry = create_escalation_log(
        ticket_id=ticket_id,
        level=level,
        resolution=resolution,
        customer=customer,
        tier=tier,
        root_cause=root_cause,
        compensation=compensation,
        follow_up_required=follow_up,
        sentiment_at_close=sentiment
    )

    return log_entry


def main():
    parser = argparse.ArgumentParser(description="Log escalation details")
    parser.add_argument("--ticket", "-t", help="Ticket ID")
    parser.add_argument("--level", "-l", type=int, choices=[1, 2, 3],
                        help="Escalation level (1-3)")
    parser.add_argument("--resolution", "-r", default="",
                        help="Resolution description")
    parser.add_argument("--customer", "-c", default="",
                        help="Customer name/account")
    parser.add_argument("--tier", choices=["free", "pro", "enterprise"],
                        default="", help="Customer tier")
    parser.add_argument("--root-cause", default="",
                        help="Root cause of escalation")
    parser.add_argument("--compensation", default="",
                        help="Compensation provided")
    parser.add_argument("--follow-up", action="store_true",
                        help="Follow-up required")
    parser.add_argument("--sentiment", choices=["satisfied", "neutral", "unsatisfied"],
                        default="neutral", help="Customer sentiment at close")
    parser.add_argument("--interactive", "-i", action="store_true",
                        help="Interactive mode")
    parser.add_argument("--pretty", "-p", action="store_true",
                        help="Pretty print output")
    parser.add_argument("--output", "-o", help="Output file (append)")

    args = parser.parse_args()

    if args.interactive:
        log_entry = interactive_log()
    elif args.ticket and args.level:
        log_entry = create_escalation_log(
            ticket_id=args.ticket,
            level=args.level,
            resolution=args.resolution,
            customer=args.customer,
            tier=args.tier,
            root_cause=args.root_cause,
            compensation=args.compensation,
            follow_up_required=args.follow_up,
            sentiment_at_close=args.sentiment
        )
    else:
        parser.print_help()
        sys.exit(1)

    # Format output
    if args.pretty:
        output = json.dumps(log_entry, indent=2)
    else:
        output = json.dumps(log_entry)

    # Write to file or stdout
    if args.output:
        with open(args.output, 'a') as f:
            f.write(output + "\n")
        print(f"Logged escalation {log_entry['escalation_id']} to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
