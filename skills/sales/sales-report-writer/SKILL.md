---
name: sales-report-writer
description: Generate pipeline, forecast, and performance reports for sales teams. Use when the user mentions "sales report," "pipeline report," "forecast report," "sales dashboard," "win rate," "deal velocity," "sales metrics," "territory report," "quota attainment," "revenue forecast," or "executive sales summary."
metadata:
  version: 1.0.0
  category: sales
---

# Sales Report Writer

Generate comprehensive pipeline, forecast, and performance reports that drive data-informed sales decisions.

## Purpose

Create standardized sales reports covering pipeline health, revenue forecasting, deal velocity, activity metrics, and territory performance. Designed for weekly team reviews, monthly business reviews, and executive board updates.

## Quick Reference

### Report Types and Audiences

| Report Type | Audience | Frequency | Key Metrics |
|-------------|----------|-----------|-------------|
| **Pipeline Report** | Sales managers | Weekly | Pipeline value, stage distribution, aging |
| **Forecast Report** | VP Sales, CFO | Weekly/Monthly | Commit, best case, weighted |
| **Win Rate Analysis** | Sales ops, enablement | Monthly | Win rate by segment, rep, source |
| **Deal Velocity** | Sales managers | Monthly | Cycle length, stage duration, conversion |
| **Activity Report** | Sales managers | Weekly | Calls, emails, meetings, demos |
| **Territory Report** | Regional managers | Monthly | Coverage, penetration, whitespace |
| **Executive Summary** | C-suite, board | Monthly/Quarterly | Revenue, growth, efficiency |

### Key Sales Metrics Reference

| Metric | Formula | Benchmark |
|--------|---------|-----------|
| **Win Rate** | Closed Won / (Closed Won + Closed Lost) | 20-30% (new), 40-60% (expansion) |
| **Pipeline Coverage** | Pipeline Value / Quota | 3-4x for healthy coverage |
| **Average Deal Size** | Total Revenue / Number of Deals | Varies by segment |
| **Sales Cycle Length** | Avg days from Opportunity Created to Close | Track by segment |
| **Deal Velocity** | (Deals x Win Rate x ACV) / Cycle Length | Higher = better |
| **Quota Attainment** | Actual Revenue / Quota | 100% target, 60-70% team avg |
| **CAC** | Total Sales+Marketing Cost / New Customers | < 1/3 of LTV |
| **Pipeline-to-Close Ratio** | Pipeline Created / Revenue Closed | Track monthly |

## Workflow

### Report Generation Checklist

```
Report Generation:
- [ ] Pull CRM data for reporting period
- [ ] Validate data quality (missing fields, stale opportunities)
- [ ] Calculate core metrics
- [ ] Compare to prior period and targets
- [ ] Identify trends and anomalies
- [ ] Segment analysis (by rep, territory, product, source)
- [ ] Add narrative commentary
- [ ] Highlight risks and opportunities
- [ ] Generate visualizations
- [ ] Review with stakeholder before distribution
```

## Templates

### Pipeline Report Template

```
PIPELINE REPORT
Period: {{period}}
Generated: {{date}}
Prepared by: {{author}}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PIPELINE SUMMARY
Total Pipeline Value: ${{total_value}}
Weighted Pipeline: ${{weighted_value}}
Number of Opportunities: {{opp_count}}
Average Deal Size: ${{avg_deal}}
Pipeline Coverage: {{coverage}}x quota

PIPELINE BY STAGE:
| Stage | # Opps | Value | % of Total | Avg Age | Conv Rate |
|-------|--------|-------|------------|---------|-----------|
| Prospecting | {{n}} | ${{v}} | {{pct}}% | {{age}}d | {{conv}}% |
| Qualification | {{n}} | ${{v}} | {{pct}}% | {{age}}d | {{conv}}% |
| Discovery | {{n}} | ${{v}} | {{pct}}% | {{age}}d | {{conv}}% |
| Proposal | {{n}} | ${{v}} | {{pct}}% | {{age}}d | {{conv}}% |
| Negotiation | {{n}} | ${{v}} | {{pct}}% | {{age}}d | {{conv}}% |
| Closed Won | {{n}} | ${{v}} | — | — | — |
| Closed Lost | {{n}} | ${{v}} | — | — | — |

PIPELINE CHANGES THIS PERIOD:
- New opportunities added: {{new_count}} (${{new_value}})
- Opportunities advanced: {{advanced_count}} (${{advanced_value}})
- Opportunities pushed: {{pushed_count}} (${{pushed_value}})
- Opportunities closed won: {{won_count}} (${{won_value}})
- Opportunities closed lost: {{lost_count}} (${{lost_value}})
- Net pipeline change: {{net_sign}}${{net_value}}

AT-RISK DEALS (stale or slipping):
| Deal | Account | Value | Stage | Days in Stage | Risk |
|------|---------|-------|-------|---------------|------|
| {{deal}} | {{acct}} | ${{val}} | {{stg}} | {{days}} | {{risk}} |

PIPELINE BY REP:
| Rep | Pipeline | Weighted | Coverage | # Opps | Avg Size |
|-----|----------|----------|----------|--------|----------|
| {{rep}} | ${{val}} | ${{wt}} | {{cov}}x | {{n}} | ${{avg}} |
```

### Forecast Report Template

```
FORECAST REPORT
Period: {{fiscal_period}}
Close Date: {{period_end_date}}
Days Remaining: {{days_left}}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FORECAST SUMMARY:
| Category | Amount | # Deals | vs Last Week |
|----------|--------|---------|-------------|
| Closed Won (to date) | ${{closed}} | {{n}} | +${{delta}} |
| Commit | ${{commit}} | {{n}} | {{delta}} |
| Best Case | ${{best}} | {{n}} | {{delta}} |
| Pipeline (upside) | ${{upside}} | {{n}} | {{delta}} |
| **Total Forecast** | **${{total}}** | **{{n}}** | **{{delta}}** |

QUOTA ATTAINMENT:
Team Quota: ${{quota}}
Closed + Commit: ${{closed_commit}} ({{pct}}% of quota)
Closed + Commit + Best Case: ${{all}} ({{pct}}% of quota)
Gap to Quota: ${{gap}}

FORECAST METHODOLOGY:
- Commit: >80% probability, decision maker engaged, timeline confirmed
- Best Case: 50-80% probability, champion identified, budget allocated
- Pipeline: <50% probability, early to mid-stage

FORECAST BY REP:
| Rep | Quota | Closed | Commit | Best Case | Attainment |
|-----|-------|--------|--------|-----------|------------|
| {{rep}} | ${{q}} | ${{c}} | ${{cm}} | ${{bc}} | {{pct}}% |

RISKS TO FORECAST:
1. {{risk_1}} — Impact: ${{amount}} — Mitigation: {{action}}
2. {{risk_2}} — Impact: ${{amount}} — Mitigation: {{action}}
3. {{risk_3}} — Impact: ${{amount}} — Mitigation: {{action}}

UPSIDE OPPORTUNITIES:
1. {{opp_1}} — Potential: ${{amount}} — Probability: {{pct}}%
2. {{opp_2}} — Potential: ${{amount}} — Probability: {{pct}}%
```

### Win Rate Analysis Template

```
WIN RATE ANALYSIS
Period: {{period}}
Benchmark: {{benchmark_period}}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

OVERALL WIN RATE:
Current: {{win_rate}}% | Prior Period: {{prior_rate}}% | Trend: {{trend}}

WIN RATE BY SEGMENT:
| Segment | Win Rate | Deals Won | Deals Lost | Avg Size | Cycle |
|---------|----------|-----------|------------|----------|-------|
| Enterprise | {{wr}}% | {{w}} | {{l}} | ${{avg}} | {{d}}d |
| Mid-Market | {{wr}}% | {{w}} | {{l}} | ${{avg}} | {{d}}d |
| SMB | {{wr}}% | {{w}} | {{l}} | ${{avg}} | {{d}}d |

WIN RATE BY LEAD SOURCE:
| Source | Win Rate | Volume | Revenue | Avg Cycle |
|--------|----------|--------|---------|-----------|
| Inbound | {{wr}}% | {{n}} | ${{rev}} | {{d}}d |
| Outbound | {{wr}}% | {{n}} | ${{rev}} | {{d}}d |
| Partner | {{wr}}% | {{n}} | ${{rev}} | {{d}}d |
| Referral | {{wr}}% | {{n}} | ${{rev}} | {{d}}d |

WIN RATE BY REP:
| Rep | Win Rate | vs Team Avg | Deals Won | Revenue |
|-----|----------|-------------|-----------|---------|
| {{rep}} | {{wr}}% | {{delta}} | {{w}} | ${{rev}} |

LOSS REASONS:
| Reason | Count | % of Losses | Trend |
|--------|-------|-------------|-------|
| Price | {{n}} | {{pct}}% | {{trend}} |
| Feature gap | {{n}} | {{pct}}% | {{trend}} |
| No decision | {{n}} | {{pct}}% | {{trend}} |
| Competitor | {{n}} | {{pct}}% | {{trend}} |
| Timing | {{n}} | {{pct}}% | {{trend}} |
```

### Deal Velocity Metrics Template

```
DEAL VELOCITY REPORT
Period: {{period}}

VELOCITY FORMULA:
Velocity = (# Opportunities x Win Rate x Average Deal Value) / Sales Cycle Length

Current Velocity: ${{velocity}}/day
Prior Period: ${{prior_velocity}}/day
Change: {{change_pct}}%

VELOCITY COMPONENTS:
| Component | Current | Prior | Change | Impact |
|-----------|---------|-------|--------|--------|
| # Opportunities | {{n}} | {{prior_n}} | {{delta}} | {{impact}} |
| Win Rate | {{wr}}% | {{prior_wr}}% | {{delta}} | {{impact}} |
| Avg Deal Value | ${{adv}} | ${{prior_adv}} | {{delta}} | {{impact}} |
| Sales Cycle (days) | {{sc}} | {{prior_sc}} | {{delta}} | {{impact}} |

STAGE CONVERSION & DURATION:
| Stage | Conversion Rate | Avg Duration | Bottleneck? |
|-------|----------------|-------------- |-------------|
| Lead → Qualified | {{cr}}% | {{d}} days | {{y/n}} |
| Qualified → Discovery | {{cr}}% | {{d}} days | {{y/n}} |
| Discovery → Proposal | {{cr}}% | {{d}} days | {{y/n}} |
| Proposal → Negotiation | {{cr}}% | {{d}} days | {{y/n}} |
| Negotiation → Closed | {{cr}}% | {{d}} days | {{y/n}} |
```

### Executive Sales Summary Template

```
EXECUTIVE SALES SUMMARY
Period: {{period}}
Prepared for: {{audience}}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HEADLINES:
• Revenue: ${{revenue}} ({{pct}}% of plan, {{yoy_change}} YoY)
• New Customers: {{new_customers}} ({{pct}}% of target)
• Expansion Revenue: ${{expansion}} ({{pct}}% of total)
• Churn: {{churn_rate}}% (target: <{{churn_target}}%)

KEY METRICS DASHBOARD:
| Metric | Actual | Target | Status | Trend |
|--------|--------|--------|--------|-------|
| Revenue | ${{val}} | ${{tgt}} | {{st}} | {{tr}} |
| New ARR | ${{val}} | ${{tgt}} | {{st}} | {{tr}} |
| Pipeline Created | ${{val}} | ${{tgt}} | {{st}} | {{tr}} |
| Win Rate | {{val}}% | {{tgt}}% | {{st}} | {{tr}} |
| Avg Deal Size | ${{val}} | ${{tgt}} | {{st}} | {{tr}} |
| Sales Cycle | {{val}}d | {{tgt}}d | {{st}} | {{tr}} |
| CAC | ${{val}} | ${{tgt}} | {{st}} | {{tr}} |
| Quota Attainment | {{val}}% | 100% | {{st}} | {{tr}} |

TOP WINS:
1. {{customer}} — ${{amount}} ARR — {{context}}
2. {{customer}} — ${{amount}} ARR — {{context}}
3. {{customer}} — ${{amount}} ARR — {{context}}

TOP RISKS:
1. {{risk}} — Impact: ${{amount}} — Action: {{action}}
2. {{risk}} — Impact: ${{amount}} — Action: {{action}}

STRATEGIC INITIATIVES UPDATE:
| Initiative | Status | Progress | Next Milestone |
|-----------|--------|----------|----------------|
| {{init}} | {{status}} | {{pct}}% | {{milestone}} |

NEXT PERIOD OUTLOOK:
{{outlook_narrative}}
```

## Scripts & Tools

**generate_pipeline_report.py**: Pull CRM data and generate pipeline report
```bash
python scripts/generate_pipeline_report.py --period this-quarter --format markdown
# Output: Formatted pipeline report with all metrics
```

**forecast_calculator.py**: Calculate weighted forecast from opportunity data
```bash
python scripts/forecast_calculator.py --method weighted --period Q2-2024
# Output: Forecast by category with confidence intervals
```

**velocity_analysis.py**: Analyze deal velocity and stage conversion
```bash
python scripts/velocity_analysis.py --period last-6-months --segment enterprise
# Output: Velocity metrics, bottleneck identification, trends
```

**executive_summary.py**: Generate board-ready executive summary
```bash
python scripts/executive_summary.py --period monthly --include-charts
# Output: Executive summary with embedded visualizations
```

## Best Practices

1. **Consistent definitions** - Ensure everyone agrees on stage definitions and forecast categories
2. **Clean data first** - Garbage in, garbage out; validate CRM hygiene before reporting
3. **Show trends, not just snapshots** - Always include prior period and year-over-year comparisons
4. **Highlight exceptions** - Call out what changed, not what stayed the same
5. **Separate leading from lagging** - Activity metrics predict; revenue metrics confirm
6. **Right report for right audience** - Reps need deal-level; execs need portfolio-level
7. **Automate recurring reports** - Manual reports waste time and introduce errors
8. **Include narrative** - Numbers without context are noise; always explain the "so what"

## Related Skills

- ROI for deals: `roi-calculator`
- Competitive context: `competitive-battlecard`
- Proposal generation: `proposal-writer`
- Lead scoring: `lead-qualifier`
