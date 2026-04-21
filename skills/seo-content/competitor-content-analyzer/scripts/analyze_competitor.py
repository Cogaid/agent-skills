#!/usr/bin/env python3
"""
Competitor Content Analyzer -- Run full competitor content analysis.

Usage:
    python analyze_competitor.py --competitor example.com --depth full
    python analyze_competitor.py --competitor blog.competitor.com --depth quick --output analysis.json
    python analyze_competitor.py --competitor example.com --depth full --format markdown
"""

import argparse
import json
import random
import sys
from datetime import datetime, timedelta
from urllib.parse import urlparse

CONTENT_TOPICS = [
    "Product Management", "Engineering", "Design", "Marketing",
    "Sales", "Customer Success", "Leadership", "Industry Trends",
    "How-to Guides", "Case Studies", "Comparisons", "Reviews",
]

CONTENT_TYPES = ["blog_post", "guide", "case_study", "video", "podcast", "tool", "whitepaper"]

CONTENT_FORMATS = ["how-to", "listicle", "comparison", "opinion", "research", "interview", "news"]


def generate_content_inventory(domain, depth):
    """Generate a simulated content inventory for a competitor."""
    rng = random.Random(hash(domain) % 2**32)

    total_pages = rng.randint(80, 500) if depth == "full" else rng.randint(30, 100)

    inventory = {
        "domain": domain,
        "total_pages": total_pages,
        "blog_posts": int(total_pages * rng.uniform(0.5, 0.7)),
        "landing_pages": int(total_pages * rng.uniform(0.1, 0.2)),
        "case_studies": rng.randint(5, 25),
        "videos": rng.randint(10, 60),
        "guides_whitepapers": rng.randint(3, 15),
        "tools_calculators": rng.randint(0, 5),
    }

    # Publishing cadence
    inventory["cadence"] = {
        "last_30_days": rng.randint(4, 20),
        "last_90_days": rng.randint(15, 60),
        "last_12_months": rng.randint(50, 200),
        "avg_per_week": round(rng.uniform(1.5, 5.0), 1),
        "trend": rng.choice(["increasing", "stable", "decreasing"]),
    }

    return inventory


def generate_topic_breakdown(domain, inventory):
    """Generate topic coverage breakdown."""
    rng = random.Random(hash(domain + "topics") % 2**32)
    topics = rng.sample(CONTENT_TOPICS, min(8, len(CONTENT_TOPICS)))

    breakdown = []
    remaining = inventory["blog_posts"]
    for i, topic in enumerate(topics):
        if i == len(topics) - 1:
            count = remaining
        else:
            count = rng.randint(5, remaining // (len(topics) - i))
            remaining -= count

        breakdown.append({
            "topic": topic,
            "pages": max(count, 1),
            "estimated_traffic": rng.randint(500, 15000),
            "top_keyword": f"[{topic.lower()} keyword]",
            "avg_word_count": rng.randint(800, 2500),
        })

    breakdown.sort(key=lambda x: -x["estimated_traffic"])
    return breakdown


def generate_top_content(domain, count=10):
    """Generate top-performing content list."""
    rng = random.Random(hash(domain + "top") % 2**32)

    content = []
    for i in range(count):
        topic = rng.choice(CONTENT_TOPICS)
        content_type = rng.choice(CONTENT_TYPES)
        fmt = rng.choice(CONTENT_FORMATS)
        traffic = int(rng.paretovariate(1.5) * 1000)
        keywords = rng.randint(20, 500)
        ref_domains = rng.randint(5, 100)

        content.append({
            "rank": i + 1,
            "url": f"https://{domain}/blog/{topic.lower().replace(' ', '-')}-{fmt}-{i+1}",
            "title": f"[{fmt.title()}] {topic}: A Complete Guide" if fmt == "how-to" else f"Top {rng.randint(5, 20)} {topic} {fmt.title()}s",
            "type": content_type,
            "format": fmt,
            "estimated_traffic": traffic,
            "keywords_ranking": keywords,
            "referring_domains": ref_domains,
            "word_count": rng.randint(800, 4000),
            "publish_date": (datetime.now() - timedelta(days=rng.randint(30, 700))).strftime("%Y-%m-%d"),
        })

    content.sort(key=lambda x: -x["estimated_traffic"])
    for i, c in enumerate(content):
        c["rank"] = i + 1

    return content


def generate_quality_assessment(domain):
    """Generate content quality assessment."""
    rng = random.Random(hash(domain + "quality") % 2**32)

    return {
        "depth_thoroughness": rng.randint(5, 9),
        "writing_quality": rng.randint(5, 9),
        "visual_design": rng.randint(4, 9),
        "originality": rng.randint(4, 8),
        "eeat_signals": rng.randint(4, 9),
        "ux_readability": rng.randint(5, 9),
        "cta_conversion_focus": rng.randint(4, 8),
        "overall": None,  # calculated below
    }


def generate_format_distribution(domain, total):
    """Generate content format distribution."""
    rng = random.Random(hash(domain + "format") % 2**32)

    formats = {
        "long_form_2000_plus": {"pct": rng.uniform(0.15, 0.35)},
        "standard_800_2000": {"pct": rng.uniform(0.35, 0.55)},
        "short_form_under_800": {"pct": rng.uniform(0.1, 0.25)},
        "video": {"pct": rng.uniform(0.05, 0.15)},
        "infographic": {"pct": rng.uniform(0.02, 0.08)},
        "interactive_tool": {"pct": rng.uniform(0.01, 0.05)},
    }

    # Normalize
    total_pct = sum(f["pct"] for f in formats.values())
    for f in formats.values():
        f["pct"] = round(f["pct"] / total_pct, 3)
        f["count"] = int(total * f["pct"])
        f["avg_traffic"] = rng.randint(200, 3000)

    return formats


def run_analysis(domain, depth):
    """Run full competitor content analysis."""
    inventory = generate_content_inventory(domain, depth)
    topics = generate_topic_breakdown(domain, inventory)
    top_content = generate_top_content(domain, count=10 if depth == "full" else 5)
    quality = generate_quality_assessment(domain)
    formats = generate_format_distribution(domain, inventory["total_pages"])

    # Calculate overall quality score
    scores = [v for k, v in quality.items() if k != "overall" and v is not None]
    quality["overall"] = round(sum(scores) / len(scores), 1)

    analysis = {
        "domain": domain,
        "depth": depth,
        "inventory": inventory,
        "topic_breakdown": topics,
        "top_performing_content": top_content,
        "quality_assessment": quality,
        "format_distribution": formats,
        "strengths": [],
        "weaknesses": [],
        "opportunities": [],
    }

    # Generate insights
    if quality["overall"] >= 7:
        analysis["strengths"].append(f"High content quality (score: {quality['overall']}/10)")
    if inventory["cadence"]["trend"] == "increasing":
        analysis["strengths"].append("Publishing frequency is increasing -- they're investing more")
    if inventory["tools_calculators"] > 2:
        analysis["strengths"].append(f"Interactive content strategy ({inventory['tools_calculators']} tools)")

    if quality["originality"] < 6:
        analysis["weaknesses"].append("Low originality -- mostly derivative content")
    if inventory["cadence"]["trend"] == "decreasing":
        analysis["weaknesses"].append("Publishing frequency declining -- possible resource constraints")
    if quality["eeat_signals"] < 6:
        analysis["weaknesses"].append("Weak E-E-A-T signals -- opportunity to outperform on trust")

    analysis["opportunities"].append("Topics they cover thinly that you can dominate with comprehensive content")
    analysis["opportunities"].append("Their older content (12+ months) is vulnerable to fresher alternatives")
    if quality["visual_design"] < 6:
        analysis["opportunities"].append("Better visual design and UX could differentiate your content")

    return analysis


def render_markdown(analysis):
    """Render analysis as markdown."""
    lines = [
        f"# Competitor Content Analysis: {analysis['domain']}",
        "",
        f"**Depth:** {analysis['depth']}",
        f"**Date:** {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "## Content Inventory",
        "",
        "| Metric | Value |",
        "|--------|-------|",
    ]

    inv = analysis["inventory"]
    lines.append(f"| Total pages | {inv['total_pages']} |")
    lines.append(f"| Blog posts | {inv['blog_posts']} |")
    lines.append(f"| Case studies | {inv['case_studies']} |")
    lines.append(f"| Videos | {inv['videos']} |")
    lines.append(f"| Guides/whitepapers | {inv['guides_whitepapers']} |")
    lines.append(f"| Tools/calculators | {inv['tools_calculators']} |")

    lines.extend([
        "",
        "## Publishing Cadence",
        "",
        f"- Last 30 days: {inv['cadence']['last_30_days']} posts",
        f"- Average: {inv['cadence']['avg_per_week']} per week",
        f"- Trend: **{inv['cadence']['trend']}**",
        "",
        "## Topic Coverage",
        "",
        "| Topic | Pages | Est. Traffic | Avg Words |",
        "|-------|-------|-------------|-----------|",
    ])

    for topic in analysis["topic_breakdown"][:8]:
        lines.append(f"| {topic['topic']} | {topic['pages']} | {topic['estimated_traffic']} | {topic['avg_word_count']} |")

    lines.extend([
        "",
        "## Top Performing Content",
        "",
        "| # | Title | Traffic | Keywords | Ref. Domains |",
        "|---|-------|---------|----------|-------------|",
    ])

    for item in analysis["top_performing_content"][:5]:
        title = item["title"][:50] + "..." if len(item["title"]) > 50 else item["title"]
        lines.append(f"| {item['rank']} | {title} | {item['estimated_traffic']} | {item['keywords_ranking']} | {item['referring_domains']} |")

    lines.extend([
        "",
        "## Quality Assessment",
        "",
        "| Dimension | Score |",
        "|-----------|-------|",
    ])
    for key, val in analysis["quality_assessment"].items():
        if val is not None:
            lines.append(f"| {key.replace('_', ' ').title()} | {val}/10 |")

    lines.extend(["", "## Key Insights", ""])
    if analysis["strengths"]:
        lines.append("**Strengths:**")
        for s in analysis["strengths"]:
            lines.append(f"- {s}")
    if analysis["weaknesses"]:
        lines.append("\n**Weaknesses:**")
        for w in analysis["weaknesses"]:
            lines.append(f"- {w}")
    if analysis["opportunities"]:
        lines.append("\n**Opportunities:**")
        for o in analysis["opportunities"]:
            lines.append(f"- {o}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Run full competitor content analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --competitor example.com --depth full
  %(prog)s --competitor blog.competitor.com --depth quick --output analysis.json
  %(prog)s --competitor example.com --depth full --format markdown
        """,
    )
    parser.add_argument("--competitor", required=True, help="Competitor domain to analyze")
    parser.add_argument(
        "--depth",
        choices=["quick", "standard", "full"],
        default="standard",
        help="Analysis depth (default: standard)",
    )
    parser.add_argument(
        "--format",
        choices=["json", "markdown"],
        default="json",
        help="Output format (default: json)",
    )
    parser.add_argument("--output", help="Output file (default: stdout)")

    args = parser.parse_args()

    domain = args.competitor.replace("https://", "").replace("http://", "").rstrip("/")
    analysis = run_analysis(domain, args.depth)

    result = {
        "generated_at": datetime.now().isoformat(),
        "tool": "competitor-content-analyzer",
        "analysis": analysis,
    }

    if args.format == "markdown":
        output = render_markdown(analysis)
    else:
        output = json.dumps(result, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Analysis written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
