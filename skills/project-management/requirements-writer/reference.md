# Requirements Writer Reference

Comprehensive reference for writing clear requirements documents, user stories, acceptance criteria, and prioritization frameworks.

## User Story Frameworks

### INVEST Criteria Deep Dive

Every user story should satisfy the INVEST criteria. Use this as a quality gate before bringing stories into sprint planning.

| Criterion | Question to Ask | Red Flags | Fix |
|-----------|----------------|-----------|-----|
| **I**ndependent | Can this story be built and deployed without waiting for other stories? | "We need US-101 done first" | Re-scope to include minimal needed functionality or rewrite as a vertical slice |
| **N**egotiable | Is there room for the team to discuss HOW to implement? | Specific library versions, pixel-perfect specs in the story | Move implementation details to technical notes; keep story at behavior level |
| **V**aluable | Does completing this story deliver value someone cares about? | Pure infrastructure work with no user benefit | Reframe: "so that [end-user benefit]" or make it a technical task, not a story |
| **E**stimable | Can the team give a reasonable effort estimate? | "We have no idea how long this will take" | Spike first to reduce unknowns; split into known and unknown parts |
| **S**mall | Can it be completed within one sprint? | Story estimated at 13+ points | Split using story splitting techniques |
| **T**estable | Can QA write a test that proves this story works? | "The app should feel fast" | Add specific, measurable criteria: "loads in < 2s on 4G connection" |

### Acceptance Criteria Patterns

#### Given-When-Then (Gherkin)

Best for: behavior-driven scenarios, complex business rules, automated testing.

```
Given [precondition / initial state]
  And [additional context]
When [action / event / trigger]
  And [additional action]
Then [expected outcome]
  And [additional outcome]
  But [exception or negative outcome]
```

**Tips:**
- One scenario per behavior (do not combine happy path and error in one scenario)
- Keep scenarios independent (no ordering dependency)
- Use concrete examples, not abstract descriptions
- Aim for 3-7 scenarios per story (if more, the story may be too large)

#### Checklist Format

Best for: simple stories, non-behavioral requirements, quick documentation.

```
Acceptance Criteria:
- [ ] [Specific, verifiable criterion]
- [ ] [Edge case handled]
- [ ] [Error state handled]
- [ ] [Performance requirement met]
- [ ] [Accessibility requirement met]
```

#### Rule-Based Format

Best for: stories with complex business rules or calculations.

```
Rules:
- IF [condition] THEN [outcome]
- IF [condition] AND [condition] THEN [different outcome]
- [Constraint]: [measurable limit]
- [Default]: [behavior when no explicit input]
```

### User Story Mapping

User Story Mapping organizes stories along two axes:

- **Horizontal (backbone):** The user's journey steps in sequence
- **Vertical (body):** Depth of functionality for each step (MVP at top, enhancements below)

```
User Journey Steps (left to right):
  Register -> Browse -> Search -> Add to Cart -> Checkout -> Track Order

For each step, depth (top to bottom):
  MVP (must have)
  Enhancement 1 (should have)
  Enhancement 2 (could have)
  Future (won't have this release)
```

**Benefits:**
- Visualizes the whole product at a glance
- Makes release planning intuitive (draw a horizontal line for release scope)
- Reveals gaps in the user journey
- Helps prioritize by seeing what is needed for a complete thin slice

## Prioritization Frameworks

### MoSCoW Deep Dive

| Priority | Rule | Stakeholder Agreement | If Removed... |
|----------|------|----------------------|---------------|
| **Must** | Non-negotiable for this release | All stakeholders agree it is essential | Product is unusable or unshippable |
| **Should** | Important, expect to include | Most stakeholders agree it should be there | Product works but is painful or limited |
| **Could** | Desirable, include if time allows | Nice to have, stakeholders not upset if deferred | No significant impact on product value |
| **Won't** | Explicitly out of scope this time | All stakeholders agree to defer | N/A (already excluded) |

**Effort allocation rule of thumb:**
- Must: 60% of available effort
- Should: 20% of available effort
- Could: 15% of available effort
- Won't: 5% (discovery/documentation only)

### RICE Scoring

For when you need a quantitative approach to prioritization:

```
RICE Score = (Reach x Impact x Confidence) / Effort

Where:
  Reach      = Number of users affected per quarter (estimate)
  Impact     = Scale: 3 (massive), 2 (high), 1 (medium), 0.5 (low), 0.25 (minimal)
  Confidence = Percentage (100% = high confidence, 50% = low)
  Effort     = Person-months of work
```

**Example:**
| Feature | Reach | Impact | Confidence | Effort | RICE Score |
|---------|-------|--------|-----------|--------|------------|
| Search filters | 5000 | 2 | 80% | 2 | 4000 |
| Dark mode | 3000 | 1 | 90% | 1.5 | 1800 |
| Admin audit log | 200 | 2 | 100% | 3 | 133 |

### Kano Model

Categorizes features by their effect on customer satisfaction:

| Category | Definition | Strategy |
|----------|-----------|----------|
| **Basic** (Must-be) | Expected by users; absence causes dissatisfaction | Always include; do not over-invest |
| **Performance** (Linear) | More is better; satisfaction scales linearly | Invest proportionally to value |
| **Excitement** (Delighters) | Unexpected; presence creates delight | Include 1-2 per release for wow factor |
| **Indifferent** | Users do not care either way | Deprioritize; save effort |
| **Reverse** | Some users actively dislike it | Validate before building |

## Requirements Traceability

### Traceability Matrix

Link requirements to their source, implementation, and verification:

| Req ID | Source | User Story | Design | Code Module | Test Case | Status |
|--------|--------|-----------|--------|-------------|-----------|--------|
| FR-01 | User interview #3 | US-101 | Figma wireframe A | auth/register.ts | TC-001, TC-002 | Verified |
| FR-02 | Support ticket #456 | US-102 | Figma wireframe B | auth/password.ts | TC-003 | In Dev |

**Why traceability matters:**
- Impact analysis: when a requirement changes, quickly find affected code and tests
- Coverage verification: ensure every requirement has corresponding tests
- Audit compliance: prove that every requirement was implemented and verified

## Non-Functional Requirements Guide

### Performance Requirements

| Metric | How to Specify | Bad Example | Good Example |
|--------|---------------|-------------|-------------|
| Response time | Percentile at specific load | "Should be fast" | "API responds in < 200ms at P95 under 1000 concurrent users" |
| Throughput | Operations per time unit | "Should handle lots of users" | "System processes 500 transactions per second" |
| Page load | Time to interactive at connection speed | "Pages load quickly" | "Time to Interactive < 3s on 4G connection" |
| Startup time | Cold start vs warm | "App starts fast" | "Cold start < 5s; warm start < 1s" |

### Security Requirements

| Area | How to Specify | Example |
|------|---------------|---------|
| Authentication | Method + strength | "Passwords hashed with bcrypt, min 12 chars, MFA supported" |
| Authorization | Model + granularity | "RBAC with Admin, Editor, Viewer roles; row-level access control" |
| Data protection | At rest + in transit | "AES-256 encryption at rest; TLS 1.3 in transit; PII masked in logs" |
| Compliance | Standard + scope | "SOC 2 Type II compliant; GDPR data subject rights supported" |

## References

- Mike Cohn, "User Stories Applied" (2004)
- Jeff Patton, "User Story Mapping" (2014)
- Karl Wiegers & Joy Beatty, "Software Requirements" (3rd Edition, 2013)
- BDD/Gherkin: https://cucumber.io/docs/gherkin/
- INVEST Criteria: Bill Wake, https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/
