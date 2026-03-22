#!/usr/bin/env python3
"""
Generate seed keywords from a topic.

Usage:
    python seed_keywords.py --topic "email marketing"
    python seed_keywords.py --topic "seo" --depth comprehensive

Output: Categorized seed keywords for expansion
"""

import argparse
import json
import sys


# Seed generation patterns
SEED_PATTERNS = {
    "core": [
        "{topic}",
        "{topic} guide",
        "{topic} tutorial",
        "{topic} tips",
        "{topic} strategies",
    ],
    "how_to": [
        "how to {topic}",
        "how to do {topic}",
        "how to use {topic}",
        "how to start {topic}",
        "how to improve {topic}",
    ],
    "what_is": [
        "what is {topic}",
        "{topic} definition",
        "{topic} meaning",
        "{topic} explained",
        "{topic} basics",
    ],
    "comparison": [
        "best {topic}",
        "top {topic}",
        "{topic} vs",
        "{topic} alternatives",
        "{topic} comparison",
    ],
    "problems": [
        "{topic} problems",
        "{topic} mistakes",
        "{topic} issues",
        "{topic} challenges",
        "{topic} fails",
    ],
    "solutions": [
        "{topic} solutions",
        "{topic} fix",
        "improve {topic}",
        "optimize {topic}",
        "{topic} best practices",
    ],
    "specific": [
        "{topic} for beginners",
        "{topic} for business",
        "{topic} for small business",
        "{topic} examples",
        "{topic} templates",
    ],
    "tools": [
        "{topic} tools",
        "{topic} software",
        "{topic} apps",
        "{topic} platforms",
        "free {topic} tools",
    ],
    "learning": [
        "learn {topic}",
        "{topic} course",
        "{topic} training",
        "{topic} certification",
        "{topic} books",
    ],
    "advanced": [
        "advanced {topic}",
        "{topic} techniques",
        "{topic} hacks",
        "{topic} secrets",
        "professional {topic}",
    ]
}

# Industry-specific modifiers
INDUSTRY_MODIFIERS = {
    "marketing": ["digital", "content", "social media", "email", "influencer"],
    "business": ["small business", "startup", "enterprise", "B2B", "B2C"],
    "technology": ["software", "app", "platform", "automation", "AI"],
    "ecommerce": ["online store", "dropshipping", "Amazon", "Shopify", "retail"],
    "finance": ["personal", "investment", "budgeting", "banking", "crypto"],
    "health": ["fitness", "nutrition", "mental", "wellness", "medical"],
    "education": ["online", "course", "training", "certification", "learning"],
}


def generate_seeds(topic, depth="standard"):
    """Generate seed keywords for a topic."""
    topic = topic.lower().strip()
    seeds = {
        "core": [],
        "informational": [],
        "commercial": [],
        "transactional": [],
        "long_tail": []
    }

    # Core seeds
    for pattern in SEED_PATTERNS["core"]:
        seeds["core"].append(pattern.format(topic=topic))

    # Informational seeds (what, how, why)
    for pattern in SEED_PATTERNS["what_is"] + SEED_PATTERNS["how_to"]:
        seeds["informational"].append(pattern.format(topic=topic))

    # Commercial seeds (best, top, comparison)
    for pattern in SEED_PATTERNS["comparison"]:
        seeds["commercial"].append(pattern.format(topic=topic))

    # Problem/solution seeds
    for pattern in SEED_PATTERNS["problems"] + SEED_PATTERNS["solutions"]:
        seeds["long_tail"].append(pattern.format(topic=topic))

    if depth == "comprehensive":
        # Add more categories
        for pattern in SEED_PATTERNS["specific"]:
            seeds["long_tail"].append(pattern.format(topic=topic))

        for pattern in SEED_PATTERNS["tools"]:
            seeds["commercial"].append(pattern.format(topic=topic))

        for pattern in SEED_PATTERNS["learning"]:
            seeds["informational"].append(pattern.format(topic=topic))

        for pattern in SEED_PATTERNS["advanced"]:
            seeds["long_tail"].append(pattern.format(topic=topic))

        # Add transactional
        transactional_patterns = [
            f"buy {topic}",
            f"{topic} pricing",
            f"{topic} cost",
            f"{topic} free trial",
            f"{topic} discount",
            f"hire {topic}",
            f"{topic} service",
            f"{topic} agency",
        ]
        seeds["transactional"] = transactional_patterns

    return seeds


def suggest_related_topics(topic):
    """Suggest related topics to research."""
    suggestions = []

    # Generic related patterns
    related_patterns = [
        f"{topic} automation",
        f"{topic} analytics",
        f"{topic} ROI",
        f"{topic} metrics",
        f"{topic} trends",
        f"{topic} statistics",
        f"{topic} industry",
        f"{topic} case studies",
    ]

    suggestions.extend(related_patterns)

    # Check for industry overlap
    topic_lower = topic.lower()
    for industry, modifiers in INDUSTRY_MODIFIERS.items():
        for modifier in modifiers:
            if modifier in topic_lower or industry in topic_lower:
                # Add cross-industry suggestions
                suggestions.append(f"{modifier} {topic}")

    return suggestions[:10]


def categorize_by_intent(seeds):
    """Categorize seeds by search intent."""
    intent_map = {
        "informational": [],
        "navigational": [],
        "commercial": [],
        "transactional": []
    }

    intent_signals = {
        "informational": ["what", "how", "why", "guide", "tutorial", "learn", "basics", "explained"],
        "commercial": ["best", "top", "vs", "comparison", "review", "alternative"],
        "transactional": ["buy", "price", "cost", "discount", "free", "hire", "service"]
    }

    all_seeds = []
    for category in seeds.values():
        all_seeds.extend(category)

    for seed in set(all_seeds):
        seed_lower = seed.lower()
        categorized = False

        for intent, signals in intent_signals.items():
            if any(signal in seed_lower for signal in signals):
                intent_map[intent].append(seed)
                categorized = True
                break

        if not categorized:
            intent_map["informational"].append(seed)

    return intent_map


def main():
    parser = argparse.ArgumentParser(description="Generate seed keywords")
    parser.add_argument("--topic", "-t", required=True, help="Topic to generate seeds for")
    parser.add_argument("--depth", "-d", choices=["minimal", "standard", "comprehensive"],
                        default="standard", help="Depth of seed generation")
    parser.add_argument("--format", "-f", choices=["json", "list"], default="json",
                        help="Output format")

    args = parser.parse_args()

    seeds = generate_seeds(args.topic, args.depth)
    related = suggest_related_topics(args.topic)
    by_intent = categorize_by_intent(seeds)

    result = {
        "topic": args.topic,
        "depth": args.depth,
        "seeds_by_category": seeds,
        "seeds_by_intent": by_intent,
        "related_topics": related,
        "total_seeds": sum(len(v) for v in seeds.values()),
        "next_steps": [
            "Use expand_keywords.py to generate long-tail variations",
            "Use analyze_intent.py to verify intent classifications",
            "Use prioritize_keywords.py after collecting volume/difficulty data"
        ]
    }

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print(f"\n=== Seed Keywords for: {args.topic} ===\n")
        for category, keywords in seeds.items():
            if keywords:
                print(f"\n{category.upper()}:")
                for kw in keywords:
                    print(f"  • {kw}")

        print(f"\n=== Related Topics ===")
        for topic in related:
            print(f"  • {topic}")

        print(f"\nTotal seeds generated: {result['total_seeds']}")


if __name__ == "__main__":
    main()
