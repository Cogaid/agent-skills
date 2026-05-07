# Financial Dashboard Template

## KPI Dashboard Layout

```
FINANCIAL DASHBOARD - {{period}} {{year}}
Last Updated: {{updated_date}}

═══════════════════════════════════════════════════════════════
  REVENUE                    PROFITABILITY              CASH
  ─────────                  ─────────────              ────
  MRR:     ${{mrr}}          Gross Margin: {{gm}}%      Cash:    ${{cash}}
  ARR:     ${{arr}}          Net Margin:   {{nm}}%      Runway:  {{runway}}mo
  Growth:  {{growth}}% QoQ   EBITDA:       ${{ebitda}}  Burn:    ${{burn}}/mo
═══════════════════════════════════════════════════════════════

  CUSTOMERS                  EFFICIENCY                 TEAM
  ─────────                  ──────────                 ────
  Total:   {{cust_total}}    LTV:CAC:  {{ltv_cac}}:1   Headcount: {{hc}}
  New:     +{{cust_new}}     CAC:      ${{cac}}        Open Roles: {{roles}}
  Churn:   {{churn}}%        NRR:      {{nrr}}%        Rev/Employee: ${{rev_emp}}
═══════════════════════════════════════════════════════════════
```

## Trend Chart Data Format

```
REVENUE TREND (Monthly)
──────────────────────────────────────────

Month       MRR         ARR          MoM %
──────      ─────────   ──────────   ─────
{{m1}}      ${{mrr1}}   ${{arr1}}    {{g1}}%
{{m2}}      ${{mrr2}}   ${{arr2}}    {{g2}}%
{{m3}}      ${{mrr3}}   ${{arr3}}    {{g3}}%
{{m4}}      ${{mrr4}}   ${{arr4}}    {{g4}}%
{{m5}}      ${{mrr5}}   ${{arr5}}    {{g5}}%
{{m6}}      ${{mrr6}}   ${{arr6}}    {{g6}}%

3-month moving avg:  ${{avg_3mo}}
6-month moving avg:  ${{avg_6mo}}
```

## Expense Breakdown Format

```
OPERATING EXPENSE BREAKDOWN - {{period}}
──────────────────────────────────────────

Category              Amount       % of Total    vs Budget   Trend
───────────────────   ──────────   ──────────    ─────────   ─────
People                ${{ppl}}     {{ppl_pct}}%  {{ppl_bv}}  {{ppl_t}}
Technology            ${{tech}}    {{tech_pct}}% {{tech_bv}} {{tech_t}}
Sales & Marketing     ${{sm}}      {{sm_pct}}%   {{sm_bv}}   {{sm_t}}
General & Admin       ${{ga}}      {{ga_pct}}%   {{ga_bv}}   {{ga_t}}
Other                 ${{oth}}     {{oth_pct}}%  {{oth_bv}}  {{oth_t}}
───────────────────   ──────────   ──────────    ─────────
TOTAL OpEx            ${{total}}   100.0%        {{t_bv}}
```

## Investor Update Template

```
INVESTOR UPDATE - {{period}} {{year}}
{{company_name}}

HEADLINE
{{headline_sentence}}

KEY METRICS
  ARR:              ${{arr}}          ({{arr_growth}}% YoY)
  Net Retention:    {{nrr}}%
  Gross Margin:     {{gm}}%
  Cash Position:    ${{cash}}         ({{runway}} months runway)
  Headcount:        {{hc}}

WINS THIS PERIOD
- {{win_1}}
- {{win_2}}
- {{win_3}}

CHALLENGES
- {{challenge_1}}
- {{challenge_2}}

PRIORITIES NEXT PERIOD
- {{priority_1}}
- {{priority_2}}
- {{priority_3}}

ASK
{{ask_description}}
```
