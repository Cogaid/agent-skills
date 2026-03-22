---
name: lead-qualifier
description: Qualifies leads and assesses opportunity fit using proven frameworks. Use when the user mentions "qualify lead," "lead scoring," "BANT," "MEDDIC," "is this a good fit," "opportunity assessment," "prospect qualification," "pipeline review," "deal assessment," or "should I pursue this."
metadata:
  version: 1.1.0
  category: sales
---

# Lead Qualifier

Qualify leads effectively using proven frameworks to focus time on opportunities most likely to close.

## Quick Start

1. **Define ICP**: Use [reference.md](reference.md#icp-template)
2. **Score lead**: Run `python scripts/score_lead.py`
3. **Apply framework**: BANT (SMB) or MEDDIC (Enterprise)
4. **Document assessment**: Use [templates/assessment.md](templates/assessment.md)
5. **Decide action**: Pursue / Nurture / Disqualify

## Qualification Workflow

```
Progress:
- [ ] Step 1: Check ICP fit (firmographics)
- [ ] Step 2: Confirm Budget exists or can be found
- [ ] Step 3: Identify Authority (decision maker access)
- [ ] Step 4: Validate Need (real problem to solve)
- [ ] Step 5: Understand Timeline (urgency)
- [ ] Step 6: Score opportunity
- [ ] Step 7: Document and decide action
```

## Framework Selection

| Framework | Best For | Key Criteria |
|-----------|----------|--------------|
| **BANT** | SMB, transactional, short cycles | Budget, Authority, Need, Timeline |
| **MEDDIC** | Enterprise, complex, long cycles | Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion |
| **CHAMP** | Consultative, customer-centric | Challenges, Authority, Money, Prioritization |

## BANT Quick Reference

| Criteria | Green Flag | Red Flag |
|----------|------------|----------|
| **Budget** | Allocated, specific amount | "No budget," won't discuss |
| **Authority** | Talking to decision-maker | "I have no influence" |
| **Need** | Clear, painful problem | Vague, nice-to-have |
| **Timeline** | Defined, urgent | "No rush," "Someday" |

**Scoring**: 4/4 = Pursue | 3/4 = Address gap | 2/4 = Nurture | <2 = Disqualify

## Utility Scripts

**score_lead.py**: Calculate lead score from inputs
```bash
python scripts/score_lead.py --company "Acme" --size 150 --industry tech --interactive
# Output: Score, classification, recommended action
```

**analyze_pipeline.py**: Review pipeline health
```bash
python scripts/analyze_pipeline.py pipeline.json
# Output: Aging deals, missing data, recommendations
```

**batch_qualify.py**: Score multiple leads from CSV
```bash
python scripts/batch_qualify.py leads.csv --output scored.csv
# Output: Scored and sorted lead list
```

## Disqualification Criteria

**Hard Disqualifiers** (Walk away):
- No budget AND no ability to create budget
- No problem you can solve
- Required features you don't have
- Company in financial distress

**Soft Disqualifiers** (Nurture):
- Timing >12 months out
- Currently in competitor contract
- Decision-maker change in progress

## Resources

- **Full framework guide**: [reference.md](reference.md)
- **Assessment template**: [templates/assessment.md](templates/assessment.md)
- **ICP worksheet**: [templates/icp.md](templates/icp.md)
- **Disqualification scripts**: [templates/disqualify.md](templates/disqualify.md)

## Related Skills

- Discovery questioning: `discovery-call`
- Handling qualification objections: `objection-handler`
- Writing proposals for qualified leads: `proposal-writer`
