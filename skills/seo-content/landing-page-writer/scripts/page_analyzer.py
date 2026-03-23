#!/usr/bin/env python3
"""
Analyze landing page copy effectiveness.

Usage:
    python page_analyzer.py page_copy.txt
    python page_analyzer.py --checklist
    python page_analyzer.py --score page_copy.txt

Output: Analysis and optimization recommendations
"""

import argparse
import json
import re


# Essential elements checklist
ESSENTIAL_ELEMENTS = {
    "headline": {
        "weight": 20,
        "patterns": [r"^#\s+.+", r"<h1>.+</h1>"],
        "check": "Has clear headline"
    },
    "subheadline": {
        "weight": 10,
        "patterns": [r"^##\s+.+", r"<h2>.+</h2>"],
        "check": "Has supporting subheadline"
    },
    "cta": {
        "weight": 20,
        "patterns": [r"\[.*(Get|Start|Join|Download|Sign|Try|Claim).*\]", r"button", r"CTA"],
        "check": "Has clear call-to-action"
    },
    "benefit": {
        "weight": 15,
        "keywords": ["save", "get", "increase", "improve", "boost", "reduce", "free", "easy"],
        "check": "Communicates benefits"
    },
    "social_proof": {
        "weight": 10,
        "keywords": ["testimonial", "review", "customer", "trusted", "clients", "companies", "users"],
        "check": "Includes social proof"
    },
    "urgency": {
        "weight": 5,
        "keywords": ["now", "today", "limited", "hurry", "don't miss", "deadline"],
        "check": "Creates urgency"
    }
}

# Power words
POWER_WORDS = [
    "free", "new", "you", "save", "guaranteed", "proven", "easy", "discover",
    "results", "secret", "instant", "how to", "now", "today", "because",
    "announcing", "introducing", "amazing", "sensational", "remarkable",
    "revolutionary", "startling", "miracle", "magic", "quick", "hurry"
]

# Words to avoid
AVOID_WORDS = [
    "maybe", "possibly", "might", "could", "try", "hope", "think",
    "submit", "click here", "buy now", "spam", "dear friend",
    "once in a lifetime", "winner"
]


def analyze_copy(content):
    """Analyze landing page copy."""

    content_lower = content.lower()
    words = content.split()
    sentences = re.split(r'[.!?]+', content)

    analysis = {
        "metrics": {},
        "elements": {},
        "power_words": [],
        "avoid_words": [],
        "readability": {},
        "recommendations": [],
        "scores": {}
    }

    # Basic metrics
    analysis["metrics"]["word_count"] = len(words)
    analysis["metrics"]["sentence_count"] = len([s for s in sentences if s.strip()])
    analysis["metrics"]["avg_sentence_length"] = round(
        len(words) / max(len(sentences), 1), 1
    )

    # Check essential elements
    total_score = 0
    for element, config in ESSENTIAL_ELEMENTS.items():
        found = False

        if "patterns" in config:
            for pattern in config["patterns"]:
                if re.search(pattern, content, re.IGNORECASE | re.MULTILINE):
                    found = True
                    break

        if "keywords" in config and not found:
            for keyword in config["keywords"]:
                if keyword.lower() in content_lower:
                    found = True
                    break

        analysis["elements"][element] = {
            "found": found,
            "weight": config["weight"],
            "description": config["check"]
        }

        if found:
            total_score += config["weight"]

    analysis["scores"]["elements"] = total_score

    # Power words analysis
    for word in POWER_WORDS:
        if word.lower() in content_lower:
            analysis["power_words"].append(word)

    power_score = min(20, len(analysis["power_words"]) * 4)
    analysis["scores"]["power_words"] = power_score

    # Avoid words check
    for word in AVOID_WORDS:
        if word.lower() in content_lower:
            analysis["avoid_words"].append(word)

    avoid_penalty = len(analysis["avoid_words"]) * 3
    analysis["scores"]["avoid_penalty"] = -avoid_penalty

    # Readability (simplified Flesch-Kincaid)
    syllable_count = sum(count_syllables(w) for w in words)
    if len(words) > 0 and len(sentences) > 0:
        fk_grade = 0.39 * (len(words) / len(sentences)) + 11.8 * (syllable_count / len(words)) - 15.59
        analysis["readability"]["flesch_kincaid_grade"] = round(max(0, fk_grade), 1)

        if fk_grade <= 8:
            analysis["readability"]["assessment"] = "Easy to read"
            analysis["scores"]["readability"] = 10
        elif fk_grade <= 12:
            analysis["readability"]["assessment"] = "Moderate"
            analysis["scores"]["readability"] = 5
        else:
            analysis["readability"]["assessment"] = "Difficult"
            analysis["scores"]["readability"] = 0
            analysis["recommendations"].append("Simplify language for easier reading")

    # Calculate total score
    analysis["scores"]["total"] = max(0, min(100,
        analysis["scores"]["elements"] +
        analysis["scores"]["power_words"] +
        analysis["scores"].get("readability", 0) +
        analysis["scores"]["avoid_penalty"]
    ))

    # Generate recommendations
    for element, data in analysis["elements"].items():
        if not data["found"]:
            analysis["recommendations"].append(f"Add {element}: {data['description']}")

    if len(analysis["power_words"]) < 3:
        analysis["recommendations"].append("Add more power words to increase impact")

    if analysis["avoid_words"]:
        analysis["recommendations"].append(f"Remove weak words: {', '.join(analysis['avoid_words'])}")

    if analysis["metrics"]["avg_sentence_length"] > 20:
        analysis["recommendations"].append("Shorten sentences for better readability")

    return analysis


def count_syllables(word):
    """Simple syllable counter."""
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for i in range(1, len(word)):
        if word[i] in vowels and word[i - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    return max(1, count)


def generate_checklist():
    """Generate landing page checklist."""

    checklist = {
        "above_the_fold": [
            "Compelling headline (benefit-driven)",
            "Clear subheadline",
            "Hero image or video",
            "Primary CTA button",
            "Trust indicator (logo, badge, stat)"
        ],
        "copy_elements": [
            "Problem statement",
            "Solution introduction",
            "Key benefits (3-5)",
            "Features with benefits",
            "Social proof (testimonials, logos)",
            "FAQ section",
            "Clear pricing (if applicable)"
        ],
        "cta_optimization": [
            "Action-oriented button text",
            "Contrasting button color",
            "Single primary CTA",
            "Value proposition in CTA",
            "Reduced form friction"
        ],
        "trust_elements": [
            "Customer testimonials",
            "Company logos",
            "Statistics/metrics",
            "Security badges",
            "Money-back guarantee"
        ],
        "technical": [
            "Mobile responsive",
            "Fast load time (<3s)",
            "Working links",
            "Form validation",
            "Analytics tracking"
        ]
    }

    return checklist


def format_analysis(analysis, format_type="text"):
    """Format analysis output."""

    if format_type == "json":
        return json.dumps(analysis, indent=2)

    lines = []
    lines.append("\n" + "=" * 60)
    lines.append("LANDING PAGE COPY ANALYSIS")
    lines.append("=" * 60)

    lines.append(f"\n--- OVERALL SCORE: {analysis['scores']['total']}/100 ---")

    lines.append("\n--- METRICS ---")
    for metric, value in analysis["metrics"].items():
        lines.append(f"  {metric}: {value}")

    lines.append("\n--- ESSENTIAL ELEMENTS ---")
    for element, data in analysis["elements"].items():
        status = "✓" if data["found"] else "✗"
        lines.append(f"  {status} {element} ({data['weight']}pts)")

    lines.append("\n--- POWER WORDS FOUND ---")
    if analysis["power_words"]:
        lines.append(f"  {', '.join(analysis['power_words'])}")
    else:
        lines.append("  None found")

    if analysis["avoid_words"]:
        lines.append("\n--- WORDS TO AVOID ---")
        lines.append(f"  ⚠ {', '.join(analysis['avoid_words'])}")

    if analysis.get("readability"):
        lines.append("\n--- READABILITY ---")
        lines.append(f"  Grade Level: {analysis['readability'].get('flesch_kincaid_grade', 'N/A')}")
        lines.append(f"  Assessment: {analysis['readability'].get('assessment', 'N/A')}")

    if analysis["recommendations"]:
        lines.append("\n--- RECOMMENDATIONS ---")
        for rec in analysis["recommendations"]:
            lines.append(f"  → {rec}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description='Analyze landing page copy')
    parser.add_argument('file', nargs='?', help='Text file with page copy')
    parser.add_argument('--checklist', '-c', action='store_true',
                        help='Show landing page checklist')
    parser.add_argument('--score', '-s', action='store_true',
                        help='Show score only')
    parser.add_argument('--format', '-f', choices=['json', 'text'],
                        default='text', help='Output format')

    args = parser.parse_args()

    if args.checklist:
        checklist = generate_checklist()
        if args.format == "json":
            print(json.dumps(checklist, indent=2))
        else:
            print("\n=== LANDING PAGE CHECKLIST ===\n")
            for section, items in checklist.items():
                print(f"\n{section.upper().replace('_', ' ')}:")
                for item in items:
                    print(f"  [ ] {item}")
        return

    if not args.file:
        parser.print_help()
        return

    try:
        with open(args.file, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {args.file}")
        return

    analysis = analyze_copy(content)

    if args.score:
        print(f"Score: {analysis['scores']['total']}/100")
        return

    print(format_analysis(analysis, args.format))


if __name__ == '__main__':
    main()
