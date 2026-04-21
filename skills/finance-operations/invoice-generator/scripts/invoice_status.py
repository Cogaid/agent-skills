#!/usr/bin/env python3
"""
Check payment status across invoices with aging analysis.

Usage:
    python invoice_status.py --status all
    python invoice_status.py --status overdue
    python invoice_status.py --status paid
    python invoice_status.py --client "Acme Corp"
"""

import argparse
import json
from datetime import datetime, timedelta

# Sample invoice data for demonstration
SAMPLE_INVOICES = [
    {
        "invoice_number": "INV-2026-0035",
        "client": "Acme Corp",
        "amount": 12500.00,
        "issue_date": "2026-01-15",
        "due_date": "2026-02-14",
        "paid_date": "2026-02-10",
        "status": "paid",
    },
    {
        "invoice_number": "INV-2026-0036",
        "client": "Globex Inc",
        "amount": 8750.00,
        "issue_date": "2026-02-01",
        "due_date": "2026-03-03",
        "paid_date": None,
        "status": "overdue",
    },
    {
        "invoice_number": "INV-2026-0037",
        "client": "Initech LLC",
        "amount": 3200.00,
        "issue_date": "2026-02-20",
        "due_date": "2026-03-22",
        "paid_date": None,
        "status": "overdue",
    },
    {
        "invoice_number": "INV-2026-0038",
        "client": "Acme Corp",
        "amount": 6000.00,
        "issue_date": "2026-03-01",
        "due_date": "2026-03-31",
        "paid_date": "2026-03-28",
        "status": "paid",
    },
    {
        "invoice_number": "INV-2026-0039",
        "client": "Umbrella Co",
        "amount": 15000.00,
        "issue_date": "2026-03-15",
        "due_date": "2026-04-14",
        "paid_date": None,
        "status": "pending",
    },
    {
        "invoice_number": "INV-2026-0040",
        "client": "Globex Inc",
        "amount": 4500.00,
        "issue_date": "2026-04-01",
        "due_date": "2026-05-01",
        "paid_date": None,
        "status": "pending",
    },
    {
        "invoice_number": "INV-2026-0041",
        "client": "Stark Industries",
        "amount": 22000.00,
        "issue_date": "2025-12-01",
        "due_date": "2025-12-31",
        "paid_date": None,
        "status": "overdue",
    },
]


def calculate_aging(due_date_str, reference_date=None):
    """Calculate days overdue from due date."""
    if reference_date is None:
        reference_date = datetime.now()
    due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
    delta = (reference_date - due_date).days
    return max(0, delta)


def get_aging_bucket(days_overdue):
    """Classify into aging bucket."""
    if days_overdue == 0:
        return "Current"
    elif days_overdue <= 30:
        return "1-30 days"
    elif days_overdue <= 60:
        return "31-60 days"
    elif days_overdue <= 90:
        return "61-90 days"
    else:
        return "90+ days"


def filter_invoices(invoices, status=None, client=None):
    """Filter invoices by status and/or client."""
    results = invoices
    if status and status != "all":
        results = [inv for inv in results if inv["status"] == status]
    if client:
        results = [inv for inv in results if client.lower() in inv["client"].lower()]
    return results


def print_status_table(invoices):
    """Print a formatted status table."""
    if not invoices:
        print("No invoices found matching the criteria.")
        return

    print()
    print(f"{'Invoice #':<18} {'Client':<20} {'Amount':>12} {'Due Date':<12} {'Status':<10} {'Aging':<12}")
    print(f"{'─'*18} {'─'*20} {'─'*12} {'─'*12} {'─'*10} {'─'*12}")

    total_outstanding = 0.0
    aging_summary = {"Current": 0, "1-30 days": 0, "31-60 days": 0, "61-90 days": 0, "90+ days": 0}

    for inv in invoices:
        days = calculate_aging(inv["due_date"])
        bucket = get_aging_bucket(days) if inv["status"] != "paid" else "Paid"
        aging_str = f"{days}d" if inv["status"] != "paid" else "--"

        status_display = inv["status"].upper()
        print(f"{inv['invoice_number']:<18} {inv['client']:<20} ${inv['amount']:>11,.2f} {inv['due_date']:<12} {status_display:<10} {aging_str:<12}")

        if inv["status"] != "paid":
            total_outstanding += inv["amount"]
            if bucket in aging_summary:
                aging_summary[bucket] += inv["amount"]

    print(f"{'─'*18} {'─'*20} {'─'*12} {'─'*12} {'─'*10} {'─'*12}")
    print(f"{'Total Outstanding:':>38} ${total_outstanding:>11,.2f}")
    print()

    # Aging summary
    if total_outstanding > 0:
        print("AGING SUMMARY:")
        print(f"  {'Bucket':<15} {'Amount':>12} {'%':>8}")
        print(f"  {'─'*15} {'─'*12} {'─'*8}")
        for bucket, amount in aging_summary.items():
            if amount > 0:
                pct = (amount / total_outstanding) * 100
                print(f"  {bucket:<15} ${amount:>11,.2f} {pct:>7.1f}%")
        print()


def main():
    parser = argparse.ArgumentParser(
        description="Check payment status and aging for invoices.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --status all
  %(prog)s --status overdue
  %(prog)s --client "Acme Corp"
  %(prog)s --status overdue --format json
        """,
    )
    parser.add_argument("--status", default="all",
                        choices=["all", "pending", "overdue", "paid"],
                        help="Filter by invoice status (default: all)")
    parser.add_argument("--client", default=None, help="Filter by client name")
    parser.add_argument("--format", choices=["table", "json"], default="table",
                        help="Output format (default: table)")

    args = parser.parse_args()
    invoices = filter_invoices(SAMPLE_INVOICES, status=args.status, client=args.client)

    if args.format == "json":
        enriched = []
        for inv in invoices:
            days = calculate_aging(inv["due_date"])
            enriched.append({
                **inv,
                "days_overdue": days if inv["status"] != "paid" else 0,
                "aging_bucket": get_aging_bucket(days) if inv["status"] != "paid" else "Paid",
            })
        print(json.dumps(enriched, indent=2))
    else:
        print(f"\nInvoice Status Report - {datetime.now().strftime('%Y-%m-%d')}")
        print(f"Filter: status={args.status}" + (f", client={args.client}" if args.client else ""))
        print_status_table(invoices)


if __name__ == "__main__":
    main()
