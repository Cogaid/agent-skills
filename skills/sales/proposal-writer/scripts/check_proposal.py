#!/usr/bin/env python3
"""
Validate proposal before sending.

Usage:
    python check_proposal.py proposal.md
    python check_proposal.py proposal.md --strict

Output: JSON with validation results
"""

import argparse
import json
import re
import sys


REQUIRED_SECTIONS = [
    "executive summary",
    "situation",
    "outcome",
    "solution",
    "investment",
    "timeline",
    "next step"
]

OPTIONAL_SECTIONS = [
    "why us",
    "team",
    "case study",
    "terms"
]

PLACEHOLDER_PATTERNS = [
    r'\[Company\s*Name?\]',
    r'\[Name\]',
    r'\[Date\]',
    r'\[Amount\]',
    r'\[X\]',
    r'\[Y\]',
    r'\[TBD\]',
    r'\[TODO\]',
    r'\[\.\.\.\]',
    r'XXX',
    r'PLACEHOLDER'
]


def analyze_proposal(content):
    """Analyze proposal content for issues."""

    lines = content.split('\n')
    word_count = len(content.split())

    issues = []
    warnings = []

    # Check for required sections
    content_lower = content.lower()
    found_sections = []
    missing_sections = []

    for section in REQUIRED_SECTIONS:
        # Check for section header variations
        patterns = [
            f"# {section}",
            f"## {section}",
            f"### {section}",
            f"**{section}**"
        ]
        found = any(p in content_lower for p in patterns)

        if found:
            found_sections.append(section)
        else:
            missing_sections.append(section)

    if missing_sections:
        issues.append({
            "type": "missing_section",
            "message": f"Missing sections: {', '.join(missing_sections)}",
            "sections": missing_sections
        })

    # Check for placeholders
    placeholders_found = []
    for pattern in PLACEHOLDER_PATTERNS:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            placeholders_found.extend(matches)

    if placeholders_found:
        issues.append({
            "type": "placeholders",
            "message": f"Found {len(placeholders_found)} unfilled placeholders",
            "examples": list(set(placeholders_found))[:5]
        })

    # Check word count
    if word_count < 500:
        warnings.append({
            "type": "too_short",
            "message": f"Proposal seems short ({word_count} words). Aim for 1000-2500."
        })
    elif word_count > 3500:
        warnings.append({
            "type": "too_long",
            "message": f"Proposal is long ({word_count} words). Consider trimming to 1500-2500."
        })

    # Check for pricing
    has_pricing = bool(re.search(r'\$[\d,]+', content))
    if not has_pricing:
        warnings.append({
            "type": "no_pricing",
            "message": "No dollar amounts found. Is pricing missing?"
        })

    # Check for dates
    has_dates = bool(re.search(r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\w+\s+\d{1,2},?\s+\d{4}', content))
    if not has_dates:
        warnings.append({
            "type": "no_dates",
            "message": "No dates found. Consider adding specific timelines."
        })

    # Check for company name usage
    company_pattern = r'(?:company|customer|client|they|them|their)'
    company_matches = len(re.findall(company_pattern, content_lower))
    you_matches = len(re.findall(r'\byou\b|\byour\b', content_lower))

    if company_matches > you_matches:
        warnings.append({
            "type": "tone",
            "message": "Consider using more 'you/your' language (customer-centric)"
        })

    # Calculate readability (simple metric)
    sentences = len(re.split(r'[.!?]+', content))
    avg_sentence_length = word_count / sentences if sentences > 0 else 0

    if avg_sentence_length > 25:
        warnings.append({
            "type": "readability",
            "message": f"Average sentence length is {avg_sentence_length:.0f} words. Consider shorter sentences."
        })

    # Determine overall status
    if issues:
        status = "NEEDS_ATTENTION"
    elif warnings:
        status = "REVIEW_RECOMMENDED"
    else:
        status = "READY_TO_SEND"

    return {
        "status": status,
        "statistics": {
            "word_count": word_count,
            "line_count": len(lines),
            "sections_found": found_sections,
            "avg_sentence_length": round(avg_sentence_length, 1)
        },
        "issues": issues,
        "warnings": warnings,
        "sections": {
            "found": found_sections,
            "missing": missing_sections,
            "required": REQUIRED_SECTIONS
        }
    }


def main():
    parser = argparse.ArgumentParser(description="Validate proposal")
    parser.add_argument("file", help="Proposal file (markdown)")
    parser.add_argument("--strict", action="store_true",
                        help="Treat warnings as errors")

    args = parser.parse_args()

    try:
        with open(args.file, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(json.dumps({"error": f"File not found: {args.file}"}))
        sys.exit(1)

    result = analyze_proposal(content)

    if args.strict and result["warnings"]:
        result["status"] = "NEEDS_ATTENTION"
        result["issues"].extend(result["warnings"])

    print(json.dumps(result, indent=2))

    # Exit with error code if issues found
    if result["issues"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
