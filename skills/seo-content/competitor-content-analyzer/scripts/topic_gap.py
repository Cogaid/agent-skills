#!/usr/bin/env python3
"""
Topic Gap Analyzer -- Identify topic and keyword gaps between you and competitors.

Usage:
    python topic_gap.py --your-domain you.com --competitors comp1.com,comp2.com
    python topic_gap.py --your-domain you.com --competitors comp1.com --min-volume 500 --output gaps.json
    python topic_gap.py --your-domain you.com --competitors comp1.com,comp2.com --format markdown
"""

import argparse
import json
import random
import sys
from datetime import datetime

SAMPLE_KEYWORDS = [
    {"keyword": "content marketing strategy", "volume": 8100, "kd": 72},
    {"keyword": "how to create a content calendar", "volume": 3600, "kd": 45},
    {"keyword": "SEO content writing", "volume": 2900, "kd": 58},
    {"keyword": "content marketing examples", "volume": 2400, "kd": 52},
    {"keyword": "blog post template", "volume": 4400, "kd": 38},
    {"keyword": "content strategy framework", "volume": 1900, "kd": 55},
    {"keyword": "editorial calendar template", "volume": 1600, "kd": 32},
    {"keyword": "content marketing tools", "volume": 3100, "kd": 65},
    {"keyword": "content writing tips", "volume": 2700, "kd": 42},
    {"keyword": "content marketing ROI", "volume": 1300, "kd": 48},
    {"keyword": "content distribution strategy", "volume": 1100, "kd": 40},
    {"keyword": "content audit checklist", "volume": 880, "kd": 35},
    {"keyword": "pillar page examples", "volume": 720, "kd": 30},
    {"keyword": "content repurposing", "volume": 1500, "kd": 28},
    {"keyword": "content marketing metrics", "volume": 1200, "kd": 45},
    {"keyword": "how to write a case study", "volume": 2100, "kd": 38},
    {"keyword": "content brief template", "volume": 1400, "kd": 25},
    {"keyword": "content marketing budget", "volume": 900, "kd": 42},
    {"keyword": "content gap analysis", "volume": 1100, "kd": 35},
    {"keyword": "content optimization", "volume": 1800, "kd": 50},
    {"keyword": "evergreen content", "volume": 2200, "kd": 40},
    {"keyword": "content marketing funnel", "volume": 1600, "kd": 48},
    {"keyword": "content writing services", "volume": 3200, "kd": 60},
    {"keyword": "content marketing agency", "volume": 4100, "kd": 70},
    {"keyword": "content promotion strategies", "volume": 800, "kd": 32},
]


def simulate_rankings(domain, keywords):
    """Simulate keyword rankings for a domain."""
    rng = random.Random(hash(domain) % 2**32)
    rankings = {}

    for kw_data in keywords:
        kw = kw_data["keyword"]
        # Higher KD = less likely to rank
        rank_chance = 1 - (kw_data["kd"] / 120)
        rank_chance += rng.uniform(-0.2, 0.3)

        if rng.random() < rank_chance:
            position = rng.randint(1, 50)
            if kw_data["kd"] > 60:
                position = rng.randint(5, 80)
            rankings[kw] = {
                "position": min(position, 100),
                "url": f"https://{domain}/blog/{kw.replace(' ', '-')}",
                "estimated_traffic": max(0, int(kw_data["volume"] * (1 / (position * 0.5)))),
            }

    return rankings


def find_gaps(your_rankings, competitor_rankings, keywords, min_volume=0):
    """Find keyword gaps between domains."""
    gaps = {
        "they_rank_you_dont": [],
        "they_rank_higher": [],
        "you_rank_they_dont": [],
        "both_rank": [],
    }

    for kw_data in keywords:
        kw = kw_data["keyword"]
        if kw_data["volume"] < min_volume:
            continue

        you_rank = your_rankings.get(kw)
        they_rank = competitor_rankings.get(kw)

        if they_rank and not you_rank:
            gaps["they_rank_you_dont"].append({
                "keyword": kw,
                "volume": kw_data["volume"],
                "difficulty": kw_data["kd"],
                "their_position": they_rank["position"],
                "their_url": they_rank["url"],
                "their_traffic": they_rank["estimated_traffic"],
                "priority": calculate_priority(kw_data["volume"], kw_data["kd"], they_rank["position"]),
            })
        elif you_rank and not they_rank:
            gaps["you_rank_they_dont"].append({
                "keyword": kw,
                "volume": kw_data["volume"],
                "your_position": you_rank["position"],
                "your_traffic": you_rank["estimated_traffic"],
            })
        elif you_rank and they_rank:
            if they_rank["position"] < you_rank["position"]:
                gaps["they_rank_higher"].append({
                    "keyword": kw,
                    "volume": kw_data["volume"],
                    "difficulty": kw_data["kd"],
                    "your_position": you_rank["position"],
                    "their_position": they_rank["position"],
                    "position_delta": you_rank["position"] - they_rank["position"],
                    "their_url": they_rank["url"],
                    "action": "optimize" if you_rank["position"] <= 20 else "major_update",
                })
            gaps["both_rank"].append({
                "keyword": kw,
                "volume": kw_data["volume"],
                "your_position": you_rank["position"],
                "their_position": they_rank["position"],
                "leader": "you" if you_rank["position"] < they_rank["position"] else "them",
            })

    # Sort by priority
    gaps["they_rank_you_dont"].sort(key=lambda x: -x["priority"])
    gaps["they_rank_higher"].sort(key=lambda x: -x["position_delta"])
    gaps["you_rank_they_dont"].sort(key=lambda x: -x["volume"])

    return gaps


def calculate_priority(volume, difficulty, their_position):
    """Calculate priority score for a gap opportunity."""
    volume_score = min(volume / 1000, 10)
    difficulty_score = max(0, 10 - (difficulty / 10))
    position_score = max(0, 10 - (their_position / 10))

    return round((volume_score * 0.35 + difficulty_score * 0.35 + position_score * 0.30), 1)


def generate_summary(gaps, your_domain, competitors):
    """Generate gap analysis summary."""
    total_gap_volume = sum(g["volume"] for g in gaps["they_rank_you_dont"])
    total_advantage_volume = sum(g["volume"] for g in gaps["you_rank_they_dont"])
    high_priority = [g for g in gaps["they_rank_you_dont"] if g["priority"] >= 6]

    return {
        "your_domain": your_domain,
        "competitors": competitors,
        "total_keywords_analyzed": len(SAMPLE_KEYWORDS),
        "gaps_found": len(gaps["they_rank_you_dont"]),
        "advantages_found": len(gaps["you_rank_they_dont"]),
        "head_to_head": len(gaps["both_rank"]),
        "total_gap_traffic_potential": total_gap_volume,
        "total_advantage_traffic": total_advantage_volume,
        "high_priority_opportunities": len(high_priority),
        "top_recommendations": [
            f"Create content for '{g['keyword']}' (vol: {g['volume']}, their position: #{g['their_position']})"
            for g in gaps["they_rank_you_dont"][:5]
        ],
    }


def render_markdown(results):
    """Render gap analysis as markdown."""
    lines = [
        "# Topic Gap Analysis",
        "",
        f"**Your Domain:** {results['summary']['your_domain']}",
        f"**Competitors:** {', '.join(results['summary']['competitors'])}",
        f"**Date:** {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "## Summary",
        "",
        f"- Keywords analyzed: {results['summary']['total_keywords_analyzed']}",
        f"- Gaps found (they rank, you don't): **{results['summary']['gaps_found']}**",
        f"- Your advantages (you rank, they don't): **{results['summary']['advantages_found']}**",
        f"- Head-to-head: {results['summary']['head_to_head']}",
        f"- High-priority opportunities: **{results['summary']['high_priority_opportunities']}**",
        f"- Total gap traffic potential: ~{results['summary']['total_gap_traffic_potential']:,} searches/mo",
        "",
    ]

    gaps = results["gaps"]

    if gaps["they_rank_you_dont"]:
        lines.extend([
            "## Keywords They Rank For, You Don't",
            "",
            "| Keyword | Volume | KD | Their Position | Priority |",
            "|---------|--------|-----|---------------|----------|",
        ])
        for g in gaps["they_rank_you_dont"][:15]:
            lines.append(f"| {g['keyword']} | {g['volume']} | {g['difficulty']} | #{g['their_position']} | {g['priority']}/10 |")
        lines.append("")

    if gaps["they_rank_higher"]:
        lines.extend([
            "## Keywords Where They Outrank You",
            "",
            "| Keyword | Volume | Your Pos | Their Pos | Delta | Action |",
            "|---------|--------|----------|-----------|-------|--------|",
        ])
        for g in gaps["they_rank_higher"][:10]:
            lines.append(f"| {g['keyword']} | {g['volume']} | #{g['your_position']} | #{g['their_position']} | {g['position_delta']} | {g['action']} |")
        lines.append("")

    if gaps["you_rank_they_dont"]:
        lines.extend([
            "## Your Advantages (You Rank, They Don't)",
            "",
            "| Keyword | Volume | Your Position | Traffic |",
            "|---------|--------|--------------|---------|",
        ])
        for g in gaps["you_rank_they_dont"][:10]:
            lines.append(f"| {g['keyword']} | {g['volume']} | #{g['your_position']} | {g['your_traffic']} |")
        lines.append("")

    if results["summary"]["top_recommendations"]:
        lines.extend(["## Top Recommendations", ""])
        for i, rec in enumerate(results["summary"]["top_recommendations"], 1):
            lines.append(f"{i}. {rec}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Identify topic and keyword gaps vs. competitors",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --your-domain you.com --competitors comp1.com,comp2.com
  %(prog)s --your-domain you.com --competitors comp1.com --min-volume 500
  %(prog)s --your-domain you.com --competitors comp1.com,comp2.com --format markdown
        """,
    )
    parser.add_argument("--your-domain", required=True, help="Your domain")
    parser.add_argument("--competitors", required=True, help="Comma-separated competitor domains")
    parser.add_argument("--min-volume", type=int, default=0, help="Minimum search volume filter")
    parser.add_argument(
        "--format",
        choices=["json", "markdown"],
        default="json",
        help="Output format (default: json)",
    )
    parser.add_argument("--output", help="Output file (default: stdout)")

    args = parser.parse_args()

    your_domain = args.your_domain.replace("https://", "").replace("http://", "").rstrip("/")
    competitors = [c.strip().replace("https://", "").replace("http://", "").rstrip("/")
                   for c in args.competitors.split(",")]

    # Simulate rankings
    your_rankings = simulate_rankings(your_domain, SAMPLE_KEYWORDS)

    # Combine competitor rankings (union of their rankings)
    all_competitor_rankings = {}
    for comp in competitors:
        comp_rankings = simulate_rankings(comp, SAMPLE_KEYWORDS)
        for kw, data in comp_rankings.items():
            if kw not in all_competitor_rankings or data["position"] < all_competitor_rankings[kw]["position"]:
                all_competitor_rankings[kw] = {**data, "competitor": comp}

    gaps = find_gaps(your_rankings, all_competitor_rankings, SAMPLE_KEYWORDS, args.min_volume)
    summary = generate_summary(gaps, your_domain, competitors)

    results = {
        "generated_at": datetime.now().isoformat(),
        "summary": summary,
        "gaps": gaps,
    }

    if args.format == "markdown":
        output = render_markdown(results)
    else:
        output = json.dumps(results, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Gap analysis written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
