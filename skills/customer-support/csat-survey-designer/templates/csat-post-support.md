# CSAT Post-Support Survey Template

## Survey Configuration

| Field | Value |
|-------|-------|
| **Survey ID** | CSAT-POST-SUPPORT-001 |
| **Type** | CSAT (5-point scale) |
| **Channel** | {{channel}} (email / in-app / post-chat / SMS) |
| **Trigger Event** | {{interaction_close_event}} |
| **Delay** | {{delay_minutes}} minutes after trigger |
| **Frequency Cap** | 1 survey per customer per 30 days |
| **Target Completion Time** | Under 2 minutes |
| **Expiry** | Survey link expires after 7 days |

---

## Questions

### Q1 - Satisfaction Rating (Required)

**Question**: "How satisfied were you with the support you received today?"

**Scale**:
| Value | Label | Emoji (if enabled) |
|-------|-------|--------------------|
| 1 | Very Dissatisfied | :( |
| 2 | Dissatisfied | :/ |
| 3 | Neutral | :| |
| 4 | Satisfied | :) |
| 5 | Very Satisfied | :D |

**Display**: Star rating or smiley faces (A/B test to determine best format)

---

### Q2 - Improvement Feedback (Conditional)

**Show When**: Q1 answer is 1, 2, or 3

**Question**: "We're sorry to hear that. What could we have done better?"

**Type**: Open text
**Character Limit**: 500
**Placeholder**: "Please share any details that would help us improve..."

---

### Q3 - Positive Feedback (Conditional)

**Show When**: Q1 answer is 4 or 5

**Question**: "Great to hear! What did you appreciate most?"

**Type**: Open text
**Character Limit**: 500
**Placeholder**: "Tell us what went well..."

---

### Q4 - Effort Rating (Optional)

**Question**: "How easy was it to get your issue resolved?"

**Scale**:
| Value | Label |
|-------|-------|
| 1 | Very Difficult |
| 2 | Difficult |
| 3 | Neutral |
| 4 | Easy |
| 5 | Very Easy |

---

### Q5 - Resolution Confirmation (Optional)

**Question**: "Was your issue fully resolved?"

**Type**: Single choice
**Options**:
- Yes
- Partially
- No

**Branching**: If "No" or "Partially" selected, auto-create follow-up ticket flag.

---

## Close Messages

**Default**: "Thank you for your feedback! It helps us improve."

**If Q1 <= 2**: "Thank you for your honesty. A team member may reach out to follow up on your experience."

**If Q1 == 5 and Q5 == "Yes"**: "Thank you! We're glad we could help. If you have a moment, we'd love a review: [Review Link]"

---

## Alert Rules

| Condition | Action |
|-----------|--------|
| Q1 score = 1 | Immediate alert to team lead; auto-flag for follow-up |
| Q1 score <= 2 | Alert to assigned agent's supervisor within 1 hour |
| Q5 = "No" | Reopen ticket or create follow-up ticket |
| Response rate < 10% | Alert survey operations to investigate delivery issues |

---

## Customization Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `{{channel}}` | Delivery channel | post-chat |
| `{{interaction_close_event}}` | Event that triggers the survey | chat.closed |
| `{{delay_minutes}}` | Minutes to wait after trigger | 5 |
| `{{company_name}}` | Company display name | (required) |
| `{{agent_name}}` | Name of agent who handled the interaction | (from ticket) |
| `{{ticket_id}}` | Reference number for the interaction | (from system) |
