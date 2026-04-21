---
name: dashboard-narrator
description: Narrate dashboard data into written insights and commentary. Use when user mentions "explain this dashboard," "narrate metrics," "data storytelling," "interpret these numbers," "write dashboard commentary," "metric summary," "data narrative."
metadata:
  version: 1.0.0
  category: data-analytics
---

# Dashboard Narrator

Transform dashboard metrics and charts into clear, written narratives that explain what the data means, why it matters, and what to do about it.

## Purpose

This skill converts raw dashboard data into structured written commentary that executives and stakeholders can quickly absorb. It applies consistent frameworks for interpreting metrics, describing trends, flagging anomalies, and recommending actions.

## Quick Reference

### Metric Interpretation Framework

| Metric Movement | Interpretation Steps                                         |
|-----------------|--------------------------------------------------------------|
| Significant increase | 1. Quantify the change  2. Identify the driver  3. Assess sustainability  4. Recommend action |
| Significant decrease | 1. Quantify the change  2. Identify root cause  3. Assess severity  4. Recommend response   |
| Flat / No change     | 1. Note the stability  2. Check if target is met  3. Assess if growth expected  4. Flag stagnation risk |
| Volatile / Erratic   | 1. Identify the range  2. Look for patterns  3. Check data quality  4. Recommend investigation |

### Narrative Strength Levels

| Level    | When to Use                    | Language                             |
|----------|--------------------------------|--------------------------------------|
| Strong   | >2 standard deviations, clear cause | "Revenue surged 34% driven by..."   |
| Moderate | 1-2 standard deviations        | "Revenue increased 12%, primarily due to..." |
| Mild     | Within normal variance         | "Revenue edged up 3%, consistent with..." |
| Neutral  | No meaningful change           | "Revenue remained stable at..."      |
| Caution  | Negative trend emerging        | "Revenue softened 5%, warranting attention..." |
| Alert    | Significant negative deviation | "Revenue declined 22%, requiring immediate..." |

## Trend Description Patterns

### Upward Trends

| Magnitude | Duration    | Pattern Language                                              |
|-----------|-------------|---------------------------------------------------------------|
| Strong    | 3+ periods  | "has sustained strong growth, rising X% over [period]"        |
| Strong    | 1 period    | "jumped sharply by X% in [period], driven by [cause]"         |
| Moderate  | 3+ periods  | "has shown steady improvement, averaging X% growth per [unit]"|
| Moderate  | 1 period    | "increased X% in [period], continuing the upward trajectory"  |
| Slight    | Any         | "edged up X%, though the movement is within normal range"     |

### Downward Trends

| Magnitude | Duration    | Pattern Language                                              |
|-----------|-------------|---------------------------------------------------------------|
| Strong    | 3+ periods  | "has been in sustained decline, falling X% over [period]"     |
| Strong    | 1 period    | "dropped sharply by X% in [period], attributed to [cause]"    |
| Moderate  | 3+ periods  | "has experienced a gradual decline, averaging X% per [unit]"  |
| Moderate  | 1 period    | "decreased X% in [period], reversing the previous trend"      |
| Slight    | Any         | "dipped slightly by X%, remaining within the expected range"  |

### Plateau and Cyclical

| Pattern     | Language                                                        |
|-------------|-----------------------------------------------------------------|
| Plateau     | "has stabilized around [value] for [N] consecutive periods"     |
| Cyclical    | "follows a seasonal pattern, with peaks in [months] and troughs in [months]" |
| Recovery    | "has recovered to [value] after the [period] decline, now at [X]% of pre-decline levels" |
| Inflection  | "appears to be at an inflection point, with [indicator] suggesting [direction]" |

## Anomaly Detection Language

### Anomaly Description Template

```
ANOMALY DETECTED: [Metric Name]

What: [Metric] [direction] by [X%] on [date/period], reaching [value].
     This is [N] standard deviations from the [period] average of [value].

Why (Hypothesis):
  - Primary: [Most likely explanation with supporting evidence]
  - Secondary: [Alternative explanation]
  - Data quality: [Rule out data issues first]

Impact:
  - [Downstream effect 1]
  - [Downstream effect 2]

Recommendation:
  - [Immediate action if needed]
  - [Investigation steps]
  - [Monitoring adjustment]
```

### Anomaly Severity Classification

| Deviation        | Classification | Action Required                   |
|------------------|----------------|-----------------------------------|
| >3 std dev       | Critical       | Immediate investigation and alert |
| 2-3 std dev      | Warning        | Investigate within 24 hours       |
| 1-2 std dev      | Notable        | Monitor, include in next review   |
| <1 std dev       | Normal         | No action needed                  |

## Comparison Templates

### Month-over-Month (MoM)

```
[Metric] [reached/hit/came in at] [value] in [month], [up/down] [X%]
from [prior value] in [prior month]. This [represents/marks] the
[Nth consecutive month of growth/decline | a reversal from | continuation of]
[prior trend description]. The [X%] change was [primarily/partially]
driven by [driver 1] and [driver 2].
```

### Year-over-Year (YoY)

```
Compared to [same month] last year, [metric] is [up/down] [X%],
moving from [prior value] to [current value]. Adjusting for
[seasonality/one-time events/growth factors], the underlying
trend shows [X%] [growth/contraction]. This [outperforms/underperforms]
the [industry/company] target of [X%] by [Y percentage points].
```

### Versus Target

```
[Metric] [achieved/fell short of/exceeded] the [period] target of
[target value], coming in at [actual value] ([X% above/below target]).
[If met]: The team [exceeded/met] target driven by [key factor].
[If missed]: The [X%] gap is [primarily/partially] attributable to
[reason]. [Remediation/acceleration plan] is expected to
[close the gap by / bring performance back to target in] [timeframe].
```

### Versus Benchmark

```
At [value], [metric] [leads/trails] the industry benchmark of
[benchmark value] by [X%]. Relative to our peer group of
[description], this positions us [in the top/bottom quartile |
at the median | above/below average].
```

## Insight Prioritization

| Priority | Criteria                                          | Narrative Treatment              |
|----------|---------------------------------------------------|----------------------------------|
| Lead     | Largest impact, most actionable                   | Open with this, full paragraph   |
| Support  | Reinforces or explains the lead                   | Second paragraph, connected      |
| Context  | Provides necessary background                     | Brief mention, one sentence      |
| Monitor  | Worth tracking but no action needed now            | Footnote or appendix             |
| Omit     | Noise, within normal variance, not actionable      | Do not include                   |

## Narrative Structure

### The Four-Part Narrative

```
1. HEADLINE (1 sentence)
   The single most important takeaway, stated as a finding.
   Example: "March revenue exceeded target by 12%, marking the
   strongest month since Q3 2024."

2. CONTEXT (1-2 sentences)
   Background that helps the reader understand significance.
   Example: "This follows two consecutive months of below-target
   performance and coincides with the launch of the enterprise
   pricing tier."

3. INSIGHT (2-3 sentences)
   What the data means beyond the surface numbers.
   Example: "The growth was concentrated in the enterprise segment,
   which contributed 68% of new ARR. Mid-market growth remained
   flat, suggesting the pricing change has not yet impacted this
   cohort. If the enterprise trend sustains, we are on track to
   hit the Q2 target without mid-market recovery."

4. RECOMMENDATION (1-2 sentences)
   What to do based on the insight.
   Example: "Recommend doubling enterprise sales capacity in Q2
   while launching a targeted campaign for mid-market reactivation."
```

### Dashboard Section Narrative Template

```
## [Section Title] — [Period]

**Status: [On Track / At Risk / Off Track]**

[Headline insight in bold.]

[2-3 sentences of context and analysis using comparison templates above.]

| Metric          | Actual   | Target   | vs Prior | Status |
|-----------------|----------|----------|----------|--------|
| [Metric 1]      | [Value]  | [Target] | [+/-X%]  | [G/Y/R]|
| [Metric 2]      | [Value]  | [Target] | [+/-X%]  | [G/Y/R]|
| [Metric 3]      | [Value]  | [Target] | [+/-X%]  | [G/Y/R]|

[Insight paragraph explaining the "so what" of these numbers.]

**Recommendation:** [Specific action based on the data.]
```

## Workflow

1. **Receive dashboard data**: Ingest metrics, charts, or raw numbers
2. **Identify top metrics**: Rank by deviation from target or prior period
3. **Classify movements**: Use the narrative strength levels to calibrate language
4. **Detect anomalies**: Flag any metric outside normal variance
5. **Build comparisons**: Apply MoM, YoY, vs target, vs benchmark templates
6. **Prioritize insights**: Use the prioritization matrix
7. **Draft narrative**: Apply the four-part structure for each section
8. **Review language**: Ensure precision, avoid hedging on clear signals
9. **Deliver commentary**: Attach to dashboard or deliver as standalone briefing

## Scripts & Tools

**Generate narrative from data**:
```bash
scripts/dashboard-narrate.sh --data metrics.csv --period "2025-03" --output narrative.md
```

**Anomaly detector**:
```bash
scripts/anomaly-detect.sh --data metrics.csv --sensitivity 2 --output anomalies.json
```

**Comparison generator**:
```bash
scripts/compare-periods.sh --current "2025-03" --prior "2025-02" --yoy "2024-03" --output comparison.md
```

## Best Practices

- Always lead with the insight, not the data point. Say "Revenue beat target by 12%" before "Revenue was $1.2M."
- Use precise language: "increased 14%" is better than "increased significantly."
- Avoid weasel words: "somewhat," "relatively," "fairly" add noise without information.
- Calibrate language to magnitude: a 2% change should not get the same language as a 20% change.
- Attribute causality carefully: say "correlated with" unless you have causal evidence.
- Include the comparison basis: "+12%" is meaningless without "vs. prior month" or "vs. target."
- Write for scanning: bold the headline, keep paragraphs under 4 sentences.
- Update narrative templates when new metrics or KPIs are added to dashboards.
- Maintain a consistent voice and format across all dashboard narratives for familiarity.
