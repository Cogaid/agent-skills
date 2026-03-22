# Lead Qualifier Reference

## Contents
- ICP Definition
- BANT Framework Deep Dive
- MEDDIC Framework Deep Dive
- Lead Scoring Model
- Qualification Questions
- Pipeline Management

---

## ICP Definition

### ICP Template

```
IDEAL CUSTOMER PROFILE

FIRMOGRAPHICS
- Company Size: [Employee range, e.g., 50-500]
- Revenue: [$X - $Y annually]
- Industry: [Primary industries]
- Geography: [Target regions]
- Stage: [Startup/Growth/Enterprise]

TECHNOGRAPHICS
- Uses: [Required tech/tools]
- Doesn't use: [Competing solutions]
- Maturity: [Tech sophistication level]

SITUATION
- Struggles with: [Problems you solve well]
- Triggered by: [Events that create urgency]
- Growing: [Growth signals that indicate fit]

BUYING BEHAVIOR
- Decision-makers: [Typical titles involved]
- Budget authority: [How decisions get made]
- Buying cycle: [Typical duration]
- Evaluation criteria: [What they prioritize]

RED FLAGS (Disqualifiers)
- [Characteristic that predicts failure]
- [Situation that leads to churn]
- [Buying behavior that wastes time]
```

### ICP Scoring

| Attribute | Perfect Fit (10) | Good Fit (7) | Okay Fit (4) | Poor Fit (0) |
|-----------|------------------|--------------|--------------|--------------|
| Size | [Range] | [Range] | [Range] | [Range] |
| Industry | [List] | [List] | [List] | [Excluded] |
| Geography | [Primary] | [Secondary] | [Tertiary] | [Not served] |
| Tech Stack | [Has X+Y] | [Has X] | [Has Y] | [Neither] |

---

## BANT Framework Deep Dive

### Budget

**Goal**: Confirm they can pay

**Questions**:
- "Have you set aside budget for solving this problem?"
- "What have you spent on similar solutions before?"
- "What's your budget cycle? When do budgets get set?"
- "If we can demonstrate clear ROI, can budget be found?"

**Scoring**:
| Signal | Score |
|--------|-------|
| Budget allocated and confirmed | 10 |
| Budget likely, discussing amounts | 7 |
| Budget possible, needs approval | 4 |
| No budget, no path to budget | 0 |

---

### Authority

**Goal**: Ensure you're talking to (or can reach) decision-makers

**Questions**:
- "Walk me through how a purchase like this gets approved."
- "Who else would need to be involved in this decision?"
- "Have you purchased something similar before? How did that work?"
- "What would your recommendation be, and how much weight does it carry?"

**Scoring**:
| Signal | Score |
|--------|-------|
| Talking to decision-maker | 10 |
| Strong champion with DM access | 7 |
| Influencer, unclear path to DM | 4 |
| No authority, no champion | 0 |

---

### Need

**Goal**: Validate they have a real problem you can solve

**Questions**:
- "What prompted you to look at this now?"
- "What happens if you don't solve this problem?"
- "How long has this been an issue?"
- "What's the business impact of this problem?"

**Scoring**:
| Signal | Score |
|--------|-------|
| Critical problem, quantified impact | 10 |
| Important problem, recognized pain | 7 |
| Nice-to-have, unclear urgency | 4 |
| No real problem | 0 |

---

### Timeline

**Goal**: Understand urgency and buying window

**Questions**:
- "Is there an event driving your timeline?"
- "When do you need to see results?"
- "What else is competing for your team's attention?"
- "If we could start tomorrow, would you?"

**Scoring**:
| Signal | Score |
|--------|-------|
| Active buying, <30 days | 10 |
| Evaluating, 1-3 months | 7 |
| Planning, 3-6 months | 4 |
| No timeline, "someday" | 0 |

---

### BANT Overall Scoring

| Total Score | Classification | Action |
|-------------|----------------|--------|
| 35-40 | Hot | Pursue aggressively |
| 25-34 | Warm | Pursue, address gaps |
| 15-24 | Cool | Nurture, build urgency |
| <15 | Cold | Disqualify or long-term nurture |

---

## MEDDIC Framework Deep Dive

### Metrics

**Goal**: Understand how they'll measure success

**Questions**:
- "How will you measure if this project is successful?"
- "What KPIs are you responsible for?"
- "What would 'good' look like in 6 months?"

**What Good Looks Like**:
- Specific KPIs identified
- Baseline numbers known
- Target improvements defined

---

### Economic Buyer

**Goal**: Identify who actually controls budget

**Questions**:
- "Who ultimately signs off on the budget for this?"
- "Who would need to approve this if it exceeds [threshold]?"
- "Who feels the pain most acutely at the executive level?"

**What Good Looks Like**:
- EB identified by name/title
- Understand EB's priorities
- Path to EB access (direct or via champion)

---

### Decision Criteria

**Goal**: Know what matters in their evaluation

**Questions**:
- "What factors are most important in your decision?"
- "What would make one option stand out over others?"
- "What's a must-have vs. nice-to-have?"

**What Good Looks Like**:
- Criteria explicitly stated
- Prioritized in order of importance
- Your solution matches top criteria

---

### Decision Process

**Goal**: Map the buying journey

**Questions**:
- "Walk me through your typical process for a decision like this."
- "Who needs to be involved at each stage?"
- "What's your timeline for making a decision?"
- "Have you purchased something like this before?"

**What Good Looks Like**:
- Steps clearly defined
- Stakeholders identified at each step
- Timeline attached to steps
- You're aligned to their process

---

### Identify Pain

**Goal**: Quantify the business impact of their problem

**Questions**:
- "What's this problem costing you today?"
- "What happens if you don't solve it?"
- "How does this affect [revenue/efficiency/risk]?"

**What Good Looks Like**:
- Pain quantified in dollars/time
- Impact felt at executive level
- Urgency to solve

---

### Champion

**Goal**: Have an internal advocate

**Questions**:
- "Who internally is most excited about solving this?"
- "Who has the most to gain from success?"
- "Can you help me understand the internal dynamics?"

**What Good Looks Like**:
- Named champion with credibility
- Champion has access to EB
- Champion is actively selling internally

---

### MEDDIC Scoring

| Criteria Strong | Qualification Level |
|-----------------|---------------------|
| 5-6 | Qualified - High probability |
| 3-4 | Developing - Promising but gaps |
| 1-2 | Risky - Significant gaps |
| 0 | Unqualified - Not a real opportunity |

---

## Lead Scoring Model

### Demographic/Firmographic Score

| Attribute | Strong Fit | Moderate | Weak | Disqualifier |
|-----------|------------|----------|------|--------------|
| Company Size | +10 | +5 | +2 | -10 |
| Industry | +10 | +5 | +2 | -10 |
| Geography | +10 | +5 | +2 | -10 |
| Title/Role | +10 | +5 | +2 | -5 |

### Behavioral Score

| Action | Points |
|--------|--------|
| Requested demo | +20 |
| Attended webinar | +10 |
| Downloaded content | +5 |
| Visited pricing page | +15 |
| Multiple site visits | +10 |
| Opened 3+ emails | +5 |
| No engagement 30 days | -10 |

### Score Thresholds

| Score | Classification | Response Time | Owner |
|-------|----------------|---------------|-------|
| 80+ | Hot | <1 hour | Sales |
| 60-79 | Warm | <4 hours | Sales |
| 40-59 | Cool | <24 hours | SDR/Nurture |
| <40 | Cold | Automated | Marketing |

---

## Qualification Questions by Category

### Budget
- "Have you allocated budget for this?"
- "What have you spent on similar solutions?"
- "Who controls this budget?"
- "Is this in this year's plan?"

### Authority
- "How does your team make decisions like this?"
- "Who needs to sign off?"
- "Who would block this if they wanted to?"
- "Can you make this decision yourself?"

### Need
- "What triggered your interest now?"
- "What's the cost of not solving this?"
- "How long has this been a problem?"
- "What happens if nothing changes?"

### Timeline
- "When do you need this solved by?"
- "What's driving that timeline?"
- "What other priorities compete with this?"
- "Is there a hard deadline?"

### Competition
- "What other options are you considering?"
- "Have you used [Competitor] before?"
- "What would make you choose one over another?"

---

## Pipeline Management

### Weekly Review Questions

For each deal:
1. What changed since last week?
2. What's the next step and when?
3. What could derail this deal?
4. Is the timeline still realistic?
5. Should this still be in pipeline?

### Pipeline Hygiene Rules

- **No activity 30+ days**: Review or remove
- **Past expected close**: Requalify or adjust date
- **Missing qualification data**: Complete or downgrade
- **Stuck in stage 60+ days**: Reassess or nurture
- **No champion identified**: Address immediately

### Deal Categories

| Category | Definition | Forecast Weight |
|----------|------------|-----------------|
| Commit | Will close this period | 90% |
| Best Case | Likely with work | 50% |
| Pipeline | Possible, needs development | 20% |
| Upside | Long shot | 5% |
