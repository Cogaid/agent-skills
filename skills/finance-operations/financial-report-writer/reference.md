# Financial Report Writer - Reference Documentation

## Financial Statement Standards

### GAAP (Generally Accepted Accounting Principles) - US
Key principles that govern financial reporting:
- **Revenue Recognition (ASC 606)**: Revenue recognized when performance obligations are satisfied
- **Matching Principle**: Expenses matched to the revenue they help generate in the same period
- **Accrual Basis**: Transactions recorded when they occur, not when cash changes hands
- **Consistency**: Same accounting methods used from period to period
- **Materiality**: All significant financial information must be disclosed

### IFRS (International Financial Reporting Standards)
Used in 140+ countries. Key differences from GAAP:
- LIFO inventory method not permitted
- Development costs can be capitalized (GAAP expenses them)
- More principles-based vs. GAAP's rules-based approach
- Single-step or multi-step income statement both acceptable

## Key Financial Metrics - Detailed Formulas

### Revenue Metrics
```
Monthly Recurring Revenue (MRR):
  MRR = Sum of all recurring revenue in the month
  
Annual Recurring Revenue (ARR):
  ARR = MRR x 12

Net Revenue Retention (NRR):
  NRR = (Starting MRR + Expansion - Contraction - Churn) / Starting MRR
  Target: >110% for SaaS

Revenue Growth Rate:
  QoQ Growth = (Current Quarter Revenue - Prior Quarter Revenue) / Prior Quarter Revenue
  YoY Growth = (Current Year Revenue - Prior Year Revenue) / Prior Year Revenue
```

### Profitability Metrics
```
Gross Margin:
  Gross Margin = (Revenue - COGS) / Revenue x 100
  SaaS benchmark: 70-85%
  Services benchmark: 30-50%

EBITDA:
  EBITDA = Net Income + Interest + Taxes + Depreciation + Amortization
  
EBITDA Margin:
  EBITDA Margin = EBITDA / Revenue x 100

Operating Margin:
  Operating Margin = Operating Income / Revenue x 100

Net Margin:
  Net Margin = Net Income / Revenue x 100

Rule of 40 (SaaS):
  Rule of 40 = Revenue Growth % + EBITDA Margin %
  Target: >40 indicates healthy balance of growth and profitability
```

### Cash Metrics
```
Cash Runway:
  Cash Runway (months) = Cash Balance / Monthly Net Burn Rate

Net Burn Rate:
  Net Burn = Monthly Operating Expenses - Monthly Revenue

Gross Burn Rate:
  Gross Burn = Total Monthly Operating Expenses (ignoring revenue)

Operating Cash Flow:
  OCF = Net Income + Non-cash Charges + Changes in Working Capital

Free Cash Flow:
  FCF = Operating Cash Flow - Capital Expenditures

Cash Conversion Cycle:
  CCC = Days Sales Outstanding + Days Inventory Outstanding - Days Payable Outstanding
```

### Efficiency Metrics
```
Customer Acquisition Cost (CAC):
  CAC = Total Sales & Marketing Expense / New Customers Acquired

Customer Lifetime Value (LTV):
  LTV = ARPU x Gross Margin % x Average Customer Lifetime (months)
  
LTV:CAC Ratio:
  LTV:CAC = LTV / CAC
  Target: >3:1

CAC Payback Period:
  Payback = CAC / (ARPU x Gross Margin %)
  Target: <18 months for SaaS

Magic Number (SaaS Sales Efficiency):
  Magic Number = Net New ARR (QoQ) / Prior Quarter Sales & Marketing Spend
  >1.0 = efficient, invest more; 0.5-1.0 = okay; <0.5 = fix before scaling
```

## Report Structure Best Practices

### Executive Summary Guidelines
- Lead with the single most important number or trend
- Limit to 5-7 key metrics
- Use directional indicators (up/down arrows, green/red)
- Compare to prior period AND budget/target
- Keep to one page maximum
- End with 2-3 actionable recommendations

### Variance Commentary Framework
For each material variance, explain using this structure:
1. **What**: State the variance amount and percentage
2. **Why**: Root cause (one-time vs. structural)
3. **Impact**: How it affects the bottom line or other metrics
4. **Action**: What is being done or should be done
5. **Outlook**: Will this continue or is it resolved?

Example:
> Marketing expense was $52K vs. $45K budget (+$7K, +16%). The overage is due to an
> unplanned trade show sponsorship ($8K) approved in mid-quarter. Net effect on operating
> margin: -0.5pp. The spend is one-time and Q2 is expected to be at or below budget. No
> reallocation needed.

### Audience Calibration

| Element | Board | Executives | Department Heads | All-Hands |
|---------|-------|-----------|-----------------|-----------|
| Revenue detail | Top-line + segments | Segment breakdown | Their department's contribution | Total only |
| Expense detail | Category totals | Category + major items | Line-item detail | Total only |
| Rounding | Millions ($X.XM) | Thousands ($XXXk) | Exact dollars | Millions |
| Period comparison | YoY + QoQ | QoQ + vs budget | Monthly + vs budget | QoQ |
| Forward outlook | 3-5 year strategic | Next 2 quarters | Next month | Next quarter |
| Risk disclosure | Full risk register | Top 3-5 risks | Department risks | High-level only |
| Recommendations | Strategic moves | Operational actions | Tactical tasks | Celebratory wins |

## Industry Benchmarks

### SaaS Metrics Benchmarks (by ARR stage)
| Metric | <$1M ARR | $1-10M ARR | $10-50M ARR | $50M+ ARR |
|--------|----------|------------|-------------|-----------|
| YoY Growth | >100% | 80-100% | 50-80% | 30-50% |
| Gross Margin | 60-70% | 70-80% | 75-85% | 80-90% |
| Net Retention | >100% | >110% | >115% | >120% |
| CAC Payback | <18 mo | <15 mo | <12 mo | <12 mo |
| LTV:CAC | >3:1 | >3:1 | >4:1 | >5:1 |
| Burn Multiple | <2x | <1.5x | <1x | Profitable |

### Professional Services Benchmarks
| Metric | Good | Great | Best-in-Class |
|--------|------|-------|---------------|
| Gross Margin | 30% | 40% | 50%+ |
| Utilization Rate | 65% | 75% | 80%+ |
| Revenue per Employee | $150K | $200K | $250K+ |
| Project Margin | 25% | 35% | 45%+ |
| Average Bill Rate | $150/hr | $200/hr | $300+/hr |

## Visualization Selection Guide

### When to Use Each Chart Type
- **Line chart**: Trends over time (revenue, growth, runway). Use for 3+ time periods.
- **Bar chart**: Comparisons between categories (departments, products, regions).
- **Stacked bar**: Composition over time (revenue mix by segment).
- **Grouped bar**: Side-by-side comparison (actual vs. budget).
- **Waterfall**: Bridge from one value to another (revenue bridge, cash flow).
- **Pie/donut**: Proportional breakdown (expense allocation). Use sparingly, max 5-6 slices.
- **Heatmap**: Pattern detection (cohort retention, seasonal revenue).
- **Gauge/bullet**: Progress toward target (KPI performance).
- **Sparkline**: Inline trend indicators in tables.

### Color Conventions
- **Green**: Positive performance, at or above target
- **Yellow/Amber**: Caution, within 5-10% of threshold
- **Red**: Negative performance, below target or over budget
- **Gray**: Baseline, prior period, or budget reference line
- **Blue**: Primary data, neutral presentation
