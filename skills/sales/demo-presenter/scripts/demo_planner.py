#!/usr/bin/env python3
"""
Generate customized demo plans based on audience and needs.

Usage:
    python demo_planner.py --audience executive --industry saas
    python demo_planner.py --interactive
    python demo_planner.py --template technical

Output: Customized demo plan with timing, talking points, and questions
"""

import argparse
import json
from datetime import datetime


# Demo templates by audience type
AUDIENCE_TEMPLATES = {
    "executive": {
        "duration": 25,
        "structure": [
            {"phase": "Opening", "duration": 3, "focus": "Strategic alignment"},
            {"phase": "Discovery", "duration": 2, "focus": "Confirm priorities"},
            {"phase": "Value Proposition", "duration": 5, "focus": "Business outcomes"},
            {"phase": "Platform Demo", "duration": 10, "focus": "High-level capabilities"},
            {"phase": "Social Proof", "duration": 2, "focus": "Similar company results"},
            {"phase": "Close", "duration": 3, "focus": "Next steps"}
        ],
        "key_messages": [
            "ROI and business impact",
            "Competitive advantage",
            "Speed to value",
            "Risk mitigation"
        ],
        "avoid": [
            "Technical deep-dives",
            "Feature-by-feature walkthrough",
            "Implementation details",
            "Pricing negotiations"
        ],
        "questions_to_ask": [
            "What's driving the timeline for this initiative?",
            "What does success look like 12 months from now?",
            "Who else is involved in this decision?",
            "What happens if nothing changes?"
        ]
    },
    "manager": {
        "duration": 35,
        "structure": [
            {"phase": "Opening", "duration": 5, "focus": "Team challenges"},
            {"phase": "Current State", "duration": 5, "focus": "Map current workflow"},
            {"phase": "Workflow Demo", "duration": 15, "focus": "Day-in-the-life"},
            {"phase": "Team Features", "duration": 5, "focus": "Management visibility"},
            {"phase": "Adoption", "duration": 3, "focus": "Training and support"},
            {"phase": "Close", "duration": 2, "focus": "Pilot or next steps"}
        ],
        "key_messages": [
            "Day-to-day efficiency gains",
            "Team adoption ease",
            "Real-time visibility",
            "Reduced manual work"
        ],
        "avoid": [
            "Architecture details",
            "Enterprise features they won't use",
            "Pricing discussions",
            "Implementation complexity"
        ],
        "questions_to_ask": [
            "What takes up most of your team's time right now?",
            "Where does your current process break down?",
            "What reports do you run manually?",
            "What concerns do you have about team adoption?"
        ]
    },
    "technical": {
        "duration": 50,
        "structure": [
            {"phase": "Opening", "duration": 5, "focus": "Technical requirements"},
            {"phase": "Architecture", "duration": 10, "focus": "Infrastructure overview"},
            {"phase": "Integration", "duration": 15, "focus": "API and connectors"},
            {"phase": "Security", "duration": 10, "focus": "Compliance and data"},
            {"phase": "Q&A", "duration": 8, "focus": "Technical deep-dive"},
            {"phase": "Close", "duration": 2, "focus": "POC or documentation"}
        ],
        "key_messages": [
            "Modern architecture",
            "API flexibility",
            "Security certifications",
            "Scalability"
        ],
        "avoid": [
            "Business case discussions",
            "Non-technical features",
            "High-level overviews only",
            "Glossing over limitations"
        ],
        "questions_to_ask": [
            "What's your current tech stack?",
            "What integrations are must-haves?",
            "What security requirements do you need to meet?",
            "What's your data residency requirement?"
        ]
    },
    "committee": {
        "duration": 45,
        "structure": [
            {"phase": "Opening", "duration": 5, "focus": "Stakeholder priorities"},
            {"phase": "Executive Overview", "duration": 8, "focus": "Business value"},
            {"phase": "Functional Demo", "duration": 15, "focus": "Key workflows"},
            {"phase": "Technical Overview", "duration": 8, "focus": "Security & integration"},
            {"phase": "Q&A", "duration": 6, "focus": "All stakeholder questions"},
            {"phase": "Close", "duration": 3, "focus": "Consensus and next steps"}
        ],
        "key_messages": [
            "Addresses all stakeholder needs",
            "Proven results",
            "Low risk implementation",
            "Strong support"
        ],
        "avoid": [
            "Ignoring any stakeholder",
            "Going too deep in one area",
            "Assuming alignment",
            "Rushing through sections"
        ],
        "questions_to_ask": [
            "What's each person most interested in seeing?",
            "What criteria will you use to evaluate?",
            "What concerns need to be addressed today?",
            "What's your decision timeline?"
        ]
    }
}

# Industry-specific content
INDUSTRY_CONTENT = {
    "saas": {
        "pain_points": ["churn", "onboarding time", "customer acquisition cost", "NRR"],
        "outcomes": ["reduced churn by 25%", "cut onboarding time 50%", "improved NRR 15%"],
        "competitors": ["existing solution", "in-house build", "manual processes"],
        "roi_metrics": ["time-to-value", "customer lifetime value", "support ticket reduction"]
    },
    "fintech": {
        "pain_points": ["compliance", "security concerns", "audit trails", "scalability"],
        "outcomes": ["passed SOC2 audit", "reduced compliance time 40%", "zero security incidents"],
        "competitors": ["legacy systems", "point solutions", "custom builds"],
        "roi_metrics": ["compliance cost reduction", "audit preparation time", "incident response time"]
    },
    "healthcare": {
        "pain_points": ["HIPAA compliance", "data silos", "care coordination", "patient experience"],
        "outcomes": ["achieved HIPAA compliance", "improved care coordination 30%", "higher patient satisfaction"],
        "competitors": ["legacy EMR", "manual processes", "point solutions"],
        "roi_metrics": ["patient outcomes", "operational efficiency", "compliance costs"]
    },
    "ecommerce": {
        "pain_points": ["cart abandonment", "inventory sync", "fulfillment speed", "customer retention"],
        "outcomes": ["reduced cart abandonment 35%", "improved fulfillment 50%", "increased AOV 20%"],
        "competitors": ["current platform", "multi-tool stack", "manual processes"],
        "roi_metrics": ["conversion rate", "average order value", "customer lifetime value"]
    },
    "default": {
        "pain_points": ["efficiency", "visibility", "collaboration", "growth"],
        "outcomes": ["improved efficiency 30%", "better visibility", "faster growth"],
        "competitors": ["current solution", "spreadsheets", "manual processes"],
        "roi_metrics": ["time savings", "cost reduction", "revenue impact"]
    }
}


def generate_demo_plan(audience, industry, company_info=None, priorities=None):
    """Generate a customized demo plan."""

    template = AUDIENCE_TEMPLATES.get(audience, AUDIENCE_TEMPLATES["manager"])
    industry_content = INDUSTRY_CONTENT.get(industry, INDUSTRY_CONTENT["default"])

    company = company_info or {
        "name": "[Company Name]",
        "industry": industry,
        "size": "[Company Size]"
    }

    plan = {
        "generated": datetime.now().isoformat(),
        "demo_type": audience,
        "total_duration": template["duration"],
        "company": company,
        "industry_context": industry_content,
        "structure": [],
        "preparation": {},
        "talking_points": {},
        "questions": template["questions_to_ask"],
        "key_messages": template["key_messages"],
        "avoid": template["avoid"]
    }

    # Build structure with timing
    for section in template["structure"]:
        plan["structure"].append({
            "phase": section["phase"],
            "duration_minutes": section["duration"],
            "focus": section["focus"],
            "talking_points": get_talking_points(section["phase"], industry_content, priorities)
        })

    # Add preparation checklist
    plan["preparation"] = {
        "research": [
            f"Review {company['name']} website and recent news",
            "Check LinkedIn profiles of attendees",
            "Identify industry-specific challenges",
            "Prepare relevant case study"
        ],
        "technical": [
            "Test demo environment",
            "Prepare relevant data/scenarios",
            "Clear browser and notifications",
            "Have backup plan ready"
        ],
        "materials": [
            "Customized slides (if using)",
            "Relevant case study",
            "ROI calculator or pricing",
            "Follow-up materials"
        ]
    }

    return plan


def get_talking_points(phase, industry_content, priorities=None):
    """Get phase-specific talking points."""

    points = {
        "Opening": [
            "Thank them for their time",
            "Confirm goals and agenda",
            "Ask what success looks like"
        ],
        "Discovery": [
            f"Explore pain points: {', '.join(industry_content['pain_points'][:2])}",
            "Understand current solution",
            "Identify decision timeline"
        ],
        "Value Proposition": [
            f"Address key pain: {industry_content['pain_points'][0]}",
            f"Share outcome: {industry_content['outcomes'][0]}",
            "Connect to their specific situation"
        ],
        "Platform Demo": [
            "Show relevant capabilities",
            "Use their language and scenarios",
            "Check for engagement every 5 min"
        ],
        "Workflow Demo": [
            "Map to their current process",
            "Show efficiency gains",
            "Demonstrate ease of use"
        ],
        "Social Proof": [
            f"Similar company achieved: {industry_content['outcomes'][0]}",
            "Reference relevant case study",
            "Share specific metrics"
        ],
        "Architecture": [
            "Cover infrastructure overview",
            "Explain data handling",
            "Address scalability"
        ],
        "Integration": [
            "Show API capabilities",
            "Demonstrate connectors",
            "Discuss data sync"
        ],
        "Security": [
            "Cover certifications",
            "Explain data protection",
            "Address compliance needs"
        ],
        "Close": [
            "Summarize value",
            "Address concerns",
            "Propose specific next step"
        ]
    }

    return points.get(phase, ["Customize based on conversation"])


def generate_checklist(plan):
    """Generate pre-demo checklist."""

    checklist = []
    checklist.append("PRE-DEMO CHECKLIST")
    checklist.append("=" * 40)

    checklist.append("\n24 Hours Before:")
    checklist.append("[ ] Confirm meeting with attendees")
    checklist.append("[ ] Review company research")
    checklist.append("[ ] Prepare demo environment")
    checklist.append("[ ] Customize talking points")

    checklist.append("\n1 Hour Before:")
    checklist.append("[ ] Test technology")
    checklist.append("[ ] Clear browser/notifications")
    checklist.append("[ ] Review attendee profiles")
    checklist.append("[ ] Have backup ready")

    checklist.append("\n5 Minutes Before:")
    checklist.append("[ ] Join early")
    checklist.append("[ ] Check audio/video")
    checklist.append("[ ] Have materials open")
    checklist.append("[ ] Take a breath")

    return "\n".join(checklist)


def export_plan(plan, format_type="json"):
    """Export demo plan in specified format."""

    if format_type == "json":
        return json.dumps(plan, indent=2)

    elif format_type == "text":
        lines = []
        lines.append("\n" + "=" * 50)
        lines.append("DEMO PLAN")
        lines.append("=" * 50)
        lines.append(f"\nType: {plan['demo_type'].upper()}")
        lines.append(f"Duration: {plan['total_duration']} minutes")
        lines.append(f"Company: {plan['company']['name']}")

        lines.append("\n--- STRUCTURE ---")
        for section in plan["structure"]:
            lines.append(f"\n[{section['duration_minutes']} min] {section['phase']}")
            lines.append(f"Focus: {section['focus']}")
            for point in section["talking_points"]:
                lines.append(f"  • {point}")

        lines.append("\n--- KEY MESSAGES ---")
        for msg in plan["key_messages"]:
            lines.append(f"  ✓ {msg}")

        lines.append("\n--- AVOID ---")
        for item in plan["avoid"]:
            lines.append(f"  ✗ {item}")

        lines.append("\n--- DISCOVERY QUESTIONS ---")
        for q in plan["questions"]:
            lines.append(f"  ? {q}")

        lines.append("\n--- PREPARATION ---")
        for category, items in plan["preparation"].items():
            lines.append(f"\n{category.upper()}:")
            for item in items:
                lines.append(f"  [ ] {item}")

        return "\n".join(lines)

    return json.dumps(plan, indent=2)


def interactive_mode():
    """Interactive demo planning mode."""

    print("\n=== Demo Planner ===\n")

    # Get audience type
    print("Audience types: executive, manager, technical, committee")
    audience = input("Select audience type [manager]: ").strip().lower() or "manager"

    # Get industry
    print("\nIndustries: saas, fintech, healthcare, ecommerce, default")
    industry = input("Select industry [default]: ").strip().lower() or "default"

    # Get company info
    print("\n--- Company Information ---")
    company_name = input("Company name: ").strip() or "[Company Name]"

    # Get priorities
    print("\nWhat are their top 1-2 priorities? (comma-separated)")
    priorities_input = input("Priorities: ").strip()
    priorities = [p.strip() for p in priorities_input.split(",")] if priorities_input else None

    # Generate plan
    company_info = {
        "name": company_name,
        "industry": industry
    }

    plan = generate_demo_plan(audience, industry, company_info, priorities)

    # Display plan
    print(export_plan(plan, "text"))

    # Show checklist
    print("\n")
    print(generate_checklist(plan))

    # Export option
    if input("\n\nExport to JSON? (y/n) [n]: ").strip().lower() == "y":
        filename = f"demo_plan_{company_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.json"
        print(f"\n{export_plan(plan, 'json')}")


def main():
    parser = argparse.ArgumentParser(description='Generate demo plans')
    parser.add_argument('--audience', '-a',
                        choices=['executive', 'manager', 'technical', 'committee'],
                        default='manager', help='Audience type')
    parser.add_argument('--industry', '-i',
                        default='default', help='Industry')
    parser.add_argument('--company', '-c', help='Company name')
    parser.add_argument('--format', '-f', choices=['json', 'text'],
                        default='text', help='Output format')
    parser.add_argument('--interactive', action='store_true',
                        help='Interactive mode')
    parser.add_argument('--list', '-l', action='store_true',
                        help='List audience templates')
    parser.add_argument('--checklist', action='store_true',
                        help='Show pre-demo checklist only')

    args = parser.parse_args()

    if args.list:
        print("\nAvailable Audience Templates:")
        for audience, template in AUDIENCE_TEMPLATES.items():
            print(f"\n  {audience.upper()}:")
            print(f"    Duration: {template['duration']} minutes")
            print(f"    Phases: {len(template['structure'])}")
            print(f"    Focus: {', '.join([s['focus'] for s in template['structure'][:3]])}...")
        return

    if args.checklist:
        plan = generate_demo_plan(args.audience, args.industry)
        print(generate_checklist(plan))
        return

    if args.interactive:
        interactive_mode()
        return

    # Generate plan
    company_info = {
        "name": args.company or "[Company Name]",
        "industry": args.industry
    }

    plan = generate_demo_plan(args.audience, args.industry, company_info)

    print(export_plan(plan, args.format))


if __name__ == '__main__':
    main()
