#!/usr/bin/env python3
"""Generate a board-ready executive sales summary.

Produces a structured executive summary with KPI dashboard, revenue breakdown,
team performance, and strategic initiative updates.

Usage:
    python executive_summary.py --period monthly --format markdown
    python executive_summary.py --period quarterly --format json
"""

import argparse
import json
from datetime import datetime


# Sample executive data
SAMPLE_DATA = {
    "monthly": {
        "period": "December 2024",
        "revenue": {
            "actual": 892000,
            "target": 850000,
            "prior_period": 810000,
            "yoy_prior": 720000,
        },
        "new_customers": {"actual": 12, "target": 10},
        "expansion_revenue": {"actual": 245000, "pct_of_total": 27.5},
        "nrr": 118,
        "churn_rate": 1.8,
        "churn_target": 2.5,
        "kpis": {
            "new_arr": {"actual": 647000, "target": 600000},
            "pipeline_created": {"actual": 2800000, "target": 2500000},
            "win_rate": {"actual": 28.5, "target": 25.0},
            "avg_deal_size": {"actual": 72000, "target": 65000},
            "sales_cycle": {"actual": 58, "target": 60},
            "cac": {"actual": 18500, "target": 20000},
            "ltv_cac": {"actual": 4.2, "target": 3.5},
            "quota_attainment": {"actual": 105, "target": 100},
            "pipeline_coverage": {"actual": 3.8, "target": 3.5},
        },
        "revenue_by_type": {
            "new_business": {"actual": 520000, "prior": 480000, "pct_of_total": 58.3},
            "expansion": {"actual": 245000, "prior": 210000, "pct_of_total": 27.5},
            "renewal": {"actual": 127000, "prior": 120000, "pct_of_total": 14.2},
        },
        "revenue_by_segment": {
            "Enterprise": {"revenue": 485000, "pct_plan": 108, "growth": 28, "avg_deal": 121000},
            "Mid-Market": {"revenue": 265000, "pct_plan": 102, "growth": 18, "avg_deal": 53000},
            "SMB": {"revenue": 142000, "pct_plan": 95, "growth": 12, "avg_deal": 18000},
        },
        "top_wins": [
            {"customer": "SecureBank", "arr": 250000, "segment": "Enterprise", "context": "Competitive displacement from Acme Corp"},
            {"customer": "HealthFirst", "arr": 150000, "segment": "Enterprise", "context": "New logo, HIPAA compliance was differentiator"},
            {"customer": "ManufacturePro", "arr": 95000, "segment": "Enterprise", "context": "Expansion from analytics to full platform"},
        ],
        "top_risks": [
            {"risk": "Enterprise pipeline softening in financial services", "impact": 350000, "mitigation": "Increase outbound to adjacent verticals"},
            {"risk": "Two senior reps departing in Q1", "impact": 200000, "mitigation": "Accelerating hiring, redistributing accounts"},
        ],
        "team": [
            {"rep": "Sarah Chen", "quota": 250000, "closed": 280000, "attainment": 112, "pipeline": 620000, "win_rate": 35, "trend": "up"},
            {"rep": "Mike Johnson", "quota": 250000, "closed": 215000, "attainment": 86, "pipeline": 480000, "win_rate": 24, "trend": "flat"},
            {"rep": "James Park", "quota": 175000, "closed": 195000, "attainment": 111, "pipeline": 520000, "win_rate": 30, "trend": "up"},
            {"rep": "Lisa Wong", "quota": 175000, "closed": 202000, "attainment": 115, "pipeline": 380000, "win_rate": 32, "trend": "up"},
        ],
        "initiatives": [
            {"name": "Partner channel launch", "status": "On Track", "progress": 75, "milestone": "First partner deals in Q1", "owner": "VP Sales"},
            {"name": "Enterprise playbook rollout", "status": "Complete", "progress": 100, "milestone": "All reps trained", "owner": "Sales Enablement"},
            {"name": "New vertical: Healthcare", "status": "At Risk", "progress": 45, "milestone": "5 qualified opps by Q1 end", "owner": "James Park"},
        ],
        "efficiency": {
            "cac": {"current": 18500, "prior": 21000, "benchmark": 20000},
            "sales_efficiency": {"current": 1.2, "prior": 1.1, "benchmark": 1.0},
            "revenue_per_rep": {"current": 223000, "prior": 202000, "benchmark": 200000},
            "ramp_time_months": {"current": 4.5, "prior": 5.0, "benchmark": 5.0},
            "quota_carrying_reps": {"current": 4, "prior": 4},
        },
    },
}


def generate_executive_summary(data):
    """Generate structured executive summary from data."""
    rev = data["revenue"]
    pct_of_plan = round(rev["actual"] / rev["target"] * 100, 1)
    yoy_change = round((rev["actual"] - rev["yoy_prior"]) / rev["yoy_prior"] * 100, 1)
    mom_change = round((rev["actual"] - rev["prior_period"]) / rev["prior_period"] * 100, 1)

    # KPI status assessment
    kpi_dashboard = {}
    for metric, values in data["kpis"].items():
        actual = values["actual"]
        target = values["target"]
        # For metrics where lower is better (cycle, cac)
        if metric in ["sales_cycle", "cac"]:
            if actual <= target:
                status = "on_track"
            elif actual <= target * 1.15:
                status = "at_risk"
            else:
                status = "off_track"
        else:
            if actual >= target:
                status = "on_track"
            elif actual >= target * 0.85:
                status = "at_risk"
            else:
                status = "off_track"

        kpi_dashboard[metric] = {
            "actual": actual,
            "target": target,
            "status": status,
            "pct_of_target": round(actual / target * 100, 1) if target != 0 else 0,
        }

    return {
        "period": data["period"],
        "headlines": {
            "revenue": rev["actual"],
            "pct_of_plan": pct_of_plan,
            "yoy_change": yoy_change,
            "mom_change": mom_change,
            "new_customers": data["new_customers"],
            "expansion_revenue": data["expansion_revenue"],
            "nrr": data["nrr"],
            "churn": {"rate": data["churn_rate"], "target": data["churn_target"]},
        },
        "kpi_dashboard": kpi_dashboard,
        "revenue_by_type": data["revenue_by_type"],
        "revenue_by_segment": data["revenue_by_segment"],
        "top_wins": data["top_wins"],
        "top_risks": data["top_risks"],
        "team_performance": data["team"],
        "strategic_initiatives": data["initiatives"],
        "efficiency_metrics": data["efficiency"],
    }


def format_markdown(summary):
    """Format as executive markdown report."""
    lines = []
    h = summary["headlines"]
    lines.append(f"# Executive Sales Summary: {summary['period']}")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("")

    lines.append("## Headlines")
    lines.append(f"- **Revenue:** ${h['revenue']:,} ({h['pct_of_plan']}% of plan, +{h['yoy_change']}% YoY)")
    lines.append(f"- **New Customers:** {h['new_customers']['actual']} ({round(h['new_customers']['actual']/h['new_customers']['target']*100)}% of target)")
    lines.append(f"- **Expansion Revenue:** ${h['expansion_revenue']['actual']:,} ({h['expansion_revenue']['pct_of_total']}% of total)")
    lines.append(f"- **Net Revenue Retention:** {h['nrr']}%")
    lines.append(f"- **Churn:** {h['churn']['rate']}% (target: <{h['churn']['target']}%)")
    lines.append("")

    lines.append("## KPI Dashboard")
    lines.append("| Metric | Actual | Target | Status |")
    lines.append("|--------|--------|--------|--------|")
    status_labels = {"on_track": "On Track", "at_risk": "At Risk", "off_track": "Off Track"}
    for metric, d in summary["kpi_dashboard"].items():
        label = metric.replace("_", " ").title()
        status = status_labels[d["status"]]
        if isinstance(d["actual"], float):
            actual_str = f"{d['actual']}"
        elif d["actual"] > 1000:
            actual_str = f"${d['actual']:,}"
        else:
            actual_str = str(d["actual"])
        lines.append(f"| {label} | {actual_str} | {d['target']} | {status} |")
    lines.append("")

    lines.append("## Top Wins")
    for i, w in enumerate(summary["top_wins"], 1):
        lines.append(f"{i}. **{w['customer']}** -- ${w['arr']:,} ARR -- {w['context']}")
    lines.append("")

    lines.append("## Top Risks")
    for i, r in enumerate(summary["top_risks"], 1):
        lines.append(f"{i}. **{r['risk']}** -- Impact: ${r['impact']:,} -- Mitigation: {r['mitigation']}")
    lines.append("")

    lines.append("## Team Performance")
    lines.append("| Rep | Quota | Closed | Attainment | Pipeline | Win Rate | Trend |")
    lines.append("|-----|-------|--------|------------|----------|----------|-------|")
    for t in summary["team_performance"]:
        lines.append(f"| {t['rep']} | ${t['quota']:,} | ${t['closed']:,} | {t['attainment']}% | ${t['pipeline']:,} | {t['win_rate']}% | {t['trend']} |")
    lines.append("")

    lines.append("## Strategic Initiatives")
    lines.append("| Initiative | Status | Progress | Next Milestone | Owner |")
    lines.append("|-----------|--------|----------|----------------|-------|")
    for i in summary["strategic_initiatives"]:
        lines.append(f"| {i['name']} | {i['status']} | {i['progress']}% | {i['milestone']} | {i['owner']} |")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Generate a board-ready executive sales summary.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python executive_summary.py --period monthly --format markdown
  python executive_summary.py --period quarterly --format json
        """,
    )
    parser.add_argument(
        "--period",
        type=str,
        choices=["monthly", "quarterly"],
        default="monthly",
        help="Report period (default: monthly)",
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["json", "markdown"],
        default="json",
        help="Output format (default: json)",
    )
    parser.add_argument(
        "--include-charts",
        action="store_true",
        help="Include chart placeholder sections (for rendering tools)",
    )

    args = parser.parse_args()

    data = SAMPLE_DATA.get(args.period, SAMPLE_DATA["monthly"])
    summary = generate_executive_summary(data)
    summary["metadata"] = {
        "period_type": args.period,
        "generated": datetime.now().isoformat(),
        "include_charts": args.include_charts,
    }

    if args.include_charts:
        summary["chart_specs"] = {
            "revenue_trend": {"type": "line", "data": "revenue by month for last 12 months"},
            "pipeline_funnel": {"type": "funnel", "data": "current pipeline by stage"},
            "quota_gauge": {"type": "gauge", "data": "team quota attainment"},
            "segment_breakdown": {"type": "pie", "data": "revenue by segment"},
        }

    if args.format == "json":
        print(json.dumps(summary, indent=2))
    else:
        print(format_markdown(summary))


if __name__ == "__main__":
    main()
