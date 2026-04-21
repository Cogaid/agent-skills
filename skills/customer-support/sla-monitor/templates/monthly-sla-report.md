# Monthly SLA Compliance Report Template

## Report Header

| Field | Value |
|-------|-------|
| **Report Period** | {{month}} {{year}} |
| **Generated** | {{report_date}} |
| **Prepared By** | {{author}} |
| **Distribution** | {{distribution_list}} |
| **Classification** | Internal / Customer-facing (select one) |

---

## Executive Summary

**Overall SLA Compliance**: {{overall_pct}}% (target: {{target_pct}}%)

**Trend**: {{trend_direction}} from {{last_month_pct}}% last month

**Total Tickets**: {{total_tickets}}

**Total Breaches**: {{total_breaches}} ({{breach_rate}}% breach rate)

**Key Takeaway**: {{one_line_summary}}

---

## Compliance by Metric

| Metric | Target | Actual | Status | Trend vs Last Month |
|--------|--------|--------|--------|-------------------|
| First Response Time | {{frt_target}}% | {{frt_actual}}% | {{frt_status}} | {{frt_trend}} |
| Resolution Time | {{rt_target}}% | {{rt_actual}}% | {{rt_status}} | {{rt_trend}} |
| Uptime | {{up_target}}% | {{up_actual}}% | {{up_status}} | {{up_trend}} |
| FCR Rate | {{fcr_target}}% | {{fcr_actual}}% | {{fcr_status}} | {{fcr_trend}} |
| Customer Wait Time | {{cwt_target}} | {{cwt_actual}} | {{cwt_status}} | {{cwt_trend}} |

---

## Compliance by Tier

| Tier | Target | Actual | Breaches | Trend |
|------|--------|--------|----------|-------|
| Enterprise | 99% | {{ent_actual}}% | {{ent_breaches}} | {{ent_trend}} |
| Premium | 97% | {{prem_actual}}% | {{prem_breaches}} | {{prem_trend}} |
| Standard | 95% | {{std_actual}}% | {{std_breaches}} | {{std_trend}} |
| Basic | 90% | {{bas_actual}}% | {{bas_breaches}} | {{bas_trend}} |

---

## Breach Analysis

### Breach Summary

| Dimension | Breakdown |
|-----------|-----------|
| By Priority | P1: {{p1_count}}, P2: {{p2_count}}, P3: {{p3_count}}, P4: {{p4_count}} |
| By Channel | Chat: {{chat_count}}, Email: {{email_count}}, Phone: {{phone_count}} |
| By Day of Week | Peak: {{peak_day}} ({{peak_day_count}} breaches) |
| By Time of Day | Peak: {{peak_hour}} ({{peak_hour_count}} breaches) |

### Root Cause Analysis

| Rank | Root Cause | Breach Count | % of Total | Action Taken |
|------|-----------|-------------|------------|-------------|
| 1 | {{cause_1}} | {{cause1_count}} | {{cause1_pct}}% | {{cause1_action}} |
| 2 | {{cause_2}} | {{cause2_count}} | {{cause2_pct}}% | {{cause2_action}} |
| 3 | {{cause_3}} | {{cause3_count}} | {{cause3_pct}}% | {{cause3_action}} |

---

## Recommendations

1. {{recommendation_1}}
2. {{recommendation_2}}
3. {{recommendation_3}}

---

## Next Month Targets

| Target | Value |
|--------|-------|
| Overall compliance | {{next_target}}% |
| Focus area | {{focus_area}} |
| Staffing changes | {{staffing_notes}} |
| Process changes | {{process_notes}} |

---

## Appendix: Incident Log

| Date | Ticket ID | Tier | Metric Breached | Overage | Root Cause | Resolved |
|------|-----------|------|----------------|---------|-----------|----------|
| {{date}} | #{{id}} | {{tier}} | {{metric}} | {{overage}} | {{cause}} | {{resolved}} |
