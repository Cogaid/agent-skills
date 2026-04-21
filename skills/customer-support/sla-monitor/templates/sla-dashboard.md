# SLA Compliance Dashboard Template

## Dashboard Configuration

| Field | Value |
|-------|-------|
| **Dashboard ID** | SLA-DASH-001 |
| **Refresh Interval** | Every 5 minutes |
| **Default Period** | Rolling 24 hours |
| **Access** | Support team leads, managers, directors |

---

## Layout

### Section 1: Overall Compliance Header

```
SLA COMPLIANCE DASHBOARD
Date: {{date}}  |  Period: {{period}}  |  Last Updated: {{last_refresh}}

OVERALL COMPLIANCE: {{overall_pct}}%  Target: 95%
Status: [ON TRACK / AT RISK / BELOW TARGET]
```

**Color coding**:
- Green: >= 95% (meeting target)
- Yellow: 90-94.9% (at risk)
- Red: < 90% (below target)

---

### Section 2: Metric Breakdown

| Metric | Target | Actual | Trend | Status |
|--------|--------|--------|-------|--------|
| First Response Time | {{frt_target}} | {{frt_actual}}% | {{frt_trend}} | {{frt_status}} |
| Resolution Time | {{rt_target}} | {{rt_actual}}% | {{rt_trend}} | {{rt_status}} |
| Uptime | {{up_target}} | {{up_actual}}% | {{up_trend}} | {{up_status}} |
| FCR Rate | {{fcr_target}} | {{fcr_actual}}% | {{fcr_trend}} | {{fcr_status}} |
| Customer Wait Time | {{cwt_target}} | {{cwt_actual}}% | {{cwt_trend}} | {{cwt_status}} |

**Trend indicators**: Up arrow (improving), Down arrow (declining), Dash (stable, <1% change)

---

### Section 3: Tier Compliance

| Tier | Compliance | Breaches | At Risk | Status |
|------|-----------|----------|---------|--------|
| Enterprise | {{ent_pct}}% | {{ent_breaches}} | {{ent_atrisk}} | {{ent_status}} |
| Premium | {{prem_pct}}% | {{prem_breaches}} | {{prem_atrisk}} | {{prem_status}} |
| Standard | {{std_pct}}% | {{std_breaches}} | {{std_atrisk}} | {{std_status}} |
| Basic | {{bas_pct}}% | {{bas_breaches}} | {{bas_atrisk}} | {{bas_status}} |

---

### Section 4: Active Alerts

| Severity | Count | Description |
|----------|-------|-------------|
| Critical (breached) | {{critical_count}} | Tickets that have breached SLA |
| At Risk (>80% elapsed) | {{atrisk_count}} | Tickets approaching SLA deadline |
| On Track | {{ontrack_count}} | Tickets within SLA parameters |

**Alert drill-down**: Click any count to see the individual ticket list.

---

### Section 5: Top Breach Categories

| Rank | Category | Breach Count | % of Total | Root Cause |
|------|----------|-------------|------------|------------|
| 1 | {{category_1}} | {{cat1_count}} | {{cat1_pct}}% | {{cat1_cause}} |
| 2 | {{category_2}} | {{cat2_count}} | {{cat2_pct}}% | {{cat2_cause}} |
| 3 | {{category_3}} | {{cat3_count}} | {{cat3_pct}}% | {{cat3_cause}} |

---

### Section 6: 30-Day Trend Chart

```
Compliance %
100|          * *
 95|    * * *     * *
 90|  *               * *
 85|*                     *
   +--+--+--+--+--+--+--+--
   W1  W2  W3  W4 (weeks)

--- Target (95%)    * Actual
```

---

## Dashboard Variables

| Variable | Source | Update Frequency |
|----------|--------|-----------------|
| `{{overall_pct}}` | Calculated from all metrics | Every 5 minutes |
| `{{frt_*}}` | Ticketing system API | Every 5 minutes |
| `{{rt_*}}` | Ticketing system API | Every 5 minutes |
| `{{up_*}}` | Uptime monitoring service | Every 1 minute |
| `{{fcr_*}}` | Calculated from ticket reopens | Every 15 minutes |
| `{{*_breaches}}` | SLA breach log | Real-time |
| `{{*_atrisk}}` | SLA time remaining calculation | Every 5 minutes |
