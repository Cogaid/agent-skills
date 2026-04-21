# TCO Comparison Template

## Analysis Header

| Field | Value |
|-------|-------|
| **Prepared For** | {{company_name}} |
| **Comparison** | Current State vs. {{our_solution}} |
| **Analysis Period** | {{years}} Years |
| **Prepared By** | {{author}} |
| **Date** | {{date}} |

---

## Executive Summary

| Metric | Current State | {{our_solution}} | Savings |
|--------|--------------|-------------------|---------|
| **{{years}}-Year TCO** | ${{total_current}} | ${{total_proposed}} | ${{savings}} |
| **Annual Average** | ${{avg_current}} | ${{avg_proposed}} | ${{avg_savings}} |
| **Savings %** | -- | -- | {{savings_pct}}% |

---

## Direct Costs

Costs with invoices, contracts, or purchase orders.

| Category | Current State | {{our_solution}} | Year 1 Delta | 3-Year Delta |
|----------|--------------|-------------------|-------------|-------------|
| **Software licenses** | ${{curr}}/yr | ${{ours}}/yr | ${{delta}} | ${{delta_3yr}} |
| **Hardware/infrastructure** | ${{curr}}/yr | ${{ours}}/yr | ${{delta}} | ${{delta_3yr}} |
| **Implementation/setup** | ${{curr}} (one-time) | ${{ours}} (one-time) | ${{delta}} | ${{delta_3yr}} |
| **Data migration** | -- | ${{ours}} (one-time) | -${{cost}} | -${{cost}} |
| **Training (initial)** | ${{curr}} | ${{ours}} | ${{delta}} | ${{delta_3yr}} |
| **Training (ongoing)** | ${{curr}}/yr | ${{ours}}/yr | ${{delta}} | ${{delta_3yr}} |
| **Annual maintenance** | ${{curr}}/yr | ${{ours}}/yr | ${{delta}} | ${{delta_3yr}} |
| **Support fees** | ${{curr}}/yr | ${{ours}}/yr | ${{delta}} | ${{delta_3yr}} |
| **Integration/middleware** | ${{curr}}/yr | ${{ours}}/yr | ${{delta}} | ${{delta_3yr}} |
| **Subtotal Direct** | **${{sub_curr}}** | **${{sub_ours}}** | **${{sub_delta}}** | **${{sub_delta_3yr}}** |

---

## Indirect Costs

Labor, productivity, and operational overhead.

| Category | Calculation | Current State | {{our_solution}} | Delta |
|----------|------------|--------------|-------------------|-------|
| **System administration** | {{hours}}/wk x ${{rate}}/hr x 52 | ${{curr}}/yr | ${{ours}}/yr | ${{delta}} |
| **Manual data entry** | {{hours}}/wk x ${{rate}}/hr x 52 | ${{curr}}/yr | ${{ours}}/yr | ${{delta}} |
| **Report generation** | {{hours}}/wk x ${{rate}}/hr x 52 | ${{curr}}/yr | ${{ours}}/yr | ${{delta}} |
| **Troubleshooting** | {{hours}}/wk x ${{rate}}/hr x 52 | ${{curr}}/yr | ${{ours}}/yr | ${{delta}} |
| **Workarounds** | {{hours}}/wk x ${{rate}}/hr x 52 | ${{curr}}/yr | ${{ours}}/yr | ${{delta}} |
| **Compliance/audit prep** | {{hours}}/yr x ${{rate}}/hr | ${{curr}}/yr | ${{ours}}/yr | ${{delta}} |
| **Integration maintenance** | {{hours}}/wk x ${{rate}}/hr x 52 | ${{curr}}/yr | ${{ours}}/yr | ${{delta}} |
| **Subtotal Indirect** | | **${{sub_curr}}/yr** | **${{sub_ours}}/yr** | **${{sub_delta}}/yr** |

---

## Opportunity Costs

Value not captured due to limitations of the current state.

| Category | Current State Impact | With {{our_solution}} | Recovered Value |
|----------|--------------------|-----------------------|----------------|
| **Revenue from faster time-to-market** | ${{curr_impact}}/yr | ${{new_impact}}/yr | ${{recovered}} |
| **Customers lost to downtime** | ${{curr_impact}}/yr | ${{new_impact}}/yr | ${{recovered}} |
| **Deals lost to slow processes** | ${{curr_impact}}/yr | ${{new_impact}}/yr | ${{recovered}} |
| **Talent attrition (poor tooling)** | ${{curr_impact}}/yr | ${{new_impact}}/yr | ${{recovered}} |
| **Innovation not pursued** | ${{curr_impact}}/yr | ${{new_impact}}/yr | ${{recovered}} |
| **Subtotal Opportunity** | **${{sub_curr}}/yr** | **${{sub_ours}}/yr** | **${{sub_recovered}}/yr** |

---

## 3-Year TCO Summary

| Cost Category | Year 1 | Year 2 | Year 3 | 3-Year Total |
|--------------|--------|--------|--------|-------------|
| **Current State** | | | | |
| Direct | ${{val}} | ${{val}} | ${{val}} | ${{total}} |
| Indirect | ${{val}} | ${{val}} | ${{val}} | ${{total}} |
| Opportunity | ${{val}} | ${{val}} | ${{val}} | ${{total}} |
| **Current Total** | **${{t1}}** | **${{t2}}** | **${{t3}}** | **${{grand}}** |
| | | | | |
| **{{our_solution}}** | | | | |
| Direct | ${{val}} | ${{val}} | ${{val}} | ${{total}} |
| Indirect | ${{val}} | ${{val}} | ${{val}} | ${{total}} |
| Opportunity | ${{val}} | ${{val}} | ${{val}} | ${{total}} |
| **Proposed Total** | **${{t1}}** | **${{t2}}** | **${{t3}}** | **${{grand}}** |
| | | | | |
| **Net Savings** | **${{s1}}** | **${{s2}}** | **${{s3}}** | **${{total_savings}}** |

---

## Hidden Cost Analysis

Costs frequently overlooked when comparing solutions:

| Hidden Cost | Current State | {{our_solution}} | Notes |
|-------------|--------------|-------------------|-------|
| **Per-seat pricing at scale** | ${{amount}} at {{n}} users | ${{amount}} at {{n}} users | {{note}} |
| **Overage charges** | ${{amount}}/yr avg | ${{amount}}/yr avg | {{note}} |
| **Annual price escalators** | {{pct}}%/yr | {{pct}}%/yr | {{note}} |
| **Premium support surcharge** | ${{amount}}/yr | Included | {{note}} |
| **Custom development** | ${{amount}}/yr | ${{amount}}/yr | {{note}} |
| **Exit/migration costs** | ${{amount}} (future) | ${{amount}} (future) | {{note}} |

---

## Assumptions

| # | Assumption | Value | Impact if Wrong |
|---|-----------|-------|----------------|
| 1 | {{assumption}} | {{value}} | {{impact}} |
| 2 | {{assumption}} | {{value}} | {{impact}} |
| 3 | {{assumption}} | {{value}} | {{impact}} |
| 4 | {{assumption}} | {{value}} | {{impact}} |
| 5 | {{assumption}} | {{value}} | {{impact}} |

---

## Data Sources

| Data Point | Source | Date | Confidence |
|-----------|--------|------|-----------|
| {{data_point}} | {{source}} | {{date}} | {{High/Med/Low}} |
| {{data_point}} | {{source}} | {{date}} | {{High/Med/Low}} |
| {{data_point}} | {{source}} | {{date}} | {{High/Med/Low}} |
