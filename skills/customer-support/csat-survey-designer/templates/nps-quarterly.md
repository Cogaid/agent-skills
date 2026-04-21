# NPS Quarterly Relationship Survey Template

## Survey Configuration

| Field | Value |
|-------|-------|
| **Survey ID** | NPS-QUARTERLY-001 |
| **Type** | NPS (0-10 scale) |
| **Channel** | Email |
| **Trigger** | Quarterly schedule (Jan, Apr, Jul, Oct) |
| **Audience** | Active customers with activity in last 90 days |
| **Exclusions** | Customers surveyed in last 60 days; churned accounts |
| **Target Completion Time** | Under 3 minutes |
| **Expiry** | Survey link expires after 14 days |
| **Reminder** | One reminder email at day 7 if not completed |

---

## Questions

### Q1 - NPS Score (Required)

**Question**: "How likely are you to recommend {{company_name}} to a friend or colleague?"

**Scale**: 0 (Not at all likely) to 10 (Extremely likely)

**Display**: Horizontal number scale with anchored labels at 0 and 10.

**Segments**:
| Score | Segment | Color Code |
|-------|---------|------------|
| 0-6 | Detractor | Red |
| 7-8 | Passive | Yellow |
| 9-10 | Promoter | Green |

---

### Q2 - Follow-Up (Required, Segment-Dependent)

**For Detractors (0-6)**:
"We appreciate your honesty. What is the primary reason for your score?"

**For Passives (7-8)**:
"What would we need to do to earn a higher score?"

**For Promoters (9-10)**:
"Wonderful! What do you value most about {{company_name}}?"

**Type**: Open text
**Character Limit**: 1000
**Placeholder**: Varies by segment (see above)

---

### Q3 - Priority Area (Optional)

**Question**: "Which area matters most to you?"

**Type**: Single choice (randomized order)
**Options**:
- Product quality
- Customer support
- Pricing
- Ease of use
- Reliability
- Other (with text field)

---

## Close Messages

**Detractors (0-6)**:
"Thank you for your candid feedback. A team member may reach out to learn more about your experience and how we can improve."

**Passives (7-8)**:
"Thank you for your feedback. We are always working to improve and appreciate your input."

**Promoters (9-10)**:
"Thank you! Your support means the world to us. Would you be willing to leave a review? [Review Link]"

---

## Email Subject Lines (A/B Test)

| Variant | Subject Line |
|---------|-------------|
| A (Control) | "Quick question about your experience with {{company_name}}" |
| B | "{{customer_name}}, how are we doing?" |
| C | "One question, 10 seconds -- your feedback matters" |

---

## Segmented Follow-Up Actions

| Segment | Automated Action | Owner | Timeline |
|---------|-----------------|-------|----------|
| Detractor (0-3) | Create high-priority follow-up task | Customer Success Manager | Within 24 hours |
| Detractor (4-6) | Add to at-risk watch list | Account Manager | Within 48 hours |
| Passive (7-8) | Tag for engagement campaign | Marketing | Next campaign cycle |
| Promoter (9-10) | Invite to referral program | Marketing | Within 7 days |
| Promoter (9-10) | Request case study participation | Marketing | Quarterly review |

---

## Reporting

### Key Metrics to Track

- **Overall NPS**: Current score and trend vs. previous quarter
- **Response Rate**: Target 20%+ of audience
- **Segment Distribution**: % Promoters, Passives, Detractors
- **Top Themes**: From open text analysis (Q2)
- **Priority Area Distribution**: From Q3 responses
- **NPS by Cohort**: By customer tenure, plan type, industry, region
