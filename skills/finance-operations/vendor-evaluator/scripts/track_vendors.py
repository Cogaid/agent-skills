#!/usr/bin/env python3
"""
Manage vendor evaluation pipeline and track progress.

Usage:
    python track_vendors.py --status
    python track_vendors.py --project "CRM Selection"
    python track_vendors.py --status --format json
"""

import argparse
import json
from datetime import datetime

SAMPLE_EVALUATIONS = [
    {
        "project": "CRM Platform Selection",
        "owner": "Sarah Chen",
        "start_date": "2026-02-15",
        "target_decision": "2026-05-01",
        "budget": 50000,
        "status": "demos",
        "vendors": [
            {"name": "CloudPlatform Pro", "status": "demo_complete", "score": 4.2, "notes": "Strong enterprise features"},
            {"name": "AgileTools Inc", "status": "demo_complete", "score": 4.0, "notes": "Best UX, weaker on security"},
            {"name": "BudgetSoft", "status": "eliminated", "score": 2.8, "notes": "Failed SOC 2 deal-breaker"},
        ],
        "next_steps": [
            "Complete reference checks for top 2 vendors",
            "Negotiate pricing with CloudPlatform Pro",
            "Run 2-week pilot with AgileTools Inc",
        ],
        "stage_history": [
            {"stage": "requirements", "date": "2026-02-15", "status": "complete"},
            {"stage": "shortlist", "date": "2026-03-01", "status": "complete"},
            {"stage": "demos", "date": "2026-03-15", "status": "in_progress"},
            {"stage": "evaluation", "date": None, "status": "pending"},
            {"stage": "negotiation", "date": None, "status": "pending"},
            {"stage": "decision", "date": None, "status": "pending"},
        ],
    },
    {
        "project": "Marketing Automation Tool",
        "owner": "Mike Rodriguez",
        "start_date": "2026-03-01",
        "target_decision": "2026-06-15",
        "budget": 30000,
        "status": "shortlist",
        "vendors": [
            {"name": "MarketFlow", "status": "shortlisted", "score": None, "notes": "Strong G2 reviews"},
            {"name": "AutoReach", "status": "shortlisted", "score": None, "notes": "Best integration with our CRM"},
            {"name": "GrowthEngine", "status": "shortlisted", "score": None, "notes": "Recommended by peer"},
            {"name": "MailBlast Pro", "status": "eliminated", "score": None, "notes": "Insufficient API capabilities"},
        ],
        "next_steps": [
            "Send demo requests to 3 shortlisted vendors",
            "Schedule demos for weeks of April 28 and May 5",
            "Prepare demo evaluation scorecard",
        ],
        "stage_history": [
            {"stage": "requirements", "date": "2026-03-01", "status": "complete"},
            {"stage": "shortlist", "date": "2026-04-01", "status": "in_progress"},
            {"stage": "demos", "date": None, "status": "pending"},
            {"stage": "evaluation", "date": None, "status": "pending"},
            {"stage": "negotiation", "date": None, "status": "pending"},
            {"stage": "decision", "date": None, "status": "pending"},
        ],
    },
    {
        "project": "Cloud Hosting Migration",
        "owner": "Priya Patel",
        "start_date": "2025-11-01",
        "target_decision": "2026-02-01",
        "budget": 80000,
        "status": "complete",
        "vendors": [
            {"name": "AWS", "status": "selected", "score": 4.5, "notes": "Best fit for scale and ecosystem"},
            {"name": "Google Cloud", "status": "runner_up", "score": 4.3, "notes": "Strong on ML, weaker support"},
            {"name": "Azure", "status": "eliminated", "score": 3.8, "notes": "Pricing complexity, integration gaps"},
        ],
        "next_steps": [],
        "stage_history": [
            {"stage": "requirements", "date": "2025-11-01", "status": "complete"},
            {"stage": "shortlist", "date": "2025-11-15", "status": "complete"},
            {"stage": "demos", "date": "2025-12-01", "status": "complete"},
            {"stage": "evaluation", "date": "2026-01-05", "status": "complete"},
            {"stage": "negotiation", "date": "2026-01-20", "status": "complete"},
            {"stage": "decision", "date": "2026-02-01", "status": "complete"},
        ],
    },
]

STAGE_ORDER = ["requirements", "shortlist", "demos", "evaluation", "negotiation", "decision"]


def print_pipeline(evaluations):
    """Print vendor evaluation pipeline."""
    print("=" * 80)
    print(f"  VENDOR EVALUATION PIPELINE")
    print(f"  As of: {datetime.now().strftime('%Y-%m-%d')}")
    print("=" * 80)

    active = [e for e in evaluations if e["status"] != "complete"]
    completed = [e for e in evaluations if e["status"] == "complete"]

    if active:
        print(f"\n  ACTIVE EVALUATIONS ({len(active)}):")
        print(f"  {'─'*75}")

        for ev in active:
            today = datetime.now()
            target = datetime.strptime(ev["target_decision"], "%Y-%m-%d")
            days_left = (target - today).days

            print(f"\n  {ev['project']}")
            print(f"    Owner: {ev['owner']} | Budget: ${ev['budget']:,}/yr | Target: {ev['target_decision']} ({days_left}d left)")

            # Stage progress
            current_idx = STAGE_ORDER.index(ev["status"]) if ev["status"] in STAGE_ORDER else 0
            progress = "    Stages: "
            for i, stage in enumerate(STAGE_ORDER):
                if i < current_idx:
                    progress += f"[{stage}] -> "
                elif i == current_idx:
                    progress += f"[>{stage}<] -> "
                else:
                    progress += f"[{stage}] -> "
            print(progress.rstrip(" -> "))

            # Vendors
            print(f"    Vendors:")
            for v in ev["vendors"]:
                score_str = f"Score: {v['score']:.1f}" if v["score"] else "Not scored"
                status_upper = v["status"].replace("_", " ").title()
                print(f"      {v['name']:<25} {status_upper:<18} {score_str}")

            if ev["next_steps"]:
                print(f"    Next steps:")
                for step in ev["next_steps"]:
                    print(f"      - {step}")

    if completed:
        print(f"\n  COMPLETED EVALUATIONS ({len(completed)}):")
        print(f"  {'─'*75}")
        for ev in completed:
            selected = next((v for v in ev["vendors"] if v["status"] == "selected"), None)
            print(f"    {ev['project']} -> Selected: {selected['name'] if selected else 'N/A'} ({ev['stage_history'][-1]['date']})")

    # Summary stats
    print(f"\n  SUMMARY:")
    print(f"    Active evaluations:    {len(active)}")
    print(f"    Completed:             {len(completed)}")
    total_budget = sum(e["budget"] for e in active)
    print(f"    Active budget at stake: ${total_budget:,}/yr")
    overdue = sum(1 for e in active if datetime.strptime(e["target_decision"], "%Y-%m-%d") < datetime.now())
    if overdue:
        print(f"    OVERDUE:               {overdue} evaluation(s)")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Track vendor evaluation pipeline and progress.",
    )
    parser.add_argument("--status", action="store_true", help="Show evaluation pipeline status")
    parser.add_argument("--project", default=None, help="Filter by project name")
    parser.add_argument("--format", choices=["text", "json"], default="text")

    args = parser.parse_args()

    evaluations = SAMPLE_EVALUATIONS
    if args.project:
        evaluations = [e for e in evaluations if args.project.lower() in e["project"].lower()]

    if args.format == "json":
        print(json.dumps(evaluations, indent=2))
    else:
        print_pipeline(evaluations)


if __name__ == "__main__":
    main()
