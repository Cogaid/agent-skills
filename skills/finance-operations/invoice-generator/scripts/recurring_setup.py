#!/usr/bin/env python3
"""
Configure recurring invoices for clients.

Usage:
    python recurring_setup.py --client "Acme Corp" --amount 2500 --frequency monthly
    python recurring_setup.py --client "Acme Corp" --amount 2500 --frequency monthly --start 2026-05-01 --escalation 3.5
    python recurring_setup.py --list
"""

import argparse
import json
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

FREQUENCY_MAP = {
    "weekly": {"weeks": 1},
    "biweekly": {"weeks": 2},
    "monthly": {"months": 1},
    "quarterly": {"months": 3},
    "annually": {"years": 1},
}

SAMPLE_RECURRING = [
    {
        "id": "REC-001",
        "client": "Acme Corp",
        "description": "Monthly retainer - consulting services",
        "amount": 5000.00,
        "currency": "USD",
        "frequency": "monthly",
        "start_date": "2026-01-01",
        "end_date": None,
        "next_invoice": "2026-05-01",
        "escalation_pct": 3.0,
        "auto_send": True,
        "status": "active",
        "invoices_sent": 4,
    },
    {
        "id": "REC-002",
        "client": "Globex Inc",
        "description": "Quarterly hosting and support",
        "amount": 7500.00,
        "currency": "USD",
        "frequency": "quarterly",
        "start_date": "2026-01-01",
        "end_date": "2026-12-31",
        "next_invoice": "2026-07-01",
        "escalation_pct": 0,
        "auto_send": False,
        "status": "active",
        "invoices_sent": 2,
    },
]


def calculate_next_invoice(start_date_str, frequency, reference_date=None):
    """Calculate the next invoice date from start date and frequency."""
    if reference_date is None:
        reference_date = datetime.now()
    start = datetime.strptime(start_date_str, "%Y-%m-%d")
    current = start

    delta_kwargs = FREQUENCY_MAP.get(frequency, {"months": 1})

    while current <= reference_date:
        current += relativedelta(**delta_kwargs)

    return current.strftime("%Y-%m-%d")


def create_recurring(client, amount, frequency, description, currency, start_date,
                     end_date, escalation, auto_send):
    """Create a new recurring invoice configuration."""
    rec_id = f"REC-{datetime.now().strftime('%Y%m%d%H%M')}"
    if start_date is None:
        start_date = datetime.now().replace(day=1).strftime("%Y-%m-%d")

    next_inv = calculate_next_invoice(start_date, frequency)

    config = {
        "id": rec_id,
        "client": client,
        "description": description or f"{frequency.capitalize()} services",
        "amount": amount,
        "currency": currency,
        "frequency": frequency,
        "start_date": start_date,
        "end_date": end_date,
        "next_invoice": next_inv,
        "escalation_pct": escalation,
        "auto_send": auto_send,
        "status": "active",
        "invoices_sent": 0,
    }
    return config


def print_recurring_list(records):
    """Print formatted list of recurring invoices."""
    if not records:
        print("No recurring invoices configured.")
        return

    print()
    print(f"{'ID':<16} {'Client':<18} {'Amount':>10} {'Freq':<12} {'Next Invoice':<14} {'Status':<8}")
    print(f"{'─'*16} {'─'*18} {'─'*10} {'─'*12} {'─'*14} {'─'*8}")
    for rec in records:
        print(f"{rec['id']:<16} {rec['client']:<18} ${rec['amount']:>9,.2f} {rec['frequency']:<12} {rec['next_invoice']:<14} {rec['status']:<8}")
    print()

    total_monthly = 0
    for rec in records:
        if rec["status"] == "active":
            if rec["frequency"] == "weekly":
                total_monthly += rec["amount"] * 4.33
            elif rec["frequency"] == "biweekly":
                total_monthly += rec["amount"] * 2.17
            elif rec["frequency"] == "monthly":
                total_monthly += rec["amount"]
            elif rec["frequency"] == "quarterly":
                total_monthly += rec["amount"] / 3
            elif rec["frequency"] == "annually":
                total_monthly += rec["amount"] / 12

    print(f"  Total recurring monthly revenue (est.): ${total_monthly:,.2f}")
    print(f"  Total recurring annual revenue (est.):  ${total_monthly * 12:,.2f}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Configure and manage recurring invoices.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --client "Acme Corp" --amount 2500 --frequency monthly
  %(prog)s --client "Acme Corp" --amount 10000 --frequency quarterly --escalation 3.5
  %(prog)s --list
  %(prog)s --list --format json
        """,
    )
    parser.add_argument("--client", help="Client company name")
    parser.add_argument("--amount", type=float, help="Invoice amount per period")
    parser.add_argument("--frequency", choices=list(FREQUENCY_MAP.keys()),
                        help="Billing frequency")
    parser.add_argument("--description", default=None, help="Service description")
    parser.add_argument("--currency", default="USD", help="Currency code (default: USD)")
    parser.add_argument("--start", default=None, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", default=None, help="End date (YYYY-MM-DD) or omit for ongoing")
    parser.add_argument("--escalation", type=float, default=0, help="Annual escalation percentage")
    parser.add_argument("--auto-send", action="store_true", help="Enable auto-send")
    parser.add_argument("--list", action="store_true", help="List all recurring invoices")
    parser.add_argument("--format", choices=["text", "json"], default="text",
                        help="Output format (default: text)")

    args = parser.parse_args()

    if args.list:
        if args.format == "json":
            print(json.dumps(SAMPLE_RECURRING, indent=2))
        else:
            print("Recurring Invoice Configurations")
            print_recurring_list(SAMPLE_RECURRING)
        return

    if not args.client or not args.amount or not args.frequency:
        parser.error("--client, --amount, and --frequency are required when creating a recurring invoice")

    config = create_recurring(
        client=args.client,
        amount=args.amount,
        frequency=args.frequency,
        description=args.description,
        currency=args.currency,
        start_date=args.start,
        end_date=args.end,
        escalation=args.escalation,
        auto_send=args.auto_send,
    )

    if args.format == "json":
        print(json.dumps(config, indent=2))
    else:
        print(f"\nRecurring invoice configured successfully!")
        print(f"  ID:             {config['id']}")
        print(f"  Client:         {config['client']}")
        print(f"  Amount:         ${config['amount']:,.2f} {config['currency']}")
        print(f"  Frequency:      {config['frequency']}")
        print(f"  Start Date:     {config['start_date']}")
        print(f"  End Date:       {config['end_date'] or 'Ongoing'}")
        print(f"  Next Invoice:   {config['next_invoice']}")
        print(f"  Escalation:     {config['escalation_pct']}% annually")
        print(f"  Auto-send:      {'Yes' if config['auto_send'] else 'No'}")
        print()


if __name__ == "__main__":
    main()
