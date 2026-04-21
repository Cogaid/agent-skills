#!/usr/bin/env python3
"""User story validator against INVEST criteria and format standards.

Validates user stories for proper format, completeness, and quality.
Checks for As-a/I-want/So-that format, acceptance criteria presence,
story size indicators, and common writing mistakes.

Usage:
    python story_validator.py --demo
    python story_validator.py --story "As a user, I want to login, so that I can access my account."
    python story_validator.py --file stories.txt
    python story_validator.py --demo --json
"""

import argparse
import json
import re
import sys


def validate_format(story_text):
    """Check user story format compliance."""
    issues = []
    warnings = []

    # Check for As a [user] clause
    if not re.search(r"[Aa]s an?\s+\w+", story_text):
        issues.append("Missing 'As a [user type]' clause")
    else:
        # Check if role is specific enough
        role_match = re.search(r"[Aa]s an?\s+(\w+)", story_text)
        if role_match:
            role = role_match.group(1).lower()
            if role in ("user", "person", "someone"):
                warnings.append(f"Role '{role}' is too generic - specify the user type (e.g., 'admin', 'new customer')")

    # Check for I want clause
    if not re.search(r"[Ii] want\s+", story_text):
        issues.append("Missing 'I want [goal]' clause")
    else:
        # Check for implementation detail
        impl_keywords = ["use react", "call the api", "database", "endpoint", "sql", "redis"]
        for kw in impl_keywords:
            if kw in story_text.lower():
                warnings.append(f"Possible implementation detail detected: '{kw}' - stories should describe WHAT, not HOW")

    # Check for So that clause
    if not re.search(r"[Ss]o that\s+", story_text):
        issues.append("Missing 'So that [benefit]' clause - every story needs a clear reason/value")

    # Check length
    if len(story_text) > 500:
        warnings.append("Story text is very long (>500 chars) - consider splitting into multiple stories")
    elif len(story_text) < 30:
        warnings.append("Story text is very short (<30 chars) - may lack sufficient detail")

    # Check for compound stories (multiple actions)
    compound_indicators = [" and ", " also ", " additionally "]
    want_section = re.search(r"[Ii] want\s+(.*?)(?:[Ss]o that|$)", story_text, re.DOTALL)
    if want_section:
        want_text = want_section.group(1)
        for indicator in compound_indicators:
            if indicator in want_text.lower():
                warnings.append(f"Possible compound story ('{indicator.strip()}' in 'I want' clause) - consider splitting")
                break

    return issues, warnings


def validate_acceptance_criteria(criteria_text):
    """Validate acceptance criteria format and completeness."""
    issues = []
    warnings = []

    if not criteria_text or criteria_text.strip() == "":
        issues.append("No acceptance criteria provided")
        return issues, warnings

    # Check for Given-When-Then or checklist format
    has_gwt = bool(re.search(r"[Gg]iven\s+", criteria_text))
    has_checklist = bool(re.search(r"- \[[ x]\]", criteria_text))
    has_bullets = bool(re.search(r"^- \w", criteria_text, re.MULTILINE))

    if not has_gwt and not has_checklist and not has_bullets:
        warnings.append("Acceptance criteria not in recognized format (Given-When-Then or checklist)")

    if has_gwt:
        given_count = len(re.findall(r"[Gg]iven\s+", criteria_text))
        when_count = len(re.findall(r"[Ww]hen\s+", criteria_text))
        then_count = len(re.findall(r"[Tt]hen\s+", criteria_text))

        if when_count == 0:
            issues.append("Given-When-Then format incomplete: missing 'When' clause")
        if then_count == 0:
            issues.append("Given-When-Then format incomplete: missing 'Then' clause")

        if given_count == 1:
            warnings.append("Only 1 scenario - consider adding error/edge case scenarios")

    # Check for vague language
    vague_terms = ["should work", "as expected", "properly", "correctly", "appropriate", "reasonable"]
    for term in vague_terms:
        if term in criteria_text.lower():
            warnings.append(f"Vague language detected: '{term}' - use specific, measurable criteria")

    return issues, warnings


def validate_story(story_text, criteria_text=None):
    """Full story validation combining format and criteria checks."""
    format_issues, format_warnings = validate_format(story_text)

    criteria_issues = []
    criteria_warnings = []
    if criteria_text:
        criteria_issues, criteria_warnings = validate_acceptance_criteria(criteria_text)

    all_issues = format_issues + criteria_issues
    all_warnings = format_warnings + criteria_warnings

    if not all_issues:
        grade = "PASS" if not all_warnings else "PASS (with warnings)"
    elif len(all_issues) <= 1:
        grade = "NEEDS WORK"
    else:
        grade = "FAIL"

    return {
        "story": story_text[:100] + ("..." if len(story_text) > 100 else ""),
        "grade": grade,
        "issues": all_issues,
        "warnings": all_warnings,
        "issue_count": len(all_issues),
        "warning_count": len(all_warnings),
    }


DEMO_STORIES = [
    {
        "story": "As a new customer, I want to sign up with my email address, so that I can create an account and start using the product.",
        "criteria": """Given I am on the registration page
And I have not previously registered
When I enter a valid email and password (8+ chars, 1 uppercase, 1 number)
And I click "Create Account"
Then my account is created
And I receive a verification email within 2 minutes

Given I am on the registration page
And an account with my email already exists
When I enter the existing email
Then I see an error: "An account with this email already exists"
""",
    },
    {
        "story": "Build the login page with React and use the OAuth endpoint",
        "criteria": "",
    },
    {
        "story": "As a user, I want to do stuff.",
        "criteria": "- It should work properly",
    },
    {
        "story": "As an admin, I want to manage users and also configure settings and additionally set up integrations, so that the system is properly configured.",
        "criteria": """- [ ] Admin can view user list
- [ ] Admin can create users
- [ ] Admin can delete users""",
    },
    {
        "story": "As a billing manager, I want to download invoices as PDF, so that I can submit them for reimbursement.",
        "criteria": """Given I am on the billing page
And I have at least one invoice
When I click the download button for an invoice
Then a PDF file is downloaded
And the PDF contains the invoice details including date, amount, and line items

Given I am on the billing page
And I have no invoices
When I view the billing page
Then I see a message "No invoices yet"
And the download button is not displayed""",
    },
]


def main():
    parser = argparse.ArgumentParser(
        description="Validate user stories against INVEST criteria and format standards",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Validate demo stories
  %(prog)s --demo

  # Validate a single story
  %(prog)s --story "As a user, I want to login, so that I can access my account."

  # JSON output
  %(prog)s --demo --json
        """,
    )
    parser.add_argument("--story", type=str, help="Single story to validate")
    parser.add_argument("--criteria", type=str, help="Acceptance criteria for the story")
    parser.add_argument("--file", type=str, help="File with stories (one per line)")
    parser.add_argument("--demo", action="store_true", help="Validate sample stories")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    results = []

    if args.demo:
        for entry in DEMO_STORIES:
            result = validate_story(entry["story"], entry.get("criteria"))
            results.append(result)
    elif args.story:
        result = validate_story(args.story, args.criteria)
        results.append(result)
    elif args.file:
        try:
            with open(args.file) as f:
                for line in f:
                    line = line.strip()
                    if line:
                        result = validate_story(line)
                        results.append(result)
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found", file=sys.stderr)
            sys.exit(1)
    else:
        print("Provide --story, --file, or --demo.")
        sys.exit(1)

    if args.json:
        summary = {
            "total": len(results),
            "pass": sum(1 for r in results if "PASS" in r["grade"]),
            "fail": sum(1 for r in results if r["grade"] == "FAIL"),
            "needs_work": sum(1 for r in results if r["grade"] == "NEEDS WORK"),
        }
        print(json.dumps({"summary": summary, "results": results}, indent=2))
    else:
        print("=" * 70)
        print("USER STORY VALIDATION REPORT")
        print("=" * 70)
        print()

        for i, r in enumerate(results, 1):
            icon = {"PASS": "[OK]", "PASS (with warnings)": "[OK]", "NEEDS WORK": "[!!]", "FAIL": "[XX]"}
            print(f"Story {i}: {r['story']}")
            print(f"  Grade: {icon.get(r['grade'], '[??]')} {r['grade']}")
            for issue in r["issues"]:
                print(f"  ERROR:   {issue}")
            for warning in r["warnings"]:
                print(f"  WARNING: {warning}")
            print()

        # Summary
        pass_count = sum(1 for r in results if "PASS" in r["grade"])
        print("-" * 70)
        print(f"Results: {pass_count}/{len(results)} stories pass validation")


if __name__ == "__main__":
    main()
