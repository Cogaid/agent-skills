#!/usr/bin/env python3
"""
Cold outreach email generator.

Usage:
    python outreach_generator.py --name "John" --company "Acme Inc" --role "VP Sales"
    python outreach_generator.py --trigger "funding" --template observation
    python outreach_generator.py --interactive

Output: Personalized cold outreach email
"""

import argparse
import json
import random


# Email templates
TEMPLATES = {
    "observation": {
        "name": "The Observation",
        "subject_templates": [
            "Noticed {observation_subject}",
            "Quick thought on {observation_subject}",
            "Re: {company}'s {observation_subject}"
        ],
        "body": """Hi {name},

{personalized_opening}

{pain_point_statement}

We've helped {social_proof_company} {social_proof_result}.

{cta}

{signature}"""
    },
    "trigger": {
        "name": "The Trigger Event",
        "subject_templates": [
            "Congrats on {trigger_event}",
            "Saw the news about {trigger_event}",
            "Re: {company}'s {trigger_event}"
        ],
        "body": """Hi {name},

{trigger_opening}

When {similar_companies} hit this stage, {common_challenge} usually becomes a priority.

We help {target_audience} {value_prop}.

{social_proof_line}

{cta}

{signature}"""
    },
    "mutual": {
        "name": "The Mutual Connection",
        "subject_templates": [
            "{mutual_connection} suggested we connect",
            "Introduction from {mutual_connection}",
            "{mutual_connection} mentioned you"
        ],
        "body": """Hi {name},

{mutual_connection} mentioned you might be interested in {topic}.

We've been helping them {mutual_result} at {mutual_company}.

They thought you might benefit from a similar approach at {company}.

{cta}

{signature}"""
    },
    "problem": {
        "name": "The Problem-Solution",
        "subject_templates": [
            "Quick question about {problem_area}",
            "Thought on {company}'s {problem_area}",
            "{problem_area} at {company}?"
        ],
        "body": """Hi {name},

{problem_question}

We work with {target_audience} who face this exact issue.

{solution_statement}

Example: We helped {social_proof_company} {social_proof_result}.

{cta}

{signature}"""
    },
    "value": {
        "name": "The Value-First",
        "subject_templates": [
            "{result} for {company}?",
            "How {similar_company} achieved {result}",
            "Quick idea for {company}"
        ],
        "body": """Hi {name},

{value_opening}

{insight_or_tip}

This is how {similar_company} {achieved_result}.

Would be happy to share how this could work for {company}.

{cta}

{signature}"""
    }
}

# Trigger event options
TRIGGERS = {
    "funding": {
        "event": "the recent funding round",
        "opening": "Saw the news about {company}'s funding - congrats!",
        "challenge": "scaling while maintaining efficiency"
    },
    "new_role": {
        "event": "your new role",
        "opening": "Congrats on joining {company} as {role}!",
        "challenge": "ramping up quickly and making an impact"
    },
    "hiring": {
        "event": "your team expansion",
        "opening": "Noticed {company} is hiring for {department}.",
        "challenge": "onboarding and enabling new team members"
    },
    "product_launch": {
        "event": "the new product launch",
        "opening": "Saw {company} just launched {product} - exciting!",
        "challenge": "driving adoption and measuring success"
    },
    "acquisition": {
        "event": "the acquisition news",
        "opening": "Saw the news about {company}'s acquisition - big move!",
        "challenge": "integration and maintaining momentum"
    }
}

# CTA options
CTAS = [
    "Worth a 15-minute chat?",
    "Would it make sense to connect?",
    "Open to a quick conversation?",
    "Interested in learning more?",
    "Can I share how this might work for {company}?",
    "Worth exploring further?"
]

# Pain points by role
PAIN_POINTS = {
    "sales": [
        "scaling outbound without sacrificing quality",
        "booking more meetings with less effort",
        "improving response rates on cold outreach"
    ],
    "marketing": [
        "generating more qualified leads",
        "proving ROI on marketing spend",
        "standing out in a crowded market"
    ],
    "engineering": [
        "shipping faster without breaking things",
        "managing technical debt while innovating",
        "keeping the team productive as you scale"
    ],
    "hr": [
        "hiring top talent in a competitive market",
        "retaining your best people",
        "building culture as you grow"
    ],
    "operations": [
        "doing more with the same resources",
        "eliminating manual processes",
        "maintaining quality while scaling"
    ],
    "default": [
        "scaling efficiently",
        "staying ahead of competition",
        "achieving more with limited resources"
    ]
}


def detect_role_category(role):
    """Detect role category from title."""
    role_lower = role.lower()

    if any(word in role_lower for word in ["sales", "revenue", "business development", "account"]):
        return "sales"
    elif any(word in role_lower for word in ["marketing", "growth", "demand", "content"]):
        return "marketing"
    elif any(word in role_lower for word in ["engineering", "technical", "developer", "cto"]):
        return "engineering"
    elif any(word in role_lower for word in ["hr", "people", "talent", "culture"]):
        return "hr"
    elif any(word in role_lower for word in ["operations", "ops", "coo", "process"]):
        return "operations"
    else:
        return "default"


def generate_outreach(
    name,
    company,
    role="",
    template_type="observation",
    trigger=None,
    observation="",
    mutual_connection="",
    product="",
    your_company="",
    your_name="",
    social_proof_company="",
    social_proof_result="",
    value_prop=""
):
    """Generate personalized outreach email."""

    template = TEMPLATES.get(template_type, TEMPLATES["observation"])

    # Detect role category for pain points
    role_category = detect_role_category(role) if role else "default"
    pain_points = PAIN_POINTS[role_category]

    # Build variables
    variables = {
        "name": name,
        "company": company,
        "role": role or "[Role]",
        "your_name": your_name or "[Your Name]",
        "your_company": your_company or "[Your Company]",
        "social_proof_company": social_proof_company or "[Similar Company]",
        "social_proof_result": social_proof_result or "[achieved specific result]",
        "value_prop": value_prop or "[your value proposition]",
        "target_audience": f"{role_category} teams" if role_category != "default" else "growing companies",
        "cta": random.choice(CTAS).format(company=company),
        "signature": your_name or "[Your Name]"
    }

    # Template-specific variables
    if template_type == "observation":
        variables["observation_subject"] = observation or f"[specific observation about {company}]"
        variables["personalized_opening"] = f"I noticed {observation or '[your specific observation]'}." if observation else f"[Your personalized observation about {company}]"
        variables["pain_point_statement"] = f"{company}'s {role_category} team might be dealing with {random.choice(pain_points)}."

    elif template_type == "trigger" and trigger:
        trigger_info = TRIGGERS.get(trigger, TRIGGERS["funding"])
        variables["trigger_event"] = trigger_info["event"]
        variables["trigger_opening"] = trigger_info["opening"].format(**variables)
        variables["common_challenge"] = trigger_info["challenge"]
        variables["similar_companies"] = f"companies like {company}"
        variables["social_proof_line"] = f"We recently helped {variables['social_proof_company']} {variables['social_proof_result']}."

    elif template_type == "mutual":
        variables["mutual_connection"] = mutual_connection or "[Mutual Connection]"
        variables["topic"] = f"improving {random.choice(pain_points)}"
        variables["mutual_result"] = variables["social_proof_result"]
        variables["mutual_company"] = variables["social_proof_company"]

    elif template_type == "problem":
        pain = random.choice(pain_points)
        variables["problem_area"] = pain
        variables["problem_question"] = f"How are you currently handling {pain}?"
        variables["solution_statement"] = f"Our {product or 'solution'} helps {variables['target_audience']} {variables['value_prop']}."

    elif template_type == "value":
        variables["result"] = variables["social_proof_result"]
        variables["similar_company"] = variables["social_proof_company"]
        variables["value_opening"] = f"I've been researching {role_category} teams and found something interesting."
        variables["insight_or_tip"] = f"The best {variables['target_audience']} are {random.choice(['automating', 'optimizing', 'rethinking'])} how they approach {random.choice(pain_points)}."
        variables["achieved_result"] = variables["social_proof_result"]

    # Generate subject line
    subject_template = random.choice(template["subject_templates"])
    try:
        subject = subject_template.format(**variables)
    except KeyError:
        subject = f"Quick thought for {company}"

    # Generate body
    try:
        body = template["body"].format(**variables)
    except KeyError as e:
        body = f"[Template error: missing {e}]"

    return {
        "template": template["name"],
        "subject": subject,
        "body": body,
        "variables_used": variables
    }


def interactive_mode():
    """Interactive outreach generation."""

    print("\n" + "=" * 50)
    print("COLD OUTREACH GENERATOR")
    print("=" * 50)

    # Gather info
    name = input("\nProspect's first name: ").strip()
    company = input("Company name: ").strip()
    role = input("Role/title (optional): ").strip()

    print("\nTemplate types:")
    for i, (key, tmpl) in enumerate(TEMPLATES.items(), 1):
        print(f"  {i}. {tmpl['name']} ({key})")

    template_choice = input("\nSelect template (1-5) [1]: ").strip()
    template_types = list(TEMPLATES.keys())
    template_type = template_types[int(template_choice) - 1] if template_choice.isdigit() else "observation"

    trigger = None
    if template_type == "trigger":
        print("\nTrigger events:")
        for i, (key, t) in enumerate(TRIGGERS.items(), 1):
            print(f"  {i}. {key}: {t['event']}")
        trigger_choice = input("Select trigger (1-5): ").strip()
        trigger = list(TRIGGERS.keys())[int(trigger_choice) - 1] if trigger_choice.isdigit() else "funding"

    observation = ""
    if template_type == "observation":
        observation = input("\nSpecific observation about them (optional): ").strip()

    mutual = ""
    if template_type == "mutual":
        mutual = input("\nMutual connection's name: ").strip()

    # Optional fields
    your_name = input("\nYour name: ").strip()
    social_proof = input("Social proof company (optional): ").strip()
    social_result = input("What you helped them achieve (optional): ").strip()

    # Generate
    result = generate_outreach(
        name=name,
        company=company,
        role=role,
        template_type=template_type,
        trigger=trigger,
        observation=observation,
        mutual_connection=mutual,
        your_name=your_name,
        social_proof_company=social_proof,
        social_proof_result=social_result
    )

    print("\n" + "=" * 50)
    print("GENERATED EMAIL")
    print("=" * 50)
    print(f"\nSUBJECT: {result['subject']}")
    print("\n---")
    print(result['body'])
    print("---")

    return result


def format_output(result, format_type="text"):
    """Format output."""

    if format_type == "json":
        return json.dumps(result, indent=2)

    lines = []
    lines.append("\n" + "=" * 50)
    lines.append(f"Template: {result['template']}")
    lines.append("=" * 50)
    lines.append(f"\nSUBJECT: {result['subject']}")
    lines.append("\n" + "-" * 50)
    lines.append(result['body'])
    lines.append("-" * 50)

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description='Cold outreach email generator')
    parser.add_argument('--name', '-n', required=False, help="Prospect's first name")
    parser.add_argument('--company', '-c', required=False, help='Company name')
    parser.add_argument('--role', '-r', help='Role/title')
    parser.add_argument('--template', '-t', choices=list(TEMPLATES.keys()),
                        default='observation', help='Email template')
    parser.add_argument('--trigger', choices=list(TRIGGERS.keys()),
                        help='Trigger event (for trigger template)')
    parser.add_argument('--observation', '-o', help='Specific observation')
    parser.add_argument('--mutual', '-m', help='Mutual connection name')
    parser.add_argument('--your-name', help='Your name')
    parser.add_argument('--proof-company', help='Social proof company')
    parser.add_argument('--proof-result', help='Social proof result')
    parser.add_argument('--interactive', '-i', action='store_true',
                        help='Interactive mode')
    parser.add_argument('--format', '-f', choices=['json', 'text'],
                        default='text', help='Output format')
    parser.add_argument('--list', '-l', action='store_true',
                        help='List templates')

    args = parser.parse_args()

    if args.list:
        print("\nAvailable Templates:\n")
        for key, tmpl in TEMPLATES.items():
            print(f"  {key}: {tmpl['name']}")
        print("\nTrigger Events:\n")
        for key, trigger in TRIGGERS.items():
            print(f"  {key}: {trigger['event']}")
        return

    if args.interactive:
        interactive_mode()
        return

    if not args.name or not args.company:
        parser.print_help()
        return

    result = generate_outreach(
        name=args.name,
        company=args.company,
        role=args.role or "",
        template_type=args.template,
        trigger=args.trigger,
        observation=args.observation or "",
        mutual_connection=args.mutual or "",
        your_name=args.your_name or "",
        social_proof_company=args.proof_company or "",
        social_proof_result=args.proof_result or ""
    )

    print(format_output(result, args.format))


if __name__ == '__main__':
    main()
