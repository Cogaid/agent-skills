#!/usr/bin/env python3
"""Generate a TCO comparison between current state and proposed solution.

Produces a side-by-side Total Cost of Ownership analysis with direct costs,
indirect costs, and opportunity costs over a multi-year period.

Usage:
    python tco_comparison.py --current-costs costs.json --proposed-costs proposal.json
    python tco_comparison.py --demo --years 3 --format markdown
"""

import argparse
import json
from datetime import datetime


# Sample cost data for demonstration
DEMO_CURRENT_COSTS = {
    "name": "Current State (Legacy Platform)",
    "direct_costs": {
        "software_licenses": {"year1": 180000, "year2": 189000, "year3": 198450, "notes": "7% annual increase"},
        "hardware_infrastructure": {"year1": 45000, "year2": 45000, "year3": 45000, "notes": "On-prem servers"},
        "implementation_setup": {"year1": 0, "year2": 0, "year3": 0, "notes": "Already deployed"},
        "training": {"year1": 15000, "year2": 12000, "year3": 12000, "notes": "New hire training"},
        "annual_maintenance": {"year1": 36000, "year2": 37800, "year3": 39690, "notes": "5% annual increase"},
        "support_fees": {"year1": 45000, "year2": 45000, "year3": 45000, "notes": "Premium support tier"},
        "integration_middleware": {"year1": 25000, "year2": 25000, "year3": 25000, "notes": "MuleSoft license"},
    },
    "indirect_costs": {
        "system_administration": {"hours_per_week": 20, "hourly_rate": 75, "annual": 78000},
        "manual_data_entry": {"hours_per_week": 15, "hourly_rate": 45, "annual": 35100},
        "report_generation": {"hours_per_week": 10, "hourly_rate": 60, "annual": 31200},
        "troubleshooting": {"hours_per_week": 8, "hourly_rate": 85, "annual": 35360},
        "workarounds": {"hours_per_week": 12, "hourly_rate": 55, "annual": 34320},
        "compliance_audit_prep": {"hours_per_year": 200, "hourly_rate": 90, "annual": 18000},
    },
    "opportunity_costs": {
        "revenue_from_faster_launch": {"annual": 150000, "notes": "3 month delay on new features"},
        "customers_lost_to_downtime": {"annual": 75000, "notes": "Est. 15 customers x $5K ACV"},
        "deals_lost_to_slow_process": {"annual": 100000, "notes": "2 deals/quarter at $50K"},
        "talent_attrition": {"annual": 50000, "notes": "1 departure/year, recruiting cost"},
    },
}

DEMO_PROPOSED_COSTS = {
    "name": "Proposed Solution (Cloud Platform)",
    "direct_costs": {
        "software_licenses": {"year1": 144000, "year2": 148320, "year3": 152770, "notes": "3% annual increase"},
        "hardware_infrastructure": {"year1": 0, "year2": 0, "year3": 0, "notes": "Cloud-native, included"},
        "implementation_setup": {"year1": 95000, "year2": 0, "year3": 0, "notes": "One-time implementation"},
        "data_migration": {"year1": 35000, "year2": 0, "year3": 0, "notes": "One-time migration"},
        "training": {"year1": 25000, "year2": 8000, "year3": 8000, "notes": "Initial + ongoing"},
        "annual_maintenance": {"year1": 0, "year2": 0, "year3": 0, "notes": "Included in SaaS license"},
        "support_fees": {"year1": 0, "year2": 0, "year3": 0, "notes": "Included in license"},
        "integration_middleware": {"year1": 10000, "year2": 10000, "year3": 10000, "notes": "Native integrations + basic iPaaS"},
    },
    "indirect_costs": {
        "system_administration": {"hours_per_week": 5, "hourly_rate": 75, "annual": 19500},
        "manual_data_entry": {"hours_per_week": 3, "hourly_rate": 45, "annual": 7020},
        "report_generation": {"hours_per_week": 2, "hourly_rate": 60, "annual": 6240},
        "troubleshooting": {"hours_per_week": 2, "hourly_rate": 85, "annual": 8840},
        "workarounds": {"hours_per_week": 2, "hourly_rate": 55, "annual": 5720},
        "compliance_audit_prep": {"hours_per_year": 40, "hourly_rate": 90, "annual": 3600},
    },
    "opportunity_costs": {
        "revenue_from_faster_launch": {"annual": 25000, "notes": "2 week delay (vs 3 months)"},
        "customers_lost_to_downtime": {"annual": 10000, "notes": "99.99% SLA, est. 2 customers"},
        "deals_lost_to_slow_process": {"annual": 25000, "notes": "0.5 deals/quarter (faster demos)"},
        "talent_attrition": {"annual": 10000, "notes": "Modern tools improve retention"},
    },
}


def sum_direct_costs(costs_data, years=3):
    """Sum direct costs over the analysis period."""
    total = 0
    by_year = {1: 0, 2: 0, 3: 0}
    details = {}

    for category, values in costs_data["direct_costs"].items():
        for year in range(1, years + 1):
            year_key = f"year{year}"
            amount = values.get(year_key, 0)
            by_year[year] += amount
            total += amount

        cat_total = sum(values.get(f"year{y}", 0) for y in range(1, years + 1))
        details[category] = {
            "year1": values.get("year1", 0),
            "year2": values.get("year2", 0),
            "year3": values.get("year3", 0),
            "total": cat_total,
            "notes": values.get("notes", ""),
        }

    return {"total": total, "by_year": by_year, "details": details}


def sum_indirect_costs(costs_data, years=3):
    """Sum indirect costs over the analysis period."""
    annual = sum(item["annual"] for item in costs_data["indirect_costs"].values())
    total = annual * years
    details = {}

    for category, values in costs_data["indirect_costs"].items():
        details[category] = {
            "annual": values["annual"],
            "total": values["annual"] * years,
            "hours_per_week": values.get("hours_per_week"),
            "hourly_rate": values.get("hourly_rate"),
        }

    return {"annual": annual, "total": total, "details": details}


def sum_opportunity_costs(costs_data, years=3):
    """Sum opportunity costs over the analysis period."""
    annual = sum(item["annual"] for item in costs_data["opportunity_costs"].values())
    total = annual * years
    details = {}

    for category, values in costs_data["opportunity_costs"].items():
        details[category] = {
            "annual": values["annual"],
            "total": values["annual"] * years,
            "notes": values.get("notes", ""),
        }

    return {"annual": annual, "total": total, "details": details}


def generate_tco_comparison(current_data, proposed_data, years=3):
    """Generate complete TCO comparison."""
    current_direct = sum_direct_costs(current_data, years)
    current_indirect = sum_indirect_costs(current_data, years)
    current_opportunity = sum_opportunity_costs(current_data, years)
    current_total = current_direct["total"] + current_indirect["total"] + current_opportunity["total"]

    proposed_direct = sum_direct_costs(proposed_data, years)
    proposed_indirect = sum_indirect_costs(proposed_data, years)
    proposed_opportunity = sum_opportunity_costs(proposed_data, years)
    proposed_total = proposed_direct["total"] + proposed_indirect["total"] + proposed_opportunity["total"]

    savings = current_total - proposed_total
    savings_pct = round(savings / current_total * 100, 1) if current_total > 0 else 0

    # Year-by-year comparison
    yearly_comparison = []
    for year in range(1, years + 1):
        curr_yr = current_direct["by_year"][year] + current_indirect["annual"] + current_opportunity["annual"]
        prop_yr = proposed_direct["by_year"][year] + proposed_indirect["annual"] + proposed_opportunity["annual"]
        yearly_comparison.append({
            "year": year,
            "current": curr_yr,
            "proposed": prop_yr,
            "savings": curr_yr - prop_yr,
        })

    # Category-level savings
    category_savings = {
        "direct_costs": current_direct["total"] - proposed_direct["total"],
        "indirect_costs": current_indirect["total"] - proposed_indirect["total"],
        "opportunity_costs": current_opportunity["total"] - proposed_opportunity["total"],
    }

    return {
        "summary": {
            "current_name": current_data["name"],
            "proposed_name": proposed_data["name"],
            "analysis_years": years,
            "current_tco": current_total,
            "proposed_tco": proposed_total,
            "total_savings": savings,
            "savings_pct": savings_pct,
            "annual_savings_avg": round(savings / years),
        },
        "current_state": {
            "direct": current_direct,
            "indirect": current_indirect,
            "opportunity": current_opportunity,
            "total": current_total,
        },
        "proposed_state": {
            "direct": proposed_direct,
            "indirect": proposed_indirect,
            "opportunity": proposed_opportunity,
            "total": proposed_total,
        },
        "yearly_comparison": yearly_comparison,
        "category_savings": category_savings,
    }


def format_markdown(comparison):
    """Format TCO comparison as markdown."""
    lines = []
    s = comparison["summary"]
    lines.append(f"# TCO Comparison: {s['analysis_years']}-Year Analysis")
    lines.append(f"**{s['current_name']}** vs. **{s['proposed_name']}**")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("")

    lines.append("## Summary")
    lines.append(f"| Metric | Current | Proposed | Savings |")
    lines.append(f"|--------|---------|----------|---------|")
    lines.append(f"| **{s['analysis_years']}-Year TCO** | ${s['current_tco']:,} | ${s['proposed_tco']:,} | ${s['total_savings']:,} ({s['savings_pct']}%) |")
    lines.append(f"| **Annual Average** | ${round(s['current_tco']/s['analysis_years']):,} | ${round(s['proposed_tco']/s['analysis_years']):,} | ${s['annual_savings_avg']:,} |")
    lines.append("")

    lines.append("## Year-by-Year Comparison")
    lines.append("| Year | Current | Proposed | Annual Savings |")
    lines.append("|------|---------|----------|---------------|")
    for yr in comparison["yearly_comparison"]:
        lines.append(f"| Year {yr['year']} | ${yr['current']:,} | ${yr['proposed']:,} | ${yr['savings']:,} |")
    lines.append("")

    lines.append("## Savings by Category")
    cs = comparison["category_savings"]
    lines.append(f"- **Direct Costs:** ${cs['direct_costs']:,}")
    lines.append(f"- **Indirect Costs:** ${cs['indirect_costs']:,}")
    lines.append(f"- **Opportunity Costs:** ${cs['opportunity_costs']:,}")
    lines.append(f"- **Total:** ${s['total_savings']:,}")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Generate a TCO comparison between current state and proposed solution.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python tco_comparison.py --demo --years 3 --format markdown
  python tco_comparison.py --current-costs current.json --proposed-costs proposed.json
  python tco_comparison.py --demo --format json
        """,
    )
    parser.add_argument("--current-costs", type=str, help="Path to JSON file with current state costs")
    parser.add_argument("--proposed-costs", type=str, help="Path to JSON file with proposed solution costs")
    parser.add_argument("--demo", action="store_true", help="Use built-in demo data")
    parser.add_argument("--years", type=int, default=3, choices=[1, 2, 3, 4, 5], help="Analysis period in years (default: 3)")
    parser.add_argument("--format", type=str, choices=["json", "markdown"], default="json", help="Output format (default: json)")

    args = parser.parse_args()

    if args.demo:
        current_data = DEMO_CURRENT_COSTS
        proposed_data = DEMO_PROPOSED_COSTS
    elif args.current_costs and args.proposed_costs:
        with open(args.current_costs) as f:
            current_data = json.load(f)
        with open(args.proposed_costs) as f:
            proposed_data = json.load(f)
    else:
        parser.error("Either --demo or both --current-costs and --proposed-costs are required")
        return

    comparison = generate_tco_comparison(current_data, proposed_data, args.years)
    comparison["metadata"] = {
        "generated": datetime.now().isoformat(),
        "analysis_years": args.years,
        "data_source": "demo" if args.demo else "user-provided",
    }

    if args.format == "json":
        print(json.dumps(comparison, indent=2))
    else:
        print(format_markdown(comparison))


if __name__ == "__main__":
    main()
