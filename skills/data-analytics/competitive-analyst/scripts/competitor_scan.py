#!/usr/bin/env python3
"""Generate a competitive analysis snapshot for a specified company.

Usage:
    python competitor_scan.py --company "Acme Inc" --depth standard
    python competitor_scan.py --company "Acme Inc" --depth quick --output brief.json
"""

import argparse
import json
import sys
from datetime import datetime

DEPTH_LEVELS = {
    "quick": {
        "name": "Quick Scan",
        "time_investment": "2-4 hours",
        "sections": ["overview", "product_summary", "pricing", "key_differentiator"],
    },
    "standard": {
        "name": "Standard Analysis",
        "time_investment": "1-2 days",
        "sections": [
            "overview", "product_comparison", "pricing_analysis",
            "strategic_assessment", "swot", "win_loss", "recommended_actions",
        ],
    },
    "deep": {
        "name": "Deep Dive",
        "time_investment": "1-2 weeks",
        "sections": [
            "overview", "product_comparison", "pricing_analysis",
            "strategic_assessment", "porters_five_forces", "swot",
            "win_loss", "financial_analysis", "team_analysis",
            "technology_assessment", "customer_analysis",
            "recommended_actions", "monitoring_plan",
        ],
    },
}

ANALYSIS_FRAMEWORKS = {
    "porters_five_forces": {
        "name": "Porter's Five Forces",
        "dimensions": [
            {"force": "Threat of New Entrants", "assessment": "[High/Medium/Low]", "factors": ["Capital requirements", "Brand loyalty", "Regulatory barriers", "Technology barriers"]},
            {"force": "Bargaining Power of Suppliers", "assessment": "[High/Medium/Low]", "factors": ["Supplier concentration", "Switching costs", "Forward integration threat"]},
            {"force": "Bargaining Power of Buyers", "assessment": "[High/Medium/Low]", "factors": ["Buyer concentration", "Price sensitivity", "Switching costs"]},
            {"force": "Threat of Substitutes", "assessment": "[High/Medium/Low]", "factors": ["Alternative solutions", "Price-performance of substitutes"]},
            {"force": "Competitive Rivalry", "assessment": "[High/Medium/Low]", "factors": ["Number of competitors", "Industry growth", "Product differentiation"]},
        ],
    },
    "swot": {
        "name": "SWOT Analysis",
        "dimensions": {
            "strengths": ["[TO BE ASSESSED]"],
            "weaknesses": ["[TO BE ASSESSED]"],
            "opportunities": ["[TO BE ASSESSED]"],
            "threats": ["[TO BE ASSESSED]"],
        },
    },
}


def generate_scan(company, depth):
    """Generate a competitive analysis skeleton."""
    depth_info = DEPTH_LEVELS.get(depth, DEPTH_LEVELS["standard"])

    scan = {
        "metadata": {
            "competitor": company,
            "depth": depth_info["name"],
            "time_investment": depth_info["time_investment"],
            "generated_date": datetime.now().strftime("%Y-%m-%d"),
            "analyst": "[ANALYST NAME]",
            "status": "TEMPLATE - Fill in with research",
        },
        "company_overview": {
            "name": company,
            "founded": "[YEAR]",
            "headquarters": "[CITY, COUNTRY]",
            "employees": "[N]",
            "funding": "[Total raised]",
            "estimated_revenue": "[Amount or range]",
            "target_market": "[ICP description]",
            "key_products": ["[Product 1]", "[Product 2]"],
        },
        "sections_to_complete": depth_info["sections"],
        "data_collection_checklist": [
            {"source": "Company website", "status": "TODO", "data_needed": "Products, pricing, messaging"},
            {"source": "LinkedIn", "status": "TODO", "data_needed": "Employee count, hiring trends"},
            {"source": "G2/Capterra reviews", "status": "TODO", "data_needed": "Ratings, pros/cons"},
            {"source": "Crunchbase", "status": "TODO", "data_needed": "Funding history, investors"},
            {"source": "Job postings", "status": "TODO", "data_needed": "Strategic priorities, tech stack"},
            {"source": "Press releases", "status": "TODO", "data_needed": "Recent announcements"},
            {"source": "Internal win/loss data", "status": "TODO", "data_needed": "Head-to-head performance"},
        ],
    }

    if "porters_five_forces" in depth_info["sections"]:
        scan["frameworks"] = {"porters_five_forces": ANALYSIS_FRAMEWORKS["porters_five_forces"]}

    if "swot" in depth_info["sections"]:
        scan.setdefault("frameworks", {})["swot"] = ANALYSIS_FRAMEWORKS["swot"]

    return scan


def main():
    parser = argparse.ArgumentParser(
        description="Generate a competitive analysis snapshot template."
    )
    parser.add_argument(
        "--company",
        required=True,
        help="Competitor company name",
    )
    parser.add_argument(
        "--depth",
        choices=list(DEPTH_LEVELS.keys()),
        default="standard",
        help="Analysis depth level (default: standard)",
    )
    parser.add_argument(
        "--output",
        help="Output file path (default: stdout)",
    )

    args = parser.parse_args()

    scan = generate_scan(company=args.company, depth=args.depth)
    output = json.dumps(scan, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Competitive scan written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
