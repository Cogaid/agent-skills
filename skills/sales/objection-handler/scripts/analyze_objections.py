#!/usr/bin/env python3
"""
Analyze objection patterns from logged data.

Usage:
    python analyze_objections.py objections.json
    python analyze_objections.py objections.json --by-type
    python analyze_objections.py objections.json --by-outcome

Output: JSON analysis of objection patterns
"""

import argparse
import json
import sys
from collections import Counter


def analyze_by_type(data):
    """Analyze objections by type."""
    types = Counter()
    type_outcomes = {}

    for record in data:
        obj_type = record.get("objection", {}).get("type", "unknown")
        outcome = record.get("outcome", "unknown")

        types[obj_type] += 1

        if obj_type not in type_outcomes:
            type_outcomes[obj_type] = Counter()
        type_outcomes[obj_type][outcome] += 1

    # Calculate success rates
    success_rates = {}
    for obj_type, outcomes in type_outcomes.items():
        total = sum(outcomes.values())
        resolved = outcomes.get("resolved", 0)
        success_rates[obj_type] = {
            "total": total,
            "resolved": resolved,
            "success_rate": round(resolved / total * 100, 1) if total > 0 else 0
        }

    return {
        "by_type": dict(types.most_common()),
        "success_rates": success_rates
    }


def analyze_by_outcome(data):
    """Analyze objections by outcome."""
    outcomes = Counter()
    outcome_types = {}

    for record in data:
        obj_type = record.get("objection", {}).get("type", "unknown")
        outcome = record.get("outcome", "unknown")

        outcomes[outcome] += 1

        if outcome not in outcome_types:
            outcome_types[outcome] = Counter()
        outcome_types[outcome][obj_type] += 1

    return {
        "by_outcome": dict(outcomes.most_common()),
        "types_by_outcome": {k: dict(v.most_common()) for k, v in outcome_types.items()}
    }


def analyze_by_deal(data):
    """Analyze objections by deal."""
    deals = {}

    for record in data:
        deal = record.get("deal", "unknown")
        obj_type = record.get("objection", {}).get("type", "unknown")
        outcome = record.get("outcome", "unknown")

        if deal not in deals:
            deals[deal] = {"objections": [], "outcomes": Counter()}

        deals[deal]["objections"].append(obj_type)
        deals[deal]["outcomes"][outcome] += 1

    return {
        "by_deal": {
            deal: {
                "total_objections": len(info["objections"]),
                "types": dict(Counter(info["objections"])),
                "outcomes": dict(info["outcomes"])
            }
            for deal, info in deals.items()
        }
    }


def extract_learnings(data):
    """Extract learnings from records that have them."""
    learnings = {
        "what_worked": [],
        "what_to_improve": []
    }

    for record in data:
        if "learnings" in record:
            worked = record["learnings"].get("worked", "").strip()
            improve = record["learnings"].get("improve", "").strip()

            if worked:
                learnings["what_worked"].append({
                    "type": record.get("objection", {}).get("type"),
                    "learning": worked
                })
            if improve:
                learnings["what_to_improve"].append({
                    "type": record.get("objection", {}).get("type"),
                    "learning": improve
                })

    return learnings


def full_analysis(data):
    """Complete analysis of all objection data."""
    total = len(data)

    if total == 0:
        return {"error": "No data to analyze"}

    type_analysis = analyze_by_type(data)
    outcome_analysis = analyze_by_outcome(data)

    # Overall success rate
    resolved = sum(1 for r in data if r.get("outcome") == "resolved")
    overall_success_rate = round(resolved / total * 100, 1)

    # Most problematic objection type
    success_rates = type_analysis["success_rates"]
    worst_type = min(
        success_rates.items(),
        key=lambda x: x[1]["success_rate"] if x[1]["total"] >= 3 else 100
    ) if success_rates else None

    return {
        "summary": {
            "total_objections": total,
            "overall_success_rate": overall_success_rate,
            "most_common_type": list(type_analysis["by_type"].keys())[0] if type_analysis["by_type"] else None,
            "needs_improvement": worst_type[0] if worst_type else None
        },
        "by_type": type_analysis,
        "by_outcome": outcome_analysis,
        "learnings": extract_learnings(data)
    }


def main():
    parser = argparse.ArgumentParser(description="Analyze objection patterns")
    parser.add_argument("file", help="JSON file with objection logs")
    parser.add_argument("--by-type", action="store_true",
                        help="Analyze by objection type")
    parser.add_argument("--by-outcome", action="store_true",
                        help="Analyze by outcome")
    parser.add_argument("--by-deal", action="store_true",
                        help="Analyze by deal")
    parser.add_argument("--learnings", action="store_true",
                        help="Extract learnings")

    args = parser.parse_args()

    try:
        with open(args.file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(json.dumps({"error": f"File not found: {args.file}"}))
        sys.exit(1)
    except json.JSONDecodeError:
        print(json.dumps({"error": "Invalid JSON file"}))
        sys.exit(1)

    if args.by_type:
        result = analyze_by_type(data)
    elif args.by_outcome:
        result = analyze_by_outcome(data)
    elif args.by_deal:
        result = analyze_by_deal(data)
    elif args.learnings:
        result = extract_learnings(data)
    else:
        result = full_analysis(data)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
