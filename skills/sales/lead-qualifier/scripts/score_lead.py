#!/usr/bin/env python3
"""
Score leads based on ICP fit and qualification criteria.

Usage:
    python score_lead.py --company "Acme" --size 150 --industry tech
    python score_lead.py --interactive
    python score_lead.py --json lead_data.json

Output: JSON with lead score and classification
"""

import argparse
import json
import sys


# Default scoring criteria (customize for your ICP)
DEFAULT_CRITERIA = {
    "size": {
        "ideal": {"min": 50, "max": 500, "score": 10},
        "good": {"min": 20, "max": 1000, "score": 7},
        "okay": {"min": 10, "max": 2000, "score": 4},
        "poor": {"score": 0}
    },
    "industry": {
        "ideal": ["technology", "tech", "software", "saas", "fintech"],
        "good": ["healthcare", "finance", "professional services"],
        "okay": ["retail", "manufacturing", "education"],
        "poor": ["government", "non-profit"]
    },
    "title": {
        "ideal": ["ceo", "cto", "vp", "director", "head of"],
        "good": ["manager", "senior"],
        "okay": ["lead", "specialist"],
        "poor": ["intern", "assistant", "coordinator"]
    }
}


def score_size(size, criteria=None):
    """Score based on company size."""
    criteria = criteria or DEFAULT_CRITERIA["size"]

    if criteria["ideal"]["min"] <= size <= criteria["ideal"]["max"]:
        return criteria["ideal"]["score"], "ideal"
    elif criteria["good"]["min"] <= size <= criteria["good"]["max"]:
        return criteria["good"]["score"], "good"
    elif criteria["okay"]["min"] <= size <= criteria["okay"]["max"]:
        return criteria["okay"]["score"], "okay"
    return criteria["poor"]["score"], "poor"


def score_industry(industry, criteria=None):
    """Score based on industry."""
    criteria = criteria or DEFAULT_CRITERIA["industry"]
    industry_lower = industry.lower().strip()

    for category in ["ideal", "good", "okay"]:
        if any(ind in industry_lower for ind in criteria[category]):
            scores = {"ideal": 10, "good": 7, "okay": 4}
            return scores[category], category

    # Check if it's a known poor fit
    if any(ind in industry_lower for ind in criteria["poor"]):
        return 0, "poor"

    return 4, "unknown"  # Unknown industries get okay score


def score_title(title, criteria=None):
    """Score based on contact title."""
    criteria = criteria or DEFAULT_CRITERIA["title"]
    title_lower = title.lower().strip()

    for category in ["ideal", "good", "okay"]:
        if any(t in title_lower for t in criteria[category]):
            scores = {"ideal": 10, "good": 7, "okay": 4}
            return scores[category], category

    if any(t in title_lower for t in criteria["poor"]):
        return 0, "poor"

    return 4, "unknown"


def score_bant(budget, authority, need, timeline):
    """Score BANT criteria."""
    bant_map = {
        "confirmed": 10,
        "likely": 7,
        "unknown": 4,
        "none": 0
    }

    scores = {
        "budget": bant_map.get(budget.lower(), 4),
        "authority": bant_map.get(authority.lower(), 4),
        "need": bant_map.get(need.lower(), 4),
        "timeline": bant_map.get(timeline.lower(), 4)
    }

    return scores


def calculate_total_score(firmographic_scores, bant_scores=None):
    """Calculate total score and classification."""
    firm_total = sum(s for s, _ in firmographic_scores.values())
    firm_max = len(firmographic_scores) * 10

    if bant_scores:
        bant_total = sum(bant_scores.values())
        bant_max = len(bant_scores) * 10
        total = firm_total + bant_total
        max_score = firm_max + bant_max
    else:
        total = firm_total
        max_score = firm_max

    percentage = (total / max_score) * 100 if max_score > 0 else 0

    # Classification
    if percentage >= 80:
        classification = "hot"
        action = "Pursue immediately"
    elif percentage >= 60:
        classification = "warm"
        action = "Pursue, prioritize"
    elif percentage >= 40:
        classification = "cool"
        action = "Nurture, develop"
    else:
        classification = "cold"
        action = "Disqualify or long-term nurture"

    return {
        "total_score": total,
        "max_score": max_score,
        "percentage": round(percentage, 1),
        "classification": classification,
        "recommended_action": action
    }


def interactive_mode():
    """Interactive scoring mode."""
    print("=== Lead Scorer ===\n")

    # Basic info
    company = input("Company name: ").strip()

    # Firmographic scoring
    print("\n--- FIRMOGRAPHIC SCORING ---")
    size_input = input("Company size (employees): ").strip()
    size = int(size_input) if size_input.isdigit() else 50

    industry = input("Industry: ").strip()
    title = input("Contact title: ").strip()

    # BANT scoring
    print("\n--- BANT SCORING ---")
    print("For each: confirmed/likely/unknown/none")

    budget = input("Budget status: ").strip() or "unknown"
    authority = input("Authority status: ").strip() or "unknown"
    need = input("Need status: ").strip() or "unknown"
    timeline = input("Timeline status: ").strip() or "unknown"

    return {
        "company": company,
        "size": size,
        "industry": industry,
        "title": title,
        "bant": {
            "budget": budget,
            "authority": authority,
            "need": need,
            "timeline": timeline
        }
    }


def score_lead(data):
    """Score a lead based on provided data."""

    firmographic_scores = {}

    if "size" in data:
        firmographic_scores["size"] = score_size(data["size"])

    if "industry" in data:
        firmographic_scores["industry"] = score_industry(data["industry"])

    if "title" in data:
        firmographic_scores["title"] = score_title(data["title"])

    bant_scores = None
    if "bant" in data:
        bant = data["bant"]
        bant_scores = score_bant(
            bant.get("budget", "unknown"),
            bant.get("authority", "unknown"),
            bant.get("need", "unknown"),
            bant.get("timeline", "unknown")
        )

    totals = calculate_total_score(firmographic_scores, bant_scores)

    return {
        "company": data.get("company", "Unknown"),
        "firmographic_scores": {
            k: {"score": v[0], "fit": v[1]}
            for k, v in firmographic_scores.items()
        },
        "bant_scores": bant_scores,
        "totals": totals
    }


def main():
    parser = argparse.ArgumentParser(description="Score a lead")
    parser.add_argument("--company", "-c", help="Company name")
    parser.add_argument("--size", "-s", type=int, help="Company size")
    parser.add_argument("--industry", "-i", help="Industry")
    parser.add_argument("--title", "-t", help="Contact title")
    parser.add_argument("--interactive", action="store_true",
                        help="Interactive mode")
    parser.add_argument("--json", help="Load from JSON file")

    args = parser.parse_args()

    if args.interactive:
        data = interactive_mode()
    elif args.json:
        with open(args.json, 'r') as f:
            data = json.load(f)
    elif args.company:
        data = {
            "company": args.company,
            "size": args.size or 50,
            "industry": args.industry or "unknown",
            "title": args.title or "unknown"
        }
    else:
        parser.print_help()
        sys.exit(1)

    result = score_lead(data)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
