# Dashboard Narrator - Reference Guide

## Narrative Language Precision Guide

### Magnitude Calibration

| Change Range | Language Category | Example Phrases |
|---|---|---|
| 0-2% | Flat/Stable | "remained stable," "held steady," "was essentially unchanged" |
| 2-5% | Slight | "edged up," "dipped slightly," "inched higher" |
| 5-10% | Moderate | "increased," "decreased," "showed moderate growth" |
| 10-20% | Notable | "grew significantly," "declined notably," "rose sharply" |
| 20-50% | Strong | "surged," "jumped," "dropped sharply," "fell steeply" |
| >50% | Dramatic | "more than doubled," "plummeted," "skyrocketed" |

### Direction Language

| Direction | Positive Context | Negative Context | Neutral Context |
|---|---|---|---|
| Strong up | "surged," "soared" | "spiked" (cost) | "jumped" |
| Moderate up | "grew," "improved" | "climbed" (cost) | "increased" |
| Slight up | "edged up," "ticked up" | "crept up" (cost) | "rose marginally" |
| Flat | "held steady" | "stagnated" | "remained stable" |
| Slight down | "eased," "softened" | "slipped" | "dipped" |
| Moderate down | "declined," "retreated" | "fell," "dropped" | "decreased" |
| Strong down | "plunged," "collapsed" | "cratered" | "plummeted" |

### Causality Language

| Confidence Level | Language | When to Use |
|---|---|---|
| High (proven cause) | "driven by," "caused by," "resulting from" | A/B test results, known events |
| Medium (strong correlation) | "attributed to," "associated with," "coinciding with" | Timing matches, logical link |
| Low (hypothesis) | "possibly due to," "may be related to," "could reflect" | Speculation, multiple factors |
| Unknown | "the driver is under investigation," "further analysis needed" | No clear explanation |

### Comparison Anchors

Always anchor data to a meaningful comparison:

| Anchor Type | When to Use | Example |
|---|---|---|
| Prior period (MoM) | Monthly reviews | "up 12% from February" |
| Year-over-year (YoY) | Seasonal businesses | "up 8% vs March last year" |
| Target/budget | Performance tracking | "exceeded the Q1 target by 5%" |
| Benchmark | Industry context | "outperformed the industry median of 15%" |
| Historical average | Trend context | "above the 12-month average of $1.1M" |
| Forecast | Expectations | "tracking 3% ahead of the Q2 forecast" |

## Narrative Structures

### The Four-Part Narrative

```
1. HEADLINE: Single most important finding as a statement
2. CONTEXT: Background that explains significance
3. INSIGHT: What the data means beyond the numbers
4. RECOMMENDATION: What to do based on the insight
```

### The Inverted Pyramid

```
Most important finding (lead)
  |
  v
Supporting details and data
  |
  v
Background context
  |
  v
Additional detail (optional, for those who want depth)
```

### The Problem-Evidence-Action Structure

```
PROBLEM: [Metric] is [not meeting expectations / showing concerning trend]
EVIDENCE: [Specific data points with comparisons]
ACTION: [Recommended response with expected impact]
```

## Anomaly Detection Framework

### Statistical Thresholds

| Deviation | Classification | Narrative Treatment |
|---|---|---|
| >3 standard deviations | Critical anomaly | Lead the narrative, investigate immediately |
| 2-3 standard deviations | Warning | Highlight prominently, investigate within 24h |
| 1-2 standard deviations | Notable | Mention in narrative, monitor |
| <1 standard deviation | Normal variation | Do not highlight, omit or footnote |

### Common Anomaly Root Causes

| Category | Examples | Verification Steps |
|---|---|---|
| Data quality | ETL failure, duplicate records, missing data | Check data pipeline, run quality checks |
| Seasonality | Holiday effect, end-of-quarter push | Compare to same period prior year |
| One-time event | Product launch, PR event, outage | Check event calendar and changelog |
| Behavioral shift | New feature adoption, pricing change | Segment by cohort, check feature logs |
| External factor | Market shift, competitor action, regulation | Check news, industry reports |

## Metric Category Narratives

### Revenue Metrics

```
Revenue reached $[X]M in [period], [up/down] [X%] from [comparison].
[Context: This represents the [Nth] consecutive [month/quarter] of
[growth/decline] and [exceeds/falls short of] the target of $[X]M.]

The [X%] change was [primarily/partially] driven by:
- [Driver 1]: [quantified contribution]
- [Driver 2]: [quantified contribution]

[Recommendation based on trajectory]
```

### Customer Metrics

```
[Customer count / NPS / Churn] [reached/came in at] [value] in [period],
[direction] [X%] from [comparison].

Segment analysis reveals:
- [Segment A]: [performance description]
- [Segment B]: [performance description]

[The overall trend suggests / This signals] [insight].
[Recommendation]
```

### Operational Metrics

```
[Uptime / Response time / Error rate] [was/averaged] [value] in [period],
[within/outside] the SLA target of [target].

[If outside SLA]: This represents [duration] of SLA breach, potentially
affecting [N] customers and [X] service credits.

Root cause: [description]
Remediation: [status and timeline]
```

## Dashboard Section Templates

### Executive Summary Section

```
## Overview -- [Period]

**Status: [On Track / At Risk / Off Track]**

**[Bold headline summarizing the most important finding.]**

[2-3 sentences providing context, key drivers, and overall health.]

| Metric | Actual | Target | vs Prior | Status |
|---|---|---|---|---|
| Revenue | $[X]M | $[X]M | [+/-X%] | [G/Y/R] |
| Customers | [N] | [N] | [+/-X%] | [G/Y/R] |
| NPS | [X] | [X] | [+/-X] | [G/Y/R] |
```

### Deep-Dive Section

```
## [Metric Name] -- Deep Dive

**Current: [Value] | Target: [Value] | Status: [G/Y/R]**

[Headline insight paragraph with comparison and driver attribution.]

Trend: [3-6 period description using trend language from reference]

Key drivers:
1. [Driver with quantified impact]
2. [Driver with quantified impact]

Segments:
- [Segment breakdown with notable differences]

**Recommendation:** [Specific action based on the analysis]
```

## Words and Phrases to Avoid

| Avoid | Use Instead | Reason |
|---|---|---|
| "Significantly" (without quantifying) | "by 14%" or "materially" | Imprecise |
| "Relatively" | State the comparison explicitly | Vague |
| "Somewhat" | "by 3%" or remove entirely | Adds no information |
| "Fairly good" | "on target" or quantify | Imprecise |
| "It seems that" | State the finding directly | Undermines confidence |
| "Basically" | Remove entirely | Filler word |
| "In order to" | "To" | Wordier |
| "At this point in time" | "Currently" | Wordier |
| "Due to the fact that" | "Because" | Wordier |
