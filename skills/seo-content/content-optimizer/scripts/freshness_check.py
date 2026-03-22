#!/usr/bin/env python3
"""
Check content for freshness and outdated elements.

Usage:
    python freshness_check.py page.md
    python freshness_check.py page.md --current-year 2025

Output: Freshness report with outdated elements
"""

import argparse
import json
import re
import sys
from datetime import datetime


def get_current_year():
    """Get the current year."""
    return datetime.now().year


def find_year_references(content, current_year):
    """Find year references in content."""
    # Find all 4-digit year references
    years = re.findall(r'\b(20\d{2})\b', content)

    outdated = []
    current = []
    future = []

    for year in years:
        year_int = int(year)
        if year_int < current_year - 1:
            outdated.append(year)
        elif year_int == current_year or year_int == current_year - 1:
            current.append(year)
        else:
            future.append(year)

    return {
        "outdated": list(set(outdated)),
        "current": list(set(current)),
        "future": list(set(future)),
        "oldest": min([int(y) for y in years]) if years else None,
        "newest": max([int(y) for y in years]) if years else None
    }


def find_outdated_references(content, current_year):
    """Find potentially outdated references."""
    issues = []

    # Check for "this year" without specific year
    if re.search(r'\bthis year\b', content, re.IGNORECASE):
        issues.append({
            "type": "vague_timeframe",
            "text": "Uses 'this year' without specific year",
            "suggestion": f"Replace with '{current_year}' for clarity"
        })

    # Check for "last year" without specific year
    if re.search(r'\blast year\b', content, re.IGNORECASE):
        issues.append({
            "type": "vague_timeframe",
            "text": "Uses 'last year' without specific year",
            "suggestion": f"Replace with '{current_year - 1}' for clarity"
        })

    # Check for "recently" or "just" without context
    if re.search(r'\b(recently|just recently|just)\b', content, re.IGNORECASE):
        issues.append({
            "type": "vague_timeframe",
            "text": "Uses vague time reference ('recently', 'just')",
            "suggestion": "Add specific date or timeframe"
        })

    # Check for specific outdated patterns
    outdated_patterns = [
        (r'\b2019\b', "Reference to 2019 - likely outdated"),
        (r'\b2020\b', "Reference to 2020 - may need update"),
        (r'\b2021\b', "Reference to 2021 - consider updating"),
        (r'COVID-?19 pandemic', "Pandemic reference - check if still relevant"),
        (r'\bnew\s+(feature|update|release)\b', "'New' claim may be outdated"),
        (r'\bupcoming\b', "'Upcoming' event may have passed"),
        (r'\bwill be\b', "Future tense may now be past"),
    ]

    for pattern, message in outdated_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            issues.append({
                "type": "potentially_outdated",
                "text": message,
                "suggestion": "Verify information is current"
            })

    return issues


def find_broken_link_patterns(content):
    """Find patterns that might indicate broken links."""
    issues = []

    # Find all markdown links
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)

    for anchor, url in links:
        # Check for suspicious patterns
        if 'example.com' in url:
            issues.append({
                "type": "placeholder_link",
                "text": f"Placeholder link found: [{anchor}]({url})",
                "suggestion": "Replace with actual URL"
            })
        elif url.startswith('#') and ' ' in url:
            issues.append({
                "type": "malformed_anchor",
                "text": f"Possibly malformed anchor: [{anchor}]({url})",
                "suggestion": "Check anchor link format"
            })

    return issues


def find_outdated_statistics(content):
    """Find statistics that might be outdated."""
    issues = []

    # Find statistics with years
    stat_patterns = [
        # "According to a 2020 study"
        (r'(?:according to|based on|from)\s+(?:a\s+)?(\d{4})\s+(?:study|report|survey|research)',
         "Citation with year"),
        # "In 2020, X% of..."
        (r'(?:in|during)\s+(\d{4}),?\s+\d+(?:\.\d+)?%',
         "Statistic from specific year"),
        # "As of 2020"
        (r'as of\s+(\d{4})',
         "Point-in-time reference"),
    ]

    current_year = get_current_year()

    for pattern, desc in stat_patterns:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            year = int(match.group(1))
            if year < current_year - 2:
                issues.append({
                    "type": "outdated_statistic",
                    "text": f"{desc} from {year}",
                    "match": match.group(0),
                    "suggestion": f"Update with more recent data (within 2 years)"
                })

    return issues


def check_update_indicators(content):
    """Check for update date indicators."""
    result = {
        "has_update_date": False,
        "update_date": None,
        "has_publish_date": False,
        "publish_date": None
    }

    # Look for "Updated:" or "Last updated:"
    update_match = re.search(r'(?:last\s+)?updated:?\s*([A-Za-z]+\s+\d{1,2},?\s+\d{4}|\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{4})',
                             content, re.IGNORECASE)
    if update_match:
        result["has_update_date"] = True
        result["update_date"] = update_match.group(1)

    # Look for "Published:"
    publish_match = re.search(r'published:?\s*([A-Za-z]+\s+\d{1,2},?\s+\d{4}|\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{4})',
                              content, re.IGNORECASE)
    if publish_match:
        result["has_publish_date"] = True
        result["publish_date"] = publish_match.group(1)

    return result


def calculate_freshness_score(year_refs, outdated_refs, statistics, update_info, current_year):
    """Calculate overall freshness score."""
    score = 100
    issues = []

    # Deduct for outdated years
    if year_refs["outdated"]:
        deduction = min(30, len(year_refs["outdated"]) * 10)
        score -= deduction
        issues.append(f"Outdated year references (-{deduction})")

    # Deduct for vague timeframes
    vague_count = sum(1 for r in outdated_refs if r["type"] == "vague_timeframe")
    if vague_count:
        deduction = min(15, vague_count * 5)
        score -= deduction
        issues.append(f"Vague time references (-{deduction})")

    # Deduct for outdated statistics
    if statistics:
        deduction = min(25, len(statistics) * 10)
        score -= deduction
        issues.append(f"Outdated statistics (-{deduction})")

    # Deduct if no update date
    if not update_info["has_update_date"]:
        score -= 10
        issues.append("No update date visible (-10)")

    # Bonus for recent update
    if update_info["update_date"]:
        try:
            # Try to extract year from date
            year_match = re.search(r'(\d{4})', update_info["update_date"])
            if year_match:
                update_year = int(year_match.group(1))
                if update_year == current_year:
                    score += 10
                    issues.append("Updated this year (+10)")
        except:
            pass

    return {
        "score": max(0, min(100, score)),
        "factors": issues
    }


def check_freshness(content, current_year=None):
    """Perform comprehensive freshness check."""
    if current_year is None:
        current_year = get_current_year()

    year_refs = find_year_references(content, current_year)
    outdated_refs = find_outdated_references(content, current_year)
    link_issues = find_broken_link_patterns(content)
    stat_issues = find_outdated_statistics(content)
    update_info = check_update_indicators(content)
    freshness = calculate_freshness_score(year_refs, outdated_refs, stat_issues, update_info, current_year)

    # Compile all issues
    all_issues = outdated_refs + link_issues + stat_issues

    # Generate recommendations
    recommendations = []

    if year_refs["outdated"]:
        recommendations.append({
            "priority": "high",
            "action": f"Update references to years: {', '.join(year_refs['outdated'])}",
            "reason": "Outdated year references harm credibility"
        })

    if stat_issues:
        recommendations.append({
            "priority": "high",
            "action": "Update statistics with recent data",
            "reason": f"Found {len(stat_issues)} potentially outdated statistics"
        })

    if not update_info["has_update_date"]:
        recommendations.append({
            "priority": "medium",
            "action": "Add visible 'Last updated' date",
            "reason": "Helps users and search engines assess freshness"
        })

    vague_refs = [r for r in outdated_refs if r["type"] == "vague_timeframe"]
    if vague_refs:
        recommendations.append({
            "priority": "medium",
            "action": "Replace vague time references with specific dates",
            "reason": "Improves clarity and longevity"
        })

    return {
        "freshness_score": freshness["score"],
        "score_factors": freshness["factors"],
        "current_year_check": current_year,
        "year_references": year_refs,
        "update_info": update_info,
        "issues_found": len(all_issues),
        "issues": all_issues,
        "recommendations": recommendations
    }


def main():
    parser = argparse.ArgumentParser(description="Check content freshness")
    parser.add_argument("file", help="Content file to check")
    parser.add_argument("--current-year", "-y", type=int, default=None,
                        help="Override current year")
    parser.add_argument("--format", "-f", choices=["json", "summary"], default="json",
                        help="Output format")

    args = parser.parse_args()

    try:
        with open(args.file, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(json.dumps({"error": f"File not found: {args.file}"}))
        sys.exit(1)

    result = check_freshness(content, args.current_year)

    if args.format == "summary":
        print("\n=== Content Freshness Check ===\n")
        print(f"Freshness Score: {result['freshness_score']}/100")
        print(f"\nScore factors:")
        for factor in result['score_factors']:
            print(f"  • {factor}")

        if result['year_references']['outdated']:
            print(f"\nOutdated years found: {', '.join(result['year_references']['outdated'])}")

        if result['issues']:
            print(f"\nIssues ({len(result['issues'])}):")
            for issue in result['issues'][:5]:
                print(f"  - {issue['text']}")

        if result['recommendations']:
            print(f"\nRecommendations:")
            for rec in result['recommendations']:
                print(f"  [{rec['priority'].upper()}] {rec['action']}")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
