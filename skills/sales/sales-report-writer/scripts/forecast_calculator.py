#!/usr/bin/env python3
"""Calculate weighted sales forecast from opportunity data.

Generates forecast by category (Closed, Commit, Best Case, Pipeline) with
rep-level breakdown and week-over-week movement tracking.

Usage:
    python forecast_calculator.py --method weighted --period Q1-2025
    python forecast_calculator.py --method category --period Q1-2025 --format markdown
"""

import argparse
import json
from datetime import datetime


# Sample forecast data with category assignments
SAMPLE_FORECAST = {
    "period": "Q1-2025",
    "quota": 2500000,
    "reps": {
        "Sarah Chen": {
            "quota": 750000,
            "deals": [
                {"deal": "TechFlow Platform", "amount": 85000, "category": "commit", "probability": 90, "close_date": "2025-01-15", "next_step": "Contract review with legal"},
                {"deal": "HealthFirst Platform", "amount": 150000, "category": "best_case", "probability": 55, "close_date": "2025-02-15", "next_step": "Executive sponsor meeting"},
                {"deal": "CloudNine Expansion", "amount": 45000, "category": "pipeline", "probability": 30, "close_date": "2025-03-01", "next_step": "Discovery call #2"},
            ],
            "closed_won": 125000,
        },
        "Mike Johnson": {
            "quota": 750000,
            "deals": [
                {"deal": "DataVault Migration", "amount": 120000, "category": "best_case", "probability": 60, "close_date": "2025-02-01", "next_step": "Technical deep dive"},
                {"deal": "ManufacturePro Suite", "amount": 175000, "category": "pipeline", "probability": 35, "close_date": "2025-03-15", "next_step": "Discovery complete, proposal prep"},
                {"deal": "LogiTech Enterprise", "amount": 95000, "category": "pipeline", "probability": 15, "close_date": "2025-03-30", "next_step": "Qualification meeting"},
            ],
            "closed_won": 80000,
        },
        "James Park": {
            "quota": 500000,
            "deals": [
                {"deal": "SecureBank Platform", "amount": 250000, "category": "commit", "probability": 80, "close_date": "2025-02-28", "next_step": "Final pricing negotiation"},
                {"deal": "FinServ Analytics", "amount": 200000, "category": "pipeline", "probability": 20, "close_date": "2025-03-31", "next_step": "Needs analysis presentation"},
                {"deal": "EduPlatform Analytics", "amount": 28000, "category": "pipeline", "probability": 10, "close_date": "2025-03-15", "next_step": "Initial outreach follow-up"},
            ],
            "closed_won": 65000,
        },
        "Lisa Wong": {
            "quota": 500000,
            "deals": [
                {"deal": "RetailMax Starter", "amount": 18000, "category": "commit", "probability": 85, "close_date": "2025-01-10", "next_step": "Contract sent, awaiting signature"},
                {"deal": "GrowthCo Starter", "amount": 22000, "category": "commit", "probability": 90, "close_date": "2025-01-05", "next_step": "Verbal yes, PO processing"},
                {"deal": "StartupHub Basic", "amount": 12000, "category": "best_case", "probability": 50, "close_date": "2025-02-28", "next_step": "Demo scheduled"},
            ],
            "closed_won": 95000,
        },
    },
    # Simulated week-over-week history
    "weekly_history": [
        {"week": "2024-12-09", "closed": 280000, "commit": 310000, "best_case": 295000, "pipeline": 520000},
        {"week": "2024-12-16", "closed": 320000, "commit": 345000, "best_case": 310000, "pipeline": 505000},
        {"week": "2024-12-23", "closed": 345000, "commit": 365000, "best_case": 325000, "pipeline": 545000},
        {"week": "2024-12-30", "closed": 365000, "commit": 375000, "best_case": 327000, "pipeline": 555000},
    ],
}


def calculate_forecast(data, method="weighted"):
    """Calculate forecast using specified methodology."""
    total_closed = 0
    total_commit = 0
    total_best_case = 0
    total_pipeline = 0
    total_weighted = 0

    rep_forecasts = {}

    for rep, rep_data in data["reps"].items():
        closed = rep_data["closed_won"]
        commit = sum(d["amount"] for d in rep_data["deals"] if d["category"] == "commit")
        best_case = sum(d["amount"] for d in rep_data["deals"] if d["category"] == "best_case")
        pipeline = sum(d["amount"] for d in rep_data["deals"] if d["category"] == "pipeline")

        if method == "weighted":
            weighted = sum(d["amount"] * d["probability"] / 100 for d in rep_data["deals"])
        else:
            weighted = commit * 0.9 + best_case * 0.5 + pipeline * 0.15

        total_forecast = closed + commit + best_case + pipeline
        attainment = round((closed + commit) / rep_data["quota"] * 100, 1) if rep_data["quota"] > 0 else 0

        rep_forecasts[rep] = {
            "quota": rep_data["quota"],
            "closed_won": closed,
            "commit": commit,
            "best_case": best_case,
            "pipeline": pipeline,
            "weighted_forecast": round(weighted),
            "total_forecast": total_forecast,
            "attainment_pct": attainment,
            "gap_to_quota": rep_data["quota"] - closed - commit,
            "deal_count": len(rep_data["deals"]),
            "commit_deals": [d for d in rep_data["deals"] if d["category"] == "commit"],
        }

        total_closed += closed
        total_commit += commit
        total_best_case += best_case
        total_pipeline += pipeline
        total_weighted += weighted

    quota = data["quota"]
    gap = quota - total_closed - total_commit

    # Risk analysis
    risks = []
    for rep, rf in rep_forecasts.items():
        if rf["attainment_pct"] < 50:
            risks.append({
                "risk": f"{rep} at {rf['attainment_pct']}% attainment (Closed + Commit)",
                "impact": rf["gap_to_quota"],
                "mitigation": "Pipeline acceleration, deal coaching",
            })

    # Upside opportunities
    upside = []
    for rep, rep_data in data["reps"].items():
        for deal in rep_data["deals"]:
            if deal["category"] == "best_case" and deal["amount"] > 100000:
                upside.append({
                    "deal": deal["deal"],
                    "amount": deal["amount"],
                    "probability": deal["probability"],
                    "close_date": deal["close_date"],
                })

    return {
        "period": data["period"],
        "method": method,
        "summary": {
            "quota": quota,
            "closed_won": total_closed,
            "commit": total_commit,
            "best_case": total_best_case,
            "pipeline": total_pipeline,
            "total_forecast": total_closed + total_commit + total_best_case + total_pipeline,
            "weighted_forecast": round(total_weighted),
            "closed_plus_commit": total_closed + total_commit,
            "closed_plus_commit_pct": round((total_closed + total_commit) / quota * 100, 1),
            "gap_to_quota": gap,
            "coverage": round((total_closed + total_commit + total_best_case + total_pipeline) / quota, 1),
        },
        "by_rep": rep_forecasts,
        "weekly_movement": data.get("weekly_history", []),
        "risks": risks,
        "upside_opportunities": upside,
    }


def format_markdown(forecast):
    """Format forecast as markdown."""
    lines = []
    s = forecast["summary"]
    lines.append(f"# Forecast Report: {forecast['period']}")
    lines.append(f"Method: {forecast['method']}")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("")

    lines.append("## Forecast Summary")
    lines.append(f"| Category | Amount | # Deals |")
    lines.append(f"|----------|--------|---------|")
    lines.append(f"| Closed Won | ${s['closed_won']:,} | -- |")
    lines.append(f"| Commit | ${s['commit']:,} | -- |")
    lines.append(f"| Best Case | ${s['best_case']:,} | -- |")
    lines.append(f"| Pipeline | ${s['pipeline']:,} | -- |")
    lines.append(f"| **Total** | **${s['total_forecast']:,}** | -- |")
    lines.append("")

    lines.append("## Quota Attainment")
    lines.append(f"- **Quota:** ${s['quota']:,}")
    lines.append(f"- **Closed + Commit:** ${s['closed_plus_commit']:,} ({s['closed_plus_commit_pct']}%)")
    lines.append(f"- **Gap to Quota:** ${s['gap_to_quota']:,}")
    lines.append(f"- **Coverage:** {s['coverage']}x")
    lines.append("")

    lines.append("## Forecast by Rep")
    lines.append("| Rep | Quota | Closed | Commit | Best Case | Pipeline | Attainment |")
    lines.append("|-----|-------|--------|--------|-----------|----------|------------|")
    for rep, d in forecast["by_rep"].items():
        lines.append(f"| {rep} | ${d['quota']:,} | ${d['closed_won']:,} | ${d['commit']:,} | ${d['best_case']:,} | ${d['pipeline']:,} | {d['attainment_pct']}% |")
    lines.append("")

    if forecast["risks"]:
        lines.append("## Risks")
        for r in forecast["risks"]:
            lines.append(f"- **{r['risk']}** -- Impact: ${r['impact']:,} -- Mitigation: {r['mitigation']}")
        lines.append("")

    if forecast["upside_opportunities"]:
        lines.append("## Upside Opportunities")
        for u in forecast["upside_opportunities"]:
            lines.append(f"- **{u['deal']}** -- ${u['amount']:,} ({u['probability']}% probability) -- Close: {u['close_date']}")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Calculate weighted sales forecast from opportunity data.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python forecast_calculator.py --method weighted --period Q1-2025
  python forecast_calculator.py --method category --period Q1-2025 --format markdown
        """,
    )
    parser.add_argument(
        "--method",
        type=str,
        choices=["weighted", "category"],
        default="weighted",
        help="Forecast methodology: weighted (probability-based) or category (commit/best-case weights)",
    )
    parser.add_argument(
        "--period",
        type=str,
        default="Q1-2025",
        help="Fiscal period (default: Q1-2025)",
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["json", "markdown"],
        default="json",
        help="Output format (default: json)",
    )

    args = parser.parse_args()

    forecast = calculate_forecast(SAMPLE_FORECAST, method=args.method)
    forecast["metadata"] = {
        "generated": datetime.now().isoformat(),
        "method": args.method,
        "period": args.period,
    }

    if args.format == "json":
        print(json.dumps(forecast, indent=2))
    else:
        print(format_markdown(forecast))


if __name__ == "__main__":
    main()
