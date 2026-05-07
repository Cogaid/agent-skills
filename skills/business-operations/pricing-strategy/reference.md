# Pricing Strategy - Reference Documentation

## Pricing Model Deep Dives

### Value-Based Pricing
The most profitable pricing approach when executed well. Price based on the economic value your product creates for the customer, not your cost to deliver it.

**Value Quantification Framework**:
```
Step 1: Identify the customer's Next Best Alternative (NBA)
Step 2: Quantify the value your product adds ABOVE the NBA

Value Components:
  Time saved:            X hours/month x $Y/hour = $Z/month
  Revenue increase:      X% lift x $Y baseline = $Z/month
  Cost reduction:        $X/month in eliminated expenses
  Risk mitigation:       $X potential loss x Y% probability = $Z expected value
  Productivity gain:     X% efficiency x $Y team cost = $Z/month

Total Economic Value:    Sum of all components
Your Price (10-30%):     Total Economic Value x capture rate
```

**Capture rate guidelines**:
| Market Position | Capture Rate | When |
|----------------|-------------|------|
| Category leader, strong moat | 25-30% | Established market, high switching costs |
| Strong differentiator | 15-25% | Clear value above alternatives |
| Competitive market | 10-15% | Multiple viable alternatives |
| New entrant | 5-10% | Building trust, need adoption |

### Usage-Based Pricing (Consumption)
Charge based on what customers actually consume. Increasingly popular in infrastructure, APIs, and data products.

**Metric Selection Criteria**:
| Metric Quality | Description | Example |
|---------------|-------------|---------|
| Value-aligned | More usage = more value for customer | API calls that generate revenue |
| Predictable | Customer can estimate usage | Monthly active users |
| Measurable | Easy to track and report | Storage GB, compute hours |
| Controllable | Customer can manage consumption | Data transfer, seats |

**Hybrid usage models**:
```
Platform Fee + Usage:
  Base platform: $500/mo (includes first 10K API calls)
  Overage: $0.01 per additional API call
  Best for: Ensuring minimum revenue with growth upside

Committed Use Discounts:
  Pay-as-you-go: $0.10 per unit
  Commit 100K units/month: $0.07 per unit (30% discount)
  Commit 500K units/month: $0.05 per unit (50% discount)
  Best for: Rewarding large customers, improving predictability

Credit-Based:
  Purchase credits: 1,000 credits = $99
  Feature A: 1 credit per use
  Feature B: 5 credits per use
  Feature C: 10 credits per use
  Best for: Multi-feature platforms with different value weights
```

### Freemium Strategy
**Core challenge**: Maximizing conversion from free to paid while minimizing support costs.

**What to include in free tier**:
- Enough value to demonstrate the product's core benefit
- Natural limits that power users hit (storage, seats, features)
- Virality mechanics (sharing, collaboration, "powered by" branding)

**What to gate behind paid**:
- Team/collaboration features
- Advanced analytics and reporting
- Integrations and API access
- Compliance and security features (SSO, audit logs)
- Priority support
- Remove branding / white-label

**Conversion benchmarks**:
| Metric | Below Average | Average | Good | Great |
|--------|--------------|---------|------|-------|
| Free to Paid conversion | <2% | 2-5% | 5-10% | >10% |
| Time to convert | >90 days | 30-90 days | 14-30 days | <14 days |
| Free user to MQL | <5% | 5-15% | 15-25% | >25% |

## Pricing Psychology

### Anchoring
Present a high-priced option first to make the target plan seem reasonable.
- Show Enterprise pricing before Professional
- Display "was $X, now $Y" for promotions
- Use decoy pricing (a plan nobody buys to make the adjacent plan look better)

### Charm Pricing
Prices ending in 9 ($29, $99, $199) consistently outperform round numbers for consumer products.
- B2C: $29/mo outperforms $30/mo
- B2B: Round numbers ($100, $500) can signal quality and simplicity
- Enterprise: Custom pricing signals premium and flexibility

### Price Framing
| Frame | Example | Psychology |
|-------|---------|-----------|
| Per day | "$3.27/day" | Less than a coffee |
| Per user per month | "$15/user/mo" | Scales with team size |
| Annual with savings | "$99/mo or $79/mo billed annually (save 20%)" | Loss aversion |
| ROI-based | "10x return on your investment" | Value, not cost |
| Comparison | "1/10th the cost of hiring a full-time [role]" | Alternative cost |

### The Rule of Three
Three pricing tiers consistently outperform two or four:
- **Tier 1 (Anchor)**: Basic - establishes the floor
- **Tier 2 (Target)**: Professional - this is what most customers should buy
- **Tier 3 (Aspirational)**: Enterprise - creates the anchor for Tier 2

**Distribution target**: 20% Tier 1 / 60% Tier 2 / 20% Tier 3

## Price Testing Methodology

### Van Westendorp Price Sensitivity Meter
Ask four questions to determine acceptable price range:
1. At what price would this product be so cheap you'd question quality?
2. At what price is this a bargain -- a great buy for the money?
3. At what price is this getting expensive -- you'd think twice?
4. At what price is this too expensive -- you'd never consider buying?

**Interpretation**:
- Plot cumulative distributions of each answer
- Optimal Price Point (OPP): Where "too cheap" = "too expensive"
- Indifference Price Point (IDP): Where "cheap" = "expensive"
- Acceptable range: Between OPP and IDP

### Conjoint Analysis
Test how customers value different attributes and price levels:
1. Define attributes (features, support level, price)
2. Create product profiles (combinations of attributes)
3. Ask customers to rank or choose between profiles
4. Analyze to determine willingness to pay for each attribute

### A/B Testing Rules for Pricing
1. **Only test with new visitors**: Existing users seeing different prices erodes trust
2. **Run for full billing cycles**: Minimum 2 billing cycles to capture behavior
3. **Segment by source**: Different channels may have different price sensitivity
4. **Track downstream metrics**: Conversion rate alone is insufficient; track LTV and churn
5. **Statistical significance**: Require 95% confidence before declaring a winner
6. **Sample size**: Minimum 1,000 visitors per variant for reliable results

## Price Change Playbook

### Raising Prices
```
PRICE INCREASE CHECKLIST:
1. Quantify the value delivered since last pricing review
2. Benchmark against competitors (are you still underpriced?)
3. Grandfather existing customers (optional, recommended)
4. Give 30-60 days advance notice
5. Communicate value, not just the increase
6. Offer annual lock-in at current price
7. Train sales team on objection handling
8. Monitor churn for 90 days post-increase

COMMUNICATION TEMPLATE:
Subject: Updates to [Product] pricing effective [Date]

We're updating our pricing to reflect the significant improvements
we've made to [Product], including [feature 1], [feature 2], and
[feature 3].

Starting [Date], new pricing will be:
  [Plan]: $[New Price]/mo (previously $[Old Price]/mo)

As a valued customer:
  - Your current pricing is locked until [Date]
  - You can lock in your current rate for 12 months by switching to annual billing
  - [Special offer or migration path]

We appreciate your partnership and are committed to delivering
even more value in the months ahead.
```

### Discounting Guidelines
| Discount Type | Typical Range | When to Offer | Warning Sign |
|--------------|--------------|---------------|-------------|
| Annual prepay | 15-20% | Standard option on pricing page | Over 25% = desperation |
| Multi-year | 20-30% | Enterprise deals, high-value accounts | Lock-in without value |
| Volume | 10-25% | Seat or usage scaling | Giving away margin |
| Startup/nonprofit | 25-50% | Brand building, social good | Unsustainable if large segment |
| Promotional | 10-20% | Seasonal, launch, competitive win | Training buyers to wait |
| Competitive match | Case-by-case | Retention, competitive loss | Race to bottom |

**Anti-discount rules**:
1. Never discount more than 20% without VP approval
2. Always require something in return (annual commitment, case study, referral)
3. Track discount frequency and average by rep
4. Sunset promotional discounts (auto-expire)
5. Document every discount with justification for audit
