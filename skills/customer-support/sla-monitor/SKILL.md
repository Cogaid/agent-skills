---
name: sla-monitor
description: Monitor and report on SLA compliance across support channels. Use when the user mentions "SLA," "service level agreement," "response time," "resolution time," "uptime monitoring," "SLA breach," "SLA report," "compliance tracking," "SLA dashboard," "service metrics," or "SLA negotiation."
metadata:
  version: 1.0.0
  category: customer-support
---

# SLA Monitor

Monitor, report, and maintain SLA compliance across all customer support channels and service tiers.

## Purpose

Track service level agreements in real time, detect potential breaches before they occur, generate compliance reports, and provide frameworks for SLA negotiation and remediation planning.

## Quick Reference

### Core SLA Metrics

| Metric | Definition | Typical Targets | Measurement |
|--------|-----------|-----------------|-------------|
| **First Response Time (FRT)** | Time from ticket creation to first agent response | 1h (critical), 4h (high), 8h (normal), 24h (low) | Clock starts at creation |
| **Resolution Time (RT)** | Time from creation to confirmed resolution | 4h (critical), 24h (high), 48h (normal), 72h (low) | Pause on customer wait |
| **Uptime** | System availability percentage | 99.9% (standard), 99.95% (premium), 99.99% (enterprise) | Monthly rolling window |
| **First Contact Resolution (FCR)** | Issues resolved in first interaction | 70-80% target | Reopens within 72h = miss |
| **Customer Wait Time** | Queue time before agent connection | <2 min (chat), <3 min (phone), <1h (email) | Median, not average |
| **Escalation Rate** | Tickets requiring escalation | <15% of total volume | Per tier tracking |

### SLA Tier Definitions

| Tier | Response Time | Resolution Time | Availability | Support Hours | Dedicated Agent |
|------|--------------|----------------|--------------|---------------|-----------------|
| **Enterprise** | 15 min | 4 hours | 99.99% | 24/7/365 | Yes |
| **Premium** | 1 hour | 8 hours | 99.95% | 24/7 | Optional |
| **Standard** | 4 hours | 24 hours | 99.9% | Business hours | No |
| **Basic** | 24 hours | 72 hours | 99.5% | Business hours | No |

### Priority Escalation Matrix

| Priority | First Response | Update Frequency | Resolution Target | Escalation After |
|----------|---------------|-------------------|-------------------|------------------|
| **P1 - Critical** | 15 minutes | Every 30 minutes | 4 hours | 1 hour |
| **P2 - High** | 1 hour | Every 2 hours | 8 hours | 4 hours |
| **P3 - Medium** | 4 hours | Every 8 hours | 48 hours | 24 hours |
| **P4 - Low** | 24 hours | Every 24 hours | 72 hours | 48 hours |

## Workflow

### SLA Monitoring Checklist

```
Daily SLA Monitoring:
- [ ] Review real-time SLA dashboard at start of shift
- [ ] Check for any overnight breaches
- [ ] Identify tickets approaching SLA threshold (80% of time elapsed)
- [ ] Verify escalation notifications are firing correctly
- [ ] Spot-check 5 recently resolved tickets for accuracy
- [ ] Review queue depth and staffing alignment
- [ ] Log any system downtime incidents
- [ ] Send end-of-day SLA summary to team leads

Weekly SLA Review:
- [ ] Generate weekly SLA compliance report
- [ ] Analyze breach patterns (time of day, category, agent)
- [ ] Review and update at-risk tickets
- [ ] Calculate rolling 30-day compliance rates
- [ ] Identify top 3 breach root causes
- [ ] Update remediation plan if compliance < target
- [ ] Present findings to management
```

### Escalation Workflow for SLA Breaches

```
SLA Breach Response Flow:

TIME REMAINING     ACTION
├── 80% elapsed    → Yellow alert: Notify assigned agent
├── 90% elapsed    → Orange alert: Notify team lead + reassign if needed
├── 100% elapsed   → Red alert: Breach logged, notify manager
├── 100% + 1 hour  → Escalate to senior management
└── 100% + 4 hours → Executive notification + incident review triggered
```

## Templates

### SLA Dashboard Template

```
╔══════════════════════════════════════════════════════════╗
║              SLA COMPLIANCE DASHBOARD                    ║
║              Date: {{date}} | Period: {{period}}         ║
╠══════════════════════════════════════════════════════════╣

OVERALL COMPLIANCE: {{overall_pct}}%  [████████░░] Target: 95%

BY METRIC:
  First Response Time:  {{frt_pct}}%  [████████░░]  {{frt_trend}}
  Resolution Time:      {{rt_pct}}%   [███████░░░]  {{rt_trend}}
  Uptime:               {{up_pct}}%   [██████████]  {{up_trend}}
  FCR Rate:             {{fcr_pct}}%  [████████░░]  {{fcr_trend}}

BY TIER:
  Enterprise:  {{ent_pct}}% compliance  ({{ent_breaches}} breaches)
  Premium:     {{prem_pct}}% compliance ({{prem_breaches}} breaches)
  Standard:    {{std_pct}}% compliance  ({{std_breaches}} breaches)
  Basic:       {{bas_pct}}% compliance  ({{bas_breaches}} breaches)

ACTIVE ALERTS:
  🔴 Critical: {{critical_count}} tickets breached
  🟠 At Risk:  {{atrisk_count}} tickets approaching SLA
  🟢 On Track: {{ontrack_count}} tickets within SLA

TOP BREACH CATEGORIES:
  1. {{category_1}}: {{cat1_count}} breaches ({{cat1_pct}}%)
  2. {{category_2}}: {{cat2_count}} breaches ({{cat2_pct}}%)
  3. {{category_3}}: {{cat3_count}} breaches ({{cat3_pct}}%)
╚══════════════════════════════════════════════════════════╝
```

### Breach Notification Template

```
SUBJECT: [SLA BREACH] {{priority}} - Ticket #{{ticket_id}} - {{customer_name}}

BREACH DETAILS:
- Ticket ID: #{{ticket_id}}
- Customer: {{customer_name}} ({{tier}} tier)
- Priority: {{priority}}
- SLA Metric Breached: {{metric}}
- Target: {{target_time}}
- Actual: {{actual_time}}
- Overage: {{overage_time}}

TICKET SUMMARY:
{{ticket_summary}}

CURRENT STATUS:
- Assigned Agent: {{agent_name}}
- Last Update: {{last_update_time}}
- Customer Waiting Since: {{wait_duration}}

REQUIRED ACTIONS:
1. Acknowledge this breach within 15 minutes
2. Contact the customer with status update
3. Provide estimated resolution time
4. Complete Root Cause field in ticket
5. Submit breach report within 24 hours

ESCALATION PATH:
{{escalation_contacts}}
```

### Monthly SLA Report Template

```
SLA COMPLIANCE REPORT
Period: {{month}} {{year}}
Generated: {{report_date}}
Prepared by: {{author}}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXECUTIVE SUMMARY
Overall SLA Compliance: {{overall_pct}}% (target: {{target_pct}}%)
Trend: {{trend_direction}} from {{last_month_pct}}% last month
Total Tickets: {{total_tickets}}
Total Breaches: {{total_breaches}}

COMPLIANCE BY METRIC:
| Metric              | Target  | Actual  | Status | Trend    |
|---------------------|---------|---------|--------|----------|
| First Response Time | {{tgt}} | {{act}} | {{st}} | {{trnd}} |
| Resolution Time     | {{tgt}} | {{act}} | {{st}} | {{trnd}} |
| Uptime              | {{tgt}} | {{act}} | {{st}} | {{trnd}} |
| FCR Rate            | {{tgt}} | {{act}} | {{st}} | {{trnd}} |
| Customer Wait Time  | {{tgt}} | {{act}} | {{st}} | {{trnd}} |

BREACH ANALYSIS:
Total Breaches: {{total_breaches}}
- By Priority: P1: {{p1}}, P2: {{p2}}, P3: {{p3}}, P4: {{p4}}
- By Channel: Chat: {{chat}}, Email: {{email}}, Phone: {{phone}}
- By Day of Week: {{peak_day}} had most breaches ({{peak_count}})
- By Time of Day: {{peak_hour}} had highest breach rate

ROOT CAUSES:
1. {{cause_1}} - {{cause1_count}} breaches - {{cause1_action}}
2. {{cause_2}} - {{cause2_count}} breaches - {{cause2_action}}
3. {{cause_3}} - {{cause3_count}} breaches - {{cause3_action}}

RECOMMENDATIONS:
1. {{recommendation_1}}
2. {{recommendation_2}}
3. {{recommendation_3}}

NEXT MONTH TARGETS:
- Overall compliance: {{next_target}}%
- Focus area: {{focus_area}}
- Staffing changes: {{staffing_notes}}
```

### Remediation Plan Format

```
SLA REMEDIATION PLAN
Trigger: Compliance dropped below {{threshold}}% for {{duration}}
Owner: {{plan_owner}}
Start Date: {{start_date}}
Review Date: {{review_date}}

PROBLEM STATEMENT:
{{problem_description}}

ROOT CAUSE ANALYSIS:
- Primary cause: {{primary_cause}}
- Contributing factors: {{contributing_factors}}
- Data supporting analysis: {{evidence}}

ACTION ITEMS:
| # | Action | Owner | Deadline | Status | Impact |
|---|--------|-------|----------|--------|--------|
| 1 | {{action}} | {{owner}} | {{date}} | {{status}} | {{impact}} |
| 2 | {{action}} | {{owner}} | {{date}} | {{status}} | {{impact}} |
| 3 | {{action}} | {{owner}} | {{date}} | {{status}} | {{impact}} |

SUCCESS CRITERIA:
- {{metric_1}} reaches {{target_1}} by {{date_1}}
- {{metric_2}} reaches {{target_2}} by {{date_2}}
- No P1/P2 breaches for {{consecutive_days}} consecutive days

ESCALATION:
If targets not met by {{review_date}}, escalate to {{escalation_contact}}
```

## SLA Negotiation Guidelines

| Factor | Consideration | Recommendation |
|--------|--------------|----------------|
| **Customer tier** | Higher tiers expect stricter SLAs | Match tier to realistic targets |
| **Historical performance** | Only commit to what you can sustain | Set targets at 90th percentile of actuals |
| **Penalty structure** | Financial vs. service credits | Cap penalties at 10-15% of monthly fee |
| **Exclusions** | Maintenance windows, force majeure | Document clearly, review annually |
| **Measurement method** | Business hours vs. calendar hours | Align with customer expectations |
| **Reporting frequency** | Monthly standard, weekly for enterprise | Automate to reduce overhead |

## Scripts & Tools

**check_sla_status.py**: Real-time SLA compliance check
```bash
python scripts/check_sla_status.py --tier enterprise --period today
# Output: Current compliance rates, at-risk tickets, breaches
```

**generate_sla_report.py**: Generate compliance reports
```bash
python scripts/generate_sla_report.py --period 2024-Q1 --format pdf
# Output: Formatted SLA compliance report
```

**alert_sla_breach.py**: Configure breach notifications
```bash
python scripts/alert_sla_breach.py --ticket 12345 --metric response_time
# Output: Breach notification sent to escalation chain
```

**forecast_compliance.py**: Predict compliance based on current trends
```bash
python scripts/forecast_compliance.py --period next-week --confidence 0.9
# Output: Predicted compliance rates with confidence intervals
```

## Best Practices

1. **Measure business hours** - Align SLA clocks with agreed support hours, not calendar time
2. **Pause on customer wait** - Stop the clock when waiting for customer response
3. **Automate alerts** - Proactive warnings at 70%, 80%, and 90% of elapsed time
4. **Track near-misses** - Tickets resolved within 90-100% of SLA are warning signs
5. **Segment reporting** - Aggregate numbers hide tier-specific problems
6. **Review quarterly** - SLA targets should evolve with capacity and customer needs
7. **Document exclusions** - Planned maintenance and force majeure must be clearly defined
8. **Correlate with CSAT** - SLA compliance without satisfaction is meaningless

## Related Skills

- Escalation handling: `escalation-handler`
- Customer satisfaction: `csat-survey-designer`
- Ticket management: `ticket-triage`
