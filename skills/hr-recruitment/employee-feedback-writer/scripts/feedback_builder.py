#!/usr/bin/env python3
"""
Feedback Builder Tool

Structures employee feedback using the SBI (Situation-Behavior-Impact)
framework. Validates completeness, checks for common pitfalls, and
generates formatted feedback documents.

Usage:
    python feedback_builder.py --demo
    python feedback_builder.py --input feedback_data.json
    python feedback_builder.py --interactive
"""

import argparse
import json
import re
import sys

# --- Feedback Quality Checks ---

VAGUE_PHRASES = [
    "good job",
    "great work",
    "nice job",
    "well done",
    "keep it up",
    "needs improvement",
    "could be better",
    "not good enough",
    "always",
    "never",
    "everyone knows",
    "you are",
    "you seem",
    "I feel like you",
    "attitude",
    "personality",
]

CHARACTER_JUDGMENTS = [
    "lazy",
    "careless",
    "irresponsible",
    "unprofessional",
    "difficult",
    "negative",
    "disorganized",
    "unreliable",
    "incompetent",
    "brilliant",
    "genius",
    "perfect",
    "amazing",
]

ABSOLUTIST_TERMS = [
    "always",
    "never",
    "every time",
    "constantly",
    "all the time",
    "everyone",
    "nobody",
    "nothing",
]

# --- Sample Data ---

SAMPLE_FEEDBACK_SET = {
    "employee": {
        "name": "Jordan Kim",
        "role": "Software Engineer",
        "level": "Mid (L3)",
        "department": "Platform Engineering",
        "manager": "Pat Rodriguez",
        "review_period": "Q1 2026",
    },
    "overall_rating": 4,
    "goals": [
        {
            "goal": "Improve API response time by 30%",
            "target": "P95 latency under 200ms",
            "actual": "P95 latency at 150ms (25% better than target)",
            "rating": 5,
        },
        {
            "goal": "Mentor one junior engineer",
            "target": "Junior engineer completes first independent project",
            "actual": "Mentee shipped two features independently",
            "rating": 4,
        },
        {
            "goal": "Reduce on-call alerts by 50%",
            "target": "From 20 alerts/week to 10",
            "actual": "Reduced to 12 alerts/week (40% reduction)",
            "rating": 3,
        },
    ],
    "accomplishments": [
        {
            "situation": "During the Q1 performance optimization sprint in February",
            "behavior": "Jordan profiled the entire API layer, identified three bottleneck queries, and rewrote them using optimized indexes and caching strategies",
            "impact": "API P95 latency dropped from 380ms to 150ms, exceeding the 200ms target. Customer-reported timeout errors decreased by 85%, and the sales team reported that performance was no longer a blocker in enterprise deals.",
        },
        {
            "situation": "When the junior engineer (Sam) struggled with their first feature assignment in January",
            "behavior": "Jordan set up twice-weekly pairing sessions, created a structured learning plan, and broke the feature into progressive milestones with clear acceptance criteria",
            "impact": "Sam shipped the feature on schedule and went on to complete a second feature independently. Sam reported in their survey that Jordan's mentorship was the most valuable part of their onboarding.",
        },
    ],
    "development_areas": [
        {
            "situation": "In three sprint planning meetings during Q1 (Jan 15, Feb 5, Feb 26)",
            "behavior": "Jordan committed to stretch goals without factoring in on-call duties and code review responsibilities, leading to incomplete sprint work in two of the three sprints",
            "impact": "The team had to redistribute 15 story points across those sprints, and two planned features slipped to the next sprint. This created downstream delays for the QA team.",
            "suggested_action": "Before committing in sprint planning, account for recurring responsibilities (on-call, reviews, meetings) and commit to 80% capacity to leave room for unplanned work.",
        },
    ],
    "competency_ratings": {
        "Technical Skills": {"rating": 4, "evidence": "Strong optimization work; needs to broaden system design skills"},
        "Communication": {"rating": 3, "evidence": "Clear in 1:1s but could improve written documentation"},
        "Collaboration": {"rating": 4, "evidence": "Excellent mentorship; proactive in code reviews"},
        "Problem Solving": {"rating": 5, "evidence": "Exceptional debugging and optimization skills"},
        "Leadership / Initiative": {"rating": 3, "evidence": "Takes initiative on technical problems; needs to step up on process improvement"},
        "Adaptability": {"rating": 4, "evidence": "Handled mid-quarter priority shifts well"},
    },
}


def validate_sbi(feedback_item, feedback_type="accomplishment"):
    """Validate the quality of an SBI feedback item."""
    issues = []
    warnings = []

    # Check completeness
    for component in ["situation", "behavior", "impact"]:
        if not feedback_item.get(component) or len(feedback_item[component].strip()) < 10:
            issues.append(f"Missing or too brief: {component}")

    situation = feedback_item.get("situation", "").lower()
    behavior = feedback_item.get("behavior", "").lower()
    impact = feedback_item.get("impact", "").lower()
    full_text = f"{situation} {behavior} {impact}"

    # Check for vague phrases
    for phrase in VAGUE_PHRASES:
        if phrase in full_text:
            warnings.append(f"Vague phrase detected: '{phrase}'. Be more specific.")

    # Check for character judgments
    for judgment in CHARACTER_JUDGMENTS:
        if judgment in full_text:
            issues.append(f"Character judgment detected: '{judgment}'. Describe behavior, not personality.")

    # Check for absolutist terms
    for term in ABSOLUTIST_TERMS:
        if re.search(rf"\b{term}\b", full_text):
            warnings.append(f"Absolutist term: '{term}'. Use specific frequency or count instead.")

    # Check situation specificity
    date_pattern = r"\b(january|february|march|april|may|june|july|august|september|october|november|december|\d{1,2}/\d{1,2}|\d{4}|q[1-4]|last\s+(?:week|month|quarter))\b"
    if not re.search(date_pattern, situation):
        warnings.append("Situation lacks a specific time reference. Add when this occurred.")

    # Check impact for measurability
    number_pattern = r"\b\d+[%xX]?\b|\$\d"
    if not re.search(number_pattern, impact):
        warnings.append("Impact lacks quantified metrics. Add numbers where possible.")

    # Check for development area suggestions
    if feedback_type == "development" and not feedback_item.get("suggested_action"):
        issues.append("Development feedback should include a suggested action.")

    quality_score = 100
    quality_score -= len(issues) * 20
    quality_score -= len(warnings) * 5
    quality_score = max(0, min(100, quality_score))

    return {
        "quality_score": quality_score,
        "issues": issues,
        "warnings": warnings,
        "passed": len(issues) == 0,
    }


def validate_review(review_data):
    """Validate a complete performance review."""
    results = {
        "employee": review_data["employee"]["name"],
        "review_period": review_data["employee"]["review_period"],
        "overall_rating": review_data["overall_rating"],
        "validation": {
            "accomplishments": [],
            "development_areas": [],
            "goals": {"total": 0, "rated": 0},
            "competencies": {"total": 0, "rated": 0, "with_evidence": 0},
            "overall_quality": 0,
            "issues": [],
            "warnings": [],
        },
    }

    # Validate accomplishments
    for i, acc in enumerate(review_data.get("accomplishments", [])):
        validation = validate_sbi(acc, "accomplishment")
        results["validation"]["accomplishments"].append({
            "index": i + 1,
            "situation_preview": acc.get("situation", "")[:60] + "...",
            **validation,
        })

    # Validate development areas
    for i, dev in enumerate(review_data.get("development_areas", [])):
        validation = validate_sbi(dev, "development")
        results["validation"]["development_areas"].append({
            "index": i + 1,
            "situation_preview": dev.get("situation", "")[:60] + "...",
            **validation,
        })

    # Check goals
    goals = review_data.get("goals", [])
    results["validation"]["goals"]["total"] = len(goals)
    results["validation"]["goals"]["rated"] = sum(1 for g in goals if g.get("rating"))

    # Check competencies
    comps = review_data.get("competency_ratings", {})
    results["validation"]["competencies"]["total"] = len(comps)
    results["validation"]["competencies"]["rated"] = sum(1 for c in comps.values() if c.get("rating"))
    results["validation"]["competencies"]["with_evidence"] = sum(1 for c in comps.values() if c.get("evidence"))

    # Overall checks
    if len(review_data.get("accomplishments", [])) < 2:
        results["validation"]["warnings"].append("Include at least 2 accomplishments with SBI evidence.")

    if len(review_data.get("development_areas", [])) < 1:
        results["validation"]["warnings"].append("Include at least 1 development area for growth.")

    if review_data.get("overall_rating") == 5 and len(review_data.get("development_areas", [])) == 0:
        results["validation"]["issues"].append("Even exceptional employees need development areas. Add at least one.")

    if review_data.get("overall_rating") == 1 and len(review_data.get("accomplishments", [])) == 0:
        results["validation"]["warnings"].append("Even underperforming employees may have some positives. Consider adding at least one accomplishment to show balanced evaluation.")

    # Calculate overall quality
    all_validations = results["validation"]["accomplishments"] + results["validation"]["development_areas"]
    if all_validations:
        avg_quality = sum(v["quality_score"] for v in all_validations) / len(all_validations)
    else:
        avg_quality = 0

    completeness = 0
    if results["validation"]["goals"]["rated"] > 0:
        completeness += 25
    if results["validation"]["competencies"]["with_evidence"] == results["validation"]["competencies"]["total"]:
        completeness += 25
    if len(review_data.get("accomplishments", [])) >= 2:
        completeness += 25
    if len(review_data.get("development_areas", [])) >= 1:
        completeness += 25

    results["validation"]["overall_quality"] = round(avg_quality * 0.6 + completeness * 0.4)
    results["validation"]["completeness"] = completeness

    return results


def format_review_document(review_data):
    """Format review data into a readable document."""
    e = review_data["employee"]
    lines = []
    lines.append(f"QUARTERLY PERFORMANCE REVIEW")
    lines.append(f"{'='*50}")
    lines.append(f"Employee: {e['name']}")
    lines.append(f"Role: {e['role']} ({e['level']})")
    lines.append(f"Department: {e['department']}")
    lines.append(f"Manager: {e['manager']}")
    lines.append(f"Period: {e['review_period']}")
    lines.append(f"Overall Rating: {review_data['overall_rating']}/5")
    lines.append("")

    lines.append("GOAL ACHIEVEMENT")
    lines.append("-" * 40)
    for g in review_data.get("goals", []):
        lines.append(f"  Goal: {g['goal']}")
        lines.append(f"  Target: {g['target']}")
        lines.append(f"  Actual: {g['actual']}")
        lines.append(f"  Rating: {g['rating']}/5")
        lines.append("")

    lines.append("KEY ACCOMPLISHMENTS")
    lines.append("-" * 40)
    for i, a in enumerate(review_data.get("accomplishments", []), 1):
        lines.append(f"  {i}. Situation: {a['situation']}")
        lines.append(f"     Behavior: {a['behavior']}")
        lines.append(f"     Impact: {a['impact']}")
        lines.append("")

    lines.append("AREAS FOR DEVELOPMENT")
    lines.append("-" * 40)
    for i, d in enumerate(review_data.get("development_areas", []), 1):
        lines.append(f"  {i}. Situation: {d['situation']}")
        lines.append(f"     Behavior: {d['behavior']}")
        lines.append(f"     Impact: {d['impact']}")
        lines.append(f"     Action: {d.get('suggested_action', 'TBD')}")
        lines.append("")

    lines.append("COMPETENCY RATINGS")
    lines.append("-" * 40)
    for comp, data in review_data.get("competency_ratings", {}).items():
        lines.append(f"  {comp}: {data['rating']}/5")
        lines.append(f"    Evidence: {data['evidence']}")
        lines.append("")

    return "\n".join(lines)


def print_summary(results):
    """Print human-readable validation summary."""
    v = results["validation"]
    print(f"=== FEEDBACK QUALITY REPORT ===")
    print(f"Employee: {results['employee']}")
    print(f"Period: {results['review_period']}")
    print(f"Overall Rating: {results['overall_rating']}/5")
    print(f"")
    print(f"Quality Score: {v['overall_quality']}/100")
    print(f"Completeness: {v['completeness']}/100")
    print(f"")

    print(f"Accomplishments ({len(v['accomplishments'])}):")
    for a in v["accomplishments"]:
        status = "PASS" if a["passed"] else "FAIL"
        print(f"  [{status}] #{a['index']}: {a['situation_preview']} (Score: {a['quality_score']})")
        for issue in a["issues"]:
            print(f"    ERROR: {issue}")
        for warning in a["warnings"]:
            print(f"    WARN: {warning}")

    print(f"\nDevelopment Areas ({len(v['development_areas'])}):")
    for d in v["development_areas"]:
        status = "PASS" if d["passed"] else "FAIL"
        print(f"  [{status}] #{d['index']}: {d['situation_preview']} (Score: {d['quality_score']})")
        for issue in d["issues"]:
            print(f"    ERROR: {issue}")
        for warning in d["warnings"]:
            print(f"    WARN: {warning}")

    print(f"\nGoals: {v['goals']['rated']}/{v['goals']['total']} rated")
    print(f"Competencies: {v['competencies']['with_evidence']}/{v['competencies']['total']} with evidence")

    if v["issues"]:
        print(f"\nReview-Level Issues:")
        for issue in v["issues"]:
            print(f"  ERROR: {issue}")

    if v["warnings"]:
        print(f"\nReview-Level Warnings:")
        for warning in v["warnings"]:
            print(f"  WARN: {warning}")


def main():
    parser = argparse.ArgumentParser(
        description="Build and validate employee feedback using SBI framework."
    )
    parser.add_argument("--input", help="Path to JSON file with feedback data")
    parser.add_argument("--demo", action="store_true", help="Run with sample data")
    parser.add_argument(
        "--mode",
        choices=["validate", "format", "both"],
        default="both",
        help="validate: check quality | format: generate document | both: do both",
    )
    parser.add_argument("--format", choices=["json", "summary"], default="json", help="Output format")

    args = parser.parse_args()

    if args.demo:
        data = SAMPLE_FEEDBACK_SET
    elif args.input:
        try:
            with open(args.input, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(json.dumps({"error": str(e)}))
            sys.exit(1)
    else:
        parser.error("Either --demo or --input is required")
        sys.exit(1)

    output = {}

    if args.mode in ("validate", "both"):
        validation = validate_review(data)
        output["validation"] = validation

    if args.mode in ("format", "both"):
        document = format_review_document(data)
        output["formatted_document"] = document

    if args.format == "summary":
        if "validation" in output:
            print_summary(output["validation"])
        if "formatted_document" in output:
            print(f"\n{'='*50}")
            print(f"FORMATTED REVIEW DOCUMENT")
            print(f"{'='*50}\n")
            print(output["formatted_document"])
    else:
        print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
