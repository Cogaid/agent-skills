---
name: pricing-strategy
description: Analyze and recommend pricing models, structures, and strategies for products and services. Use when the user mentions "pricing," "pricing strategy," "pricing model," "cost-plus pricing," "value-based pricing," "freemium," "tiered pricing," "price elasticity," "competitor pricing," "pricing page," "monetization," or "how to price."
metadata:
  version: 1.0.0
  category: finance-operations
---

# Pricing Strategy

Analyze market positioning, costs, and value to recommend effective pricing models and structures.

## Purpose

This skill helps you evaluate pricing approaches, compare models, analyze competitors, and design pricing structures that balance revenue, growth, and customer perception. It covers both initial pricing decisions and ongoing optimization through testing.

## Quick Start

1. **Understand your costs**: Calculate fully loaded unit economics
2. **Research competitors**: Build the competitor pricing matrix
3. **Assess value delivered**: Quantify the ROI your product creates for customers
4. **Choose a model**: Select from the comparison table below
5. **Design tiers**: Structure plans that serve different segments
6. **Test and iterate**: Use the A/B test framework to optimize

## Pricing Model Comparison

| Model | How It Works | Best For | Pros | Cons |
|-------|-------------|----------|------|------|
| **Cost-Plus** | Cost + markup % | Manufacturing, commodities, agencies | Simple, guaranteed margin | Ignores value and competition |
| **Value-Based** | Price = % of value delivered | SaaS, consulting, premium products | Highest margins, aligned with ROI | Hard to quantify value |
| **Competitive** | Match or undercut market | Commoditized markets, new entrants | Easy to justify, market-validated | Race to bottom, margin pressure |
| **Freemium** | Free base + paid upgrades | SaaS, apps, platforms | Fast adoption, viral growth | Low conversion (2-5%), high support cost |
| **Tiered** | Good / Better / Best plans | SaaS, subscriptions | Serves multiple segments | Complexity, choice paralysis |
| **Usage-Based** | Pay per unit consumed | APIs, cloud, infrastructure | Scales with value, low barrier | Revenue unpredictable, hard to forecast |
| **Per-Seat** | Price per user per month | Collaboration tools, B2B SaaS | Predictable, scales with org size | Discourages adoption, seat sharing |
| **Flat Rate** | One price for everything | Simple products, early-stage | Simple, no decision fatigue | Leaves money on table |
| **Dynamic** | Price fluctuates by demand | Travel, events, e-commerce | Maximizes revenue | Customer frustration, complexity |
| **Penetration** | Low price to gain market share | New markets, network effects | Fast adoption | Hard to raise later, margin pain |

## Pricing Analysis Framework

```
PRICING ANALYSIS WORKSHEET
═══════════════════════════════════════════════════════

1. COST ANALYSIS
────────────────────────────────────────────────────
   Variable cost per unit:         $________
   Fixed costs (monthly):         $________
   Target units/month:            ________
   Fully loaded cost per unit:    $________ (fixed/units + variable)
   Minimum viable price:          $________ (cost + minimum margin)

2. VALUE ANALYSIS
────────────────────────────────────────────────────
   Customer problem cost:          $________ /month (what they spend now)
   Time saved per month:           ________ hours x $____/hr = $________
   Revenue generated:              $________ /month (if applicable)
   Risk avoided:                   $________ (compliance, downtime, etc.)
   Total value delivered:          $________ /month
   Value-based price (10-30%):     $________ /month

3. COMPETITIVE POSITION
────────────────────────────────────────────────────
   Market price range:             $________ to $________
   Average competitor price:       $________
   Your differentiation:           [List key differentiators]
   Premium/discount justified:     +/- ________%

4. WILLINGNESS TO PAY
────────────────────────────────────────────────────
   Van Westendorp survey results:
     Too cheap (quality concern):  $________
     Cheap (good deal):            $________
     Expensive (hesitation):       $________
     Too expensive (won't buy):    $________
   Optimal price point:            $________
   Acceptable range:               $________ to $________

5. RECOMMENDED PRICE
────────────────────────────────────────────────────
   Floor (cost-based):             $________
   Target (value-based):           $________
   Ceiling (market-based):         $________
   Recommended launch price:       $________
   Rationale: [Why this price wins]
```

## Competitor Pricing Matrix

```
COMPETITOR PRICING ANALYSIS
═══════════════════════════════════════════════════════

                    Competitor A   Competitor B   Competitor C    YOU
                    ───────────    ───────────    ───────────    ──────
Company             [Name]         [Name]         [Name]         [Name]

PLANS & PRICING
Free tier           □ Yes □ No     □ Yes □ No     □ Yes □ No     □ Yes □ No
Starter plan        $__/mo         $__/mo         $__/mo         $__/mo
Mid-tier plan       $__/mo         $__/mo         $__/mo         $__/mo
Enterprise plan     Custom         $__/mo         Custom         $__/mo
Annual discount     ___%           ___%           ___%           ___%

PRICING MODEL
Model type          [per-seat]     [usage]        [flat]         [tiered]
Billing cycles      Mo/Yr          Mo/Yr          Mo/Yr/Qtr      Mo/Yr
Free trial          __ days        __ days        __ days        __ days

KEY FEATURES BY TIER
Feature 1           ✓/✗/Limit      ✓/✗/Limit      ✓/✗/Limit      ✓/✗/Limit
Feature 2           ✓/✗/Limit      ✓/✗/Limit      ✓/✗/Limit      ✓/✗/Limit
Feature 3           ✓/✗/Limit      ✓/✗/Limit      ✓/✗/Limit      ✓/✗/Limit
Feature 4           ✓/✗/Limit      ✓/✗/Limit      ✓/✗/Limit      ✓/✗/Limit

POSITIONING
Target segment      [SMB/Mid/Ent]  [SMB/Mid/Ent]  [SMB/Mid/Ent]  [SMB/Mid/Ent]
Value prop          [Summary]      [Summary]      [Summary]      [Summary]
Market share        ~___%          ~___%          ~___%          ~___%

OBSERVATIONS:
• [Gap in competitor offerings you can exploit]
• [Feature they charge extra for that you include]
• [Pricing trend in the market]
```

## Price Elasticity Considerations

| Factor | High Elasticity (price sensitive) | Low Elasticity (price tolerant) |
|--------|----------------------------------|-------------------------------|
| **Alternatives** | Many substitutes available | Few or no alternatives |
| **Necessity** | Nice-to-have product | Mission-critical / must-have |
| **Switching cost** | Easy to switch | High switching cost / lock-in |
| **Budget impact** | Large % of budget | Small % of budget |
| **Buyer type** | Consumer / SMB | Enterprise with budgets |
| **Differentiation** | Commodity / undifferentiated | Unique value / brand loyalty |
| **Transparency** | Prices easily compared | Complex, hard to compare |

**Elasticity test**: If you raise price 10%, how much volume do you lose?

| Volume Loss | Elasticity | Implication |
|------------|-----------|-------------|
| <5% | Inelastic | You are underpriced; raise prices |
| 5-15% | Unit elastic | Price is near optimal |
| >15% | Elastic | Market is price-sensitive; compete on value, not price |

## Pricing Tier Design

```
TIERED PRICING STRUCTURE
═══════════════════════════════════════════════════════

                    FREE           STARTER        PROFESSIONAL    ENTERPRISE
                    ──────         ──────         ──────          ──────
Price               $0/mo          $29/mo         $99/mo          Custom
                                   ($24/mo ann.)  ($79/mo ann.)
Target              Individuals    Small teams    Growing teams    Large orgs
Users               1              Up to 5        Up to 25         Unlimited
Storage             500 MB         5 GB           50 GB            Unlimited

Core Features
Feature A           ✓ (limited)    ✓              ✓                ✓
Feature B           ✗              ✓              ✓                ✓
Feature C           ✗              ✗              ✓                ✓
Feature D           ✗              ✗              ✗                ✓

Support
Email support       Community      48hr response  24hr response    4hr response
Phone support       ✗              ✗              ✓                ✓
Dedicated CSM       ✗              ✗              ✗                ✓

Extras
API access          ✗              100 calls/day  10K calls/day    Unlimited
SSO/SAML            ✗              ✗              ✗                ✓
Custom branding     ✗              ✗              ✓                ✓
Audit logs          ✗              ✗              ✗                ✓

DESIGN PRINCIPLES:
• Free tier: Hook users, demonstrate value, create habit
• Starter: Monetize individuals and small teams; remove biggest friction
• Professional: Core revenue driver; should be the most popular plan
• Enterprise: Capture high willingness-to-pay; security/compliance features gate
• Annual discount: 15-20% to improve cash flow and reduce churn
```

## Pricing Page Copy Template

```
PRICING PAGE STRUCTURE
═══════════════════════════════════════════════════════

HEADLINE:
"[Simple, clear statement about pricing philosophy]"
Example: "Simple pricing that scales with you"

SUBHEADLINE:
"[Address the main objection or highlight key benefit]"
Example: "Start free. Upgrade when you're ready. No surprises."

PLAN CARDS: [Display 3-4 tiers side by side]
• Highlight the recommended plan with a "Most Popular" badge
• Show monthly and annual toggle (with savings %)
• List 5-7 features per plan; use checkmarks and X marks
• CTA button: "Start Free" / "Start Trial" / "Contact Sales"

SOCIAL PROOF:
"Trusted by [X,XXX] teams including [Logo] [Logo] [Logo]"

FAQ SECTION:
• Can I change plans later?
• What happens when I hit my limit?
• Do you offer discounts for nonprofits / startups?
• What payment methods do you accept?
• Is there a contract or commitment?
• What's your refund policy?

TRUST ELEMENTS:
• Money-back guarantee (14 or 30 days)
• No credit card required for free/trial
• SOC 2 / GDPR compliance badges
• Enterprise security certifications
```

## A/B Test Framework for Pricing

| Test | What to Test | Hypothesis | Metric | Duration |
|------|-------------|------------|--------|----------|
| **Price point** | $29 vs. $39 vs. $49 | Higher price won't reduce conversion >10% | Revenue per visitor | 4-6 weeks |
| **Annual discount** | 15% vs. 20% vs. 25% off | 20% is optimal for annual conversion | Annual plan adoption rate | 4-6 weeks |
| **Tier names** | Basic/Pro/Enterprise vs. Starter/Growth/Scale | Names affect perceived value | Click-through rate | 2-4 weeks |
| **Default plan** | Pre-select mid-tier vs. no default | Pre-selection anchors choice | Mid-tier conversion | 2-4 weeks |
| **Feature gating** | Move Feature X up or down a tier | Ungating increases upgrades | Upgrade rate | 4-8 weeks |
| **CTA copy** | "Start Free" vs. "Try for Free" vs. "Get Started" | Action-oriented CTA wins | Signup rate | 2-4 weeks |
| **Social proof** | With logos vs. without | Logos increase trust | Conversion rate | 2-4 weeks |
| **Price anchoring** | Show enterprise price first vs. last | High anchor increases mid-tier | Revenue per visitor | 4-6 weeks |

```
A/B TEST PLAN
═══════════════════════════════════════════
Test Name:       [Descriptive name]
Hypothesis:      [If we X, then Y because Z]
Control:         [Current pricing/design]
Variant:         [Changed pricing/design]
Primary Metric:  [One metric that decides the winner]
Secondary:       [Supporting metrics]
Sample Size:     [Calculated minimum per variant]
Duration:        [X weeks, minimum 2 full billing cycles]
Segment:         [New visitors only / all visitors]
Significance:    95% confidence level

RESULTS:
Control:   [metric] = ___    (n = ___)
Variant:   [metric] = ___    (n = ___)
Lift:      +/- ____%
p-value:   ____
Decision:  [Ship variant / Keep control / Run longer]
```

## Scripts & Tools

**pricing_calculator.py**: Model pricing scenarios
```bash
python scripts/pricing_calculator.py --cost 15 --target-margin 70 --volume 1000
# Output: Price recommendations with revenue projections
```

**competitor_tracker.py**: Monitor competitor pricing changes
```bash
python scripts/competitor_tracker.py --competitors "compA,compB,compC"
# Output: Current pricing with change history
```

**elasticity_model.py**: Estimate price sensitivity
```bash
python scripts/elasticity_model.py --current-price 49 --test-range "29,39,59,79"
# Output: Projected volume and revenue at each price point
```

## Best Practices

1. **Price on value, not cost**: Customers pay for outcomes, not your expenses
2. **Don't be the cheapest**: Low price signals low quality and attracts price-sensitive churners
3. **Raise prices regularly**: Most companies underprice; test increases annually
4. **Grandfather existing customers**: Honor old pricing for current customers to maintain trust
5. **Make the popular plan obvious**: Visual design should guide users to your target tier
6. **Use anchoring**: Show the enterprise price to make the mid-tier feel reasonable
7. **Simplify choices**: Three tiers is ideal; more than four causes decision paralysis
8. **Separate pricing from packaging**: What you charge vs. what you include are different decisions
9. **Test before committing**: Never change pricing based on intuition alone
10. **Monitor the metrics**: Track ARPU, conversion rate, and churn by cohort after any price change
