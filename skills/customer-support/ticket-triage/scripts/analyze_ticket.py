#!/usr/bin/env python3
"""
Analyze support ticket text and extract structured data.

Usage:
    python analyze_ticket.py "ticket text here"
    python analyze_ticket.py --file ticket.txt
    cat ticket.txt | python analyze_ticket.py --stdin

Output: JSON with sentiment, keywords, category suggestion, priority indicators
"""

import argparse
import json
import re
import sys
from collections import Counter

# Category keyword mappings
CATEGORY_KEYWORDS = {
    "bug": [
        "doesn't work", "not working", "broken", "error", "crash", "bug",
        "unexpected", "wrong", "failed", "failing", "issue", "problem"
    ],
    "performance": [
        "slow", "timeout", "lag", "hanging", "loading", "takes forever",
        "performance", "speed", "sluggish", "freezing", "unresponsive"
    ],
    "billing": [
        "charge", "invoice", "payment", "subscription", "refund", "billing",
        "cost", "price", "pricing", "plan", "upgrade", "downgrade"
    ],
    "access": [
        "login", "password", "locked", "access", "permission", "sso",
        "can't get in", "denied", "unauthorized", "authentication"
    ],
    "howto": [
        "how do i", "how to", "where is", "can i", "help with", "setup",
        "configure", "tutorial", "guide", "instructions"
    ],
    "feature_request": [
        "would be nice", "suggestion", "wish", "please add", "feature",
        "could you add", "it would help", "requesting"
    ],
    "integration": [
        "api", "webhook", "sync", "integration", "connect", "third-party",
        "salesforce", "slack", "zapier", "oauth"
    ]
}

# Priority indicators
PRIORITY_INDICATORS = {
    "p1_critical": [
        "outage", "down", "all users", "entire company", "breach", "exposed",
        "data loss", "security", "urgent", "emergency", "asap", "critical"
    ],
    "p2_high": [
        "broken", "can't complete", "blocking", "enterprise", "vip",
        "affecting multiple", "deadline", "important"
    ],
    "p3_normal": [
        "sometimes", "occasionally", "when i", "would like", "question"
    ],
    "p4_low": [
        "minor", "cosmetic", "suggestion", "just wondering", "feedback",
        "not urgent", "when you have time"
    ]
}

# Sentiment indicators
NEGATIVE_WORDS = [
    "frustrated", "angry", "disappointed", "terrible", "worst", "hate",
    "unacceptable", "ridiculous", "awful", "useless", "pathetic"
]

POSITIVE_WORDS = [
    "thanks", "appreciate", "great", "love", "excellent", "amazing",
    "helpful", "wonderful", "fantastic"
]

URGENCY_INDICATORS = [
    "urgent", "asap", "immediately", "critical", "emergency", "now",
    "deadline", "today", "!!!",  "URGENT", "ASAP"
]


def extract_keywords(text: str) -> list:
    """Extract significant keywords from text."""
    # Normalize
    text_lower = text.lower()

    # Remove common words
    stopwords = {
        "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
        "have", "has", "had", "do", "does", "did", "will", "would", "could",
        "should", "may", "might", "must", "shall", "can", "need", "dare",
        "to", "of", "in", "for", "on", "with", "at", "by", "from", "as",
        "i", "me", "my", "we", "our", "you", "your", "it", "its", "this",
        "that", "these", "those", "and", "or", "but", "if", "then", "so",
        "because", "when", "where", "which", "what", "who", "how", "why"
    }

    # Extract words
    words = re.findall(r'\b[a-z]+\b', text_lower)

    # Filter and count
    filtered = [w for w in words if w not in stopwords and len(w) > 2]
    word_counts = Counter(filtered)

    # Return top keywords
    return [word for word, count in word_counts.most_common(10)]


def detect_category(text: str) -> dict:
    """Detect most likely category based on keywords."""
    text_lower = text.lower()
    scores = {}

    for category, keywords in CATEGORY_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in text_lower)
        if score > 0:
            scores[category] = score

    if not scores:
        return {"primary": "unknown", "confidence": 0}

    # Sort by score
    sorted_categories = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    result = {
        "primary": sorted_categories[0][0],
        "confidence": min(sorted_categories[0][1] / 3, 1.0)  # Normalize
    }

    if len(sorted_categories) > 1:
        result["secondary"] = sorted_categories[1][0]

    return result


def detect_priority(text: str) -> dict:
    """Detect priority indicators."""
    text_lower = text.lower()

    for priority, indicators in PRIORITY_INDICATORS.items():
        matches = [ind for ind in indicators if ind in text_lower]
        if matches:
            return {
                "suggested": priority,
                "indicators": matches
            }

    return {"suggested": "p3_normal", "indicators": []}


def analyze_sentiment(text: str) -> dict:
    """Analyze sentiment of ticket text."""
    text_lower = text.lower()

    negative_count = sum(1 for word in NEGATIVE_WORDS if word in text_lower)
    positive_count = sum(1 for word in POSITIVE_WORDS if word in text_lower)
    urgency_count = sum(1 for word in URGENCY_INDICATORS if word in text_lower)

    # Check for ALL CAPS (anger indicator)
    caps_ratio = sum(1 for c in text if c.isupper()) / max(len(text), 1)

    # Check for multiple exclamation marks
    exclamation_count = text.count('!')

    # Determine overall sentiment
    if negative_count > positive_count or caps_ratio > 0.3 or exclamation_count > 3:
        sentiment = "negative"
    elif positive_count > negative_count:
        sentiment = "positive"
    else:
        sentiment = "neutral"

    return {
        "overall": sentiment,
        "negative_indicators": negative_count,
        "positive_indicators": positive_count,
        "urgency_level": min(urgency_count, 3),  # 0-3 scale
        "frustration_signals": {
            "caps_ratio": round(caps_ratio, 2),
            "exclamation_marks": exclamation_count
        }
    }


def analyze_ticket(text: str) -> dict:
    """Main analysis function."""
    return {
        "keywords": extract_keywords(text),
        "category": detect_category(text),
        "priority": detect_priority(text),
        "sentiment": analyze_sentiment(text),
        "metadata": {
            "char_count": len(text),
            "word_count": len(text.split())
        }
    }


def main():
    parser = argparse.ArgumentParser(description="Analyze support ticket text")
    parser.add_argument("text", nargs="?", help="Ticket text to analyze")
    parser.add_argument("--file", "-f", help="Read text from file")
    parser.add_argument("--stdin", action="store_true", help="Read from stdin")
    parser.add_argument("--pretty", "-p", action="store_true", help="Pretty print output")

    args = parser.parse_args()

    # Get input text
    if args.stdin:
        text = sys.stdin.read()
    elif args.file:
        with open(args.file, 'r') as f:
            text = f.read()
    elif args.text:
        text = args.text
    else:
        parser.print_help()
        sys.exit(1)

    # Analyze
    result = analyze_ticket(text)

    # Output
    if args.pretty:
        print(json.dumps(result, indent=2))
    else:
        print(json.dumps(result))


if __name__ == "__main__":
    main()
