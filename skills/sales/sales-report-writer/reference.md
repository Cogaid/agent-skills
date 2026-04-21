# Sales Report Writer Reference

Detailed reference documentation for generating pipeline, forecast, and performance reports.

## Sales Metrics Deep Dive

### Pipeline Metrics

| Metric | Formula | What It Tells You | Healthy Range |
|--------|---------|-------------------|---------------|
| **Pipeline Coverage** | Total Pipeline / Quota | Whether you have enough pipeline to hit quota | 3-4x quota |
| **Weighted Pipeline** | Sum(Deal Value x Probability) | Probability-adjusted pipeline value | 1.2-1.5x quota |
| **Pipeline Velocity** | (Opps x Win Rate x ACV) / Cycle | Revenue generation speed | Track trend |
| **Stage Distribution** | % of pipeline in each stage | Pipeline shape and health | Balanced funnel |
| **Pipeline Age** | Days since opportunity created | Stale deal identification | <2x avg cycle |
| **Pipeline Created** | New pipeline added in period | Leading indicator of future revenue | Track to target |
| **Pipeline Sourced by Marketing** | Marketing-sourced pipeline / Total | Marketing contribution | 40-60% |
| **Net New Pipeline** | Created - Closed Won - Closed Lost - Removed | Pipeline growth/shrinkage | Positive |

### Forecast Categories and Definitions

Standardize these definitions across the entire sales organization:

| Category | Probability | Criteria | Example |
|----------|------------|----------|---------|
| **Closed Won** | 100% | Signed contract, PO received | Deal is done |
| **Commit** | >80% | Decision maker engaged, timeline confirmed, budget approved, verbal yes | "They said yes, contract in legal" |
| **Best Case** | 50-80% | Champion identified, budget allocated, active evaluation | "We are in final evaluation with strong champion" |
| **Pipeline** | 20-50% | Qualified opportunity, discovery complete | "Good fit, early stage engagement" |
| **Upside** | <20% | Early stage, not yet fully qualified | "Interesting lead, needs qualification" |

### Forecast Accuracy Measurement

| Metric | Formula | Target |
|--------|---------|--------|
| **Forecast Accuracy** | 1 - abs(Forecast - Actual) / Actual | >85% |
| **Forecast Bias** | (Forecast - Actual) / Actual | Within +/-10% |
| **Commit Accuracy** | Commit that closed / Total Commit | >80% |
| **Best Case Conversion** | Best Case that closed / Total Best Case | 40-60% |
| **Week-over-Week Variance** | Change in forecast from prior week | Decreasing over quarter |

## Report Design Principles

### Audience-Specific Reporting

| Audience | Focus | Detail Level | Frequency | Key Questions Answered |
|----------|-------|-------------|-----------|----------------------|
| **Sales Reps** | Deal-level activity and pipeline | High detail | Daily/Weekly | "What should I work on today?" |
| **Sales Managers** | Team performance, pipeline health | Deal + summary | Weekly | "Is my team on track? Where do I coach?" |
| **VP of Sales** | Forecast, team comparisons | Summary + exceptions | Weekly/Monthly | "Will we hit the number? Where are the risks?" |
| **CFO/CEO** | Revenue, efficiency, growth | Executive summary | Monthly/Quarterly | "Are we growing efficiently?" |
| **Board** | Strategic metrics, trends | High-level + narrative | Quarterly | "Is the business model working?" |

### Data Quality Checklist

Before generating any report, validate:

| Check | What to Look For | Impact if Missed |
|-------|-----------------|-----------------|
| **Missing close dates** | Opportunities without expected close | Forecast inaccuracy |
| **Stale opportunities** | No activity in >30 days | Inflated pipeline |
| **Missing amounts** | $0 or blank deal values | Pipeline miscalculation |
| **Wrong stage** | Stage does not match last activity | Incorrect stage distribution |
| **Duplicate records** | Same deal entered twice | Double-counted pipeline |
| **Missing contacts** | No decision maker or champion | Risk assessment gaps |
| **Outdated forecast category** | Commit that should be downgraded | Forecast over-projection |

## Sales Funnel Analysis Framework

### Stage-by-Stage Conversion Benchmarks

| Stage Transition | Healthy Conversion Rate | Warning Threshold |
|-----------------|------------------------|------------------|
| Lead to Qualified | 15-25% | <10% |
| Qualified to Discovery | 60-75% | <50% |
| Discovery to Proposal | 50-65% | <40% |
| Proposal to Negotiation | 60-75% | <50% |
| Negotiation to Closed Won | 70-85% | <60% |
| Overall Lead to Close | 3-8% | <2% |

### Funnel Shape Analysis

| Shape | Description | Diagnosis | Action |
|-------|------------|-----------|--------|
| **Healthy funnel** | Wider at top, steadily narrows | Working well | Maintain cadence |
| **Top-heavy** | Many early stage, few late stage | Qualification or progression issue | Improve discovery, tighten qualification |
| **Bottom-heavy** | Few early stage, deals stacking late | Pipeline generation problem | Increase prospecting and marketing |
| **Hourglass** | Wide top and bottom, thin middle | Stage skipping or stale mid-funnel | Audit stage criteria, enforce progression |
| **Inverted** | More late stage than early | Future pipeline risk | Urgent pipeline generation needed |

## Activity Metrics Framework

### Activity-to-Outcome Ratios

Track these ratios to diagnose performance issues:

| Ratio | Formula | Benchmark | Diagnostic Value |
|-------|---------|-----------|-----------------|
| **Calls to Meetings** | Meetings booked / Calls made | 5-15% | Measures messaging effectiveness |
| **Meetings to Opportunities** | Opps created / Meetings held | 20-40% | Measures qualification skill |
| **Emails to Replies** | Replies / Emails sent | 5-15% | Measures email quality |
| **Demos to Proposals** | Proposals sent / Demos given | 40-60% | Measures demo effectiveness |
| **Proposals to Close** | Closed won / Proposals sent | 25-40% | Measures proposal and negotiation skill |

### Rep Performance Segmentation

Segment reps for targeted coaching:

| Segment | Characteristics | Coaching Focus |
|---------|----------------|---------------|
| **Stars** (top 20%) | High activity, high conversion | Stretch goals, mentoring others |
| **Core** (middle 60%) | Adequate activity, adequate conversion | Specific skill development |
| **Ramping** | New hires, building pipeline | Activity targets, process adherence |
| **Coaching needed** | Low activity OR low conversion | Diagnose root cause, structured plan |
| **High activity / low conversion** | Lots of effort, poor results | Quality over quantity, skill training |
| **Low activity / high conversion** | Efficient but limited output | Increase activity to maximize potential |

## Territory and Segment Analysis

### Territory Health Metrics

| Metric | Formula | What It Reveals |
|--------|---------|----------------|
| **Coverage ratio** | Accounts assigned / Total addressable | How much whitespace remains |
| **Penetration rate** | Active customers / Total accounts | Current market share in territory |
| **Engagement rate** | Accounts with activity / Total accounts | How actively territory is worked |
| **Revenue per account** | Revenue / Active customers | Account monetization efficiency |
| **Growth rate** | (Current period - Prior period) / Prior period | Territory momentum |
| **Churn rate** | Lost customers / Starting customers | Territory retention health |

### Segment Comparison Framework

| Dimension | Enterprise | Mid-Market | SMB |
|-----------|-----------|-----------|-----|
| **Typical ACV** | $100K+ | $25K-$100K | <$25K |
| **Sales cycle** | 6-12 months | 3-6 months | 1-3 months |
| **Decision makers** | 5-10 stakeholders | 2-4 stakeholders | 1-2 stakeholders |
| **Win rate** | 15-25% | 25-35% | 30-45% |
| **Churn rate** | 5-10% annually | 10-15% annually | 15-25% annually |
| **CAC** | Higher | Moderate | Lower |
| **LTV:CAC** | 5-10x | 3-5x | 2-4x |

## Visualization Best Practices

### Chart Type Selection

| Data Type | Best Chart | When to Use |
|-----------|-----------|-------------|
| **Trend over time** | Line chart | Revenue, pipeline, win rate over quarters |
| **Part of whole** | Stacked bar or pie | Pipeline by stage, revenue by segment |
| **Comparison** | Grouped bar chart | Rep performance, territory comparison |
| **Distribution** | Histogram | Deal size distribution, cycle length distribution |
| **Correlation** | Scatter plot | Activity vs. revenue, deal size vs. cycle length |
| **Funnel** | Funnel chart | Stage conversion, lead-to-close flow |
| **KPI status** | Gauge or traffic light | Quota attainment, forecast accuracy |
| **Waterfall** | Waterfall chart | Pipeline changes (added, moved, closed) |

### Dashboard Layout Principles

1. **Most important metrics at top-left** -- The eye starts there
2. **Group related metrics** -- Pipeline, forecast, and activity in logical sections
3. **Show trend context** -- Never show a number without comparison (prior period, target)
4. **Use consistent color coding** -- Green for on-track, yellow for at-risk, red for off-track
5. **Limit to 6-8 visualizations per page** -- Avoid dashboard overload
6. **Include a narrative section** -- Numbers need interpretation

## Report Automation Guide

### Automated Report Cadence

| Report | Frequency | Trigger | Distribution |
|--------|-----------|---------|-------------|
| **Daily pipeline snapshot** | Daily | 6:00 AM | Slack channel |
| **Weekly pipeline review** | Monday AM | Start of week | Email to managers |
| **Weekly forecast update** | Friday PM | End of week | Email to VP Sales + CFO |
| **Monthly business review** | 1st of month | Month close | Email to leadership |
| **Quarterly board report** | End of quarter | Quarter close | Board portal |

### Data Refresh and Lag

| Data Source | Typical Refresh | Lag | Mitigation |
|-------------|----------------|-----|-----------|
| **CRM (Salesforce, HubSpot)** | Real-time to daily | 0-24 hours | Schedule reports after sync |
| **Marketing automation** | Daily | 24-48 hours | Note lag in report |
| **Finance/billing** | Daily to weekly | 1-7 days | Use CRM for leading indicators |
| **Customer success** | Weekly | Up to 7 days | Note "as of" date |
