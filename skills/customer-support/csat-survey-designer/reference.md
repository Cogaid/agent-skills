# CSAT Survey Designer - Reference Guide

## Survey Methodology Deep Dive

### CSAT (Customer Satisfaction Score)

**Definition**: A transactional metric that measures customer satisfaction with a specific interaction, product, or service on a numeric scale.

**Calculation**:
```
CSAT % = (Number of satisfied responses / Total responses) x 100
```
Where "satisfied" typically means 4 or 5 on a 5-point scale.

**When to Use**:
- After a support interaction (call, chat, email)
- After a purchase or delivery
- After onboarding completion
- After a feature release

**Advantages**:
- Simple and universally understood
- Directly tied to specific interactions
- Easy to benchmark across industries
- High response rates due to simplicity

**Limitations**:
- Recency bias (reflects mood at survey time)
- Does not predict long-term loyalty
- Cultural differences in scale usage (some cultures avoid extremes)
- Ceiling effect in high-performing organizations

---

### NPS (Net Promoter Score)

**Definition**: A relationship metric that measures customer loyalty by asking how likely they are to recommend the company on a 0-10 scale.

**Calculation**:
```
NPS = % Promoters (9-10) - % Detractors (0-6)
Range: -100 to +100
```

**Segment Definitions**:
| Segment | Score Range | Behavior Pattern |
|---------|------------|------------------|
| Detractors | 0-6 | At risk of churning; may share negative word-of-mouth |
| Passives | 7-8 | Satisfied but unenthusiastic; vulnerable to competitors |
| Promoters | 9-10 | Loyal enthusiasts who drive referrals and growth |

**Industry Benchmarks**:
| Industry | Average NPS | Top Quartile |
|----------|------------|-------------|
| SaaS / Technology | 30-40 | 55+ |
| E-commerce / Retail | 35-45 | 60+ |
| Financial Services | 20-35 | 50+ |
| Telecommunications | 10-25 | 40+ |
| Healthcare | 25-40 | 55+ |
| Airlines / Travel | 15-30 | 45+ |

**When to Use**:
- Quarterly relationship check-ins
- Annual strategic planning input
- Post-major-release sentiment tracking
- Board-level reporting metric

---

### CES (Customer Effort Score)

**Definition**: A metric that measures how easy it was for a customer to accomplish a task or resolve an issue on a 1-7 agree/disagree scale.

**Calculation**:
```
CES = Sum of all scores / Number of responses
Target: 5.0+ on 7-point scale
```

**The Effortless Experience Framework**:
Research by the Corporate Executive Board (now Gartner) found that reducing customer effort is the strongest predictor of future loyalty -- stronger than delight or satisfaction.

**High-Effort Indicators**:
- Multiple contacts to resolve one issue
- Channel switching (started on chat, had to call)
- Repeating information to different agents
- Confusing self-service options
- Long hold or wait times

**Low-Effort Indicators**:
- First contact resolution
- Proactive issue notification
- Seamless channel transitions with context preserved
- Clear, jargon-free communication
- Self-service success

---

## Question Design Principles

### The BRUSO Framework

Every survey question should be evaluated against five criteria:

| Criterion | Definition | Bad Example | Good Example |
|-----------|-----------|-------------|--------------|
| **B**rief | Short and to the point | "Thinking about your most recent interaction with our customer support team, including all the steps you went through..." | "How satisfied were you with today's support?" |
| **R**elevant | Connected to the survey goal | "How do you feel about our brand colors?" (in a support survey) | "Was your issue fully resolved?" |
| **U**nambiguous | One clear interpretation | "Was the agent nice and helpful?" | "How helpful was the agent?" |
| **S**pecific | Focused on one concept | "How was the speed and quality?" | "How would you rate the response speed?" |
| **O**bjective | Neutral, no leading language | "How excellent was your experience?" | "How would you rate your experience?" |

### Scale Design Guidelines

**5-Point Likert Scale (CSAT)**:
```
1 - Very Dissatisfied
2 - Dissatisfied
3 - Neutral
4 - Satisfied
5 - Very Satisfied
```
Best for: Quick transactional surveys. Familiar to respondents. Sufficient granularity for most use cases.

**7-Point Likert Scale (CES)**:
```
1 - Strongly Disagree
2 - Disagree
3 - Somewhat Disagree
4 - Neither Agree nor Disagree
5 - Somewhat Agree
6 - Agree
7 - Strongly Agree
```
Best for: Effort measurement. More granularity allows detection of smaller shifts.

**11-Point Scale (NPS)**:
```
0 - Not at all likely
...
10 - Extremely likely
```
Best for: Loyalty measurement. The 0-10 scale is the NPS standard and should not be modified.

### Conditional Branching Logic

Branching reduces survey fatigue by showing relevant follow-ups only:

```
IF rating <= 3 (Dissatisfied):
  -> Show: "What could we have done better?" (open text)
  -> Show: "Which area needs improvement?" (multi-select)

IF rating == 4 (Neutral):
  -> Show: "What would make this a 5?" (open text)

IF rating == 5 (Satisfied):
  -> Show: "What did you appreciate most?" (open text)
  -> Show: "Would you recommend us?" (yes/no)
```

---

## Response Rate Optimization

### Factors That Increase Response Rates

| Factor | Impact | Implementation |
|--------|--------|---------------|
| Timing | +10-20% | Send within optimal window for channel |
| Brevity | +15-25% | Keep under 3 questions for transactional |
| Personalization | +5-10% | Use customer name, reference interaction |
| Progress indicator | +5-8% | Show "Question 1 of 3" |
| Mobile optimization | +10-15% | Large tap targets, single-column layout |
| Incentives | +15-30% | Prize draws, discount codes (use sparingly) |
| Brand trust | +5-10% | Explain how feedback is used |
| Follow-up proof | +5-15% | Show "You said X, we did Y" campaigns |

### Factors That Decrease Response Rates

| Factor | Impact | Mitigation |
|--------|--------|-----------|
| Survey fatigue | -20-40% | Enforce frequency caps (1 per 30 days) |
| Poor timing | -15-25% | A/B test send times |
| Too many questions | -5-10% per extra question | Ruthlessly prioritize |
| No mobile support | -30-50% of mobile users | Responsive design mandatory |
| Broken surveys | -100% of affected users | Test every flow before launch |

---

## Statistical Analysis

### Sample Size Requirements

To detect meaningful differences with 95% confidence:

| Desired Margin of Error | Required Sample Size |
|------------------------|---------------------|
| +/- 1% | ~9,600 |
| +/- 2% | ~2,400 |
| +/- 3% | ~1,067 |
| +/- 5% | ~384 |
| +/- 10% | ~96 |

### Trend Analysis

**Moving Average**: Use a 4-week rolling average to smooth out weekly noise while detecting real trends.

**Statistical Significance Testing**:
- For CSAT/CES: Two-sample t-test to compare periods
- For NPS: Chi-squared test on promoter/passive/detractor proportions
- Minimum period: 2 weeks or 200 responses per comparison group

### Text Analysis for Open-Ended Responses

**Theme Categorization Framework**:
1. Agent behavior (empathy, knowledge, professionalism)
2. Process friction (wait times, transfers, repeating info)
3. Resolution quality (completeness, accuracy, speed)
4. Product/service issues (bugs, missing features, pricing)
5. Communication quality (clarity, tone, follow-up)

---

## Survey Channel Specifications

### In-App Popup
- Max questions: 2-3
- Format: Bottom-sheet or modal
- Dismiss behavior: Easy close, do not re-show for 30 days
- Accessibility: Screen reader compatible, keyboard navigable

### Email Survey
- Subject line: Include purpose, keep under 50 characters
- Preview text: Show the question itself
- Embed first question: Clickable stars/numbers in email body
- Fallback: Link to web form if email client blocks interactive elements

### SMS Survey
- Max length: 160 characters for initial message
- Response format: Reply with a number (e.g., "Reply 1-5")
- Opt-out: Always include STOP instructions
- Compliance: TCPA (US), GDPR (EU) consent required

### Post-Chat Embedded
- Trigger: On chat close event
- Format: Inline within chat widget
- Timeout: Auto-dismiss after 5 minutes if no response
- Persistence: Do not block the user from closing the chat

---

## Compliance and Privacy

### GDPR Considerations
- Obtain explicit consent before collecting survey data
- State purpose of data collection
- Provide option to delete survey responses
- Do not tie survey responses to PII without consent
- Data retention: Define and enforce retention period

### Accessibility (WCAG 2.1 AA)
- All form elements must have labels
- Color is not the only indicator (use icons/text too)
- Minimum tap target: 44x44px
- Screen reader compatibility for all question types
- Keyboard navigation support
