---
name: financial-report-writer
description: Write financial summaries, reports, and analysis for various audiences. Use when the user mentions "financial report," "P&L," "profit and loss," "cash flow report," "balance sheet," "budget variance," "financial summary," "executive summary," "quarterly report," "annual report," "financial analysis," or "board report."
metadata:
  version: 1.0.0
  category: finance-operations
---

# Financial Report Writer

Write clear, audience-appropriate financial summaries and reports with proper structure and key metrics.

## Purpose

This skill helps you create financial reports that communicate performance, trends, and insights effectively. It supports multiple report types (P&L, cash flow, balance sheet summaries, budget variance) and tailors format and depth to the audience -- board members, executives, or team leads.

## Quick Start

1. **Identify report type**: P&L, cash flow, balance sheet, or variance
2. **Define audience**: Board, executive, department, or team
3. **Gather data**: Pull actuals, budgets, and prior period comparisons
4. **Draft executive summary**: Lead with the headline numbers
5. **Add detail sections**: Tables, trends, and commentary
6. **Include recommendations**: Forward-looking actions based on data

## Report Types Overview

| Report Type | Purpose | Frequency | Primary Audience |
|-------------|---------|-----------|-----------------|
| **P&L (Income Statement)** | Revenue vs. expenses, net income | Monthly / Quarterly | Exec, Board |
| **Cash Flow Statement** | Cash in vs. cash out, runway | Monthly / Quarterly | CFO, Board |
| **Balance Sheet Summary** | Assets, liabilities, equity snapshot | Quarterly / Annual | Board, Investors |
| **Budget Variance** | Actual vs. planned spending | Monthly | Dept Heads, CFO |
| **Financial Dashboard** | KPI summary with trends | Weekly / Monthly | Exec Team |
| **Board Financial Package** | Comprehensive multi-report bundle | Quarterly | Board of Directors |
| **Investor Update** | Metrics + narrative for investors | Monthly / Quarterly | Investors |

## Executive Summary Template

```
EXECUTIVE FINANCIAL SUMMARY
Period: [Month/Quarter] [Year]
Prepared: [Date]
Prepared by: [Name/Title]

─── HEADLINE NUMBERS ───────────────────────────────
Revenue:          $[X.XM]    (↑/↓ XX% vs. prior period)
Gross Margin:     XX.X%      (↑/↓ X.X pp vs. prior period)
Operating Expense: $[X.XM]   (↑/↓ XX% vs. budget)
Net Income:       $[X.XM]    (↑/↓ XX% vs. prior period)
Cash Position:    $[X.XM]    (runway: XX months)
Burn Rate:        $[XXXk]/mo

─── KEY HIGHLIGHTS ─────────────────────────────────
1. [Most important positive development]
2. [Second highlight or concern]
3. [Third item requiring attention]

─── RISKS & WATCH ITEMS ────────────────────────────
• [Risk 1 with potential impact]
• [Risk 2 with mitigation status]

─── RECOMMENDED ACTIONS ────────────────────────────
1. [Action item with owner and deadline]
2. [Action item with owner and deadline]
```

## Key Metrics Table

| Category | Metric | Formula | Target | Frequency |
|----------|--------|---------|--------|-----------|
| **Revenue** | MRR / ARR | Sum of recurring revenue | Per plan | Monthly |
| **Revenue** | Revenue Growth Rate | (Current - Prior) / Prior | >10% QoQ | Quarterly |
| **Profitability** | Gross Margin | (Revenue - COGS) / Revenue | >60% | Monthly |
| **Profitability** | Net Margin | Net Income / Revenue | >15% | Quarterly |
| **Profitability** | EBITDA | Earnings before interest, tax, depreciation, amort. | Positive | Quarterly |
| **Cash** | Cash Runway | Cash Balance / Monthly Burn | >12 months | Monthly |
| **Cash** | Operating Cash Flow | Cash from operations | Positive | Monthly |
| **Efficiency** | CAC | Total Sales+Marketing / New Customers | <LTV/3 | Quarterly |
| **Efficiency** | LTV:CAC Ratio | Customer LTV / CAC | >3:1 | Quarterly |
| **Efficiency** | Rule of 40 | Revenue Growth % + Profit Margin % | >40 | Annual |
| **Expense** | OpEx Ratio | Operating Expenses / Revenue | <70% | Monthly |
| **Expense** | Headcount Cost Ratio | Total Comp / Revenue | <50% | Quarterly |

## P&L Report Template

```
PROFIT & LOSS STATEMENT
Period: [Start Date] to [End Date]
Comparison: vs. Prior Period | vs. Budget

                          Actual      Budget     Variance   Prior Period   % Change
                         ────────    ────────    ────────   ────────────   ────────
REVENUE
  Product Revenue        $XXX,XXX    $XXX,XXX    $XX,XXX    $XXX,XXX       +XX%
  Service Revenue        $XXX,XXX    $XXX,XXX   ($XX,XXX)   $XXX,XXX       -XX%
  Other Revenue           $XX,XXX     $XX,XXX     $X,XXX     $XX,XXX       +XX%
                         ────────    ────────    ────────   ────────────
  TOTAL REVENUE          $XXX,XXX    $XXX,XXX    $XX,XXX    $XXX,XXX       +XX%

COST OF GOODS SOLD
  Direct Costs           $XXX,XXX    $XXX,XXX    $XX,XXX    $XXX,XXX
  Hosting / Infra         $XX,XXX     $XX,XXX     $X,XXX     $XX,XXX
                         ────────    ────────    ────────   ────────────
  TOTAL COGS             $XXX,XXX    $XXX,XXX    $XX,XXX    $XXX,XXX

GROSS PROFIT             $XXX,XXX    $XXX,XXX    $XX,XXX    $XXX,XXX
  Gross Margin              XX.X%       XX.X%                   XX.X%

OPERATING EXPENSES
  Salaries & Benefits    $XXX,XXX    $XXX,XXX   ($XX,XXX)   $XXX,XXX
  Sales & Marketing       $XX,XXX     $XX,XXX     $X,XXX     $XX,XXX
  R&D / Engineering       $XX,XXX     $XX,XXX    ($X,XXX)    $XX,XXX
  General & Admin         $XX,XXX     $XX,XXX     $X,XXX     $XX,XXX
                         ────────    ────────    ────────   ────────────
  TOTAL OpEx             $XXX,XXX    $XXX,XXX   ($XX,XXX)   $XXX,XXX

NET INCOME (LOSS)         $XX,XXX     $XX,XXX    ($X,XXX)    $XX,XXX
  Net Margin                XX.X%       XX.X%                   XX.X%
```

## Trend Analysis Format

```
TREND ANALYSIS: [Metric Name]
──────────────────────────────────────────────────

Period     Value      Change    Trend    Notes
──────     ──────     ──────    ─────    ─────────────────
Q1 2025    $1.2M       --       --      Baseline
Q2 2025    $1.4M      +16.7%    ↑       New product launch
Q3 2025    $1.3M       -7.1%    ↓       Seasonal dip
Q4 2025    $1.8M      +38.5%    ↑↑      Holiday + expansion
Q1 2026    $2.1M      +16.7%    ↑       Sustained growth

3-month moving avg:  $1.73M
6-month moving avg:  $1.65M
YoY growth:          +75.0%
Trajectory:          Accelerating

Commentary:
[2-3 sentences interpreting the trend, noting inflection points,
seasonality, and what's driving the numbers.]
```

## Audience-Specific Formats

| Audience | Length | Focus | Tone | Visuals |
|----------|--------|-------|------|---------|
| **Board of Directors** | 3-5 pages | Strategic: revenue, margin, runway, risks | Formal, concise | Charts + summary tables |
| **Executive Team** | 2-3 pages | Operational: KPIs, variance, actions | Direct, action-oriented | Dashboard-style |
| **Department Heads** | 1-2 pages | Departmental: budget vs. actual, headcount | Detailed, practical | Line-item tables |
| **Team / All-Hands** | 1 page | High-level wins, growth, priorities | Motivational, transparent | Simple charts |
| **Investors** | 2-4 pages | Metrics: ARR, burn, LTV/CAC, cohorts | Confident, data-driven | Benchmark comparisons |

### Board Package Outline

```
Board Financial Package:
1. Executive Summary (1 page)
2. P&L with commentary (1-2 pages)
3. Cash flow and runway (1 page)
4. Key metrics dashboard (1 page)
5. Budget variance highlights (1 page)
6. Forward outlook and risks (1 page)
7. Appendix: Detailed financials (as needed)
```

## Visualization Recommendations

| Data Type | Best Chart | Why |
|-----------|-----------|-----|
| Revenue over time | Line chart | Shows trajectory and trend |
| Revenue by segment | Stacked bar | Shows composition and growth |
| Expense breakdown | Pie / donut chart | Shows proportional allocation |
| Budget vs. actual | Grouped bar chart | Side-by-side comparison |
| Cash runway | Waterfall chart | Shows inflows and outflows |
| KPI performance | Gauge / bullet chart | Shows vs. target at a glance |
| Cohort analysis | Heatmap | Shows retention patterns |

## Scripts & Tools

**generate_pnl.py**: Build P&L from accounting data
```bash
python scripts/generate_pnl.py --period Q1-2026 --compare budget,prior
# Output: P&L report with variance analysis
```

**financial_dashboard.py**: Generate KPI dashboard
```bash
python scripts/financial_dashboard.py --metrics revenue,margin,runway --format html
# Output: Interactive dashboard with trend charts
```

**variance_report.py**: Budget variance analysis
```bash
python scripts/variance_report.py --period 2026-03 --threshold 10
# Output: All line items with >10% variance flagged
```

## Best Practices

1. **Lead with the story**: Start with what matters most -- don't bury the headline
2. **Compare periods**: Always show vs. prior period and vs. budget for context
3. **Explain variances**: Numbers without commentary leave readers guessing
4. **Use consistent formatting**: Same structure every period builds reader familiarity
5. **Flag risks early**: Surface problems before they surprise stakeholders
6. **Round appropriately**: Board reports in millions, team reports in thousands
7. **Include forward outlook**: Reports should inform decisions, not just record history
8. **Separate recurring from one-time**: Normalize results so trends are meaningful
9. **Define your metrics**: Include a glossary if your audience may not know terms like EBITDA or CAC
10. **Deliver on time**: A late report loses most of its decision-making value
