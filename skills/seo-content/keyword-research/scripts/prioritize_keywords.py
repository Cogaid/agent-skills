#!/usr/bin/env python3
"""
Prioritize keywords based on multiple factors.

Usage:
    python prioritize_keywords.py keywords.json
    python prioritize_keywords.py keywords.json --weights business:2,volume:1,difficulty:1

Output: Prioritized keyword list with scores and recommendations
"""

import argparse
import json
import sys


# Default weights for scoring
DEFAULT_WEIGHTS = {
    "volume": 1.0,
    "difficulty": 1.0,
    "business_value": 1.5,
    "intent_match": 1.2,
    "competition": 0.8
}


def normalize_score(value, min_val, max_val, invert=False):
    """Normalize a value to 0-100 scale."""
    if max_val == min_val:
        return 50
    normalized = (value - min_val) / (max_val - min_val) * 100
    if invert:
        normalized = 100 - normalized
    return max(0, min(100, normalized))


def calculate_opportunity_score(keyword_data, weights):
    """Calculate opportunity score for a keyword."""
    scores = {}

    # Volume score (higher is better)
    volume = keyword_data.get("volume", keyword_data.get("search_volume", 0))
    if volume:
        if volume >= 10000:
            scores["volume"] = 100
        elif volume >= 1000:
            scores["volume"] = 80
        elif volume >= 100:
            scores["volume"] = 60
        elif volume >= 10:
            scores["volume"] = 40
        else:
            scores["volume"] = 20
    else:
        scores["volume"] = 50  # Unknown

    # Difficulty score (lower difficulty is better)
    difficulty = keyword_data.get("difficulty", keyword_data.get("kd", None))
    if difficulty is not None:
        scores["difficulty"] = 100 - min(100, max(0, difficulty))
    else:
        scores["difficulty"] = 50  # Unknown

    # Business value (if provided)
    business = keyword_data.get("business_value", keyword_data.get("value", None))
    if business is not None:
        scores["business_value"] = min(100, max(0, business * 20))  # Assuming 1-5 scale
    else:
        scores["business_value"] = 50  # Default

    # Intent match (if intent provided)
    intent = keyword_data.get("intent", "").lower()
    intent_scores = {
        "transactional": 100,
        "commercial": 80,
        "informational": 50,
        "navigational": 30
    }
    scores["intent_match"] = intent_scores.get(intent, 50)

    # Competition score (if CPC provided, higher CPC = higher competition value)
    cpc = keyword_data.get("cpc", None)
    if cpc is not None:
        if cpc >= 5:
            scores["competition"] = 100  # High value keywords
        elif cpc >= 2:
            scores["competition"] = 75
        elif cpc >= 1:
            scores["competition"] = 50
        else:
            scores["competition"] = 25
    else:
        scores["competition"] = 50

    # Calculate weighted average
    total_weight = 0
    weighted_sum = 0

    for factor, score in scores.items():
        weight = weights.get(factor, 1.0)
        weighted_sum += score * weight
        total_weight += weight

    final_score = weighted_sum / total_weight if total_weight > 0 else 0

    return {
        "opportunity_score": round(final_score, 1),
        "factor_scores": {k: round(v, 1) for k, v in scores.items()},
        "weights_used": weights
    }


def classify_priority(score):
    """Classify priority based on score."""
    if score >= 75:
        return "high"
    elif score >= 50:
        return "medium"
    else:
        return "low"


def prioritize_keywords(keywords, weights):
    """Prioritize a list of keywords."""
    results = []

    for kw in keywords:
        if isinstance(kw, str):
            kw = {"keyword": kw}

        keyword_text = kw.get("keyword", kw.get("term", str(kw)))
        score_data = calculate_opportunity_score(kw, weights)

        result = {
            "keyword": keyword_text,
            "opportunity_score": score_data["opportunity_score"],
            "priority": classify_priority(score_data["opportunity_score"]),
            "factor_scores": score_data["factor_scores"],
            "original_data": {
                "volume": kw.get("volume", kw.get("search_volume")),
                "difficulty": kw.get("difficulty", kw.get("kd")),
                "cpc": kw.get("cpc"),
                "intent": kw.get("intent")
            }
        }
        results.append(result)

    # Sort by score descending
    results.sort(key=lambda x: x["opportunity_score"], reverse=True)

    # Add rank
    for i, result in enumerate(results):
        result["rank"] = i + 1

    return results


def generate_recommendations(prioritized):
    """Generate action recommendations based on prioritization."""
    recommendations = {
        "quick_wins": [],
        "strategic_targets": [],
        "long_term": [],
        "consider_skipping": []
    }

    for kw in prioritized:
        score = kw["opportunity_score"]
        factors = kw["factor_scores"]

        # Quick wins: high score, low difficulty
        if score >= 70 and factors.get("difficulty", 0) >= 70:
            recommendations["quick_wins"].append(kw["keyword"])

        # Strategic targets: high value, medium difficulty
        elif factors.get("business_value", 0) >= 70 or factors.get("competition", 0) >= 70:
            recommendations["strategic_targets"].append(kw["keyword"])

        # Long term: high difficulty but worth pursuing
        elif score >= 50 and factors.get("difficulty", 0) < 50:
            recommendations["long_term"].append(kw["keyword"])

        # Consider skipping: low score all around
        elif score < 30:
            recommendations["consider_skipping"].append(kw["keyword"])

    return recommendations


def parse_weights(weights_str):
    """Parse weights string into dictionary."""
    weights = DEFAULT_WEIGHTS.copy()

    if weights_str:
        pairs = weights_str.split(",")
        for pair in pairs:
            if ":" in pair:
                key, value = pair.split(":")
                key = key.strip().lower()
                if key in weights:
                    try:
                        weights[key] = float(value)
                    except ValueError:
                        pass

    return weights


def main():
    parser = argparse.ArgumentParser(description="Prioritize keywords")
    parser.add_argument("input_file", nargs="?", help="JSON file with keyword data")
    parser.add_argument("--weights", "-w",
                        help="Custom weights (e.g., 'business:2,volume:1')")
    parser.add_argument("--format", "-f", choices=["json", "summary", "table"],
                        default="json", help="Output format")
    parser.add_argument("--top", "-t", type=int, default=None,
                        help="Show only top N results")

    args = parser.parse_args()

    if not args.input_file:
        print("Error: Input file required")
        sys.exit(1)

    try:
        with open(args.input_file, 'r') as f:
            data = json.load(f)
            if isinstance(data, list):
                keywords = data
            elif isinstance(data, dict):
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

    weights = parse_weights(args.weights)
    prioritized = prioritize_keywords(keywords, weights)
    recommendations = generate_recommendations(prioritized)

    if args.top:
        prioritized = prioritized[:args.top]

    result = {
        "total_keywords": len(keywords),
        "weights_used": weights,
        "prioritized_keywords": prioritized,
        "recommendations": recommendations,
        "summary": {
            "high_priority": len([k for k in prioritized if k["priority"] == "high"]),
            "medium_priority": len([k for k in prioritized if k["priority"] == "medium"]),
            "low_priority": len([k for k in prioritized if k["priority"] == "low"])
        }
    }

    if args.format == "summary":
        print("\n=== Keyword Prioritization ===\n")
        print(f"Total keywords: {result['total_keywords']}")
        print(f"High priority: {result['summary']['high_priority']}")
        print(f"Medium priority: {result['summary']['medium_priority']}")
        print(f"Low priority: {result['summary']['low_priority']}\n")

        print("Top 10 Keywords:")
        for kw in prioritized[:10]:
            print(f"  {kw['rank']:2}. {kw['keyword'][:40]:40} Score: {kw['opportunity_score']:5.1f} [{kw['priority'].upper()}]")

        if recommendations["quick_wins"]:
            print(f"\nQuick Wins ({len(recommendations['quick_wins'])}):")
            for kw in recommendations["quick_wins"][:5]:
                print(f"  • {kw}")

    elif args.format == "table":
        print("\n| Rank | Keyword | Score | Priority | Volume | Difficulty |")
        print("|------|---------|-------|----------|--------|------------|")
        for kw in prioritized[:20]:
            print(f"| {kw['rank']:4} | {kw['keyword'][:30]:30} | {kw['opportunity_score']:5.1f} | {kw['priority']:8} | {kw['original_data'].get('volume', 'N/A')} | {kw['original_data'].get('difficulty', 'N/A')} |")

    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
