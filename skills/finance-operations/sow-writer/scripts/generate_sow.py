#!/usr/bin/env python3
"""
Generate a Statement of Work from engagement parameters.

Usage:
    python generate_sow.py --client "Acme Corp" --type fixed-price --duration 12w
    python generate_sow.py --client "Acme Corp" --type tm --duration 6m --rate 175
    python generate_sow.py --client "Acme Corp" --type retainer --duration 12m --amount 5000
"""

import argparse
import json
from datetime import datetime, timedelta

ENGAGEMENT_TEMPLATES = {
    "fixed-price": {
        "type_label": "Fixed Price",
        "payment_structure": "Milestone-based",
        "milestones": [
            {"name": "SOW Execution (Deposit)", "pct": 20},
            {"name": "Design Approved", "pct": 20},
            {"name": "Development Complete", "pct": 30},
            {"name": "Go-Live Accepted", "pct": 25},
            {"name": "30-Day Post-Launch", "pct": 5},
        ],
        "default_value": 120000,
        "phases": [
            {"name": "Discovery & Planning", "duration_pct": 15, "deliverables": ["Project Plan", "Requirements Doc"]},
            {"name": "Design", "duration_pct": 20, "deliverables": ["Wireframes", "Visual Design", "Tech Spec"]},
            {"name": "Development", "duration_pct": 40, "deliverables": ["Working Prototype", "Test Results"]},
            {"name": "Testing & Launch", "duration_pct": 25, "deliverables": ["Final Deliverable", "Documentation", "Training"]},
        ],
    },
    "tm": {
        "type_label": "Time & Materials",
        "payment_structure": "Monthly invoicing, Net 30",
        "milestones": [
            {"name": "Monthly Invoice", "pct": None},
        ],
        "default_value": None,
        "phases": [
            {"name": "Ongoing Services", "duration_pct": 100, "deliverables": ["Monthly Status Reports", "Deliverables per Sprint"]},
        ],
    },
    "retainer": {
        "type_label": "Retainer",
        "payment_structure": "Monthly prepay, 1st of each month",
        "milestones": [
            {"name": "Monthly Retainer", "pct": None},
        ],
        "default_value": None,
        "phases": [
            {"name": "Ongoing Retainer Services", "duration_pct": 100, "deliverables": ["Monthly Activity Report", "Deliverables as defined"]},
        ],
    },
}


def parse_duration(duration_str):
    """Parse duration string like '12w', '6m', '3m' into weeks."""
    if duration_str.endswith("w"):
        return int(duration_str[:-1])
    elif duration_str.endswith("m"):
        return int(duration_str[:-1]) * 4
    elif duration_str.endswith("d"):
        return int(duration_str[:-1]) // 7
    return int(duration_str)


def generate_sow(client, eng_type, duration_str, rate, amount, project_name):
    """Generate SOW data structure."""
    template = ENGAGEMENT_TEMPLATES.get(eng_type, ENGAGEMENT_TEMPLATES["fixed-price"])
    duration_weeks = parse_duration(duration_str)
    start_date = datetime.now() + timedelta(days=7)  # Start in 1 week
    end_date = start_date + timedelta(weeks=duration_weeks)

    sow_number = f"SOW-{datetime.now().year}-{datetime.now().strftime('%m%d')}"

    # Calculate total value
    if eng_type == "fixed-price":
        total_value = amount or template["default_value"]
    elif eng_type == "tm":
        hourly_rate = rate or 175
        est_hours = duration_weeks * 40 * 0.8  # 80% utilization
        total_value = hourly_rate * est_hours
    elif eng_type == "retainer":
        monthly_amount = amount or 5000
        months = duration_weeks // 4
        total_value = monthly_amount * months
    else:
        total_value = amount or 100000

    # Build phases with dates
    phases = []
    current_week = 0
    for phase in template["phases"]:
        phase_weeks = max(1, round(duration_weeks * phase["duration_pct"] / 100))
        phase_start = start_date + timedelta(weeks=current_week)
        phase_end = start_date + timedelta(weeks=current_week + phase_weeks)
        phases.append({
            "name": phase["name"],
            "start_date": phase_start.strftime("%Y-%m-%d"),
            "end_date": phase_end.strftime("%Y-%m-%d"),
            "duration_weeks": phase_weeks,
            "deliverables": phase["deliverables"],
        })
        current_week += phase_weeks

    # Build payment schedule
    payments = []
    for ms in template["milestones"]:
        if ms["pct"] is not None:
            payments.append({
                "trigger": ms["name"],
                "amount": round(total_value * ms["pct"] / 100, 2),
                "percentage": ms["pct"],
            })
        else:
            payments.append({
                "trigger": ms["name"],
                "amount": amount or rate * 160 if rate else None,
                "percentage": None,
            })

    sow = {
        "sow_number": sow_number,
        "client": client,
        "project_name": project_name or f"{client} - Professional Services Engagement",
        "engagement_type": template["type_label"],
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": end_date.strftime("%Y-%m-%d"),
        "duration_weeks": duration_weeks,
        "total_value": round(total_value, 2),
        "payment_structure": template["payment_structure"],
        "payments": payments,
        "phases": phases,
        "rate": rate,
        "assumptions": [
            "Client will provide a single point of contact with decision-making authority",
            "Client feedback and approvals within 5 business days of submission",
            "Access to client systems and environments by project start date",
            "Work performed during standard business hours (US Eastern Time)",
        ],
        "exclusions": [
            "Ongoing maintenance and support (available under separate agreement)",
            "Third-party software licenses and subscription fees",
            "Content creation (copywriting, photography, video production)",
            "Data migration from legacy systems (unless specified in scope)",
        ],
        "generated": datetime.now().strftime("%Y-%m-%d"),
    }
    return sow


def print_sow(sow):
    """Print formatted SOW summary."""
    print("=" * 70)
    print(f"  STATEMENT OF WORK")
    print(f"  {sow['sow_number']}")
    print("=" * 70)
    print(f"  Client:           {sow['client']}")
    print(f"  Project:          {sow['project_name']}")
    print(f"  Type:             {sow['engagement_type']}")
    print(f"  Duration:         {sow['duration_weeks']} weeks")
    print(f"  Start Date:       {sow['start_date']}")
    print(f"  End Date:         {sow['end_date']}")
    print(f"  Total Value:      ${sow['total_value']:,.2f}")
    if sow["rate"]:
        print(f"  Hourly Rate:      ${sow['rate']:.2f}")

    print(f"\n  PHASES:")
    print(f"  {'─'*65}")
    for i, phase in enumerate(sow["phases"], 1):
        print(f"  Phase {i}: {phase['name']} ({phase['start_date']} to {phase['end_date']}, {phase['duration_weeks']}w)")
        for d in phase["deliverables"]:
            print(f"    - {d}")

    print(f"\n  PAYMENT SCHEDULE:")
    print(f"  {'─'*65}")
    print(f"  Structure: {sow['payment_structure']}")
    for p in sow["payments"]:
        pct_str = f" ({p['percentage']}%)" if p["percentage"] else ""
        amt_str = f"${p['amount']:,.2f}" if p["amount"] else "Per timesheet"
        print(f"    {p['trigger']:<35} {amt_str:>12}{pct_str}")

    print(f"\n  ASSUMPTIONS:")
    for a in sow["assumptions"]:
        print(f"    - {a}")

    print(f"\n  EXCLUSIONS:")
    for e in sow["exclusions"]:
        print(f"    - {e}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Generate Statement of Work from engagement parameters.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --client "Acme Corp" --type fixed-price --duration 12w
  %(prog)s --client "Acme Corp" --type tm --duration 6m --rate 175
  %(prog)s --client "Acme Corp" --type retainer --duration 12m --amount 5000
        """,
    )
    parser.add_argument("--client", required=True, help="Client company name")
    parser.add_argument("--type", required=True, choices=["fixed-price", "tm", "retainer"],
                        help="Engagement type")
    parser.add_argument("--duration", required=True, help="Duration (e.g., 12w, 6m, 3m)")
    parser.add_argument("--rate", type=float, default=None, help="Hourly rate (for T&M)")
    parser.add_argument("--amount", type=float, default=None, help="Contract value (fixed) or monthly amount (retainer)")
    parser.add_argument("--project", default=None, help="Project name")
    parser.add_argument("--format", choices=["text", "json"], default="text")

    args = parser.parse_args()
    sow = generate_sow(args.client, args.type, args.duration, args.rate, args.amount, args.project)

    if args.format == "json":
        print(json.dumps(sow, indent=2))
    else:
        print_sow(sow)


if __name__ == "__main__":
    main()
