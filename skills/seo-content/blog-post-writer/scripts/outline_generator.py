#!/usr/bin/env python3
"""
Generate blog post outline from topic and type.

Usage:
    python outline_generator.py --topic "email marketing tips" --type listicle
    python outline_generator.py --topic "how to start a blog" --type how-to

Output: Structured outline ready for writing
"""

import argparse
import json
import sys


# Outline templates by content type
OUTLINE_TEMPLATES = {
    "how-to": {
        "sections": [
            {"type": "h1", "template": "How to {topic}: A Step-by-Step Guide"},
            {"type": "intro", "template": "Introduction (2-3 paragraphs)", "notes": [
                "Hook: Why this matters to the reader",
                "What they'll learn",
                "Who this is for"
            ]},
            {"type": "h2", "template": "What You'll Need", "notes": [
                "Prerequisites",
                "Tools/resources",
                "Time estimate"
            ]},
            {"type": "h2", "template": "Step 1: {action_1}", "notes": [
                "What to do",
                "Why it matters",
                "Pro tip or common mistake"
            ]},
            {"type": "h2", "template": "Step 2: {action_2}", "notes": ["Same structure"]},
            {"type": "h2", "template": "Step 3: {action_3}", "notes": ["Same structure"]},
            {"type": "h2", "template": "Step 4: {action_4}", "notes": ["Same structure"]},
            {"type": "h2", "template": "Step 5: {action_5}", "notes": ["Same structure"]},
            {"type": "h2", "template": "Common Mistakes to Avoid", "notes": [
                "Mistake 1 + solution",
                "Mistake 2 + solution",
                "Mistake 3 + solution"
            ]},
            {"type": "h2", "template": "Troubleshooting", "notes": [
                "Common problem 1 + fix",
                "Common problem 2 + fix"
            ]},
            {"type": "h2", "template": "Frequently Asked Questions", "notes": [
                "3-5 common questions",
                "Brief answers"
            ]},
            {"type": "h2", "template": "Conclusion", "notes": [
                "Recap key steps",
                "Encouragement",
                "Call to action"
            ]}
        ],
        "word_count": "1,500-2,500"
    },

    "listicle": {
        "sections": [
            {"type": "h1", "template": "[Number] Best {topic} in [Year]"},
            {"type": "intro", "template": "Introduction", "notes": [
                "Why this list matters",
                "How items were selected",
                "Quick overview"
            ]},
            {"type": "h2", "template": "Quick Comparison Table", "notes": [
                "Summary table of all items",
                "Key differentiators"
            ]},
            {"type": "h2", "template": "1. [Item Name]", "notes": [
                "What it is",
                "Key features",
                "Pros and cons",
                "Who it's best for"
            ]},
            {"type": "h2", "template": "2. [Item Name]", "notes": ["Same structure"]},
            {"type": "h2", "template": "3. [Item Name]", "notes": ["Same structure"]},
            {"type": "h2", "template": "4. [Item Name]", "notes": ["Same structure"]},
            {"type": "h2", "template": "5. [Item Name]", "notes": ["Same structure"]},
            {"type": "h2", "template": "How to Choose", "notes": [
                "Decision criteria",
                "Recommendations by use case"
            ]},
            {"type": "h2", "template": "Frequently Asked Questions", "notes": [
                "3-5 common questions"
            ]},
            {"type": "h2", "template": "Conclusion", "notes": [
                "Top recommendation",
                "Call to action"
            ]}
        ],
        "word_count": "2,000-4,000"
    },

    "guide": {
        "sections": [
            {"type": "h1", "template": "The Complete Guide to {topic}"},
            {"type": "toc", "template": "Table of Contents", "notes": ["Linked sections"]},
            {"type": "intro", "template": "Introduction", "notes": [
                "What this guide covers",
                "Who it's for",
                "How to use it"
            ]},
            {"type": "h2", "template": "What is {topic}?", "notes": [
                "Clear definition",
                "Key terminology",
                "Brief history if relevant"
            ]},
            {"type": "h2", "template": "Why {topic} Matters", "notes": [
                "Benefits",
                "Use cases",
                "Statistics/data"
            ]},
            {"type": "h2", "template": "How {topic} Works", "notes": [
                "Core principles",
                "Mechanisms",
                "Visual explanation"
            ]},
            {"type": "h2", "template": "Getting Started with {topic}", "notes": [
                "Prerequisites",
                "Step-by-step basics",
                "Beginner tips"
            ]},
            {"type": "h2", "template": "Best Practices", "notes": [
                "Do's and don'ts",
                "Expert tips",
                "Common approaches"
            ]},
            {"type": "h2", "template": "Advanced Strategies", "notes": [
                "Advanced techniques",
                "Pro tips",
                "Case examples"
            ]},
            {"type": "h2", "template": "Common Challenges", "notes": [
                "Typical problems",
                "Solutions",
                "Prevention tips"
            ]},
            {"type": "h2", "template": "Tools and Resources", "notes": [
                "Recommended tools",
                "Further reading",
                "Communities"
            ]},
            {"type": "h2", "template": "Frequently Asked Questions", "notes": [
                "5-10 common questions"
            ]},
            {"type": "h2", "template": "Conclusion", "notes": [
                "Key takeaways",
                "Next steps",
                "Call to action"
            ]}
        ],
        "word_count": "3,000-6,000"
    },

    "comparison": {
        "sections": [
            {"type": "h1", "template": "[Option A] vs [Option B]: Which is Best for {topic}?"},
            {"type": "intro", "template": "Introduction", "notes": [
                "The decision readers face",
                "What this comparison covers"
            ]},
            {"type": "h2", "template": "Quick Verdict", "notes": [
                "TL;DR recommendation",
                "When to choose each"
            ]},
            {"type": "h2", "template": "Comparison Table", "notes": [
                "Side-by-side features",
                "Pricing",
                "Ratings"
            ]},
            {"type": "h2", "template": "What is [Option A]?", "notes": [
                "Overview",
                "Key features",
                "Best for"
            ]},
            {"type": "h2", "template": "What is [Option B]?", "notes": ["Same structure"]},
            {"type": "h2", "template": "[Feature 1] Comparison", "notes": [
                "How each performs",
                "Winner for this criteria"
            ]},
            {"type": "h2", "template": "[Feature 2] Comparison", "notes": ["Same structure"]},
            {"type": "h2", "template": "Pricing Comparison", "notes": [
                "Price tiers",
                "Value analysis"
            ]},
            {"type": "h2", "template": "Pros and Cons", "notes": [
                "Option A pros/cons",
                "Option B pros/cons"
            ]},
            {"type": "h2", "template": "Which Should You Choose?", "notes": [
                "Recommendations by scenario",
                "Decision guide"
            ]},
            {"type": "h2", "template": "Frequently Asked Questions"},
            {"type": "h2", "template": "Final Verdict", "notes": [
                "Overall winner",
                "Context-specific recommendations"
            ]}
        ],
        "word_count": "2,000-3,500"
    },

    "tips": {
        "sections": [
            {"type": "h1", "template": "[Number] {topic} Tips That Actually Work"},
            {"type": "intro", "template": "Introduction", "notes": [
                "Why these tips matter",
                "How to use them"
            ]},
            {"type": "h2", "template": "1. [Tip Title]", "notes": [
                "The tip",
                "Why it works",
                "How to implement",
                "Quick win action"
            ]},
            {"type": "h2", "template": "2. [Tip Title]", "notes": ["Same structure"]},
            {"type": "h2", "template": "3. [Tip Title]", "notes": ["Same structure"]},
            {"type": "h2", "template": "4. [Tip Title]", "notes": ["Same structure"]},
            {"type": "h2", "template": "5. [Tip Title]", "notes": ["Same structure"]},
            {"type": "h2", "template": "Bonus Tip", "notes": ["Extra value"]},
            {"type": "h2", "template": "Action Plan", "notes": [
                "How to implement",
                "Priority order"
            ]},
            {"type": "h2", "template": "Key Takeaways", "notes": [
                "Summary points",
                "Call to action"
            ]}
        ],
        "word_count": "1,500-2,500"
    }
}


def generate_outline(topic, content_type, num_items=None):
    """Generate outline based on topic and type."""
    template = OUTLINE_TEMPLATES.get(content_type)

    if not template:
        return {"error": f"Unknown content type: {content_type}"}

    outline = {
        "topic": topic,
        "content_type": content_type,
        "target_word_count": template["word_count"],
        "sections": []
    }

    for section in template["sections"]:
        section_data = {
            "type": section["type"],
            "heading": section["template"].format(topic=topic.title()),
            "notes": section.get("notes", [])
        }
        outline["sections"].append(section_data)

    # Add metadata
    outline["writing_tips"] = [
        f"Target word count: {template['word_count']}",
        "Include the target keyword in H1 and at least one H2",
        "Add images or visuals for key sections",
        "Include internal links to related content",
        "End each major section with a transition"
    ]

    return outline


def format_outline_markdown(outline):
    """Format outline as markdown."""
    lines = []
    lines.append(f"# Outline: {outline['topic']}\n")
    lines.append(f"**Content Type:** {outline['content_type']}")
    lines.append(f"**Target Word Count:** {outline['target_word_count']}\n")
    lines.append("---\n")

    for section in outline["sections"]:
        if section["type"] == "h1":
            lines.append(f"# {section['heading']}\n")
        elif section["type"] == "h2":
            lines.append(f"## {section['heading']}")
        elif section["type"] == "intro":
            lines.append(f"### {section['heading']}")
        elif section["type"] == "toc":
            lines.append(f"### {section['heading']}")

        if section.get("notes"):
            for note in section["notes"]:
                lines.append(f"  - {note}")
        lines.append("")

    lines.append("---\n")
    lines.append("## Writing Tips\n")
    for tip in outline["writing_tips"]:
        lines.append(f"- {tip}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate blog post outline")
    parser.add_argument("--topic", "-t", required=True, help="Topic for the post")
    parser.add_argument("--type", "-T", required=True,
                        choices=list(OUTLINE_TEMPLATES.keys()),
                        help="Content type")
    parser.add_argument("--format", "-f", choices=["json", "markdown"],
                        default="markdown", help="Output format")
    parser.add_argument("--items", "-n", type=int, help="Number of items (for listicles)")

    args = parser.parse_args()

    outline = generate_outline(args.topic, args.type, args.items)

    if "error" in outline:
        print(json.dumps(outline))
        sys.exit(1)

    if args.format == "markdown":
        print(format_outline_markdown(outline))
    else:
        print(json.dumps(outline, indent=2))


if __name__ == "__main__":
    main()
