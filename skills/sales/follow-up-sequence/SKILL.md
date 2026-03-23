# Follow-Up Sequence

---
name: follow-up-sequence
description: Create and manage multi-touch follow-up sequences for prospects. Use when the user mentions "follow-up email," "drip campaign," "nurture sequence," "lead follow-up," "sales cadence," "outreach sequence," or "prospect touchpoints."
metadata:
  version: 1.0.0
  category: sales
---

## Purpose

Design effective follow-up sequences that nurture prospects through the sales funnel while maintaining engagement without being pushy.

## Quick Reference

### Optimal Sequence Timing

| Touch # | Timing | Channel | Purpose |
|---------|--------|---------|---------|
| 1 | Day 0 | Email | Initial outreach/connection |
| 2 | Day 2-3 | Email | Value add / Resource share |
| 3 | Day 5-7 | LinkedIn/Call | Different channel engagement |
| 4 | Day 10-12 | Email | Case study / Social proof |
| 5 | Day 14-15 | Call | Direct conversation attempt |
| 6 | Day 18-21 | Email | Breakup / Final attempt |

### Response Rate Benchmarks

| Touch # | Expected Response | Action if No Response |
|---------|-------------------|----------------------|
| 1 | 10-15% | Continue sequence |
| 2 | 8-12% | Continue sequence |
| 3 | 5-10% | Continue sequence |
| 4 | 3-8% | Evaluate engagement |
| 5 | 5-10% | Consider breakup |
| 6 | 10-15% | Archive if no response |

## Sequence Types

### Cold Outreach Sequence
- **Duration:** 3-4 weeks
- **Touches:** 6-8
- **Goal:** Get initial meeting
- **Tone:** Curious, value-focused

### Post-Meeting Follow-Up
- **Duration:** 1-2 weeks
- **Touches:** 3-4
- **Goal:** Move to next stage
- **Tone:** Helpful, momentum-building

### Re-Engagement Sequence
- **Duration:** 2-3 weeks
- **Touches:** 4-5
- **Goal:** Restart stalled deal
- **Tone:** Fresh angle, new value

### Lost Deal Revival
- **Duration:** 4-6 weeks
- **Touches:** 3-4
- **Goal:** Reopen opportunity
- **Tone:** No pressure, check-in

## Workflow Checklist

### 1. Sequence Planning
- [ ] Define sequence goal/outcome
- [ ] Identify target persona
- [ ] Choose sequence type
- [ ] Set timing intervals
- [ ] Select channels per touch

### 2. Content Creation
- [ ] Write subject lines (2-3 options per email)
- [ ] Draft email body copy
- [ ] Create call scripts
- [ ] Prepare LinkedIn messages
- [ ] Include personalization tokens

### 3. Personalization Setup
- [ ] Research prospect company
- [ ] Identify relevant triggers
- [ ] Note personal details
- [ ] Find mutual connections
- [ ] Prepare custom hooks

### 4. Sequence Launch
- [ ] Load into CRM/automation tool
- [ ] Set sending times
- [ ] Configure pause triggers
- [ ] Test all touchpoints
- [ ] Enable reply detection

### 5. Monitoring & Optimization
- [ ] Track open rates
- [ ] Monitor reply rates
- [ ] Note objections received
- [ ] A/B test variations
- [ ] Iterate on messaging

## Email Templates

→ See `templates/email_sequences.md` for ready-to-use email templates

## Sequence Reference

→ See `reference.md` for detailed guidance on timing, personalization, and optimization

## Scripts & Tools

| Script | Purpose |
|--------|---------|
| `scripts/sequence_builder.py` | Generate customized follow-up sequences |
| `scripts/sequence_analyzer.py` | Analyze sequence performance metrics |

## Best Practices

### Do's
- Provide value in every touch
- Vary your channels
- Personalize beyond {name}
- Reference their specific situation
- Include clear CTAs
- Keep emails under 150 words

### Don'ts
- Send generic templates
- Follow up same day
- Use aggressive language
- Make false urgency claims
- Send only text (use video, links)
- Ignore engagement signals

## Key Metrics

| Metric | Good | Great |
|--------|------|-------|
| Open Rate | 25%+ | 40%+ |
| Reply Rate | 5%+ | 10%+ |
| Meeting Book Rate | 2%+ | 5%+ |
| Sequence Completion | 80%+ | 90%+ |
