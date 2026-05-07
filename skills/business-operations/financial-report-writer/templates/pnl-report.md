# Profit & Loss Report Template

## Executive Summary Section

```
EXECUTIVE FINANCIAL SUMMARY
Period: {{period}} {{year}}
Prepared: {{prepared_date}}
Prepared by: {{preparer_name}}, {{preparer_title}}

--- HEADLINE NUMBERS -------------------------------------------------
Revenue:           {{revenue}}        ({{revenue_change}} vs. prior period)
Gross Margin:      {{gross_margin}}%  ({{gm_change}} vs. prior period)
Operating Expense: {{opex}}           ({{opex_change}} vs. budget)
Net Income:        {{net_income}}     ({{ni_change}} vs. prior period)
Cash Position:     {{cash_position}}  (runway: {{runway_months}} months)
Burn Rate:         {{burn_rate}}/mo

--- KEY HIGHLIGHTS ---------------------------------------------------
1. {{highlight_1}}
2. {{highlight_2}}
3. {{highlight_3}}

--- RISKS & WATCH ITEMS ----------------------------------------------
- {{risk_1}}
- {{risk_2}}

--- RECOMMENDED ACTIONS -----------------------------------------------
1. {{action_1}} (Owner: {{owner_1}}, Deadline: {{deadline_1}})
2. {{action_2}} (Owner: {{owner_2}}, Deadline: {{deadline_2}})
```

## Detailed P&L Template

```
PROFIT & LOSS STATEMENT
Period: {{start_date}} to {{end_date}}
Comparison: vs. Prior Period | vs. Budget

                          Actual      Budget     Variance   Prior Period   % Change
                         --------    --------    --------   ------------   --------
REVENUE
  Product Revenue        ${{pp_rev}} ${{pp_bud}} ${{pp_var}} ${{pp_pri}}  {{pp_chg}}%
  Service Revenue        ${{sr_rev}} ${{sr_bud}} ${{sr_var}} ${{sr_pri}}  {{sr_chg}}%
  Other Revenue          ${{or_rev}} ${{or_bud}} ${{or_var}} ${{or_pri}}  {{or_chg}}%
                         --------    --------    --------   ------------
  TOTAL REVENUE          ${{t_rev}}  ${{t_bud}}  ${{t_var}}  ${{t_pri}}  {{t_chg}}%

COST OF GOODS SOLD
  Direct Costs           ${{dc}}     ${{dc_b}}   ${{dc_v}}   ${{dc_p}}
  Hosting / Infra        ${{hi}}     ${{hi_b}}   ${{hi_v}}   ${{hi_p}}
                         --------    --------    --------   ------------
  TOTAL COGS             ${{cogs}}   ${{cogs_b}} ${{cogs_v}} ${{cogs_p}}

GROSS PROFIT             ${{gp}}     ${{gp_b}}   ${{gp_v}}   ${{gp_p}}
  Gross Margin              {{gm}}%     {{gm_b}}%                {{gm_p}}%

OPERATING EXPENSES
  Salaries & Benefits    ${{sal}}    ${{sal_b}}  ${{sal_v}}  ${{sal_p}}
  Sales & Marketing      ${{sm}}     ${{sm_b}}   ${{sm_v}}   ${{sm_p}}
  R&D / Engineering      ${{rd}}     ${{rd_b}}   ${{rd_v}}   ${{rd_p}}
  General & Admin        ${{ga}}     ${{ga_b}}   ${{ga_v}}   ${{ga_p}}
                         --------    --------    --------   ------------
  TOTAL OpEx             ${{opex}}   ${{opex_b}} ${{opex_v}} ${{opex_p}}

NET INCOME (LOSS)        ${{ni}}     ${{ni_b}}   ${{ni_v}}   ${{ni_p}}
  Net Margin                {{nm}}%     {{nm_b}}%                {{nm_p}}%
```

## Variance Commentary Template

```
VARIANCE ANALYSIS - {{period}}

MATERIAL VARIANCES (>{{threshold}}% or >${{threshold_amount}})

1. {{category_1}}: {{variance_amount_1}} ({{variance_pct_1}}%)
   What:    {{variance_desc_1}}
   Why:     {{root_cause_1}}
   Impact:  {{impact_1}}
   Action:  {{action_1}}
   Outlook: {{outlook_1}}

2. {{category_2}}: {{variance_amount_2}} ({{variance_pct_2}}%)
   What:    {{variance_desc_2}}
   Why:     {{root_cause_2}}
   Impact:  {{impact_2}}
   Action:  {{action_2}}
   Outlook: {{outlook_2}}
```

## Board Package Template

```
BOARD FINANCIAL PACKAGE
Period: {{period}} {{year}}

1. EXECUTIVE SUMMARY (1 page)
   [Use Executive Summary Section above]

2. P&L WITH COMMENTARY (1-2 pages)
   [Use Detailed P&L Template above + Variance Commentary]

3. CASH FLOW AND RUNWAY (1 page)
   Beginning Cash:     ${{begin_cash}}
   + Cash Inflows:     ${{cash_in}}
   - Cash Outflows:    ${{cash_out}}
   = Ending Cash:      ${{end_cash}}
   
   Monthly Burn Rate:  ${{burn}}
   Cash Runway:        {{runway}} months
   Next Funding Need:  {{funding_date}} (if applicable)

4. KEY METRICS DASHBOARD (1 page)
   Metric              Target    Actual    Status
   -----------------   -------   ------    ------
   MRR / ARR           {{t}}     {{a}}     {{s}}
   Gross Margin        {{t}}     {{a}}     {{s}}
   Net Retention       {{t}}     {{a}}     {{s}}
   CAC Payback         {{t}}     {{a}}     {{s}}
   LTV:CAC             {{t}}     {{a}}     {{s}}
   Headcount           {{t}}     {{a}}     {{s}}
   Cash Runway         {{t}}     {{a}}     {{s}}

5. BUDGET VARIANCE HIGHLIGHTS (1 page)
   [Top 5-7 material variances with brief commentary]

6. FORWARD OUTLOOK AND RISKS (1 page)
   Next Quarter Forecast:
   - Revenue: ${{q_rev}} ({{q_rev_growth}}% growth)
   - Expenses: ${{q_exp}}
   - Net: ${{q_net}}
   
   Key Risks:
   - {{risk_1}}
   - {{risk_2}}
   - {{risk_3}}
   
   Strategic Decisions Needed:
   - {{decision_1}}
   - {{decision_2}}
```
