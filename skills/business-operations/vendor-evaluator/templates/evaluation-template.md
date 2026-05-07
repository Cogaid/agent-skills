# Vendor Evaluation Templates

## Vendor Evaluation Scorecard

```
VENDOR EVALUATION SCORECARD
=============================================
Project:          {{project_name}}
Evaluated by:     {{evaluator_names}}
Date:             {{date}}
Vendors:          {{vendor_a}} | {{vendor_b}} | {{vendor_c}}

                                          {{vendor_a}}  {{vendor_b}}  {{vendor_c}}
Criteria               Weight   Max Pts   Score  Wtd   Score  Wtd   Score  Wtd
---------------------  ------   -------   -----  ---   -----  ---   -----  ---
Feature coverage        20%      5         {{}}  {{}}  {{}}  {{}}  {{}}  {{}}
Integration             10%      5         {{}}  {{}}  {{}}  {{}}  {{}}  {{}}
Ease of use             10%      5         {{}}  {{}}  {{}}  {{}}  {{}}  {{}}
Implementation effort    5%      5         {{}}  {{}}  {{}}  {{}}  {{}}  {{}}
Uptime / SLA            10%      5         {{}}  {{}}  {{}}  {{}}  {{}}  {{}}
Security & compliance   10%      5         {{}}  {{}}  {{}}  {{}}  {{}}  {{}}
Support quality          5%      5         {{}}  {{}}  {{}}  {{}}  {{}}  {{}}
Documentation            5%      5         {{}}  {{}}  {{}}  {{}}  {{}}  {{}}
Price / value           15%      5         {{}}  {{}}  {{}}  {{}}  {{}}  {{}}
Financial stability      5%      5         {{}}  {{}}  {{}}  {{}}  {{}}  {{}}
Roadmap alignment        5%      5         {{}}  {{}}  {{}}  {{}}  {{}}  {{}}
---------------------  ------             ---------   ---------   ---------
WEIGHTED TOTAL          100%               {{}} /5.0   {{}} /5.0   {{}} /5.0

SCORING: 5=Exceeds | 4=Fully meets | 3=Mostly meets | 2=Partially | 1=Does not meet

DEAL-BREAKER CHECK:
  [ ] SOC 2 Type II           [A: {{}}] [B: {{}}] [C: {{}}]
  [ ] SSO / SAML              [A: {{}}] [B: {{}}] [C: {{}}]
  [ ] Data residency          [A: {{}}] [B: {{}}] [C: {{}}]
  [ ] API availability        [A: {{}}] [B: {{}}] [C: {{}}]
  [ ] {{custom_requirement}}  [A: {{}}] [B: {{}}] [C: {{}}]
```

## TCO Comparison Template

```
TOTAL COST OF OWNERSHIP (3-YEAR)
=============================================
Vendors: {{vendor_a}} | {{vendor_b}} | {{vendor_c}}
Users: {{users}} (Year 1) -> {{users_y3}} (Year 3)

                              {{vendor_a}}          {{vendor_b}}          {{vendor_c}}
                              Y1    Y2    Y3        Y1    Y2    Y3        Y1    Y2    Y3
                              ----  ----  ----      ----  ----  ----      ----  ----  ----
DIRECT COSTS
License/Subscription          ${{}} ${{}} ${{}}     ${{}} ${{}} ${{}}     ${{}} ${{}} ${{}}
Setup/Onboarding              ${{}} --    --         ${{}} --    --         ${{}} --    --
Implementation                ${{}} --    --         ${{}} --    --         ${{}} --    --
Training                      ${{}} ${{}} ${{}}     ${{}} ${{}} ${{}}     ${{}} ${{}} ${{}}
Data Migration                ${{}} --    --         ${{}} --    --         ${{}} --    --

INDIRECT COSTS
Internal team (impl.)         ${{}} --    --         ${{}} --    --         ${{}} --    --
Internal admin (ongoing)      ${{}} ${{}} ${{}}     ${{}} ${{}} ${{}}     ${{}} ${{}} ${{}}
Integration maintenance       ${{}} ${{}} ${{}}     ${{}} ${{}} ${{}}     ${{}} ${{}} ${{}}
Productivity loss (ramp)      ${{}} --    --         ${{}} --    --         ${{}} --    --

GROWTH COSTS
Additional users              --    ${{}} ${{}}     --    ${{}} ${{}}     --    ${{}} ${{}}
Price escalation (est.)       --    ${{}} ${{}}     --    ${{}} ${{}}     --    ${{}} ${{}}
Add-on modules                --    ${{}} ${{}}     --    ${{}} ${{}}     --    ${{}} ${{}}

                              ------  ------        ------  ------        ------  ------
3-YEAR TOTAL                  ${{total_a}}           ${{total_b}}           ${{total_c}}
COST/USER/MONTH               ${{cpu_a}}             ${{cpu_b}}             ${{cpu_c}}
```

## Vendor Selection Recommendation Template

```
VENDOR SELECTION RECOMMENDATION
=============================================
Prepared by:      {{name}}, {{title}}
Date:             {{date}}
Project:          {{project_description}}
Decision Needed:  {{decision_date}}

EXECUTIVE SUMMARY
--------------------------------------------
We evaluated {{vendor_count}} vendors for {{purpose}}.
Based on weighted scoring, TCO analysis, and reference checks,
we recommend {{recommended_vendor}}.

EVALUATION RESULTS
--------------------------------------------
  {{vendor_a}}: {{score_a}} / 5.0 -- {{summary_a}}
  {{vendor_b}}: {{score_b}} / 5.0 -- {{summary_b}}
  {{vendor_c}}: {{score_c}} / 5.0 -- {{summary_c}}

RECOMMENDED: {{recommended_vendor}}
--------------------------------------------
Strengths:
  - {{strength_1}}
  - {{strength_2}}
  - {{strength_3}}

Weaknesses / Mitigations:
  - {{weakness_1}} -> {{mitigation_1}}
  - {{weakness_2}} -> {{mitigation_2}}

3-Year TCO: ${{tco}} (${{per_user_month}}/user/month)

WHY NOT THE OTHERS
--------------------------------------------
  {{vendor_b}}: {{rejection_reason_b}}
  {{vendor_c}}: {{rejection_reason_c}}

RISKS
--------------------------------------------
  - {{risk_1}} (Mitigation: {{mitigation_1}})
  - {{risk_2}} (Mitigation: {{mitigation_2}})

IMPLEMENTATION PLAN
--------------------------------------------
  Phase 1: Contract negotiation     ({{phase_1_duration}})
  Phase 2: Setup and configuration  ({{phase_2_duration}})
  Phase 3: Pilot with {{pilot_team}} ({{phase_3_duration}})
  Phase 4: Full rollout             ({{phase_4_duration}})

BUDGET REQUEST
--------------------------------------------
  Year 1 total:       ${{year_1}}
  Ongoing annual:     ${{ongoing}}
  Budget source:      {{budget_source}}

APPROVAL
--------------------------------------------
  [ ] Approved -- proceed with contract
  [ ] Approved with conditions: _______________
  [ ] Not approved -- reason: _______________

  Approver: ________________  Date: ________
```

## Reference Check Template

```
VENDOR REFERENCE CHECK
=============================================
Reference Company:  {{company}}
Contact:            {{contact_name}}, {{contact_title}}
Date:               {{date}}
Vendor:             {{vendor_name}}

RELATIONSHIP
1. How long using [Vendor]?          {{answer}}
2. Scale (users/volume)?             {{answer}}
3. What did you replace?             {{answer}}

IMPLEMENTATION
4. Timeline (actual vs. promised)?   {{answer}}
5. Unexpected costs?                 {{answer}}
6. Onboarding experience?            {{answer}}

PRODUCT
7. What does [Vendor] do well?       {{answer}}
8. Biggest limitations?              {{answer}}
9. Update frequency?                 {{answer}}
10. Significant outages?             {{answer}}

SUPPORT
11. Support responsiveness?          {{answer}}
12. Dedicated account manager?       {{answer}}
13. Escalation handling?             {{answer}}

VALUE
14. ROI as expected?                 {{answer}}
15. Pricing changes since signing?   {{answer}}
16. Aggressive upselling?            {{answer}}

RELATIONSHIP
17. Partnership overall?             {{answer}}
18. Choose them again?               {{answer}}
19. Advice for new customer?         {{answer}}

OVERALL RATING (1-10): {{rating}}
```
