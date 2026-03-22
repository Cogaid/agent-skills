#!/usr/bin/env python3
"""
Generate optimized title and meta description variations for better CTR.

Usage:
    python ctr_optimizer.py --title "Your Current Title" --keyword "target keyword"
    python ctr_optimizer.py --title "Your Title" --description "Current meta" --keyword "seo"

Output: Optimized variations with CTR boosters
"""

import argparse
import json
import re
import sys


# Power words that tend to increase CTR
POWER_WORDS = {
    "urgency": ["now", "today", "instant", "immediate", "fast", "quick"],
    "value": ["free", "bonus", "save", "discount", "deal", "exclusive"],
    "curiosity": ["secret", "hidden", "surprising", "unexpected", "little-known", "shocking"],
    "emotion": ["amazing", "incredible", "powerful", "essential", "critical", "proven"],
    "authority": ["expert", "official", "complete", "ultimate", "definitive", "comprehensive"],
    "numbers": ["#1", "top", "best", "only", "first"],
    "time": ["2025", "[Updated]", "[New]", "latest", "current"]
}

# Title formulas that perform well
TITLE_FORMULAS = [
    "{keyword}: {benefit} | {brand}",
    "How to {keyword} ({outcome})",
    "{number} {adjective} Ways to {keyword} in {year}",
    "{keyword} Guide: {benefit} [{year}]",
    "The {adjective} {keyword} {guide_type} for {audience}",
    "{keyword}: {number} {things} You Need to Know",
    "Why {keyword} {matters} (And How to {action})",
    "{keyword} vs {alternative}: Which is {better}?",
    "The Best {keyword} for {outcome} [{year} Guide]",
    "{number} {keyword} {mistakes} to Avoid in {year}"
]

# Meta description formulas
META_FORMULAS = [
    "{hook}. Learn {benefit} with our {adjective} guide. {cta}",
    "Discover {benefit} with {keyword}. {proof}. {cta}",
    "{question}? Our {adjective} guide shows you {outcome}. {cta}",
    "Looking for {keyword}? {benefit}. {social_proof}. {cta}",
    "{problem}? Learn how to {solution} with our {keyword} guide. {cta}"
]


def analyze_current_title(title):
    """Analyze current title for optimization opportunities."""
    analysis = {
        "length": len(title),
        "word_count": len(title.split()),
        "has_number": bool(re.search(r'\d+', title)),
        "has_brackets": bool(re.search(r'[\[\(\{]', title)),
        "has_power_words": [],
        "issues": [],
        "score": 100
    }

    # Check length
    if len(title) > 60:
        analysis["issues"].append("Too long (will be truncated in SERPs)")
        analysis["score"] -= 15
    elif len(title) < 30:
        analysis["issues"].append("Too short (missing optimization opportunity)")
        analysis["score"] -= 10

    # Check for power words
    title_lower = title.lower()
    for category, words in POWER_WORDS.items():
        for word in words:
            if word.lower() in title_lower:
                analysis["has_power_words"].append({"word": word, "category": category})

    if not analysis["has_power_words"]:
        analysis["issues"].append("No power words found")
        analysis["score"] -= 10

    if not analysis["has_number"]:
        analysis["issues"].append("No numbers (numbers increase CTR)")
        analysis["score"] -= 5

    if not analysis["has_brackets"]:
        analysis["issues"].append("No brackets/parentheses (can increase CTR)")
        analysis["score"] -= 5

    return analysis


def analyze_current_meta(description):
    """Analyze current meta description."""
    analysis = {
        "length": len(description),
        "has_cta": False,
        "has_value_prop": False,
        "issues": [],
        "score": 100
    }

    # Check length
    if len(description) > 160:
        analysis["issues"].append("Too long (will be truncated)")
        analysis["score"] -= 15
    elif len(description) < 120:
        analysis["issues"].append("Too short (missing optimization opportunity)")
        analysis["score"] -= 10

    # Check for CTA
    cta_patterns = [r'learn', r'discover', r'get', r'find out', r'read', r'click', r'start']
    for pattern in cta_patterns:
        if re.search(pattern, description.lower()):
            analysis["has_cta"] = True
            break

    if not analysis["has_cta"]:
        analysis["issues"].append("No clear call-to-action")
        analysis["score"] -= 10

    return analysis


def generate_title_variations(keyword, current_title=None):
    """Generate optimized title variations."""
    variations = []
    year = "2025"

    # Clean keyword
    keyword_clean = keyword.strip()
    keyword_cap = keyword_clean.title()

    # Generate variations based on formulas
    templates = [
        f"{keyword_cap}: The Complete Guide [{year}]",
        f"How to {keyword_cap} (Step-by-Step Guide)",
        f"7 {keyword_cap} Tips That Actually Work [{year}]",
        f"The Ultimate {keyword_cap} Guide for Beginners",
        f"{keyword_cap}: Everything You Need to Know",
        f"10 Best {keyword_cap} Strategies for {year}",
        f"Why {keyword_cap} Matters (+ How to Get Started)",
        f"The Secret to {keyword_cap} Success [Expert Guide]",
        f"{keyword_cap} 101: A Beginner's Complete Guide",
        f"Master {keyword_cap} in {year}: Proven Strategies"
    ]

    for template in templates:
        variation = {
            "title": template,
            "length": len(template),
            "ctr_boosters": []
        }

        # Identify CTR boosters
        if re.search(r'\d+', template):
            variation["ctr_boosters"].append("number")
        if re.search(r'[\[\]]', template):
            variation["ctr_boosters"].append("brackets")
        if year in template:
            variation["ctr_boosters"].append("current_year")

        for category, words in POWER_WORDS.items():
            for word in words:
                if word.lower() in template.lower():
                    variation["ctr_boosters"].append(f"power_word:{word}")

        variations.append(variation)

    return variations


def generate_meta_variations(keyword, title=None):
    """Generate optimized meta description variations."""
    variations = []
    keyword_clean = keyword.strip()

    templates = [
        f"Learn everything about {keyword_clean} with our comprehensive guide. Discover proven strategies, tips, and best practices. Start improving today!",
        f"Looking for {keyword_clean} advice? Our expert guide covers everything you need to know. Get actionable tips you can use right away.",
        f"Master {keyword_clean} with our step-by-step guide. Trusted by thousands of readers. Click to discover proven strategies that work.",
        f"Struggling with {keyword_clean}? Our complete guide shows you exactly what to do. Free tips, examples, and expert advice inside.",
        f"Discover the secrets of successful {keyword_clean}. Learn from experts with our comprehensive, easy-to-follow guide. Read now!"
    ]

    for template in templates:
        length = len(template)
        variation = {
            "description": template,
            "length": length,
            "status": "good" if 120 <= length <= 160 else ("too_long" if length > 160 else "too_short"),
            "ctr_boosters": []
        }

        # Identify boosters
        if re.search(r'free|proven|expert', template.lower()):
            variation["ctr_boosters"].append("trust_words")
        if re.search(r'discover|learn|master', template.lower()):
            variation["ctr_boosters"].append("action_verb")
        if re.search(r'now|today|start', template.lower()):
            variation["ctr_boosters"].append("urgency")

        variations.append(variation)

    return variations


def optimize_for_ctr(current_title, current_description, keyword):
    """Generate complete CTR optimization suggestions."""
    result = {
        "keyword": keyword,
        "current_title_analysis": None,
        "current_meta_analysis": None,
        "title_variations": [],
        "meta_variations": [],
        "quick_wins": []
    }

    if current_title:
        result["current_title_analysis"] = analyze_current_title(current_title)

        # Generate quick wins
        if not result["current_title_analysis"]["has_number"]:
            result["quick_wins"].append("Add a number to your title (e.g., '7 Ways...', 'Top 10...')")
        if not result["current_title_analysis"]["has_brackets"]:
            result["quick_wins"].append("Add brackets with year or qualifier (e.g., '[2025 Guide]')")
        if not result["current_title_analysis"]["has_power_words"]:
            result["quick_wins"].append("Add power words: proven, ultimate, essential, complete")

    if current_description:
        result["current_meta_analysis"] = analyze_current_meta(current_description)

        if not result["current_meta_analysis"]["has_cta"]:
            result["quick_wins"].append("Add a CTA to meta: 'Learn more', 'Discover how', 'Read now'")

    result["title_variations"] = generate_title_variations(keyword, current_title)
    result["meta_variations"] = generate_meta_variations(keyword, current_title)

    return result


def main():
    parser = argparse.ArgumentParser(description="CTR optimization for titles and meta descriptions")
    parser.add_argument("--title", "-t", help="Current title tag")
    parser.add_argument("--description", "-d", help="Current meta description")
    parser.add_argument("--keyword", "-k", required=True, help="Target keyword")
    parser.add_argument("--format", "-f", choices=["json", "summary"], default="json",
                        help="Output format")

    args = parser.parse_args()

    result = optimize_for_ctr(args.title, args.description, args.keyword)

    if args.format == "summary":
        print("\n=== CTR Optimization Report ===\n")
        print(f"Target keyword: {args.keyword}\n")

        if result["current_title_analysis"]:
            print(f"Current title score: {result['current_title_analysis']['score']}/100")
            if result["current_title_analysis"]["issues"]:
                print("Issues:")
                for issue in result["current_title_analysis"]["issues"]:
                    print(f"  - {issue}")
            print()

        if result["quick_wins"]:
            print("Quick Wins:")
            for win in result["quick_wins"]:
                print(f"  ✓ {win}")
            print()

        print("Title Variations:")
        for i, var in enumerate(result["title_variations"][:5], 1):
            print(f"  {i}. {var['title']} ({var['length']} chars)")
        print()

        print("Meta Description Variations:")
        for i, var in enumerate(result["meta_variations"][:3], 1):
            print(f"  {i}. {var['description'][:80]}...")
            print(f"     ({var['length']} chars, {var['status']})")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
