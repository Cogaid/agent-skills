# Budget Planner - Reference Documentation

## Budgeting Methodologies Deep Dive

### Zero-Based Budgeting (ZBB)

**Process**:
1. Start every budget line at $0
2. Each department builds "decision packages" -- bundles of activities with costs and benefits
3. Decision packages are ranked by priority
4. Funding allocated from highest priority down until budget is exhausted

**Decision Package Format**:
```
Package Name:     [Activity or program]
Department:       [Name]
Priority Rank:    [1 = critical, 5 = nice-to-have]
Annual Cost:      $[Amount]
Headcount:        [FTEs required]
Benefit:          [Quantified output or outcome]
What happens if cut: [Impact of not funding this package]
```

**When to use ZBB**:
- Organization has grown 50%+ and costs have not been re-examined
- Major strategic pivot (new market, new product line)
- Cost reduction mandate from board or investors
- Post-acquisition integration
- Every 2-3 years as a reset, even in healthy organizations

### Activity-Based Budgeting (ABB)
Allocates costs based on activities that drive expenses, not departments.

**Steps**:
1. Identify key activities (e.g., "process customer orders", "onboard new employees")
2. Determine cost drivers for each activity (e.g., number of orders, number of hires)
3. Estimate volume of each cost driver
4. Calculate cost per activity unit
5. Total budget = sum of (activity volume x cost per unit)

**Best for**: Organizations where overhead is a large % of costs and traditional allocation distorts true cost.

### Rolling Forecast
Always maintain a forward-looking 12-18 month forecast that updates monthly or quarterly.

**Comparison**:
| Feature | Traditional Budget | Rolling Forecast |
|---------|-------------------|-----------------|
| Horizon | Fixed 12 months | Always 12-18 months ahead |
| Update frequency | Annual | Monthly or quarterly |
| Accuracy | Decays over time | Stays current |
| Effort | Heavy annual cycle | Lighter continuous updates |
| Decision support | Backward-looking | Forward-looking |

## Budget Category Benchmarks

### SaaS Company (by stage)
| Category | Seed/Series A | Series B | Series C+ |
|----------|--------------|----------|-----------|
| People (% of revenue) | 70-90% | 55-70% | 45-55% |
| R&D (% of revenue) | 30-40% | 25-35% | 20-30% |
| Sales & Marketing (% of revenue) | 30-50% | 35-45% | 25-35% |
| G&A (% of revenue) | 15-25% | 10-15% | 8-12% |
| COGS (% of revenue) | 15-30% | 15-25% | 15-20% |

### Professional Services
| Category | Small Firm | Mid-Market | Large Firm |
|----------|-----------|------------|------------|
| People (% of revenue) | 55-65% | 50-60% | 45-55% |
| Technology (% of revenue) | 3-5% | 4-7% | 5-8% |
| Facilities (% of revenue) | 5-10% | 8-12% | 10-15% |
| Business Development (% of revenue) | 5-10% | 8-12% | 10-15% |
| G&A (% of revenue) | 8-12% | 8-10% | 6-8% |

### E-commerce
| Category | Small | Medium | Large |
|----------|-------|--------|-------|
| COGS (% of revenue) | 40-60% | 35-50% | 30-45% |
| Fulfillment (% of revenue) | 10-20% | 8-15% | 5-10% |
| Marketing (% of revenue) | 15-25% | 10-20% | 8-15% |
| Technology (% of revenue) | 3-8% | 5-10% | 5-8% |
| Customer Support (% of revenue) | 3-5% | 2-4% | 1-3% |

## Forecasting Methods - Technical Detail

### Moving Average
```
Simple Moving Average (3-month):
  Forecast = (Month_n + Month_n-1 + Month_n-2) / 3

Weighted Moving Average:
  Forecast = (Month_n x 0.5) + (Month_n-1 x 0.3) + (Month_n-2 x 0.2)

Exponential Smoothing:
  Forecast = alpha x Actual_n + (1 - alpha) x Forecast_n
  Where alpha = smoothing factor (0.1 to 0.3 typical)
```

### Scenario Planning
Build three scenarios with explicit assumptions:

| Parameter | Conservative | Base | Optimistic |
|-----------|-------------|------|-----------|
| Revenue growth | -5% to +5% | +10% to +20% | +25% to +40% |
| Customer acquisition | 80% of target | 100% of target | 120% of target |
| Churn rate | +0.5pp worse | Flat | -0.5pp better |
| Hiring pace | Delayed 1 quarter | On plan | Accelerated |
| Price increases | None | Per plan | Larger than plan |

**Probability weighting**:
```
Expected Value = (Conservative x 25%) + (Base x 50%) + (Optimistic x 25%)
```

## Contingency Planning

### Contingency Sizing Guidelines
| Organization Type | Recommended Contingency |
|------------------|----------------------|
| Startup (pre-revenue) | 15-20% of total budget |
| Early-stage (< 2 years revenue) | 10-15% |
| Growth stage | 7-10% |
| Mature / stable | 5-7% |
| Government / regulated | 5-10% (often required) |

### Contingency Release Criteria
1. **Threshold**: Contingency release requires documented justification and approval
2. **Authority levels**:
   - <$5K: Department head
   - $5K-$25K: Finance lead
   - $25K-$100K: CFO
   - >$100K: CEO or Board
3. **Documentation**: Every contingency draw must record: amount, reason, category, approval, date
4. **Replenishment**: If contingency drops below 50%, trigger a budget review

## Capital vs. Operating Expense

| Criterion | Capital Expense (CapEx) | Operating Expense (OpEx) |
|-----------|------------------------|------------------------|
| Definition | Assets with useful life >1 year | Day-to-day business costs |
| Accounting | Capitalized, depreciated/amortized | Expensed in current period |
| Tax impact | Depreciation deduction over time | Immediate deduction |
| Cash flow statement | Investing activities | Operating activities |
| Examples | Equipment, software development, property | Rent, salaries, utilities, SaaS subscriptions |
| Budget approval | Often requires separate CapEx approval | Normal budget process |

### Depreciation Methods
```
Straight-Line:
  Annual Depreciation = (Cost - Salvage Value) / Useful Life

Double Declining Balance:
  Annual Depreciation = 2 x (1 / Useful Life) x Book Value at Start of Year

MACRS (US Tax):
  Uses IRS depreciation tables based on asset class
  Common: 3-year, 5-year, 7-year, 15-year, 27.5-year, 39-year
```

## Budget Approval Workflow

```
1. Department heads submit budget requests (8 weeks before fiscal year)
2. Finance consolidates and identifies gaps vs. revenue plan (6 weeks)
3. Executive review and challenge session (4-5 weeks)
4. Board/CEO approval of final budget (2-3 weeks)
5. Budget loaded into financial system (1 week)
6. Budget owners notified and empowered (fiscal year start)

Reforecast cycle:
  Q1: Reforecast Q2-Q4 based on Q1 actuals
  Q2: Mid-year reset, reforecast Q3-Q4
  Q3: Reforecast Q4, begin next year planning
  Q4: Finalize current year, approve next year budget
```
