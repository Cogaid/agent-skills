#!/usr/bin/env python3
"""Score emails by priority using weighted criteria.

Usage:
    python priority_score.py --account user@example.com --unread-only
    python priority_score.py --account user@example.com --format json --top 5
"""

import argparse
import json
import sys
from datetime import datetime

SAMPLE_EMAILS = [
    {
        "id": "E001",
        "from": "ceo@company.com",
        "subject": "Q2 Strategy - Need Input by EOD",
        "sender_importance": 5,
        "time_sensitivity": 5,
        "impact": 5,
        "effort_required": 4,
        "thread_activity": 1,
        "unread": True,
    },
    {
        "id": "E002",
        "from": "client@acme.com",
        "subject": "Re: Proposal Questions - deal closing Friday",
        "sender_importance": 5,
        "time_sensitivity": 3,
        "impact": 5,
        "effort_required": 3,
        "thread_activity": 4,
        "unread": True,
    },
    {
        "id": "E003",
        "from": "colleague@company.com",
        "subject": "Sprint retro notes",
        "sender_importance": 3,
        "time_sensitivity": 1,
        "impact": 2,
        "effort_required": 5,
        "thread_activity": 2,
        "unread": True,
    },
    {
        "id": "E004",
        "from": "manager@company.com",
        "subject": "1:1 prep - performance review discussion",
        "sender_importance": 4,
        "time_sensitivity": 4,
        "impact": 4,
        "effort_required": 2,
        "thread_activity": 1,
        "unread": True,
    },
    {
        "id": "E005",
        "from": "newsletter@techcrunch.com",
        "subject": "This Week in AI",
        "sender_importance": 1,
        "time_sensitivity": 1,
        "impact": 1,
        "effort_required": 5,
        "thread_activity": 1,
        "unread": True,
    },
    {
        "id": "E006",
        "from": "vendor@saasproduct.com",
        "subject": "Your license expires in 3 days",
        "sender_importance": 2,
        "time_sensitivity": 4,
        "impact": 3,
        "effort_required": 4,
        "thread_activity": 1,
        "unread": False,
    },
]

WEIGHTS = {
    "sender_importance": 0.30,
    "time_sensitivity": 0.25,
    "impact": 0.25,
    "effort_required": 0.10,
    "thread_activity": 0.10,
}

PRIORITY_LEVELS = [
    (4.0, "Critical", "Handle immediately"),
    (3.0, "High", "Handle within 2 hours"),
    (2.0, "Medium", "Handle within 24 hours"),
    (1.0, "Low", "Batch process end of day"),
]


def calculate_priority(email: dict) -> dict:
    """Calculate weighted priority score for an email."""
    score = sum(email[factor] * weight for factor, weight in WEIGHTS.items())
    score = round(score, 2)

    priority_level = "Low"
    recommended_action = "Batch process end of day"
    for threshold, level, action in PRIORITY_LEVELS:
        if score >= threshold:
            priority_level = level
            recommended_action = action
            break

    return {
        "email_id": email["id"],
        "from": email["from"],
        "subject": email["subject"],
        "score": score,
        "priority_level": priority_level,
        "recommended_action": recommended_action,
        "factor_scores": {
            "sender_importance": email["sender_importance"],
            "time_sensitivity": email["time_sensitivity"],
            "impact": email["impact"],
            "effort_required": email["effort_required"],
            "thread_activity": email["thread_activity"],
        },
    }


def main():
    parser = argparse.ArgumentParser(description="Score emails by priority using weighted criteria.")
    parser.add_argument("--account", required=True, help="Email account to analyze")
    parser.add_argument("--unread-only", action="store_true", help="Only score unread emails")
    parser.add_argument("--top", type=int, default=None, help="Show only top N results")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format")

    args = parser.parse_args()

    emails = SAMPLE_EMAILS
    if args.unread_only:
        emails = [e for e in emails if e.get("unread", True)]

    scored = [calculate_priority(e) for e in emails]
    scored.sort(key=lambda x: x["score"], reverse=True)

    if args.top:
        scored = scored[: args.top]

    if args.format == "json":
        output = {
            "account": args.account,
            "scored_at": datetime.now().isoformat(),
            "unread_only": args.unread_only,
            "total_scored": len(scored),
            "weights": WEIGHTS,
            "results": scored,
        }
        print(json.dumps(output, indent=2))
    else:
        print(f"Email Priority Scores")
        print(f"Account: {args.account}")
        filter_note = " (unread only)" if args.unread_only else ""
        print(f"Emails scored: {len(scored)}{filter_note}")
        print("=" * 60)
        for i, r in enumerate(scored, 1):
            print(f"\n  #{i} [{r['priority_level']}] Score: {r['score']}")
            print(f"    From: {r['from']}")
            print(f"    Subject: {r['subject']}")
            print(f"    Action: {r['recommended_action']}")
        print("\n" + "=" * 60)
        print(f"\nWeights: {', '.join(f'{k}: {int(v*100)}%' for k, v in WEIGHTS.items())}")


if __name__ == "__main__":
    main()
