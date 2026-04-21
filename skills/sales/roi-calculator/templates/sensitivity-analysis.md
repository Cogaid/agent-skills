# Sensitivity Analysis Template

## Analysis Header

| Field | Value |
|-------|-------|
| **Base Model** | {{model_name}} |
| **Prepared For** | {{company_name}} |
| **Date** | {{date}} |
| **Analyst** | {{author}} |

---

## Base Case Summary

| Metric | Base Case Value |
|--------|----------------|
| **Total Investment** | ${{investment}} |
| **Annual Gains** | ${{annual_gains}} |
| **Annual Cost** | ${{annual_cost}} |
| **Net Annual Benefit** | ${{net_benefit}} |
| **3-Year ROI** | {{roi}}% |
| **Payback Period** | {{payback}} months |
| **NPV** | ${{npv}} |

---

## Scenario Analysis

### Three Scenarios

| Metric | Conservative (75%) | Moderate (100%) | Aggressive (125%) |
|--------|-------------------|-----------------|-------------------|
| **Annual Gains** | ${{cons_gain}} | ${{mod_gain}} | ${{agg_gain}} |
| **Annual Cost** | ${{cons_cost}} | ${{mod_cost}} | ${{agg_cost}} |
| **Net Annual Benefit** | ${{cons_net}} | ${{mod_net}} | ${{agg_net}} |
| **3-Year ROI** | {{cons_roi}}% | {{mod_roi}}% | {{agg_roi}}% |
| **Payback Period** | {{cons_pb}} months | {{mod_pb}} months | {{agg_pb}} months |
| **3-Year NPV** | ${{cons_npv}} | ${{mod_npv}} | ${{agg_npv}} |
| **3-Year Net Benefit** | ${{cons_total}} | ${{mod_total}} | ${{agg_total}} |

---

## Variable Sensitivity

### Impact of Individual Variables on ROI

| Variable | -25% | -10% | Base | +10% | +25% | Sensitivity |
|----------|------|------|------|------|------|------------|
| **Adoption rate** | {{roi}}% | {{roi}}% | {{roi}}% | {{roi}}% | {{roi}}% | {{High/Med/Low}} |
| **License cost** | {{roi}}% | {{roi}}% | {{roi}}% | {{roi}}% | {{roi}}% | {{High/Med/Low}} |
| **Headcount affected** | {{roi}}% | {{roi}}% | {{roi}}% | {{roi}}% | {{roi}}% | {{High/Med/Low}} |
| **Productivity improvement** | {{roi}}% | {{roi}}% | {{roi}}% | {{roi}}% | {{roi}}% | {{High/Med/Low}} |
| **Implementation timeline** | {{roi}}% | {{roi}}% | {{roi}}% | {{roi}}% | {{roi}}% | {{High/Med/Low}} |
| **Revenue growth rate** | {{roi}}% | {{roi}}% | {{roi}}% | {{roi}}% | {{roi}}% | {{High/Med/Low}} |

### Most Impactful Variables (Ranked)

1. **{{variable_1}}** -- {{pct}}% ROI swing for 25% change -- Sensitivity: High
2. **{{variable_2}}** -- {{pct}}% ROI swing for 25% change -- Sensitivity: High
3. **{{variable_3}}** -- {{pct}}% ROI swing for 25% change -- Sensitivity: Medium
4. **{{variable_4}}** -- {{pct}}% ROI swing for 25% change -- Sensitivity: Low

---

## Break-Even Analysis

### Minimum Thresholds for Positive ROI

| Variable | Break-Even Value | Base Case Value | Margin of Safety |
|----------|-----------------|----------------|-----------------|
| **Adoption rate** | {{breakeven}}% | {{base}}% | {{margin}} pts |
| **Cost savings** | ${{breakeven}}/yr | ${{base}}/yr | ${{margin}} |
| **Productivity gain** | {{breakeven}}% | {{base}}% | {{margin}} pts |
| **Maximum acceptable price** | ${{breakeven}}/yr | ${{base}}/yr | ${{margin}} |
| **Maximum implementation cost** | ${{breakeven}} | ${{base}} | ${{margin}} |

### Break-Even Timeline

| Scenario | Break-Even Month | Cumulative Cost at Break-Even | Cumulative Benefit at Break-Even |
|----------|-----------------|------------------------------|--------------------------------|
| **Conservative** | Month {{n}} | ${{cost}} | ${{benefit}} |
| **Moderate** | Month {{n}} | ${{cost}} | ${{benefit}} |
| **Aggressive** | Month {{n}} | ${{cost}} | ${{benefit}} |

---

## Risk Adjustments

| Risk Factor | Probability | Impact on ROI | Risk-Adjusted Impact | Mitigation |
|-------------|------------|---------------|---------------------|-----------|
| **Implementation delay (30 days)** | {{pct}}% | -{{impact}}% ROI | -{{adjusted}}% | {{mitigation}} |
| **Lower adoption (50% in Year 1)** | {{pct}}% | -{{impact}}% ROI | -{{adjusted}}% | {{mitigation}} |
| **Price increase (10% Year 2)** | {{pct}}% | -{{impact}}% ROI | -{{adjusted}}% | {{mitigation}} |
| **Staff turnover during rollout** | {{pct}}% | -{{impact}}% ROI | -{{adjusted}}% | {{mitigation}} |
| **Integration complexity** | {{pct}}% | -{{impact}}% ROI | -{{adjusted}}% | {{mitigation}} |

### Risk-Adjusted ROI

| Metric | Unadjusted | Risk-Adjusted |
|--------|-----------|--------------|
| **3-Year ROI** | {{roi}}% | {{adj_roi}}% |
| **NPV** | ${{npv}} | ${{adj_npv}} |
| **Payback** | {{pb}} months | {{adj_pb}} months |

---

## Key Assumptions

| # | Assumption | Value | Sensitivity | Rationale |
|---|-----------|-------|-------------|-----------|
| 1 | {{assumption}} | {{value}} | {{High/Med/Low}} | {{rationale}} |
| 2 | {{assumption}} | {{value}} | {{High/Med/Low}} | {{rationale}} |
| 3 | {{assumption}} | {{value}} | {{High/Med/Low}} | {{rationale}} |
| 4 | {{assumption}} | {{value}} | {{High/Med/Low}} | {{rationale}} |
| 5 | {{assumption}} | {{value}} | {{High/Med/Low}} | {{rationale}} |

---

## Recommendation

Based on the sensitivity analysis:

- **Even in the conservative scenario**, the investment delivers a {{cons_roi}}% ROI with a {{cons_pb}}-month payback.
- **The most critical variable** is {{variable}}, which should be closely monitored during implementation.
- **Break-even requires only** {{breakeven_pct}}% of estimated gains, providing a {{margin}}% margin of safety.

**Conclusion:** {{recommendation_text}}
