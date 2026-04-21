# CES Customer Effort Score Survey Template

## Survey Configuration

| Field | Value |
|-------|-------|
| **Survey ID** | CES-EFFORT-001 |
| **Type** | CES (7-point agreement scale) |
| **Channel** | In-app / Post-chat |
| **Trigger Event** | {{process_completion_event}} |
| **Delay** | Immediate (0-2 minutes) |
| **Frequency Cap** | 1 survey per customer per 14 days |
| **Target Completion Time** | Under 1 minute |
| **Expiry** | Auto-dismiss after 5 minutes |

---

## Questions

### Q1 - Effort Rating (Required)

**Statement**: "{{company_name}} made it easy to handle my issue."

**Scale**:
| Value | Label |
|-------|-------|
| 1 | Strongly Disagree |
| 2 | Disagree |
| 3 | Somewhat Disagree |
| 4 | Neither Agree nor Disagree |
| 5 | Somewhat Agree |
| 6 | Agree |
| 7 | Strongly Agree |

**Display**: Horizontal scale with labels visible. Highlight selected value.

---

### Q2 - Difficulty Details (Conditional)

**Show When**: Q1 answer is 1, 2, or 3

**Question**: "What made this process difficult?"

**Type**: Open text
**Character Limit**: 500
**Placeholder**: "Please describe what made this harder than expected..."

---

### Q3 - Contact Attempts (Optional)

**Question**: "How many times did you contact us about this issue?"

**Type**: Single choice
**Options**:
- This was my first contact
- 2 times
- 3 times
- 4 or more times

---

## Close Message

"Thank you for your feedback!"

---

## Scoring and Interpretation

| CES Score | Interpretation | Action |
|-----------|---------------|--------|
| 1.0 - 3.0 | High effort -- significant friction | Immediate process review; flag for UX audit |
| 3.1 - 4.0 | Moderate effort -- room for improvement | Add to quarterly improvement backlog |
| 4.1 - 5.0 | Acceptable effort -- meets baseline | Monitor for trends |
| 5.1 - 6.0 | Low effort -- good experience | Identify and replicate success patterns |
| 6.1 - 7.0 | Very low effort -- effortless | Benchmark as best practice |

---

## High-Effort Alert Rules

| Condition | Action |
|-----------|--------|
| Q1 score <= 2 | Alert team lead; tag ticket for process review |
| Q3 = "4 or more times" | Flag as repeat contact; escalate to operations |
| Average CES < 4.0 for a category | Trigger process improvement initiative |
| CES drops > 0.5 points week-over-week | Alert operations manager |

---

## Recommended Use Cases

| Process | Trigger Event | Expected CES |
|---------|--------------|-------------|
| Password reset | reset.completed | 6.0+ |
| Billing inquiry | ticket.resolved (billing tag) | 5.0+ |
| Technical troubleshooting | ticket.resolved (technical tag) | 4.5+ |
| Account cancellation | cancellation.processed | 4.0+ |
| Product return/refund | refund.processed | 5.0+ |
| Onboarding setup | onboarding.step_complete | 5.5+ |
