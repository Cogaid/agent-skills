#!/usr/bin/env python3
"""
Subscription management utility.

Usage:
    python subscription_manager.py --action upgrade --plan pro
    python subscription_manager.py --action cancel --reason price
    python subscription_manager.py --action pause --duration 30
    python subscription_manager.py --retention-offers

Output: Subscription changes and retention recommendations
"""

import argparse
import json
from datetime import datetime, timedelta


# Plan definitions
PLANS = {
    "free": {
        "name": "Free",
        "price": 0,
        "period": "forever",
        "features": ["Basic features", "Community support", "1 GB storage"]
    },
    "basic": {
        "name": "Basic",
        "price": 19,
        "period": "month",
        "features": ["All Free features", "Email support", "10 GB storage", "5 team members"]
    },
    "pro": {
        "name": "Professional",
        "price": 49,
        "period": "month",
        "features": ["All Basic features", "Priority support", "100 GB storage", "25 team members", "API access"]
    },
    "enterprise": {
        "name": "Enterprise",
        "price": 199,
        "period": "month",
        "features": ["All Pro features", "Dedicated support", "Unlimited storage", "Unlimited team members", "Custom integrations", "SLA"]
    }
}

# Cancellation reasons and responses
CANCELLATION_REASONS = {
    "price": {
        "label": "Too expensive",
        "offers": ["discount_20", "downgrade", "annual_discount"],
        "response": "I understand budget is a concern. Let me see what options we have."
    },
    "value": {
        "label": "Not getting enough value",
        "offers": ["training", "feature_tour", "usage_analysis"],
        "response": "I'd love to help you get more value from your subscription."
    },
    "features": {
        "label": "Missing features I need",
        "offers": ["roadmap_preview", "feature_request", "upgrade_trial"],
        "response": "I'd like to understand what features you're looking for."
    },
    "competitor": {
        "label": "Switching to competitor",
        "offers": ["comparison_help", "price_match", "exit_interview"],
        "response": "I appreciate your honesty. May I ask which solution you're considering?"
    },
    "usage": {
        "label": "Not using it enough",
        "offers": ["pause", "downgrade", "training"],
        "response": "Totally understand. Would a pause option work for you?"
    },
    "temporary": {
        "label": "Temporary situation",
        "offers": ["pause", "discount_temp", "downgrade_temp"],
        "response": "I get it - life happens. Let me offer some flexibility."
    },
    "experience": {
        "label": "Poor experience",
        "offers": ["escalation", "free_month", "dedicated_support"],
        "response": "I'm sorry to hear that. I want to make this right."
    },
    "other": {
        "label": "Other reason",
        "offers": ["explore", "pause", "downgrade"],
        "response": "Thank you for sharing. Tell me more so I can help."
    }
}

# Retention offers
RETENTION_OFFERS = {
    "discount_20": {
        "name": "20% discount for 3 months",
        "type": "discount",
        "value": 20,
        "duration": 3,
        "success_rate": 0.22
    },
    "discount_temp": {
        "name": "30% discount for 2 months",
        "type": "discount",
        "value": 30,
        "duration": 2,
        "success_rate": 0.25
    },
    "downgrade": {
        "name": "Downgrade to lower plan",
        "type": "plan_change",
        "success_rate": 0.35
    },
    "downgrade_temp": {
        "name": "Temporary downgrade (3 months)",
        "type": "plan_change",
        "duration": 3,
        "success_rate": 0.30
    },
    "annual_discount": {
        "name": "Switch to annual (2 months free)",
        "type": "billing_change",
        "success_rate": 0.18
    },
    "pause": {
        "name": "Pause subscription",
        "type": "pause",
        "duration_options": [1, 2, 3],
        "success_rate": 0.28
    },
    "training": {
        "name": "Free training session",
        "type": "service",
        "success_rate": 0.15
    },
    "feature_tour": {
        "name": "Personalized feature walkthrough",
        "type": "service",
        "success_rate": 0.12
    },
    "roadmap_preview": {
        "name": "Preview of upcoming features",
        "type": "information",
        "success_rate": 0.10
    },
    "free_month": {
        "name": "One month free",
        "type": "credit",
        "success_rate": 0.20
    },
    "escalation": {
        "name": "Escalate to customer success",
        "type": "escalation",
        "success_rate": 0.25
    }
}


def calculate_proration(current_plan, new_plan, days_remaining, days_in_period=30):
    """Calculate proration for plan change."""

    current_price = PLANS.get(current_plan, {}).get("price", 0)
    new_price = PLANS.get(new_plan, {}).get("price", 0)

    current_daily = current_price / days_in_period
    new_daily = new_price / days_in_period

    credit = round(current_daily * days_remaining, 2)
    charge = round(new_daily * days_remaining, 2)
    net = round(charge - credit, 2)

    return {
        "current_plan": current_plan,
        "new_plan": new_plan,
        "days_remaining": days_remaining,
        "credit": credit,
        "charge": charge,
        "net_charge": net if net > 0 else 0,
        "net_credit": abs(net) if net < 0 else 0
    }


def process_upgrade(current_plan, new_plan, days_remaining=15):
    """Process plan upgrade."""

    if current_plan not in PLANS or new_plan not in PLANS:
        return {"error": "Invalid plan"}

    current_idx = list(PLANS.keys()).index(current_plan)
    new_idx = list(PLANS.keys()).index(new_plan)

    if new_idx <= current_idx:
        return {"error": "New plan must be higher tier for upgrade"}

    proration = calculate_proration(current_plan, new_plan, days_remaining)

    new_features = []
    current_features = PLANS[current_plan]["features"]
    for feature in PLANS[new_plan]["features"]:
        if feature not in current_features:
            new_features.append(feature)

    return {
        "action": "upgrade",
        "from": PLANS[current_plan]["name"],
        "to": PLANS[new_plan]["name"],
        "new_price": f"${PLANS[new_plan]['price']}/month",
        "proration": proration,
        "new_features": new_features,
        "effective": "immediately",
        "message": f"Upgrade to {PLANS[new_plan]['name']} - you'll be charged ${proration['net_charge']} today"
    }


def process_downgrade(current_plan, new_plan):
    """Process plan downgrade."""

    if current_plan not in PLANS or new_plan not in PLANS:
        return {"error": "Invalid plan"}

    current_idx = list(PLANS.keys()).index(current_plan)
    new_idx = list(PLANS.keys()).index(new_plan)

    if new_idx >= current_idx:
        return {"error": "New plan must be lower tier for downgrade"}

    # Features that will be lost
    lost_features = []
    new_features = PLANS[new_plan]["features"]
    for feature in PLANS[current_plan]["features"]:
        if feature not in new_features:
            lost_features.append(feature)

    return {
        "action": "downgrade",
        "from": PLANS[current_plan]["name"],
        "to": PLANS[new_plan]["name"],
        "new_price": f"${PLANS[new_plan]['price']}/month",
        "lost_features": lost_features,
        "effective": "end of current billing period",
        "message": f"Downgrade to {PLANS[new_plan]['name']} will take effect at the end of your billing period"
    }


def process_cancellation(reason, customer_tenure_days=90):
    """Process cancellation with retention offers."""

    reason_info = CANCELLATION_REASONS.get(reason, CANCELLATION_REASONS["other"])

    offers = []
    for offer_key in reason_info["offers"]:
        offer = RETENTION_OFFERS.get(offer_key, {})
        if offer:
            offers.append({
                "key": offer_key,
                "name": offer["name"],
                "type": offer["type"],
                "success_rate": f"{offer['success_rate'] * 100:.0f}%"
            })

    # Sort by success rate
    offers.sort(key=lambda x: float(x["success_rate"].rstrip("%")), reverse=True)

    return {
        "action": "cancel",
        "reason": reason_info["label"],
        "agent_response": reason_info["response"],
        "retention_offers": offers,
        "if_declined": {
            "effective": "end of billing period",
            "access_until": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"),
            "data_retention": "30 days after cancellation"
        }
    }


def process_pause(duration_months, current_plan):
    """Process subscription pause."""

    plan_info = PLANS.get(current_plan, {})

    resume_date = datetime.now() + timedelta(days=duration_months * 30)

    return {
        "action": "pause",
        "duration": f"{duration_months} month(s)",
        "pause_starts": datetime.now().strftime("%Y-%m-%d"),
        "auto_resume": resume_date.strftime("%Y-%m-%d"),
        "billing_impact": f"No charges for {duration_months} month(s)",
        "access_during_pause": "Suspended (data preserved)",
        "plan_on_resume": plan_info.get("name", current_plan),
        "message": f"Your subscription will be paused until {resume_date.strftime('%B %d, %Y')}"
    }


def get_retention_offers(reason=None):
    """Get all retention offers or filtered by reason."""

    if reason:
        reason_info = CANCELLATION_REASONS.get(reason, {})
        offer_keys = reason_info.get("offers", [])
        offers = {k: RETENTION_OFFERS[k] for k in offer_keys if k in RETENTION_OFFERS}
    else:
        offers = RETENTION_OFFERS

    return offers


def list_plans():
    """List all available plans."""
    return PLANS


def format_output(data, format_type="text"):
    """Format output for display."""

    if format_type == "json":
        return json.dumps(data, indent=2)

    lines = []
    lines.append("\n" + "=" * 50)

    if "action" in data:
        lines.append(f"SUBSCRIPTION {data['action'].upper()}")
        lines.append("=" * 50)

        if data["action"] == "upgrade":
            lines.append(f"\n📈 Upgrading: {data['from']} → {data['to']}")
            lines.append(f"💰 New price: {data['new_price']}")
            lines.append(f"⏱️  Effective: {data['effective']}")

            if data.get("proration"):
                lines.append(f"\nProration:")
                lines.append(f"  Credit: ${data['proration']['credit']}")
                lines.append(f"  Charge: ${data['proration']['charge']}")
                lines.append(f"  Net today: ${data['proration']['net_charge']}")

            if data.get("new_features"):
                lines.append(f"\nNew features:")
                for f in data["new_features"]:
                    lines.append(f"  ✓ {f}")

        elif data["action"] == "downgrade":
            lines.append(f"\n📉 Downgrading: {data['from']} → {data['to']}")
            lines.append(f"💰 New price: {data['new_price']}")
            lines.append(f"⏱️  Effective: {data['effective']}")

            if data.get("lost_features"):
                lines.append(f"\nFeatures you'll lose:")
                for f in data["lost_features"]:
                    lines.append(f"  ✗ {f}")

        elif data["action"] == "cancel":
            lines.append(f"\n❌ Cancellation Request")
            lines.append(f"Reason: {data['reason']}")
            lines.append(f"\nAgent response: \"{data['agent_response']}\"")

            lines.append(f"\nRetention offers (by success rate):")
            for offer in data["retention_offers"]:
                lines.append(f"  [{offer['success_rate']}] {offer['name']}")

            lines.append(f"\nIf declined:")
            lines.append(f"  Access until: {data['if_declined']['access_until']}")

        elif data["action"] == "pause":
            lines.append(f"\n⏸️  Pausing Subscription")
            lines.append(f"Duration: {data['duration']}")
            lines.append(f"Resumes: {data['auto_resume']}")
            lines.append(f"Billing: {data['billing_impact']}")

    else:
        lines.append("INFORMATION")
        lines.append("=" * 50)
        for key, value in data.items():
            lines.append(f"\n{key}:")
            if isinstance(value, dict):
                for k, v in value.items():
                    lines.append(f"  {k}: {v}")
            elif isinstance(value, list):
                for item in value:
                    lines.append(f"  - {item}")
            else:
                lines.append(f"  {value}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description='Subscription management utility')
    parser.add_argument('--action', '-a',
                        choices=['upgrade', 'downgrade', 'cancel', 'pause', 'resume'],
                        help='Action to perform')
    parser.add_argument('--current-plan', '-c', default='basic',
                        choices=list(PLANS.keys()),
                        help='Current plan')
    parser.add_argument('--plan', '-p',
                        choices=list(PLANS.keys()),
                        help='Target plan (for upgrade/downgrade)')
    parser.add_argument('--reason', '-r',
                        choices=list(CANCELLATION_REASONS.keys()),
                        help='Cancellation reason')
    parser.add_argument('--duration', '-d', type=int, default=1,
                        help='Pause duration in months')
    parser.add_argument('--days-remaining', type=int, default=15,
                        help='Days remaining in current period')
    parser.add_argument('--list-plans', '-l', action='store_true',
                        help='List available plans')
    parser.add_argument('--retention-offers', action='store_true',
                        help='Show retention offers')
    parser.add_argument('--format', '-f', choices=['json', 'text'],
                        default='text', help='Output format')

    args = parser.parse_args()

    if args.list_plans:
        plans = list_plans()
        print(format_output(plans, args.format))
        return

    if args.retention_offers:
        offers = get_retention_offers(args.reason)
        if args.format == "json":
            print(json.dumps(offers, indent=2))
        else:
            print("\nRetention Offers:")
            for key, offer in offers.items():
                print(f"\n  {key}:")
                print(f"    Name: {offer['name']}")
                print(f"    Success rate: {offer['success_rate'] * 100:.0f}%")
        return

    if args.action == "upgrade":
        if not args.plan:
            print("Error: --plan required for upgrade")
            return
        result = process_upgrade(args.current_plan, args.plan, args.days_remaining)

    elif args.action == "downgrade":
        if not args.plan:
            print("Error: --plan required for downgrade")
            return
        result = process_downgrade(args.current_plan, args.plan)

    elif args.action == "cancel":
        reason = args.reason or "other"
        result = process_cancellation(reason)

    elif args.action == "pause":
        result = process_pause(args.duration, args.current_plan)

    else:
        parser.print_help()
        return

    print(format_output(result, args.format))


if __name__ == '__main__':
    main()
