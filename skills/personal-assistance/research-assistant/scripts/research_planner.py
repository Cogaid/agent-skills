#!/usr/bin/env python3
"""
Generate research plans and track research progress.

Usage:
    python research_planner.py --topic "market research for CRM software"
    python research_planner.py --type company --target "Acme Corp"
    python research_planner.py --interactive

Output: Structured research plan with sources and timeline
"""

import argparse
import json
from datetime import datetime, timedelta


# Research type configurations
RESEARCH_TYPES = {
    "quick": {
        "name": "Quick Scan",
        "duration_hours": 0.5,
        "min_sources": 3,
        "depth": "surface",
        "deliverable": "Key facts summary"
    },
    "standard": {
        "name": "Standard Research",
        "duration_hours": 2,
        "min_sources": 8,
        "depth": "moderate",
        "deliverable": "Summary report with analysis"
    },
    "deep": {
        "name": "Deep Dive",
        "duration_hours": 6,
        "min_sources": 15,
        "depth": "comprehensive",
        "deliverable": "Full research report"
    },
    "ongoing": {
        "name": "Ongoing Research",
        "duration_hours": 20,
        "min_sources": 25,
        "depth": "exhaustive",
        "deliverable": "Multi-part comprehensive report"
    }
}

# Research area templates
RESEARCH_AREAS = {
    "company": {
        "areas": [
            "Company background and history",
            "Leadership and key personnel",
            "Products and services",
            "Business model and financials",
            "Market position and competitors",
            "Recent news and developments"
        ],
        "sources": [
            "Company website",
            "LinkedIn company page",
            "Crunchbase/PitchBook",
            "News articles",
            "Industry reports",
            "SEC filings (if public)",
            "Glassdoor reviews"
        ]
    },
    "market": {
        "areas": [
            "Market definition and scope",
            "Market size and growth",
            "Key players and market share",
            "Market segments",
            "Industry trends",
            "Regulatory environment",
            "Future outlook"
        ],
        "sources": [
            "Industry reports (Gartner, Forrester, IBISWorld)",
            "Trade publications",
            "Government statistics",
            "Academic research",
            "News analysis",
            "Company reports"
        ]
    },
    "product": {
        "areas": [
            "Product features and capabilities",
            "Pricing and plans",
            "User reviews and ratings",
            "Pros and cons",
            "Competitive comparison",
            "Integration and compatibility",
            "Customer support"
        ],
        "sources": [
            "Product website",
            "G2/Capterra reviews",
            "Product Hunt",
            "User forums",
            "YouTube demos",
            "Expert reviews"
        ]
    },
    "topic": {
        "areas": [
            "Definition and background",
            "Key concepts",
            "Current state",
            "Different perspectives",
            "Recent developments",
            "Expert opinions",
            "Practical applications"
        ],
        "sources": [
            "Academic sources",
            "Expert articles",
            "Books/publications",
            "News coverage",
            "Industry analysis",
            "Case studies"
        ]
    },
    "decision": {
        "areas": [
            "Options identification",
            "Criteria definition",
            "Option evaluation",
            "Risk assessment",
            "Cost analysis",
            "Stakeholder considerations",
            "Recommendation"
        ],
        "sources": [
            "Expert opinions",
            "Comparison sites",
            "User reviews",
            "Case studies",
            "Industry best practices",
            "Cost calculators"
        ]
    }
}


def generate_research_plan(topic, research_type="standard", area_type="topic", target=None):
    """Generate a structured research plan."""

    config = RESEARCH_TYPES.get(research_type, RESEARCH_TYPES["standard"])
    area_config = RESEARCH_AREAS.get(area_type, RESEARCH_AREAS["topic"])

    plan = {
        "generated": datetime.now().isoformat(),
        "topic": topic,
        "target": target,
        "research_type": config["name"],
        "estimated_hours": config["duration_hours"],
        "minimum_sources": config["min_sources"],
        "depth": config["depth"],
        "deliverable": config["deliverable"],
        "research_question": generate_research_question(topic, area_type, target),
        "areas_to_investigate": area_config["areas"],
        "suggested_sources": area_config["sources"],
        "phases": generate_phases(config, area_config),
        "quality_checklist": [
            "Research question clearly answered",
            "Multiple sources consulted",
            "Sources properly documented",
            "Information is current",
            "Findings cross-verified",
            "Bias acknowledged",
            "Limitations stated",
            "Recommendations are actionable"
        ]
    }

    return plan


def generate_research_question(topic, area_type, target):
    """Generate the primary research question."""

    templates = {
        "company": f"What is the current state, market position, and outlook for {target or topic}?",
        "market": f"What is the size, structure, and trajectory of the {topic} market?",
        "product": f"How does {target or topic} compare to alternatives and what are its strengths/weaknesses?",
        "topic": f"What are the key facts, perspectives, and implications regarding {topic}?",
        "decision": f"What is the best option for {topic} based on defined criteria?"
    }

    return templates.get(area_type, templates["topic"])


def generate_phases(config, area_config):
    """Generate research phases with time allocation."""

    total_hours = config["duration_hours"]
    depth = config["depth"]

    if depth == "surface":
        phases = [
            {
                "phase": "1. Quick Search",
                "duration_percent": 60,
                "tasks": [
                    "Search key terms",
                    "Review top 3-5 sources",
                    "Extract key facts"
                ]
            },
            {
                "phase": "2. Verify & Document",
                "duration_percent": 25,
                "tasks": [
                    "Cross-check critical facts",
                    "Document sources",
                    "Note confidence level"
                ]
            },
            {
                "phase": "3. Summarize",
                "duration_percent": 15,
                "tasks": [
                    "Write key findings",
                    "List sources",
                    "Flag unknowns"
                ]
            }
        ]
    elif depth == "moderate":
        phases = [
            {
                "phase": "1. Planning",
                "duration_percent": 10,
                "tasks": [
                    "Clarify research question",
                    "Identify key areas",
                    "Plan source strategy"
                ]
            },
            {
                "phase": "2. Information Gathering",
                "duration_percent": 50,
                "tasks": [
                    "Search primary sources",
                    "Review secondary sources",
                    "Document all sources",
                    "Note conflicting info"
                ]
            },
            {
                "phase": "3. Analysis",
                "duration_percent": 25,
                "tasks": [
                    "Organize findings",
                    "Identify patterns",
                    "Evaluate source quality",
                    "Draw conclusions"
                ]
            },
            {
                "phase": "4. Reporting",
                "duration_percent": 15,
                "tasks": [
                    "Write summary",
                    "Document sources",
                    "Add recommendations"
                ]
            }
        ]
    else:  # comprehensive or exhaustive
        phases = [
            {
                "phase": "1. Research Design",
                "duration_percent": 10,
                "tasks": [
                    "Define scope and objectives",
                    "Create research framework",
                    "Map information landscape",
                    "Prioritize areas"
                ]
            },
            {
                "phase": "2. Primary Research",
                "duration_percent": 25,
                "tasks": [
                    "Official/authoritative sources",
                    "Original data sources",
                    "Expert sources",
                    "Document thoroughly"
                ]
            },
            {
                "phase": "3. Secondary Research",
                "duration_percent": 20,
                "tasks": [
                    "Analysis and commentary",
                    "News and media",
                    "Reviews and opinions",
                    "Aggregate findings"
                ]
            },
            {
                "phase": "4. Verification",
                "duration_percent": 10,
                "tasks": [
                    "Cross-reference facts",
                    "Resolve conflicts",
                    "Assess reliability",
                    "Fill gaps"
                ]
            },
            {
                "phase": "5. Analysis & Synthesis",
                "duration_percent": 20,
                "tasks": [
                    "Organize by theme",
                    "Identify patterns",
                    "Draw conclusions",
                    "Develop recommendations"
                ]
            },
            {
                "phase": "6. Reporting",
                "duration_percent": 15,
                "tasks": [
                    "Write comprehensive report",
                    "Executive summary",
                    "Source documentation",
                    "Appendices"
                ]
            }
        ]

    # Calculate actual hours
    for phase in phases:
        phase["estimated_hours"] = round(total_hours * phase["duration_percent"] / 100, 1)

    return phases


def export_plan(plan, format_type="json"):
    """Export research plan in specified format."""

    if format_type == "json":
        return json.dumps(plan, indent=2)

    elif format_type == "text":
        lines = []
        lines.append("\n" + "=" * 60)
        lines.append("RESEARCH PLAN")
        lines.append("=" * 60)

        lines.append(f"\nTopic: {plan['topic']}")
        if plan.get('target'):
            lines.append(f"Target: {plan['target']}")
        lines.append(f"Type: {plan['research_type']}")
        lines.append(f"Estimated Time: {plan['estimated_hours']} hours")
        lines.append(f"Minimum Sources: {plan['minimum_sources']}")

        lines.append(f"\n--- RESEARCH QUESTION ---")
        lines.append(plan['research_question'])

        lines.append(f"\n--- AREAS TO INVESTIGATE ---")
        for i, area in enumerate(plan['areas_to_investigate'], 1):
            lines.append(f"  {i}. {area}")

        lines.append(f"\n--- SUGGESTED SOURCES ---")
        for source in plan['suggested_sources']:
            lines.append(f"  • {source}")

        lines.append(f"\n--- PHASES ---")
        for phase in plan['phases']:
            lines.append(f"\n{phase['phase']} ({phase['estimated_hours']}h)")
            for task in phase['tasks']:
                lines.append(f"  [ ] {task}")

        lines.append(f"\n--- QUALITY CHECKLIST ---")
        for item in plan['quality_checklist']:
            lines.append(f"  [ ] {item}")

        return "\n".join(lines)

    elif format_type == "markdown":
        lines = []
        lines.append(f"# Research Plan: {plan['topic']}")
        lines.append(f"\n**Generated:** {plan['generated'][:10]}")
        lines.append(f"**Type:** {plan['research_type']}")
        lines.append(f"**Estimated Time:** {plan['estimated_hours']} hours")

        lines.append(f"\n## Research Question")
        lines.append(plan['research_question'])

        lines.append(f"\n## Areas to Investigate")
        for area in plan['areas_to_investigate']:
            lines.append(f"- [ ] {area}")

        lines.append(f"\n## Suggested Sources")
        for source in plan['suggested_sources']:
            lines.append(f"- {source}")

        lines.append(f"\n## Research Phases")
        for phase in plan['phases']:
            lines.append(f"\n### {phase['phase']} ({phase['estimated_hours']}h)")
            for task in phase['tasks']:
                lines.append(f"- [ ] {task}")

        return "\n".join(lines)

    return json.dumps(plan, indent=2)


def interactive_mode():
    """Interactive research planning mode."""

    print("\n=== Research Planner ===\n")

    # Get topic
    topic = input("What do you want to research? ").strip()

    # Get research type
    print("\nResearch types:")
    for key, config in RESEARCH_TYPES.items():
        print(f"  {key}: {config['name']} (~{config['duration_hours']}h)")
    research_type = input("\nSelect type [standard]: ").strip().lower() or "standard"

    # Get area type
    print("\nResearch area:")
    for key in RESEARCH_AREAS.keys():
        print(f"  {key}")
    area_type = input("\nSelect area [topic]: ").strip().lower() or "topic"

    # Get target if applicable
    target = None
    if area_type in ["company", "product"]:
        target = input(f"\nSpecific {area_type} to research: ").strip()

    # Generate plan
    plan = generate_research_plan(topic, research_type, area_type, target)

    # Display
    print(export_plan(plan, "text"))

    # Export option
    if input("\n\nExport to markdown? (y/n) [n]: ").strip().lower() == "y":
        print("\n" + export_plan(plan, "markdown"))


def main():
    parser = argparse.ArgumentParser(description='Generate research plans')
    parser.add_argument('--topic', '-t', help='Research topic')
    parser.add_argument('--type', '-y', choices=list(RESEARCH_TYPES.keys()),
                        default='standard', help='Research type/depth')
    parser.add_argument('--area', '-a', choices=list(RESEARCH_AREAS.keys()),
                        default='topic', help='Research area')
    parser.add_argument('--target', '-g', help='Specific target (company, product)')
    parser.add_argument('--format', '-f', choices=['json', 'text', 'markdown'],
                        default='text', help='Output format')
    parser.add_argument('--interactive', '-i', action='store_true',
                        help='Interactive mode')
    parser.add_argument('--list', '-l', action='store_true',
                        help='List research types')

    args = parser.parse_args()

    if args.list:
        print("\nResearch Types:")
        for key, config in RESEARCH_TYPES.items():
            print(f"\n  {key}: {config['name']}")
            print(f"    Duration: {config['duration_hours']} hours")
            print(f"    Min Sources: {config['min_sources']}")
            print(f"    Deliverable: {config['deliverable']}")
        return

    if args.interactive:
        interactive_mode()
        return

    if not args.topic:
        parser.print_help()
        return

    plan = generate_research_plan(args.topic, args.type, args.area, args.target)
    print(export_plan(plan, args.format))


if __name__ == '__main__':
    main()
