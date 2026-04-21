#!/usr/bin/env python3
"""Analyze deal velocity and stage conversion rates.

Calculates the sales velocity equation components, identifies bottleneck stages,
and tracks trends over time.

Usage:
    python velocity_analysis.py --period last-6-months --segment enterprise
    python velocity_analysis.py --period last-12-months --format markdown
"""

import argparse
import json
from datetime import datetime, timedelta


# Sample closed deal data for velocity analysis
SAMPLE_CLOSED_DEALS = [
    {"id": "D-001", "amount": 85000, "stage_history": {"Prospecting": 8, "Qualification": 12, "Discovery": 18, "Proposal": 14, "Negotiation": 10}, "segment": "Enterprise", "outcome": "won", "close_date": "2024-12-15", "rep": "Sarah Chen"},
    {"id": "D-002", "amount": 120000, "stage_history": {"Prospecting": 5, "Qualification": 15, "Discovery": 25, "Proposal": 20, "Negotiation": 15}, "segment": "Enterprise", "outcome": "lost", "close_date": "2024-11-30", "rep": "Mike Johnson"},
    {"id": "D-003", "amount": 45000, "stage_history": {"Prospecting": 6, "Qualification": 8, "Discovery": 12, "Proposal": 10, "Negotiation": 7}, "segment": "Mid-Market", "outcome": "won", "close_date": "2024-12-01", "rep": "Sarah Chen"},
    {"id": "D-004", "amount": 200000, "stage_history": {"Prospecting": 10, "Qualification": 20, "Discovery": 30, "Proposal": 25, "Negotiation": 20}, "segment": "Enterprise", "outcome": "lost", "close_date": "2024-10-20", "rep": "James Park"},
    {"id": "D-005", "amount": 18000, "stage_history": {"Prospecting": 3, "Qualification": 5, "Discovery": 8, "Proposal": 5, "Negotiation": 4}, "segment": "SMB", "outcome": "won", "close_date": "2024-12-10", "rep": "Lisa Wong"},
    {"id": "D-006", "amount": 150000, "stage_history": {"Prospecting": 7, "Qualification": 14, "Discovery": 20, "Proposal": 18, "Negotiation": 12}, "segment": "Enterprise", "outcome": "won", "close_date": "2024-11-15", "rep": "Sarah Chen"},
    {"id": "D-007", "amount": 35000, "stage_history": {"Prospecting": 4, "Qualification": 7, "Discovery": 10, "Proposal": 8, "Negotiation": 6}, "segment": "Mid-Market", "outcome": "won", "close_date": "2024-12-05", "rep": "Mike Johnson"},
    {"id": "D-008", "amount": 95000, "stage_history": {"Prospecting": 9, "Qualification": 16, "Discovery": 22, "Proposal": 16, "Negotiation": 14}, "segment": "Enterprise", "outcome": "won", "close_date": "2024-11-28", "rep": "James Park"},
    {"id": "D-009", "amount": 22000, "stage_history": {"Prospecting": 3, "Qualification": 4, "Discovery": 6, "Proposal": 5, "Negotiation": 3}, "segment": "SMB", "outcome": "won", "close_date": "2024-12-20", "rep": "Lisa Wong"},
    {"id": "D-010", "amount": 65000, "stage_history": {"Prospecting": 6, "Qualification": 10, "Discovery": 15, "Proposal": 12, "Negotiation": 8}, "segment": "Mid-Market", "outcome": "lost", "close_date": "2024-11-10", "rep": "Mike Johnson"},
    {"id": "D-011", "amount": 175000, "stage_history": {"Prospecting": 8, "Qualification": 18, "Discovery": 28, "Proposal": 22, "Negotiation": 18}, "segment": "Enterprise", "outcome": "lost", "close_date": "2024-10-30", "rep": "Mike Johnson"},
    {"id": "D-012", "amount": 28000, "stage_history": {"Prospecting": 4, "Qualification": 6, "Discovery": 9, "Proposal": 7, "Negotiation": 5}, "segment": "SMB", "outcome": "won", "close_date": "2024-12-08", "rep": "Sarah Chen"},
    {"id": "D-013", "amount": 250000, "stage_history": {"Prospecting": 12, "Qualification": 22, "Discovery": 35, "Proposal": 28, "Negotiation": 25}, "segment": "Enterprise", "outcome": "won", "close_date": "2024-09-30", "rep": "James Park"},
    {"id": "D-014", "amount": 12000, "stage_history": {"Prospecting": 2, "Qualification": 3, "Discovery": 5, "Proposal": 4, "Negotiation": 3}, "segment": "SMB", "outcome": "won", "close_date": "2024-12-18", "rep": "Lisa Wong"},
    {"id": "D-015", "amount": 55000, "stage_history": {"Prospecting": 5, "Qualification": 9, "Discovery": 13, "Proposal": 10, "Negotiation": 7}, "segment": "Mid-Market", "outcome": "won", "close_date": "2024-11-25", "rep": "Lisa Wong"},
]

STAGES = ["Prospecting", "Qualification", "Discovery", "Proposal", "Negotiation"]
STAGE_DURATION_BENCHMARKS = {
    "Prospecting": 7,
    "Qualification": 10,
    "Discovery": 15,
    "Proposal": 12,
    "Negotiation": 10,
}


def filter_deals(deals, period, segment=None):
    """Filter deals by period and segment."""
    now = datetime.now()
    period_days = {"last-3-months": 90, "last-6-months": 180, "last-12-months": 365}
    cutoff = now - timedelta(days=period_days.get(period, 180))

    filtered = []
    for deal in deals:
        close_date = datetime.strptime(deal["close_date"], "%Y-%m-%d")
        if close_date < cutoff:
            continue
        if segment and deal["segment"].lower() != segment.lower():
            continue
        filtered.append(deal)
    return filtered


def calculate_velocity(deals):
    """Calculate sales velocity and component metrics."""
    won_deals = [d for d in deals if d["outcome"] == "won"]
    lost_deals = [d for d in deals if d["outcome"] == "lost"]

    total_deals = len(deals)
    num_won = len(won_deals)
    num_lost = len(lost_deals)
    win_rate = round(num_won / total_deals * 100, 1) if total_deals > 0 else 0

    # Average deal value (won)
    avg_deal_value = round(sum(d["amount"] for d in won_deals) / num_won) if num_won > 0 else 0

    # Average sales cycle
    def cycle_length(deal):
        return sum(deal["stage_history"].values())

    won_cycles = [cycle_length(d) for d in won_deals]
    lost_cycles = [cycle_length(d) for d in lost_deals]
    avg_won_cycle = round(sum(won_cycles) / len(won_cycles)) if won_cycles else 0
    avg_lost_cycle = round(sum(lost_cycles) / len(lost_cycles)) if lost_cycles else 0

    # Velocity = (# Opportunities x Win Rate x ACV) / Sales Cycle Length
    velocity = round((total_deals * (win_rate / 100) * avg_deal_value) / avg_won_cycle) if avg_won_cycle > 0 else 0

    # Stage analysis
    stage_analysis = {}
    for stage in STAGES:
        won_durations = [d["stage_history"].get(stage, 0) for d in won_deals]
        all_durations = [d["stage_history"].get(stage, 0) for d in deals]
        avg_duration = round(sum(all_durations) / len(all_durations)) if all_durations else 0
        benchmark = STAGE_DURATION_BENCHMARKS.get(stage, 10)

        # Conversion rate: estimate based on deals that progressed past this stage
        stage_idx = STAGES.index(stage)
        entered = len(deals)  # Simplified: all deals enter all stages
        progressed = len([d for d in deals if stage_idx < len(STAGES) - 1 or d["outcome"] == "won"])

        stage_analysis[stage] = {
            "avg_duration_days": avg_duration,
            "benchmark_days": benchmark,
            "is_bottleneck": avg_duration > benchmark * 1.5,
            "deals_in_stage": entered,
        }

    # Stage conversion rates
    conversions = {}
    stage_pairs = list(zip(STAGES[:-1], STAGES[1:]))
    for i, (from_stage, to_stage) in enumerate(stage_pairs):
        # All deals passed through all stages in sample data
        conv_rate = round((total_deals - i * (num_lost / len(stage_pairs))) / total_deals * 100, 1)
        conversions[f"{from_stage} -> {to_stage}"] = {
            "conversion_rate": min(conv_rate, 100),
            "avg_duration": stage_analysis[from_stage]["avg_duration_days"],
        }
    # Final conversion to close
    conversions[f"Negotiation -> Closed Won"] = {
        "conversion_rate": win_rate,
        "avg_duration": stage_analysis["Negotiation"]["avg_duration_days"],
    }

    # Identify bottlenecks
    bottlenecks = [
        {"stage": stage, "avg_days": data["avg_duration_days"], "benchmark": data["benchmark_days"],
         "excess_days": data["avg_duration_days"] - data["benchmark_days"]}
        for stage, data in stage_analysis.items()
        if data["is_bottleneck"]
    ]

    return {
        "velocity": {
            "daily_velocity": velocity,
            "monthly_velocity": velocity * 30,
            "formula": "(# Opportunities x Win Rate x ACV) / Sales Cycle",
            "components": {
                "opportunities": total_deals,
                "win_rate_pct": win_rate,
                "average_deal_value": avg_deal_value,
                "avg_sales_cycle_days": avg_won_cycle,
            },
        },
        "deal_summary": {
            "total_deals": total_deals,
            "won": num_won,
            "lost": num_lost,
            "win_rate": win_rate,
            "total_revenue_won": sum(d["amount"] for d in won_deals),
            "avg_won_cycle_days": avg_won_cycle,
            "avg_lost_cycle_days": avg_lost_cycle,
        },
        "stage_analysis": stage_analysis,
        "stage_conversions": conversions,
        "bottlenecks": bottlenecks,
    }


def format_markdown(analysis):
    """Format velocity analysis as markdown."""
    lines = []
    v = analysis["velocity"]
    lines.append("# Deal Velocity Report")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("")

    lines.append("## Velocity")
    lines.append(f"**Daily Velocity:** ${v['daily_velocity']:,}/day")
    lines.append(f"**Monthly Velocity:** ${v['monthly_velocity']:,}/month")
    lines.append(f"Formula: {v['formula']}")
    lines.append("")

    c = v["components"]
    lines.append("## Velocity Components")
    lines.append("| Component | Value |")
    lines.append("|-----------|-------|")
    lines.append(f"| Opportunities | {c['opportunities']} |")
    lines.append(f"| Win Rate | {c['win_rate_pct']}% |")
    lines.append(f"| Average Deal Value | ${c['average_deal_value']:,} |")
    lines.append(f"| Avg Sales Cycle | {c['avg_sales_cycle_days']} days |")
    lines.append("")

    lines.append("## Stage Duration & Bottlenecks")
    lines.append("| Stage | Avg Duration | Benchmark | Bottleneck? |")
    lines.append("|-------|-------------|-----------|-------------|")
    for stage in STAGES:
        d = analysis["stage_analysis"][stage]
        bottleneck = "YES" if d["is_bottleneck"] else "No"
        lines.append(f"| {stage} | {d['avg_duration_days']}d | {d['benchmark_days']}d | {bottleneck} |")
    lines.append("")

    lines.append("## Stage Conversions")
    lines.append("| Transition | Conversion Rate | Avg Duration |")
    lines.append("|-----------|----------------|-------------|")
    for transition, data in analysis["stage_conversions"].items():
        lines.append(f"| {transition} | {data['conversion_rate']}% | {data['avg_duration']}d |")
    lines.append("")

    if analysis["bottlenecks"]:
        lines.append("## Bottleneck Alert")
        for b in analysis["bottlenecks"]:
            lines.append(f"- **{b['stage']}**: {b['avg_days']}d avg vs. {b['benchmark']}d benchmark (+{b['excess_days']}d)")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Analyze deal velocity and stage conversion rates.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python velocity_analysis.py --period last-6-months --segment enterprise
  python velocity_analysis.py --period last-12-months --format markdown
        """,
    )
    parser.add_argument(
        "--period",
        type=str,
        choices=["last-3-months", "last-6-months", "last-12-months"],
        default="last-6-months",
        help="Analysis period (default: last-6-months)",
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
        choices=["json", "markdown"],
        default="json",
        help="Output format (default: json)",
    )

    args = parser.parse_args()

    deals = filter_deals(SAMPLE_CLOSED_DEALS, args.period, args.segment)

    if not deals:
        print(json.dumps({"status": "no_data", "message": "No deals found for the specified filters"}, indent=2))
        return

    analysis = calculate_velocity(deals)
    analysis["metadata"] = {
        "period": args.period,
        "segment_filter": args.segment,
        "generated": datetime.now().isoformat(),
        "deals_analyzed": len(deals),
    }

    if args.format == "json":
        print(json.dumps(analysis, indent=2))
    else:
        print(format_markdown(analysis))


if __name__ == "__main__":
    main()
