#!/usr/bin/env python3
"""
Analyze and classify keywords by search intent.

Usage:
    python analyze_intent.py keywords.json
    python analyze_intent.py --keywords "keyword1" "keyword2" "keyword3"

Output: Keywords with intent classification and content recommendations
"""

import argparse
import json
import re
import sys


# Intent classification patterns
INTENT_PATTERNS = {
    "informational": {
        "strong_signals": [
            r"^what is",
            r"^what are",
            r"^how to",
            r"^how do",
            r"^why",
            r"^when",
            r"^where",
            r"^who is",
            r"guide$",
            r"tutorial$",
            r"^learn",
            r"explained$",
            r"definition$",
            r"meaning$",
            r"^understanding",
            r"basics$",
            r"introduction$",
            r"^tips for",
        ],
        "weak_signals": [
            r"tips$",
            r"ideas$",
            r"examples$",
            r"types of",
            r"benefits of",
            r"advantages",
            r"disadvantages",
            r"pros and cons",
            r"history of",
        ],
        "content_types": ["blog post", "guide", "tutorial", "FAQ", "explainer"],
        "description": "User wants to learn or understand something"
    },
    "navigational": {
        "strong_signals": [
            r"login$",
            r"sign in$",
            r"log in$",
            r"website$",
            r"official",
            r"portal$",
            r"app$",
            r"download$",
            r"customer service",
            r"support$",
            r"contact$",
        ],
        "weak_signals": [
            r"\.com",
            r"\.org",
            r"\.net",
        ],
        "content_types": ["homepage", "landing page", "product page", "contact page"],
        "description": "User wants to find a specific website or page"
    },
    "commercial": {
        "strong_signals": [
            r"^best",
            r"^top \d+",
            r"^top$",
            r"vs\.?$",
            r"versus",
            r"comparison$",
            r"compare$",
            r"review$",
            r"reviews$",
            r"alternative",
            r"alternatives$",
            r"which is better",
            r"difference between",
        ],
        "weak_signals": [
            r"for \w+$",  # "for beginners", "for business"
            r"cheap",
            r"affordable",
            r"professional",
            r"enterprise",
        ],
        "content_types": ["comparison post", "review", "listicle", "buyer's guide"],
        "description": "User is researching before making a purchase decision"
    },
    "transactional": {
        "strong_signals": [
            r"^buy",
            r"purchase$",
            r"^order",
            r"price$",
            r"pricing$",
            r"cost$",
            r"coupon$",
            r"discount$",
            r"deal$",
            r"deals$",
            r"sale$",
            r"free trial$",
            r"subscribe$",
            r"subscription$",
            r"hire$",
            r"book$",
            r"quote$",
            r"near me$",
        ],
        "weak_signals": [
            r"cheap$",
            r"free$",
            r"online$",
            r"delivery$",
            r"shipping$",
        ],
        "content_types": ["product page", "pricing page", "checkout", "landing page"],
        "description": "User wants to complete a specific action or purchase"
    }
}


def classify_intent(keyword):
    """Classify a single keyword by intent."""
    keyword_lower = keyword.lower().strip()

    scores = {
        "informational": 0,
        "navigational": 0,
        "commercial": 0,
        "transactional": 0
    }

    matched_patterns = []

    for intent, patterns in INTENT_PATTERNS.items():
        # Check strong signals (worth 3 points)
        for pattern in patterns["strong_signals"]:
            if re.search(pattern, keyword_lower):
                scores[intent] += 3
                matched_patterns.append({"intent": intent, "pattern": pattern, "strength": "strong"})

        # Check weak signals (worth 1 point)
        for pattern in patterns["weak_signals"]:
            if re.search(pattern, keyword_lower):
                scores[intent] += 1
                matched_patterns.append({"intent": intent, "pattern": pattern, "strength": "weak"})

    # Determine primary intent
    max_score = max(scores.values())
    if max_score == 0:
        primary_intent = "informational"  # Default
        confidence = "low"
    else:
        primary_intent = max(scores, key=scores.get)
        # Calculate confidence based on score differential
        sorted_scores = sorted(scores.values(), reverse=True)
        if sorted_scores[0] > sorted_scores[1] + 2:
            confidence = "high"
        elif sorted_scores[0] > sorted_scores[1]:
            confidence = "medium"
        else:
            confidence = "low"

    # Get secondary intent if applicable
    sorted_intents = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    secondary_intent = None
    if len(sorted_intents) > 1 and sorted_intents[1][1] > 0:
        secondary_intent = sorted_intents[1][0]

    return {
        "keyword": keyword,
        "primary_intent": primary_intent,
        "secondary_intent": secondary_intent,
        "confidence": confidence,
        "scores": scores,
        "matched_patterns": matched_patterns[:3],  # Top 3 matched
        "recommended_content": INTENT_PATTERNS[primary_intent]["content_types"],
        "intent_description": INTENT_PATTERNS[primary_intent]["description"]
    }


def analyze_keyword_list(keywords):
    """Analyze a list of keywords."""
    results = []
    intent_counts = {
        "informational": 0,
        "navigational": 0,
        "commercial": 0,
        "transactional": 0
    }

    for keyword in keywords:
        if isinstance(keyword, dict):
            keyword = keyword.get("keyword", keyword.get("term", str(keyword)))
        result = classify_intent(keyword)
        results.append(result)
        intent_counts[result["primary_intent"]] += 1

    # Group by intent
    grouped = {
        "informational": [],
        "navigational": [],
        "commercial": [],
        "transactional": []
    }

    for result in results:
        grouped[result["primary_intent"]].append(result)

    return {
        "total_keywords": len(keywords),
        "intent_distribution": intent_counts,
        "intent_percentage": {
            k: round(v / len(keywords) * 100, 1) if keywords else 0
            for k, v in intent_counts.items()
        },
        "keywords_by_intent": grouped,
        "all_results": results
    }


def main():
    parser = argparse.ArgumentParser(description="Analyze keyword search intent")
    parser.add_argument("input_file", nargs="?", help="JSON file with keywords")
    parser.add_argument("--keywords", "-k", nargs="+", help="Keywords to analyze directly")
    parser.add_argument("--format", "-f", choices=["json", "summary"], default="json",
                        help="Output format")

    args = parser.parse_args()

    keywords = []

    if args.keywords:
        keywords = args.keywords
    elif args.input_file:
        try:
            with open(args.input_file, 'r') as f:
                data = json.load(f)
                if isinstance(data, list):
                    keywords = data
                elif isinstance(data, dict):
                    # Try to find keywords in common structures
                    keywords = (data.get("keywords") or
                               data.get("terms") or
                               data.get("data") or
                               list(data.values())[0] if data else [])
        except FileNotFoundError:
            print(json.dumps({"error": f"File not found: {args.input_file}"}))
            sys.exit(1)
        except json.JSONDecodeError:
            print(json.dumps({"error": "Invalid JSON file"}))
            sys.exit(1)
    else:
        print("Error: Provide either a file or --keywords")
        sys.exit(1)

    result = analyze_keyword_list(keywords)

    if args.format == "summary":
        print("\n=== Intent Analysis Summary ===\n")
        print(f"Total keywords: {result['total_keywords']}\n")

        print("Intent Distribution:")
        for intent, count in result['intent_distribution'].items():
            pct = result['intent_percentage'][intent]
            bar = "█" * int(pct / 5) + "░" * (20 - int(pct / 5))
            print(f"  {intent.capitalize():15} {bar} {count:3} ({pct}%)")

        print("\n=== Keywords by Intent ===")
        for intent, keywords in result['keywords_by_intent'].items():
            if keywords:
                print(f"\n{intent.upper()}:")
                for kw in keywords[:5]:
                    conf = f"[{kw['confidence']}]"
                    print(f"  • {kw['keyword']} {conf}")
                if len(keywords) > 5:
                    print(f"  ... and {len(keywords) - 5} more")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
