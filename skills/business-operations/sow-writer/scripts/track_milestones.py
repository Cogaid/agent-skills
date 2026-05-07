#!/usr/bin/env python3
"""
Track milestone status and dependencies for SOW engagements.

Usage:
    python track_milestones.py --sow SOW-2026-0015
    python track_milestones.py --sow SOW-2026-0015 --format json
    python track_milestones.py --all
"""

import argparse
import json
from datetime import datetime, timedelta

SAMPLE_SOWS = {
    "SOW-2026-0015": {
        "title": "Website Redesign - Acme Corp",
        "client": "Acme Corporation",
        "total_value": 120000,
        "start_date": "2026-02-01",
        "end_date": "2026-07-31",
        "milestones": [
            {
                "id": "M1", "name": "Project Kickoff & Plan Approved",
                "phase": "Discovery", "due_date": "2026-02-14",
                "status": "completed", "completed_date": "2026-02-12",
                "payment": 24000, "payment_status": "paid",
                "deliverables": ["Project Plan", "Requirements Document"],
                "blockers": [],
            },
            {
                "id": "M2", "name": "Design Approved",
                "phase": "Design", "due_date": "2026-03-21",
                "status": "completed", "completed_date": "2026-03-25",
                "payment": 24000, "payment_status": "paid",
                "deliverables": ["Wireframes", "Visual Designs", "Technical Spec"],
                "blockers": [],
                "notes": "4 days late due to client feedback delay",
            },
            {
                "id": "M3", "name": "Development Complete",
                "phase": "Development", "due_date": "2026-05-16",
                "status": "in_progress", "completed_date": None,
                "payment": 36000, "payment_status": "pending",
                "deliverables": ["Working Application", "Test Results"],
                "blockers": ["Waiting for API credentials from client (requested 2026-04-10)"],
                "notes": "Sprint 1 complete, Sprint 2 in progress",
            },
            {
                "id": "M4", "name": "UAT Complete",
                "phase": "Testing", "due_date": "2026-06-13",
                "status": "not_started", "completed_date": None,
                "payment": 0, "payment_status": "n/a",
                "deliverables": ["UAT Sign-off", "Bug Fix Report"],
                "blockers": [],
            },
            {
                "id": "M5", "name": "Go-Live",
                "phase": "Launch", "due_date": "2026-07-11",
                "status": "not_started", "completed_date": None,
                "payment": 30000, "payment_status": "pending",
                "deliverables": ["Production Deployment", "Documentation", "Training"],
                "blockers": [],
            },
            {
                "id": "M6", "name": "Post-Launch Review",
                "phase": "Support", "due_date": "2026-07-31",
                "status": "not_started", "completed_date": None,
                "payment": 6000, "payment_status": "pending",
                "deliverables": ["30-Day Review Report"],
                "blockers": [],
            },
        ],
        "change_orders": [
            {
                "id": "CO-001", "description": "Add reporting dashboard module",
                "amount": 15000, "status": "approved", "date": "2026-03-15",
            },
        ],
    },
}


def print_milestone_tracker(sow_data):
    """Print formatted milestone tracker."""
    today = datetime.now()
    print("=" * 80)
    print(f"  MILESTONE TRACKER: {sow_data['title']}")
    print(f"  SOW Value: ${sow_data['total_value']:,.0f}")
    print(f"  Period: {sow_data['start_date']} to {sow_data['end_date']}")
    print(f"  As of: {today.strftime('%Y-%m-%d')}")
    print("=" * 80)

    status_icons = {
        "completed": "DONE",
        "in_progress": "ACTIVE",
        "not_started": "PENDING",
        "blocked": "BLOCKED",
        "at_risk": "AT RISK",
    }

    total_payments = 0
    paid_amount = 0

    print(f"\n  {'ID':<5} {'Milestone':<30} {'Due':<12} {'Status':<10} {'Payment':>10}")
    print(f"  {'─'*5} {'─'*30} {'─'*12} {'─'*10} {'─'*10}")

    for ms in sow_data["milestones"]:
        status = status_icons.get(ms["status"], ms["status"])
        due = datetime.strptime(ms["due_date"], "%Y-%m-%d")
        late = ""
        if ms["status"] != "completed" and due < today:
            days_late = (today - due).days
            late = f" ({days_late}d late)"
        elif ms["status"] == "completed" and ms.get("completed_date"):
            comp = datetime.strptime(ms["completed_date"], "%Y-%m-%d")
            if comp > due:
                late = f" ({(comp - due).days}d late)"

        pmt = f"${ms['payment']:,.0f}" if ms["payment"] else "--"
        print(f"  {ms['id']:<5} {ms['name']:<30} {ms['due_date']:<12} {status:<10} {pmt:>10}{late}")

        total_payments += ms["payment"]
        if ms["payment_status"] == "paid":
            paid_amount += ms["payment"]

    # Summary
    completed = sum(1 for m in sow_data["milestones"] if m["status"] == "completed")
    total = len(sow_data["milestones"])
    print(f"\n  PROGRESS: {completed}/{total} milestones complete ({completed/total*100:.0f}%)")
    print(f"  PAYMENTS: ${paid_amount:,.0f} paid / ${total_payments:,.0f} total ({paid_amount/total_payments*100:.0f}% billed)")

    # Blockers
    all_blockers = []
    for ms in sow_data["milestones"]:
        for b in ms.get("blockers", []):
            all_blockers.append({"milestone": ms["id"], "blocker": b})

    if all_blockers:
        print(f"\n  BLOCKERS:")
        print(f"  {'─'*70}")
        for b in all_blockers:
            print(f"    [{b['milestone']}] {b['blocker']}")

    # Change orders
    if sow_data.get("change_orders"):
        cos = sow_data["change_orders"]
        co_total = sum(co["amount"] for co in cos)
        print(f"\n  CHANGE ORDERS:")
        print(f"  {'─'*70}")
        for co in cos:
            print(f"    {co['id']}: {co['description']} (+${co['amount']:,.0f}) - {co['status'].upper()}")
        print(f"    Total change orders: ${co_total:,.0f}")
        print(f"    Revised SOW value: ${sow_data['total_value'] + co_total:,.0f}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Track SOW milestone status and dependencies.",
    )
    parser.add_argument("--sow", default=None, help="SOW number (e.g., SOW-2026-0015)")
    parser.add_argument("--all", action="store_true", help="Show all SOWs")
    parser.add_argument("--format", choices=["text", "json"], default="text")

    args = parser.parse_args()

    if args.all or args.sow is None:
        sow_ids = list(SAMPLE_SOWS.keys())
    else:
        sow_ids = [args.sow if args.sow in SAMPLE_SOWS else list(SAMPLE_SOWS.keys())[0]]

    for sow_id in sow_ids:
        sow_data = SAMPLE_SOWS[sow_id]
        if args.format == "json":
            print(json.dumps({sow_id: sow_data}, indent=2))
        else:
            print_milestone_tracker(sow_data)


if __name__ == "__main__":
    main()
