#!/usr/bin/env python3
"""
Calculate appropriate compensation based on situation parameters.

Usage:
    python calculate_compensation.py --tier pro --impact high --duration 8
    python calculate_compensation.py --tier enterprise --impact critical --churn-risk

Output: JSON with compensation recommendation and justification
"""

import argparse
import json
import sys
from datetime import datetime

# Compensation matrix
COMPENSATION_MATRIX = {
    "free": {
        "minor": {"type": "apology", "value": 0, "description": "Sincere apology"},
        "moderate": {"type": "apology", "value": 0, "description": "Apology with explanation"},
        "high": {"type": "goodwill", "value": 0, "description": "Extended trial consideration"},
        "critical": {"type": "escalate", "value": 0, "description": "Manager discretion"}
    },
    "pro": {
        "minor": {"type": "apology", "value": 0, "description": "Sincere apology"},
        "moderate": {"type": "credit", "value": 7, "description": "1 week service credit"},
        "high": {"type": "credit", "value": 14, "description": "2 weeks service credit"},
        "critical": {"type": "credit", "value": 30, "description": "1 month service credit"}
    },
    "enterprise": {
        "minor": {"type": "credit", "value": 7, "description": "1 week service credit"},
        "moderate": {"type": "credit", "value": 30, "description": "1 month service credit"},
        "high": {"type": "credit_plus", "value": 30, "description": "1 month credit + feature upgrade"},
        "critical": {"type": "custom", "value": 60, "description": "2 months + executive call + custom package"}
    }
}

# Impact duration multipliers
DURATION_MULTIPLIERS = {
    "< 1 hour": 0.5,
    "1-4 hours": 1.0,
    "4-24 hours": 1.5,
    "> 24 hours": 2.0
}

# Special circumstance modifiers
MODIFIERS = {
    "churn_risk": 1.5,
    "repeat_issue": 1.3,
    "our_fault_clear": 1.2,
    "vip_account": 1.5,
    "long_tenure": 1.2,  # Customer > 2 years
    "first_issue": 0.8
}


def get_duration_category(hours: float) -> str:
    """Categorize duration into buckets."""
    if hours < 1:
        return "< 1 hour"
    elif hours < 4:
        return "1-4 hours"
    elif hours < 24:
        return "4-24 hours"
    else:
        return "> 24 hours"


def calculate_compensation(
    tier: str,
    impact: str,
    duration_hours: float = 0,
    churn_risk: bool = False,
    repeat_issue: bool = False,
    our_fault: bool = True,
    vip: bool = False,
    tenure_years: float = 0
) -> dict:
    """Calculate recommended compensation."""

    # Normalize inputs
    tier = tier.lower()
    impact = impact.lower()

    # Validate
    if tier not in COMPENSATION_MATRIX:
        tier = "pro"  # Default
    if impact not in ["minor", "moderate", "high", "critical"]:
        impact = "moderate"  # Default

    # Get base compensation
    base = COMPENSATION_MATRIX[tier][impact].copy()

    # Calculate multiplier
    multiplier = 1.0

    # Duration impact
    duration_cat = get_duration_category(duration_hours)
    multiplier *= DURATION_MULTIPLIERS[duration_cat]

    # Apply modifiers
    modifiers_applied = []

    if churn_risk:
        multiplier *= MODIFIERS["churn_risk"]
        modifiers_applied.append("churn_risk")

    if repeat_issue:
        multiplier *= MODIFIERS["repeat_issue"]
        modifiers_applied.append("repeat_issue")

    if our_fault:
        multiplier *= MODIFIERS["our_fault_clear"]
        modifiers_applied.append("our_fault")

    if vip:
        multiplier *= MODIFIERS["vip_account"]
        modifiers_applied.append("vip_account")

    if tenure_years > 2:
        multiplier *= MODIFIERS["long_tenure"]
        modifiers_applied.append("long_tenure")

    # Calculate final value
    final_value_days = int(base["value"] * multiplier)

    # Determine approval level
    if final_value_days == 0:
        approval = "agent"
    elif final_value_days <= 14:
        approval = "agent"
    elif final_value_days <= 30:
        approval = "team_lead"
    elif final_value_days <= 60:
        approval = "manager"
    else:
        approval = "director"

    # Build recommendation
    recommendation = {
        "compensation_type": base["type"],
        "base_value_days": base["value"],
        "final_value_days": final_value_days,
        "description": base["description"],
        "multiplier_applied": round(multiplier, 2),
        "modifiers_applied": modifiers_applied,
        "approval_required": approval,
        "justification": []
    }

    # Build justification
    justification = []
    justification.append(f"Customer tier: {tier.title()}")
    justification.append(f"Impact level: {impact.title()}")

    if duration_hours > 0:
        justification.append(f"Duration: {duration_hours} hours ({duration_cat})")

    if modifiers_applied:
        justification.append(f"Factors: {', '.join(modifiers_applied)}")

    recommendation["justification"] = justification

    # Add alternative options
    if final_value_days > 0:
        recommendation["alternatives"] = [
            {
                "option": "Service credit",
                "value": f"{final_value_days} days",
                "approval": approval
            }
        ]

        if tier == "enterprise" and final_value_days >= 30:
            recommendation["alternatives"].append({
                "option": "Feature upgrade",
                "value": "Add premium features for 3 months",
                "approval": "manager"
            })

        if impact in ["high", "critical"]:
            recommendation["alternatives"].append({
                "option": "Executive call",
                "value": "Personal call from leadership",
                "approval": "director"
            })

    return recommendation


def main():
    parser = argparse.ArgumentParser(description="Calculate compensation")
    parser.add_argument("--tier", "-t", required=True,
                        choices=["free", "pro", "enterprise"],
                        help="Customer tier")
    parser.add_argument("--impact", "-i", required=True,
                        choices=["minor", "moderate", "high", "critical"],
                        help="Impact severity")
    parser.add_argument("--duration", "-d", type=float, default=0,
                        help="Duration in hours")
    parser.add_argument("--churn-risk", action="store_true",
                        help="Customer is at risk of churning")
    parser.add_argument("--repeat", action="store_true",
                        help="This is a repeat issue")
    parser.add_argument("--not-our-fault", action="store_true",
                        help="Issue was not caused by us")
    parser.add_argument("--vip", action="store_true",
                        help="VIP/strategic account")
    parser.add_argument("--tenure", type=float, default=0,
                        help="Customer tenure in years")
    parser.add_argument("--pretty", "-p", action="store_true",
                        help="Pretty print output")

    args = parser.parse_args()

    result = calculate_compensation(
        tier=args.tier,
        impact=args.impact,
        duration_hours=args.duration,
        churn_risk=args.churn_risk,
        repeat_issue=args.repeat,
        our_fault=not args.not_our_fault,
        vip=args.vip,
        tenure_years=args.tenure
    )

    if args.pretty:
        print(json.dumps(result, indent=2))
    else:
        print(json.dumps(result))


if __name__ == "__main__":
    main()
