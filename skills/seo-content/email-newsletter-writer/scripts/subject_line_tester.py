#!/usr/bin/env python3
"""
Analyze and score email subject line effectiveness.

Usage:
    python subject_line_tester.py "Your subject line here"
    python subject_line_tester.py --compare "Line 1" "Line 2" "Line 3"
    python subject_line_tester.py --generate --topic "marketing"

Output: Subject line analysis with score and recommendations
"""

import argparse
import json
import re
import random


# Scoring criteria weights
WEIGHTS = {
    "length": 15,
    "power_words": 15,
    "personalization": 10,
    "urgency": 10,
    "curiosity": 15,
    "clarity": 15,
    "spam_check": 20
}

# Power words that increase opens
POWER_WORDS = {
    "curiosity": ["secret", "revealed", "discover", "surprising", "shocking", "truth", "hidden", "unknown", "mystery"],
    "urgency": ["now", "today", "hurry", "limited", "expires", "deadline", "last chance", "final", "ending"],
    "value": ["free", "save", "bonus", "exclusive", "instant", "proven", "guaranteed", "results"],
    "personal": ["you", "your", "you're", "yourself"],
    "emotional": ["amazing", "incredible", "powerful", "breakthrough", "transform", "life-changing"]
}

# Spam trigger words
SPAM_TRIGGERS = [
    "buy now", "click here", "act now", "limited time", "order now",
    "free gift", "winner", "congratulations", "you won", "claim your",
    "100% free", "no cost", "no obligation", "risk free", "guarantee",
    "!!!!", "$$$$", "all caps", "urgent", "important", "attention"
]

# Subject line templates by category
TEMPLATES = {
    "curiosity": [
        "The surprising truth about {topic}",
        "What most people don't know about {topic}",
        "I was wrong about {topic}",
        "The {topic} mistake everyone makes",
        "{Number} things I wish I knew about {topic}"
    ],
    "benefit": [
        "How to {benefit} in {timeframe}",
        "The easy way to {benefit}",
        "{Number} ways to {benefit}",
        "Finally: {benefit} made simple",
        "Get {benefit} without {sacrifice}"
    ],
    "question": [
        "Are you making this {topic} mistake?",
        "Want to {benefit}?",
        "Struggling with {topic}?",
        "What if you could {benefit}?",
        "Ready to {action}?"
    ],
    "personal": [
        "[Name], your {topic} update",
        "A personal note about {topic}",
        "[Name], I noticed something...",
        "Quick question for you",
        "Can I share something with you?"
    ],
    "list": [
        "{Number} {topic} tips you need to know",
        "{Number} ways to {benefit} this week",
        "{Number} {topic} mistakes to avoid",
        "The top {number} {topic} trends",
        "{Number} lessons from {source}"
    ],
    "news": [
        "New: {announcement}",
        "Introducing {feature}",
        "Just released: {product}",
        "Big news about {topic}",
        "Update: {news_item}"
    ]
}


def analyze_subject_line(subject):
    """Analyze a subject line and return detailed scoring."""

    analysis = {
        "subject": subject,
        "scores": {},
        "details": {},
        "recommendations": [],
        "overall_score": 0
    }

    subject_lower = subject.lower()
    words = subject.split()

    # 1. Length analysis (optimal: 30-50 characters, 6-10 words)
    char_count = len(subject)
    word_count = len(words)

    if 30 <= char_count <= 50:
        length_score = 100
        analysis["details"]["length"] = f"{char_count} chars - Optimal"
    elif 20 <= char_count <= 60:
        length_score = 70
        analysis["details"]["length"] = f"{char_count} chars - Acceptable"
    elif char_count < 20:
        length_score = 50
        analysis["details"]["length"] = f"{char_count} chars - Too short"
        analysis["recommendations"].append("Add more descriptive words to reach 30+ characters")
    else:
        length_score = 40
        analysis["details"]["length"] = f"{char_count} chars - Too long (may be cut off)"
        analysis["recommendations"].append("Shorten to under 50 characters for mobile")

    analysis["scores"]["length"] = length_score

    # 2. Power words check
    power_word_count = 0
    found_power_words = []
    for category, words_list in POWER_WORDS.items():
        for word in words_list:
            if word.lower() in subject_lower:
                power_word_count += 1
                found_power_words.append(word)

    if power_word_count >= 2:
        power_score = 100
    elif power_word_count == 1:
        power_score = 70
    else:
        power_score = 30
        analysis["recommendations"].append("Add power words like 'discover', 'proven', or 'you'")

    analysis["scores"]["power_words"] = power_score
    analysis["details"]["power_words"] = found_power_words if found_power_words else "None found"

    # 3. Personalization check
    has_personalization = "[name]" in subject_lower or "you" in subject_lower or "your" in subject_lower
    if has_personalization:
        personalization_score = 100
        analysis["details"]["personalization"] = "Contains personalization"
    else:
        personalization_score = 40
        analysis["details"]["personalization"] = "No personalization"
        analysis["recommendations"].append("Consider adding 'you/your' or [Name] merge tag")

    analysis["scores"]["personalization"] = personalization_score

    # 4. Urgency check
    urgency_words = POWER_WORDS["urgency"]
    has_urgency = any(word in subject_lower for word in urgency_words)
    has_deadline = bool(re.search(r'\d+\s*(hour|day|week|%|off)', subject_lower))

    if has_urgency or has_deadline:
        urgency_score = 100
        analysis["details"]["urgency"] = "Contains urgency elements"
    else:
        urgency_score = 50
        analysis["details"]["urgency"] = "No urgency elements"

    analysis["scores"]["urgency"] = urgency_score

    # 5. Curiosity check
    curiosity_indicators = [
        subject.endswith("?"),
        "..." in subject,
        any(word in subject_lower for word in POWER_WORDS["curiosity"]),
        re.search(r'what|why|how|when|who', subject_lower) is not None
    ]

    curiosity_count = sum(curiosity_indicators)
    if curiosity_count >= 2:
        curiosity_score = 100
    elif curiosity_count == 1:
        curiosity_score = 70
    else:
        curiosity_score = 40
        analysis["recommendations"].append("Add curiosity elements like questions or ellipsis")

    analysis["scores"]["curiosity"] = curiosity_score
    analysis["details"]["curiosity"] = f"{curiosity_count} curiosity indicators"

    # 6. Clarity check
    has_clear_benefit = any(word in subject_lower for word in
        ["how to", "get", "save", "learn", "discover", "find", "improve"])
    has_specific = bool(re.search(r'\d+', subject))

    clarity_count = sum([has_clear_benefit, has_specific, word_count <= 10])
    if clarity_count >= 2:
        clarity_score = 100
    elif clarity_count == 1:
        clarity_score = 70
    else:
        clarity_score = 50
        analysis["recommendations"].append("Make the benefit or value clearer")

    analysis["scores"]["clarity"] = clarity_score
    analysis["details"]["clarity"] = f"Clear benefit: {has_clear_benefit}, Specific: {has_specific}"

    # 7. Spam check
    spam_count = 0
    found_spam = []
    for trigger in SPAM_TRIGGERS:
        if trigger.lower() in subject_lower:
            spam_count += 1
            found_spam.append(trigger)

    # Check for all caps
    if subject.isupper():
        spam_count += 2
        found_spam.append("ALL CAPS")

    # Check for excessive punctuation
    if re.search(r'[!?]{2,}', subject):
        spam_count += 1
        found_spam.append("Excessive punctuation")

    if spam_count == 0:
        spam_score = 100
    elif spam_count == 1:
        spam_score = 70
    else:
        spam_score = max(0, 100 - (spam_count * 20))
        analysis["recommendations"].append(f"Remove spam triggers: {', '.join(found_spam)}")

    analysis["scores"]["spam_check"] = spam_score
    analysis["details"]["spam_triggers"] = found_spam if found_spam else "None found"

    # Calculate overall score
    total = 0
    for criterion, weight in WEIGHTS.items():
        total += (analysis["scores"].get(criterion, 0) / 100) * weight

    analysis["overall_score"] = round(total, 1)

    # Overall assessment
    if analysis["overall_score"] >= 80:
        analysis["assessment"] = "Excellent - Ready to send"
    elif analysis["overall_score"] >= 60:
        analysis["assessment"] = "Good - Minor improvements possible"
    elif analysis["overall_score"] >= 40:
        analysis["assessment"] = "Fair - Needs improvement"
    else:
        analysis["assessment"] = "Poor - Significant revision needed"

    return analysis


def compare_subject_lines(subjects):
    """Compare multiple subject lines."""

    results = []
    for subject in subjects:
        analysis = analyze_subject_line(subject)
        results.append({
            "subject": subject,
            "score": analysis["overall_score"],
            "assessment": analysis["assessment"],
            "top_recommendation": analysis["recommendations"][0] if analysis["recommendations"] else None
        })

    # Sort by score
    results.sort(key=lambda x: x["score"], reverse=True)

    return {
        "ranked_results": results,
        "winner": results[0]["subject"] if results else None,
        "winner_score": results[0]["score"] if results else None
    }


def generate_subject_lines(topic, category=None, count=5):
    """Generate subject line variations."""

    if category and category in TEMPLATES:
        categories = [category]
    else:
        categories = list(TEMPLATES.keys())

    generated = []
    placeholders = {
        "topic": topic,
        "benefit": f"master {topic}",
        "timeframe": random.choice(["7 days", "30 days", "one week"]),
        "sacrifice": "the hard work",
        "action": f"improve your {topic}",
        "announcement": f"New {topic} feature",
        "feature": f"{topic} toolkit",
        "product": f"Our {topic} guide",
        "news_item": f"{topic} updates",
        "source": "experts",
        "Number": str(random.choice([3, 5, 7, 10])),
        "number": str(random.choice([3, 5, 7, 10]))
    }

    attempts = 0
    while len(generated) < count and attempts < count * 3:
        category = random.choice(categories)
        template = random.choice(TEMPLATES[category])

        try:
            subject = template.format(**placeholders)
            if subject not in generated:
                generated.append(subject)
        except KeyError:
            pass

        attempts += 1

    # Analyze generated lines
    analyzed = []
    for subject in generated:
        analysis = analyze_subject_line(subject)
        analyzed.append({
            "subject": subject,
            "score": analysis["overall_score"]
        })

    analyzed.sort(key=lambda x: x["score"], reverse=True)

    return {
        "topic": topic,
        "generated": analyzed
    }


def format_analysis(analysis, format_type="text"):
    """Format analysis output."""

    if format_type == "json":
        return json.dumps(analysis, indent=2)

    lines = []
    lines.append("\n" + "=" * 60)
    lines.append("SUBJECT LINE ANALYSIS")
    lines.append("=" * 60)

    lines.append(f"\nSubject: \"{analysis['subject']}\"")
    lines.append(f"Overall Score: {analysis['overall_score']}/100")
    lines.append(f"Assessment: {analysis['assessment']}")

    lines.append("\n--- SCORES ---")
    for criterion, score in analysis['scores'].items():
        weight = WEIGHTS.get(criterion, 0)
        bar = "█" * (score // 10) + "░" * (10 - score // 10)
        lines.append(f"  {criterion.replace('_', ' ').title()}: {bar} {score} (weight: {weight}%)")

    lines.append("\n--- DETAILS ---")
    for key, value in analysis['details'].items():
        if isinstance(value, list):
            value = ", ".join(value) if value else "None"
        lines.append(f"  {key.replace('_', ' ').title()}: {value}")

    if analysis['recommendations']:
        lines.append("\n--- RECOMMENDATIONS ---")
        for rec in analysis['recommendations']:
            lines.append(f"  → {rec}")

    return "\n".join(lines)


def format_comparison(comparison, format_type="text"):
    """Format comparison output."""

    if format_type == "json":
        return json.dumps(comparison, indent=2)

    lines = []
    lines.append("\n" + "=" * 60)
    lines.append("SUBJECT LINE COMPARISON")
    lines.append("=" * 60)

    lines.append(f"\nWinner: \"{comparison['winner']}\"")
    lines.append(f"Score: {comparison['winner_score']}/100")

    lines.append("\n--- RANKINGS ---")
    for i, result in enumerate(comparison['ranked_results'], 1):
        medal = ["🥇", "🥈", "🥉"][i-1] if i <= 3 else f"{i}."
        lines.append(f"\n{medal} Score: {result['score']}/100")
        lines.append(f"   \"{result['subject']}\"")
        if result['top_recommendation']:
            lines.append(f"   Tip: {result['top_recommendation']}")

    return "\n".join(lines)


def interactive_mode():
    """Interactive subject line testing."""

    print("\n=== Subject Line Tester ===\n")

    while True:
        print("\nOptions:")
        print("  1. Analyze a subject line")
        print("  2. Compare multiple subject lines")
        print("  3. Generate subject lines")
        print("  4. Exit")

        choice = input("\nSelect option (1-4): ").strip()

        if choice == "1":
            subject = input("Enter subject line: ").strip()
            if subject:
                analysis = analyze_subject_line(subject)
                print(format_analysis(analysis))

        elif choice == "2":
            subjects = []
            print("Enter subject lines (empty line to finish):")
            while True:
                line = input(f"  {len(subjects) + 1}. ").strip()
                if not line:
                    break
                subjects.append(line)

            if len(subjects) >= 2:
                comparison = compare_subject_lines(subjects)
                print(format_comparison(comparison))
            else:
                print("Need at least 2 subject lines to compare")

        elif choice == "3":
            topic = input("Enter topic: ").strip() or "marketing"
            count = input("How many to generate [5]: ").strip()
            count = int(count) if count else 5

            result = generate_subject_lines(topic, count=count)
            print(f"\n--- GENERATED SUBJECT LINES FOR '{topic}' ---\n")
            for item in result["generated"]:
                print(f"  [{item['score']}/100] {item['subject']}")

        elif choice == "4":
            break

        else:
            print("Invalid option")


def main():
    parser = argparse.ArgumentParser(description='Analyze email subject lines')
    parser.add_argument('subject', nargs='?', help='Subject line to analyze')
    parser.add_argument('--compare', '-c', nargs='+', help='Compare multiple subject lines')
    parser.add_argument('--generate', '-g', action='store_true', help='Generate subject lines')
    parser.add_argument('--topic', '-t', help='Topic for generation')
    parser.add_argument('--count', type=int, default=5, help='Number to generate')
    parser.add_argument('--format', '-f', choices=['json', 'text'],
                        default='text', help='Output format')
    parser.add_argument('--interactive', '-i', action='store_true',
                        help='Interactive mode')

    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
        return

    if args.compare:
        comparison = compare_subject_lines(args.compare)
        print(format_comparison(comparison, args.format))
        return

    if args.generate:
        topic = args.topic or "marketing"
        result = generate_subject_lines(topic, count=args.count)
        if args.format == "json":
            print(json.dumps(result, indent=2))
        else:
            print(f"\n--- GENERATED SUBJECT LINES FOR '{topic}' ---\n")
            for item in result["generated"]:
                print(f"  [{item['score']}/100] {item['subject']}")
        return

    if args.subject:
        analysis = analyze_subject_line(args.subject)
        print(format_analysis(analysis, args.format))
        return

    parser.print_help()


if __name__ == '__main__':
    main()
