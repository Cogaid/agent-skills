#!/usr/bin/env python3
"""
Analyze pipeline health and identify issues.

Usage:
    python analyze_pipeline.py pipeline.json
    python analyze_pipeline.py pipeline.json --aging-threshold 30

Output: JSON with pipeline analysis
"""

import argparse
import json
import sys
from datetime import datetime, timedelta


def parse_date(date_str):
    """Parse date string to datetime."""
    formats = ["%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y", "%Y-%m-%dT%H:%M:%S"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None


def analyze_deal(deal, today, aging_threshold):
    """Analyze a single deal for issues."""
    issues = []
    warnings = []

    deal_name = deal.get("name", deal.get("company", "Unknown"))

    # Check for aging
    last_activity = deal.get("last_activity")
    if last_activity:
        last_date = parse_date(last_activity)
        if last_date:
            days_since = (today - last_date).days
            if days_since > aging_threshold:
                issues.append({
                    "type": "aging",
                    "message": f"No activity in {days_since} days",
                    "days": days_since
                })
            elif days_since > aging_threshold // 2:
                warnings.append({
                    "type": "aging",
                    "message": f"Activity slowing ({days_since} days)",
                    "days": days_since
                })

    # Check for past close date
    expected_close = deal.get("expected_close", deal.get("close_date"))
    if expected_close:
        close_date = parse_date(expected_close)
        if close_date and close_date < today:
            days_past = (today - close_date).days
            issues.append({
                "type": "past_due",
                "message": f"Expected close was {days_past} days ago",
                "days": days_past
            })

    # Check for missing data
    required_fields = ["value", "stage", "contact", "next_step"]
    missing = [f for f in required_fields if not deal.get(f)]
    if missing:
        warnings.append({
            "type": "missing_data",
            "message": f"Missing: {', '.join(missing)}",
            "fields": missing
        })

    # Check for stuck in stage
    stage_entered = deal.get("stage_entered")
    if stage_entered:
        entered_date = parse_date(stage_entered)
        if entered_date:
            days_in_stage = (today - entered_date).days
            if days_in_stage > 60:
                issues.append({
                    "type": "stuck",
                    "message": f"In '{deal.get('stage', 'current stage')}' for {days_in_stage} days",
                    "days": days_in_stage
                })
            elif days_in_stage > 30:
                warnings.append({
                    "type": "stuck",
                    "message": f"In stage for {days_in_stage} days",
                    "days": days_in_stage
                })

    # Check qualification completeness
    bant = deal.get("qualification", {})
    missing_qual = []
    for criterion in ["budget", "authority", "need", "timeline"]:
        if criterion not in bant or bant[criterion] == "unknown":
            missing_qual.append(criterion)

    if missing_qual:
        warnings.append({
            "type": "qualification",
            "message": f"Incomplete qualification: {', '.join(missing_qual)}",
            "missing": missing_qual
        })

    return {
        "deal": deal_name,
        "value": deal.get("value", 0),
        "stage": deal.get("stage", "unknown"),
        "issues": issues,
        "warnings": warnings,
        "health": "critical" if issues else ("warning" if warnings else "healthy")
    }


def analyze_pipeline(deals, aging_threshold=30):
    """Analyze full pipeline."""
    today = datetime.now()

    deal_analyses = []
    for deal in deals:
        analysis = analyze_deal(deal, today, aging_threshold)
        deal_analyses.append(analysis)

    # Aggregate stats
    total_value = sum(d.get("value", 0) for d in deals)
    critical_count = sum(1 for a in deal_analyses if a["health"] == "critical")
    warning_count = sum(1 for a in deal_analyses if a["health"] == "warning")
    healthy_count = sum(1 for a in deal_analyses if a["health"] == "healthy")

    # At-risk value
    at_risk_value = sum(
        a["value"] for a in deal_analyses
        if a["health"] in ["critical", "warning"]
    )

    # Issue breakdown
    issue_types = {}
    for analysis in deal_analyses:
        for issue in analysis["issues"] + analysis["warnings"]:
            issue_type = issue["type"]
            issue_types[issue_type] = issue_types.get(issue_type, 0) + 1

    # Recommendations
    recommendations = []

    if critical_count > 0:
        critical_deals = [a["deal"] for a in deal_analyses if a["health"] == "critical"]
        recommendations.append({
            "priority": "high",
            "action": f"Review {critical_count} critical deals immediately",
            "deals": critical_deals[:5]
        })

    aging_deals = [
        a for a in deal_analyses
        if any(i["type"] == "aging" for i in a["issues"])
    ]
    if aging_deals:
        recommendations.append({
            "priority": "high",
            "action": f"Re-engage {len(aging_deals)} aging deals or remove from pipeline",
            "deals": [d["deal"] for d in aging_deals[:5]]
        })

    past_due = [
        a for a in deal_analyses
        if any(i["type"] == "past_due" for i in a["issues"])
    ]
    if past_due:
        recommendations.append({
            "priority": "medium",
            "action": f"Update close dates for {len(past_due)} past-due deals",
            "deals": [d["deal"] for d in past_due[:5]]
        })

    incomplete_qual = [
        a for a in deal_analyses
        if any(w["type"] == "qualification" for w in a["warnings"])
    ]
    if incomplete_qual:
        recommendations.append({
            "priority": "medium",
            "action": f"Complete qualification for {len(incomplete_qual)} deals",
            "deals": [d["deal"] for d in incomplete_qual[:5]]
        })

    return {
        "summary": {
            "total_deals": len(deals),
            "total_value": total_value,
            "healthy": healthy_count,
            "warning": warning_count,
            "critical": critical_count,
            "at_risk_value": at_risk_value
        },
        "issue_breakdown": issue_types,
        "deals": deal_analyses,
        "recommendations": recommendations
    }


def main():
    parser = argparse.ArgumentParser(description="Analyze pipeline health")
    parser.add_argument("file", help="JSON file with pipeline data")
    parser.add_argument("--aging-threshold", type=int, default=30,
                        help="Days without activity to flag (default 30)")

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

    # Handle both array and object with "deals" key
    deals = data if isinstance(data, list) else data.get("deals", [])

    result = analyze_pipeline(deals, args.aging_threshold)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
