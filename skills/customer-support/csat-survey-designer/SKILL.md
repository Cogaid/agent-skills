---
name: csat-survey-designer
description: Design post-interaction customer satisfaction surveys with optimized question flows. Use when the user mentions "CSAT survey," "satisfaction survey," "NPS survey," "customer effort score," "CES," "survey design," "post-interaction survey," "feedback survey," "survey questions," "survey template," or "measure satisfaction."
metadata:
  version: 1.0.0
  category: customer-support
---

# CSAT Survey Designer

Design effective post-interaction satisfaction surveys that maximize response rates and yield actionable insights.

## Purpose

Create surveys that accurately capture customer sentiment without causing survey fatigue. This skill covers survey type selection, question design, timing optimization, and results analysis to drive continuous improvement.

## Quick Reference

### Survey Types Comparison

| Survey Type | Metric | Scale | Best For | Frequency |
|-------------|--------|-------|----------|-----------|
| **CSAT** | Satisfaction | 1-5 stars or 1-7 scale | Transaction-level feedback | After each interaction |
| **NPS** | Loyalty | 0-10 scale | Relationship health | Quarterly |
| **CES** | Effort | 1-7 scale | Process friction | After support/purchase |
| **PSAT** | Product satisfaction | 1-5 scale | Feature feedback | Monthly/quarterly |
| **SUS** | Usability | 1-5 (10 items) | UI/UX evaluation | After onboarding |

### Response Rate Benchmarks

| Channel | Average Rate | Good Rate | Excellent Rate |
|---------|-------------|-----------|----------------|
| In-app popup | 12-15% | 20-25% | 30%+ |
| Email | 5-10% | 15-20% | 25%+ |
| SMS | 10-15% | 20-30% | 35%+ |
| Post-chat | 15-25% | 30-40% | 45%+ |
| IVR/Phone | 5-8% | 10-15% | 20%+ |

## Workflow

### Survey Design Checklist

```
Survey Design Progress:
- [ ] Step 1: Define survey objective and target audience
- [ ] Step 2: Select survey type (CSAT, NPS, CES)
- [ ] Step 3: Draft questions (max 5 for transactional, max 12 for relational)
- [ ] Step 4: Set rating scale and labels
- [ ] Step 5: Add conditional logic / branching
- [ ] Step 6: Configure timing and delivery channel
- [ ] Step 7: Set up response collection and alerts
- [ ] Step 8: Test survey flow end-to-end
- [ ] Step 9: Launch to pilot group (10% of audience)
- [ ] Step 10: Analyze pilot results and adjust
- [ ] Step 11: Full rollout
```

### Timing Optimization Matrix

| Interaction Type | Optimal Send Time | Max Delay | Notes |
|-----------------|-------------------|-----------|-------|
| Live chat | Immediately after | 5 minutes | Embed in chat close |
| Phone call | 1-2 hours after | 24 hours | SMS or IVR callback |
| Email support | 1-4 hours after | 48 hours | Reply-chain or link |
| In-store visit | Same day evening | 24 hours | SMS preferred |
| Product delivery | 2-3 days after use | 7 days | Allow usage time |
| Onboarding | 7 days after start | 14 days | After initial value |

## Templates

### CSAT Survey Template (Post-Support)

```
SURVEY: Post-Support Satisfaction
TYPE: CSAT (5-point scale)
CHANNEL: {{channel}}
TRIGGER: {{interaction_close_event}}
DELAY: {{delay_minutes}} minutes

---

Q1 (Required - Rating):
"How satisfied were you with the support you received today?"
Scale: 1 (Very Dissatisfied) | 2 (Dissatisfied) | 3 (Neutral) | 4 (Satisfied) | 5 (Very Satisfied)

Q2 (Conditional - if Q1 <= 3, open text):
"We're sorry to hear that. What could we have done better?"
Character limit: 500

Q3 (Conditional - if Q1 >= 4, open text):
"Great to hear! What did you appreciate most?"
Character limit: 500

Q4 (Optional - Rating):
"How easy was it to get your issue resolved?"
Scale: 1 (Very Difficult) | 2 | 3 | 4 | 5 (Very Easy)

Q5 (Optional - Multiple choice):
"Was your issue fully resolved?"
Options: Yes | Partially | No

CLOSE MESSAGE: "Thank you for your feedback! It helps us improve."
```

### NPS Survey Template (Quarterly Relationship)

```
SURVEY: Quarterly NPS
TYPE: NPS (0-10 scale)
CHANNEL: Email
TRIGGER: Quarterly schedule
AUDIENCE: Active customers (last 90 days)

---

Q1 (Required - NPS):
"How likely are you to recommend {{company_name}} to a friend or colleague?"
Scale: 0 (Not at all likely) -------- 10 (Extremely likely)

Q2 (Required - Open text):
Detractors (0-6): "We appreciate your honesty. What is the primary reason for your score?"
Passives (7-8): "What would we need to do to earn a higher score?"
Promoters (9-10): "Wonderful! What do you value most about {{company_name}}?"

Q3 (Optional - Multiple choice):
"Which area matters most to you?"
Options: Product quality | Customer support | Pricing | Ease of use | Reliability | Other

CLOSE MESSAGE:
Detractors: "Thank you. A team member may reach out to learn more about your experience."
Passives: "Thank you for your feedback. We are always working to improve."
Promoters: "Thank you! Would you be willing to leave a review? [Link]"
```

### CES Survey Template (Effort Score)

```
SURVEY: Customer Effort Score
TYPE: CES (7-point scale)
CHANNEL: In-app / Post-chat
TRIGGER: {{process_completion_event}}

---

Q1 (Required - CES):
"To what extent do you agree: {{company_name}} made it easy to handle my issue."
Scale: 1 (Strongly Disagree) | 2 | 3 | 4 | 5 | 6 | 7 (Strongly Agree)

Q2 (Conditional - if Q1 <= 3, open text):
"What made this process difficult?"
Character limit: 500

Q3 (Optional - Multiple choice):
"How many times did you contact us about this issue?"
Options: This was my first contact | 2 times | 3 times | 4+ times
```

## Survey Length Guidelines

| Survey Type | Max Questions | Target Completion Time | Drop-off Threshold |
|-------------|--------------|----------------------|-------------------|
| Transactional CSAT | 3-5 | Under 2 minutes | >3 min = 40%+ drop |
| Relational NPS | 3-5 | Under 3 minutes | >4 min = 50%+ drop |
| CES | 2-3 | Under 1 minute | >2 min = 35%+ drop |
| Detailed quarterly | 8-12 | Under 5 minutes | >7 min = 60%+ drop |
| Annual relationship | 15-20 | Under 10 minutes | Incentive required |

## Analysis Framework

### Score Interpretation

| Metric | Poor | Below Average | Average | Good | Excellent |
|--------|------|---------------|---------|------|-----------|
| CSAT (5pt) | <3.0 | 3.0-3.5 | 3.5-4.0 | 4.0-4.5 | 4.5-5.0 |
| NPS | <0 | 0-20 | 20-40 | 40-60 | 60+ |
| CES (7pt) | <3.0 | 3.0-4.0 | 4.0-5.0 | 5.0-6.0 | 6.0-7.0 |

### Analysis Process

```
Analysis Checklist:
- [ ] Calculate overall score and trend (vs. last period)
- [ ] Segment by channel, agent, product, customer tier
- [ ] Identify top 3 positive themes from open text
- [ ] Identify top 3 negative themes from open text
- [ ] Calculate response rate and compare to benchmark
- [ ] Flag any scores below threshold for immediate action
- [ ] Correlate with operational metrics (handle time, FCR)
- [ ] Generate improvement recommendations
```

## Improvement Action Template

```
SURVEY IMPROVEMENT PLAN
Date: {{date}}
Period: {{start_date}} to {{end_date}}
Current Score: {{score}} ({{trend}} from last period)

TOP ISSUES IDENTIFIED:
1. {{issue_1}} - Mentioned in {{count}} responses ({{percentage}}%)
   Root Cause: {{root_cause}}
   Owner: {{owner}}
   Action: {{action}}
   Target Date: {{target_date}}

2. {{issue_2}} - Mentioned in {{count}} responses ({{percentage}}%)
   Root Cause: {{root_cause}}
   Owner: {{owner}}
   Action: {{action}}
   Target Date: {{target_date}}

3. {{issue_3}} - Mentioned in {{count}} responses ({{percentage}}%)
   Root Cause: {{root_cause}}
   Owner: {{owner}}
   Action: {{action}}
   Target Date: {{target_date}}

SUCCESS METRICS:
- Target score next period: {{target}}
- Target response rate: {{rate_target}}
- Review date: {{review_date}}
```

## Scripts & Tools

**design_survey.py**: Generate survey configuration from parameters
```bash
python scripts/design_survey.py --type csat --channel email --questions 5
# Output: Survey JSON config with questions, logic, and timing
```

**analyze_responses.py**: Analyze collected survey responses
```bash
python scripts/analyze_responses.py --survey-id SRV-001 --period last-quarter
# Output: Score summary, trends, themes, and recommendations
```

**optimize_timing.py**: A/B test survey timing for best response rates
```bash
python scripts/optimize_timing.py --survey-id SRV-001 --variants 3
# Output: Timing recommendations based on response rate data
```

## Best Practices

1. **Keep it short** - Every additional question reduces completion by 5-10%
2. **Ask the rating first** - Lead with the quantitative question before open text
3. **Use conditional branching** - Show follow-ups based on score to reduce fatigue
4. **Avoid double-barreled questions** - Ask one thing at a time
5. **Randomize option order** - Prevent position bias on multiple-choice questions
6. **Close the loop** - Follow up with detractors within 48 hours
7. **Respect frequency caps** - No more than one survey per customer per 30 days
8. **Mobile-optimize** - 60%+ of surveys are completed on mobile devices
9. **Test before launch** - Pilot with 10% of audience before full rollout
10. **Track trends, not snapshots** - Monthly trending reveals more than point-in-time scores

## Related Skills

- Feedback analysis: `customer-feedback-analyzer`
- Escalation from low scores: `escalation-handler`
- Response templates: `canned-response-library`
