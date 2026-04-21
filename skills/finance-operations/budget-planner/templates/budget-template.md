# Budget Templates

## Annual Budget Template

```
ANNUAL BUDGET: {{department_or_company}}
Fiscal Year: {{fiscal_year}}
Prepared by: {{preparer}} | Approved by: {{approver}}
Last Updated: {{last_updated}}
Approach: {{approach}} (Zero-Based / Incremental / Hybrid)

CATEGORY                          Q1         Q2         Q3         Q4        ANNUAL
================================  =========  =========  =========  =========  ==========
REVENUE
  Product / Service Revenue       ${{}}      ${{}}      ${{}}      ${{}}      ${{}}
  Other Income                    ${{}}      ${{}}      ${{}}      ${{}}      ${{}}
  TOTAL REVENUE                   ${{}}      ${{}}      ${{}}      ${{}}      ${{}}

PEOPLE (target: {{people_pct}}% of OpEx)
  Salaries & Wages                ${{}}      ${{}}      ${{}}      ${{}}      ${{}}
  Benefits & Insurance            ${{}}      ${{}}      ${{}}      ${{}}      ${{}}
  Contractors & Freelancers       ${{}}      ${{}}      ${{}}      ${{}}      ${{}}
  Recruiting & Onboarding         ${{}}      ${{}}      ${{}}      ${{}}      ${{}}
  Training & Development          ${{}}      ${{}}      ${{}}      ${{}}      ${{}}

TECHNOLOGY
  SaaS & Subscriptions            ${{}}      ${{}}      ${{}}      ${{}}      ${{}}
  Infrastructure / Cloud          ${{}}      ${{}}      ${{}}      ${{}}      ${{}}
  Hardware & Equipment            ${{}}      ${{}}      ${{}}      ${{}}      ${{}}
  Licenses                        ${{}}      ${{}}      ${{}}      ${{}}      ${{}}

SALES & MARKETING
  Advertising & Paid Media        ${{}}      ${{}}      ${{}}      ${{}}      ${{}}
  Content & Creative              ${{}}      ${{}}      ${{}}      ${{}}      ${{}}
  Events & Conferences            ${{}}      ${{}}      ${{}}      ${{}}      ${{}}
  Sales Tools & Commissions       ${{}}      ${{}}      ${{}}      ${{}}      ${{}}

GENERAL & ADMIN
  Office / Rent                   ${{}}      ${{}}      ${{}}      ${{}}      ${{}}
  Legal & Accounting              ${{}}      ${{}}      ${{}}      ${{}}      ${{}}
  Insurance (D&O, E&O, GL)        ${{}}      ${{}}      ${{}}      ${{}}      ${{}}
  Travel & Meals                  ${{}}      ${{}}      ${{}}      ${{}}      ${{}}
  Miscellaneous                   ${{}}      ${{}}      ${{}}      ${{}}      ${{}}

CONTINGENCY ({{contingency_pct}}%)  ${{}}    ${{}}      ${{}}      ${{}}      ${{}}

================================  =========  =========  =========  =========  ==========
TOTAL EXPENSES                    ${{}}      ${{}}      ${{}}      ${{}}      ${{}}
NET (Revenue - Expenses)          ${{}}      ${{}}      ${{}}      ${{}}      ${{}}
```

## Department Budget Request Template

```
DEPARTMENT BUDGET REQUEST
-----------------------------------------
Department:       {{department_name}}
Manager:          {{manager_name}}
Fiscal Year:      {{fiscal_year}}
Submission Date:  {{submission_date}}

1. DEPARTMENT MISSION
   {{mission_statement}}

2. KEY OBJECTIVES FOR THE YEAR
   a. {{objective_1}} (tied to company goal: {{company_goal_1}})
   b. {{objective_2}} (tied to company goal: {{company_goal_2}})
   c. {{objective_3}} (tied to company goal: {{company_goal_3}})

3. HEADCOUNT PLAN
   Current FTEs:     {{current_ftes}}
   Planned hires:    {{planned_hires}} (roles: {{hire_roles}})
   Planned exits:    {{planned_exits}}
   Year-end FTEs:    {{yearend_ftes}}

4. BUDGET SUMMARY
   Category              Request       Last Year     Change
   -------------------   ----------    ----------    ------
   People                ${{}}         ${{}}         {{}}%
   Technology            ${{}}         ${{}}         {{}}%
   Marketing             ${{}}         ${{}}         {{}}%
   Travel & Events       ${{}}         ${{}}         {{}}%
   Other                 ${{}}         ${{}}         {{}}%
   -------------------   ----------    ----------    ------
   TOTAL                 ${{}}         ${{}}         {{}}%

5. KEY ASSUMPTIONS
   - {{assumption_1}}
   - {{assumption_2}}
   - {{assumption_3}}

6. RISKS TO BUDGET
   - {{risk_1}} (potential impact: ${{risk_1_impact}})
   - {{risk_2}} (potential impact: ${{risk_2_impact}})

7. TRADE-OFF OPTIONS (if budget is reduced 10-20%)
   - Cut option A: {{cut_a_desc}} (saves ${{cut_a_amount}}, impact: {{cut_a_impact}})
   - Cut option B: {{cut_b_desc}} (saves ${{cut_b_amount}}, impact: {{cut_b_impact}})
```

## Variance Report Template

```
BUDGET VARIANCE REPORT
Period: {{period}}
Prepared by: {{preparer}}
Date: {{report_date}}

Category              Budget      Actual      Variance    Var %    Status
--------------------  --------    --------    --------    -----    ------
{{category_1}}        ${{}}       ${{}}       ${{}}       {{}}%    {{status}}
{{category_2}}        ${{}}       ${{}}       ${{}}       {{}}%    {{status}}
{{category_3}}        ${{}}       ${{}}       ${{}}       {{}}%    {{status}}
--------------------  --------    --------    --------    -----
TOTAL                 ${{}}       ${{}}       ${{}}       {{}}%    {{status}}

Status Thresholds:
  OK:     within +/-5%
  WARN:   5-15% over budget
  ALERT:  >15% over budget

MATERIAL VARIANCES REQUIRING EXPLANATION:

1. {{category}}: ${{variance}} ({{variance_pct}}%)
   Cause:    {{cause}}
   Type:     [One-time / Structural]
   Action:   {{action}}
   Forecast: {{forecast_impact}}

2. {{category}}: ${{variance}} ({{variance_pct}}%)
   Cause:    {{cause}}
   Type:     [One-time / Structural]
   Action:   {{action}}
   Forecast: {{forecast_impact}}
```

## Scenario Forecast Template

```
SCENARIO FORECAST
Period: {{forecast_period}}
Prepared: {{date}}

                    Conservative    Base Case    Optimistic    Weighted Avg
                    (25% prob.)     (50% prob.)  (25% prob.)   (Expected)
                    -----------     -----------  -----------   -----------
REVENUE
  Product           ${{}}           ${{}}        ${{}}         ${{}}
  Service           ${{}}           ${{}}        ${{}}         ${{}}
  TOTAL             ${{}}           ${{}}        ${{}}         ${{}}

EXPENSES
  People            ${{}}           ${{}}        ${{}}         ${{}}
  Technology        ${{}}           ${{}}        ${{}}         ${{}}
  Marketing         ${{}}           ${{}}        ${{}}         ${{}}
  G&A               ${{}}           ${{}}        ${{}}         ${{}}
  TOTAL             ${{}}           ${{}}        ${{}}         ${{}}

NET                 ${{}}           ${{}}        ${{}}         ${{}}
Cash Runway         {{}} months     {{}} months  {{}} months

KEY ASSUMPTIONS:
  Conservative: {{conservative_assumptions}}
  Base Case:    {{base_assumptions}}
  Optimistic:   {{optimistic_assumptions}}
```
