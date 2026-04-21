# Report Generator - Reference Guide

## Report Design Frameworks

### The Pyramid Principle (Barbara Minto)

Structure all communication top-down:

1. **Answer first:** Lead with the conclusion or recommendation
2. **Group arguments:** Organize supporting points into logical groups
3. **Logical ordering:** Arrange within groups by time, structure, or importance
4. **Mutual exclusivity:** Groups should not overlap (MECE principle)

### SCQA Framework (Situation, Complication, Question, Answer)

| Component | Purpose | Example |
|---|---|---|
| Situation | Establish shared context | "Q1 revenue grew 15% YoY, ahead of plan" |
| Complication | Identify the tension | "However, CAC increased 40% in March" |
| Question | Frame what needs answering | "Is the CAC spike temporary or structural?" |
| Answer | Provide the insight and recommendation | "Analysis shows 70% is platform migration cost; recommend continuing" |

### The So-What Test

Every data point in a report should pass this test:

```
Data Point -> So What? -> Therefore... -> Recommendation

Example:
  NPS dropped from 52 to 41
  -> So what? Customer satisfaction is declining significantly
  -> Therefore, churn risk is elevated for next quarter
  -> Recommendation: Launch customer success intervention for detractors
```

## Data Visualization Reference

### Chart Type Decision Tree

```
What are you comparing?
|
+-- Over time? -> Line chart (continuous) or Bar chart (discrete periods)
|
+-- Among items? -> Bar chart (horizontal if many items, vertical if few)
|
+-- Part of whole? -> Pie chart (<=5 parts) or Stacked bar (>5 or over time)
|
+-- Relationship? -> Scatter plot (2 variables) or Bubble chart (3 variables)
|
+-- Distribution? -> Histogram (one variable) or Box plot (compare groups)
|
+-- Geographic? -> Map / Choropleth
|
+-- Single KPI? -> Scorecard / Big number with trend indicator
```

### Color Palette Best Practices

| Use Case | Colors | Notes |
|---|---|---|
| Sequential data | Single hue, light to dark | Revenue over time |
| Diverging data | Two hues from center | Profit/loss, above/below target |
| Categorical data | Distinct hues | Product lines, regions |
| Status indicators | Green/Yellow/Red | KPI health, traffic lights |
| Emphasis | Gray base + one accent | Highlight one data series |

### Formatting Standards

| Element | Standard | Example |
|---|---|---|
| Currency | Symbol + comma separators | $1,234,567 |
| Percentage | One decimal place | 12.5% |
| Large numbers | Abbreviate with K/M/B | $1.2M, 450K users |
| Dates | Consistent format | Jan 2025, Q1 2025 |
| Trend arrows | Unicode or emoji | Up, Down, Flat |
| Delta/change | +/- with percentage | +12.3%, -5.1% |

## Report Type Specifications

### Weekly Operations Report

| Section | Content | Length |
|---|---|---|
| TLDR | 2-3 sentence summary | 50 words |
| Metrics dashboard | 5-8 key metrics with WoW change | 1 table |
| Completed this week | Deliverables and milestones hit | 3-5 bullets |
| Blockers and issues | Active problems with status | 2-4 bullets |
| Priorities next week | Top focus areas | 3-5 bullets |

### Monthly Business Review

| Section | Content | Length |
|---|---|---|
| Executive summary | Key wins, risks, decisions needed | 1 page |
| Financial summary | Revenue, expenses, margin vs budget | 1 table + narrative |
| Department deep-dives | Each department's KPIs and highlights | 1-2 pages per dept |
| Customer metrics | NPS, churn, expansion, pipeline | 1 page |
| Product metrics | Usage, adoption, feature performance | 1 page |
| Outlook | Forward-looking projections | 0.5 page |

### Quarterly Board Report

| Section | Content | Length |
|---|---|---|
| Strategic overview | Progress against company OKRs | 2 pages |
| Financial performance | P&L, cash flow, runway | 3-4 pages |
| Growth metrics | ARR, customer count, pipeline | 2 pages |
| Product and technology | Roadmap progress, tech debt | 2 pages |
| Team and organization | Headcount, hiring, retention | 1 page |
| Competitive landscape | Market position, threats | 1 page |
| Risk register | Top 5 risks with mitigations | 1 page |
| Ask of the board | Decisions needed, advice sought | 1 page |

## Statistical Concepts for Reports

### Significance and Confidence

| Concept | Definition | When to Use |
|---|---|---|
| Statistical significance | p < 0.05, result unlikely due to chance | A/B test results, survey comparisons |
| Confidence interval | Range likely containing true value | Survey results, estimates |
| Sample size | Number of observations | Survey responses, experiment participants |
| Effect size | Magnitude of the difference | Comparing before/after, A vs B |
| Correlation | Strength of linear relationship (-1 to 1) | Identifying relationships between metrics |

### Common Statistical Pitfalls

| Pitfall | Description | Prevention |
|---|---|---|
| Survivorship bias | Only analyzing successes | Include churned/failed data |
| Simpson's paradox | Trend reverses when data is grouped | Always segment data |
| Regression to mean | Extreme values naturally return to average | Use longer time periods |
| Correlation vs causation | Assuming X causes Y because they correlate | Use controlled experiments |
| Cherry-picking | Selecting only favorable data ranges | Use consistent time periods |
| Small sample size | Drawing conclusions from too few data points | Report confidence intervals |

## Data Source Quality Checklist

- [ ] Source system is documented and version-tracked
- [ ] Data extraction logic is automated and repeatable
- [ ] Last refresh timestamp is known and within acceptable range
- [ ] Missing data is identified and handling approach documented
- [ ] Outliers are identified and treatment documented
- [ ] Metric definitions match across all report types
- [ ] Historical data is available for trend analysis
- [ ] Data transformations are documented and auditable
