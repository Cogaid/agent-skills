---
name: escalation-handler
description: Handles escalated customer issues, angry customers, and complex complaints. Use when the user mentions "escalation," "angry customer," "frustrated user," "complaint," "wants to speak to manager," "threatening to cancel," "demanding refund," "negative review threat," "customer is upset," "de-escalation," or "service recovery." Also use for compensation decisions and escalation tracking.
metadata:
  version: 1.1.0
  category: customer-support
---

# Escalation Handler

Handle escalated customer issues with empathy and effective resolution strategies.

## Quick Start

1. **Assess severity**: Run `python scripts/assess_escalation.py` on ticket text
2. **Apply HEARD framework**: Listen → Acknowledge → Explore → Resolve → Diagnose
3. **Determine compensation**: Use [compensation guidelines](reference.md#compensation)
4. **Draft response**: Use templates from [templates/responses.md](templates/responses.md)
5. **Document**: Log escalation with `python scripts/log_escalation.py`

## Escalation Workflow

Copy this checklist:

```
Escalation Progress:
- [ ] Step 1: Assess severity (run assess_escalation.py)
- [ ] Step 2: Review customer history
- [ ] Step 3: Apply HEARD framework
- [ ] Step 4: Propose resolution
- [ ] Step 5: Determine compensation (if applicable)
- [ ] Step 6: Draft response using template
- [ ] Step 7: Document escalation
- [ ] Step 8: Follow up within 24 hours
```

## The HEARD Framework

| Step | Action | Key Phrases |
|------|--------|-------------|
| **H**ear | Let them explain fully | "Tell me more..." |
| **E**mpathize | Validate feelings | "I understand why you're frustrated" |
| **A**pologize | Take responsibility | "I apologize for this experience" |
| **R**esolve | Propose solution | "Here's what I'm going to do..." |
| **D**iagnose | Document root cause | Internal notes for prevention |

## Escalation Levels

| Level | Signals | Response |
|-------|---------|----------|
| **1 - Frustrated** | Firm tone, multiple contacts | Extra attention, faster response |
| **2 - Angry** | Raised voice, threats | Active listening, immediate action |
| **3 - Critical** | Legal, media, exec involvement | Senior leadership, white-glove |

**Full escalation criteria**: See [reference.md](reference.md#escalation-levels)

## Utility Scripts

**assess_escalation.py**: Evaluate escalation severity
```bash
python scripts/assess_escalation.py "ticket text"
# Output: Level, risk factors, recommended approach
```

**calculate_compensation.py**: Suggest appropriate compensation
```bash
python scripts/calculate_compensation.py --tier enterprise --impact high --duration 3
# Output: Compensation recommendation with justification
```

**log_escalation.py**: Document escalation for tracking
```bash
python scripts/log_escalation.py --ticket 12345 --level 2 --resolution "credit applied"
```

## Resources

- **Escalation levels & criteria**: [reference.md](reference.md#escalation-levels)
- **Compensation guidelines**: [reference.md](reference.md#compensation)
- **Legal red flags**: [reference.md](reference.md#legal-triggers)
- **Response templates**: [templates/responses.md](templates/responses.md)

## Related Skills

- Initial triage: `ticket-triage`
- Knowledge base: `knowledge-base-writer`
- Pattern analysis: `customer-feedback-analyzer`
