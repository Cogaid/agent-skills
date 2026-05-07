# Pricing Analysis Templates

## Pricing Analysis Worksheet

```
PRICING ANALYSIS WORKSHEET
=============================================
Product/Service: {{product_name}}
Date:            {{date}}
Analyst:         {{analyst_name}}

1. COST ANALYSIS
--------------------------------------------
Variable cost per unit:         ${{variable_cost}}
Fixed costs (monthly):         ${{fixed_costs}}
Target units/month:            {{target_units}}
Fully loaded cost per unit:    ${{loaded_cost}}
Minimum viable price:          ${{min_price}} (cost + {{min_margin}}% margin)

2. VALUE ANALYSIS
--------------------------------------------
Customer problem cost:          ${{problem_cost}}/month
Time saved per month:           {{hours_saved}} hours x ${{hourly_value}}/hr = ${{time_value}}
Revenue generated:              ${{revenue_generated}}/month
Risk avoided:                   ${{risk_avoided}}
Total value delivered:          ${{total_value}}/month
Value-based price (10-30%):     ${{value_price_low}} to ${{value_price_high}}/month

3. COMPETITIVE POSITION
--------------------------------------------
Market price range:             ${{market_low}} to ${{market_high}}
Average competitor price:       ${{avg_competitor}}
Your differentiation:           {{differentiators}}
Premium/discount justified:     {{premium_pct}}%
Competitive price:              ${{competitive_price}}

4. WILLINGNESS TO PAY
--------------------------------------------
Too cheap:                      ${{too_cheap}}
Cheap (bargain):                ${{cheap}}
Expensive (hesitation):         ${{expensive}}
Too expensive:                  ${{too_expensive}}
Optimal price point:            ${{optimal}}
Acceptable range:               ${{range_low}} to ${{range_high}}

5. RECOMMENDED PRICE
--------------------------------------------
Floor (cost-based):             ${{floor}}
Target (value-based):           ${{target}}
Ceiling (market-based):         ${{ceiling}}
Recommended launch price:       ${{recommended}}
Rationale: {{rationale}}
```

## Competitor Pricing Matrix

```
COMPETITOR PRICING ANALYSIS
=============================================
Market: {{market_name}}
Date:   {{date}}

                    {{comp_a}}     {{comp_b}}     {{comp_c}}     YOU
                    ----------     ----------     ----------     ------
PLANS & PRICING
Free tier           {{}}           {{}}           {{}}           {{}}
Starter plan        ${{/mo}}       ${{/mo}}       ${{/mo}}       ${{/mo}}
Mid-tier            ${{/mo}}       ${{/mo}}       ${{/mo}}       ${{/mo}}
Enterprise          {{}}           {{}}           {{}}           {{}}
Annual discount     {{}}%          {{}}%          {{}}%          {{}}%
Free trial          {{}} days      {{}} days      {{}} days      {{}} days

KEY FEATURES
{{feature_1}}       {{}}           {{}}           {{}}           {{}}
{{feature_2}}       {{}}           {{}}           {{}}           {{}}
{{feature_3}}       {{}}           {{}}           {{}}           {{}}
{{feature_4}}       {{}}           {{}}           {{}}           {{}}

POSITIONING
Target segment      {{}}           {{}}           {{}}           {{}}
Market share        ~{{}}%         ~{{}}%         ~{{}}%         ~{{}}%

OBSERVATIONS:
- {{observation_1}}
- {{observation_2}}
- {{observation_3}}
```

## Pricing Tier Design Template

```
TIERED PRICING STRUCTURE
=============================================
Product: {{product_name}}

                    FREE           STARTER        PROFESSIONAL    ENTERPRISE
                    ------         ------         ------          ------
Price               $0/mo          ${{s_price}}   ${{p_price}}    Custom
                                   (${{s_ann}})   (${{p_ann}})
Target              {{f_target}}   {{s_target}}   {{p_target}}    {{e_target}}
Users               {{f_users}}    {{s_users}}    {{p_users}}     {{e_users}}

CORE FEATURES
{{feature_1}}       {{f1_free}}    {{f1_start}}   {{f1_pro}}      {{f1_ent}}
{{feature_2}}       {{f2_free}}    {{f2_start}}   {{f2_pro}}      {{f2_ent}}
{{feature_3}}       {{f3_free}}    {{f3_start}}   {{f3_pro}}      {{f3_ent}}
{{feature_4}}       {{f4_free}}    {{f4_start}}   {{f4_pro}}      {{f4_ent}}

SUPPORT
Email               {{}}           {{}}           {{}}            {{}}
Phone               {{}}           {{}}           {{}}            {{}}
Dedicated CSM       {{}}           {{}}           {{}}            {{}}

COMPLIANCE
SSO/SAML            {{}}           {{}}           {{}}            {{}}
Audit logs          {{}}           {{}}           {{}}            {{}}
Custom branding     {{}}           {{}}           {{}}            {{}}
```

## A/B Test Plan Template

```
PRICING A/B TEST PLAN
=============================================
Test Name:       {{test_name}}
Hypothesis:      If we {{change}}, then {{expected_outcome}} because {{reason}}
Test Owner:      {{owner}}
Start Date:      {{start_date}}
End Date:        {{end_date}} (minimum {{min_weeks}} weeks)

VARIANTS:
  Control (A):   {{control_description}}
  Variant (B):   {{variant_description}}

METRICS:
  Primary:       {{primary_metric}}
  Secondary:     {{secondary_metrics}}
  Guardrail:     {{guardrail_metrics}} (must not degrade)

TARGETING:
  Audience:      {{audience}} (new visitors only / all / segment)
  Traffic split: {{split}}% / {{split}}%
  Min sample:    {{sample_size}} per variant
  Confidence:    95%

RESULTS:
  Control (A):   {{a_metric}} = ___    (n = ___)
  Variant (B):   {{b_metric}} = ___    (n = ___)
  Lift:          +/- ____%
  p-value:       ____
  Confidence:    ____%
  Decision:      [ ] Ship variant  [ ] Keep control  [ ] Run longer
  Revenue impact: ${{monthly_impact}}/mo estimated
```
