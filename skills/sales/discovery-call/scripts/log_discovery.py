#!/usr/bin/env python3
"""
Log discovery call findings in structured format.

Usage:
    python log_discovery.py --company "Acme" --contact "John Doe" --interactive
    python log_discovery.py --company "Acme" --json findings.json

Output: Structured discovery notes in JSON or markdown
"""

import argparse
import json
import sys
from datetime import datetime


def interactive_discovery():
    """Interactive mode for logging discovery findings."""

    print("=== Discovery Call Logger ===\n")

    # Basic info
    company = input("Company name: ").strip()
    contact = input("Contact name and title: ").strip()
    duration = input("Call duration (minutes): ").strip()

    print("\n--- SITUATION ---")
    current_process = input("Current process/approach: ").strip()
    tools_used = input("Tools/systems they use: ").strip()
    team_structure = input("Team structure: ").strip()

    print("\n--- PROBLEMS (enter each, blank to finish) ---")
    problems = []
    while True:
        problem = input(f"Problem {len(problems)+1}: ").strip()
        if not problem:
            break
        quote = input("  Their exact words: ").strip()
        problems.append({"problem": problem, "quote": quote})

    print("\n--- IMPLICATIONS ---")
    business_impact = input("Business impact: ").strip()
    cost = input("Cost of problem (if discussed): ").strip()
    urgency = input("Urgency level (low/medium/high): ").strip()

    print("\n--- DESIRED STATE ---")
    future_state = input("What they want to achieve: ").strip()

    print("\n--- DECISION PROCESS ---")
    decision_makers = input("Decision makers: ").strip()
    timeline = input("Timeline: ").strip()
    budget = input("Budget status (confirmed/unknown/concern): ").strip()
    criteria = input("Evaluation criteria: ").strip()

    print("\n--- ASSESSMENT ---")
    fit = input("Fit (strong/moderate/weak): ").strip()
    probability = input("Win probability (%): ").strip()
    next_action = input("Next action: ").strip()

    return {
        "metadata": {
            "date": datetime.now().isoformat(),
            "company": company,
            "contact": contact,
            "duration_minutes": duration
        },
        "situation": {
            "current_process": current_process,
            "tools": tools_used,
            "team": team_structure
        },
        "problems": problems,
        "implications": {
            "business_impact": business_impact,
            "cost": cost,
            "urgency": urgency
        },
        "desired_state": future_state,
        "decision_process": {
            "decision_makers": decision_makers,
            "timeline": timeline,
            "budget": budget,
            "criteria": criteria
        },
        "assessment": {
            "fit": fit,
            "probability": probability,
            "next_action": next_action
        }
    }


def format_markdown(data: dict) -> str:
    """Format discovery data as markdown."""
    md = f"""# Discovery Notes: {data['metadata']['company']}

**Date**: {data['metadata']['date']}
**Contact**: {data['metadata']['contact']}
**Duration**: {data['metadata']['duration_minutes']} minutes

## Situation
- **Current Process**: {data['situation']['current_process']}
- **Tools**: {data['situation']['tools']}
- **Team**: {data['situation']['team']}

## Problems Identified
"""
    for i, p in enumerate(data['problems'], 1):
        md += f"\n{i}. **{p['problem']}**\n   > \"{p['quote']}\"\n"

    md += f"""
## Implications
- **Business Impact**: {data['implications']['business_impact']}
- **Cost**: {data['implications']['cost']}
- **Urgency**: {data['implications']['urgency']}

## Desired Future State
{data['desired_state']}

## Decision Process
- **Decision Makers**: {data['decision_process']['decision_makers']}
- **Timeline**: {data['decision_process']['timeline']}
- **Budget**: {data['decision_process']['budget']}
- **Criteria**: {data['decision_process']['criteria']}

## Assessment
- **Fit**: {data['assessment']['fit']}
- **Probability**: {data['assessment']['probability']}%
- **Next Action**: {data['assessment']['next_action']}
"""
    return md


def main():
    parser = argparse.ArgumentParser(description="Log discovery call")
    parser.add_argument("--company", "-c", help="Company name")
    parser.add_argument("--contact", help="Contact name")
    parser.add_argument("--interactive", "-i", action="store_true",
                        help="Interactive mode")
    parser.add_argument("--json", help="Load from JSON file")
    parser.add_argument("--output", "-o", help="Output file")
    parser.add_argument("--format", "-f", choices=["json", "markdown"],
                        default="json", help="Output format")

    args = parser.parse_args()

    if args.interactive:
        data = interactive_discovery()
    elif args.json:
        with open(args.json, 'r') as f:
            data = json.load(f)
    else:
        parser.print_help()
        sys.exit(1)

    # Format output
    if args.format == "markdown":
        output = format_markdown(data)
    else:
        output = json.dumps(data, indent=2)

    # Write output
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
        print(f"Saved to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
