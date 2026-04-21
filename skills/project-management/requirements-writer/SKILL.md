---
name: requirements-writer
description: Write clear PRDs, user stories, and requirements documents with structured formats. Use when user mentions "PRD," "product requirements," "user stories," "acceptance criteria," "requirements document," "functional requirements," "MoSCoW."
metadata:
  version: 1.0.0
  category: project-management
---

# Requirements Writer

Write structured product requirements documents, user stories, and acceptance criteria using industry-standard formats.

## Purpose

Clear requirements are the foundation of successful software delivery. Ambiguous or incomplete requirements lead to rework, scope creep, and missed expectations. This skill provides templates for PRDs, user story formats, acceptance criteria patterns, prioritization frameworks, and review checklists to ensure requirements are complete, testable, and understood by all stakeholders.

## Quick Reference

### Requirements Hierarchy

| Level | Document | Audience | Detail Level | Example |
|-------|----------|----------|-------------|---------|
| Vision | Product brief | Executives, investors | High-level | "A platform for team collaboration" |
| Strategy | PRD | Product, engineering, design | Medium | Feature set, success metrics, constraints |
| Execution | User stories | Engineering, QA | Detailed | Specific behaviors and acceptance criteria |
| Verification | Test cases | QA, engineering | Very detailed | Step-by-step validation scripts |

### User Story Format

```
As a [type of user],
I want [goal or action],
So that [benefit or value].
```

**Examples:**

| Role | Want | So That |
|------|------|---------|
| As a new user | I want to sign up with my email | so that I can create an account quickly |
| As a team admin | I want to invite members by email | so that I can onboard my team |
| As a billing manager | I want to download invoices as PDF | so that I can submit them for reimbursement |

### Acceptance Criteria Format (Given-When-Then)

```
Given [precondition or context],
When [action or trigger],
Then [expected outcome].
```

**Example for "Sign up with email":**

```
Scenario 1: Successful registration
  Given I am on the registration page
  And I have not previously registered
  When I enter a valid email and password (8+ chars, 1 uppercase, 1 number)
  And I click "Create Account"
  Then my account is created
  And I receive a verification email within 2 minutes
  And I am redirected to the onboarding page

Scenario 2: Duplicate email
  Given I am on the registration page
  And an account with my email already exists
  When I enter the existing email and a password
  And I click "Create Account"
  Then I see an error: "An account with this email already exists"
  And no duplicate account is created

Scenario 3: Invalid password
  Given I am on the registration page
  When I enter a valid email and a password shorter than 8 characters
  And I click "Create Account"
  Then I see a validation error explaining the password requirements
  And the account is not created
```

### MoSCoW Prioritization

| Priority | Label | Definition | Rule of Thumb |
|----------|-------|------------|--------------|
| **M** | Must Have | Critical for launch; system is unusable without it | 60% of effort |
| **S** | Should Have | Important but not critical; painful to omit | 20% of effort |
| **C** | Could Have | Desirable if time permits; nice to have | 15% of effort |
| **W** | Won't Have (this time) | Agreed out of scope for this release | 5% (discovery only) |

## Workflow

### Requirements Writing Process

1. **Understand the problem**
   - Interview stakeholders
   - Review user feedback and analytics
   - Study the competitive landscape
   - Define the target persona

2. **Draft the PRD**
   - Use the template below
   - Start with the problem statement, not the solution
   - Define success metrics before detailing features

3. **Write user stories**
   - Break features into user stories using the format above
   - Each story should be independently deliverable (INVEST criteria)
   - Add acceptance criteria to every story

4. **Prioritize**
   - Apply MoSCoW classification with stakeholders
   - Validate priorities against project goals and constraints
   - Resolve conflicts through facilitated prioritization sessions

5. **Review and refine**
   - Use the review checklist (see below)
   - Walk through with engineering for feasibility
   - Walk through with QA for testability
   - Get stakeholder sign-off

### INVEST Criteria for User Stories

| Criterion | Question | Bad Example | Good Example |
|-----------|----------|-------------|-------------|
| **I**ndependent | Can it be built without other stories? | "Build the database schema" | "User can create an account" |
| **N**egotiable | Is there room for discussion on implementation? | "Use React table component v3.2.1" | "Display data in a sortable table" |
| **V**aluable | Does it deliver value to a user or stakeholder? | "Refactor the auth module" | "User can reset password via email" |
| **E**stimable | Can the team estimate the effort? | "Make the app better" | "Add search filters for name and date" |
| **S**mall | Can it be completed in one sprint? | "Build the entire payment system" | "User can add a credit card" |
| **T**estable | Can you write a test for it? | "App should be fast" | "Page loads in under 2 seconds on 3G" |

## Templates

### PRD Template

```markdown
# Product Requirements Document: [Feature/Product Name]

**Author:** [Name]
**Date:** [Date]
**Status:** [Draft / In Review / Approved]
**Version:** [1.0]
**Reviewers:** [Names]

---

## 1. Problem Statement

### What problem are we solving?
[Clear description of the user pain point or business need]

### Who has this problem?
[Target persona or user segment with demographics/behaviors]

### How do they solve it today?
[Current workarounds, competitor solutions, or manual processes]

### How do we know this is a real problem?
[Evidence: user research, support tickets, analytics data, market research]

## 2. Goals and Success Metrics

### Goals
- [Primary goal: what does success look like?]
- [Secondary goal]

### Success Metrics (KPIs)

| Metric | Current Value | Target Value | Measurement Method |
|--------|--------------|-------------|-------------------|
| [Metric 1, e.g., Sign-up conversion] | [X%] | [Y%] | [Analytics tool] |
| [Metric 2, e.g., Task completion time] | [X min] | [Y min] | [User testing] |
| [Metric 3, e.g., Support ticket volume] | [X/week] | [Y/week] | [Help desk data] |

### Non-Goals
- [Explicitly state what this feature will NOT do]
- [Things that are out of scope]

## 3. User Stories and Requirements

### Epic: [Epic Name]

#### Story 1: [Story Title]
**Priority:** Must Have

As a [user type],
I want [action],
So that [benefit].

**Acceptance Criteria:**

Given [context],
When [action],
Then [result].

Given [alternate context],
When [action],
Then [alternate result].

#### Story 2: [Story Title]
**Priority:** Should Have

As a [user type],
I want [action],
So that [benefit].

**Acceptance Criteria:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

## 4. Functional Requirements

| ID | Requirement | Priority | Notes |
|----|------------|----------|-------|
| FR-01 | System shall allow users to register with email and password | Must | OAuth as separate story |
| FR-02 | System shall send email verification within 2 minutes | Must | Use SendGrid |
| FR-03 | System shall support password reset via email link | Must | Link valid for 24 hours |
| FR-04 | System shall display password strength indicator | Should | Real-time feedback |
| FR-05 | System shall support SSO via Google and GitHub | Could | Phase 2 candidate |

## 5. Non-Functional Requirements

| Category | Requirement | Target | Measurement |
|----------|------------|--------|-------------|
| Performance | Page load time | < 2 seconds (P95) | Lighthouse, real user monitoring |
| Performance | API response time | < 200ms (P95) | APM tool |
| Scalability | Concurrent users | 10,000 | Load testing |
| Availability | Uptime | 99.9% | Monitoring |
| Security | Data encryption | AES-256 at rest, TLS 1.3 in transit | Security audit |
| Security | Authentication | bcrypt password hashing, CSRF protection | Penetration test |
| Accessibility | WCAG compliance | Level AA | Axe/Lighthouse audit |
| Compatibility | Browser support | Chrome, Firefox, Safari, Edge (last 2 versions) | Cross-browser testing |
| Localization | Language support | English (Phase 1), i18n-ready | Manual review |

## 6. Design and UX

### Wireframes / Mockups
[Link to Figma / design files]

### User Flow
[Description or link to user flow diagram]

### Edge Cases
- [What happens if the user loses connectivity mid-action?]
- [What happens if the email is already taken?]
- [What if the user has JavaScript disabled?]

## 7. Technical Considerations

### Architecture Notes
[Any known technical constraints or recommendations]

### Dependencies
- [External service or API dependency]
- [Internal team dependency]

### Migration / Backwards Compatibility
[Any data migration needs or backward compatibility requirements]

## 8. Release Plan

| Phase | Scope | Target Date | Dependencies |
|-------|-------|------------|-------------|
| Phase 1 (MVP) | Must Have stories only | [Date] | Design sign-off |
| Phase 2 | Should Have stories | [Date] | Phase 1 launch |
| Phase 3 | Could Have stories | [Date] | User feedback from Phase 1 |

## 9. Open Questions

| # | Question | Owner | Needed By | Answer |
|---|----------|-------|-----------|--------|
| 1 | [Open question] | [Name] | [Date] | [Pending / Answer] |
| 2 | [Open question] | [Name] | [Date] | [Pending / Answer] |

## 10. Appendix

### Glossary
- **[Term]:** [Definition]

### References
- [Link to user research]
- [Link to competitive analysis]
- [Link to related PRDs]
```

### Functional vs Non-Functional Requirements Guide

| Aspect | Functional | Non-Functional |
|--------|-----------|---------------|
| Answers | "What does the system do?" | "How well does the system do it?" |
| Format | "System shall [verb] [object]" | "[Quality attribute] shall be [measurable target]" |
| Testing | Feature tests, integration tests | Load tests, security scans, accessibility audits |
| Examples | Login, search, export, notify | Performance, security, scalability, usability |
| Ownership | Product Owner defines | Engineering + Product jointly define |
| Change frequency | Changes with every release | Relatively stable across releases |

## Scripts & Tools

### User Story Validator

```python
# scripts/story_validator.py
# Validates user stories against INVEST criteria
# Usage: python scripts/story_validator.py

import re

def validate_story(story: str) -> list[str]:
    """Check user story format and return issues."""
    issues = []
    if not re.search(r"[Aa]s an?\s+", story):
        issues.append("Missing 'As a [user]' clause")
    if not re.search(r"[Ii] want\s+", story):
        issues.append("Missing 'I want [goal]' clause")
    if not re.search(r"[Ss]o that\s+", story):
        issues.append("Missing 'So that [benefit]' clause")
    if len(story) > 500:
        issues.append("Story too long - consider splitting")
    if not issues:
        issues.append("Format OK")
    return issues

# Example
stories = [
    "As a user, I want to reset my password, so that I can regain access to my account.",
    "Build the login page",
    "As an admin, I want to manage users.",
]

for s in stories:
    result = validate_story(s)
    print(f"Story: {s[:60]}...")
    for r in result:
        print(f"  - {r}")
    print()
```

### Requirements Coverage Report

```bash
#!/bin/bash
# scripts/requirements-coverage.sh
# Count requirements by priority in a PRD markdown file
# Usage: ./scripts/requirements-coverage.sh prd.md

FILE="${1:-prd.md}"
echo "=== Requirements Coverage Report ==="
echo "File: $FILE"
echo ""
echo "Must Have:   $(grep -ci 'must have\|must' "$FILE" 2>/dev/null || echo 0)"
echo "Should Have: $(grep -ci 'should have\|should' "$FILE" 2>/dev/null || echo 0)"
echo "Could Have:  $(grep -ci 'could have\|could' "$FILE" 2>/dev/null || echo 0)"
echo "Won't Have:  $(grep -ci "won't have\|wont have" "$FILE" 2>/dev/null || echo 0)"
echo ""
echo "Total stories: $(grep -c 'As a\|As an' "$FILE" 2>/dev/null || echo 0)"
echo "Acceptance criteria: $(grep -c 'Given\|Scenario' "$FILE" 2>/dev/null || echo 0)"
```

## Best Practices

### Requirements Review Checklist

| # | Check | Question |
|---|-------|----------|
| 1 | Complete | Are all user scenarios covered, including error cases? |
| 2 | Unambiguous | Could two developers interpret this differently? |
| 3 | Testable | Can QA write a test case from this requirement? |
| 4 | Prioritized | Does every requirement have a MoSCoW priority? |
| 5 | Feasible | Has engineering confirmed this is technically achievable? |
| 6 | Traceable | Can each requirement be traced to a user need or business goal? |
| 7 | Consistent | Do any requirements contradict each other? |
| 8 | Independent | Can stories be built and deployed independently? |
| 9 | Measurable | Are success metrics defined with specific targets? |
| 10 | Bounded | Are non-goals and out-of-scope items explicitly stated? |

### Common Writing Mistakes

| Mistake | Example | Fix |
|---------|---------|-----|
| Vague language | "System should be fast" | "Page loads in < 2s at P95 on 4G" |
| Implementation detail | "Use Redis for caching" | "Frequently accessed data loads in < 100ms" |
| Missing persona | "User can export data" | "As an analyst, I want to export data as CSV" |
| No acceptance criteria | Story with no AC | Add Given-When-Then for every scenario |
| Compound stories | "User can create, edit, and delete projects" | Split into 3 separate stories |
| Missing edge cases | Only happy path described | Add error, empty state, and boundary scenarios |
| Unmeasurable NFRs | "System must be secure" | "All endpoints require authentication; PII encrypted at rest" |
| Gold plating | Over-specifying UI details | Focus on what, not how; leave design flexibility |
