#!/usr/bin/env python3
"""Generate a presentation-ready ROI business case.

Creates a structured slide-by-slide ROI presentation with data from the ROI model.
Outputs as markdown (for conversion to slides) or JSON (for rendering engines).

Usage:
    python roi_presentation.py --model roi_model.json --format markdown
    python roi_presentation.py --demo --company "Acme Corp" --format json
"""

import argparse
import json
from datetime import datetime


# Demo presentation data
DEMO_PRESENTATION = {
    "company": "TechFlow Inc",
    "prepared_by": "Sales Team",
    "our_product": "CloudPlatform Pro",
    "pain_points": [
        {"pain": "Manual reporting takes 15+ hours per week", "annual_cost": 78000},
        {"pain": "System downtime costs revenue and customers", "annual_cost": 75000},
        {"pain": "Data silos prevent cross-team collaboration", "annual_cost": 52000},
    ],
    "solution_capabilities": [
        {"capability": "Automated reporting engine", "addresses": "Manual reporting", "outcome": "Eliminates 15 hrs/week of manual work"},
        {"capability": "99.99% uptime SLA with redundancy", "addresses": "System downtime", "outcome": "Reduces downtime from 40hrs/yr to 1hr/yr"},
        {"capability": "Unified data platform", "addresses": "Data silos", "outcome": "Single source of truth for all teams"},
    ],
    "financial_impact": {
        "cost_savings": 120000,
        "revenue_impact": 45000,
        "productivity_gains": 60000,
        "risk_reduction": 25000,
        "total_annual_value": 250000,
    },
    "investment": {
        "software_license": 48000,
        "implementation": 75000,
        "training": 20000,
        "integration": 7000,
        "total_year1": 150000,
        "annual_ongoing": 48000,
    },
    "roi_metrics": {
        "roi_pct": 235,
        "payback_months": 8.9,
        "three_year_npv": 312000,
        "irr_pct": 89,
    },
    "proof_points": [
        {"customer": "DataVault Systems", "result": "Reduced reporting time by 80%, saving $95K/year", "industry": "Financial Services"},
        {"customer": "HealthFirst Corp", "result": "Achieved 99.99% uptime, zero revenue-impacting outages in 12 months", "industry": "Healthcare"},
        {"customer": "RetailMax", "result": "Consolidated 4 tools into 1, 45% faster decision-making", "industry": "Retail"},
    ],
    "next_steps": [
        {"step": "Review and validate assumptions together", "owner": "Joint", "timeline": "This week"},
        {"step": "Technical deep-dive with IT team", "owner": "Us + IT", "timeline": "Next week"},
        {"step": "Executive presentation to CFO", "owner": "Champion + Us", "timeline": "Week 3"},
        {"step": "Contract negotiation", "owner": "Procurement", "timeline": "Week 4"},
    ],
}


def generate_presentation(data):
    """Generate slide-by-slide presentation structure."""
    slides = []

    # Slide 1: Title
    slides.append({
        "slide_number": 1,
        "title": "ROI Business Case",
        "subtitle": f"Prepared for {data['company']}",
        "content": {
            "prepared_by": data["prepared_by"],
            "date": datetime.now().strftime("%B %d, %Y"),
            "product": data["our_product"],
        },
    })

    # Slide 2: The Problem / Cost of Status Quo
    total_cost = sum(p["annual_cost"] for p in data["pain_points"])
    slides.append({
        "slide_number": 2,
        "title": "The Cost of Status Quo",
        "subtitle": f"Your current challenges cost ${total_cost:,}/year",
        "content": {
            "pain_points": data["pain_points"],
            "total_annual_cost": total_cost,
            "key_message": "Every month without action costs your organization money.",
        },
    })

    # Slide 3: The Solution
    slides.append({
        "slide_number": 3,
        "title": f"How {data['our_product']} Solves This",
        "subtitle": "Capability-to-outcome mapping",
        "content": {
            "capabilities": data["solution_capabilities"],
            "key_message": "Purpose-built to address your specific challenges.",
        },
    })

    # Slide 4: Financial Impact
    fi = data["financial_impact"]
    slides.append({
        "slide_number": 4,
        "title": "Financial Impact",
        "subtitle": f"${fi['total_annual_value']:,} in annual value",
        "content": {
            "value_categories": [
                {"category": "Cost Savings", "amount": fi["cost_savings"]},
                {"category": "Revenue Impact", "amount": fi["revenue_impact"]},
                {"category": "Productivity Gains", "amount": fi["productivity_gains"]},
                {"category": "Risk Reduction", "amount": fi["risk_reduction"]},
            ],
            "total_annual_value": fi["total_annual_value"],
        },
    })

    # Slide 5: Investment and Return
    inv = data["investment"]
    roi = data["roi_metrics"]
    slides.append({
        "slide_number": 5,
        "title": "Investment and Return",
        "subtitle": f"{roi['roi_pct']}% ROI with {roi['payback_months']}-month payback",
        "content": {
            "investment": {
                "year1_total": inv["total_year1"],
                "breakdown": {
                    "Software": inv["software_license"],
                    "Implementation": inv["implementation"],
                    "Training": inv["training"],
                    "Integration": inv["integration"],
                },
                "annual_ongoing": inv["annual_ongoing"],
            },
            "returns": {
                "roi_pct": roi["roi_pct"],
                "payback_months": roi["payback_months"],
                "three_year_npv": roi["three_year_npv"],
                "irr_pct": roi["irr_pct"],
            },
        },
    })

    # Slide 6: Scenarios
    slides.append({
        "slide_number": 6,
        "title": "Even Conservative Estimates Show Strong ROI",
        "subtitle": "Sensitivity across scenarios",
        "content": {
            "scenarios": [
                {"name": "Conservative (75%)", "roi": round(roi["roi_pct"] * 0.65), "payback": round(roi["payback_months"] * 1.4, 1)},
                {"name": "Moderate (Base)", "roi": roi["roi_pct"], "payback": roi["payback_months"]},
                {"name": "Aggressive (125%)", "roi": round(roi["roi_pct"] * 1.35), "payback": round(roi["payback_months"] * 0.7, 1)},
            ],
            "key_message": "Even at 75% of projected gains, the investment delivers strong returns.",
        },
    })

    # Slide 7: Proof Points
    slides.append({
        "slide_number": 7,
        "title": "Proven Results with Similar Companies",
        "subtitle": "Customer success stories",
        "content": {
            "proof_points": data["proof_points"],
            "key_message": "These results are repeatable and documented.",
        },
    })

    # Slide 8: Next Steps
    slides.append({
        "slide_number": 8,
        "title": "Next Steps",
        "subtitle": "Path to value",
        "content": {
            "steps": data["next_steps"],
            "key_message": "We can start delivering value within weeks.",
        },
    })

    return {
        "presentation": {
            "title": f"ROI Business Case: {data['our_product']} for {data['company']}",
            "total_slides": len(slides),
            "slides": slides,
        },
    }


def format_markdown(presentation):
    """Format presentation as markdown slides."""
    lines = []
    pres = presentation["presentation"]
    lines.append(f"# {pres['title']}")
    lines.append("")

    for slide in pres["slides"]:
        lines.append(f"---")
        lines.append("")
        lines.append(f"## Slide {slide['slide_number']}: {slide['title']}")
        if slide.get("subtitle"):
            lines.append(f"*{slide['subtitle']}*")
        lines.append("")

        content = slide["content"]
        if "pain_points" in content:
            for pp in content["pain_points"]:
                lines.append(f"- {pp['pain']} -- **${pp['annual_cost']:,}/year**")
            lines.append(f"\n**Total cost of status quo: ${content['total_annual_cost']:,}/year**")

        elif "capabilities" in content:
            for cap in content["capabilities"]:
                lines.append(f"- **{cap['capability']}** -> {cap['outcome']}")

        elif "value_categories" in content:
            lines.append("| Category | Annual Value |")
            lines.append("|----------|-------------|")
            for vc in content["value_categories"]:
                lines.append(f"| {vc['category']} | ${vc['amount']:,} |")
            lines.append(f"| **Total** | **${content['total_annual_value']:,}** |")

        elif "investment" in content and "returns" in content:
            inv = content["investment"]
            ret = content["returns"]
            lines.append(f"**Investment:** ${inv['year1_total']:,} (Year 1)")
            lines.append("")
            for k, v in inv["breakdown"].items():
                lines.append(f"  - {k}: ${v:,}")
            lines.append("")
            lines.append(f"**Returns:**")
            lines.append(f"  - ROI: {ret['roi_pct']}%")
            lines.append(f"  - Payback: {ret['payback_months']} months")
            lines.append(f"  - 3-Year NPV: ${ret['three_year_npv']:,}")

        elif "scenarios" in content:
            lines.append("| Scenario | ROI | Payback |")
            lines.append("|----------|-----|---------|")
            for sc in content["scenarios"]:
                lines.append(f"| {sc['name']} | {sc['roi']}% | {sc['payback']} mo |")

        elif "proof_points" in content:
            for pp in content["proof_points"]:
                lines.append(f"- **{pp['customer']}** ({pp['industry']}): {pp['result']}")

        elif "steps" in content:
            for step in content["steps"]:
                lines.append(f"- {step['step']} -- *{step['owner']}* -- {step['timeline']}")

        if content.get("key_message"):
            lines.append(f"\n> {content['key_message']}")

        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Generate a presentation-ready ROI business case.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python roi_presentation.py --demo --format markdown
  python roi_presentation.py --demo --company "Acme Corp" --format json
  python roi_presentation.py --model roi_model.json --format markdown
        """,
    )
    parser.add_argument("--model", type=str, help="Path to JSON file with ROI model/data")
    parser.add_argument("--demo", action="store_true", help="Use built-in demo data")
    parser.add_argument("--company", type=str, help="Override company name")
    parser.add_argument("--format", type=str, choices=["json", "markdown"], default="json", help="Output format (default: json)")

    args = parser.parse_args()

    if args.demo:
        data = DEMO_PRESENTATION.copy()
    elif args.model:
        with open(args.model) as f:
            data = json.load(f)
    else:
        parser.error("Either --demo or --model is required")
        return

    if args.company:
        data["company"] = args.company

    presentation = generate_presentation(data)
    presentation["metadata"] = {
        "generated": datetime.now().isoformat(),
        "company": data["company"],
        "data_source": "demo" if args.demo else "user-provided",
    }

    if args.format == "json":
        print(json.dumps(presentation, indent=2))
    else:
        print(format_markdown(presentation))


if __name__ == "__main__":
    main()
