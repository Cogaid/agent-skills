---
name: sow-writer
description: Write clear statements of work for service engagements with scope, deliverables, and timelines. Use when the user mentions "statement of work," "SOW," "scope of work," "project scope," "deliverables," "work order," "service agreement," "engagement letter," "project proposal," "milestones," "acceptance criteria," or "change order."
metadata:
  version: 1.0.0
  category: finance-operations
---

# SOW Writer

Write structured statements of work that clearly define scope, deliverables, timelines, and payment terms for service engagements.

## Purpose

This skill helps you draft SOWs that protect both parties by clearly defining what will be delivered, when, how it will be accepted, and what happens when scope changes. A well-written SOW prevents scope creep, payment disputes, and misaligned expectations.

## Quick Start

1. **Confirm the engagement type**: Fixed-price, time & materials, or retainer
2. **Define scope boundaries**: What is included and what is explicitly excluded
3. **List deliverables**: Tangible outputs with acceptance criteria
4. **Build the timeline**: Milestones with dates and dependencies
5. **Set payment schedule**: Tied to milestones or time periods
6. **Document assumptions**: What must be true for the plan to work
7. **Include change order process**: How scope changes are handled

## SOW Structure Template

```
STATEMENT OF WORK

SOW #:            [SOW-YYYY-NNNN]
Reference MSA:    [MSA Date / Reference #]
Client:           [Client Company Name]
Provider:         [Your Company Name]
Effective Date:   [Date]
SOW Expiration:   [Date]
Prepared by:      [Name, Title]

═══════════════════════════════════════════════════════════

1. OVERVIEW & OBJECTIVES
────────────────────────────────────────────────────────
   [2-3 paragraph description of the engagement, business context,
   and what success looks like. This section sets the stage but does
   NOT define scope -- that comes next.]

   Project Objectives:
   a. [Objective 1 -- measurable outcome]
   b. [Objective 2 -- measurable outcome]
   c. [Objective 3 -- measurable outcome]

2. SCOPE OF SERVICES
────────────────────────────────────────────────────────
   2.1 In Scope:
       • [Service/activity 1]
       • [Service/activity 2]
       • [Service/activity 3]
       • [Service/activity 4]

   2.2 Out of Scope:
       • [Excluded item 1]
       • [Excluded item 2]
       • [Excluded item 3]

       Note: Any work not explicitly listed in Section 2.1 is out
       of scope and requires a Change Order (see Section 8).

3. DELIVERABLES
────────────────────────────────────────────────────────
   [See Deliverables Table below]

4. TIMELINE & MILESTONES
────────────────────────────────────────────────────────
   [See Timeline Section below]

5. ACCEPTANCE CRITERIA & PROCESS
────────────────────────────────────────────────────────
   [See Acceptance Section below]

6. PAYMENT SCHEDULE
────────────────────────────────────────────────────────
   [See Payment Section below]

7. ASSUMPTIONS & DEPENDENCIES
────────────────────────────────────────────────────────
   [See Assumptions Section below]

8. CHANGE ORDER PROCESS
────────────────────────────────────────────────────────
   [See Change Order Section below]

9. ROLES & RESPONSIBILITIES
────────────────────────────────────────────────────────
   Provider Responsibilities:
   • [Responsibility 1]
   • [Responsibility 2]

   Client Responsibilities:
   • [Responsibility 1 -- e.g., timely feedback]
   • [Responsibility 2 -- e.g., access to systems]
   • [Responsibility 3 -- e.g., designated point of contact]

10. GOVERNANCE & COMMUNICATION
────────────────────────────────────────────────────────
    Status Reports:     [Weekly / Bi-weekly]
    Status Meetings:    [Day, Time, Duration]
    Escalation Path:    [Name/Role] → [Name/Role] → [Name/Role]
    Tools:              [Slack, Jira, Email, etc.]

SIGNATURES
────────────────────────────────────────────────────────
Provider: ________________  Date: ________  Title: ____________
Client:   ________________  Date: ________  Title: ____________
```

## Scope Definition Framework

Use the MoSCoW method to prioritize scope items:

| Priority | Label | Meaning | Treatment in SOW |
|----------|-------|---------|-----------------|
| **Must Have** | M | Critical to project success | In scope, included in price |
| **Should Have** | S | Important but not critical | In scope, may be deferred if timeline slips |
| **Could Have** | C | Desirable enhancement | In scope only if time/budget allows |
| **Won't Have** | W | Explicitly excluded this phase | Listed in Out of Scope |

```
SCOPE MATRIX
───────────────────────────────────────────
Feature / Activity            MoSCoW    Phase    Est. Hours
────────────────────────────  ──────    ─────    ──────────
User authentication           Must       1         40
Dashboard design              Must       1         60
API integration               Must       2         80
Reporting module              Should     2         50
Mobile responsive             Should     1         30
Advanced analytics            Could      3         40
Multi-language support        Won't      --        --
Legacy system migration       Won't      --        --
```

## Deliverables Table Format

| # | Deliverable | Description | Format | Milestone | Due Date |
|---|-------------|-------------|--------|-----------|----------|
| D1 | Project Plan | Detailed project plan with WBS | PDF + MPP | M1 | Week 1 |
| D2 | Design Mockups | UI/UX wireframes and visual designs | Figma link | M2 | Week 3 |
| D3 | Technical Spec | Architecture and data model documentation | PDF | M2 | Week 4 |
| D4 | Working Prototype | Functional prototype with core features | Staging URL | M3 | Week 8 |
| D5 | Test Results | QA test plan execution and results report | PDF | M4 | Week 10 |
| D6 | Final Deliverable | Production-ready application | Production URL + source | M5 | Week 12 |
| D7 | Documentation | Admin guide, user guide, API docs | PDF + Wiki | M5 | Week 12 |
| D8 | Training | 2x training sessions (recorded) | Video + slides | M5 | Week 13 |

## Timeline & Milestone Section

```
PROJECT TIMELINE
══════════════════════════════════════════════════════════

Phase 1: Discovery & Planning (Weeks 1-2)
──────────────────────────────────────────
  M1: Project Kickoff & Plan Approved        Week 1
  • Stakeholder interviews
  • Requirements documentation
  • Project plan finalization

Phase 2: Design (Weeks 3-5)
──────────────────────────────────────────
  M2: Design Approved                        Week 5
  • Wireframes and user flows
  • Visual design mockups
  • Technical architecture document
  • Client review and approval (5 business days)

Phase 3: Development (Weeks 6-9)
──────────────────────────────────────────
  M3: Development Complete                   Week 9
  • Sprint 1: Core functionality (Weeks 6-7)
  • Sprint 2: Integration & features (Weeks 8-9)
  • Internal QA throughout

Phase 4: Testing & Launch (Weeks 10-12)
──────────────────────────────────────────
  M4: UAT Complete                           Week 11
  M5: Go-Live                                Week 12
  • User acceptance testing
  • Bug fixes and refinements
  • Production deployment
  • Post-launch monitoring (1 week)

TOTAL DURATION: 12 weeks
BUFFER: 1 week built into Phase 3-4

DEPENDENCIES:
  • Client feedback on M2 deliverables within 5 business days
  • API credentials and system access by Week 5
  • Content and assets provided by Week 4
```

## Acceptance Criteria

```
ACCEPTANCE PROCESS
══════════════════════════════════════════════════════════

1. Provider submits deliverable with completion notice
2. Client has [5-10] business days to review
3. Client responds with one of:
   a. ACCEPTED -- deliverable approved as-is
   b. ACCEPTED WITH COMMENTS -- minor items noted, deliverable approved
   c. REJECTED WITH SPECIFICS -- specific deficiencies listed per acceptance criteria

4. If rejected, Provider has [5-10] business days to remedy
5. Re-submission triggers a new review period
6. Maximum [2] rounds of revision per deliverable
7. If not accepted after [2] rounds, escalation per Section 10

DEEMED ACCEPTANCE:
If Client does not respond within the review period, the deliverable
is deemed accepted.

ACCEPTANCE CRITERIA PER DELIVERABLE:

D1 - Project Plan:
  □ Includes WBS with task-level detail
  □ Resource assignments identified
  □ Dependencies and critical path shown
  □ Risk register included

D4 - Working Prototype:
  □ All Must Have features functional
  □ No critical or high-severity bugs
  □ Performance: page load < 3 seconds
  □ Browser support: Chrome, Firefox, Safari, Edge (latest 2 versions)
  □ Accessibility: WCAG 2.1 AA compliance
```

## Change Order Process

```
CHANGE ORDER FORM
═══════════════════════════════════════════
Change Order #:    CO-[SOW#]-[NN]
Date Requested:    [Date]
Requested by:      [Name, Company]

DESCRIPTION OF CHANGE:
[Clear description of what is being added, removed, or modified]

REASON FOR CHANGE:
[Business justification]

IMPACT ASSESSMENT:
  Schedule Impact:     +[X] days / weeks
  Cost Impact:         +$[X,XXX]
  Resource Impact:     [Additional resources needed]
  Risk Impact:         [New risks introduced]
  Deliverable Impact:  [Modified deliverables]

REVISED TOTALS:
  Original SOW Value:    $[XXX,XXX]
  This Change Order:     $[XX,XXX]
  Previous Change Orders: $[XX,XXX]
  New Total:             $[XXX,XXX]

APPROVAL:
Provider: ________________  Date: ________
Client:   ________________  Date: ________

Note: Work on change order items begins only after written approval.
```

## Payment Schedule Template

| Engagement Type | Payment Structure | When |
|----------------|-------------------|------|
| **Fixed Price** | Milestone-based | Upon acceptance of each milestone |
| **Time & Materials** | Monthly invoicing | Net 30 from invoice date |
| **Retainer** | Monthly prepay | 1st of each month |
| **Hybrid** | Upfront + milestone + final | Per schedule below |

```
PAYMENT SCHEDULE (Fixed Price Example)
═══════════════════════════════════════════
Total Contract Value: $120,000

Payment    Trigger                        Amount      % of Total
────────   ───────────────────────────    ────────    ──────────
1          SOW execution (deposit)        $24,000       20%
2          M2: Design approved            $24,000       20%
3          M3: Development complete        $36,000       30%
4          M5: Go-live accepted            $30,000       25%
5          30 days post-launch (retainer)   $6,000        5%
                                          ────────    ──────────
           TOTAL                         $120,000      100%

Payment Terms: Net 15 from milestone acceptance
Late Payment: 1.5% per month on overdue balances
Expenses: Pre-approved expenses reimbursed at cost, no markup
```

## Assumptions and Exclusions

```
ASSUMPTIONS:
═══════════════════════════════════════════
1. Client will provide a single point of contact with decision-making authority
2. Client feedback and approvals will be provided within stated review periods
3. Client will provide all necessary content, assets, and data by agreed dates
4. Access to client systems and environments will be granted by [date]
5. Third-party APIs and services referenced in scope are available and functional
6. Work is performed during standard business hours [timezone]
7. Meetings and communication conducted in English
8. Provider team will work remotely unless otherwise specified

EXCLUSIONS:
═══════════════════════════════════════════
1. Ongoing maintenance and support (available under separate agreement)
2. Third-party software licenses and subscription fees
3. Hardware procurement
4. Data migration from legacy systems (unless specified in scope)
5. Content creation (copywriting, photography, video)
6. Legal, regulatory, or compliance certifications
7. Performance tuning beyond stated acceptance criteria
```

## Scripts & Tools

**generate_sow.py**: Create SOW from engagement parameters
```bash
python scripts/generate_sow.py --client "Acme Corp" --type fixed-price --duration 12w
# Output: SOW draft with all sections populated
```

**track_milestones.py**: Track milestone status and dependencies
```bash
python scripts/track_milestones.py --sow SOW-2026-0015
# Output: Milestone tracker with status, dates, blockers
```

**change_order.py**: Generate change order document
```bash
python scripts/change_order.py --sow SOW-2026-0015 --description "Add reporting module"
# Output: Change order form with impact assessment
```

## Best Practices

1. **Reference the MSA**: The SOW should operate under an existing Master Services Agreement
2. **Be exhaustive on exclusions**: What you leave out matters as much as what you include
3. **Use measurable acceptance criteria**: "Client is satisfied" is not a criterion
4. **Tie payments to acceptance, not dates**: You get paid when deliverables are accepted, not when time passes
5. **Build in buffer**: Add 15-20% schedule buffer without padding the price
6. **Define "done" upfront**: Acceptance criteria written before work starts prevent disputes later
7. **Limit revision rounds**: Uncapped revisions are a path to project losses
8. **Require timely client participation**: Delays from client feedback should adjust the timeline, not your quality
9. **Version the SOW**: Every revision gets a version number and date
10. **Keep scope atomic**: One SOW per engagement; don't bundle unrelated work
