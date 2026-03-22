#!/usr/bin/env python3
"""
Analyze content gaps between your page and competitor pages.

Usage:
    python gap_analysis.py your-page.md competitor-page.md
    python gap_analysis.py your-page.md comp1.md comp2.md comp3.md

Output: Gap analysis with missing topics and recommendations
"""

import argparse
import json
import re
import sys
from collections import Counter


def extract_structure(content):
    """Extract content structure and topics."""
    # Headers
    h1 = re.findall(r'^#\s+(.+)$', content, re.MULTILINE)
    h2 = re.findall(r'^##\s+(.+)$', content, re.MULTILINE)
    h3 = re.findall(r'^###\s+(.+)$', content, re.MULTILINE)

    # Word count
    words = content.split()
    word_count = len(words)

    # Key phrases (simplified extraction)
    # Get all sentences
    sentences = re.split(r'[.!?]', content)

    # Images
    images = len(re.findall(r'!\[', content))

    # Links
    internal_links = len(re.findall(r'\]\(/', content))
    external_links = len(re.findall(r'\]\(https?://', content))

    # Lists
    bullet_count = len(re.findall(r'^\s*[-*]\s', content, re.MULTILINE))
    numbered_count = len(re.findall(r'^\s*\d+[.)]\s', content, re.MULTILINE))

    return {
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "all_headers": h1 + h2 + h3,
        "word_count": word_count,
        "images": images,
        "internal_links": internal_links,
        "external_links": external_links,
        "bullet_points": bullet_count,
        "numbered_lists": numbered_count,
        "sentence_count": len([s for s in sentences if s.strip()])
    }


def normalize_topic(topic):
    """Normalize topic for comparison."""
    # Remove common words and normalize
    topic = topic.lower()
    topic = re.sub(r'[^\w\s]', '', topic)
    # Remove common stop words
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
    words = [w for w in topic.split() if w not in stop_words]
    return ' '.join(sorted(words))


def find_topic_matches(your_topics, competitor_topics, threshold=0.5):
    """Find matching topics between lists."""
    matches = []
    your_unmatched = []
    comp_unmatched = list(competitor_topics)

    for your_topic in your_topics:
        your_normalized = normalize_topic(your_topic)
        your_words = set(your_normalized.split())

        found_match = False
        for i, comp_topic in enumerate(comp_unmatched):
            comp_normalized = normalize_topic(comp_topic)
            comp_words = set(comp_normalized.split())

            # Calculate similarity
            if your_words and comp_words:
                intersection = your_words & comp_words
                union = your_words | comp_words
                similarity = len(intersection) / len(union)

                if similarity >= threshold:
                    matches.append({
                        "yours": your_topic,
                        "competitor": comp_topic,
                        "similarity": round(similarity, 2)
                    })
                    comp_unmatched.pop(i)
                    found_match = True
                    break

        if not found_match:
            your_unmatched.append(your_topic)

    return {
        "matches": matches,
        "only_yours": your_unmatched,
        "only_competitor": comp_unmatched
    }


def analyze_gaps(your_content, competitor_contents):
    """Perform comprehensive gap analysis."""
    your_structure = extract_structure(your_content)

    competitor_structures = []
    for i, comp_content in enumerate(competitor_contents):
        comp_structure = extract_structure(comp_content)
        comp_structure["index"] = i + 1
        competitor_structures.append(comp_structure)

    # Calculate averages
    avg_word_count = sum(c["word_count"] for c in competitor_structures) / len(competitor_structures)
    avg_h2_count = sum(len(c["h2"]) for c in competitor_structures) / len(competitor_structures)
    avg_images = sum(c["images"] for c in competitor_structures) / len(competitor_structures)

    # Word count gap
    word_count_gap = avg_word_count - your_structure["word_count"]

    # Topic gaps (combine all competitor H2s)
    all_competitor_topics = []
    for comp in competitor_structures:
        all_competitor_topics.extend(comp["h2"])

    # Count topic frequency
    topic_frequency = Counter()
    for topic in all_competitor_topics:
        normalized = normalize_topic(topic)
        topic_frequency[normalized] += 1

    # Find common topics (in 2+ competitors)
    common_topics = [topic for topic, count in topic_frequency.items() if count >= 2]

    # Check which common topics you cover
    your_normalized = [normalize_topic(h) for h in your_structure["h2"]]
    missing_common = []
    for topic in common_topics:
        if topic not in your_normalized:
            # Find original form
            for comp_topic in all_competitor_topics:
                if normalize_topic(comp_topic) == topic:
                    missing_common.append(comp_topic)
                    break

    # Topic comparison
    topic_comparison = find_topic_matches(your_structure["h2"], all_competitor_topics)

    # Build recommendations
    recommendations = []

    if word_count_gap > 500:
        recommendations.append({
            "priority": "high",
            "action": f"Add approximately {int(word_count_gap)} words",
            "reason": "Content is significantly shorter than competitors"
        })
    elif word_count_gap > 200:
        recommendations.append({
            "priority": "medium",
            "action": f"Consider adding {int(word_count_gap)} words",
            "reason": "Content is shorter than average"
        })

    if missing_common:
        recommendations.append({
            "priority": "high",
            "action": f"Add sections covering: {', '.join(missing_common[:3])}",
            "reason": "Topics covered by multiple competitors"
        })

    if your_structure["images"] < avg_images:
        recommendations.append({
            "priority": "medium",
            "action": f"Add {int(avg_images - your_structure['images'])} more images",
            "reason": "Fewer visuals than competitors"
        })

    return {
        "your_content": {
            "word_count": your_structure["word_count"],
            "h2_count": len(your_structure["h2"]),
            "h2_topics": your_structure["h2"],
            "images": your_structure["images"],
            "internal_links": your_structure["internal_links"],
            "external_links": your_structure["external_links"]
        },
        "competitor_averages": {
            "word_count": round(avg_word_count),
            "h2_count": round(avg_h2_count, 1),
            "images": round(avg_images, 1)
        },
        "gaps": {
            "word_count": round(word_count_gap),
            "topics_missing": missing_common[:5],
            "topics_only_you_have": topic_comparison["only_yours"],
            "topic_overlap": len(topic_comparison["matches"])
        },
        "recommendations": recommendations,
        "competitor_topics_all": list(set(all_competitor_topics))[:15]
    }


def main():
    parser = argparse.ArgumentParser(description="Content gap analysis")
    parser.add_argument("your_page", help="Your content file")
    parser.add_argument("competitor_pages", nargs="+", help="Competitor content files")
    parser.add_argument("--format", "-f", choices=["json", "summary"], default="json",
                        help="Output format")

    args = parser.parse_args()

    # Read your content
    try:
        with open(args.your_page, 'r') as f:
            your_content = f.read()
    except FileNotFoundError:
        print(json.dumps({"error": f"File not found: {args.your_page}"}))
        sys.exit(1)

    # Read competitor content
    competitor_contents = []
    for comp_file in args.competitor_pages:
        try:
            with open(comp_file, 'r') as f:
                competitor_contents.append(f.read())
        except FileNotFoundError:
            print(json.dumps({"error": f"File not found: {comp_file}"}))
            sys.exit(1)

    result = analyze_gaps(your_content, competitor_contents)

    if args.format == "summary":
        print("\n=== Content Gap Analysis ===\n")
        print(f"Your word count: {result['your_content']['word_count']}")
        print(f"Competitor average: {result['competitor_averages']['word_count']}")
        print(f"Gap: {result['gaps']['word_count']} words\n")

        print("Missing Topics (covered by competitors):")
        for topic in result['gaps']['topics_missing']:
            print(f"  - {topic}")

        print("\nUnique Topics (only you have):")
        for topic in result['gaps']['topics_only_you_have']:
            print(f"  + {topic}")

        print("\nRecommendations:")
        for rec in result['recommendations']:
            print(f"  [{rec['priority'].upper()}] {rec['action']}")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
