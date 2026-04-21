#!/usr/bin/env python3
"""Generate facilitation materials for group decisions.

Usage:
    python facilitate_decision.py --participants 6 --method weighted-matrix
    python facilitate_decision.py --participants 4 --method rapid --format json
"""

import argparse
import json
import sys
from datetime import datetime, timedelta

SAMPLE_DECISION = {
    "question": "Which cloud provider should we migrate to?",
    "options": ["AWS", "Google Cloud", "Azure", "Stay on-prem (status quo)"],
    "criteria": [
        {"name": "Cost (3yr TCO)", "weight": 25},
        {"name": "Performance", "weight": 20},
        {"name": "Team expertise", "weight": 20},
        {"name": "Migration effort", "weight": 20},
        {"name": "Vendor lock-in risk", "weight": 15},
    ],
}


def generate_weighted_matrix_materials(decision: dict, participants: int) -> dict:
    """Generate pre-read and scoring sheets for weighted matrix."""
    meeting_date = (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d")

    agenda = {
        "meeting_type": "Decision Meeting - Weighted Matrix",
        "decision": decision["question"],
        "date": meeting_date,
        "duration": "90 minutes",
        "participants": participants,
        "agenda": [
            {"time": "5 min", "item": "Frame the decision -- what we are deciding and why now"},
            {"time": "10 min", "item": "Confirm criteria and weights -- adjust if group disagrees"},
            {"time": "15 min", "item": "Review each option -- facts only, no opinions yet"},
            {"time": "20 min", "item": "Individual scoring -- silent, independent scoring"},
            {"time": "15 min", "item": "Discuss outliers -- where scores differ by 2+ points"},
            {"time": "10 min", "item": "Re-score if needed -- after discussion"},
            {"time": "5 min", "item": "Calculate results and announce recommendation"},
            {"time": "5 min", "item": "Confirm decision and assign next steps"},
        ],
    }

    pre_read = {
        "title": f"Pre-Read: {decision['question']}",
        "distribute_by": (datetime.now() + timedelta(days=0)).strftime("%Y-%m-%d"),
        "sections": [
            {"heading": "Decision Context", "content": "We need to decide on a cloud provider by Q2 for the infrastructure modernization initiative."},
            {"heading": "Options", "content": decision["options"]},
            {"heading": "Proposed Criteria and Weights", "content": decision["criteria"]},
            {"heading": "Preparation", "content": "Please review the options and come prepared with your independent scores (1-5 scale) for each criterion."},
        ],
    }

    scoring_sheet = {
        "instructions": "Score each option 1-5 on each criterion. Score independently before discussion.",
        "scale": "1=Unacceptable, 2=Poor, 3=Adequate, 4=Good, 5=Excellent",
        "criteria": [c["name"] for c in decision["criteria"]],
        "weights": [c["weight"] for c in decision["criteria"]],
        "options": decision["options"],
        "sheets_needed": participants,
    }

    return {
        "agenda": agenda,
        "pre_read": pre_read,
        "scoring_sheet": scoring_sheet,
    }


def generate_rapid_materials(decision: dict, participants: int) -> dict:
    """Generate RAPID framework materials."""
    roles = {
        "R (Recommend)": "Drives analysis, proposes recommendation",
        "A (Agree)": "Has veto power, ensures compliance/legal OK",
        "P (Perform)": "Executes once decision is made",
        "I (Input)": "Provides expertise, data, perspective",
        "D (Decide)": "Makes the final call (ONE person only)",
    }

    suggested_allocation = []
    if participants >= 6:
        suggested_allocation = [
            {"role": "R", "count": 1, "note": "Usually the project lead or analyst"},
            {"role": "A", "count": 1, "note": "Legal, compliance, or finance lead"},
            {"role": "P", "count": 2, "note": "Engineering/ops team leads"},
            {"role": "I", "count": participants - 5, "note": "Subject matter experts"},
            {"role": "D", "count": 1, "note": "Executive sponsor or budget owner"},
        ]
    else:
        suggested_allocation = [
            {"role": "R", "count": 1},
            {"role": "A", "count": 0, "note": "Optional for small groups"},
            {"role": "P", "count": 1},
            {"role": "I", "count": max(1, participants - 3)},
            {"role": "D", "count": 1},
        ]

    return {
        "framework": "RAPID",
        "decision": decision["question"],
        "roles": roles,
        "suggested_allocation": suggested_allocation,
        "process": [
            "R completes analysis and proposes recommendation",
            "I provides feedback and data within 48 hours",
            "R revises recommendation based on input",
            "A reviews and either agrees or escalates concerns",
            "D makes the final decision",
            "P executes the decision",
        ],
        "timeline": {
            "analysis_complete": (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d"),
            "input_deadline": (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d"),
            "decision_date": (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d"),
        },
    }


def main():
    parser = argparse.ArgumentParser(description="Generate facilitation materials for group decisions.")
    parser.add_argument("--participants", type=int, required=True, help="Number of participants")
    parser.add_argument("--method", choices=["weighted-matrix", "rapid", "pros-cons"], default="weighted-matrix", help="Decision method")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format")

    args = parser.parse_args()

    if args.method == "weighted-matrix":
        materials = generate_weighted_matrix_materials(SAMPLE_DECISION, args.participants)
    elif args.method == "rapid":
        materials = generate_rapid_materials(SAMPLE_DECISION, args.participants)
    else:
        materials = generate_weighted_matrix_materials(SAMPLE_DECISION, args.participants)

    materials["generated_at"] = datetime.now().isoformat()
    materials["method"] = args.method
    materials["participants"] = args.participants

    if args.format == "json":
        print(json.dumps(materials, indent=2))
    else:
        print(f"Facilitation Materials: {SAMPLE_DECISION['question']}")
        print(f"Method: {args.method}")
        print(f"Participants: {args.participants}")
        print("=" * 60)

        if args.method == "weighted-matrix":
            print("\nAGENDA:")
            for item in materials["agenda"]["agenda"]:
                print(f"  [{item['time']}] {item['item']}")
            print(f"\nPRE-READ (distribute by {materials['pre_read']['distribute_by']}):")
            for section in materials["pre_read"]["sections"]:
                print(f"  - {section['heading']}")
            print(f"\nSCORING SHEETS: {materials['scoring_sheet']['sheets_needed']} copies needed")
            print(f"  Criteria: {', '.join(materials['scoring_sheet']['criteria'])}")
            print(f"  Options: {', '.join(materials['scoring_sheet']['options'])}")
        elif args.method == "rapid":
            print("\nROLE ASSIGNMENTS:")
            for alloc in materials["suggested_allocation"]:
                note = f" -- {alloc.get('note', '')}" if alloc.get("note") else ""
                print(f"  {alloc['role']}: {alloc['count']} person(s){note}")
            print(f"\nTIMELINE:")
            for step, date in materials["timeline"].items():
                print(f"  {step}: {date}")

        print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
