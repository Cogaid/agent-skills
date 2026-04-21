#!/usr/bin/env python3
"""Risk score calculator and priority assessor.

Calculates risk scores from probability and impact ratings, supports
detectability (RPN), generates risk matrices, and provides priority
recommendations.

Usage:
    python risk_calculator.py --demo
    python risk_calculator.py --probability 3 --impact 4
    python risk_calculator.py --probability 3 --impact 4 --detectability 2
    python risk_calculator.py --demo --json
"""

import argparse
import json
import sys


def calculate_risk_score(probability, impact, detectability=1):
    """Calculate risk score and determine priority level."""
    if not (1 <= probability <= 5 and 1 <= impact <= 5):
        raise ValueError("Probability and impact must be between 1 and 5")
    if not (1 <= detectability <= 5):
        raise ValueError("Detectability must be between 1 and 5")

    score = probability * impact * detectability
    use_rpn = detectability > 1

    if use_rpn:
        if score >= 60:
            level = "CRITICAL"
        elif score >= 30:
            level = "HIGH"
        elif score >= 12:
            level = "MEDIUM"
        else:
            level = "LOW"
        max_score = 125
    else:
        if score >= 16:
            level = "CRITICAL"
        elif score >= 10:
            level = "HIGH"
        elif score >= 5:
            level = "MEDIUM"
        else:
            level = "LOW"
        max_score = 25

    escalation = {
        "LOW": {"target": "Team lead", "response_time": "Next review cycle", "action": "Monitor"},
        "MEDIUM": {"target": "Project Manager", "response_time": "Within 1 week", "action": "Mitigation plan required"},
        "HIGH": {"target": "Program Manager / Director", "response_time": "Within 48 hours", "action": "Active mitigation + status report"},
        "CRITICAL": {"target": "Executive Sponsor / VP", "response_time": "Within 4 hours", "action": "Emergency review + recovery plan"},
    }

    return {
        "probability": probability,
        "impact": impact,
        "detectability": detectability,
        "score": score,
        "max_score": max_score,
        "level": level,
        "method": "RPN" if use_rpn else "Simple (P x I)",
        "escalation": escalation[level],
    }


def generate_risk_matrix():
    """Generate a 5x5 probability-impact matrix."""
    matrix = []
    for prob in range(5, 0, -1):
        row = []
        for imp in range(1, 6):
            score = prob * imp
            if score >= 16:
                level = "CRITICAL"
            elif score >= 10:
                level = "HIGH"
            elif score >= 5:
                level = "MEDIUM"
            else:
                level = "LOW"
            row.append({"score": score, "level": level})
        matrix.append({"probability": prob, "cells": row})
    return matrix


def format_matrix_text():
    """Format the risk matrix as text art."""
    lines = []
    lines.append("PROBABILITY-IMPACT RISK MATRIX")
    lines.append("")
    lines.append("              Impact")
    lines.append("         1     2     3     4     5")
    lines.append("       +-----+-----+-----+-----+-----+")

    colors = {"LOW": " ", "MEDIUM": ".", "HIGH": "#", "CRITICAL": "X"}

    for prob in range(5, 0, -1):
        row = f"  P={prob}  |"
        for imp in range(1, 6):
            score = prob * imp
            if score >= 16:
                marker = "X"
            elif score >= 10:
                marker = "#"
            elif score >= 5:
                marker = "."
            else:
                marker = " "
            row += f" {score:>2}{marker} |"
        lines.append(row)
        lines.append("       +-----+-----+-----+-----+-----+")

    lines.append("")
    lines.append("Legend: X=Critical(16-25) #=High(10-15) .=Medium(5-9) =Low(1-4)")
    return "\n".join(lines)


SAMPLE_RISKS = [
    {"name": "Key developer leaves", "probability": 3, "impact": 4, "category": "Resource"},
    {"name": "Payment API incompatibility", "probability": 2, "impact": 5, "category": "Technical"},
    {"name": "Client scope creep", "probability": 4, "impact": 3, "category": "Scope"},
    {"name": "Database performance under load", "probability": 3, "impact": 3, "category": "Technical"},
    {"name": "Regulatory compliance unclear", "probability": 2, "impact": 4, "category": "External"},
    {"name": "Third-party API deprecation", "probability": 3, "impact": 2, "category": "External"},
    {"name": "Team burnout before release", "probability": 2, "impact": 3, "category": "Resource"},
]


def main():
    parser = argparse.ArgumentParser(
        description="Risk score calculator and priority assessor",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Score a single risk
  %(prog)s --probability 3 --impact 4

  # Score with detectability (RPN method)
  %(prog)s --probability 3 --impact 4 --detectability 2

  # Demo with sample risks
  %(prog)s --demo

  # Show risk matrix
  %(prog)s --matrix

  # JSON output
  %(prog)s --demo --json
        """,
    )
    parser.add_argument("--probability", "-p", type=int, help="Probability score (1-5)")
    parser.add_argument("--impact", "-i", type=int, help="Impact score (1-5)")
    parser.add_argument("--detectability", "-d", type=int, default=1, help="Detectability score (1-5, default: 1)")
    parser.add_argument("--demo", action="store_true", help="Score sample risks")
    parser.add_argument("--matrix", action="store_true", help="Display risk matrix")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.matrix:
        if args.json:
            print(json.dumps({"matrix": generate_risk_matrix()}, indent=2))
        else:
            print(format_matrix_text())
        return

    if args.demo:
        results = []
        for risk in SAMPLE_RISKS:
            result = calculate_risk_score(risk["probability"], risk["impact"])
            results.append({**risk, **result})

        if args.json:
            print(json.dumps({"risks": results}, indent=2))
        else:
            print("=" * 70)
            print("RISK ASSESSMENT - SAMPLE PROJECT")
            print("=" * 70)
            print()
            print(f"{'Risk':<30} {'Cat':<10} {'P':>3} {'I':>3} {'Score':>6} {'Level':<10}")
            print("-" * 70)
            for r in sorted(results, key=lambda x: x["score"], reverse=True):
                print(f"{r['name']:<30} {r['category']:<10} {r['probability']:>3} "
                      f"{r['impact']:>3} {r['score']:>6} {r['level']:<10}")
            print()

            # Summary
            levels = {}
            for r in results:
                levels[r["level"]] = levels.get(r["level"], 0) + 1
            print("SUMMARY")
            print("-" * 30)
            for level in ["CRITICAL", "HIGH", "MEDIUM", "LOW"]:
                count = levels.get(level, 0)
                if count > 0:
                    print(f"  {level:<10}: {count}")
            print()
            print(format_matrix_text())

    elif args.probability and args.impact:
        result = calculate_risk_score(args.probability, args.impact, args.detectability)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"Probability: {result['probability']}")
            print(f"Impact:      {result['impact']}")
            if args.detectability > 1:
                print(f"Detectability: {result['detectability']}")
            print(f"Score:       {result['score']} / {result['max_score']}")
            print(f"Level:       {result['level']}")
            print(f"Method:      {result['method']}")
            print()
            print("ESCALATION")
            esc = result["escalation"]
            print(f"  Target:   {esc['target']}")
            print(f"  Response: {esc['response_time']}")
            print(f"  Action:   {esc['action']}")
    else:
        print("Provide --probability and --impact, use --demo, or use --matrix.")
        print("Run with --help for usage information.")
        sys.exit(1)


if __name__ == "__main__":
    main()
