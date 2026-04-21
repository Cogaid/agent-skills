#!/usr/bin/env python3
"""Generate a competitive battlecard from competitor data.

Creates a structured battlecard document with placeholder prompts for
sales enablement teams to fill in competitor intelligence.

Usage:
    python generate_battlecard.py --competitor "Acme Corp" --template full
    python generate_battlecard.py --competitor "Acme Corp" --template quick --format json
"""

import argparse
import json
import sys
from datetime import datetime


TEMPLATES = {
    "full": {
        "sections": [
            "competitor_snapshot",
            "positioning",
            "feature_comparison",
            "pricing_intelligence",
            "win_loss_summary",
            "objection_responses",
            "trap_questions",
            "landmines",
            "customer_references",
        ],
        "description": "Complete battlecard with all sections",
    },
    "quick": {
        "sections": [
            "competitor_snapshot",
            "positioning",
            "objection_responses",
            "trap_questions",
        ],
        "description": "Quick-reference card for live conversations",
    },
    "feature-only": {
        "sections": [
            "competitor_snapshot",
            "feature_comparison",
            "pricing_intelligence",
        ],
        "description": "Feature and pricing comparison only",
    },
}

SAMPLE_COMPETITOR_DATA = {
    "Acme Corp": {
        "name": "Acme Corp",
        "founded": 2015,
        "headquarters": "San Francisco, CA",
        "employees": 850,
        "revenue_estimate": "$120M ARR",
        "funding": "$200M Series D",
        "ceo": "Jane Smith",
        "target_market": "Mid-market and Enterprise",
        "key_verticals": ["SaaS", "Financial Services", "Healthcare"],
        "notable_customers": ["BigBank Inc", "HealthCo", "TechStart"],
        "strengths": [
            "Strong brand recognition",
            "Large customer base",
            "Mature integrations ecosystem",
        ],
        "weaknesses": [
            "Legacy architecture limits scalability",
            "Slow feature release cadence",
            "Complex pricing with hidden fees",
        ],
        "their_pitch": "The enterprise-grade platform trusted by 2,000+ companies.",
        "pricing": {
            "starter": "$49/user/month",
            "professional": "$99/user/month",
            "enterprise": "Custom (typically $149/user/month)",
        },
    },
    "BetaTools": {
        "name": "BetaTools",
        "founded": 2019,
        "headquarters": "Austin, TX",
        "employees": 200,
        "revenue_estimate": "$25M ARR",
        "funding": "$50M Series B",
        "ceo": "John Doe",
        "target_market": "SMB and Mid-market",
        "key_verticals": ["E-commerce", "Marketing", "Startups"],
        "notable_customers": ["ShopFast", "GrowthCo", "MarketPro"],
        "strengths": [
            "Modern UX and fast onboarding",
            "Aggressive pricing",
            "Strong self-serve motion",
        ],
        "weaknesses": [
            "Limited enterprise features",
            "Small customer success team",
            "Narrow integration set",
        ],
        "their_pitch": "The fastest way to get started. No enterprise bloat.",
        "pricing": {
            "starter": "$29/user/month",
            "professional": "$59/user/month",
            "enterprise": "$99/user/month",
        },
    },
}


def generate_section(section_name, competitor_data):
    """Generate a battlecard section with data and prompts."""
    generators = {
        "competitor_snapshot": generate_snapshot,
        "positioning": generate_positioning,
        "feature_comparison": generate_feature_comparison,
        "pricing_intelligence": generate_pricing,
        "win_loss_summary": generate_win_loss,
        "objection_responses": generate_objections,
        "trap_questions": generate_trap_questions,
        "landmines": generate_landmines,
        "customer_references": generate_references,
    }
    generator = generators.get(section_name)
    if generator:
        return generator(competitor_data)
    return {"section": section_name, "status": "template", "content": "Fill in this section."}


def generate_snapshot(data):
    return {
        "section": "competitor_snapshot",
        "company": data["name"],
        "founded": data["founded"],
        "headquarters": data["headquarters"],
        "employees": data["employees"],
        "revenue_estimate": data["revenue_estimate"],
        "funding": data["funding"],
        "ceo": data["ceo"],
        "target_market": data["target_market"],
        "key_verticals": data["key_verticals"],
        "notable_customers": data["notable_customers"],
        "strengths": data["strengths"],
        "weaknesses": data["weaknesses"],
        "their_pitch": data["their_pitch"],
    }


def generate_positioning(data):
    return {
        "section": "positioning",
        "their_positioning": data["their_pitch"],
        "our_counter_positioning": "[ACTION REQUIRED] Draft counter-positioning statement",
        "why_we_win": [
            "[ACTION REQUIRED] Differentiator 1",
            "[ACTION REQUIRED] Differentiator 2",
            "[ACTION REQUIRED] Differentiator 3",
        ],
        "why_we_lose": [
            {
                "reason": "[ACTION REQUIRED] Loss reason 1",
                "mitigation": "[ACTION REQUIRED] Mitigation strategy",
            },
            {
                "reason": "[ACTION REQUIRED] Loss reason 2",
                "mitigation": "[ACTION REQUIRED] Mitigation strategy",
            },
        ],
    }


def generate_feature_comparison(data):
    return {
        "section": "feature_comparison",
        "competitor": data["name"],
        "features": [
            {
                "area": "[Feature Area 1]",
                "us": "Full",
                "them": "Partial",
                "advantage": "Us",
                "notes": "[ACTION REQUIRED] Add detail",
            },
            {
                "area": "[Feature Area 2]",
                "us": "Full",
                "them": "Full",
                "advantage": "Tie",
                "notes": "[ACTION REQUIRED] Add detail",
            },
            {
                "area": "[Feature Area 3]",
                "us": "Partial",
                "them": "Full",
                "advantage": "Them",
                "notes": "[ACTION REQUIRED] Add detail",
            },
        ],
        "summary": {
            "us_leading": "[COUNT]",
            "tied": "[COUNT]",
            "them_leading": "[COUNT]",
        },
        "instructions": "Add all relevant feature areas. Minimum 8-10 features for a complete comparison.",
    }


def generate_pricing(data):
    return {
        "section": "pricing_intelligence",
        "competitor": data["name"],
        "confidence_level": "Medium",
        "source": "[ACTION REQUIRED] Add source (G2, direct quote, customer intel)",
        "their_pricing": data["pricing"],
        "our_pricing": {
            "starter": "[ACTION REQUIRED] Our starter price",
            "professional": "[ACTION REQUIRED] Our professional price",
            "enterprise": "[ACTION REQUIRED] Our enterprise price",
        },
        "their_tactics": [
            "[ACTION REQUIRED] Pricing tactic 1 (e.g., first-year discount)",
            "[ACTION REQUIRED] Pricing tactic 2 (e.g., hidden fees)",
            "[ACTION REQUIRED] Pricing tactic 3 (e.g., per-seat scaling)",
        ],
        "our_response": {
            "if_undercut": "[ACTION REQUIRED] Response when they undercut",
            "if_bundled": "[ACTION REQUIRED] Response when they bundle",
            "tco_argument": "[ACTION REQUIRED] TCO talking point",
        },
    }


def generate_win_loss(data):
    return {
        "section": "win_loss_summary",
        "competitor": data["name"],
        "period": "Last 6 months",
        "results": {
            "total_opportunities": "[ACTION REQUIRED] Pull from CRM",
            "wins": "[COUNT]",
            "losses": "[COUNT]",
            "no_decision": "[COUNT]",
            "win_rate": "[PERCENTAGE]",
        },
        "win_themes": [
            "[ACTION REQUIRED] Theme 1 - frequency and example",
            "[ACTION REQUIRED] Theme 2 - frequency and example",
            "[ACTION REQUIRED] Theme 3 - frequency and example",
        ],
        "loss_themes": [
            "[ACTION REQUIRED] Theme 1 - frequency and mitigation",
            "[ACTION REQUIRED] Theme 2 - frequency and mitigation",
            "[ACTION REQUIRED] Theme 3 - frequency and mitigation",
        ],
        "instructions": "Pull data from CRM. Interview 3+ reps for qualitative themes.",
    }


def generate_objections(data):
    return {
        "section": "objection_responses",
        "competitor": data["name"],
        "objections": [
            {
                "objection": f"{data['name']} has [FEATURE] and you don't.",
                "response": "[ACTION REQUIRED] Draft response using LAER framework",
                "proof_point": "[ACTION REQUIRED] Add customer example or data",
            },
            {
                "objection": f"{data['name']} is cheaper.",
                "response": "[ACTION REQUIRED] Draft TCO-based response",
                "proof_point": "[ACTION REQUIRED] Add TCO comparison data",
            },
            {
                "objection": f"We are already using {data['name']}.",
                "response": "[ACTION REQUIRED] Draft switch/displacement response",
                "proof_point": "[ACTION REQUIRED] Add customer switch story",
            },
            {
                "objection": f"{data['name']} is the market leader.",
                "response": "[ACTION REQUIRED] Draft market position response",
                "proof_point": "[ACTION REQUIRED] Add growth data or analyst ranking",
            },
            {
                "objection": f"I've heard {data['name']} is easier to use.",
                "response": "[ACTION REQUIRED] Draft UX/time-to-value response",
                "proof_point": "[ACTION REQUIRED] Add G2 ratings or onboarding data",
            },
        ],
        "instructions": "Use LAER framework: Listen, Acknowledge, Explore, Respond. Always include a proof point.",
    }


def generate_trap_questions(data):
    weaknesses = data.get("weaknesses", [])
    return {
        "section": "trap_questions",
        "competitor": data["name"],
        "known_weaknesses": weaknesses,
        "questions": [
            {
                "question": "[ACTION REQUIRED] Question exposing weakness 1",
                "leads_to": "[ACTION REQUIRED] What this reveals",
                "when_to_ask": "During discovery",
            },
            {
                "question": "[ACTION REQUIRED] Question exposing weakness 2",
                "leads_to": "[ACTION REQUIRED] What this reveals",
                "when_to_ask": "During evaluation",
            },
            {
                "question": "[ACTION REQUIRED] Question about implementation timeline",
                "leads_to": "Their implementation takes longer than ours",
                "when_to_ask": "During evaluation",
            },
            {
                "question": "[ACTION REQUIRED] Question about hidden costs",
                "leads_to": "Exposes fees not mentioned upfront",
                "when_to_ask": "During pricing discussion",
            },
            {
                "question": "[ACTION REQUIRED] Question about scale scenario",
                "leads_to": "Their architecture does not scale well",
                "when_to_ask": "During technical evaluation",
            },
        ],
        "instructions": "Frame as genuine curiosity about the prospect's needs. Never position as attacks.",
    }


def generate_landmines(data):
    return {
        "section": "landmines",
        "competitor": data["name"],
        "what_they_say_about_us": [
            {
                "their_claim": "[ACTION REQUIRED] Claim 1",
                "reality": "[ACTION REQUIRED] What's actually true",
                "our_response": "[ACTION REQUIRED] How to respond",
            },
            {
                "their_claim": "[ACTION REQUIRED] Claim 2",
                "reality": "[ACTION REQUIRED] What's actually true",
                "our_response": "[ACTION REQUIRED] How to respond",
            },
            {
                "their_claim": "[ACTION REQUIRED] Claim 3",
                "reality": "[ACTION REQUIRED] What's actually true",
                "our_response": "[ACTION REQUIRED] How to respond",
            },
        ],
        "instructions": "Gather from win/loss interviews and field reports. Update whenever new claims surface.",
    }


def generate_references(data):
    return {
        "section": "customer_references",
        "competitor": data["name"],
        "win_stories": [
            {
                "customer": "[ACTION REQUIRED] Customer name",
                "industry": "[INDUSTRY]",
                "deal_size": "[AMOUNT]",
                "why_they_chose_us": "[ACTION REQUIRED] Key decision factors",
                "quote": "[ACTION REQUIRED] Customer quote",
                "result": "[ACTION REQUIRED] Measurable outcome",
            },
            {
                "customer": "[ACTION REQUIRED] Customer name",
                "industry": "[INDUSTRY]",
                "deal_size": "[AMOUNT]",
                "why_they_chose_us": "[ACTION REQUIRED] Key decision factors",
                "quote": "[ACTION REQUIRED] Customer quote",
                "result": "[ACTION REQUIRED] Measurable outcome",
            },
        ],
        "instructions": "Collect from customer success team. Need minimum 2-3 win stories per competitor.",
    }


def format_markdown(battlecard):
    """Format battlecard data as markdown."""
    lines = []
    lines.append(f"# Competitive Battlecard: {battlecard['competitor']}")
    lines.append(f"Generated: {battlecard['generated']}")
    lines.append(f"Template: {battlecard['template']}")
    lines.append("")

    for section in battlecard["sections"]:
        section_name = section.get("section", "Unknown")
        lines.append(f"## {section_name.replace('_', ' ').title()}")
        lines.append("")
        for key, value in section.items():
            if key == "section":
                continue
            if isinstance(value, list):
                lines.append(f"### {key.replace('_', ' ').title()}")
                for item in value:
                    if isinstance(item, dict):
                        for k, v in item.items():
                            lines.append(f"  - **{k}**: {v}")
                        lines.append("")
                    else:
                        lines.append(f"  - {item}")
                lines.append("")
            elif isinstance(value, dict):
                lines.append(f"### {key.replace('_', ' ').title()}")
                for k, v in value.items():
                    lines.append(f"  - **{k}**: {v}")
                lines.append("")
            else:
                lines.append(f"**{key.replace('_', ' ').title()}**: {value}")
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Generate a competitive battlecard from competitor data.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_battlecard.py --competitor "Acme Corp" --template full
  python generate_battlecard.py --competitor "BetaTools" --template quick --format json
  python generate_battlecard.py --list-templates
  python generate_battlecard.py --list-competitors
        """,
    )
    parser.add_argument(
        "--competitor",
        type=str,
        help="Name of the competitor to generate a battlecard for",
    )
    parser.add_argument(
        "--template",
        type=str,
        choices=list(TEMPLATES.keys()),
        default="full",
        help="Battlecard template to use (default: full)",
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["json", "markdown"],
        default="json",
        help="Output format (default: json)",
    )
    parser.add_argument(
        "--list-templates",
        action="store_true",
        help="List available templates and exit",
    )
    parser.add_argument(
        "--list-competitors",
        action="store_true",
        help="List sample competitors with data and exit",
    )

    args = parser.parse_args()

    if args.list_templates:
        print(json.dumps(TEMPLATES, indent=2))
        return

    if args.list_competitors:
        competitors = {name: {"name": d["name"], "revenue": d["revenue_estimate"]}
                      for name, d in SAMPLE_COMPETITOR_DATA.items()}
        print(json.dumps(competitors, indent=2))
        return

    if not args.competitor:
        parser.error("--competitor is required (use --list-competitors to see available sample data)")

    # Look up competitor data
    competitor_data = SAMPLE_COMPETITOR_DATA.get(args.competitor)
    if not competitor_data:
        # Generate a skeleton for unknown competitors
        competitor_data = {
            "name": args.competitor,
            "founded": "[ACTION REQUIRED]",
            "headquarters": "[ACTION REQUIRED]",
            "employees": "[ACTION REQUIRED]",
            "revenue_estimate": "[ACTION REQUIRED]",
            "funding": "[ACTION REQUIRED]",
            "ceo": "[ACTION REQUIRED]",
            "target_market": "[ACTION REQUIRED]",
            "key_verticals": ["[ACTION REQUIRED]"],
            "notable_customers": ["[ACTION REQUIRED]"],
            "strengths": ["[ACTION REQUIRED]"],
            "weaknesses": ["[ACTION REQUIRED]"],
            "their_pitch": "[ACTION REQUIRED]",
            "pricing": {
                "starter": "[ACTION REQUIRED]",
                "professional": "[ACTION REQUIRED]",
                "enterprise": "[ACTION REQUIRED]",
            },
        }
        print(f"Note: No sample data for '{args.competitor}'. Generating skeleton with prompts.",
              file=sys.stderr)

    template = TEMPLATES[args.template]
    sections = []
    for section_name in template["sections"]:
        sections.append(generate_section(section_name, competitor_data))

    battlecard = {
        "competitor": args.competitor,
        "template": args.template,
        "generated": datetime.now().isoformat(),
        "sections": sections,
    }

    if args.format == "json":
        print(json.dumps(battlecard, indent=2))
    else:
        print(format_markdown(battlecard))


if __name__ == "__main__":
    main()
