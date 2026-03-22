---
name: discovery-call
description: Conducts effective sales discovery conversations to uncover needs and qualify opportunities. Use when the user mentions "discovery call," "first sales meeting," "qualifying call," "needs assessment," "understand the prospect," "prepare for meeting," "sales conversation," "diagnostic call," "consultative selling," "what questions to ask," or "discovery agenda."
metadata:
  version: 1.1.0
  category: sales
---

# Discovery Call

Conduct discovery conversations that uncover true needs and set the foundation for successful deals.

## Quick Start

1. **Research prospect**: Run `python scripts/research_prospect.py`
2. **Prepare questions**: Use [templates/questions.md](templates/questions.md)
3. **Use SPIN framework**: Situation → Problem → Implication → Need-Payoff
4. **Document findings**: Run `python scripts/log_discovery.py`
5. **Send follow-up**: Use [templates/followup.md](templates/followup.md)

## Discovery Workflow

```
Discovery Progress:
- [ ] Step 1: Pre-call research (15 min)
- [ ] Step 2: Set agenda at call start
- [ ] Step 3: SPIN discovery questions (20-30 min)
- [ ] Step 4: Brief solution preview (5-10 min)
- [ ] Step 5: Confirm next steps
- [ ] Step 6: Send follow-up email (within 1 hour)
- [ ] Step 7: Update CRM notes
```

## SPIN Framework

| Phase | Purpose | Example |
|-------|---------|---------|
| **Situation** | Understand current state | "Walk me through your current process..." |
| **Problem** | Uncover challenges | "What's working? What's not?" |
| **Implication** | Amplify pain | "How does that affect your team?" |
| **Need-Payoff** | Envision solution | "If you could fix this, what would change?" |

**Full question library**: See [reference.md](reference.md#spin-questions)

## Utility Scripts

**research_prospect.py**: Compile prospect research
```bash
python scripts/research_prospect.py "Company Name"
# Output: Company info, recent news, potential pain points
```

**log_discovery.py**: Document discovery findings
```bash
python scripts/log_discovery.py --company "Acme" --contact "John" --interactive
# Output: Structured discovery notes
```

## Key Metrics

Target talk ratio: **30% you / 70% prospect**

## Resources

- **Question library**: [reference.md](reference.md)
- **Pre-call template**: [templates/precall.md](templates/precall.md)
- **Follow-up email**: [templates/followup.md](templates/followup.md)

## Related Skills

- Handling objections: `objection-handler`
- Qualifying leads: `lead-qualifier`
- Creating proposals: `proposal-writer`
