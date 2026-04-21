#!/usr/bin/env python3
"""Configure and simulate SLA breach notifications.

Usage:
    python scripts/alert_sla_breach.py --ticket 12345 --metric response_time
    python scripts/alert_sla_breach.py --ticket 12345 --metric resolution_time --priority P1
    python scripts/alert_sla_breach.py --list-active --tier enterprise
"""

import argparse
import json
import random
import sys
from datetime import datetime, timedelta

random.seed(42)

ESCALATION_CHAINS = {
    "P1": [
        {"level": 1, "role": "Team Lead", "name": "Sarah Chen", "method": "Slack + PagerDuty", "timeout_minutes": 15},
        {"level": 2, "role": "Manager", "name": "James Park", "method": "Phone + Email", "timeout_minutes": 30},
        {"level": 3, "role": "Director", "name": "Lisa Wong", "method": "Phone", "timeout_minutes": 60},
    ],
    "P2": [
        {"level": 1, "role": "Team Lead", "name": "Sarah Chen", "method": "Slack + Email", "timeout_minutes": 30},
        {"level": 2, "role": "Manager", "name": "James Park", "method": "Email + Slack", "timeout_minutes": 120},
    ],
    "P3": [
        {"level": 1, "role": "Team Lead", "name": "Sarah Chen", "method": "Email", "timeout_minutes": 120},
    ],
    "P4": [
        {"level": 1, "role": "Team Lead", "name": "Sarah Chen", "method": "Email", "timeout_minutes": 240},
    ],
}

METRIC_LABELS = {
    "response_time": "First Response Time",
    "resolution_time": "Resolution Time",
    "uptime": "System Uptime",
    "fcr": "First Contact Resolution",
}

SAMPLE_ACTIVE_BREACHES = [
    {
        "ticket_id": "TK-10234",
        "customer": "Acme Corp",
        "tier": "enterprise",
        "priority": "P1",
        "metric": "response_time",
        "target": "15 minutes",
        "actual": "47 minutes",
        "overage": "32 minutes",
        "agent": "Bob Kim",
        "status": "acknowledged",
    },
    {
        "ticket_id": "TK-10298",
        "customer": "GlobalTech Inc",
        "tier": "premium",
        "priority": "P2",
        "metric": "resolution_time",
        "target": "8 hours",
        "actual": "10.5 hours",
        "overage": "2.5 hours",
        "agent": "Carol Martinez",
        "status": "unacknowledged",
    },
    {
        "ticket_id": "TK-10315",
        "customer": "StartupXYZ",
        "tier": "standard",
        "priority": "P3",
        "metric": "response_time",
        "target": "4 hours",
        "actual": "5.2 hours",
        "overage": "1.2 hours",
        "agent": None,
        "status": "unacknowledged",
    },
]


def generate_breach_notification(ticket_id, metric, priority):
    """Generate a breach notification payload."""
    now = datetime.utcnow()
    tier = random.choice(["enterprise", "premium", "standard"])
    target_map = {
        "response_time": {"enterprise": "15 min", "premium": "1 hour", "standard": "4 hours"},
        "resolution_time": {"enterprise": "4 hours", "premium": "8 hours", "standard": "24 hours"},
    }

    target = target_map.get(metric, {}).get(tier, "4 hours")
    overage_minutes = random.randint(10, 180)

    notification = {
        "notification_id": f"BREACH-{now.strftime('%Y%m%d%H%M%S')}-{ticket_id}",
        "timestamp": now.isoformat() + "Z",
        "severity": "critical" if priority in ["P1", "P2"] else "warning",
        "breach_details": {
            "ticket_id": f"TK-{ticket_id}",
            "customer": f"Customer-{random.randint(100, 999)}",
            "tier": tier,
            "priority": priority,
            "metric_breached": METRIC_LABELS.get(metric, metric),
            "target": target,
            "actual_elapsed": f"{overage_minutes + random.randint(10, 60)} minutes",
            "overage": f"{overage_minutes} minutes",
        },
        "ticket_context": {
            "subject": f"Sample issue for ticket {ticket_id}",
            "status": "open",
            "assigned_agent": random.choice(["Alice Chen", "Bob Kim", "Carol Martinez", None]),
            "last_update": (now - timedelta(minutes=random.randint(30, 240))).isoformat() + "Z",
            "customer_waiting_since": (now - timedelta(minutes=overage_minutes + random.randint(10, 60))).isoformat() + "Z",
        },
        "required_actions": [
            {"action": "Acknowledge this breach", "deadline_minutes": 15},
            {"action": "Contact customer with status update", "deadline_minutes": 30},
            {"action": "Provide estimated resolution time", "deadline_minutes": 30},
            {"action": "Complete root cause field", "deadline_minutes": 60},
            {"action": "Submit breach report", "deadline_hours": 24},
        ],
        "escalation_chain": ESCALATION_CHAINS.get(priority, ESCALATION_CHAINS["P3"]),
        "notification_channels": {
            "email": True,
            "slack": priority in ["P1", "P2"],
            "pagerduty": priority == "P1",
            "sms": priority == "P1",
        },
    }

    return notification


def list_active_breaches(tier_filter=None):
    """List currently active breaches."""
    breaches = SAMPLE_ACTIVE_BREACHES
    if tier_filter and tier_filter != "all":
        breaches = [b for b in breaches if b["tier"] == tier_filter]

    return {
        "active_breaches": breaches,
        "total_count": len(breaches),
        "unacknowledged_count": sum(1 for b in breaches if b["status"] == "unacknowledged"),
        "checked_at": datetime.utcnow().isoformat() + "Z",
    }


def main():
    parser = argparse.ArgumentParser(
        description="Configure and send SLA breach notifications"
    )
    parser.add_argument(
        "--ticket",
        help="Ticket ID to generate breach notification for",
    )
    parser.add_argument(
        "--metric",
        choices=["response_time", "resolution_time", "uptime", "fcr"],
        help="SLA metric that was breached",
    )
    parser.add_argument(
        "--priority",
        choices=["P1", "P2", "P3", "P4"],
        default="P3",
        help="Ticket priority (default: P3)",
    )
    parser.add_argument(
        "--list-active",
        action="store_true",
        help="List all currently active breaches",
    )
    parser.add_argument(
        "--tier",
        choices=["enterprise", "premium", "standard", "basic", "all"],
        default="all",
        help="Filter by tier (used with --list-active)",
    )

    args = parser.parse_args()

    if args.list_active:
        result = list_active_breaches(args.tier)
        print(json.dumps(result, indent=2))
    elif args.ticket and args.metric:
        notification = generate_breach_notification(args.ticket, args.metric, args.priority)
        print(json.dumps(notification, indent=2))
    else:
        parser.error("Either --list-active or both --ticket and --metric are required")


if __name__ == "__main__":
    main()
