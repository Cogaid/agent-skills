# KPI Tracker - Reference Guide

## KPI Design Principles

### Leading vs Lagging Indicators

| Type | Definition | Examples | Use |
|---|---|---|---|
| Leading | Predict future outcomes | Pipeline value, website traffic, demo requests | Early warning, proactive action |
| Lagging | Measure past outcomes | Revenue, churn rate, NPS | Confirm results, measure success |

### The Balanced Scorecard Framework

| Perspective | Question | Example KPIs |
|---|---|---|
| Financial | How do we look to shareholders? | Revenue growth, profit margin, ROI |
| Customer | How do customers see us? | NPS, CSAT, retention rate, CAC |
| Internal Process | What must we excel at? | Cycle time, defect rate, deployment frequency |
| Learning and Growth | Can we continue to improve? | Employee engagement, training hours, innovation rate |

### KPI Anti-Patterns

| Anti-Pattern | Description | Fix |
|---|---|---|
| Vanity metrics | Look good but do not drive decisions | Replace with actionable metrics |
| Too many KPIs | Dilutes focus (>8 per team) | Prioritize to 5-8 maximum |
| No owner | Nobody accountable for the KPI | Assign single accountable owner |
| Stale targets | Targets not updated as conditions change | Review targets quarterly |
| Gaming | People optimize the metric, not the goal | Use balanced metric sets |
| Measurement without action | Track but never act on results | Tie each KPI to a decision or action |
| Lag-only | Only measuring outcomes, no predictive metrics | Add leading indicators |
| Input-only | Measuring effort, not results | Add outcome metrics |

## Department KPI Deep Dive

### SaaS Metrics Framework

| Metric | Formula | Healthy Range | Danger Signal |
|---|---|---|---|
| MRR Growth Rate | (MRR this month - MRR last month) / MRR last month | 5-15% MoM (early stage) | Negative or declining growth |
| Net Revenue Retention | (Start MRR + Expansion - Contraction - Churn) / Start MRR | >100% (120%+ excellent) | Below 90% |
| Gross Margin | (Revenue - COGS) / Revenue | >70% for SaaS | Below 60% |
| LTV:CAC Ratio | Customer Lifetime Value / Customer Acquisition Cost | >3:1 | Below 1:1 |
| CAC Payback | CAC / (ARPU x Gross Margin %) | <12 months | >18 months |
| Quick Ratio | (New MRR + Expansion MRR) / (Contraction MRR + Churn MRR) | >4 | Below 1 |
| Rule of 40 | Revenue Growth Rate + Profit Margin | >40% | Below 20% |
| Magic Number | Net New ARR / Sales & Marketing Spend (prior quarter) | >0.75 | Below 0.5 |
| Burn Multiple | Net Burn / Net New ARR | <1x (efficient) | >2x |

### DORA Metrics (Engineering)

| Metric | Elite | High | Medium | Low |
|---|---|---|---|---|
| Deployment Frequency | On-demand (multiple/day) | Weekly to monthly | Monthly to every 6 months | Every 6+ months |
| Lead Time for Changes | Less than 1 hour | 1 day to 1 week | 1 week to 1 month | 1 to 6 months |
| Change Failure Rate | 0-15% | 16-30% | 16-30% | 16-30% |
| Time to Restore Service | Less than 1 hour | Less than 1 day | 1 day to 1 week | More than 6 months |

### Pirate Metrics (AARRR)

| Stage | Metric | Calculation | Benchmark |
|---|---|---|---|
| Acquisition | New signups | Count per period | Growing MoM |
| Activation | Activated users | Users completing key action / Total signups | >25% |
| Retention | Returning users | Users active in period N / Users active in period 0 | D30 >20% |
| Revenue | Paying customers | Paying / Total active x 100 | >5% free-to-paid |
| Referral | Viral coefficient | Invites sent x Conversion rate | >1.0 for viral growth |

## Target Setting Deep Dive

### Historical Baseline Method

```
1. Gather 12+ months of historical data
2. Calculate average and standard deviation
3. Identify trend (linear regression slope)
4. Project forward using trend + growth rate
5. Add stretch factor (5-15% above projection)
6. Validate against resource constraints
```

### OKR Alignment

| Level | Objective Example | Key Result (KPI) |
|---|---|---|
| Company | Become the market leader in [segment] | Achieve $[X]M ARR by Q4 |
| Department | Accelerate revenue growth | Increase MRR growth rate from 8% to 12% |
| Team | Improve sales efficiency | Reduce sales cycle from 45 to 30 days |
| Individual | Close enterprise deals | Win 3 enterprise accounts at $100K+ each |

### Target Calibration

| Signal | Action |
|---|---|
| Consistently hitting 120%+ for 3 periods | Target is too easy -- raise it |
| Consistently missing at 60-70% for 3 periods | Target may be too aggressive -- recalibrate |
| High variance (some periods 50%, some 150%) | Process issue -- investigate root cause |
| New metric with no history | Set conservative target, adjust after 2 quarters |

## Traffic Light Scoring System

### Standard Thresholds

| Color | Range | Meaning | Dashboard Display |
|---|---|---|---|
| Green | >= 90% of target | On track | Green circle / checkmark |
| Yellow | 70-89% of target | At risk | Yellow triangle / warning |
| Red | < 70% of target | Off track | Red circle / X |
| Blue | > 120% of target | Exceeding | Blue star (validate data) |
| Gray | No data available | Not measured | Gray dash |

### Custom Thresholds by Metric Type

| Metric Type | Green | Yellow | Red |
|---|---|---|---|
| Revenue | >= 95% | 85-94% | < 85% |
| Customer satisfaction | >= 90% | 75-89% | < 75% |
| Operational (uptime) | >= 99.5% | 99.0-99.4% | < 99.0% |
| Cost metrics | <= 105% of budget | 106-120% | > 120% |
| Growth rates | >= 90% of target | 70-89% | < 70% |

## Review Meeting Frameworks

### Weekly Review Agenda (30 minutes)

| Time | Activity | Owner |
|---|---|---|
| 0-5 min | Scorecard review: green/yellow/red | Team lead |
| 5-15 min | Deep-dive on red/yellow KPIs | KPI owners |
| 15-25 min | Action items and blockers | All |
| 25-30 min | Priorities for next week | Team lead |

### Monthly Review Agenda (60 minutes)

| Time | Activity | Owner |
|---|---|---|
| 0-10 min | Month-end scorecard | Department head |
| 10-30 min | Trend analysis and insights | Analyst |
| 30-45 min | Deep-dive on underperforming areas | KPI owners |
| 45-55 min | Resource allocation and support needs | Department head |
| 55-60 min | Action items and next steps | All |

### Quarterly Review Agenda (90 minutes)

| Time | Activity | Owner |
|---|---|---|
| 0-15 min | Quarter-end scorecard and trends | Executive |
| 15-35 min | Strategic KPI performance analysis | Department heads |
| 35-55 min | Target recalibration for next quarter | All leads |
| 55-75 min | KPI additions, retirements, and redefinitions | Strategy |
| 75-90 min | Action items and commitments | All |
