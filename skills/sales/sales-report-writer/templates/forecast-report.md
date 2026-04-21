# Forecast Report Template

## Report Header

| Field | Value |
|-------|-------|
| **Fiscal Period** | {{fiscal_period}} |
| **Period End Date** | {{period_end_date}} |
| **Days Remaining** | {{days_left}} |
| **Generated** | {{date}} |
| **Prepared By** | {{author}} |

---

## Forecast Summary

| Category | Amount | # Deals | Avg Size | vs. Last Week |
|----------|--------|---------|----------|--------------|
| **Closed Won (to date)** | ${{closed}} | {{n}} | ${{avg}} | +${{delta}} |
| **Commit** | ${{commit}} | {{n}} | ${{avg}} | {{sign}}${{delta}} |
| **Best Case** | ${{best}} | {{n}} | ${{avg}} | {{sign}}${{delta}} |
| **Pipeline (upside)** | ${{upside}} | {{n}} | ${{avg}} | {{sign}}${{delta}} |
| **Total Forecast** | **${{total}}** | **{{n}}** | **${{avg}}** | **{{sign}}${{delta}}** |

---

## Quota Attainment

| Metric | Value |
|--------|-------|
| **Team Quota** | ${{quota}} |
| **Closed Won** | ${{closed}} ({{pct_closed}}% of quota) |
| **Closed + Commit** | ${{closed_commit}} ({{pct_cc}}% of quota) |
| **Closed + Commit + Best Case** | ${{closed_commit_best}} ({{pct_ccb}}% of quota) |
| **Gap to Quota** | ${{gap}} |
| **Required Close Rate on Commit** | {{required_pct}}% |
| **Required Close Rate on Commit + Best Case** | {{required_pct_all}}% |

---

## Forecast by Rep

| Rep | Quota | Closed | Commit | Best Case | Pipeline | Total Forecast | Attainment |
|-----|-------|--------|--------|-----------|----------|---------------|------------|
| {{rep_1}} | ${{q}} | ${{c}} | ${{cm}} | ${{bc}} | ${{p}} | ${{t}} | {{pct}}% |
| {{rep_2}} | ${{q}} | ${{c}} | ${{cm}} | ${{bc}} | ${{p}} | ${{t}} | {{pct}}% |
| {{rep_3}} | ${{q}} | ${{c}} | ${{cm}} | ${{bc}} | ${{p}} | ${{t}} | {{pct}}% |
| {{rep_4}} | ${{q}} | ${{c}} | ${{cm}} | ${{bc}} | ${{p}} | ${{t}} | {{pct}}% |
| **Team** | **${{q}}** | **${{c}}** | **${{cm}}** | **${{bc}}** | **${{p}}** | **${{t}}** | **{{pct}}%** |

---

## Forecast by Segment

| Segment | Closed | Commit | Best Case | Pipeline | Total | % of Quota |
|---------|--------|--------|-----------|----------|-------|-----------|
| **Enterprise** | ${{c}} | ${{cm}} | ${{bc}} | ${{p}} | ${{t}} | {{pct}}% |
| **Mid-Market** | ${{c}} | ${{cm}} | ${{bc}} | ${{p}} | ${{t}} | {{pct}}% |
| **SMB** | ${{c}} | ${{cm}} | ${{bc}} | ${{p}} | ${{t}} | {{pct}}% |

---

## Forecast by Product

| Product | Closed | Commit | Best Case | Total | vs. Target |
|---------|--------|--------|-----------|-------|-----------|
| {{product_1}} | ${{c}} | ${{cm}} | ${{bc}} | ${{t}} | {{status}} |
| {{product_2}} | ${{c}} | ${{cm}} | ${{bc}} | ${{t}} | {{status}} |
| {{product_3}} | ${{c}} | ${{cm}} | ${{bc}} | ${{t}} | {{status}} |

---

## Week-over-Week Forecast Movement

| Week | Closed | Commit | Best Case | Total | Change |
|------|--------|--------|-----------|-------|--------|
| {{week_4_ago}} | ${{c}} | ${{cm}} | ${{bc}} | ${{t}} | -- |
| {{week_3_ago}} | ${{c}} | ${{cm}} | ${{bc}} | ${{t}} | {{sign}}${{delta}} |
| {{week_2_ago}} | ${{c}} | ${{cm}} | ${{bc}} | ${{t}} | {{sign}}${{delta}} |
| {{last_week}} | ${{c}} | ${{cm}} | ${{bc}} | ${{t}} | {{sign}}${{delta}} |
| **This Week** | **${{c}}** | **${{cm}}** | **${{bc}}** | **${{t}}** | **{{sign}}${{delta}}** |

---

## Commit Deals Detail

| Deal | Account | Amount | Close Date | Rep | Confidence | Next Step |
|------|---------|--------|-----------|-----|------------|-----------|
| {{deal_1}} | {{acct}} | ${{amt}} | {{date}} | {{rep}} | {{High/Med}} | {{step}} |
| {{deal_2}} | {{acct}} | ${{amt}} | {{date}} | {{rep}} | {{High/Med}} | {{step}} |
| {{deal_3}} | {{acct}} | ${{amt}} | {{date}} | {{rep}} | {{High/Med}} | {{step}} |

---

## Risks to Forecast

| Risk | Impact | Probability | Affected Deals | Mitigation |
|------|--------|-------------|---------------|------------|
| {{risk_1}} | ${{amount}} | {{High/Med/Low}} | {{deals}} | {{action}} |
| {{risk_2}} | ${{amount}} | {{High/Med/Low}} | {{deals}} | {{action}} |
| {{risk_3}} | ${{amount}} | {{High/Med/Low}} | {{deals}} | {{action}} |

**Total Risk Exposure:** ${{total_risk}}

---

## Upside Opportunities

| Opportunity | Potential | Probability | Expected Close | What Needs to Happen |
|-------------|----------|-------------|---------------|---------------------|
| {{opp_1}} | ${{amount}} | {{pct}}% | {{date}} | {{requirement}} |
| {{opp_2}} | ${{amount}} | {{pct}}% | {{date}} | {{requirement}} |
| {{opp_3}} | ${{amount}} | {{pct}}% | {{date}} | {{requirement}} |

**Total Upside Potential:** ${{total_upside}}

---

## Forecast Methodology

| Category | Probability Range | Criteria |
|----------|------------------|----------|
| **Commit** | >80% | Decision maker engaged, timeline confirmed, budget approved, verbal commitment |
| **Best Case** | 50-80% | Champion identified, budget allocated, active evaluation, strong engagement |
| **Pipeline** | 20-50% | Qualified opportunity, discovery complete or in progress |
| **Upside** | <20% | Early stage, not fully qualified, speculative |

---

## Commentary

### Forecast Narrative

{{narrative_explaining_current_forecast_position_and_trajectory}}

### Key Changes This Week

1. {{change_1}}
2. {{change_2}}
3. {{change_3}}

### Actions to Close the Gap

| Action | Owner | Timeline | Expected Impact |
|--------|-------|----------|----------------|
| {{action_1}} | {{owner}} | {{timeline}} | ${{impact}} |
| {{action_2}} | {{owner}} | {{timeline}} | ${{impact}} |
| {{action_3}} | {{owner}} | {{timeline}} | ${{impact}} |
