# Decision Record Template

## Usage

Document every significant decision with this template. Assign a sequential ID (DEC-001, DEC-002, etc.). Fill in the outcome section at the review date.

---

## Decision Record

**ID:** DEC-{{number}}
**Date:** {{date}}
**Decision Maker:** {{name}}
**Status:** {{Proposed / Decided / Reviewed}}

### Decision Question

{{What specific question are we answering?}}

### Context

{{Why is this decision needed now? What triggered it?}}

### Options Considered

| # | Option | Description | Status |
|---|--------|-------------|--------|
| 1 | {{option_1}} | {{brief_description}} | {{Chosen / Rejected / Deferred}} |
| 2 | {{option_2}} | {{brief_description}} | {{Chosen / Rejected / Deferred}} |
| 3 | {{option_3}} | {{brief_description}} | {{Chosen / Rejected / Deferred}} |
| 4 | Status Quo | {{what_happens_if_we_do_nothing}} | {{Chosen / Rejected}} |

### Evaluation Method

{{Weighted Matrix / Pros-Cons / RAPID / Cost-Benefit / Other}}

### Decision

**Chosen Option:** {{chosen_option}}

### Rationale

{{Why this option was chosen. Reference scores, data, or key arguments.}}

### Key Tradeoffs

| Tradeoff Accepted | Mitigation |
|--------------------|------------|
| {{tradeoff_1}} | {{how_we_address_it}} |
| {{tradeoff_2}} | {{how_we_address_it}} |

### Dissenting Views

{{Who disagreed, what their argument was, and why the decision went differently.
If no dissent, note "No dissenting views recorded."}}

### Reversibility

**Type:** {{One-way door / Two-way door}}
**Explanation:** {{How hard would it be to reverse this decision?}}
**Point of no return:** {{Date or milestone after which reversal is difficult}}

### Implementation

| Action | Owner | Due Date |
|--------|-------|----------|
| {{action_1}} | {{name}} | {{date}} |
| {{action_2}} | {{name}} | {{date}} |

### Review

**Review Date:** {{date_to_evaluate_outcome}}
**Success Criteria:** {{how_we_will_know_this_was_a_good_decision}}

### Outcome (filled in at review date)

**Date Reviewed:** {{actual_review_date}}
**Outcome:** {{what_actually_happened}}
**Decision Quality:** {{Good / Acceptable / Poor}}
**Lessons Learned:** {{what_we_would_do_differently}}
