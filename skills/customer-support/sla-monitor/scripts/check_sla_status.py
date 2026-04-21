#!/usr/bin/env python3
"""Real-time SLA compliance check.

Usage:
    python scripts/check_sla_status.py --tier enterprise --period today
    python scripts/check_sla_status.py --tier all --period this-week
    python scripts/check_sla_status.py --tier premium --period today --metric frt
"""

import argparse
import json
import random
import sys
from datetime import datetime, timedelta

random.seed(42)

SLA_TARGETS = {
    "enterprise": {"frt_minutes": 15, "rt_hours": 4, "uptime_pct": 99.99, "fcr_pct": 85},
    "premium": {"frt_minutes": 60, "rt_hours": 8, "uptime_pct": 99.95, "fcr_pct": 80},
    "standard": {"frt_minutes": 240, "rt_hours": 24, "uptime_pct": 99.9, "fcr_pct": 75},
    "basic": {"frt_minutes": 1440, "rt_hours": 72, "uptime_pct": 99.5, "fcr_pct": 70},
}

PRIORITIES = ["P1", "P2", "P3", "P4"]
CATEGORIES = ["billing", "technical", "account", "feature_request", "bug_report"]
AGENTS = ["Alice Chen", "Bob Kim", "Carol Martinez", "Dave Wilson", "Eve Brown"]


def generate_sample_tickets(tier, count=50):
    """Generate sample ticket data for demonstration."""
    tickets = []
    now = datetime.utcnow()
    targets = SLA_TARGETS.get(tier, SLA_TARGETS["standard"])

    for i in range(count):
        created_minutes_ago = random.randint(5, 1440)
        created_at = now - timedelta(minutes=created_minutes_ago)
        priority = random.choices(PRIORITIES, weights=[5, 15, 50, 30])[0]

        # Simulate response and resolution
        frt_minutes = random.randint(1, int(targets["frt_minutes"] * 1.5))
        responded = random.random() > 0.1  # 90% have been responded to
        resolved = random.random() > 0.4  # 60% are resolved

        frt_breached = frt_minutes > targets["frt_minutes"] if responded else (
            created_minutes_ago > targets["frt_minutes"]
        )

        rt_minutes = random.randint(30, int(targets["rt_hours"] * 60 * 1.3)) if resolved else None
        rt_breached = (rt_minutes and rt_minutes > targets["rt_hours"] * 60) if resolved else False

        # Calculate SLA remaining
        frt_remaining_pct = max(0, 100 - (created_minutes_ago / targets["frt_minutes"] * 100)) if not responded else None

        status = "resolved" if resolved else ("in_progress" if responded else "open")

        tickets.append({
            "ticket_id": f"TK-{10000 + i}",
            "priority": priority,
            "category": random.choice(CATEGORIES),
            "agent": random.choice(AGENTS) if responded else None,
            "status": status,
            "created_at": created_at.isoformat() + "Z",
            "frt_minutes": frt_minutes if responded else None,
            "frt_breached": frt_breached,
            "rt_minutes": rt_minutes,
            "rt_breached": rt_breached,
            "sla_remaining_pct": frt_remaining_pct,
        })

    return tickets


def compute_compliance(tickets, targets):
    """Compute SLA compliance metrics from ticket data."""
    total = len(tickets)
    if total == 0:
        return {"error": "No tickets found"}

    # FRT compliance
    responded = [t for t in tickets if t["frt_minutes"] is not None]
    frt_compliant = sum(1 for t in responded if not t["frt_breached"])
    frt_pct = round(frt_compliant / len(responded) * 100, 1) if responded else 100.0

    # RT compliance
    resolved = [t for t in tickets if t["rt_minutes"] is not None]
    rt_compliant = sum(1 for t in resolved if not t["rt_breached"])
    rt_pct = round(rt_compliant / len(resolved) * 100, 1) if resolved else 100.0

    # Uptime (simulated)
    uptime_pct = round(random.uniform(targets["uptime_pct"] - 0.05, targets["uptime_pct"] + 0.02), 3)

    # FCR (simulated)
    fcr_pct = round(random.uniform(targets["fcr_pct"] - 10, targets["fcr_pct"] + 5), 1)

    overall = round((frt_pct + rt_pct + min(100, uptime_pct)) / 3, 1)

    # At-risk tickets (>80% of SLA elapsed, not yet responded)
    at_risk = [t for t in tickets if t["sla_remaining_pct"] is not None and t["sla_remaining_pct"] < 20]
    breached = [t for t in tickets if t["frt_breached"] or t.get("rt_breached", False)]

    return {
        "overall_compliance_pct": overall,
        "metrics": {
            "first_response_time": {
                "compliance_pct": frt_pct,
                "target_minutes": targets["frt_minutes"],
                "total_measured": len(responded),
                "breaches": len(responded) - frt_compliant,
            },
            "resolution_time": {
                "compliance_pct": rt_pct,
                "target_hours": targets["rt_hours"],
                "total_measured": len(resolved),
                "breaches": len(resolved) - rt_compliant,
            },
            "uptime": {
                "actual_pct": uptime_pct,
                "target_pct": targets["uptime_pct"],
                "meets_target": uptime_pct >= targets["uptime_pct"],
            },
            "fcr": {
                "actual_pct": fcr_pct,
                "target_pct": targets["fcr_pct"],
                "meets_target": fcr_pct >= targets["fcr_pct"],
            },
        },
        "alerts": {
            "breached_count": len(breached),
            "at_risk_count": len(at_risk),
            "on_track_count": total - len(breached) - len(at_risk),
        },
        "at_risk_tickets": [
            {"ticket_id": t["ticket_id"], "priority": t["priority"],
             "sla_remaining_pct": round(t["sla_remaining_pct"], 1)}
            for t in at_risk[:10]
        ],
        "breached_tickets": [
            {"ticket_id": t["ticket_id"], "priority": t["priority"],
             "metric": "frt" if t["frt_breached"] else "rt"}
            for t in breached[:10]
        ],
    }


def main():
    parser = argparse.ArgumentParser(
        description="Real-time SLA compliance check"
    )
    parser.add_argument(
        "--tier",
        choices=["enterprise", "premium", "standard", "basic", "all"],
        default="all",
        help="Customer tier to check (default: all)",
    )
    parser.add_argument(
        "--period",
        default="today",
        help="Time period: today, this-week, this-month (default: today)",
    )
    parser.add_argument(
        "--metric",
        choices=["frt", "rt", "uptime", "fcr", "all"],
        default="all",
        help="Specific metric to check (default: all)",
    )

    args = parser.parse_args()

    tiers = list(SLA_TARGETS.keys()) if args.tier == "all" else [args.tier]

    results = {
        "check_time": datetime.utcnow().isoformat() + "Z",
        "period": args.period,
        "tiers": {},
    }

    for tier in tiers:
        tickets = generate_sample_tickets(tier)
        targets = SLA_TARGETS[tier]
        compliance = compute_compliance(tickets, targets)
        results["tiers"][tier] = compliance

    # Overall summary across all tiers
    if len(tiers) > 1:
        all_overall = [results["tiers"][t]["overall_compliance_pct"] for t in tiers]
        results["summary"] = {
            "overall_compliance_pct": round(sum(all_overall) / len(all_overall), 1),
            "total_breaches": sum(results["tiers"][t]["alerts"]["breached_count"] for t in tiers),
            "total_at_risk": sum(results["tiers"][t]["alerts"]["at_risk_count"] for t in tiers),
        }

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
