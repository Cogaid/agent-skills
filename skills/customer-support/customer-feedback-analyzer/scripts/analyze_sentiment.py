#!/usr/bin/env python3
"""
Analyze sentiment of customer feedback.

Usage:
    python analyze_sentiment.py feedback.csv --text-column content
    python analyze_sentiment.py "feedback text here"

Output: JSON with sentiment scores and summary
"""

import argparse
import csv
import json
import re
import sys
from collections import Counter

# Sentiment word lists
SENTIMENT_WORDS = {
    "very_positive": [
        "love", "amazing", "excellent", "fantastic", "outstanding",
        "incredible", "brilliant", "perfect", "awesome", "wonderful",
        "best", "exceptional", "superb"
    ],
    "positive": [
        "good", "great", "nice", "helpful", "works", "easy", "simple",
        "fast", "quick", "reliable", "useful", "happy", "pleased",
        "satisfied", "recommend", "thank"
    ],
    "negative": [
        "bad", "poor", "slow", "difficult", "hard", "confusing",
        "frustrating", "annoying", "disappointed", "unhappy", "problem",
        "issue", "broken", "doesn't work", "fail", "error"
    ],
    "very_negative": [
        "terrible", "awful", "horrible", "worst", "hate", "useless",
        "pathetic", "disaster", "unacceptable", "ridiculous", "disgusting",
        "furious", "outraged", "scam"
    ]
}


def score_text(text: str) -> dict:
    """Score sentiment of a single text."""
    text_lower = text.lower()

    scores = {
        "very_positive": 0,
        "positive": 0,
        "negative": 0,
        "very_negative": 0
    }

    matched_words = []

    for category, words in SENTIMENT_WORDS.items():
        for word in words:
            count = text_lower.count(word)
            if count > 0:
                scores[category] += count
                matched_words.append(word)

    # Calculate overall score (-2 to +2)
    overall = (
        scores["very_positive"] * 2 +
        scores["positive"] * 1 +
        scores["negative"] * -1 +
        scores["very_negative"] * -2
    )

    # Normalize by text length
    word_count = len(text.split())
    normalized_score = overall / max(word_count / 10, 1)

    # Determine sentiment label
    if normalized_score >= 1.5:
        label = "very_positive"
    elif normalized_score >= 0.5:
        label = "positive"
    elif normalized_score <= -1.5:
        label = "very_negative"
    elif normalized_score <= -0.5:
        label = "negative"
    else:
        label = "neutral"

    return {
        "raw_score": overall,
        "normalized_score": round(normalized_score, 2),
        "label": label,
        "word_counts": scores,
        "matched_words": matched_words[:10]
    }


def analyze_csv(filepath: str, text_column: str = "content") -> dict:
    """Analyze sentiment of CSV feedback file."""
    results = []
    labels = Counter()

    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            text = row.get(text_column, "")
            if text:
                sentiment = score_text(text)
                sentiment["text_preview"] = text[:100]
                results.append(sentiment)
                labels[sentiment["label"]] += 1

    # Calculate summary statistics
    total = len(results)
    if total == 0:
        return {"error": "No feedback found"}

    avg_score = sum(r["normalized_score"] for r in results) / total

    return {
        "total_entries": total,
        "average_score": round(avg_score, 2),
        "distribution": dict(labels),
        "distribution_percent": {
            k: round(v / total * 100, 1) for k, v in labels.items()
        },
        "overall_sentiment": (
            "positive" if avg_score > 0.3 else
            "negative" if avg_score < -0.3 else
            "neutral"
        ),
        "samples": {
            "most_positive": sorted(results, key=lambda x: x["normalized_score"], reverse=True)[:3],
            "most_negative": sorted(results, key=lambda x: x["normalized_score"])[:3]
        }
    }


def main():
    parser = argparse.ArgumentParser(description="Analyze feedback sentiment")
    parser.add_argument("input", help="CSV file or text to analyze")
    parser.add_argument("--text-column", "-c", default="content",
                        help="Column name containing text (for CSV)")
    parser.add_argument("--output", "-o", help="Output file")
    parser.add_argument("--pretty", "-p", action="store_true", help="Pretty print")

    args = parser.parse_args()

    # Determine input type
    if args.input.endswith('.csv'):
        result = analyze_csv(args.input, args.text_column)
    else:
        result = score_text(args.input)

    # Format output
    if args.pretty:
        output = json.dumps(result, indent=2)
    else:
        output = json.dumps(result)

    # Write output
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
    else:
        print(output)


if __name__ == "__main__":
    main()
