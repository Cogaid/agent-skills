---
name: kpi-tracker
description: Define, track, and report on key performance indicators across departments. Use when user mentions "KPI," "key performance indicator," "OKR," "metrics tracking," "performance dashboard," "target setting," "scorecard," "business metrics."
metadata:
  version: 1.0.0
  category: data-analytics
---

# KPI Tracker

Define meaningful KPIs, set targets, track performance, and produce structured KPI reports with traffic light scoring and trend analysis.

## Purpose

This skill helps organizations select the right KPIs, set achievable targets, establish review cadences, and produce clear reports that drive accountability and data-informed decisions across all departments.

## Quick Reference

### KPI Selection Framework (SMART Criteria)

| Criterion   | Definition                                | Test Question                              |
|-------------|-------------------------------------------|--------------------------------------------|
| Specific    | Clearly defined, no ambiguity             | Can everyone agree on what this measures?  |
| Measurable  | Quantifiable with available data          | Can we pull this number reliably?          |
| Achievable  | Realistic given resources and constraints | Is the target within reach with effort?    |
| Relevant    | Aligned with strategic objectives         | Does moving this metric advance our goals? |
| Time-bound  | Has a defined measurement period          | When will we evaluate performance?         |

### KPI Quality Checklist

- [ ] The KPI has a clear, documented definition
- [ ] Data source is identified and reliable
- [ ] Measurement frequency is established
- [ ] Target is set with rationale documented
- [ ] Owner is assigned and accountable
- [ ] Leading indicators are identified (not just lagging)
- [ ] The KPI drives behavior that aligns with strategy
- [ ] There are no perverse incentives from optimizing this metric

## Department KPI Libraries

### Sales KPIs

| KPI                        | Definition                                    | Formula                                | Typical Target     |
|----------------------------|-----------------------------------------------|----------------------------------------|--------------------|
| Monthly Recurring Revenue  | Predictable monthly revenue from subscriptions | Sum of all active subscription values  | +X% MoM growth     |
| Annual Recurring Revenue   | Annualized value of recurring revenue          | MRR * 12                               | $X by year-end     |
| Win Rate                   | Deals won / total deals in pipeline            | Won / (Won + Lost) * 100              | 25-35%             |
| Average Deal Size          | Mean revenue per closed deal                   | Total revenue / Number of deals        | $X per deal        |
| Sales Cycle Length         | Average days from opportunity to close         | Sum of cycle days / Number of deals    | <X days            |
| Pipeline Coverage          | Pipeline value vs. quota                       | Pipeline value / Quota                 | 3-4x               |
| Quota Attainment           | Revenue vs. assigned quota                     | Actual / Quota * 100                   | >100%              |
| Customer Acquisition Cost  | Total sales+marketing spend per new customer   | (Sales + Mktg spend) / New customers   | <$X                |

### Marketing KPIs

| KPI                        | Definition                                    | Formula                                | Typical Target     |
|----------------------------|-----------------------------------------------|----------------------------------------|--------------------|
| Marketing Qualified Leads  | Leads meeting marketing criteria               | Count of leads passing MQL score       | X per month        |
| Cost per Lead              | Marketing spend per lead generated             | Total spend / Total leads              | <$X                |
| Conversion Rate            | Visitors who complete desired action            | Conversions / Visitors * 100           | >X%                |
| Customer Lifetime Value    | Total revenue expected from a customer          | ARPU * Avg lifespan                    | >3x CAC            |
| Email Open Rate            | Emails opened / emails delivered                | Opens / Delivered * 100                | >20%               |
| Organic Traffic            | Visitors from non-paid search                   | Count from analytics                   | +X% MoM            |
| Brand Awareness            | Unaided recall in target market                 | Survey-based measurement               | >X%                |
| Return on Ad Spend         | Revenue generated per dollar of ad spend        | Revenue / Ad spend                     | >4x                |

### Customer Support KPIs

| KPI                        | Definition                                    | Formula                                | Typical Target     |
|----------------------------|-----------------------------------------------|----------------------------------------|--------------------|
| First Response Time        | Time from ticket creation to first response     | Avg(first response - created)          | <X hours           |
| Resolution Time            | Time from ticket creation to resolution         | Avg(resolved - created)                | <X hours           |
| First Contact Resolution   | Tickets resolved in first interaction            | FCR tickets / Total tickets * 100     | >70%               |
| Customer Satisfaction      | Post-interaction satisfaction score              | Avg CSAT rating                        | >4.0/5.0           |
| Net Promoter Score         | Likelihood to recommend                          | % Promoters - % Detractors            | >50                |
| Ticket Volume              | Total support requests per period                | Count of tickets                       | Trend downward     |
| Escalation Rate            | Tickets escalated to higher tier                 | Escalated / Total * 100               | <10%               |
| Agent Utilization          | Productive time / available time                 | Handle time / Available time * 100    | 70-80%             |

### Product KPIs

| KPI                        | Definition                                    | Formula                                | Typical Target     |
|----------------------------|-----------------------------------------------|----------------------------------------|--------------------|
| Daily Active Users         | Unique users active per day                     | Count of unique daily sessions         | +X% MoM            |
| Monthly Active Users       | Unique users active per month                   | Count of unique monthly sessions       | +X% MoM            |
| Feature Adoption Rate      | Users who use a specific feature                 | Feature users / Total users * 100     | >X% in 30 days     |
| Retention Rate (D7/D30)    | Users returning after 7 or 30 days              | Returning / Original cohort * 100     | >X%                |
| Churn Rate                 | Customers who cancel in a period                 | Churned / Start count * 100           | <X% monthly        |
| Time to Value              | Time from signup to first value moment           | Avg(value event - signup)              | <X minutes         |
| Error Rate                 | Application errors per session                   | Errors / Sessions * 100               | <0.1%              |
| Page Load Time             | Average time to render page                      | Avg(load complete - request)           | <2 seconds         |

### Engineering KPIs

| KPI                        | Definition                                    | Formula                                | Typical Target     |
|----------------------------|-----------------------------------------------|----------------------------------------|--------------------|
| Deployment Frequency       | How often code is deployed to production        | Deployments per period                 | Daily+             |
| Lead Time for Changes      | Time from commit to production                  | Avg(deploy time - commit time)         | <1 day             |
| Change Failure Rate        | Deployments causing failures                    | Failed deploys / Total deploys * 100  | <15%               |
| Mean Time to Recovery      | Time to restore after a failure                  | Avg(recovery - incident start)         | <1 hour            |
| Sprint Velocity            | Story points completed per sprint                | Sum of completed story points          | Stable +/-10%      |
| Code Review Turnaround     | Time from PR opened to merged                    | Avg(merged - opened)                   | <24 hours          |
| Test Coverage              | Code covered by automated tests                  | Covered lines / Total lines * 100     | >80%               |
| Tech Debt Ratio            | Time on tech debt vs. new features               | Tech debt hours / Total hours * 100   | <20%               |

## Target Setting Methodology

### Approaches

| Method              | When to Use                        | Process                                     |
|---------------------|------------------------------------|---------------------------------------------|
| Historical baseline | Established metrics with data      | Use past performance + growth rate           |
| Benchmarking        | Industry data available            | Set targets relative to peer performance     |
| Top-down            | Executive-driven goals             | Break strategic targets into KPI targets     |
| Bottom-up           | Team-driven planning               | Aggregate team estimates upward              |
| Stretch targets     | Innovation or transformation       | Set aspirational targets 20-30% above base   |

### Target Setting Template

```
KPI TARGET SETTING

KPI: [NAME]
Owner: [NAME, TITLE]
Period: [Q1 2025 / FY 2025]

HISTORICAL PERFORMANCE
| Period    | Actual  | Target  | Attainment |
|-----------|---------|---------|------------|
| Q1 2024   | [Value] | [Value] | [X%]       |
| Q2 2024   | [Value] | [Value] | [X%]       |
| Q3 2024   | [Value] | [Value] | [X%]       |
| Q4 2024   | [Value] | [Value] | [X%]       |

PROPOSED TARGET: [VALUE]
Rationale: [Why this target is appropriate]
Assumptions: [Key assumptions underlying the target]
Risks to target: [What could prevent achievement]
Dependencies: [Resources, projects, or events required]

MILESTONES
| Milestone       | Date       | Checkpoint Value |
|-----------------|------------|------------------|
| Month 1         | [Date]     | [Value]          |
| Month 2         | [Date]     | [Value]          |
| Month 3 (End)   | [Date]     | [Value]          |
```

## Traffic Light Scoring

| Color  | Score Range      | Meaning                              | Action Required             |
|--------|------------------|--------------------------------------|-----------------------------|
| Green  | >= 90% of target | On track or exceeding target         | Continue current approach   |
| Yellow | 70-89% of target | At risk, may miss target             | Investigate, adjust plan    |
| Red    | < 70% of target  | Off track, unlikely to hit target    | Escalate, intervention needed|
| Blue   | > 120% of target | Significantly exceeding              | Validate data, raise target |
| Gray   | No data          | Data not available or not yet due    | Establish data collection   |

## Review Cadence

| Review Type      | Frequency  | Participants              | Duration | Focus                        |
|------------------|------------|---------------------------|----------|------------------------------|
| Daily standup     | Daily      | Team members              | 15 min   | Blockers, daily metrics      |
| Weekly review     | Weekly     | Team lead + team          | 30 min   | Weekly KPIs, action items    |
| Monthly review    | Monthly    | Department head + leads   | 60 min   | Monthly KPIs, trends, risks  |
| Quarterly review  | Quarterly  | Executive + dept heads    | 90 min   | Quarterly KPIs, strategy adj |
| Annual planning   | Annual     | All leadership            | Half day | Target setting, KPI revision |

## KPI Dashboard Template

```
KPI DASHBOARD
Department: [NAME]
Period: [MONTH/QUARTER YEAR]
Last Updated: [DATE]

SUMMARY SCORECARD
| KPI                  | Actual   | Target   | % Attain | Trend  | Status |
|----------------------|----------|----------|----------|--------|--------|
| [KPI 1]              | [Value]  | [Target] | [X%]     | [Up/Dn]| [G/Y/R]|
| [KPI 2]              | [Value]  | [Target] | [X%]     | [Up/Dn]| [G/Y/R]|
| [KPI 3]              | [Value]  | [Target] | [X%]     | [Up/Dn]| [G/Y/R]|
| [KPI 4]              | [Value]  | [Target] | [X%]     | [Up/Dn]| [G/Y/R]|
| [KPI 5]              | [Value]  | [Target] | [X%]     | [Up/Dn]| [G/Y/R]|

OVERALL HEALTH: [X of Y KPIs on track]

HIGHLIGHTS
- [Key win or achievement this period]

CONCERNS
- [KPI at risk with explanation and mitigation]

ACTION ITEMS
| Action                    | Owner    | Deadline   | Status      |
|---------------------------|----------|------------|-------------|
| [Action 1]                | [Name]   | [Date]     | [Status]    |
| [Action 2]                | [Name]   | [Date]     | [Status]    |
```

## KPI Report Template

```
KPI PERFORMANCE REPORT
Period: [MONTH/QUARTER YEAR]
Prepared by: [NAME]
Date: [DATE]

EXECUTIVE SUMMARY
- [X] of [Y] KPIs are on track (green)
- [X] KPIs are at risk (yellow)
- [X] KPIs are off track (red)
- Key theme: [One sentence summary of performance story]

DETAILED PERFORMANCE

[For each KPI:]

### [KPI Name]
- **Current:** [Value] | **Target:** [Value] | **Status:** [G/Y/R]
- **Trend:** [3-period sparkline or direction]
- **Analysis:** [2-3 sentences: what happened, why, what it means]
- **Action:** [What will be done to maintain or improve]

CROSS-CUTTING THEMES
[Patterns that emerge across multiple KPIs]

RECOMMENDATIONS
1. [Recommendation with supporting KPI evidence]
2. [Recommendation with supporting KPI evidence]

NEXT PERIOD OUTLOOK
[Expected trajectory based on leading indicators]
```

## Workflow

1. **Identify strategic objectives**: What does the organization need to achieve
2. **Select KPIs**: Use the department libraries, apply SMART criteria and quality checklist
3. **Set targets**: Apply appropriate target setting methodology
4. **Assign owners**: Each KPI must have a single accountable owner
5. **Establish data sources**: Confirm reliable, automated data collection
6. **Build dashboard**: Create the dashboard using the template
7. **Set review cadence**: Schedule recurring review meetings
8. **Track and report**: Produce KPI reports per the cadence
9. **Adjust**: Retire irrelevant KPIs, add new ones, adjust targets as strategy evolves

## Scripts & Tools

**KPI dashboard generator**:
```bash
scripts/kpi-dashboard.sh --department sales --period "2025-Q1" --output dashboard.md
```

**Target calculator**:
```bash
scripts/target-calc.sh --kpi "mrr" --method historical --growth-rate 10 --output targets.csv
```

**Traffic light scorer**:
```bash
scripts/kpi-score.sh --actuals actuals.csv --targets targets.csv --output scorecard.md
```

**Trend analyzer**:
```bash
scripts/kpi-trends.sh --data kpi-history.csv --periods 12 --output trends.md
```

## Best Practices

- Limit each team or department to 5-8 KPIs. More than that dilutes focus and accountability.
- Balance leading indicators (predictive) with lagging indicators (outcomes).
- Review and retire KPIs that no longer align with strategic priorities.
- Automate data collection to eliminate manual reporting burden and reduce errors.
- Display KPIs publicly within teams to create transparency and shared ownership.
- Set targets collaboratively between top-down strategic needs and bottom-up team input.
- Always pair a metric with its context: a number without a benchmark is just a number.
- Investigate KPIs that are consistently green at 120%+; the target may be too easy.
- Document every KPI definition in a central glossary to prevent interpretation drift.
- When a KPI is red for three consecutive periods, escalate for structural intervention rather than continuing tactical fixes.
