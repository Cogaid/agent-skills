---
name: ticket-triage
description: Categorizes, prioritizes, and routes support tickets. Use when the user mentions "triage tickets," "categorize support requests," "prioritize issues," "sort tickets," "classify customer issues," "route tickets," "assign priority," "urgent vs normal," "ticket queue," "support backlog," "which tickets first," or "incoming tickets." Also use for bulk ticket processing and triage workflows.
metadata:
  version: 1.1.0
  category: customer-support
---

# Ticket Triage

Categorize, prioritize, and route support tickets for optimal resolution.

## Quick Start

1. **Analyze ticket**: Run `python scripts/analyze_ticket.py` to extract key information
2. **Assign priority**: Use the priority framework below
3. **Categorize**: Assign primary and secondary categories
4. **Route**: Direct to appropriate team
5. **Respond**: Use templates from [templates/responses.md](templates/responses.md)

## Triage Workflow

Copy this checklist and track progress:

```
Triage Progress:
- [ ] Step 1: Extract ticket data (run analyze_ticket.py)
- [ ] Step 2: Check for red flags (run check_red_flags.py)
- [ ] Step 3: Assign priority (P1-P4)
- [ ] Step 4: Categorize (primary + secondary)
- [ ] Step 5: Route to team
- [ ] Step 6: Draft initial response
```

## Priority Framework

| Priority | Response Time | Criteria |
|----------|---------------|----------|
| **P1 Critical** | < 1 hour | Service down, security breach, revenue impact |
| **P2 High** | < 4 hours | Feature broken, VIP issues, workflow disruption |
| **P3 Normal** | < 24 hours | Single user issues, config questions, non-blocking bugs |
| **P4 Low** | < 72 hours | General questions, feature suggestions, minor UI |

**Full priority definitions**: See [reference.md](reference.md#priority-definitions)

## Category Quick Reference

| Category | Keywords |
|----------|----------|
| Bug | "doesn't work," "error," "broken," "crash" |
| Performance | "slow," "timeout," "lag," "loading" |
| Billing | "charge," "invoice," "payment," "refund" |
| Access | "can't login," "password," "locked out" |
| How-To | "how do I," "where is," "help with" |

**Full category list**: See [reference.md](reference.md#categories)

## Utility Scripts

**analyze_ticket.py**: Extract structured data from ticket text
```bash
python scripts/analyze_ticket.py "ticket text here"
# Output: JSON with sentiment, keywords, suggested category
```

**check_red_flags.py**: Detect escalation triggers
```bash
python scripts/check_red_flags.py "ticket text here"
# Output: List of detected red flags (legal, regulatory, churn risk)
```

**batch_triage.py**: Process multiple tickets from CSV
```bash
python scripts/batch_triage.py tickets.csv --output triaged.csv
```

## Output Format

```
TICKET: [ID]
PRIORITY: [P1/P2/P3/P4] - [Reason]
CATEGORY: [Primary] > [Secondary]
ROUTE TO: [Team]
RED FLAGS: [None / List]
SUGGESTED RESPONSE: [Template name]
```

## Resources

- **Priority definitions & examples**: [reference.md](reference.md)
- **Response templates**: [templates/responses.md](templates/responses.md)
- **Routing rules**: [reference.md](reference.md#routing-rules)

## Related Skills

- Escalated tickets: `escalation-handler`
- Creating help articles: `knowledge-base-writer`
- Analyzing patterns: `customer-feedback-analyzer`
