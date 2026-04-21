#!/usr/bin/env python3
"""
Resume Scoring Tool

Scores resumes against job criteria using a weighted rubric. Supports
batch processing and generates ranked shortlists with decision recommendations.

Usage:
    python resume_scorer.py --demo
    python resume_scorer.py --criteria criteria.json --resumes resumes.json
    python resume_scorer.py --criteria criteria.json --resumes resumes.json --format summary
"""

import argparse
import json
import sys

# --- Sample Data ---

SAMPLE_CRITERIA = {
    "position": "Senior Backend Engineer",
    "criteria": [
        {"name": "Relevant Experience", "weight": 25, "must_have": True},
        {"name": "Technical Skills (Core)", "weight": 25, "must_have": True},
        {"name": "System Design", "weight": 15, "must_have": False},
        {"name": "Achievements / Impact", "weight": 15, "must_have": False},
        {"name": "Education", "weight": 10, "must_have": False},
        {"name": "Communication Quality", "weight": 5, "must_have": False},
        {"name": "Culture Alignment", "weight": 5, "must_have": False},
    ],
    "thresholds": {
        "advance": 80,
        "hold": 60,
        "waitlist": 40,
    },
}

SAMPLE_RESUMES = [
    {
        "candidate_id": "C001",
        "name": "Alex Chen",
        "scores": {
            "Relevant Experience": 3,
            "Technical Skills (Core)": 3,
            "System Design": 2,
            "Achievements / Impact": 3,
            "Education": 2,
            "Communication Quality": 3,
            "Culture Alignment": 2,
        },
        "notes": {
            "Relevant Experience": "8 years backend, 4 at scale-up companies",
            "Technical Skills (Core)": "Expert Go and Python, strong Kubernetes",
            "Achievements / Impact": "Led migration saving $500K/year in infra costs",
        },
        "red_flags": [],
        "green_flags": ["Quantified achievements", "Progressive responsibility"],
    },
    {
        "candidate_id": "C002",
        "name": "Jordan Smith",
        "scores": {
            "Relevant Experience": 2,
            "Technical Skills (Core)": 2,
            "System Design": 2,
            "Achievements / Impact": 1,
            "Education": 3,
            "Communication Quality": 2,
            "Culture Alignment": 2,
        },
        "notes": {
            "Relevant Experience": "5 years, mostly at large enterprises",
            "Technical Skills (Core)": "Strong Java, learning Go",
            "Achievements / Impact": "Mentions projects but no quantified outcomes",
        },
        "red_flags": ["No quantified achievements"],
        "green_flags": ["Strong education (MS CS)"],
    },
    {
        "candidate_id": "C003",
        "name": "Taylor Martinez",
        "scores": {
            "Relevant Experience": 3,
            "Technical Skills (Core)": 3,
            "System Design": 3,
            "Achievements / Impact": 2,
            "Education": 1,
            "Communication Quality": 3,
            "Culture Alignment": 3,
        },
        "notes": {
            "Relevant Experience": "10 years, including 3 at FAANG",
            "Technical Skills (Core)": "Expert in Go, Rust, distributed systems",
            "System Design": "Designed systems handling 1M+ RPS",
            "Education": "Bootcamp graduate, no traditional degree",
        },
        "red_flags": [],
        "green_flags": ["FAANG experience", "System design at scale", "Open source contributor"],
    },
    {
        "candidate_id": "C004",
        "name": "Sam Williams",
        "scores": {
            "Relevant Experience": 1,
            "Technical Skills (Core)": 2,
            "System Design": 1,
            "Achievements / Impact": 1,
            "Education": 2,
            "Communication Quality": 2,
            "Culture Alignment": 1,
        },
        "notes": {
            "Relevant Experience": "3 years, mostly frontend with some backend",
            "Technical Skills (Core)": "JavaScript/Node.js, some Python",
        },
        "red_flags": ["Limited backend experience", "No system design evidence"],
        "green_flags": [],
    },
    {
        "candidate_id": "C005",
        "name": "Morgan Lee",
        "scores": {
            "Relevant Experience": 2,
            "Technical Skills (Core)": 3,
            "System Design": 2,
            "Achievements / Impact": 2,
            "Education": 2,
            "Communication Quality": 2,
            "Culture Alignment": 2,
        },
        "notes": {
            "Relevant Experience": "6 years, 2 year gap (returned from caregiving)",
            "Technical Skills (Core)": "Strong Go and distributed systems skills",
            "Achievements / Impact": "Led team of 4, shipped 2 major features",
        },
        "red_flags": ["2-year employment gap (caregiving - investigate in screen)"],
        "green_flags": ["Strong technical skills despite gap", "Leadership experience"],
    },
]


def calculate_weighted_score(scores, criteria):
    """Calculate the weighted score for a candidate."""
    total_weighted = 0
    max_possible = 0

    for criterion in criteria:
        name = criterion["name"]
        weight = criterion["weight"]
        score = scores.get(name, 0)

        normalized = score / 3.0  # 0-3 scale normalized to 0-1
        total_weighted += normalized * weight
        max_possible += weight

    if max_possible == 0:
        return 0

    return round(total_weighted / max_possible * 100, 1)


def check_must_haves(scores, criteria):
    """Check if all must-have criteria score above 0."""
    failed = []
    for criterion in criteria:
        if criterion["must_have"]:
            score = scores.get(criterion["name"], 0)
            if score == 0:
                failed.append(criterion["name"])
    return failed


def determine_decision(weighted_score, thresholds, must_have_failures):
    """Determine the screening decision based on score and thresholds."""
    if must_have_failures:
        return "decline", f"Failed must-have criteria: {', '.join(must_have_failures)}"

    if weighted_score >= thresholds["advance"]:
        return "advance", "Score meets advance threshold"
    elif weighted_score >= thresholds["hold"]:
        return "hold", "Borderline - review with hiring manager"
    elif weighted_score >= thresholds["waitlist"]:
        return "waitlist", "Below threshold but may suit future roles"
    else:
        return "decline", "Score below minimum threshold"


def score_batch(criteria_config, resumes):
    """Score a batch of resumes and generate a ranked shortlist."""
    results = {
        "position": criteria_config["position"],
        "total_candidates": len(resumes),
        "criteria_used": criteria_config["criteria"],
        "thresholds": criteria_config["thresholds"],
        "candidates": [],
        "summary": {
            "advance": 0,
            "hold": 0,
            "waitlist": 0,
            "decline": 0,
        },
    }

    for resume in resumes:
        weighted_score = calculate_weighted_score(
            resume["scores"], criteria_config["criteria"]
        )
        must_have_failures = check_must_haves(
            resume["scores"], criteria_config["criteria"]
        )
        decision, reason = determine_decision(
            weighted_score, criteria_config["thresholds"], must_have_failures
        )

        candidate_result = {
            "candidate_id": resume["candidate_id"],
            "name": resume.get("name", "Anonymous"),
            "weighted_score": weighted_score,
            "decision": decision,
            "reason": reason,
            "must_have_pass": len(must_have_failures) == 0,
            "must_have_failures": must_have_failures,
            "criterion_scores": [],
            "red_flags": resume.get("red_flags", []),
            "green_flags": resume.get("green_flags", []),
        }

        for criterion in criteria_config["criteria"]:
            name = criterion["name"]
            score = resume["scores"].get(name, 0)
            candidate_result["criterion_scores"].append({
                "criterion": name,
                "weight": criterion["weight"],
                "must_have": criterion["must_have"],
                "score": score,
                "max_score": 3,
                "notes": resume.get("notes", {}).get(name, ""),
            })

        results["candidates"].append(candidate_result)
        results["summary"][decision] += 1

    # Sort by weighted score descending
    results["candidates"].sort(key=lambda x: x["weighted_score"], reverse=True)

    # Add rank
    for i, candidate in enumerate(results["candidates"], 1):
        candidate["rank"] = i

    return results


def print_summary(results):
    """Print a human-readable summary of results."""
    print(f"=== RESUME SCREENING REPORT ===")
    print(f"Position: {results['position']}")
    print(f"Total Candidates: {results['total_candidates']}")
    print(f"")
    print(f"Decision Summary:")
    print(f"  Advance:  {results['summary']['advance']}")
    print(f"  Hold:     {results['summary']['hold']}")
    print(f"  Waitlist: {results['summary']['waitlist']}")
    print(f"  Decline:  {results['summary']['decline']}")
    print(f"")
    print(f"Ranked Candidates:")
    print(f"{'Rank':<6}{'ID':<8}{'Name':<22}{'Score':<10}{'Decision':<12}{'Flags'}")
    print(f"{'-'*80}")
    for c in results["candidates"]:
        flags = ""
        if c["red_flags"]:
            flags += f"RED: {len(c['red_flags'])} "
        if c["green_flags"]:
            flags += f"GREEN: {len(c['green_flags'])}"
        print(f"{c['rank']:<6}{c['candidate_id']:<8}{c['name']:<22}{c['weighted_score']:<10}{c['decision']:<12}{flags}")

    print(f"")
    print(f"Detailed Breakdown:")
    for c in results["candidates"]:
        print(f"\n  {c['rank']}. {c['name']} ({c['candidate_id']}) - {c['weighted_score']}% - {c['decision'].upper()}")
        print(f"     Reason: {c['reason']}")
        if c["red_flags"]:
            print(f"     Red Flags: {'; '.join(c['red_flags'])}")
        if c["green_flags"]:
            print(f"     Green Flags: {'; '.join(c['green_flags'])}")


def main():
    parser = argparse.ArgumentParser(
        description="Score resumes against job criteria and generate ranked shortlists."
    )
    parser.add_argument("--criteria", help="Path to JSON file with screening criteria")
    parser.add_argument("--resumes", help="Path to JSON file with resume scores")
    parser.add_argument("--demo", action="store_true", help="Run with sample data")
    parser.add_argument("--format", choices=["json", "summary"], default="json", help="Output format (default: json)")

    args = parser.parse_args()

    if args.demo:
        criteria_config = SAMPLE_CRITERIA
        resumes = SAMPLE_RESUMES
    elif args.criteria and args.resumes:
        try:
            with open(args.criteria, "r") as f:
                criteria_config = json.load(f)
            with open(args.resumes, "r") as f:
                resumes = json.load(f)
        except FileNotFoundError as e:
            print(json.dumps({"error": str(e)}))
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(json.dumps({"error": f"Invalid JSON: {e}"}))
            sys.exit(1)
    else:
        parser.error("Either --demo or both --criteria and --resumes are required")
        sys.exit(1)

    results = score_batch(criteria_config, resumes)

    if args.format == "summary":
        print_summary(results)
    else:
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
