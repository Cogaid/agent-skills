#!/usr/bin/env python3
"""
Generate change order documents for SOW scope changes.

Usage:
    python change_order.py --sow SOW-2026-0015 --description "Add reporting module" --hours 80 --rate 175
    python change_order.py --sow SOW-2026-0015 --description "Additional user training" --cost 5000
"""

import argparse
import json
from datetime import datetime, timedelta

SAMPLE_SOW_CONTEXT = {
    "SOW-2026-0015": {
        "title": "Website Redesign - Acme Corp",
        "client": "Acme Corporation",
        "original_value": 120000,
        "previous_cos": 15000,
        "current_end_date": "2026-07-31",
        "co_count": 1,
    },
}


def generate_change_order(sow_id, description, reason, hours, rate, cost, schedule_impact_days):
    """Generate a change order document."""
    context = SAMPLE_SOW_CONTEXT.get(sow_id, {
        "title": "Project",
        "client": "Client",
        "original_value": 100000,
        "previous_cos": 0,
        "current_end_date": (datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d"),
        "co_count": 0,
    })

    co_number = context["co_count"] + 1
    co_id = f"CO-{sow_id}-{co_number:03d}"

    # Calculate cost
    if cost:
        additional_cost = cost
    elif hours and rate:
        additional_cost = hours * rate
    elif hours:
        additional_cost = hours * 175  # default rate
    else:
        additional_cost = 0

    # Calculate schedule impact
    current_end = datetime.strptime(context["current_end_date"], "%Y-%m-%d")
    new_end = current_end + timedelta(days=schedule_impact_days) if schedule_impact_days else current_end

    new_total = context["original_value"] + context["previous_cos"] + additional_cost

    change_order = {
        "change_order_id": co_id,
        "sow_reference": sow_id,
        "sow_title": context["title"],
        "client": context["client"],
        "date_requested": datetime.now().strftime("%Y-%m-%d"),
        "description": description,
        "reason": reason or "Client-requested scope addition",
        "impact": {
            "additional_hours": hours,
            "hourly_rate": rate,
            "additional_cost": additional_cost,
            "schedule_impact_days": schedule_impact_days or 0,
            "current_end_date": context["current_end_date"],
            "new_end_date": new_end.strftime("%Y-%m-%d"),
        },
        "financial_summary": {
            "original_sow_value": context["original_value"],
            "previous_change_orders": context["previous_cos"],
            "this_change_order": additional_cost,
            "new_total": new_total,
            "total_change_pct": round((context["previous_cos"] + additional_cost) / context["original_value"] * 100, 1),
        },
        "status": "pending_approval",
    }
    return change_order


def print_change_order(co):
    """Print formatted change order."""
    print("=" * 65)
    print(f"  CHANGE ORDER: {co['change_order_id']}")
    print("=" * 65)
    print(f"  SOW Reference:  {co['sow_reference']}")
    print(f"  Project:        {co['sow_title']}")
    print(f"  Client:         {co['client']}")
    print(f"  Date Requested: {co['date_requested']}")
    print(f"  Status:         {co['status'].upper()}")

    print(f"\n  DESCRIPTION OF CHANGE:")
    print(f"  {co['description']}")

    print(f"\n  REASON FOR CHANGE:")
    print(f"  {co['reason']}")

    imp = co["impact"]
    print(f"\n  IMPACT ASSESSMENT:")
    if imp["additional_hours"]:
        print(f"    Additional Hours:  {imp['additional_hours']}")
    if imp["hourly_rate"]:
        print(f"    Rate:              ${imp['hourly_rate']:.2f}/hr")
    print(f"    Cost Impact:       +${imp['additional_cost']:,.2f}")
    print(f"    Schedule Impact:   +{imp['schedule_impact_days']} days")
    print(f"    Current End:       {imp['current_end_date']}")
    print(f"    New End:           {imp['new_end_date']}")

    fin = co["financial_summary"]
    print(f"\n  FINANCIAL SUMMARY:")
    print(f"    Original SOW Value:       ${fin['original_sow_value']:>12,.2f}")
    print(f"    Previous Change Orders:   ${fin['previous_change_orders']:>12,.2f}")
    print(f"    This Change Order:       +${fin['this_change_order']:>12,.2f}")
    print(f"    {'─'*42}")
    print(f"    New Total:                ${fin['new_total']:>12,.2f}")
    print(f"    Total Change:             {fin['total_change_pct']:>11.1f}% over original")

    if fin["total_change_pct"] > 25:
        print(f"\n  WARNING: Total changes exceed 25% of original SOW value.")
        print(f"  Consider whether a new SOW is more appropriate.")

    print(f"\n  APPROVAL:")
    print(f"  Provider: ________________  Date: ________")
    print(f"  Client:   ________________  Date: ________")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Generate change order documents for SOW scope changes.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --sow SOW-2026-0015 --description "Add reporting module" --hours 80 --rate 175
  %(prog)s --sow SOW-2026-0015 --description "Training sessions" --cost 5000
  %(prog)s --sow SOW-2026-0015 --description "API integration" --hours 40 --schedule 14
        """,
    )
    parser.add_argument("--sow", required=True, help="SOW reference number")
    parser.add_argument("--description", required=True, help="Description of the change")
    parser.add_argument("--reason", default=None, help="Reason for the change")
    parser.add_argument("--hours", type=float, default=None, help="Additional hours")
    parser.add_argument("--rate", type=float, default=None, help="Hourly rate")
    parser.add_argument("--cost", type=float, default=None, help="Fixed additional cost")
    parser.add_argument("--schedule", type=int, default=0, help="Schedule impact in days")
    parser.add_argument("--format", choices=["text", "json"], default="text")

    args = parser.parse_args()
    co = generate_change_order(args.sow, args.description, args.reason,
                                args.hours, args.rate, args.cost, args.schedule)

    if args.format == "json":
        print(json.dumps(co, indent=2))
    else:
        print_change_order(co)


if __name__ == "__main__":
    main()
