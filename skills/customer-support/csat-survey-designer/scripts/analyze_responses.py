#!/usr/bin/env python3
"""Analyze collected survey responses and generate insights.

Usage:
    python scripts/analyze_responses.py --survey-id SRV-001 --period last-quarter
    python scripts/analyze_responses.py --survey-id SRV-001 --period last-month --format summary
    python scripts/analyze_responses.py --survey-id SRV-001 --period 2024-Q1 --segments channel,agent
"""

import argparse
import json
import random
import sys
from datetime import datetime

# Sample data for demonstration
SAMPLE_RESPONSES = [
    {"id": f"R-{i:04d}", "score": random.choice([1, 2, 3, 3, 4, 4, 4, 5, 5, 5]),
     "channel": random.choice(["chat", "email", "phone"]),
     "agent": random.choice(["Alice", "Bob", "Carol", "Dave"]),
     "text": random.choice([
         "Quick and helpful response",
         "Had to wait too long",
         "Agent was very knowledgeable",
         "Issue was not fully resolved",
         "Great experience overall",
         "Needed to explain my issue multiple times",
         "Fast resolution, thank you",
         "",
     ]),
     "resolved": random.choice([True, True, True, False]),
     "timestamp": f"2024-{random.randint(1,3):02d}-{random.randint(1,28):02d}T{random.randint(8,18):02d}:00:00Z"}
    for i in range(200)
]

# Fix random seed for consistent demo output
random.seed(42)


def compute_csat_metrics(responses):
    """Compute CSAT score and distribution."""
    scores = [r["score"] for r in responses]
    total = len(scores)
    if total == 0:
        return {"error": "No responses found"}

    distribution = {}
    for s in range(1, 6):
        count = scores.count(s)
        distribution[str(s)] = {"count": count, "percentage": round(count / total * 100, 1)}

    satisfied = sum(1 for s in scores if s >= 4)
    avg_score = sum(scores) / total

    return {
        "total_responses": total,
        "average_score": round(avg_score, 2),
        "csat_percentage": round(satisfied / total * 100, 1),
        "distribution": distribution,
        "median_score": sorted(scores)[total // 2],
    }


def compute_segments(responses, segment_fields):
    """Break down scores by segment."""
    segments = {}
    for field in segment_fields:
        field_segments = {}
        values = set(r.get(field, "unknown") for r in responses)
        for val in values:
            subset = [r for r in responses if r.get(field) == val]
            scores = [r["score"] for r in subset]
            if scores:
                field_segments[str(val)] = {
                    "count": len(scores),
                    "average_score": round(sum(scores) / len(scores), 2),
                    "csat_pct": round(sum(1 for s in scores if s >= 4) / len(scores) * 100, 1),
                }
        segments[field] = field_segments
    return segments


def extract_themes(responses):
    """Extract common themes from open-text responses."""
    theme_keywords = {
        "wait_time": ["wait", "long", "slow", "delay"],
        "agent_knowledge": ["knowledgeable", "helpful", "understood", "expert"],
        "resolution": ["resolved", "fixed", "solved", "not resolved", "not fully"],
        "communication": ["explain", "clear", "confusing", "multiple times"],
        "speed": ["quick", "fast", "immediate", "prompt"],
    }

    theme_counts = {theme: {"positive": 0, "negative": 0, "total": 0} for theme in theme_keywords}

    for r in responses:
        text = r.get("text", "").lower()
        if not text:
            continue
        score = r["score"]
        for theme, keywords in theme_keywords.items():
            if any(kw in text for kw in keywords):
                theme_counts[theme]["total"] += 1
                if score >= 4:
                    theme_counts[theme]["positive"] += 1
                else:
                    theme_counts[theme]["negative"] += 1

    # Sort by total mentions
    sorted_themes = sorted(theme_counts.items(), key=lambda x: x[1]["total"], reverse=True)
    return {theme: counts for theme, counts in sorted_themes if counts["total"] > 0}


def generate_recommendations(metrics, themes, segments):
    """Generate improvement recommendations based on analysis."""
    recommendations = []

    if metrics["csat_percentage"] < 80:
        recommendations.append({
            "priority": "high",
            "area": "overall_satisfaction",
            "recommendation": "CSAT is below 80% target. Conduct agent coaching sessions focused on top negative themes.",
        })

    if metrics["average_score"] < 4.0:
        recommendations.append({
            "priority": "high",
            "area": "score_improvement",
            "recommendation": f"Average score is {metrics['average_score']}. Review bottom-quartile interactions for common failure patterns.",
        })

    for theme, counts in themes.items():
        if counts["negative"] > counts["positive"] and counts["total"] >= 5:
            recommendations.append({
                "priority": "medium",
                "area": theme,
                "recommendation": f"Theme '{theme}' has more negative than positive mentions ({counts['negative']} neg vs {counts['positive']} pos). Investigate root cause.",
            })

    if not recommendations:
        recommendations.append({
            "priority": "low",
            "area": "maintenance",
            "recommendation": "Scores are within target. Continue monitoring and run quarterly deep-dive analysis.",
        })

    return recommendations


def main():
    parser = argparse.ArgumentParser(
        description="Analyze collected survey responses"
    )
    parser.add_argument(
        "--survey-id",
        required=True,
        help="Survey identifier (e.g., SRV-001)",
    )
    parser.add_argument(
        "--period",
        default="last-quarter",
        help="Analysis period: last-week, last-month, last-quarter, or YYYY-QN (default: last-quarter)",
    )
    parser.add_argument(
        "--segments",
        default="channel,agent",
        help="Comma-separated fields to segment by (default: channel,agent)",
    )
    parser.add_argument(
        "--format",
        choices=["full", "summary", "json"],
        default="full",
        help="Output format (default: full)",
    )

    args = parser.parse_args()

    # Use sample data for demonstration
    responses = SAMPLE_RESPONSES
    segment_fields = [s.strip() for s in args.segments.split(",")]

    metrics = compute_csat_metrics(responses)
    segments = compute_segments(responses, segment_fields)
    themes = extract_themes(responses)
    recommendations = generate_recommendations(metrics, themes, segments)

    report = {
        "survey_id": args.survey_id,
        "period": args.period,
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "metrics": metrics,
        "segments": segments,
        "themes": themes,
        "recommendations": recommendations,
    }

    if args.format == "summary":
        summary = {
            "survey_id": args.survey_id,
            "period": args.period,
            "csat_percentage": metrics["csat_percentage"],
            "average_score": metrics["average_score"],
            "total_responses": metrics["total_responses"],
            "top_recommendation": recommendations[0]["recommendation"] if recommendations else "None",
        }
        print(json.dumps(summary, indent=2))
    else:
        print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
