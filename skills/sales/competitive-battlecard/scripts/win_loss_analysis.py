#!/usr/bin/env python3
"""Analyze CRM data for win/loss patterns against a specific competitor.

Processes deal data to identify win/loss themes, rates, and deal characteristics
when competing against a specific competitor.

Usage:
    python win_loss_analysis.py --competitor "Acme Corp" --period last-6-months
    python win_loss_analysis.py --competitor "Acme Corp" --period last-12-months --segment enterprise
"""

import argparse
import json
from datetime import datetime, timedelta
import random

# Sample CRM data for demonstration
SAMPLE_DEALS = [
    {
        "id": "OPP-001",
        "account": "TechFlow Inc",
        "amount": 85000,
        "stage": "Closed Won",
        "competitor": "Acme Corp",
        "segment": "Enterprise",
        "source": "Inbound",
        "rep": "Sarah Chen",
        "close_date": "2024-11-15",
        "created_date": "2024-06-20",
        "win_reason": "Superior product capabilities",
        "loss_reason": None,
    },
    {
        "id": "OPP-002",
        "account": "DataVault Systems",
        "amount": 120000,
        "stage": "Closed Lost",
        "competitor": "Acme Corp",
        "segment": "Enterprise",
        "source": "Outbound",
        "rep": "Mike Johnson",
        "close_date": "2024-10-30",
        "created_date": "2024-04-15",
        "win_reason": None,
        "loss_reason": "Price - competitor undercut by 30%",
    },
    {
        "id": "OPP-003",
        "account": "CloudNine SaaS",
        "amount": 45000,
        "stage": "Closed Won",
        "competitor": "Acme Corp",
        "segment": "Mid-Market",
        "source": "Referral",
        "rep": "Sarah Chen",
        "close_date": "2024-12-01",
        "created_date": "2024-08-10",
        "win_reason": "Better UX and faster implementation",
        "loss_reason": None,
    },
    {
        "id": "OPP-004",
        "account": "FinServ Global",
        "amount": 200000,
        "stage": "Closed Lost",
        "competitor": "Acme Corp",
        "segment": "Enterprise",
        "source": "Inbound",
        "rep": "James Park",
        "close_date": "2024-09-20",
        "created_date": "2024-02-10",
        "win_reason": None,
        "loss_reason": "Feature gap - compliance module",
    },
    {
        "id": "OPP-005",
        "account": "RetailMax",
        "amount": 35000,
        "stage": "Closed Won",
        "competitor": "Acme Corp",
        "segment": "Mid-Market",
        "source": "Partner",
        "rep": "Mike Johnson",
        "close_date": "2024-11-28",
        "created_date": "2024-07-15",
        "win_reason": "Integration depth with existing tools",
        "loss_reason": None,
    },
    {
        "id": "OPP-006",
        "account": "HealthFirst",
        "amount": 150000,
        "stage": "Closed Won",
        "competitor": "Acme Corp",
        "segment": "Enterprise",
        "source": "Outbound",
        "rep": "Sarah Chen",
        "close_date": "2024-10-15",
        "created_date": "2024-05-01",
        "win_reason": "Superior product capabilities",
        "loss_reason": None,
    },
    {
        "id": "OPP-007",
        "account": "StartupHub",
        "amount": 18000,
        "stage": "Closed Lost",
        "competitor": "Acme Corp",
        "segment": "SMB",
        "source": "Inbound",
        "rep": "James Park",
        "close_date": "2024-12-10",
        "created_date": "2024-10-01",
        "win_reason": None,
        "loss_reason": "Price - budget constraints",
    },
    {
        "id": "OPP-008",
        "account": "LogiTech Solutions",
        "amount": 65000,
        "stage": "No Decision",
        "competitor": "Acme Corp",
        "segment": "Mid-Market",
        "source": "Inbound",
        "rep": "Mike Johnson",
        "close_date": "2024-11-01",
        "created_date": "2024-06-01",
        "win_reason": None,
        "loss_reason": "Budget frozen - project deprioritized",
    },
    {
        "id": "OPP-009",
        "account": "EduPlatform",
        "amount": 28000,
        "stage": "Closed Won",
        "competitor": "BetaTools",
        "segment": "SMB",
        "source": "Inbound",
        "rep": "Sarah Chen",
        "close_date": "2024-11-20",
        "created_date": "2024-09-05",
        "win_reason": "More robust feature set",
        "loss_reason": None,
    },
    {
        "id": "OPP-010",
        "account": "ManufacturePro",
        "amount": 95000,
        "stage": "Closed Won",
        "competitor": "Acme Corp",
        "segment": "Enterprise",
        "source": "Referral",
        "rep": "James Park",
        "close_date": "2024-12-05",
        "created_date": "2024-07-20",
        "win_reason": "Better customer support and faster time-to-value",
        "loss_reason": None,
    },
]


def filter_deals(deals, competitor, period, segment=None):
    """Filter deals by competitor, period, and optionally segment."""
    now = datetime.now()
    if period == "last-6-months":
        cutoff = now - timedelta(days=180)
    elif period == "last-12-months":
        cutoff = now - timedelta(days=365)
    elif period == "last-3-months":
        cutoff = now - timedelta(days=90)
    else:
        cutoff = now - timedelta(days=180)

    filtered = []
    for deal in deals:
        if deal["competitor"].lower() != competitor.lower():
            continue
        close_date = datetime.strptime(deal["close_date"], "%Y-%m-%d")
        if close_date < cutoff:
            continue
        if segment and deal["segment"].lower() != segment.lower():
            continue
        filtered.append(deal)

    return filtered


def calculate_cycle_length(deal):
    """Calculate sales cycle length in days."""
    created = datetime.strptime(deal["created_date"], "%Y-%m-%d")
    closed = datetime.strptime(deal["close_date"], "%Y-%m-%d")
    return (closed - created).days


def analyze_win_loss(deals):
    """Perform win/loss analysis on filtered deals."""
    wins = [d for d in deals if d["stage"] == "Closed Won"]
    losses = [d for d in deals if d["stage"] == "Closed Lost"]
    no_decision = [d for d in deals if d["stage"] == "No Decision"]

    total = len(deals)
    win_count = len(wins)
    loss_count = len(losses)
    nd_count = len(no_decision)

    # Win rate (excluding no-decision)
    decided = win_count + loss_count
    win_rate = round((win_count / decided * 100), 1) if decided > 0 else 0

    # Deal characteristics
    win_amounts = [d["amount"] for d in wins]
    loss_amounts = [d["amount"] for d in losses]
    win_cycles = [calculate_cycle_length(d) for d in wins]
    loss_cycles = [calculate_cycle_length(d) for d in losses]

    avg_win_size = round(sum(win_amounts) / len(win_amounts)) if win_amounts else 0
    avg_loss_size = round(sum(loss_amounts) / len(loss_amounts)) if loss_amounts else 0
    avg_win_cycle = round(sum(win_cycles) / len(win_cycles)) if win_cycles else 0
    avg_loss_cycle = round(sum(loss_cycles) / len(loss_cycles)) if loss_cycles else 0

    # Win themes
    win_reasons = {}
    for deal in wins:
        reason = deal.get("win_reason", "Unknown")
        if reason:
            win_reasons[reason] = win_reasons.get(reason, 0) + 1

    # Loss themes
    loss_reasons = {}
    for deal in losses:
        reason = deal.get("loss_reason", "Unknown")
        if reason:
            loss_reasons[reason] = loss_reasons.get(reason, 0) + 1

    # By segment
    segments = {}
    for deal in deals:
        seg = deal["segment"]
        if seg not in segments:
            segments[seg] = {"wins": 0, "losses": 0, "no_decision": 0, "total_value": 0}
        if deal["stage"] == "Closed Won":
            segments[seg]["wins"] += 1
        elif deal["stage"] == "Closed Lost":
            segments[seg]["losses"] += 1
        else:
            segments[seg]["no_decision"] += 1
        segments[seg]["total_value"] += deal["amount"]

    for seg, data in segments.items():
        decided_seg = data["wins"] + data["losses"]
        data["win_rate"] = round((data["wins"] / decided_seg * 100), 1) if decided_seg > 0 else 0

    # By rep
    reps = {}
    for deal in deals:
        rep = deal["rep"]
        if rep not in reps:
            reps[rep] = {"wins": 0, "losses": 0, "revenue_won": 0}
        if deal["stage"] == "Closed Won":
            reps[rep]["wins"] += 1
            reps[rep]["revenue_won"] += deal["amount"]
        elif deal["stage"] == "Closed Lost":
            reps[rep]["losses"] += 1

    for rep, data in reps.items():
        decided_rep = data["wins"] + data["losses"]
        data["win_rate"] = round((data["wins"] / decided_rep * 100), 1) if decided_rep > 0 else 0

    # By source
    sources = {}
    for deal in deals:
        source = deal["source"]
        if source not in sources:
            sources[source] = {"wins": 0, "losses": 0, "revenue_won": 0}
        if deal["stage"] == "Closed Won":
            sources[source]["wins"] += 1
            sources[source]["revenue_won"] += deal["amount"]
        elif deal["stage"] == "Closed Lost":
            sources[source]["losses"] += 1

    for source, data in sources.items():
        decided_src = data["wins"] + data["losses"]
        data["win_rate"] = round((data["wins"] / decided_src * 100), 1) if decided_src > 0 else 0

    return {
        "summary": {
            "total_opportunities": total,
            "wins": win_count,
            "losses": loss_count,
            "no_decision": nd_count,
            "win_rate_pct": win_rate,
            "total_revenue_won": sum(win_amounts),
            "total_revenue_lost": sum(loss_amounts),
        },
        "deal_characteristics": {
            "avg_win_size": avg_win_size,
            "avg_loss_size": avg_loss_size,
            "avg_win_cycle_days": avg_win_cycle,
            "avg_loss_cycle_days": avg_loss_cycle,
        },
        "win_themes": [
            {"theme": reason, "count": count}
            for reason, count in sorted(win_reasons.items(), key=lambda x: -x[1])
        ],
        "loss_themes": [
            {"theme": reason, "count": count}
            for reason, count in sorted(loss_reasons.items(), key=lambda x: -x[1])
        ],
        "by_segment": segments,
        "by_rep": reps,
        "by_source": sources,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Analyze CRM data for win/loss patterns against a specific competitor.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python win_loss_analysis.py --competitor "Acme Corp" --period last-6-months
  python win_loss_analysis.py --competitor "Acme Corp" --period last-12-months --segment enterprise
  python win_loss_analysis.py --competitor "Acme Corp" --period last-6-months --format json
        """,
    )
    parser.add_argument(
        "--competitor",
        type=str,
        required=True,
        help="Competitor name to analyze",
    )
    parser.add_argument(
        "--period",
        type=str,
        choices=["last-3-months", "last-6-months", "last-12-months"],
        default="last-6-months",
        help="Time period to analyze (default: last-6-months)",
    )
    parser.add_argument(
        "--segment",
        type=str,
        choices=["enterprise", "mid-market", "smb"],
        help="Filter by segment (optional)",
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["json", "summary"],
        default="json",
        help="Output format (default: json)",
    )

    args = parser.parse_args()

    deals = filter_deals(SAMPLE_DEALS, args.competitor, args.period, args.segment)

    if not deals:
        result = {
            "status": "no_data",
            "message": f"No competitive deals found for '{args.competitor}' in {args.period}",
            "competitor": args.competitor,
            "period": args.period,
        }
        print(json.dumps(result, indent=2))
        return

    analysis = analyze_win_loss(deals)
    analysis["metadata"] = {
        "competitor": args.competitor,
        "period": args.period,
        "segment_filter": args.segment,
        "generated": datetime.now().isoformat(),
        "deal_count": len(deals),
    }

    if args.format == "json":
        print(json.dumps(analysis, indent=2))
    else:
        # Summary format
        s = analysis["summary"]
        print(f"Win/Loss Analysis: vs. {args.competitor}")
        print(f"Period: {args.period}")
        print(f"{'=' * 50}")
        print(f"Total Opportunities: {s['total_opportunities']}")
        print(f"Wins: {s['wins']} | Losses: {s['losses']} | No Decision: {s['no_decision']}")
        print(f"Win Rate: {s['win_rate_pct']}%")
        print(f"Revenue Won: ${s['total_revenue_won']:,}")
        print(f"Revenue Lost: ${s['total_revenue_lost']:,}")
        print()
        dc = analysis["deal_characteristics"]
        print(f"Avg Win Size: ${dc['avg_win_size']:,} | Avg Loss Size: ${dc['avg_loss_size']:,}")
        print(f"Avg Win Cycle: {dc['avg_win_cycle_days']}d | Avg Loss Cycle: {dc['avg_loss_cycle_days']}d")
        print()
        print("Win Themes:")
        for theme in analysis["win_themes"]:
            print(f"  - {theme['theme']} ({theme['count']} deals)")
        print()
        print("Loss Themes:")
        for theme in analysis["loss_themes"]:
            print(f"  - {theme['theme']} ({theme['count']} deals)")


if __name__ == "__main__":
    main()
