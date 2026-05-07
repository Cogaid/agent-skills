#!/usr/bin/env python3
"""Check readability of a legal document and suggest improvements.

Usage:
    python readability_check.py --input terms.md --target-grade 8
    python readability_check.py --input terms.md --output readability-report.json
"""

import argparse
import json
import math
import re
import sys


def count_syllables(word):
    """Estimate syllable count for a word."""
    word = word.lower().strip()
    if not word:
        return 0
    if len(word) <= 3:
        return 1
    word = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", word)
    word = re.sub(r"^y", "", word)
    matches = re.findall(r"[aeiouy]{1,2}", word)
    return max(1, len(matches))


def analyze_readability(text):
    """Analyze text readability using multiple formulas."""
    # Clean markdown formatting
    clean = re.sub(r"#+ ", "", text)
    clean = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", clean)
    clean = re.sub(r"[*_`~]", "", clean)
    clean = re.sub(r"\|[^\n]+\|", "", clean)
    clean = re.sub(r"```[\s\S]*?```", "", clean)
    clean = re.sub(r"\n{2,}", "\n", clean)

    sentences = re.split(r"[.!?]+", clean)
    sentences = [s.strip() for s in sentences if s.strip() and len(s.strip().split()) > 2]

    words = re.findall(r"\b[a-zA-Z]+\b", clean)

    if not sentences or not words:
        return {"error": "Insufficient text for analysis"}

    total_sentences = len(sentences)
    total_words = len(words)
    total_syllables = sum(count_syllables(w) for w in words)
    complex_words = [w for w in words if count_syllables(w) >= 3]
    long_sentences = [s for s in sentences if len(s.split()) > 25]

    # Flesch-Kincaid Grade Level
    fk_grade = (0.39 * (total_words / total_sentences) + 11.8 * (total_syllables / total_words) - 15.59)

    # Flesch Reading Ease
    fre = 206.835 - 1.015 * (total_words / total_sentences) - 84.6 * (total_syllables / total_words)

    # Gunning Fog Index
    fog = 0.4 * ((total_words / total_sentences) + 100 * (len(complex_words) / total_words))

    # Average sentence length
    avg_sentence_length = total_words / total_sentences

    return {
        "statistics": {
            "total_words": total_words,
            "total_sentences": total_sentences,
            "total_syllables": total_syllables,
            "average_sentence_length": round(avg_sentence_length, 1),
            "complex_word_count": len(complex_words),
            "complex_word_percentage": round(100 * len(complex_words) / total_words, 1),
            "long_sentence_count": len(long_sentences),
        },
        "scores": {
            "flesch_kincaid_grade": round(fk_grade, 1),
            "flesch_reading_ease": round(max(0, min(100, fre)), 1),
            "gunning_fog_index": round(fog, 1),
        },
        "interpretation": {
            "grade_level": f"Grade {round(fk_grade)}",
            "reading_ease": (
                "Very Easy" if fre >= 80 else
                "Easy" if fre >= 60 else
                "Moderate" if fre >= 40 else
                "Difficult" if fre >= 20 else
                "Very Difficult"
            ),
        },
    }


def generate_suggestions(analysis, target_grade):
    """Generate improvement suggestions based on analysis."""
    suggestions = []
    stats = analysis["statistics"]
    scores = analysis["scores"]

    if scores["flesch_kincaid_grade"] > target_grade:
        suggestions.append({
            "priority": "High",
            "issue": f"Grade level ({scores['flesch_kincaid_grade']}) exceeds target ({target_grade})",
            "suggestion": "Simplify sentence structure and replace complex words with simpler alternatives",
        })

    if stats["average_sentence_length"] > 20:
        suggestions.append({
            "priority": "High",
            "issue": f"Average sentence length ({stats['average_sentence_length']} words) is too long",
            "suggestion": "Break long sentences into shorter ones. Target 15-20 words per sentence.",
        })

    if stats["complex_word_percentage"] > 15:
        suggestions.append({
            "priority": "Medium",
            "issue": f"Complex word usage ({stats['complex_word_percentage']}%) is high",
            "suggestion": "Replace multi-syllable words with simpler alternatives where possible",
        })

    if stats["long_sentence_count"] > 0:
        suggestions.append({
            "priority": "Medium",
            "issue": f"{stats['long_sentence_count']} sentences exceed 25 words",
            "suggestion": "Identify and split sentences longer than 25 words",
        })

    if not suggestions:
        suggestions.append({
            "priority": "Info",
            "issue": "Document meets readability targets",
            "suggestion": "No changes needed",
        })

    return suggestions


def main():
    parser = argparse.ArgumentParser(
        description="Check readability of a legal document and provide improvement suggestions."
    )
    parser.add_argument(
        "--input",
        help="Input file to analyze (default: reads sample text)",
    )
    parser.add_argument(
        "--target-grade",
        type=int,
        default=8,
        help="Target grade level for readability (default: 8)",
    )
    parser.add_argument(
        "--output",
        help="Output file path (default: stdout)",
    )

    args = parser.parse_args()

    if args.input:
        try:
            with open(args.input) as f:
                text = f.read()
        except FileNotFoundError:
            print(f"Error: File not found: {args.input}", file=sys.stderr)
            sys.exit(1)
    else:
        text = """
        We may process your personal data pursuant to applicable legislation and
        notwithstanding the foregoing provisions herein. The data subject shall have
        the right to lodge a complaint with the supervisory authority. Our sub-processors
        may engage in further processing activities as deemed necessary by the controller.
        Your continued utilization of our services constitutes acceptance of the
        modifications to this privacy policy. We reserve the right to amend these terms
        at our sole discretion without prior notification to the affected parties.
        """

    analysis = analyze_readability(text)
    if "error" in analysis:
        print(json.dumps(analysis, indent=2))
        sys.exit(1)

    suggestions = generate_suggestions(analysis, args.target_grade)

    report = {
        "target_grade_level": args.target_grade,
        "analysis": analysis,
        "meets_target": analysis["scores"]["flesch_kincaid_grade"] <= args.target_grade,
        "suggestions": suggestions,
    }

    output = json.dumps(report, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Readability report written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
