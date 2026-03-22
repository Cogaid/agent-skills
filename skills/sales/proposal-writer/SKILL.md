---
name: proposal-writer
description: Creates compelling sales proposals and commercial offers. Use when the user mentions "write proposal," "create quote," "sales proposal," "pricing proposal," "SOW," "statement of work," "RFP response," "executive summary," "ROI analysis," "business case," or "prepare bid."
metadata:
  version: 1.1.0
  category: sales
---

# Proposal Writer

Create compelling proposals that communicate value clearly and make it easy for prospects to say yes.

## Quick Start

1. **Gather inputs**: Discovery notes, pricing, timeline
2. **Calculate ROI**: Run `python scripts/calculate_roi.py`
3. **Draft sections**: Use [templates/](templates/)
4. **Review checklist**: Use [reference.md](reference.md#review-checklist)
5. **Generate proposal**: Run `python scripts/generate_proposal.py`

## Proposal Workflow

```
Progress:
- [ ] Step 1: Review discovery notes for their words
- [ ] Step 2: Calculate ROI / value justification
- [ ] Step 3: Draft executive summary (1 page max)
- [ ] Step 4: Write scope of work
- [ ] Step 5: Add relevant case studies / proof
- [ ] Step 6: Format pricing with value framing
- [ ] Step 7: Define clear next steps
- [ ] Step 8: Proofread (especially names!)
- [ ] Step 9: Send with brief email
```

## Proposal Structure

| Section | Purpose | Length |
|---------|---------|--------|
| Executive Summary | Decision-maker overview | 1 page |
| Current Situation | Show you understand them | 0.5-1 page |
| Desired Outcomes | Align on success metrics | 0.5 page |
| Proposed Solution | What you'll deliver | 1-2 pages |
| Why Us | Differentiate from alternatives | 0.5-1 page |
| Investment | Pricing with value frame | 1 page |
| Timeline | When they'll see value | 0.5 page |
| Next Steps | Make it easy to proceed | 0.25 page |

**Total: 5-8 pages**

## Core Principles

- **Customer-centric**: Their goals first, your solution second
- **Use their words**: Reference exact phrases from discovery
- **Make ROI obvious**: Quantify the value they'll receive
- **Remove friction**: Clear next steps with specific dates

## Utility Scripts

**calculate_roi.py**: Build ROI analysis from inputs
```bash
python scripts/calculate_roi.py --current-cost 50000 --savings 30000 --investment 25000
# Output: Payback period, Year 1 ROI, 3-year value
```

**generate_proposal.py**: Generate proposal from template
```bash
python scripts/generate_proposal.py --company "Acme" --template standard --interactive
# Output: Markdown proposal document
```

**check_proposal.py**: Validate proposal before sending
```bash
python scripts/check_proposal.py proposal.md
# Output: Missing sections, word count, readability
```

## Resources

- **Full writing guide**: [reference.md](reference.md)
- **Executive summary template**: [templates/executive-summary.md](templates/executive-summary.md)
- **Pricing tables**: [templates/pricing.md](templates/pricing.md)
- **ROI calculator template**: [templates/roi-analysis.md](templates/roi-analysis.md)

## Related Skills

- Discovery for proposal inputs: `discovery-call`
- Handling proposal objections: `objection-handler`
- Qualifying before writing: `lead-qualifier`
