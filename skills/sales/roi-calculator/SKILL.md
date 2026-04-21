---
name: roi-calculator
description: Build ROI and TCO calculations to quantify value for prospects. Use when the user mentions "ROI calculation," "return on investment," "TCO analysis," "total cost of ownership," "business case," "payback period," "cost-benefit analysis," "value justification," "cost savings," or "investment analysis."
metadata:
  version: 1.0.0
  category: sales
---

# ROI Calculator

Build compelling ROI and TCO calculations that quantify the financial value of your solution for prospects and customers.

## Purpose

Create data-driven business cases that translate product capabilities into financial outcomes. Covers ROI formulas, TCO frameworks, payback period analysis, sensitivity modeling, and presentation formats for different buyer personas.

## Quick Reference

### ROI Formula Components

| Component | Definition | How to Calculate |
|-----------|-----------|------------------|
| **Investment Cost** | Total cost of solution | License + Implementation + Training + Ongoing |
| **Gains** | Revenue and savings from solution | Revenue uplift + Cost savings + Productivity gains |
| **ROI %** | Return on investment | ((Gains - Investment) / Investment) x 100 |
| **Net Benefit** | Total value minus total cost | Total Gains - Total Investment |
| **Payback Period** | Time to recoup investment | Investment / Monthly Net Benefit |
| **NPV** | Net present value | Sum of discounted future cash flows - Investment |
| **IRR** | Internal rate of return | Rate where NPV = 0 |

### ROI Calculation Framework

```
ROI CALCULATION:

GAINS (Annual):
  Revenue Increase:         ${{revenue_gain}}
  Cost Reduction:           ${{cost_savings}}
  Productivity Savings:     ${{productivity_gain}}
  Risk Avoidance:           ${{risk_value}}
  ─────────────────────────────────────
  Total Annual Gains:       ${{total_gains}}

INVESTMENT (Year 1):
  Software License:         ${{license_cost}}
  Implementation:           ${{impl_cost}}
  Training:                 ${{training_cost}}
  Integration:              ${{integration_cost}}
  ─────────────────────────────────────
  Total Year 1 Investment:  ${{total_investment}}

Ongoing Annual Cost:        ${{annual_cost}}

ROI = (${{total_gains}} - ${{annual_cost}}) / ${{total_investment}} x 100
ROI = {{roi_percentage}}%

Payback Period = ${{total_investment}} / (${{total_gains}} - ${{annual_cost}}) x 12
Payback Period = {{payback_months}} months
```

## Workflow

### ROI Analysis Checklist

```
ROI Build Progress:
- [ ] Step 1: Identify prospect's current costs and pain points
- [ ] Step 2: Quantify current state costs (labor, tools, inefficiency)
- [ ] Step 3: Map solution capabilities to financial outcomes
- [ ] Step 4: Gather prospect-specific data (headcount, volume, rates)
- [ ] Step 5: Calculate direct cost savings
- [ ] Step 6: Calculate productivity/efficiency gains
- [ ] Step 7: Estimate revenue impact (if applicable)
- [ ] Step 8: Total all investment costs (license, implementation, ongoing)
- [ ] Step 9: Calculate ROI, payback period, 3-year NPV
- [ ] Step 10: Run sensitivity analysis (conservative/moderate/aggressive)
- [ ] Step 11: Build visual presentation
- [ ] Step 12: Review with champion before presenting to CFO
```

## Templates

### TCO Framework

```
TOTAL COST OF OWNERSHIP COMPARISON
3-Year Analysis: Current State vs. {{our_solution}}

                        CURRENT STATE    OUR SOLUTION     DELTA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DIRECT COSTS:
Software licenses       ${{curr}}        ${{ours}}        ${{delta}}
Hardware/infrastructure  ${{curr}}        ${{ours}}        ${{delta}}
Implementation/setup     ${{curr}}        ${{ours}}        ${{delta}}
Training                 ${{curr}}        ${{ours}}        ${{delta}}
Annual maintenance       ${{curr}}        ${{ours}}        ${{delta}}
Support fees             ${{curr}}        ${{ours}}        ${{delta}}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Subtotal Direct:         ${{sub}}         ${{sub}}         ${{delta}}

INDIRECT COSTS:
Staff time (admin)       ${{curr}}        ${{ours}}        ${{delta}}
Downtime costs           ${{curr}}        ${{ours}}        ${{delta}}
Integration maintenance  ${{curr}}        ${{ours}}        ${{delta}}
Workaround labor         ${{curr}}        ${{ours}}        ${{delta}}
Compliance/audit costs   ${{curr}}        ${{ours}}        ${{delta}}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Subtotal Indirect:       ${{sub}}         ${{sub}}         ${{delta}}

OPPORTUNITY COSTS:
Lost revenue (downtime)  ${{curr}}        ${{ours}}        ${{delta}}
Delayed time-to-market   ${{curr}}        ${{ours}}        ${{delta}}
Customer churn impact    ${{curr}}        ${{ours}}        ${{delta}}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Subtotal Opportunity:    ${{sub}}         ${{sub}}         ${{delta}}

═══════════════════════════════════════════════════════════════
3-YEAR TCO:              ${{total_curr}}  ${{total_ours}}  ${{savings}}
═══════════════════════════════════════════════════════════════

TCO Savings: ${{savings}} ({{savings_pct}}% reduction)
```

### Cost Categories Deep Dive

```
COST CATEGORY BREAKDOWN

DIRECT COSTS (hard costs with invoices):
┌─────────────────────────────────────────────────────────┐
│ Category           │ Year 1    │ Year 2    │ Year 3    │
├─────────────────────────────────────────────────────────┤
│ License/subscription│ ${{y1}}  │ ${{y2}}  │ ${{y3}}  │
│ Implementation      │ ${{y1}}  │ —        │ —        │
│ Data migration      │ ${{y1}}  │ —        │ —        │
│ Training (initial)  │ ${{y1}}  │ —        │ —        │
│ Training (ongoing)  │ —        │ ${{y2}}  │ ${{y3}}  │
│ Support tier        │ ${{y1}}  │ ${{y2}}  │ ${{y3}}  │
│ Add-ons/modules     │ ${{y1}}  │ ${{y2}}  │ ${{y3}}  │
├─────────────────────────────────────────────────────────┤
│ TOTAL DIRECT        │ ${{t1}}  │ ${{t2}}  │ ${{t3}}  │
└─────────────────────────────────────────────────────────┘

INDIRECT COSTS (labor and productivity):
Calculate using: Hours per week x Hourly rate x 52 weeks

│ Activity              │ Hours/Week │ Rate    │ Annual Cost │
├───────────────────────┼────────────┼─────────┼─────────────┤
│ System administration │ {{h}}      │ ${{r}}  │ ${{c}}      │
│ Manual data entry     │ {{h}}      │ ${{r}}  │ ${{c}}      │
│ Report generation     │ {{h}}      │ ${{r}}  │ ${{c}}      │
│ Troubleshooting       │ {{h}}      │ ${{r}}  │ ${{c}}      │
│ Workarounds           │ {{h}}      │ ${{r}}  │ ${{c}}      │
├───────────────────────┼────────────┼─────────┼─────────────┤
│ TOTAL INDIRECT        │ {{total_h}}│         │ ${{total}}  │

OPPORTUNITY COSTS (what you are missing out on):
│ Missed Opportunity         │ Estimated Annual Impact │
├────────────────────────────┼────────────────────────│
│ Revenue from faster launch │ ${{amount}}            │
│ Customers lost to downtime │ ${{amount}}            │
│ Deals lost to slow process │ ${{amount}}            │
│ Talent attrition (tooling) │ ${{amount}}            │
```

### Sensitivity Analysis Template

```
SENSITIVITY ANALYSIS
Scenarios: Conservative / Moderate / Aggressive

                     CONSERVATIVE   MODERATE     AGGRESSIVE
                     (75% of est.)  (100%)       (125%)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Annual Gains:        ${{cons_gain}}  ${{mod_gain}} ${{agg_gain}}
Annual Cost:         ${{cons_cost}}  ${{mod_cost}} ${{agg_cost}}
Net Annual Benefit:  ${{cons_net}}   ${{mod_net}}  ${{agg_net}}
3-Year ROI:          {{cons_roi}}%   {{mod_roi}}%  {{agg_roi}}%
Payback Period:      {{cons_pb}} mo  {{mod_pb}} mo {{agg_pb}} mo
NPV (3-year):        ${{cons_npv}}   ${{mod_npv}}  ${{agg_npv}}

BREAK-EVEN ANALYSIS:
Minimum adoption rate for positive ROI: {{breakeven_pct}}%
Minimum cost savings for positive ROI: ${{breakeven_savings}}
Maximum acceptable price increase: {{max_price_increase}}%

KEY ASSUMPTIONS:
1. {{assumption_1}} — Sensitivity: {{high/medium/low}}
2. {{assumption_2}} — Sensitivity: {{high/medium/low}}
3. {{assumption_3}} — Sensitivity: {{high/medium/low}}
4. {{assumption_4}} — Sensitivity: {{high/medium/low}}

RISK ADJUSTMENTS:
- Implementation delay (30-day): Impact on ROI: {{impact}}
- Lower adoption (50% in Year 1): Impact on ROI: {{impact}}
- Price increase (10% Year 2): Impact on ROI: {{impact}}
```

### ROI Presentation Format

```
ROI BUSINESS CASE
Prepared for: {{company_name}}
Prepared by: {{sales_rep}}
Date: {{date}}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SLIDE 1: THE OPPORTUNITY
Current challenges:
• {{pain_point_1}} costing ${{amount}}/year
• {{pain_point_2}} costing ${{amount}}/year
• {{pain_point_3}} costing ${{amount}}/year
Total cost of status quo: ${{total_cost}}/year

SLIDE 2: THE SOLUTION
{{solution_overview}}
Key capabilities that address your challenges:
• {{capability_1}} → Eliminates {{pain_1}}
• {{capability_2}} → Reduces {{pain_2}}
• {{capability_3}} → Improves {{pain_3}}

SLIDE 3: FINANCIAL IMPACT
| Category | Annual Value |
|----------|-------------|
| Cost savings | ${{savings}} |
| Revenue impact | ${{revenue}} |
| Productivity gains | ${{productivity}} |
| Risk reduction | ${{risk}} |
| **Total Annual Value** | **${{total}}** |

SLIDE 4: INVESTMENT & RETURN
Investment: ${{investment}}
Annual Value: ${{value}}
ROI: {{roi}}%
Payback: {{months}} months
3-Year NPV: ${{npv}}

SLIDE 5: PROOF POINTS
Similar customer results:
• {{customer_1}}: {{result_1}}
• {{customer_2}}: {{result_2}}
• {{customer_3}}: {{result_3}}

SLIDE 6: NEXT STEPS
1. {{next_step_1}}
2. {{next_step_2}}
3. {{next_step_3}}
```

### Industry-Specific ROI Benchmarks

| Industry | Primary Value Driver | Typical ROI Range | Payback Period |
|----------|---------------------|-------------------|----------------|
| **SaaS/Tech** | Productivity, speed to market | 150-300% | 6-12 months |
| **Financial Services** | Risk reduction, compliance | 100-250% | 8-14 months |
| **Healthcare** | Error reduction, efficiency | 120-200% | 10-18 months |
| **Manufacturing** | Downtime reduction, yield | 100-250% | 8-16 months |
| **Retail/E-commerce** | Revenue uplift, conversion | 150-400% | 4-10 months |
| **Professional Services** | Utilization, margin | 100-200% | 6-12 months |

### Payback Period Calculation

```
PAYBACK PERIOD ANALYSIS

INVESTMENT TIMELINE:
Month 0:   Implementation start     Cost: ${{impl_cost}}
Month 1-2: Training and rollout     Cost: ${{training_cost}}
Month 3:   Go-live                  Cost: ${{go_live_cost}}
Month 3+:  Monthly subscription     Cost: ${{monthly_cost}}/mo

BENEFIT RAMP:
Month 1-3: Onboarding (25% benefit) Monthly: ${{m1_benefit}}
Month 4-6: Adoption (50% benefit)   Monthly: ${{m2_benefit}}
Month 7-9: Optimization (75%)       Monthly: ${{m3_benefit}}
Month 10+: Full value (100%)        Monthly: ${{m4_benefit}}

CUMULATIVE CASH FLOW:
| Month | Cumulative Cost | Cumulative Benefit | Net Position |
|-------|----------------|--------------------|-------------|
| 3     | ${{cost}}      | ${{benefit}}       | -${{net}}   |
| 6     | ${{cost}}      | ${{benefit}}       | -${{net}}   |
| 9     | ${{cost}}      | ${{benefit}}       | +${{net}}   |
| 12    | ${{cost}}      | ${{benefit}}       | +${{net}}   |

BREAKEVEN: Month {{breakeven_month}}
```

## Scripts & Tools

**calculate_roi.py**: Build ROI model from inputs
```bash
python scripts/calculate_roi.py --investment 150000 --annual-savings 200000 --years 3
# Output: ROI percentage, payback period, NPV, sensitivity ranges
```

**tco_comparison.py**: Generate TCO comparison between current and proposed
```bash
python scripts/tco_comparison.py --current-costs costs.json --proposed-costs proposal.json
# Output: Side-by-side TCO with 3-year projections
```

**sensitivity_analysis.py**: Run sensitivity model across assumptions
```bash
python scripts/sensitivity_analysis.py --model roi_model.json --scenarios 3
# Output: Conservative, moderate, aggressive scenarios with breakeven
```

**roi_presentation.py**: Generate presentation-ready ROI slides
```bash
python scripts/roi_presentation.py --model roi_model.json --format pptx
# Output: Formatted ROI presentation deck
```

## Best Practices

1. **Use customer's own numbers** - Their data is more credible than your benchmarks
2. **Be conservative** - CFOs discount aggressive projections; under-promise and over-deliver
3. **Show the cost of doing nothing** - Status quo has a price; quantify it
4. **Include soft benefits but label them** - Acknowledge intangible value without inflating ROI
5. **Build with the champion** - Co-create the business case so they own the numbers
6. **Tailor to the buyer** - CFOs want NPV/IRR; VPs want productivity; CEOs want strategic impact
7. **Account for ramp time** - No solution delivers 100% value on day one
8. **Benchmark against similar customers** - Social proof makes numbers believable
9. **Prepare for scrutiny** - Document every assumption; be ready to defend each number
10. **Update post-sale** - Track actual ROI to build future business cases

## Related Skills

- Competitive pricing: `competitive-battlecard`
- Proposal writing: `proposal-writer`
- Sales reporting: `sales-report-writer`
