#!/usr/bin/env python3
"""Generate a pipeline report from CRM opportunity data.

Produces a structured pipeline report with stage distribution, rep breakdown,
at-risk deals, and pipeline health indicators.

Usage:
    python generate_pipeline_report.py --period this-quarter --format markdown
    python generate_pipeline_report.py --period this-month --format json
    python generate_pipeline_report.py --period this-quarter --segment enterprise
"""

import argparse
import json
from datetime import datetime, timedelta
import random

# Sample opportunity data
SAMPLE_OPPORTUNITIES = [
    {"id": "OPP-001", "deal": "TechFlow Platform Deal", "account": "TechFlow Inc", "amount": 85000, "stage": "Negotiation", "probability": 80, "rep": "Sarah Chen", "segment": "Enterprise", "product": "Platform", "created": "2024-06-20", "close_date": "2025-01-15", "last_activity": "2024-12-28", "days_in_stage": 14},
    {"id": "OPP-002", "deal": "DataVault Migration", "account": "DataVault Systems", "amount": 120000, "stage": "Proposal", "probability": 60, "rep": "Mike Johnson", "segment": "Enterprise", "product": "Platform", "created": "2024-08-15", "close_date": "2025-02-01", "last_activity": "2024-12-20", "days_in_stage": 21},
    {"id": "OPP-003", "deal": "CloudNine Expansion", "account": "CloudNine SaaS", "amount": 45000, "stage": "Discovery", "probability": 30, "rep": "Sarah Chen", "segment": "Mid-Market", "product": "Analytics", "created": "2024-10-10", "close_date": "2025-03-01", "last_activity": "2024-12-30", "days_in_stage": 8},
    {"id": "OPP-004", "deal": "FinServ Analytics Suite", "account": "FinServ Global", "amount": 200000, "stage": "Qualification", "probability": 20, "rep": "James Park", "segment": "Enterprise", "product": "Analytics", "created": "2024-11-01", "close_date": "2025-04-15", "last_activity": "2024-12-15", "days_in_stage": 35},
    {"id": "OPP-005", "deal": "RetailMax Starter", "account": "RetailMax", "amount": 18000, "stage": "Negotiation", "probability": 85, "rep": "Lisa Wong", "segment": "SMB", "product": "Starter", "created": "2024-09-15", "close_date": "2025-01-10", "last_activity": "2024-12-29", "days_in_stage": 7},
    {"id": "OPP-006", "deal": "HealthFirst Platform", "account": "HealthFirst", "amount": 150000, "stage": "Proposal", "probability": 55, "rep": "Sarah Chen", "segment": "Enterprise", "product": "Platform", "created": "2024-07-01", "close_date": "2025-02-15", "last_activity": "2024-12-10", "days_in_stage": 42},
    {"id": "OPP-007", "deal": "StartupHub Basic", "account": "StartupHub", "amount": 12000, "stage": "Discovery", "probability": 25, "rep": "Lisa Wong", "segment": "SMB", "product": "Starter", "created": "2024-11-20", "close_date": "2025-02-28", "last_activity": "2024-12-27", "days_in_stage": 12},
    {"id": "OPP-008", "deal": "LogiTech Enterprise", "account": "LogiTech Solutions", "amount": 95000, "stage": "Qualification", "probability": 15, "rep": "Mike Johnson", "segment": "Mid-Market", "product": "Platform", "created": "2024-12-01", "close_date": "2025-05-01", "last_activity": "2024-12-22", "days_in_stage": 18},
    {"id": "OPP-009", "deal": "EduPlatform Analytics", "account": "EduPlatform", "amount": 28000, "stage": "Prospecting", "probability": 10, "rep": "James Park", "segment": "SMB", "product": "Analytics", "created": "2024-12-15", "close_date": "2025-06-01", "last_activity": "2024-12-28", "days_in_stage": 5},
    {"id": "OPP-010", "deal": "ManufacturePro Suite", "account": "ManufacturePro", "amount": 175000, "stage": "Discovery", "probability": 35, "rep": "Mike Johnson", "segment": "Enterprise", "product": "Platform", "created": "2024-09-01", "close_date": "2025-03-15", "last_activity": "2024-12-18", "days_in_stage": 28},
    {"id": "OPP-011", "deal": "GrowthCo Starter", "account": "GrowthCo", "amount": 22000, "stage": "Negotiation", "probability": 90, "rep": "Lisa Wong", "segment": "SMB", "product": "Starter", "created": "2024-10-01", "close_date": "2025-01-05", "last_activity": "2024-12-30", "days_in_stage": 5},
    {"id": "OPP-012", "deal": "SecureBank Platform", "account": "SecureBank", "amount": 250000, "stage": "Proposal", "probability": 50, "rep": "James Park", "segment": "Enterprise", "product": "Platform", "created": "2024-06-15", "close_date": "2025-02-28", "last_activity": "2024-12-05", "days_in_stage": 55},
]

STAGE_ORDER = ["Prospecting", "Qualification", "Discovery", "Proposal", "Negotiation"]
TEAM_QUOTA = 2500000  # Quarterly quota


def generate_pipeline_report(opportunities, quota, segment_filter=None):
    """Generate a complete pipeline report from opportunity data."""
    if segment_filter:
        opportunities = [o for o in opportunities if o["segment"].lower() == segment_filter.lower()]

    # Pipeline summary
    total_value = sum(o["amount"] for o in opportunities)
    weighted_value = sum(o["amount"] * o["probability"] / 100 for o in opportunities)
    opp_count = len(opportunities)
    avg_deal = round(total_value / opp_count) if opp_count > 0 else 0
    coverage = round(total_value / quota, 1) if quota > 0 else 0

    # By stage
    stage_data = {}
    for stage in STAGE_ORDER:
        stage_opps = [o for o in opportunities if o["stage"] == stage]
        if stage_opps:
            stage_value = sum(o["amount"] for o in stage_opps)
            stage_weighted = sum(o["amount"] * o["probability"] / 100 for o in stage_opps)
            avg_age = round(sum(o["days_in_stage"] for o in stage_opps) / len(stage_opps))
            stage_data[stage] = {
                "count": len(stage_opps),
                "value": stage_value,
                "weighted": round(stage_weighted),
                "pct_of_total": round(stage_value / total_value * 100, 1) if total_value > 0 else 0,
                "avg_days_in_stage": avg_age,
            }

    # By rep
    rep_data = {}
    for opp in opportunities:
        rep = opp["rep"]
        if rep not in rep_data:
            rep_data[rep] = {"pipeline": 0, "weighted": 0, "count": 0, "deals": []}
        rep_data[rep]["pipeline"] += opp["amount"]
        rep_data[rep]["weighted"] += round(opp["amount"] * opp["probability"] / 100)
        rep_data[rep]["count"] += 1
        rep_data[rep]["deals"].append(opp["deal"])

    for rep in rep_data:
        rep_data[rep]["avg_size"] = round(rep_data[rep]["pipeline"] / rep_data[rep]["count"])
        rep_data[rep]["coverage"] = round(rep_data[rep]["pipeline"] / (quota / 4), 1)  # Per-rep quota estimate

    # By segment
    segment_data = {}
    for opp in opportunities:
        seg = opp["segment"]
        if seg not in segment_data:
            segment_data[seg] = {"pipeline": 0, "count": 0, "deals": []}
        segment_data[seg]["pipeline"] += opp["amount"]
        segment_data[seg]["count"] += 1

    for seg in segment_data:
        segment_data[seg]["avg_size"] = round(segment_data[seg]["pipeline"] / segment_data[seg]["count"])
        segment_data[seg]["pct_of_total"] = round(segment_data[seg]["pipeline"] / total_value * 100, 1)

    # By product
    product_data = {}
    for opp in opportunities:
        prod = opp["product"]
        if prod not in product_data:
            product_data[prod] = {"pipeline": 0, "count": 0}
        product_data[prod]["pipeline"] += opp["amount"]
        product_data[prod]["count"] += 1

    for prod in product_data:
        product_data[prod]["avg_size"] = round(product_data[prod]["pipeline"] / product_data[prod]["count"])

    # At-risk deals (stale or very long in stage)
    at_risk = []
    for opp in opportunities:
        risk_factors = []
        if opp["days_in_stage"] > 30:
            risk_factors.append("Stale - over 30 days in stage")
        days_since_activity = (datetime.now() - datetime.strptime(opp["last_activity"], "%Y-%m-%d")).days
        if days_since_activity > 14:
            risk_factors.append(f"No activity in {days_since_activity} days")
        if risk_factors:
            at_risk.append({
                "deal": opp["deal"],
                "account": opp["account"],
                "amount": opp["amount"],
                "stage": opp["stage"],
                "days_in_stage": opp["days_in_stage"],
                "last_activity": opp["last_activity"],
                "risk_factors": risk_factors,
            })

    at_risk_value = sum(d["amount"] for d in at_risk)

    # Health indicators
    health = {
        "coverage": {"status": "green" if coverage >= 3 else "yellow" if coverage >= 2 else "red", "value": f"{coverage}x", "target": "3-4x"},
        "stage_balance": {"status": "green" if len(stage_data) >= 4 else "yellow", "detail": f"{len(stage_data)} of 5 stages populated"},
        "at_risk_pct": {"status": "green" if at_risk_value / total_value < 0.2 else "yellow" if at_risk_value / total_value < 0.35 else "red", "value": f"{round(at_risk_value / total_value * 100)}%"},
    }

    return {
        "summary": {
            "total_pipeline": total_value,
            "weighted_pipeline": round(weighted_value),
            "opportunity_count": opp_count,
            "average_deal_size": avg_deal,
            "pipeline_coverage": coverage,
            "quota": quota,
        },
        "by_stage": stage_data,
        "by_rep": {k: {kk: vv for kk, vv in v.items() if kk != "deals"} for k, v in rep_data.items()},
        "by_segment": segment_data,
        "by_product": product_data,
        "at_risk_deals": at_risk,
        "at_risk_total": at_risk_value,
        "health_indicators": health,
    }


def format_markdown(report):
    """Format pipeline report as markdown."""
    lines = []
    s = report["summary"]
    lines.append("# Pipeline Report")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("")
    lines.append("## Summary")
    lines.append(f"- **Total Pipeline:** ${s['total_pipeline']:,}")
    lines.append(f"- **Weighted Pipeline:** ${s['weighted_pipeline']:,}")
    lines.append(f"- **Opportunities:** {s['opportunity_count']}")
    lines.append(f"- **Average Deal Size:** ${s['average_deal_size']:,}")
    lines.append(f"- **Pipeline Coverage:** {s['pipeline_coverage']}x quota")
    lines.append("")

    lines.append("## Pipeline by Stage")
    lines.append("| Stage | # Opps | Value | Weighted | % of Total | Avg Days |")
    lines.append("|-------|--------|-------|----------|------------|----------|")
    for stage in STAGE_ORDER:
        if stage in report["by_stage"]:
            d = report["by_stage"][stage]
            lines.append(f"| {stage} | {d['count']} | ${d['value']:,} | ${d['weighted']:,} | {d['pct_of_total']}% | {d['avg_days_in_stage']}d |")
    lines.append("")

    lines.append("## Pipeline by Rep")
    lines.append("| Rep | Pipeline | Weighted | Coverage | # Opps | Avg Size |")
    lines.append("|-----|----------|----------|----------|--------|----------|")
    for rep, d in report["by_rep"].items():
        lines.append(f"| {rep} | ${d['pipeline']:,} | ${d['weighted']:,} | {d['coverage']}x | {d['count']} | ${d['avg_size']:,} |")
    lines.append("")

    if report["at_risk_deals"]:
        lines.append("## At-Risk Deals")
        lines.append("| Deal | Account | Value | Stage | Days in Stage | Risk |")
        lines.append("|------|---------|-------|-------|---------------|------|")
        for d in report["at_risk_deals"]:
            risk_str = "; ".join(d["risk_factors"])
            lines.append(f"| {d['deal']} | {d['account']} | ${d['amount']:,} | {d['stage']} | {d['days_in_stage']}d | {risk_str} |")
        lines.append(f"\n**Total At-Risk:** ${report['at_risk_total']:,}")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Generate a pipeline report from CRM opportunity data.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_pipeline_report.py --period this-quarter --format markdown
  python generate_pipeline_report.py --period this-month --format json
  python generate_pipeline_report.py --period this-quarter --segment enterprise
        """,
    )
    parser.add_argument(
        "--period",
        type=str,
        choices=["this-month", "this-quarter", "this-year"],
        default="this-quarter",
        help="Reporting period (default: this-quarter)",
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["json", "markdown"],
        default="json",
        help="Output format (default: json)",
    )
    parser.add_argument(
        "--segment",
        type=str,
        choices=["enterprise", "mid-market", "smb"],
        help="Filter by segment (optional)",
    )
    parser.add_argument(
        "--quota",
        type=int,
        default=TEAM_QUOTA,
        help=f"Team quota for coverage calculation (default: ${TEAM_QUOTA:,})",
    )

    args = parser.parse_args()

    report = generate_pipeline_report(SAMPLE_OPPORTUNITIES, args.quota, args.segment)
    report["metadata"] = {
        "period": args.period,
        "segment_filter": args.segment,
        "generated": datetime.now().isoformat(),
    }

    if args.format == "json":
        print(json.dumps(report, indent=2))
    else:
        print(format_markdown(report))


if __name__ == "__main__":
    main()
