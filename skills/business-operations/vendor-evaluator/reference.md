# Vendor Evaluator - Reference Documentation

## Vendor Evaluation Process

### Phase 1: Requirements Definition
Before evaluating any vendor, define what you need. This prevents demos from influencing requirements.

**Requirements Gathering Worksheet**:
```
1. Business Problem Statement:
   What problem are we solving? Who has it? How severe is it?

2. Stakeholders:
   Decision maker:     [Name, Role]
   Budget owner:       [Name, Role]
   End users:          [Team/Group]
   IT/Security:        [Name, Role]
   Procurement:        [Name, Role]

3. Functional Requirements:
   Must Have (P1):     [List -- deal-breakers if missing]
   Should Have (P2):   [List -- important but not blocking]
   Nice to Have (P3):  [List -- would be a bonus]

4. Non-Functional Requirements:
   Security:           [Certifications, encryption, access control]
   Compliance:         [GDPR, SOC 2, HIPAA, etc.]
   Performance:        [Uptime SLA, response time, scale]
   Integration:        [Must connect to: X, Y, Z]
   Data:               [Portability, ownership, residency]

5. Constraints:
   Budget:             $[Annual max]
   Timeline:           Must be live by [Date]
   Resources:          [Internal team capacity for implementation]

6. Evaluation Criteria Weights:
   [Use the weighted scoring template from SKILL.md]
```

### Phase 2: Market Research and Shortlisting
**Sources for vendor discovery**:
- G2, Capterra, TrustRadius (user reviews and comparisons)
- Gartner Magic Quadrant / Forrester Wave (analyst reports)
- Industry communities and forums
- Peer referrals and recommendations
- LinkedIn searches for solution categories
- Conference exhibitor lists

**Shortlisting criteria** (narrow from 10+ to 3-5):
1. Meets all Must Have requirements
2. Within budget range (or negotiable)
3. Serves your company size / industry
4. Positive user reviews from similar companies
5. No deal-breaker security or compliance gaps

### Phase 3: Evaluation Deep Dive
**Demo best practices**:
- Send your use case and requirements BEFORE the demo
- Prepare a script: specific scenarios you want to see
- Include end users in the demo, not just buyers
- Ask to see the actual product, not just slides
- Request access to a sandbox or trial environment
- Note what they skip or promise for "future roadmap"

**Questions to ask during demos**:
1. Can you show us how [specific workflow] works?
2. How does this integrate with [your tools]?
3. What does implementation look like? Timeline? Resources?
4. Who are your largest customers in our industry?
5. What are the top 3 things your customers wish you did better?
6. How do you handle [your edge case]?
7. What's on your product roadmap for the next 12 months?
8. Can we speak with 2-3 reference customers similar to our size?

### Phase 4: TCO Analysis
Go beyond the sticker price. True cost includes:

**Direct Costs** (visible):
- License or subscription fees
- Implementation / onboarding fees
- Training costs
- Data migration costs
- Custom development or configuration

**Indirect Costs** (hidden):
- Internal team time for implementation and management
- Productivity loss during transition period
- Ongoing admin and maintenance effort
- Integration development and maintenance
- Consultant or contractor assistance

**Opportunity Costs**:
- Time to implement vs. time to value
- Features you build around missing capabilities
- Vendor lock-in if you need to switch later

**Risk Costs** (probability-weighted):
- Vendor goes out of business: switching cost x probability
- Data breach: remediation cost x probability
- Downtime: revenue loss per hour x estimated annual downtime

### Phase 5: Decision and Negotiation

## Weighted Scoring Methodology

### Score Calibration Guide

Each criterion is scored 1-5. To ensure consistency across evaluators:

**5 - Exceeds Requirements**:
- Feature is native, mature, and requires no workaround
- Performance exceeds your benchmarks
- Reference customers confirm excellence in this area
- Clearly superior to alternatives

**4 - Fully Meets Requirements**:
- Feature works as needed out of the box
- Minor configuration may be needed
- No significant gaps or concerns
- Competitive with best alternatives

**3 - Mostly Meets, Minor Gaps**:
- Feature exists but has limitations
- Workaround is available and reasonable
- Some configuration or customization needed
- Acceptable but not ideal

**2 - Partially Meets, Significant Gaps**:
- Feature is limited or in early development
- Workaround is cumbersome
- Custom development may be required
- Notable disadvantage vs. alternatives

**1 - Minimally Meets or Does Not Meet**:
- Feature is missing or fundamentally inadequate
- No reasonable workaround
- Would require building around the gap
- Deal-breaker consideration

### Multi-Evaluator Scoring
When multiple people evaluate:
1. Each evaluator scores independently
2. Aggregate scores (average or median)
3. Identify criteria where scores diverge by >2 points
4. Discuss divergent scores to reach consensus
5. Document rationale for final scores

## RFP Best Practices

### RFP Dos and Don'ts

| Do | Don't |
|----|-------|
| Send requirements before the RFP | Write requirements to match a preferred vendor |
| Give vendors enough time (2-3 weeks) | Rush responses with <1 week deadline |
| Provide a clear response format | Leave format open-ended (makes comparison hard) |
| Ask for specific, quantified answers | Accept vague marketing language |
| Include evaluation criteria | Keep scoring secret (vendors can't optimize) |
| Allow a Q&A period | Refuse to answer vendor questions |
| Set a realistic budget range | Hide budget entirely (wastes everyone's time) |
| Evaluate at least 3 vendors | Evaluate only 1 (no leverage, no comparison) |

### RFP Response Scoring Rubric
| Section | Weight | What to Look For |
|---------|--------|-----------------|
| Solution Fit | 30% | Addresses each requirement specifically, not generically |
| Pricing | 25% | Transparent, detailed, within budget, TCO considered |
| Experience | 20% | Similar customers, case studies, industry expertise |
| Implementation | 15% | Realistic timeline, clear plan, dedicated resources |
| Support | 10% | SLA, channels, escalation, customer success model |

## Buy vs. Build Decision Framework

| Factor | Buy (Vendor) | Build (In-House) |
|--------|-------------|-----------------|
| **Time to value** | Faster (weeks-months) | Slower (months-years) |
| **Upfront cost** | Lower (subscription) | Higher (development) |
| **Ongoing cost** | Recurring license fees | Maintenance and hosting |
| **Customization** | Limited by vendor | Unlimited |
| **Competitive advantage** | Same tool as competitors | Unique to your business |
| **Maintenance burden** | Vendor handles updates | Your team handles everything |
| **Integration** | Pre-built integrations | Custom integration required |
| **Data control** | Vendor holds data | Full control |
| **Vendor risk** | Dependency on vendor | No vendor risk |
| **Best when** | Commodity capability | Core differentiator |

**Decision rule**: Build only when the capability is a core competitive differentiator AND you have the engineering capacity to maintain it long-term. Buy everything else.

## Vendor Risk Assessment

### Financial Viability Signals
| Signal | Green (Low Risk) | Yellow (Monitor) | Red (High Risk) |
|--------|-----------------|------------------|----------------|
| Funding | Profitable or well-funded | Recent funding round | Running low, seeking bridge |
| Revenue | Growing, diversified | Flat or concentrated | Declining |
| Customers | 500+ and growing | 100-500 | <100 |
| Team | Stable, growing | Key departures | Mass layoffs |
| Product | Active development | Slow releases | Stagnant |

### Vendor Lock-in Assessment
| Dimension | Low Lock-in | Medium Lock-in | High Lock-in |
|-----------|------------|----------------|-------------|
| Data export | Full export, standard format | Partial export, proprietary format | No export capability |
| API access | Full API, well-documented | Limited API | No API |
| Contract | Month-to-month or annual | 2-year commitment | 3+ years, penalties |
| Migration | Easy to switch, tools exist | Moderate effort to switch | Months to migrate |
| Workflow dependency | Standalone | Some dependencies | Deeply embedded |

## Contract Negotiation Tips for Vendor Agreements

### Negotiation Levers
| Lever | How to Use It |
|-------|--------------|
| Multi-year commitment | Offer 2-3 years for 20-30% discount |
| Annual prepay | Pay upfront for 10-15% discount |
| Volume | Commit to seats/usage for volume discount |
| Case study | Offer to be a reference for 10-15% discount |
| Timing | Buy at end of quarter/year for quota pressure discounts |
| Competitive bids | Use competing proposals for leverage |
| Implementation help | Ask vendor to include onboarding at no charge |
| Extended trial | Get 60-90 day pilot instead of 14-day trial |

### Key Contract Terms to Negotiate
1. **Price protection**: Cap annual increases at CPI or 5%
2. **Termination for convenience**: 30-day out clause
3. **Data portability**: Full export on termination
4. **SLA with teeth**: Credits or termination right for breaches
5. **Auto-renewal notice**: Reduce to 30 days
6. **Seat flexibility**: Right to reduce seats at renewal
7. **Payment terms**: Net 30 or Net 45
8. **Security addendum**: Right to security questionnaire annually
