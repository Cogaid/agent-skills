#!/usr/bin/env python3
"""
Expand seed keywords with modifiers and variations.

Usage:
    python expand_keywords.py --seed "email marketing"
    python expand_keywords.py --seed "email marketing" --modifiers howto,best,question

Output: JSON with expanded keyword list
"""

import argparse
import json
import sys


MODIFIER_TEMPLATES = {
    "howto": [
        "how to {seed}",
        "how to {seed} for beginners",
        "how to {seed} step by step",
        "how to {seed} without {seed}",
        "how to improve {seed}",
        "how to start {seed}",
        "how to learn {seed}",
    ],
    "best": [
        "best {seed}",
        "best {seed} tools",
        "best {seed} software",
        "best {seed} for small business",
        "best {seed} for beginners",
        "best free {seed}",
        "best {seed} practices",
    ],
    "question": [
        "what is {seed}",
        "why {seed}",
        "why is {seed} important",
        "when to use {seed}",
        "who needs {seed}",
        "is {seed} worth it",
        "does {seed} work",
    ],
    "comparison": [
        "{seed} vs",
        "{seed} alternative",
        "{seed} alternatives",
        "{seed} comparison",
        "{seed} or",
    ],
    "modifier": [
        "{seed} tips",
        "{seed} strategy",
        "{seed} examples",
        "{seed} templates",
        "{seed} guide",
        "{seed} tutorial",
        "{seed} course",
        "{seed} certification",
    ],
    "intent": [
        "{seed} services",
        "{seed} agency",
        "{seed} consultant",
        "{seed} pricing",
        "{seed} cost",
        "hire {seed}",
        "outsource {seed}",
    ],
    "audience": [
        "{seed} for startups",
        "{seed} for ecommerce",
        "{seed} for b2b",
        "{seed} for saas",
        "{seed} for small business",
        "{seed} for enterprise",
        "{seed} for beginners",
    ],
    "time": [
        "{seed} 2025",
        "{seed} trends",
        "{seed} statistics",
        "future of {seed}",
        "{seed} in 2025",
    ]
}


def expand_keyword(seed, modifier_types=None):
    """Expand a seed keyword with modifiers."""

    if modifier_types is None or modifier_types == ["all"]:
        modifier_types = list(MODIFIER_TEMPLATES.keys())

    expanded = {
        "seed": seed,
        "variations": {}
    }

    for mod_type in modifier_types:
        if mod_type in MODIFIER_TEMPLATES:
            keywords = [
                template.format(seed=seed)
                for template in MODIFIER_TEMPLATES[mod_type]
            ]
            expanded["variations"][mod_type] = keywords

    # Calculate total count
    total = sum(len(v) for v in expanded["variations"].values())
    expanded["total_keywords"] = total

    return expanded


def main():
    parser = argparse.ArgumentParser(description="Expand seed keywords")
    parser.add_argument("--seed", "-s", required=True, help="Seed keyword to expand")
    parser.add_argument("--modifiers", "-m", default="all",
                        help="Modifier types (comma-separated or 'all')")

    args = parser.parse_args()

    # Parse modifier types
    if args.modifiers == "all":
        modifier_types = None
    else:
        modifier_types = [m.strip() for m in args.modifiers.split(",")]

    result = expand_keyword(args.seed, modifier_types)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
