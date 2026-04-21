#!/usr/bin/env python3
"""
Track contract deadlines, renewals, and key dates.

Usage:
    python contract_tracker.py --upcoming 90
    python contract_tracker.py --status all
    python contract_tracker.py --upcoming 30 --format json
"""

import argparse
import json
from datetime import datetime, timedelta

SAMPLE_CONTRACTS = [
    {
        "id": "MSA-2024-001",
        "title": "Master Services Agreement",
        "counterparty": "Acme Corporation",
        "type": "MSA",
        "value": 240000,
        "effective_date": "2024-06-01",
        "expiration_date": "2026-05-31",
        "auto_renewal": True,
        "renewal_notice_days": 90,
        "status": "active",
        "key_dates": [
            {"date": "2026-03-02", "event": "Renewal notice deadline (90 days)"},
            {"date": "2026-05-31", "event": "Auto-renewal date"},
        ],
    },
    {
        "id": "SOW-2026-015",
        "title": "Website Redesign Project",
        "counterparty": "Acme Corporation",
        "type": "SOW",
        "value": 120000,
        "effective_date": "2026-02-01",
        "expiration_date": "2026-07-31",
        "auto_renewal": False,
        "renewal_notice_days": 0,
        "status": "active",
        "key_dates": [
            {"date": "2026-04-30", "event": "Milestone 3: Development complete"},
            {"date": "2026-06-15", "event": "UAT deadline"},
            {"date": "2026-07-31", "event": "Project completion"},
        ],
    },
    {
        "id": "SAAS-2025-008",
        "title": "CRM Platform Subscription",
        "counterparty": "CloudCRM Inc.",
        "type": "SaaS",
        "value": 36000,
        "effective_date": "2025-07-01",
        "expiration_date": "2026-06-30",
        "auto_renewal": True,
        "renewal_notice_days": 60,
        "status": "active",
        "key_dates": [
            {"date": "2026-05-01", "event": "Renewal notice deadline (60 days)"},
            {"date": "2026-06-30", "event": "Auto-renewal / expiration"},
        ],
    },
    {
        "id": "NDA-2025-022",
        "title": "Mutual NDA - Partnership Evaluation",
        "counterparty": "TechPartner Ltd.",
        "type": "NDA",
        "value": 0,
        "effective_date": "2025-10-01",
        "expiration_date": "2027-09-30",
        "auto_renewal": False,
        "renewal_notice_days": 0,
        "status": "active",
        "key_dates": [
            {"date": "2027-09-30", "event": "NDA expiration"},
        ],
    },
    {
        "id": "VENDOR-2025-004",
        "title": "Cloud Hosting Agreement",
        "counterparty": "HostPro Services",
        "type": "Vendor",
        "value": 60000,
        "effective_date": "2025-04-01",
        "expiration_date": "2026-03-31",
        "auto_renewal": True,
        "renewal_notice_days": 30,
        "status": "expired",
        "key_dates": [
            {"date": "2026-03-01", "event": "Renewal notice deadline (missed)"},
            {"date": "2026-03-31", "event": "Auto-renewed for 1 year"},
        ],
    },
]


def get_upcoming_dates(contracts, days_ahead):
    """Get all contract dates within the next N days."""
    today = datetime.now()
    cutoff = today + timedelta(days=days_ahead)
    upcoming = []

    for contract in contracts:
        for kd in contract["key_dates"]:
            event_date = datetime.strptime(kd["date"], "%Y-%m-%d")
            if today <= event_date <= cutoff:
                days_until = (event_date - today).days
                upcoming.append({
                    "contract_id": contract["id"],
                    "counterparty": contract["counterparty"],
                    "type": contract["type"],
                    "event": kd["event"],
                    "date": kd["date"],
                    "days_until": days_until,
                    "urgency": "critical" if days_until <= 7 else "high" if days_until <= 30 else "normal",
                })

    return sorted(upcoming, key=lambda x: x["days_until"])


def print_upcoming(upcoming, days_ahead):
    """Print upcoming contract events."""
    print("=" * 80)
    print(f"  UPCOMING CONTRACT EVENTS (next {days_ahead} days)")
    print(f"  As of: {datetime.now().strftime('%Y-%m-%d')}")
    print("=" * 80)

    if not upcoming:
        print(f"\n  No contract events in the next {days_ahead} days.")
        return

    print(f"\n  {'Date':<12} {'Days':>5} {'Urgency':<10} {'Contract':<18} {'Event'}")
    print(f"  {'─'*12} {'─'*5} {'─'*10} {'─'*18} {'─'*30}")

    for event in upcoming:
        urgency_display = event["urgency"].upper()
        print(f"  {event['date']:<12} {event['days_until']:>5}d {urgency_display:<10} {event['contract_id']:<18} {event['event']}")

    critical = [e for e in upcoming if e["urgency"] == "critical"]
    if critical:
        print(f"\n  CRITICAL (within 7 days):")
        for e in critical:
            print(f"    - {e['contract_id']}: {e['event']} on {e['date']}")


def print_all_contracts(contracts):
    """Print all contracts summary."""
    print("=" * 85)
    print(f"  CONTRACT PORTFOLIO")
    print(f"  As of: {datetime.now().strftime('%Y-%m-%d')}")
    print("=" * 85)

    print(f"\n  {'ID':<18} {'Counterparty':<20} {'Type':<8} {'Value':>10} {'Expires':<12} {'Status':<8}")
    print(f"  {'─'*18} {'─'*20} {'─'*8} {'─'*10} {'─'*12} {'─'*8}")

    total_value = 0
    for c in contracts:
        value_str = f"${c['value']:,.0f}" if c['value'] else "N/A"
        auto = " (AR)" if c["auto_renewal"] else ""
        print(f"  {c['id']:<18} {c['counterparty']:<20} {c['type']:<8} {value_str:>10} {c['expiration_date']:<12} {c['status'].upper():<8}{auto}")
        if c["status"] == "active":
            total_value += c["value"]

    print(f"\n  Active contracts: {sum(1 for c in contracts if c['status'] == 'active')}")
    print(f"  Total active value: ${total_value:,.0f}")
    print(f"  Auto-renewing: {sum(1 for c in contracts if c['auto_renewal'] and c['status'] == 'active')}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Track contract deadlines and renewals.",
    )
    parser.add_argument("--upcoming", type=int, default=None,
                        help="Show events in next N days")
    parser.add_argument("--status", default=None, choices=["all", "active", "expired"],
                        help="Filter by contract status")
    parser.add_argument("--format", choices=["text", "json"], default="text")

    args = parser.parse_args()

    if args.upcoming is not None:
        upcoming = get_upcoming_dates(SAMPLE_CONTRACTS, args.upcoming)
        if args.format == "json":
            print(json.dumps(upcoming, indent=2))
        else:
            print_upcoming(upcoming, args.upcoming)
    elif args.status:
        contracts = SAMPLE_CONTRACTS
        if args.status != "all":
            contracts = [c for c in contracts if c["status"] == args.status]
        if args.format == "json":
            print(json.dumps(contracts, indent=2))
        else:
            print_all_contracts(contracts)
    else:
        # Default: show upcoming 90 days + all contracts
        print_all_contracts(SAMPLE_CONTRACTS)
        upcoming = get_upcoming_dates(SAMPLE_CONTRACTS, 90)
        print_upcoming(upcoming, 90)


if __name__ == "__main__":
    main()
