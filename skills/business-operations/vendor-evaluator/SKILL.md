---
name: vendor-evaluator
description: Compare and evaluate vendors, tools, and platforms with structured scoring and analysis. Use when the user mentions "evaluate vendor," "compare vendors," "vendor selection," "tool comparison," "RFP," "request for proposal," "vendor scorecard," "buy vs build," "total cost of ownership," "TCO," "vendor review," or "software selection."
metadata:
  version: 1.0.0
  category: finance-operations
---

# Vendor Evaluator

Compare and evaluate vendors systematically using weighted scoring, TCO analysis, and structured decision frameworks.

## Purpose

This skill helps you make defensible vendor selection decisions by providing a repeatable evaluation process. It covers criteria definition, weighted scoring, cost analysis, reference checks, and a recommendation format that stakeholders can review and approve. Use it for SaaS tools, service providers, agencies, contractors, and technology platforms.

## Quick Start

1. **Define requirements**: List must-haves, nice-to-haves, and deal-breakers
2. **Identify candidates**: Research and shortlist 3-5 vendors
3. **Build evaluation matrix**: Set criteria and weights
4. **Collect information**: Demos, RFPs, references, trials
5. **Score and rank**: Apply the weighted scoring model
6. **Calculate TCO**: Look beyond sticker price
7. **Make recommendation**: Document rationale for stakeholders

## Evaluation Criteria Matrix

| Category | Criteria | Weight | Description |
|----------|---------|--------|-------------|
| **Functionality** | Feature coverage | 20% | Does it solve the core problem? |
| **Functionality** | Integration capabilities | 10% | Connects to existing stack? |
| **Usability** | Ease of use / UX | 10% | Can the team adopt it without heavy training? |
| **Usability** | Implementation effort | 5% | Time and resources to go live |
| **Reliability** | Uptime / SLA | 10% | 99.9%+ availability guarantee |
| **Reliability** | Security & compliance | 10% | SOC 2, GDPR, encryption, access controls |
| **Support** | Customer support quality | 5% | Response time, channels, quality |
| **Support** | Documentation & resources | 5% | Docs, community, knowledge base |
| **Cost** | Price / value ratio | 15% | Total cost relative to value delivered |
| **Vendor** | Financial stability | 5% | Will they be around in 3-5 years? |
| **Vendor** | Roadmap alignment | 5% | Are they building what you'll need next? |
| | | **100%** | |

Adjust weights based on your priorities. Functionality and cost typically dominate.

## Weighted Scoring Template

```
VENDOR EVALUATION SCORECARD
═══════════════════════════════════════════════════════════════

Project:          [Name / Description]
Evaluated by:     [Name(s)]
Date:             [Date]
Vendors:          [Vendor A] | [Vendor B] | [Vendor C]

                                          Vendor A    Vendor B    Vendor C
Criteria               Weight   Max Pts   Score  Wtd  Score  Wtd  Score  Wtd
─────────────────────  ──────   ───────   ─────  ───  ─────  ───  ─────  ───
Feature coverage        20%      5         [ ]   [ ]  [ ]   [ ]  [ ]   [ ]
Integration             10%      5         [ ]   [ ]  [ ]   [ ]  [ ]   [ ]
Ease of use             10%      5         [ ]   [ ]  [ ]   [ ]  [ ]   [ ]
Implementation effort    5%      5         [ ]   [ ]  [ ]   [ ]  [ ]   [ ]
Uptime / SLA            10%      5         [ ]   [ ]  [ ]   [ ]  [ ]   [ ]
Security & compliance   10%      5         [ ]   [ ]  [ ]   [ ]  [ ]   [ ]
Support quality          5%      5         [ ]   [ ]  [ ]   [ ]  [ ]   [ ]
Documentation            5%      5         [ ]   [ ]  [ ]   [ ]  [ ]   [ ]
Price / value           15%      5         [ ]   [ ]  [ ]   [ ]  [ ]   [ ]
Financial stability      5%      5         [ ]   [ ]  [ ]   [ ]  [ ]   [ ]
Roadmap alignment        5%      5         [ ]   [ ]  [ ]   [ ]  [ ]   [ ]
─────────────────────  ──────             ─────────  ─────────  ─────────
WEIGHTED TOTAL          100%               [ ]/5.0    [ ]/5.0    [ ]/5.0

SCORING GUIDE:
  5 = Exceeds requirements
  4 = Fully meets requirements
  3 = Mostly meets, minor gaps
  2 = Partially meets, significant gaps
  1 = Minimally meets or does not meet

DEAL-BREAKER CHECK:
  □ SOC 2 Type II certification      [A: ✓/✗] [B: ✓/✗] [C: ✓/✗]
  □ SSO / SAML support                [A: ✓/✗] [B: ✓/✗] [C: ✓/✗]
  □ Data residency (region)           [A: ✓/✗] [B: ✓/✗] [C: ✓/✗]
  □ API availability                  [A: ✓/✗] [B: ✓/✗] [C: ✓/✗]
  □ [Custom requirement]              [A: ✓/✗] [B: ✓/✗] [C: ✓/✗]

Note: Any vendor failing a deal-breaker is eliminated regardless of score.
```

## RFP Template

```
REQUEST FOR PROPOSAL (RFP)
═══════════════════════════════════════════════════════════════

RFP #:              [RFP-YYYY-NNNN]
Issued by:          [Company Name]
Issue Date:         [Date]
Response Deadline:  [Date + 2-3 weeks]
Contact:            [Name, Email]

1. COMPANY OVERVIEW
──────────────────────────────────────────────────────────
   [2-3 paragraphs about your company, size, industry, and context
   for this procurement.]

2. PROJECT OVERVIEW
──────────────────────────────────────────────────────────
   [Description of the business need and what you are looking for.
   Include current state, desired future state, and key objectives.]

3. REQUIREMENTS
──────────────────────────────────────────────────────────
   3.1 Functional Requirements (Must Have)
       □ [Requirement 1]
       □ [Requirement 2]
       □ [Requirement 3]

   3.2 Functional Requirements (Nice to Have)
       □ [Requirement 4]
       □ [Requirement 5]

   3.3 Technical Requirements
       □ [Integration with X system]
       □ [API specifications]
       □ [Performance / scale requirements]

   3.4 Security & Compliance
       □ [Certifications required]
       □ [Data handling requirements]

   3.5 Support & SLA
       □ [Uptime requirement]
       □ [Support hours and response times]

4. PROPOSAL FORMAT
──────────────────────────────────────────────────────────
   Please structure your response as follows:
   a. Executive Summary
   b. Company Background and References
   c. Proposed Solution (address each requirement)
   d. Implementation Plan and Timeline
   e. Team and Resources
   f. Pricing (detailed breakdown)
   g. Contract Terms
   h. Case Studies (2-3 relevant examples)

5. EVALUATION CRITERIA
──────────────────────────────────────────────────────────
   Proposals will be evaluated on:
   • Solution fit (30%)
   • Pricing and value (25%)
   • Vendor experience and references (20%)
   • Implementation approach (15%)
   • Support and partnership (10%)

6. TIMELINE
──────────────────────────────────────────────────────────
   RFP Issued:              [Date]
   Questions Due:           [Date + 1 week]
   Answers Published:       [Date + 10 days]
   Proposals Due:           [Date + 3 weeks]
   Shortlist Notified:      [Date + 4 weeks]
   Demos / Presentations:   [Date + 5-6 weeks]
   Decision:                [Date + 7 weeks]
   Contract Execution:      [Date + 9 weeks]

7. TERMS
──────────────────────────────────────────────────────────
   • This RFP does not obligate [Company] to award a contract
   • All proposals become property of [Company]
   • [Company] reserves the right to negotiate with any respondent
   • Vendors must hold pricing for 90 days from submission
```

## Vendor Comparison Table

```
VENDOR COMPARISON SUMMARY
═══════════════════════════════════════════════════════════════

                        Vendor A          Vendor B          Vendor C
                        ──────────        ──────────        ──────────
Company Info
  Founded               [Year]            [Year]            [Year]
  Employees             [#]               [#]               [#]
  Funding / Revenue     [Stage/$$]        [Stage/$$]        [Stage/$$]
  Customers             [#]               [#]               [#]

Pricing
  Monthly (per user)    $XX               $XX               $XX
  Annual (per user)     $XX               $XX               $XX
  Setup / Onboarding    $X,XXX            $X,XXX            Included
  Minimum commitment    [12 mo / None]    [12 mo / None]    [12 mo / None]

Product
  Core strength         [Summary]         [Summary]         [Summary]
  Key weakness          [Summary]         [Summary]         [Summary]
  Mobile app            ✓ / ✗             ✓ / ✗             ✓ / ✗
  API                   ✓ / ✗             ✓ / ✗             ✓ / ✗
  Integrations          [#]               [#]               [#]

Support
  Channels              [List]            [List]            [List]
  SLA (response)        [Time]            [Time]            [Time]
  Dedicated CSM         ✓ / ✗             ✓ / ✗             ✓ / ✗

Security
  SOC 2                 ✓ / ✗             ✓ / ✗             ✓ / ✗
  GDPR                  ✓ / ✗             ✓ / ✗             ✓ / ✗
  SSO                   ✓ / ✗             ✓ / ✗             ✓ / ✗
  Encryption            [Details]         [Details]         [Details]

References
  Ref 1 sentiment       [Pos/Neg/Mixed]   [Pos/Neg/Mixed]   [Pos/Neg/Mixed]
  Ref 2 sentiment       [Pos/Neg/Mixed]   [Pos/Neg/Mixed]   [Pos/Neg/Mixed]

WEIGHTED SCORE          [X.X / 5.0]       [X.X / 5.0]       [X.X / 5.0]
RANK                    [#]               [#]               [#]
```

## TCO Calculation Framework

```
TOTAL COST OF OWNERSHIP (3-YEAR)
═══════════════════════════════════════════════════════════════

                                Year 1      Year 2      Year 3      3-Year Total
                               ────────    ────────    ────────    ────────────
DIRECT COSTS
  License / Subscription       $XX,XXX     $XX,XXX     $XX,XXX      $XXX,XXX
  Setup / Onboarding fees       $X,XXX         $0          $0         $X,XXX
  Implementation services      $XX,XXX         $0          $0        $XX,XXX
  Training                      $X,XXX       $XXX        $XXX         $X,XXX
  Data migration                $X,XXX         $0          $0         $X,XXX

INDIRECT COSTS
  Internal team time (impl.)   $XX,XXX         $0          $0        $XX,XXX
  Internal admin (ongoing)      $X,XXX      $X,XXX      $X,XXX       $X,XXX
  Integration maintenance       $X,XXX      $X,XXX      $X,XXX       $X,XXX
  Productivity loss (ramp-up)   $X,XXX         $0          $0         $X,XXX

GROWTH COSTS
  Additional users              N/A         $X,XXX      $X,XXX       $XX,XXX
  Price escalation (est. 5%)    N/A          $XXX       $X,XXX        $X,XXX
  Add-on modules                N/A         $X,XXX      $X,XXX        $X,XXX

RISK COSTS (probability-weighted)
  Switching cost if vendor fails $X,XXX     $X,XXX      $X,XXX       $X,XXX
  Downtime cost (est.)           $XXX        $XXX        $XXX         $X,XXX

                               ────────    ────────    ────────    ────────────
TOTAL COST OF OWNERSHIP        $XX,XXX     $XX,XXX     $XX,XXX      $XXX,XXX

COST PER USER PER MONTH:       $XXX
COST PER USER PER YEAR:        $X,XXX

NOTES:
• Assumes [XX] users Year 1, [XX] Year 2, [XX] Year 3
• Price escalation estimated at 5% annually
• Internal time valued at $[XX]/hour fully loaded
```

## Reference Check Questions

Ask each vendor reference these questions:

```
VENDOR REFERENCE CHECK
═══════════════════════════════════════════
Reference Company:  [Name]
Contact:            [Name, Title]
Date:               [Date]
Vendor:             [Vendor Name]

RELATIONSHIP
1. How long have you been using [Vendor]?
2. How many users / what scale are you at?
3. What were you using before, and why did you switch?

IMPLEMENTATION
4. How long did implementation take vs. what was promised?
5. Were there unexpected costs or complications?
6. How was the onboarding experience?

PRODUCT
7. What does [Vendor] do really well?
8. What are the biggest limitations or frustrations?
9. How often do they ship meaningful updates?
10. Have you experienced any significant outages?

SUPPORT
11. How responsive is their support team?
12. Do you have a dedicated account manager?
13. How do they handle escalations or critical issues?

VALUE
14. Has the product delivered the ROI you expected?
15. How has pricing changed since you signed?
16. Have they tried to upsell you aggressively?

RELATIONSHIP
17. How would you describe the partnership overall?
18. If you were starting over, would you choose them again?
19. What advice would you give to a new customer?

OVERALL RATING (1-10): ___
```

## Decision Recommendation Template

```
VENDOR SELECTION RECOMMENDATION
═══════════════════════════════════════════════════════════════

Prepared by:      [Name, Title]
Date:             [Date]
Project:          [Description]
Decision Needed:  [Date]

EXECUTIVE SUMMARY
──────────────────────────────────────────────────────────
We evaluated [X] vendors for [purpose]. Based on weighted scoring,
TCO analysis, and reference checks, we recommend [Vendor Name].

EVALUATION RESULTS
──────────────────────────────────────────────────────────
  Vendor A: [X.X / 5.0] -- [One-line summary]
  Vendor B: [X.X / 5.0] -- [One-line summary]
  Vendor C: [X.X / 5.0] -- [One-line summary]

RECOMMENDED VENDOR: [Name]
──────────────────────────────────────────────────────────
  Strengths:
  • [Key strength 1]
  • [Key strength 2]
  • [Key strength 3]

  Weaknesses / Mitigations:
  • [Weakness 1] → [How we'll address it]
  • [Weakness 2] → [How we'll address it]

  3-Year TCO: $XXX,XXX ($XX/user/month)

WHY NOT THE OTHERS
──────────────────────────────────────────────────────────
  Vendor B: [Eliminated because...]
  Vendor C: [Eliminated because...]

RISKS
──────────────────────────────────────────────────────────
  • [Risk 1 with mitigation plan]
  • [Risk 2 with mitigation plan]

IMPLEMENTATION PLAN
──────────────────────────────────────────────────────────
  Phase 1: Contract negotiation (2 weeks)
  Phase 2: Setup and configuration (4 weeks)
  Phase 3: Pilot with [team] (4 weeks)
  Phase 4: Full rollout (2 weeks)

BUDGET REQUEST
──────────────────────────────────────────────────────────
  Year 1 total: $XX,XXX
  Ongoing annual: $XX,XXX
  Budget source: [Department / line item]

APPROVAL
──────────────────────────────────────────────────────────
  □ Approved -- proceed with contract
  □ Approved with conditions: _______________
  □ Not approved -- reason: _______________

  Approver: ________________  Date: ________
```

## Scripts & Tools

**evaluate_vendor.py**: Run weighted scoring analysis
```bash
python scripts/evaluate_vendor.py --vendors "vendorA,vendorB,vendorC" --criteria criteria.json
# Output: Scored comparison with rankings
```

**calculate_tco.py**: Build TCO model
```bash
python scripts/calculate_tco.py --vendor "Vendor A" --users 50 --years 3
# Output: 3-year TCO breakdown with per-user costs
```

**track_vendors.py**: Manage vendor evaluation pipeline
```bash
python scripts/track_vendors.py --status
# Output: All active evaluations with stage and next steps
```

## Best Practices

1. **Start with requirements, not demos**: Define what you need before vendors show you what they have
2. **Weight your criteria**: Not all factors are equal; force-rank what matters most
3. **Always check references**: Vendor-provided references are curated; ask for similar-sized customers
4. **Calculate TCO, not just price**: Implementation, training, admin, and switching costs add up
5. **Run a pilot**: Before committing, test with a real team on a real workflow
6. **Negotiate everything**: List price is a starting point; multi-year, prepay, and volume discounts exist
7. **Read the contract**: Auto-renewal, price escalation, and data portability clauses matter
8. **Plan for exit**: Before signing, understand what it takes to leave (data export, switching cost)
9. **Involve end users**: The people who use the tool daily should score usability, not just the buyer
10. **Document the decision**: Future you will want to know why you chose this vendor over the alternatives
