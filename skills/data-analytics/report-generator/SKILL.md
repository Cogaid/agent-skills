---
name: report-generator
description: Create data-driven reports with insights and visualizations. Use when user mentions "generate report," "data report," "business review," "executive summary," "weekly report," "monthly report," "quarterly report," "board report."
metadata:
  version: 1.0.0
  category: data-analytics
---

# Report Generator

Create structured, data-driven reports with clear insights, appropriate visualizations, and actionable recommendations for various audiences and cadences.

## Purpose

This skill produces reports that transform raw data into meaningful narratives. It supports weekly operations reports, monthly business reviews, quarterly board decks, and ad-hoc analysis reports, adapting depth and language to the target audience.

## Quick Reference

### Report Types

| Type                    | Audience        | Cadence    | Length     | Focus                           |
|-------------------------|-----------------|------------|------------|----------------------------------|
| Weekly Ops Report       | Team leads      | Weekly     | 2-4 pages  | Metrics, blockers, priorities    |
| Monthly Business Review | Department heads| Monthly    | 8-15 pages | Trends, performance vs targets   |
| Quarterly Board Report  | Board/investors | Quarterly  | 15-25 pages| Strategy, financials, outlook    |
| Ad-Hoc Analysis         | Requestor       | As needed  | 3-10 pages | Specific question or hypothesis  |
| Annual Review           | All stakeholders| Annual     | 20-40 pages| Year in review, next year plan   |

### Audience Adaptation Guide

| Audience       | Jargon Level | Detail Level | Viz Preference       | Action Orientation |
|----------------|--------------|--------------|----------------------|--------------------|
| Executive/Board| None         | High-level   | Charts, scorecards   | Strategic decisions|
| Department Head| Some         | Moderate     | Dashboards, trends   | Resource allocation|
| Team Lead      | Full         | Detailed     | Tables, drill-downs  | Tactical actions   |
| Technical Team | Full         | Granular     | Raw data, logs       | Implementation     |
| External Client| None         | Summary      | Polished charts      | Partnership value  |

## Report Structure Template

```
REPORT TITLE
Report Period: [START DATE] to [END DATE]
Prepared by: [AUTHOR]
Date: [DATE]
Distribution: [AUDIENCE]
Classification: [Internal / Confidential / Public]

---

1. EXECUTIVE SUMMARY
   [3-5 bullet points: key wins, key risks, key decisions needed]

   Overall Status: [On Track / At Risk / Off Track]

   Key Metrics Snapshot:
   | Metric          | Current  | Target   | vs Prior Period | Status |
   |-----------------|----------|----------|-----------------|--------|
   | [Metric 1]      | [Value]  | [Target] | [+/-X%]         | [G/Y/R]|
   | [Metric 2]      | [Value]  | [Target] | [+/-X%]         | [G/Y/R]|
   | [Metric 3]      | [Value]  | [Target] | [+/-X%]         | [G/Y/R]|

2. PERFORMANCE ANALYSIS
   2.1 [Area 1]: Detailed metrics with context
   2.2 [Area 2]: Detailed metrics with context
   2.3 [Area 3]: Detailed metrics with context

3. TRENDS AND PATTERNS
   - Period-over-period comparisons
   - Seasonal adjustments
   - Leading indicator analysis

4. INSIGHTS AND OBSERVATIONS
   [What the data tells us, not just what the numbers are]

5. RISKS AND ISSUES
   | Risk/Issue       | Impact | Likelihood | Mitigation            | Owner  |
   |------------------|--------|------------|-----------------------|--------|
   | [Risk 1]         | H/M/L  | H/M/L      | [Action]              | [Name] |
   | [Risk 2]         | H/M/L  | H/M/L      | [Action]              | [Name] |

6. RECOMMENDATIONS
   - [Action 1]: [Rationale based on data]
   - [Action 2]: [Rationale based on data]
   - [Action 3]: [Rationale based on data]

7. OUTLOOK
   [Forward-looking projections based on current trends]

8. APPENDIX
   A. Methodology and data sources
   B. Detailed data tables
   C. Glossary of terms
```

## Data Visualization Guidelines

### Chart Selection Framework

| Data Relationship     | Best Chart Type          | Avoid                   |
|-----------------------|--------------------------|-------------------------|
| Trend over time       | Line chart               | Pie chart               |
| Part of whole         | Stacked bar, pie (<=6)   | Line chart              |
| Comparison            | Bar chart (horizontal)   | Area chart              |
| Distribution          | Histogram, box plot      | Pie chart               |
| Correlation           | Scatter plot             | Bar chart               |
| Geographic            | Map/choropleth           | Table                   |
| Composition over time | Stacked area chart       | Multiple pie charts     |
| Ranking               | Horizontal bar chart     | Vertical bar (many)     |
| KPI status            | Scorecard, gauge         | Complex charts          |

### Visualization Best Practices

| Do                                    | Do Not                               |
|---------------------------------------|---------------------------------------|
| Start Y-axis at zero for bar charts   | Truncate axes to exaggerate change    |
| Use consistent color coding           | Use more than 6-7 colors             |
| Label axes and units clearly          | Rely on legends for critical info     |
| Include data source and date          | Present data without context          |
| Annotate key data points              | Add decorative 3D effects            |
| Use the same scale for comparisons    | Compare different scales side-by-side |

## Insight Writing Framework

### The SCQA Framework (Situation, Complication, Question, Answer)

```
SITUATION: [What is the current state or context]
COMPLICATION: [What changed, what is the tension]
QUESTION: [What does this mean for us]
ANSWER: [What should we do about it]

Example:
SITUATION: Customer acquisition cost has been steady at $45 for 6 months.
COMPLICATION: CAC increased 32% to $59 in March following the new ad platform migration.
QUESTION: Is this a temporary transition cost or a structural increase?
ANSWER: Analysis shows 80% of the increase is due to learning-phase inefficiency.
         Recommend maintaining current spend for 4 more weeks; model projects
         CAC will return to $48-52 range by week 6.
```

### Insight Quality Checklist

- [ ] States the "so what," not just the "what"
- [ ] Quantifies the impact (dollars, percentages, time)
- [ ] Compares to a meaningful benchmark (target, prior period, competitor)
- [ ] Identifies causality or at least correlation
- [ ] Leads to a specific, actionable recommendation
- [ ] Acknowledges uncertainty or caveats where appropriate

## Executive Summary Format

```
EXECUTIVE SUMMARY

HEADLINE: [One sentence capturing the most important takeaway]

KEY WINS
- [Achievement 1 with quantified impact]
- [Achievement 2 with quantified impact]

KEY RISKS
- [Risk 1 with potential impact and mitigation status]
- [Risk 2 with potential impact and mitigation status]

DECISIONS NEEDED
- [Decision 1: context + options + recommendation]
- [Decision 2: context + options + recommendation]

OUTLOOK: [1-2 sentences on expected trajectory]
```

## Report Types: Detailed Formats

### Weekly Ops Report

```
WEEKLY OPERATIONS REPORT
Week of [DATE]

TLDR: [2-3 sentences]

METRICS DASHBOARD
| Metric           | This Week | Last Week | WoW Change | Target | Status |
|------------------|-----------|-----------|------------|--------|--------|
| [Metric]         | [Value]   | [Value]   | [+/-X%]    | [Tgt]  | [G/Y/R]|

COMPLETED THIS WEEK
- [Item 1]
- [Item 2]

BLOCKERS AND ISSUES
- [Blocker 1]: [Status and next step]

PRIORITIES NEXT WEEK
- [Priority 1]
- [Priority 2]
```

### Monthly Business Review

```
MONTHLY BUSINESS REVIEW
[MONTH YEAR]

FINANCIAL SUMMARY
| Metric       | Actual    | Budget    | Variance  | YTD Actual | YTD Budget |
|--------------|-----------|-----------|-----------|------------|------------|
| Revenue      | $X        | $X        | +/-X%     | $X         | $X         |
| Expenses     | $X        | $X        | +/-X%     | $X         | $X         |
| Margin       | X%        | X%        | +/-Xbps   | X%         | X%         |

DEPARTMENT DEEP-DIVES
[Each department section with metrics, highlights, and challenges]

CUSTOMER METRICS
[NPS, churn, expansion, satisfaction]

PRODUCT METRICS
[Usage, adoption, feature performance]
```

## Distribution and Access Control

| Classification | Who Can Access          | Distribution Method     | Retention   |
|----------------|------------------------|-------------------------|-------------|
| Public         | Anyone                 | Website, public channels| Indefinite  |
| Internal       | All employees          | Email, intranet         | 2 years     |
| Confidential   | Named recipients only  | Encrypted email, secure share | 1 year |
| Restricted     | Board + executives     | Secure portal, watermarked | 6 months |

## Workflow

1. **Define scope**: Report type, audience, time period, key questions
2. **Gather data**: Pull metrics from sources, validate accuracy
3. **Analyze trends**: Compare to prior periods, targets, and benchmarks
4. **Generate insights**: Apply the SCQA framework to significant findings
5. **Select visualizations**: Choose chart types using the selection framework
6. **Draft report**: Fill in the structure template with analysis
7. **Write executive summary**: Summarize after the body is complete (write last)
8. **Review and validate**: Cross-check numbers, review with stakeholders
9. **Distribute**: Send via appropriate channel based on classification

## Scripts & Tools

**Generate report skeleton**:
```bash
scripts/report-generator.sh --type monthly --period "2025-03" --template mbr --output report.md
```

**Data pull automation**:
```bash
scripts/data-pull.sh --sources analytics,crm,finance --period "2025-03-01:2025-03-31" --output data/
```

**Chart generator**:
```bash
scripts/chart-gen.sh --data metrics.csv --type line --x date --y revenue --output charts/revenue.png
```

## Best Practices

- Write the executive summary last, after all analysis is complete.
- Lead with insights, not data. The reader wants to know "so what" before "what."
- Use traffic light colors (green/yellow/red) consistently across all reports.
- Include data sources and methodology in every report appendix.
- Keep the same metric definitions across all report types for consistency.
- Highlight variances that exceed thresholds (e.g., greater than 10% from target).
- Always include an "outlook" section with forward-looking projections.
- Archive reports in a central, searchable repository with consistent naming.
- Solicit feedback from report consumers quarterly to improve relevance.
