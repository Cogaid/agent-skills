#!/usr/bin/env python3
"""
Case Study Generator -- Generate structured case study drafts from interview data.

Usage:
    python case_study_generator.py --company "Acme Corp" --industry "SaaS" --challenge "Manual reporting" --result "73% time savings" --product "ReportBot"
    python case_study_generator.py --input interview_notes.json --format standard
    python case_study_generator.py --company "TechScale" --industry "E-commerce" --format one-pager --output draft.json
"""

import argparse
import json
import sys
from datetime import datetime

CASE_STUDY_FORMATS = {
    "standard": {
        "name": "Standard Case Study",
        "target_words": "800-1200",
        "sections": [
            "at_a_glance",
            "about",
            "challenge",
            "solution",
            "results",
            "whats_next",
            "cta",
        ],
    },
    "one-pager": {
        "name": "One-Pager",
        "target_words": "300-500",
        "sections": ["headline", "metrics_table", "challenge", "solution", "results", "cta"],
    },
    "metrics": {
        "name": "Metrics-Heavy",
        "target_words": "1000-1500",
        "sections": [
            "dashboard",
            "background",
            "problem_quantified",
            "approach",
            "results_deep_dive",
            "roi_analysis",
            "customer_quote",
            "cta",
        ],
    },
    "video": {
        "name": "Video Script (2-3 min)",
        "target_words": "400-600",
        "sections": ["opening", "challenge", "solution", "results", "endorsement", "closing"],
    },
}

SECTION_PROMPTS = {
    "at_a_glance": {
        "title": "At a Glance",
        "prompt": "Summary table with company info and key metrics",
        "template": (
            "| | |\n"
            "|---|---|\n"
            "| **Company** | {company} |\n"
            "| **Industry** | {industry} |\n"
            "| **Size** | {company_size} |\n"
            "| **Products Used** | {product} |\n"
            "\n"
            "| Metric | Result |\n"
            "|--------|--------|\n"
            "| {primary_metric_name} | {primary_metric_value} |\n"
            "| {secondary_metric_name} | {secondary_metric_value} |"
        ),
    },
    "about": {
        "title": "About {company}",
        "prompt": "2-3 sentences about the company, establishing relatability and scale",
        "template": (
            "{company} is a {company_size} {industry} company that {company_description}. "
            "[Expand with relevant operational context that makes the challenge relatable to your target audience.]"
        ),
    },
    "challenge": {
        "title": "The Challenge",
        "prompt": "Describe the problems faced, with quantified impact",
        "template": (
            "Before {product}, {company} faced significant challenges with {challenge}.\n\n"
            "[Expand: What was the specific impact? How much time/money was lost? "
            "What was the emotional toll on the team?]\n\n"
            '> "[Insert customer quote about the challenge]"\n'
            "> -- [Name], [Title], {company}\n\n"
            "Key challenges included:\n"
            "- {challenge}\n"
            "- [Challenge 2 -- specific and quantified]\n"
            "- [Challenge 3 -- specific and quantified]"
        ),
    },
    "solution": {
        "title": "The Solution",
        "prompt": "How they implemented and used your product",
        "template": (
            "{company} chose {product} to address {challenge}.\n\n"
            "[Describe the implementation process, timeline, and key features used.]\n\n"
            "**Key features used:**\n"
            "- **[Feature 1]:** [How they use it]\n"
            "- **[Feature 2]:** [How they use it]\n"
            "- **[Feature 3]:** [How they use it]"
        ),
    },
    "results": {
        "title": "The Results",
        "prompt": "Quantified outcomes and qualitative benefits",
        "template": (
            "Since implementing {product}, {company} has achieved remarkable results.\n\n"
            '> "[Insert powerful quote about results]"\n'
            "> -- [Name], [Title], {company}\n\n"
            "### By the Numbers\n\n"
            "- **{result}**\n"
            "- [Secondary metric and result]\n"
            "- [Financial impact]\n\n"
            "### Beyond the Numbers\n\n"
            "- [Qualitative benefit 1]\n"
            "- [Qualitative benefit 2]"
        ),
    },
    "whats_next": {
        "title": "What's Next",
        "prompt": "Future plans and continued partnership",
        "template": (
            "[Describe future plans: expanding usage, adopting new features, "
            "or long-term strategic vision with {product}.]"
        ),
    },
    "cta": {
        "title": "Call to Action",
        "prompt": "Clear next step for the reader",
        "template": (
            "**Ready to achieve similar results?** [CTA -- e.g., Schedule a demo, "
            "Start your free trial]\n\n"
            "[Your Company] helps companies like {company} {result_lower}. "
            "Learn more at [URL]."
        ),
    },
    "headline": {
        "title": "Headline",
        "prompt": "One bold sentence summarizing the result",
        "template": "**{company} achieved {result} with {product}.**",
    },
    "metrics_table": {
        "title": "Key Metrics",
        "prompt": "Before/after comparison table",
        "template": (
            "| | Before | After | Impact |\n"
            "|---|--------|-------|--------|\n"
            "| {primary_metric_name} | [Before] | [After] | {primary_metric_value} |\n"
            "| {secondary_metric_name} | [Before] | [After] | {secondary_metric_value} |"
        ),
    },
    "dashboard": {
        "title": "Results Dashboard",
        "prompt": "Comprehensive metrics overview",
        "template": (
            "| Category | Before | After | Change |\n"
            "|----------|--------|-------|--------|\n"
            "| {primary_metric_name} | [Before] | [After] | {primary_metric_value} |\n"
            "| {secondary_metric_name} | [Before] | [After] | {secondary_metric_value} |\n"
            "| [Additional metric] | [Before] | [After] | [Change] |\n\n"
            "**Industry:** {industry} | **Size:** {company_size} | "
            "**Implementation Time:** [Duration]"
        ),
    },
    "background": {
        "title": "Background",
        "prompt": "Brief company overview focusing on scale",
        "template": "{company} is a {company_size} company in the {industry} space. {company_description}",
    },
    "problem_quantified": {
        "title": "The Problem (Quantified)",
        "prompt": "Quantified problem statements",
        "template": (
            "- Lost **$[X]** annually to {challenge}\n"
            "- Spent **[X] hours** per week on [specific task]\n"
            "- Experienced **[X]%** error rate in [process]"
        ),
    },
    "approach": {
        "title": "The Approach",
        "prompt": "Phased implementation timeline",
        "template": (
            "**Week 1-2:** [Phase 1 -- setup and configuration]\n"
            "**Week 3-4:** [Phase 2 -- team onboarding]\n"
            "**Week 5+:** [Phase 3 -- optimization and scaling]"
        ),
    },
    "results_deep_dive": {
        "title": "Results Deep Dive",
        "prompt": "Detailed analysis of each key metric",
        "template": (
            "### {primary_metric_name}: {primary_metric_value}\n\n"
            "[2-3 sentences explaining what drove this improvement and why it matters.]\n\n"
            "### {secondary_metric_name}: {secondary_metric_value}\n\n"
            "[2-3 sentences with context.]"
        ),
    },
    "roi_analysis": {
        "title": "ROI Analysis",
        "prompt": "Financial return on investment",
        "template": (
            "| Item | Amount |\n"
            "|------|--------|\n"
            "| Annual investment | $[X] |\n"
            "| Annual savings | $[Y] |\n"
            "| Net annual benefit | $[Z] |\n"
            "| Payback period | [N] months |\n"
            "| 3-year ROI | [X]% |"
        ),
    },
    "customer_quote": {
        "title": "Customer Perspective",
        "prompt": "Powerful testimonial quote",
        "template": (
            '> "[Quote about the measurable impact and what it means for the business]"\n'
            "> -- [Name], [Title], {company}"
        ),
    },
    "opening": {
        "title": "Opening (0:00-0:15)",
        "prompt": "Speaker introduction",
        "template": (
            '[VISUAL: Customer at their workspace]\n[LOWER THIRD: Name, Title, {company}]\n\n'
            '"Hi, I\'m [Name], [Title] at {company}. We {company_description}."'
        ),
    },
    "endorsement": {
        "title": "Endorsement (2:10-2:25)",
        "prompt": "Direct recommendation",
        "template": (
            "[VISUAL: Close-up of speaker]\n\n"
            '"I\'d recommend {product} to any [role] who is dealing with {challenge}. '
            'The results speak for themselves."'
        ),
    },
    "closing": {
        "title": "Closing (2:25-2:30)",
        "prompt": "Logo and CTA",
        "template": "[VISUAL: Logo + Tagline + CTA]\n\n[Your Company] -- [Tagline]\nLearn more at [URL]",
    },
}


def generate_case_study(config, format_key):
    """Generate a structured case study from configuration."""
    fmt = CASE_STUDY_FORMATS[format_key]

    result_lower = config.get("result", "")
    if result_lower:
        result_lower = result_lower[0].lower() + result_lower[1:]

    context = {
        "company": config.get("company", "[Company Name]"),
        "industry": config.get("industry", "[Industry]"),
        "company_size": config.get("company_size", "[Size]"),
        "company_description": config.get(
            "company_description", "[what the company does]"
        ),
        "challenge": config.get("challenge", "[primary challenge]"),
        "product": config.get("product", "[Your Product]"),
        "result": config.get("result", "[primary result]"),
        "result_lower": result_lower,
        "primary_metric_name": config.get("primary_metric_name", "Primary Metric"),
        "primary_metric_value": config.get("primary_metric_value", "[value]"),
        "secondary_metric_name": config.get("secondary_metric_name", "Secondary Metric"),
        "secondary_metric_value": config.get("secondary_metric_value", "[value]"),
    }

    title_templates = {
        "standard": "How {company} Achieved {result} with {product}",
        "one-pager": "{company} + {product}: {result}",
        "metrics": "{result} -- The {company} Story",
        "video": "{company} Customer Story",
    }

    title = title_templates[format_key].format(**context)

    sections = []
    for section_key in fmt["sections"]:
        section_def = SECTION_PROMPTS.get(section_key, {})
        section_title = section_def.get("title", section_key).format(**context)
        content = section_def.get("template", "[Content for {section}]").format(
            section=section_key, **context
        )
        sections.append(
            {
                "key": section_key,
                "title": section_title,
                "content": content,
                "writing_prompt": section_def.get("prompt", ""),
            }
        )

    return {
        "title": title,
        "format": fmt["name"],
        "target_words": fmt["target_words"],
        "sections": sections,
        "context": context,
    }


def render_markdown(case_study):
    """Render case study as markdown."""
    lines = [f"# {case_study['title']}", ""]

    for section in case_study["sections"]:
        lines.append(f"## {section['title']}")
        lines.append("")
        lines.append(section["content"])
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Generate structured case study drafts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --company "Acme Corp" --industry "SaaS" --challenge "Manual reporting" --result "73%% time savings"
  %(prog)s --input interview.json --format one-pager
  %(prog)s --company "TechScale" --format metrics --output draft.json
        """,
    )
    parser.add_argument("--company", help="Customer company name")
    parser.add_argument("--industry", help="Customer industry")
    parser.add_argument("--company-size", help="Company size (e.g., '200 employees')")
    parser.add_argument("--company-description", help="What the company does")
    parser.add_argument("--challenge", help="Primary challenge faced")
    parser.add_argument("--product", help="Your product name")
    parser.add_argument("--result", help="Primary result achieved")
    parser.add_argument("--primary-metric", help="Primary metric name:value (e.g., 'Response Time:-73%%')")
    parser.add_argument("--secondary-metric", help="Secondary metric name:value")
    parser.add_argument(
        "--format",
        choices=list(CASE_STUDY_FORMATS.keys()),
        default="standard",
        help="Case study format (default: standard)",
    )
    parser.add_argument("--input", help="JSON file with interview data")
    parser.add_argument("--output", help="Output file (default: stdout)")
    parser.add_argument(
        "--render",
        choices=["json", "markdown"],
        default="json",
        help="Output rendering (default: json)",
    )

    args = parser.parse_args()

    if args.input:
        with open(args.input) as f:
            config = json.load(f)
    else:
        config = {}
        if args.company:
            config["company"] = args.company
        if args.industry:
            config["industry"] = args.industry
        if args.company_size:
            config["company_size"] = args.company_size
        if args.company_description:
            config["company_description"] = args.company_description
        if args.challenge:
            config["challenge"] = args.challenge
        if args.product:
            config["product"] = args.product
        if args.result:
            config["result"] = args.result
        if args.primary_metric:
            parts = args.primary_metric.split(":", 1)
            config["primary_metric_name"] = parts[0]
            config["primary_metric_value"] = parts[1] if len(parts) > 1 else "[value]"
        if args.secondary_metric:
            parts = args.secondary_metric.split(":", 1)
            config["secondary_metric_name"] = parts[0]
            config["secondary_metric_value"] = parts[1] if len(parts) > 1 else "[value]"

    case_study = generate_case_study(config, args.format)

    result = {
        "generated_at": datetime.now().isoformat(),
        "format": args.format,
        "case_study": case_study,
    }

    if args.render == "markdown":
        output = render_markdown(case_study)
    else:
        output = json.dumps(result, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Case study draft written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
