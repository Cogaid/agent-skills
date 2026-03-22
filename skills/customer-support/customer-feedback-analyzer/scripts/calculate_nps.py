#!/usr/bin/env python3
"""
Calculate Net Promoter Score from survey data.

Usage:
    python calculate_nps.py survey.csv --score-column rating
    python calculate_nps.py survey.csv --score-column nps_score --comment-column feedback

Output: JSON with NPS score and breakdown
"""

import argparse
import csv
import json
import sys
from collections import Counter


def categorize_score(score: int) -> str:
    """Categorize NPS score into promoter/passive/detractor."""
    if score >= 9:
        return "promoter"
    elif score >= 7:
        return "passive"
    else:
        return "detractor"


def calculate_nps(scores: list) -> dict:
    """Calculate NPS from list of scores (0-10)."""
    if not scores:
        return {"error": "No scores provided"}

    categories = Counter(categorize_score(s) for s in scores)
    total = len(scores)

    promoters = categories.get("promoter", 0)
    passives = categories.get("passive", 0)
    detractors = categories.get("detractor", 0)

    promoter_pct = promoters / total * 100
    detractor_pct = detractors / total * 100
    nps = promoter_pct - detractor_pct

    # Interpret NPS
    if nps >= 50:
        interpretation = "Excellent - World-class customer loyalty"
    elif nps >= 30:
        interpretation = "Good - Strong customer satisfaction"
    elif nps >= 0:
        interpretation = "Needs improvement - Opportunity to increase loyalty"
    else:
        interpretation = "Critical - Significant customer experience issues"

    return {
        "nps_score": round(nps, 1),
        "interpretation": interpretation,
        "responses": {
            "total": total,
            "promoters": promoters,
            "passives": passives,
            "detractors": detractors
        },
        "percentages": {
            "promoters": round(promoter_pct, 1),
            "passives": round(passives / total * 100, 1),
            "detractors": round(detractor_pct, 1)
        },
        "score_distribution": dict(Counter(scores))
    }


def analyze_csv(filepath: str, score_column: str, comment_column: str = None) -> dict:
    """Analyze NPS from CSV file."""
    scores = []
    comments = {"promoter": [], "passive": [], "detractor": []}

    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                score = int(row.get(score_column, "").strip())
                if 0 <= score <= 10:
                    scores.append(score)

                    # Capture comments if available
                    if comment_column and row.get(comment_column):
                        category = categorize_score(score)
                        comments[category].append({
                            "score": score,
                            "comment": row[comment_column][:200]
                        })
            except (ValueError, TypeError):
                continue

    result = calculate_nps(scores)

    # Add sample comments
    if comment_column:
        result["sample_comments"] = {
            "promoters": comments["promoter"][:3],
            "detractors": comments["detractor"][:3]
        }

    return result


def main():
    parser = argparse.ArgumentParser(description="Calculate NPS score")
    parser.add_argument("input", help="CSV file with survey data")
    parser.add_argument("--score-column", "-s", default="score",
                        help="Column name containing NPS score (0-10)")
    parser.add_argument("--comment-column", "-c",
                        help="Column name containing comments (optional)")
    parser.add_argument("--output", "-o", help="Output file")
    parser.add_argument("--pretty", "-p", action="store_true", help="Pretty print")

    args = parser.parse_args()

    result = analyze_csv(args.input, args.score_column, args.comment_column)

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
