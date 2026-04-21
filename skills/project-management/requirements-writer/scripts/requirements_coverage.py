#!/usr/bin/env python3
"""Requirements coverage analyzer.

Parses PRD/requirements markdown files and reports on coverage metrics:
priority distribution, acceptance criteria presence, story completeness,
and traceability gaps.

Usage:
    python requirements_coverage.py --demo
    python requirements_coverage.py --file prd.md
    python requirements_coverage.py --demo --json
"""

import argparse
import json
import re
import sys


def analyze_requirements(content):
    """Analyze a requirements document for coverage metrics."""
    lines = content.split("\n")

    # Count stories
    story_pattern = re.compile(r"[Aa]s an?\s+")
    stories = [line.strip() for line in lines if story_pattern.search(line)]

    # Count acceptance criteria
    gwt_count = len(re.findall(r"(?i)\b(?:given|scenario)\b", content))
    checklist_count = len(re.findall(r"- \[[ x]\]", content))

    # Count by priority
    priorities = {
        "Must Have": len(re.findall(r"(?i)must\s*have", content)),
        "Should Have": len(re.findall(r"(?i)should\s*have", content)),
        "Could Have": len(re.findall(r"(?i)could\s*have", content)),
        "Won't Have": len(re.findall(r"(?i)won'?t\s*have", content)),
    }

    # Count functional requirements (FR-XX pattern)
    fr_pattern = re.compile(r"FR-\d+")
    functional_reqs = len(set(fr_pattern.findall(content)))

    # Count NFRs (common NFR keywords)
    nfr_keywords = ["performance", "security", "scalability", "availability",
                    "accessibility", "compatibility", "reliability"]
    nfr_mentions = sum(1 for kw in nfr_keywords if kw in content.lower())

    # Check for open questions
    open_questions = len(re.findall(r"(?i)\bpending\b|\bTBD\b|\bTBC\b|\?\s*$", content))

    # Check for design references
    has_wireframes = bool(re.search(r"(?i)figma|wireframe|mockup|design\s*file", content))
    has_user_flow = bool(re.search(r"(?i)user\s*flow|journey|diagram", content))

    # Completeness score
    score = 0
    max_score = 100
    if stories:
        score += 20
    if gwt_count > 0 or checklist_count > 0:
        score += 20
    if sum(priorities.values()) > 0:
        score += 15
    if functional_reqs > 0:
        score += 15
    if nfr_mentions >= 3:
        score += 10
    if has_wireframes:
        score += 10
    if has_user_flow:
        score += 5
    if open_questions == 0:
        score += 5

    return {
        "stories": {
            "count": len(stories),
            "examples": stories[:3],
        },
        "acceptance_criteria": {
            "given_when_then_scenarios": gwt_count,
            "checklist_items": checklist_count,
            "total": gwt_count + checklist_count,
        },
        "priorities": priorities,
        "functional_requirements": functional_reqs,
        "nfr_coverage": {
            "keywords_found": nfr_mentions,
            "total_checked": len(nfr_keywords),
        },
        "completeness": {
            "score": score,
            "max_score": max_score,
            "grade": "A" if score >= 85 else "B" if score >= 70 else "C" if score >= 55 else "D" if score >= 40 else "F",
            "has_wireframes": has_wireframes,
            "has_user_flow": has_user_flow,
            "open_questions": open_questions,
        },
    }


DEMO_CONTENT = """
# Product Requirements Document: User Authentication

**Status:** In Review
**Priority:** Must Have

## Problem Statement

As a new user, I want to sign up with my email, so that I can create an account quickly.

As a returning user, I want to log in with my credentials, so that I can access my data.

As a user who forgot their password, I want to reset it via email, so that I can regain access.

## Functional Requirements

| ID | Requirement | Priority |
|----|------------|----------|
| FR-01 | System shall allow registration with email and password | Must Have |
| FR-02 | System shall send verification email within 2 minutes | Must Have |
| FR-03 | System shall support password reset via email link | Must Have |
| FR-04 | System shall display password strength indicator | Should Have |
| FR-05 | System shall support SSO via Google and GitHub | Could Have |
| FR-06 | System shall log all authentication attempts | Must Have |

## User Stories

### Story 1: Email Registration
**Priority:** Must Have

As a new customer, I want to register with my email and password, so that I can create an account.

**Acceptance Criteria:**

Scenario 1: Successful registration
  Given I am on the registration page
  And I have not previously registered
  When I enter a valid email and password
  Then my account is created
  And I receive a verification email

Scenario 2: Duplicate email
  Given an account with my email already exists
  When I try to register with the same email
  Then I see an error message

Scenario 3: Invalid password
  Given I am on the registration page
  When I enter a password shorter than 8 characters
  Then I see a validation error

### Story 2: Password Reset
**Priority:** Must Have

As a user who forgot my password, I want to reset it via email, so that I can regain access to my account.

**Acceptance Criteria:**
- [ ] User can request password reset by entering email
- [ ] Reset link is sent within 2 minutes
- [ ] Reset link expires after 24 hours
- [ ] User can set a new password using the link
- [ ] Old password no longer works after reset

### Story 3: SSO Login
**Priority:** Could Have

As a user, I want to log in with Google or GitHub, so that I do not need to remember another password.

## Non-Functional Requirements

| Category | Requirement | Target |
|----------|------------|--------|
| Performance | Login response time | < 500ms at P95 |
| Security | Password hashing | bcrypt with cost factor 12 |
| Availability | Auth service uptime | 99.9% |
| Scalability | Concurrent logins | 5000 |
| Accessibility | WCAG compliance | Level AA |

## Design

Wireframes available in Figma: [link]
User flow diagram: [link]

## Open Questions

| # | Question | Status |
|---|----------|--------|
| 1 | Should we support passwordless login? | Pending |
"""


def main():
    parser = argparse.ArgumentParser(
        description="Analyze requirements document coverage and completeness",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze demo PRD
  %(prog)s --demo

  # Analyze a file
  %(prog)s --file path/to/prd.md

  # JSON output
  %(prog)s --demo --json
        """,
    )
    parser.add_argument("--file", type=str, help="Path to requirements/PRD markdown file")
    parser.add_argument("--demo", action="store_true", help="Analyze sample PRD")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.demo:
        content = DEMO_CONTENT
    elif args.file:
        try:
            with open(args.file) as f:
                content = f.read()
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found", file=sys.stderr)
            sys.exit(1)
    else:
        print("Provide --file or --demo.")
        sys.exit(1)

    result = analyze_requirements(content)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("=" * 60)
        print("REQUIREMENTS COVERAGE REPORT")
        print("=" * 60)
        print()

        c = result["completeness"]
        print(f"Completeness Score: {c['score']}/{c['max_score']} (Grade: {c['grade']})")
        print()

        print("USER STORIES")
        print(f"  Count: {result['stories']['count']}")
        print()

        print("ACCEPTANCE CRITERIA")
        ac = result["acceptance_criteria"]
        print(f"  Given-When-Then scenarios: {ac['given_when_then_scenarios']}")
        print(f"  Checklist items: {ac['checklist_items']}")
        print(f"  Total criteria: {ac['total']}")
        print()

        print("PRIORITY DISTRIBUTION")
        for priority, count in result["priorities"].items():
            bar = "#" * count + "." * (10 - min(count, 10))
            print(f"  {priority:<12} [{bar}] {count}")
        print()

        print("FUNCTIONAL REQUIREMENTS")
        print(f"  Identified: {result['functional_requirements']}")
        print()

        print("NON-FUNCTIONAL COVERAGE")
        nfr = result["nfr_coverage"]
        print(f"  Categories covered: {nfr['keywords_found']}/{nfr['total_checked']}")
        print()

        print("DOCUMENT COMPLETENESS")
        print(f"  Has wireframes/design: {'Yes' if c['has_wireframes'] else 'No'}")
        print(f"  Has user flow: {'Yes' if c['has_user_flow'] else 'No'}")
        print(f"  Open questions: {c['open_questions']}")
        print()


if __name__ == "__main__":
    main()
