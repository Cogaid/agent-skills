---
name: objection-handler
description: Handles sales objections with proven frameworks to address concerns and advance deals. Use when the user mentions "objection," "pushback," "prospect said no," "price concern," "too expensive," "not the right time," "need to think about it," "competitor mentioned," "overcoming resistance," or "handling concerns."
metadata:
  version: 1.1.0
  category: sales
---

# Objection Handler

Address objections confidently using proven frameworks that acknowledge concerns and move deals forward.

## Quick Start

1. **Identify objection type**: Use [reference.md](reference.md#objection-categories)
2. **Apply LAER framework**: Listen → Acknowledge → Explore → Respond
3. **Select response**: Use [templates/responses.md](templates/responses.md)
4. **Log outcome**: Run `python scripts/log_objection.py`

## Objection Handling Workflow

```
Progress:
- [ ] Step 1: Listen fully (don't interrupt)
- [ ] Step 2: Acknowledge the concern
- [ ] Step 3: Explore with questions
- [ ] Step 4: Respond with evidence
- [ ] Step 5: Confirm resolution
- [ ] Step 6: Advance to next step
- [ ] Step 7: Log objection and outcome
```

## LAER Framework

| Phase | Purpose | Example |
|-------|---------|---------|
| **Listen** | Hear fully without interrupting | Let them finish completely |
| **Acknowledge** | Validate the concern | "That's a fair concern..." |
| **Explore** | Understand the root cause | "Help me understand what's behind that..." |
| **Respond** | Address with evidence | Case study, ROI data, guarantee |

## Common Objection Types

| Type | Signal Phrases | Response Approach |
|------|----------------|-------------------|
| Price | "Too expensive," "Over budget" | ROI focus, payment options |
| Timing | "Not now," "Next quarter" | Cost of delay, quick wins |
| Authority | "Need to check with..." | Enable the champion |
| Competition | "Looking at X too" | Differentiation, proof |
| Status Quo | "Current solution works" | Hidden costs, future risk |

## Utility Scripts

**log_objection.py**: Document objection and outcome
```bash
python scripts/log_objection.py --type price --outcome resolved --deal "Acme"
python scripts/log_objection.py --interactive
```

**analyze_objections.py**: Analyze objection patterns from logs
```bash
python scripts/analyze_objections.py objections.json
# Output: Most common objections, success rates
```

## Resources

- **Full objection library**: [reference.md](reference.md)
- **Response templates**: [templates/responses.md](templates/responses.md)
- **Competitor comparisons**: [templates/battlecards.md](templates/battlecards.md)

## Related Skills

- Discovery questions: `discovery-call`
- Price negotiation: `proposal-writer`
- Qualifying fit: `lead-qualifier`
