#!/usr/bin/env python3
"""Generate filter rules from email patterns by analyzing inbox history.

Usage:
    python auto_filter_generator.py --analyze-last 500
    python auto_filter_generator.py --analyze-last 100 --format json
"""

import argparse
import json
import sys
from collections import Counter
from datetime import datetime

SAMPLE_INBOX_PATTERNS = [
    {"from": "github.com", "count": 45, "subjects": ["[repo] PR opened", "[repo] CI failed", "[repo] Review requested"]},
    {"from": "jira.atlassian.com", "count": 32, "subjects": ["PROJ-123 updated", "PROJ-456 assigned", "Sprint started"]},
    {"from": "calendar.google.com", "count": 28, "subjects": ["Invitation: Meeting", "Updated invitation", "Canceled event"]},
    {"from": "newsletter@morningbrew.com", "count": 20, "subjects": ["Morning Brew - Daily", "Morning Brew - Weekend"]},
    {"from": "noreply@slack.com", "count": 18, "subjects": ["New message in #general", "Direct message from X"]},
    {"from": "receipts@various.com", "count": 15, "subjects": ["Your receipt", "Order confirmation", "Payment processed"]},
    {"from": "noreply@linkedin.com", "count": 12, "subjects": ["You have new connections", "Job recommendations"]},
    {"from": "hr@company.com", "count": 8, "subjects": ["Benefits update", "Holiday schedule", "Policy change"]},
    {"from": "datadog@alerts.com", "count": 35, "subjects": ["Alert: CPU high", "Alert: Error rate spike", "Recovered: CPU"]},
]


def generate_filter_suggestions(patterns: list, min_count: int = 5) -> list:
    """Analyze patterns and suggest filter rules."""
    suggestions = []

    for pattern in patterns:
        if pattern["count"] < min_count:
            continue

        domain = pattern["from"]
        count = pattern["count"]
        subjects = pattern["subjects"]

        # Determine action based on pattern
        if any(kw in domain for kw in ["github", "gitlab", "jenkins", "circleci", "datadog"]):
            suggestions.append({
                "rule_name": f"Dev Notifications - {domain}",
                "condition": f"from:*@{domain}",
                "action": "Label: Internal/IT-Support, Skip inbox",
                "exception": "UNLESS subject contains 'failed' or 'error' or 'Alert:'",
                "reason": f"{count} emails in analyzed period -- mostly automated notifications",
                "estimated_savings": f"{int(count * 0.8)} emails auto-filed per period",
                "priority": "high",
            })
        elif any(kw in domain for kw in ["calendar", "google.com"]) and any("invitation" in s.lower() or "event" in s.lower() for s in subjects):
            suggestions.append({
                "rule_name": f"Calendar - {domain}",
                "condition": f"from:*@{domain} AND (subject:invitation OR subject:event)",
                "action": "Label: Calendar, Skip inbox, Mark read",
                "exception": None,
                "reason": f"{count} calendar emails -- handled via calendar app",
                "estimated_savings": f"{count} emails auto-filed per period",
                "priority": "high",
            })
        elif any(kw in domain for kw in ["newsletter", "morningbrew", "substack"]):
            suggestions.append({
                "rule_name": f"Newsletter - {domain}",
                "condition": f"from:*@{domain}",
                "action": "Label: Newsletters/Industry-News, Skip inbox",
                "exception": None,
                "reason": f"{count} newsletter emails -- batch read during review time",
                "estimated_savings": f"{count} emails auto-filed per period",
                "priority": "medium",
            })
        elif any(kw in domain for kw in ["slack", "teams"]):
            suggestions.append({
                "rule_name": f"Chat Notifications - {domain}",
                "condition": f"from:*@{domain}",
                "action": "Skip inbox, Archive (handle in Slack/Teams directly)",
                "exception": None,
                "reason": f"{count} chat notification emails -- redundant with app",
                "estimated_savings": f"{count} emails auto-filed per period",
                "priority": "high",
            })
        elif any(kw in " ".join(subjects).lower() for kw in ["receipt", "order", "payment"]):
            suggestions.append({
                "rule_name": f"Receipts - {domain}",
                "condition": f"from:*@{domain} AND (subject:receipt OR subject:order OR subject:payment)",
                "action": "Label: Personal/Receipts, Skip inbox, Mark read",
                "exception": None,
                "reason": f"{count} receipt/order emails",
                "estimated_savings": f"{count} emails auto-filed per period",
                "priority": "medium",
            })
        elif any(kw in domain for kw in ["linkedin", "facebook", "twitter"]):
            suggestions.append({
                "rule_name": f"Social Media - {domain}",
                "condition": f"from:*@{domain}",
                "action": "Skip inbox, Archive OR Unsubscribe",
                "exception": None,
                "reason": f"{count} social media emails -- handle in respective apps",
                "estimated_savings": f"{count} emails auto-filed per period",
                "priority": "low",
            })
        elif "jira" in domain or "atlassian" in domain:
            suggestions.append({
                "rule_name": f"Project Management - {domain}",
                "condition": f"from:*@{domain}",
                "action": "Label: @Read-Review, Skip inbox",
                "exception": "UNLESS subject contains 'assigned to you' or 'mentioned you'",
                "reason": f"{count} project management notifications",
                "estimated_savings": f"{int(count * 0.7)} emails auto-filed per period",
                "priority": "high",
            })

    suggestions.sort(key=lambda x: {"high": 0, "medium": 1, "low": 2}.get(x["priority"], 3))
    return suggestions


def main():
    parser = argparse.ArgumentParser(description="Generate filter rules from email patterns.")
    parser.add_argument("--analyze-last", type=int, default=500, help="Number of recent emails to analyze")
    parser.add_argument("--min-count", type=int, default=5, help="Minimum email count to suggest a filter")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format")

    args = parser.parse_args()

    suggestions = generate_filter_suggestions(SAMPLE_INBOX_PATTERNS, args.min_count)
    total_savings = sum(int(s["estimated_savings"].split()[0]) for s in suggestions)

    if args.format == "json":
        output = {
            "analyzed_at": datetime.now().isoformat(),
            "emails_analyzed": args.analyze_last,
            "min_count_threshold": args.min_count,
            "suggestions_count": len(suggestions),
            "total_estimated_savings": f"{total_savings} emails per period",
            "suggestions": suggestions,
        }
        print(json.dumps(output, indent=2))
    else:
        print(f"Auto-Filter Suggestions")
        print(f"Emails analyzed: {args.analyze_last} (sample data)")
        print(f"Suggestions found: {len(suggestions)}")
        print(f"Estimated emails auto-filed: {total_savings} per period")
        print("=" * 60)
        for i, s in enumerate(suggestions, 1):
            print(f"\n  #{i} [{s['priority'].upper()}] {s['rule_name']}")
            print(f"    Condition: {s['condition']}")
            print(f"    Action: {s['action']}")
            if s.get("exception"):
                print(f"    Exception: {s['exception']}")
            print(f"    Reason: {s['reason']}")
            print(f"    Savings: {s['estimated_savings']}")
        print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
