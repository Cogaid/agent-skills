#!/usr/bin/env python3
"""
Generate proposal document from inputs.

Usage:
    python generate_proposal.py --company "Acme" --interactive
    python generate_proposal.py --company "Acme" --json inputs.json

Output: Markdown proposal document
"""

import argparse
import json
import sys
from datetime import datetime, timedelta


def interactive_input():
    """Gather proposal inputs interactively."""

    print("=== Proposal Generator ===\n")

    # Basic info
    print("--- PROSPECT INFORMATION ---")
    company = input("Company name: ").strip()
    contact = input("Primary contact name: ").strip()
    contact_title = input("Contact title: ").strip()

    # Situation
    print("\n--- THEIR SITUATION (from discovery) ---")
    challenge1 = input("Main challenge: ").strip()
    challenge2 = input("Second challenge: ").strip()
    impact = input("Business impact (quantified if possible): ").strip()

    # Desired outcomes
    print("\n--- DESIRED OUTCOMES ---")
    goal = input("Primary goal: ").strip()
    metric1 = input("Success metric 1: ").strip()
    metric2 = input("Success metric 2: ").strip()
    timeline = input("Their timeline: ").strip()

    # Solution
    print("\n--- YOUR SOLUTION ---")
    solution_summary = input("Solution summary (1-2 sentences): ").strip()
    deliverable1 = input("Key deliverable 1: ").strip()
    deliverable2 = input("Key deliverable 2: ").strip()
    deliverable3 = input("Key deliverable 3: ").strip()

    # Pricing
    print("\n--- PRICING ---")
    price = input("Total investment: $").strip()
    includes = input("What's included (comma-separated): ").strip()

    # ROI
    print("\n--- VALUE (optional, press Enter to skip) ---")
    current_cost = input("Their current annual cost: $").strip()
    expected_benefit = input("Expected annual benefit: $").strip()

    # Timeline
    print("\n--- IMPLEMENTATION ---")
    duration = input("Implementation duration (weeks): ").strip()

    # Proof
    print("\n--- SOCIAL PROOF (optional) ---")
    case_study_company = input("Reference company name: ").strip()
    case_study_result = input("Result achieved: ").strip()

    return {
        "company": company,
        "contact": contact,
        "contact_title": contact_title,
        "challenges": [challenge1, challenge2],
        "impact": impact,
        "goal": goal,
        "metrics": [metric1, metric2],
        "timeline": timeline,
        "solution": solution_summary,
        "deliverables": [deliverable1, deliverable2, deliverable3],
        "price": price,
        "includes": [i.strip() for i in includes.split(",")],
        "current_cost": current_cost,
        "expected_benefit": expected_benefit,
        "duration_weeks": duration,
        "case_study": {
            "company": case_study_company,
            "result": case_study_result
        } if case_study_company else None,
        "generated_date": datetime.now().strftime("%B %d, %Y")
    }


def generate_proposal(data):
    """Generate markdown proposal from data."""

    proposal = f"""# Proposal for {data['company']}

**Prepared for**: {data['contact']}, {data['contact_title']}
**Date**: {data['generated_date']}
**Prepared by**: [Your Name]

---

## Executive Summary

{data['company']} is currently facing challenges with {data['challenges'][0].lower()}{f' and {data["challenges"][1].lower()}' if data['challenges'][1] else ''}. This is resulting in {data['impact']}.

Your goal is to {data['goal']} by {data['timeline']}.

We propose {data['solution']}

**Expected Outcomes:**
- {data['metrics'][0]}
- {data['metrics'][1]}

**Investment:** ${data['price']}
**Timeline:** {data['duration_weeks']} weeks to full deployment

---

## Current Situation

Based on our conversations, {data['company']} is experiencing:

1. **{data['challenges'][0]}**
   - Impact: {data['impact']}

{f"2. **{data['challenges'][1]}**" if data['challenges'][1] else ""}

This is creating urgency to act now, with a target of {data['timeline']}.

---

## Desired Outcomes

**Primary Goal:** {data['goal']}

**Success Metrics:**

| Metric | Target | Timeline |
|--------|--------|----------|
| {data['metrics'][0]} | [Target] | {data['timeline']} |
| {data['metrics'][1]} | [Target] | {data['timeline']} |

---

## Proposed Solution

{data['solution']}

### Scope of Work

**What You'll Receive:**

"""

    for i, deliverable in enumerate(data['deliverables'], 1):
        if deliverable:
            proposal += f"{i}. {deliverable}\n"

    proposal += f"""
### What's Included

"""
    for item in data['includes']:
        if item:
            proposal += f"✓ {item}\n"

    proposal += """
### What's Not Included

- [Item 1 - available as add-on]
- [Item 2 - available as add-on]

---

## Why [Your Company]

"""

    if data.get('case_study') and data['case_study']['company']:
        proposal += f"""**Relevant Experience:**

> "{data['case_study']['result']}"
> — {data['case_study']['company']}

"""

    proposal += """**What Sets Us Apart:**
1. [Differentiator 1]
2. [Differentiator 2]
3. [Differentiator 3]

---

## Investment

"""

    proposal += f"""**Total Investment:** ${data['price']}

**What's Included:**
"""
    for item in data['includes']:
        if item:
            proposal += f"- {item}\n"

    # ROI section if data provided
    if data.get('current_cost') and data.get('expected_benefit'):
        try:
            current = float(data['current_cost'].replace(',', ''))
            benefit = float(data['expected_benefit'].replace(',', ''))
            investment = float(data['price'].replace(',', ''))
            roi = ((benefit - investment) / investment) * 100
            payback = investment / (benefit / 12)

            proposal += f"""
### Value Analysis

| Metric | Amount |
|--------|--------|
| Current Annual Cost | ${data['current_cost']} |
| Expected Annual Benefit | ${data['expected_benefit']} |
| Investment | ${data['price']} |
| **Payback Period** | **{payback:.0f} months** |
| **Year 1 ROI** | **{roi:.0f}%** |
"""
        except (ValueError, ZeroDivisionError):
            pass

    proposal += f"""
**Payment Terms:** [50% upfront, 50% on completion / Monthly / etc.]

---

## Timeline

**Implementation Duration:** {data['duration_weeks']} weeks

| Week | Phase | Deliverable |
|------|-------|-------------|
| 1-2 | Discovery & Setup | [Deliverable] |
| 3-4 | Implementation | [Deliverable] |
| 5-{data['duration_weeks']} | Optimization | [Final deliverable] |

**Assumptions:**
- {data['company']} provides [required resources]
- Decision made by [date]
- Kick-off within 1 week of agreement

---

## Next Steps

To proceed:

1. [ ] Review this proposal and share feedback
2. [ ] Schedule alignment call if needed
3. [ ] Sign agreement (attached)
4. [ ] Complete onboarding questionnaire

**Upon agreement:**
- Day 1: Kick-off call scheduled
- Week 1: {data['deliverables'][0] if data['deliverables'] else '[First deliverable]'}

**Questions?** Contact [Your Name] at [email] or [phone]

---

*This proposal is valid for 30 days from the date above.*
"""

    return proposal


def main():
    parser = argparse.ArgumentParser(description="Generate proposal")
    parser.add_argument("--company", "-c", help="Company name")
    parser.add_argument("--interactive", "-i", action="store_true",
                        help="Interactive mode")
    parser.add_argument("--json", help="Load inputs from JSON file")
    parser.add_argument("--output", "-o", help="Output file")

    args = parser.parse_args()

    if args.interactive:
        data = interactive_input()
    elif args.json:
        with open(args.json, 'r') as f:
            data = json.load(f)
    else:
        parser.print_help()
        sys.exit(1)

    proposal = generate_proposal(data)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(proposal)
        print(f"Proposal saved to {args.output}")
    else:
        print(proposal)


if __name__ == "__main__":
    main()
