#!/usr/bin/env python3
"""
Generate newsletter structure and content framework.

Usage:
    python newsletter_builder.py --type weekly --topic "AI Updates"
    python newsletter_builder.py --type promotional --offer "50% off"
    python newsletter_builder.py --interactive

Output: Complete newsletter structure ready for customization
"""

import argparse
import json
from datetime import datetime


# Newsletter type configurations
NEWSLETTER_TYPES = {
    "weekly": {
        "name": "Weekly Digest",
        "sections": ["opening_hook", "top_story", "curated_links", "quick_tip", "action_item", "closing"],
        "tone": "informative and friendly",
        "length": "medium (500-800 words)",
        "cta_style": "soft"
    },
    "product": {
        "name": "Product Update",
        "sections": ["announcement", "feature_details", "benefits", "how_to", "whats_next", "closing"],
        "tone": "excited and helpful",
        "length": "short (300-500 words)",
        "cta_style": "action-oriented"
    },
    "educational": {
        "name": "Educational",
        "sections": ["hook", "problem_statement", "step_by_step", "key_takeaways", "next_step", "closing"],
        "tone": "authoritative and approachable",
        "length": "long (800-1200 words)",
        "cta_style": "value-driven"
    },
    "promotional": {
        "name": "Promotional",
        "sections": ["hook", "offer_details", "benefits", "social_proof", "urgency", "cta", "faq"],
        "tone": "urgent and persuasive",
        "length": "short (300-500 words)",
        "cta_style": "urgent"
    },
    "personal": {
        "name": "Personal/Story",
        "sections": ["story_opening", "narrative", "lesson", "application", "ask", "closing"],
        "tone": "conversational and vulnerable",
        "length": "medium (500-700 words)",
        "cta_style": "soft"
    },
    "curated": {
        "name": "Curated Content",
        "sections": ["intro", "must_read", "also_worth", "media_pick", "personal_thought", "closing"],
        "tone": "helpful and opinionated",
        "length": "medium (500-800 words)",
        "cta_style": "engagement"
    },
    "welcome": {
        "name": "Welcome Email",
        "sections": ["greeting", "expectations", "gift", "about_me", "whitelist_ask", "engagement_question"],
        "tone": "warm and welcoming",
        "length": "short (300-400 words)",
        "cta_style": "relationship-building"
    },
    "reengagement": {
        "name": "Re-engagement",
        "sections": ["acknowledgment", "value_reminder", "missed_content", "preference_option", "final_ask"],
        "tone": "understanding and non-pushy",
        "length": "short (200-300 words)",
        "cta_style": "choice-based"
    }
}

# Section templates
SECTION_TEMPLATES = {
    "opening_hook": {
        "description": "Grab attention with timely observation or question",
        "template": """Hey {name},

{hook_content}

Here's what's inside this week:"""
    },
    "top_story": {
        "description": "Main story or insight of the newsletter",
        "template": """TOP STORY

{headline}

{summary_2_3_sentences}

[Read more]"""
    },
    "curated_links": {
        "description": "3-5 curated links with descriptions",
        "template": """WORTH YOUR TIME

1. {title_1}
   {description_1}
   [Link]

2. {title_2}
   {description_2}
   [Link]

3. {title_3}
   {description_3}
   [Link]"""
    },
    "quick_tip": {
        "description": "Brief actionable tip",
        "template": """QUICK TIP

{tip_content}"""
    },
    "action_item": {
        "description": "Single clear action with CTA",
        "template": """YOUR ACTION ITEM

{action_description}

[CTA Button: {cta_text}]"""
    },
    "announcement": {
        "description": "Feature or product announcement",
        "template": """INTRODUCING: {feature_name}

{what_it_is_and_why_it_matters}

[Screenshot or GIF]"""
    },
    "feature_details": {
        "description": "What the feature does",
        "template": """HERE'S WHAT YOU CAN DO:

- {capability_1} - {benefit_1}
- {capability_2} - {benefit_2}
- {capability_3} - {benefit_3}"""
    },
    "benefits": {
        "description": "Key benefits list",
        "template": """WHY YOU'LL LOVE IT:

- {benefit_1}
- {benefit_2}
- {benefit_3}"""
    },
    "how_to": {
        "description": "Getting started steps",
        "template": """HOW TO GET STARTED:

1. {step_1}
2. {step_2}
3. {step_3}"""
    },
    "hook": {
        "description": "Opening hook - problem or desire",
        "template": """{name},

{problem_or_desire_statement}

Today, I'm sharing exactly how to {outcome}."""
    },
    "step_by_step": {
        "description": "Detailed process steps",
        "template": """THE {number}-STEP PROCESS

STEP 1: {action_1}

{explanation_1}

Pro tip: {tip_1}

STEP 2: {action_2}

{explanation_2}

Common mistake: {mistake_2}

STEP 3: {action_3}

{explanation_3}"""
    },
    "key_takeaways": {
        "description": "Summary of main points",
        "template": """KEY TAKEAWAYS:

- {takeaway_1}
- {takeaway_2}
- {takeaway_3}"""
    },
    "offer_details": {
        "description": "Promotional offer details",
        "template": """{offer_name}

{offer_description}

WHAT YOU GET:
- {item_1} (Value: ${value_1})
- {item_2} (Value: ${value_2})
- {item_3} (Value: ${value_3})

Total Value: ${total_value}
Your Price: ${price}"""
    },
    "urgency": {
        "description": "Create urgency",
        "template": """DEADLINE: {deadline}

{urgency_reason}"""
    },
    "social_proof": {
        "description": "Testimonials or proof",
        "template": """WHAT OTHERS ARE SAYING:

"{testimonial}"
- {customer_name}, {customer_title}"""
    },
    "story_opening": {
        "description": "Personal story hook",
        "template": """Hey {name},

{vulnerable_relatable_moment}"""
    },
    "narrative": {
        "description": "Story continuation",
        "template": """{story_continuation_with_tension}

{turning_point}"""
    },
    "lesson": {
        "description": "Key insight or lesson",
        "template": """Here's what I realized:

{key_insight}"""
    },
    "application": {
        "description": "How it applies to reader",
        "template": """This matters for you because:

{reader_application}"""
    },
    "closing": {
        "description": "Sign-off",
        "template": """Until next time,
{signature}

P.S. {ps_content}"""
    }
}


def generate_newsletter_structure(newsletter_type, topic=None, name="[Name]", **kwargs):
    """Generate newsletter structure."""

    if newsletter_type not in NEWSLETTER_TYPES:
        return {"error": f"Unknown type. Available: {', '.join(NEWSLETTER_TYPES.keys())}"}

    config = NEWSLETTER_TYPES[newsletter_type]

    structure = {
        "type": config["name"],
        "topic": topic or "[Your Topic]",
        "tone": config["tone"],
        "recommended_length": config["length"],
        "cta_style": config["cta_style"],
        "subject_line_suggestions": generate_subject_lines(newsletter_type, topic),
        "preheader_suggestions": generate_preheaders(newsletter_type, topic),
        "sections": []
    }

    for section_name in config["sections"]:
        section = {
            "name": section_name.replace("_", " ").title(),
            "description": SECTION_TEMPLATES.get(section_name, {}).get(
                "description", "Content section"
            ),
            "template": SECTION_TEMPLATES.get(section_name, {}).get(
                "template", f"[{section_name} content]"
            )
        }
        structure["sections"].append(section)

    # Add footer
    structure["footer"] = {
        "required_elements": [
            "Unsubscribe link",
            "Physical address (CAN-SPAM)",
            "Social media links (optional)",
            "Preference center link (optional)"
        ]
    }

    return structure


def generate_subject_lines(newsletter_type, topic=None):
    """Generate subject line suggestions."""

    topic = topic or "[Topic]"

    suggestions = {
        "weekly": [
            f"Your {topic} Weekly: [Key Highlight]",
            f"This week in {topic}: [Number] things you need to know",
            f"[Name], here's your weekly {topic} roundup",
            f"The {topic} update you've been waiting for",
            f"[Number] {topic} insights for this week"
        ],
        "product": [
            f"New: [Feature] makes [task] easier",
            f"Introducing [Feature] - [benefit]",
            f"You asked, we built it: [Feature]",
            f"[Product] just got better",
            f"See what's new in [Product]"
        ],
        "educational": [
            f"How to [achieve result] (step-by-step)",
            f"The [number]-step process to [outcome]",
            f"[Name], here's how to [benefit]",
            f"What I learned about {topic}",
            f"The complete guide to [topic]"
        ],
        "promotional": [
            f"[X]% off ends [timeframe]",
            f"Last chance: [Offer name]",
            f"Don't miss this: [benefit]",
            f"[Name], your exclusive offer inside",
            f"[Hours/Days] left to save"
        ],
        "personal": [
            f"Can I be honest with you?",
            f"I made a mistake",
            f"Something I've never shared",
            f"A personal note about {topic}",
            f"What [experience] taught me"
        ],
        "curated": [
            f"[Number] {topic} links you shouldn't miss",
            f"Your {topic} reading list",
            f"The best of {topic} this week",
            f"I read [X] {topic} articles so you don't have to",
            f"Hand-picked {topic} resources"
        ],
        "welcome": [
            f"Welcome! Here's what to expect",
            f"You're in! Let's get started",
            f"Welcome to [Newsletter Name]",
            f"[Name], welcome to the community",
            f"Your first [resource] is inside"
        ],
        "reengagement": [
            f"We miss you, [Name]",
            f"Is this goodbye?",
            f"[Name], are you still there?",
            f"Should we break up?",
            f"One last thing before you go"
        ]
    }

    return suggestions.get(newsletter_type, suggestions["weekly"])


def generate_preheaders(newsletter_type, topic=None):
    """Generate preheader suggestions."""

    topic = topic or "[Topic]"

    suggestions = {
        "weekly": [
            f"Plus [number] more {topic} updates...",
            f"This week's top {topic} insights inside",
            f"Your weekly dose of {topic} wisdom"
        ],
        "product": [
            f"See what's new in [Product]",
            f"Your workflow just got easier",
            f"The feature you've been asking for"
        ],
        "educational": [
            f"The exact process I use for [outcome]",
            f"Step-by-step guide inside",
            f"Learn how to [benefit] today"
        ],
        "promotional": [
            f"[Specific benefit] + [deadline]",
            f"Save [amount] before [time]",
            f"This offer won't last"
        ],
        "personal": [
            f"[Intriguing continuation]...",
            f"I've been meaning to tell you this",
            f"A story I've never shared"
        ],
        "curated": [
            f"Hand-picked by [Name]",
            f"The best {topic} content this week",
            f"[Number] must-read articles"
        ],
        "welcome": [
            f"Your first [resource] is inside",
            f"Let's make this official",
            f"Here's what happens next"
        ],
        "reengagement": [
            f"Is this the end?",
            f"We'd love to have you back",
            f"Here's what you've missed"
        ]
    }

    return suggestions.get(newsletter_type, suggestions["weekly"])


def generate_full_draft(newsletter_type, topic, name="[Name]", **kwargs):
    """Generate a full newsletter draft."""

    structure = generate_newsletter_structure(newsletter_type, topic, name, **kwargs)

    if "error" in structure:
        return structure

    draft_lines = []
    draft_lines.append(f"SUBJECT: {structure['subject_line_suggestions'][0]}")
    draft_lines.append(f"PREHEADER: {structure['preheader_suggestions'][0]}")
    draft_lines.append("")
    draft_lines.append("---")
    draft_lines.append("")

    for section in structure["sections"]:
        draft_lines.append(f"[{section['name'].upper()}]")
        draft_lines.append(f"# {section['description']}")
        draft_lines.append("")
        template = section["template"].replace("{name}", name)
        draft_lines.append(template)
        draft_lines.append("")
        draft_lines.append("---")
        draft_lines.append("")

    draft_lines.append("[FOOTER]")
    for element in structure["footer"]["required_elements"]:
        draft_lines.append(f"- {element}")

    return {
        "structure": structure,
        "draft": "\n".join(draft_lines)
    }


def interactive_mode():
    """Interactive newsletter builder."""

    print("\n=== Newsletter Builder ===\n")

    print("Available newsletter types:")
    for key, config in NEWSLETTER_TYPES.items():
        print(f"  {key}: {config['name']} ({config['length']})")

    newsletter_type = input("\nSelect type: ").strip().lower()
    if newsletter_type not in NEWSLETTER_TYPES:
        print(f"Invalid type. Using 'weekly'.")
        newsletter_type = "weekly"

    topic = input("Newsletter topic: ").strip() or None
    name = input("Recipient name placeholder [Name]: ").strip() or "[Name]"

    result = generate_full_draft(newsletter_type, topic, name)

    if "error" in result:
        print(f"\nError: {result['error']}")
        return

    print("\n" + "=" * 60)
    print("GENERATED NEWSLETTER STRUCTURE")
    print("=" * 60)

    print(f"\nType: {result['structure']['type']}")
    print(f"Topic: {result['structure']['topic']}")
    print(f"Tone: {result['structure']['tone']}")
    print(f"Length: {result['structure']['recommended_length']}")

    print("\n--- SUBJECT LINE OPTIONS ---")
    for i, subj in enumerate(result['structure']['subject_line_suggestions'], 1):
        print(f"  {i}. {subj}")

    print("\n--- PREHEADER OPTIONS ---")
    for i, pre in enumerate(result['structure']['preheader_suggestions'], 1):
        print(f"  {i}. {pre}")

    print("\n" + "=" * 60)
    print("DRAFT TEMPLATE")
    print("=" * 60)
    print(result["draft"])


def format_output(result, format_type="text"):
    """Format output."""

    if format_type == "json":
        return json.dumps(result, indent=2)

    if "error" in result:
        return f"Error: {result['error']}"

    lines = []
    lines.append("\n" + "=" * 60)
    lines.append("NEWSLETTER STRUCTURE")
    lines.append("=" * 60)

    structure = result.get("structure", result)

    lines.append(f"\nType: {structure['type']}")
    lines.append(f"Topic: {structure['topic']}")
    lines.append(f"Tone: {structure['tone']}")
    lines.append(f"Length: {structure['recommended_length']}")
    lines.append(f"CTA Style: {structure['cta_style']}")

    lines.append("\n--- SUBJECT LINES ---")
    for subj in structure['subject_line_suggestions']:
        lines.append(f"  - {subj}")

    lines.append("\n--- SECTIONS ---")
    for section in structure['sections']:
        lines.append(f"\n  [{section['name']}]")
        lines.append(f"  {section['description']}")

    if "draft" in result:
        lines.append("\n" + "=" * 60)
        lines.append("DRAFT TEMPLATE")
        lines.append("=" * 60)
        lines.append(result["draft"])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description='Generate newsletter structure')
    parser.add_argument('--type', '-t', choices=list(NEWSLETTER_TYPES.keys()),
                        default='weekly', help='Newsletter type')
    parser.add_argument('--topic', help='Newsletter topic')
    parser.add_argument('--name', default='[Name]', help='Recipient name placeholder')
    parser.add_argument('--draft', '-d', action='store_true',
                        help='Generate full draft template')
    parser.add_argument('--format', '-f', choices=['json', 'text'],
                        default='text', help='Output format')
    parser.add_argument('--interactive', '-i', action='store_true',
                        help='Interactive mode')
    parser.add_argument('--list', '-l', action='store_true',
                        help='List newsletter types')

    args = parser.parse_args()

    if args.list:
        print("\nNewsletter Types:\n")
        for key, config in NEWSLETTER_TYPES.items():
            print(f"  {key}:")
            print(f"    Name: {config['name']}")
            print(f"    Tone: {config['tone']}")
            print(f"    Length: {config['length']}")
            print(f"    Sections: {len(config['sections'])}")
            print()
        return

    if args.interactive:
        interactive_mode()
        return

    if args.draft:
        result = generate_full_draft(args.type, args.topic, args.name)
    else:
        result = generate_newsletter_structure(args.type, args.topic, args.name)

    print(format_output(result, args.format))


if __name__ == '__main__':
    main()
