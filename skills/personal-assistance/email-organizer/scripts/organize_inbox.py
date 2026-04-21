#!/usr/bin/env python3
"""Scan and categorize inbox messages based on rules.

Usage:
    python organize_inbox.py --account user@example.com --rules rules.json
    python organize_inbox.py --account user@example.com --dry-run --format json
"""

import argparse
import json
import sys
from datetime import datetime

SAMPLE_EMAILS = [
    {
        "id": "E001",
        "from": "ceo@company.com",
        "to": "user@company.com",
        "subject": "Q2 Strategy - Need Your Input",
        "date": "2025-01-15 08:30",
        "thread_count": 1,
        "has_attachment": False,
        "has_unsubscribe": False,
    },
    {
        "id": "E002",
        "from": "client@acme.com",
        "to": "user@company.com",
        "subject": "Re: Proposal Review - Questions",
        "date": "2025-01-15 09:15",
        "thread_count": 4,
        "has_attachment": True,
        "has_unsubscribe": False,
    },
    {
        "id": "E003",
        "from": "noreply@calendar.google.com",
        "to": "user@company.com",
        "subject": "Invitation: Team Sync @ Wed 3pm",
        "date": "2025-01-15 10:00",
        "thread_count": 1,
        "has_attachment": False,
        "has_unsubscribe": False,
    },
    {
        "id": "E004",
        "from": "newsletter@techdigest.com",
        "to": "user@company.com",
        "subject": "Weekly Tech Roundup - AI Updates",
        "date": "2025-01-15 06:00",
        "thread_count": 1,
        "has_attachment": False,
        "has_unsubscribe": True,
    },
    {
        "id": "E005",
        "from": "colleague@company.com",
        "to": "user@company.com",
        "subject": "Re: Sprint Planning Notes",
        "date": "2025-01-15 11:30",
        "thread_count": 7,
        "has_attachment": False,
        "has_unsubscribe": False,
    },
    {
        "id": "E006",
        "from": "noreply@amazon.com",
        "to": "user@company.com",
        "subject": "Your order has shipped - Order #12345",
        "date": "2025-01-15 07:45",
        "thread_count": 1,
        "has_attachment": False,
        "has_unsubscribe": True,
    },
    {
        "id": "E007",
        "from": "auto-reply@vendor.com",
        "to": "user@company.com",
        "subject": "Out of Office: John Smith",
        "date": "2025-01-15 08:00",
        "thread_count": 1,
        "has_attachment": False,
        "has_unsubscribe": False,
    },
]

VIP_SENDERS = ["ceo@company.com", "cto@company.com"]
CLIENT_DOMAINS = ["acme.com", "globex.com", "initech.com"]


def categorize_email(email: dict) -> dict:
    """Apply triage rules to categorize an email."""
    sender = email["from"]
    subject = email["subject"].lower()
    domain = sender.split("@")[-1] if "@" in sender else ""

    result = {
        "email_id": email["id"],
        "from": email["from"],
        "subject": email["subject"],
    }

    # Rule 8: Out-of-office auto-replies
    if any(kw in subject for kw in ["out of office", "ooo", "auto-reply", "automatic reply"]):
        result["category"] = "Archive"
        result["label"] = None
        result["action"] = "Archive immediately"
        result["skip_inbox"] = True
        return result

    # Rule 1: Executive emails
    if sender in VIP_SENDERS:
        result["category"] = "Action Required"
        result["label"] = "@Action-Required"
        result["action"] = "Handle immediately - VIP sender"
        result["skip_inbox"] = False
        result["priority"] = "Critical"
        return result

    # Rule 2: Client emails
    if domain in CLIENT_DOMAINS:
        client_name = domain.split(".")[0].capitalize()
        result["category"] = "Action Required"
        result["label"] = f"Clients/{client_name}, @Action-Required"
        result["action"] = "Respond within 4 hours"
        result["skip_inbox"] = False
        result["priority"] = "High"
        return result

    # Rule 3: Calendar notifications
    if "calendar" in sender or "invitation" in subject:
        result["category"] = "Calendar"
        result["label"] = "Calendar"
        result["action"] = "Process via calendar app"
        result["skip_inbox"] = True
        return result

    # Rule 6: Receipts and invoices
    if any(kw in subject for kw in ["receipt", "invoice", "order", "shipped", "payment"]):
        result["category"] = "Receipt"
        result["label"] = "Personal/Receipts"
        result["action"] = "Auto-filed"
        result["skip_inbox"] = True
        return result

    # Rule 5: Newsletters
    if email.get("has_unsubscribe"):
        result["category"] = "Newsletter"
        result["label"] = "Newsletters/General"
        result["action"] = "Read in batch window or unsubscribe"
        result["skip_inbox"] = True
        return result

    # Rule 7: Hot threads where you are CC
    if email.get("thread_count", 1) > 5:
        result["category"] = "Read/Review"
        result["label"] = "@Read-Review"
        result["action"] = "Hot thread - review if relevant"
        result["skip_inbox"] = False
        return result

    # Default: needs triage
    result["category"] = "Needs Triage"
    result["label"] = None
    result["action"] = "Apply 2-minute rule: Delete, Do, Delegate, or Defer"
    result["skip_inbox"] = False
    return result


def main():
    parser = argparse.ArgumentParser(description="Scan and categorize inbox messages.")
    parser.add_argument("--account", required=True, help="Email account to process")
    parser.add_argument("--rules", default=None, help="Path to rules JSON file (optional)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without applying changes")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format")

    args = parser.parse_args()

    results = [categorize_email(email) for email in SAMPLE_EMAILS]

    if args.format == "json":
        output = {
            "account": args.account,
            "processed_at": datetime.now().isoformat(),
            "dry_run": args.dry_run,
            "total_emails": len(results),
            "results": results,
            "summary": {},
        }
        categories = {}
        for r in results:
            cat = r["category"]
            categories[cat] = categories.get(cat, 0) + 1
        output["summary"] = categories
        print(json.dumps(output, indent=2))
    else:
        mode = "DRY RUN" if args.dry_run else "LIVE"
        print(f"Inbox Organization [{mode}]")
        print(f"Account: {args.account}")
        print(f"Emails processed: {len(results)}")
        print("=" * 60)
        for r in results:
            skip = " [SKIP INBOX]" if r.get("skip_inbox") else ""
            priority = f" [{r.get('priority', '')}]" if r.get("priority") else ""
            print(f"\n  {r['from']}")
            print(f"    Subject: {r['subject']}")
            print(f"    Category: {r['category']}{priority}{skip}")
            print(f"    Label: {r.get('label', 'None')}")
            print(f"    Action: {r['action']}")
        print("\n" + "=" * 60)
        categories = {}
        for r in results:
            cat = r["category"]
            categories[cat] = categories.get(cat, 0) + 1
        print("Summary:", ", ".join(f"{k}: {v}" for k, v in categories.items()))


if __name__ == "__main__":
    main()
