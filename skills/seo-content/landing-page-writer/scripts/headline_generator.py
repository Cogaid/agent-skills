#!/usr/bin/env python3
"""
Generate landing page headline variations.

Usage:
    python headline_generator.py --product "CRM Software" --benefit "close more deals"
    python headline_generator.py --interactive
    python headline_generator.py --template benefit

Output: Multiple headline variations for A/B testing
"""

import argparse
import json
import random


# Headline templates
TEMPLATES = {
    "benefit": [
        "Get {benefit} in {timeframe}",
        "The {adjective} Way to {benefit}",
        "{benefit} — Without {sacrifice}",
        "Finally, {benefit} Made Easy",
        "Discover How to {benefit}"
    ],
    "question": [
        "Want to {benefit}?",
        "Ready to {benefit}?",
        "Struggling to {benefit}?",
        "What If You Could {benefit}?",
        "Why Aren't You {benefit_ing} Yet?"
    ],
    "number": [
        "{number} Ways to {benefit}",
        "{number} Steps to {benefit}",
        "{number} Secrets to {benefit}",
        "Join {number}+ {audience} Who {benefit}",
        "{number} Reasons to {action}"
    ],
    "curiosity": [
        "The Secret to {benefit}",
        "What {audience} Know About {topic}",
        "The Surprising Truth About {topic}",
        "Why {common_approach} Doesn't Work",
        "The Hidden Cost of {pain_point}"
    ],
    "command": [
        "Stop {pain_point}. Start {benefit_ing}.",
        "Transform Your {area}",
        "Unlock {benefit}",
        "Master {skill}",
        "Accelerate Your {goal}"
    ],
    "how_to": [
        "How to {benefit} in {timeframe}",
        "How to {benefit} Without {sacrifice}",
        "How to {benefit} Even If {obstacle}",
        "How {audience} Are {benefit_ing}",
        "How to Go From {before} to {after}"
    ],
    "social_proof": [
        "Join {number}+ {audience} {benefit_ing}",
        "See Why {number} {companies} Trust {product}",
        "The #{ranking} {category}",
        "{audience} Love {product}. Here's Why.",
        "Trusted by {type} at {example_companies}"
    ],
    "problem_agitate": [
        "Tired of {pain_point}?",
        "{pain_point} Is Killing Your {area}",
        "Stop Losing {loss} to {pain_point}",
        "The {pain_point} Problem, Solved",
        "{pain_point} Ends Here"
    ]
}

# Power words by category
POWER_WORDS = {
    "urgency": ["now", "today", "instant", "fast", "quick", "immediately"],
    "exclusivity": ["exclusive", "limited", "secret", "insider", "VIP", "premium"],
    "value": ["free", "bonus", "save", "discount", "guaranteed", "proven"],
    "results": ["transform", "boost", "increase", "grow", "improve", "maximize"],
    "emotion": ["amazing", "breakthrough", "revolutionary", "game-changing", "powerful"]
}

# Adjectives
ADJECTIVES = [
    "simple", "easy", "proven", "powerful", "complete", "ultimate",
    "essential", "smart", "modern", "effective", "fastest", "best"
]

# Timeframes
TIMEFRAMES = [
    "30 days", "7 days", "24 hours", "minutes", "seconds",
    "one week", "one month", "less time"
]


def generate_headlines(
    product=None,
    benefit=None,
    audience=None,
    pain_point=None,
    template_type=None,
    count=10
):
    """Generate headline variations."""

    # Defaults
    product = product or "[Product]"
    benefit = benefit or "[achieve result]"
    audience = audience or "[audience]"
    pain_point = pain_point or "[problem]"

    # Create benefit variations
    benefit_ing = benefit.replace("get ", "getting ").replace("save ", "saving ")
    if not benefit_ing.endswith("ing"):
        # Simple conversion
        words = benefit.split()
        if words:
            words[0] = words[0] + "ing" if not words[0].endswith("ing") else words[0]
            benefit_ing = " ".join(words)

    # Variables for templates
    vars = {
        "product": product,
        "benefit": benefit,
        "benefit_ing": benefit_ing,
        "audience": audience,
        "pain_point": pain_point,
        "adjective": random.choice(ADJECTIVES),
        "timeframe": random.choice(TIMEFRAMES),
        "number": random.choice(["3", "5", "7", "10", "100", "1000+"]),
        "sacrifice": "the hard work",
        "obstacle": "you've failed before",
        "topic": pain_point,
        "common_approach": "the old way",
        "area": "business",
        "skill": benefit,
        "goal": "success",
        "before": pain_point,
        "after": benefit,
        "loss": "time and money",
        "companies": "companies",
        "category": "solution",
        "ranking": "1",
        "type": "teams",
        "example_companies": "leading companies",
        "action": f"use {product}"
    }

    headlines = []

    # Select template types
    if template_type:
        types = [template_type]
    else:
        types = list(TEMPLATES.keys())

    # Generate headlines
    for _ in range(count * 2):  # Generate extra, then dedupe
        template_type = random.choice(types)
        template = random.choice(TEMPLATES[template_type])

        # Refresh random values
        vars["adjective"] = random.choice(ADJECTIVES)
        vars["timeframe"] = random.choice(TIMEFRAMES)
        vars["number"] = random.choice(["3", "5", "7", "10", "100", "1000+", "10,000+"])

        try:
            headline = template.format(**vars)
            if headline not in headlines:
                headlines.append(headline)
        except KeyError:
            continue

        if len(headlines) >= count:
            break

    return headlines[:count]


def add_power_words(headline, category="results"):
    """Add power words to enhance headline."""

    words = POWER_WORDS.get(category, POWER_WORDS["results"])
    power_word = random.choice(words)

    # Different positions
    variations = [
        f"{power_word.title()}: {headline}",
        f"{headline} — {power_word.title()}",
        headline.replace("to ", f"to {power_word} ")
    ]

    return variations


def analyze_headline(headline):
    """Analyze headline effectiveness."""

    analysis = {
        "headline": headline,
        "character_count": len(headline),
        "word_count": len(headline.split()),
        "scores": {},
        "suggestions": []
    }

    # Length check
    if len(headline) < 40:
        analysis["scores"]["length"] = "good"
    elif len(headline) < 60:
        analysis["scores"]["length"] = "okay"
    else:
        analysis["scores"]["length"] = "too_long"
        analysis["suggestions"].append("Consider shortening headline")

    # Power words check
    power_word_count = 0
    for category in POWER_WORDS.values():
        for word in category:
            if word.lower() in headline.lower():
                power_word_count += 1

    if power_word_count >= 2:
        analysis["scores"]["power_words"] = "good"
    elif power_word_count >= 1:
        analysis["scores"]["power_words"] = "okay"
    else:
        analysis["scores"]["power_words"] = "weak"
        analysis["suggestions"].append("Add power words for more impact")

    # Number check
    if any(char.isdigit() for char in headline):
        analysis["scores"]["specificity"] = "good"
    else:
        analysis["scores"]["specificity"] = "okay"
        analysis["suggestions"].append("Consider adding numbers for specificity")

    # Question check
    if headline.endswith("?"):
        analysis["scores"]["engagement"] = "good"
    else:
        analysis["scores"]["engagement"] = "neutral"

    # Calculate overall score
    score_map = {"good": 3, "okay": 2, "neutral": 2, "weak": 1, "too_long": 1}
    scores = [score_map.get(s, 2) for s in analysis["scores"].values()]
    analysis["overall_score"] = round(sum(scores) / len(scores) * 33.3, 1)

    return analysis


def interactive_mode():
    """Interactive headline generation."""

    print("\n=== Headline Generator ===\n")

    product = input("Product/Service name: ").strip() or None
    benefit = input("Main benefit (e.g., 'close more deals'): ").strip() or None
    audience = input("Target audience (e.g., 'marketers'): ").strip() or None
    pain_point = input("Pain point (e.g., 'wasted time'): ").strip() or None

    print(f"\nTemplate types: {', '.join(TEMPLATES.keys())}")
    template = input("Template type (or 'all') [all]: ").strip() or None

    count = input("Number of headlines [10]: ").strip()
    count = int(count) if count else 10

    headlines = generate_headlines(
        product=product,
        benefit=benefit,
        audience=audience,
        pain_point=pain_point,
        template_type=template if template != "all" else None,
        count=count
    )

    print("\n" + "=" * 50)
    print("GENERATED HEADLINES")
    print("=" * 50)

    for i, h in enumerate(headlines, 1):
        print(f"\n{i}. {h}")

    # Analyze top ones
    if input("\n\nAnalyze these headlines? (y/n) [n]: ").strip().lower() == "y":
        print("\n--- ANALYSIS ---")
        for h in headlines[:5]:
            analysis = analyze_headline(h)
            print(f"\n\"{h[:50]}...\"")
            print(f"  Score: {analysis['overall_score']}/100")
            if analysis['suggestions']:
                for s in analysis['suggestions']:
                    print(f"  → {s}")


def main():
    parser = argparse.ArgumentParser(description='Generate landing page headlines')
    parser.add_argument('--product', '-p', help='Product or service name')
    parser.add_argument('--benefit', '-b', help='Main benefit')
    parser.add_argument('--audience', '-a', help='Target audience')
    parser.add_argument('--pain', help='Pain point')
    parser.add_argument('--template', '-t', choices=list(TEMPLATES.keys()),
                        help='Template type')
    parser.add_argument('--count', '-c', type=int, default=10,
                        help='Number of headlines')
    parser.add_argument('--format', '-f', choices=['json', 'text'],
                        default='text', help='Output format')
    parser.add_argument('--interactive', '-i', action='store_true',
                        help='Interactive mode')
    parser.add_argument('--analyze', help='Analyze a specific headline')
    parser.add_argument('--list', '-l', action='store_true',
                        help='List template types')

    args = parser.parse_args()

    if args.list:
        print("\nHeadline Template Types:\n")
        for ttype, templates in TEMPLATES.items():
            print(f"  {ttype}:")
            for t in templates[:2]:
                print(f"    • {t}")
            print()
        return

    if args.analyze:
        analysis = analyze_headline(args.analyze)
        if args.format == "json":
            print(json.dumps(analysis, indent=2))
        else:
            print(f"\nAnalysis: \"{args.analyze}\"")
            print(f"Score: {analysis['overall_score']}/100")
            print(f"Length: {analysis['character_count']} chars, {analysis['word_count']} words")
            for suggestion in analysis['suggestions']:
                print(f"  → {suggestion}")
        return

    if args.interactive:
        interactive_mode()
        return

    headlines = generate_headlines(
        product=args.product,
        benefit=args.benefit,
        audience=args.audience,
        pain_point=args.pain,
        template_type=args.template,
        count=args.count
    )

    if args.format == "json":
        print(json.dumps({"headlines": headlines}, indent=2))
    else:
        print("\n=== Generated Headlines ===\n")
        for i, h in enumerate(headlines, 1):
            print(f"{i}. {h}")


if __name__ == '__main__':
    main()
