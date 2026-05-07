# Contract Reviewer - Reference Documentation

## Contract Types and Key Characteristics

### Master Services Agreement (MSA)
**Purpose**: Umbrella contract that governs the overall relationship between parties.
**Typical term**: 1-3 years with auto-renewal
**Key sections**: Liability, indemnification, IP ownership, confidentiality, termination, governing law
**Works with**: Individual SOWs or Work Orders that define specific engagements

### Statement of Work (SOW)
**Purpose**: Defines specific project scope, deliverables, timeline, and pricing under an MSA
**Typical term**: Project-based (weeks to months)
**Key sections**: Scope, deliverables, acceptance criteria, payment schedule, change orders

### Non-Disclosure Agreement (NDA)
**Purpose**: Protects confidential information shared between parties
**Typical term**: 2-5 years for obligations (trade secrets may be indefinite)
**Types**: Mutual (both parties share info) vs. Unilateral (one party discloses)
**Key sections**: Definition of confidential info, exclusions, permitted use, return/destruction

### SaaS / Software License Agreement
**Purpose**: Governs use of software as a service or licensed software
**Key sections**: License grant, usage limits, data ownership, SLA, support terms, data portability
**Watch for**: Auto-renewal, price escalation, data lock-in, termination rights

### Employment Agreement
**Purpose**: Terms of employment relationship
**Key sections**: Compensation, benefits, non-compete, non-solicitation, IP assignment, termination
**Watch for**: Overbroad non-compete, IP assignment of personal projects, at-will vs. for-cause

### Vendor / Procurement Agreement
**Purpose**: Purchase of goods or services from a vendor
**Key sections**: Pricing, delivery, warranties, acceptance, returns, liability
**Watch for**: Price escalation clauses, minimum commitments, exclusivity

## Clause-by-Clause Review Guide

### Liability Cap Structures
```
Typical Structures (from most to least favorable for the buyer):

1. UNCAPPED LIABILITY
   "Neither party's liability shall be limited..."
   Risk: Maximum exposure; avoid if possible
   When acceptable: Very small contracts under $10K

2. AGGREGATE CAP - FEES PAID
   "Total liability shall not exceed fees paid in the prior 12 months"
   Risk: Moderate; standard B2B
   Most common: SaaS agreements, service contracts

3. AGGREGATE CAP - FIXED AMOUNT
   "Total liability shall not exceed $[X]"
   Risk: Depends on amount vs. contract value
   Use: When fees are variable or usage-based

4. SUPER CAP (CARVE-OUTS)
   "General cap of 12 months fees, except:
    - IP infringement: 2x annual fees
    - Confidentiality breach: 3x annual fees
    - Willful misconduct: uncapped"
   Risk: Moderate; reflects severity of breach type
   Best practice: Include super cap for IP and confidentiality

5. PER-INCIDENT CAP
   "Liability per incident shall not exceed $[X]"
   Risk: Can add up if multiple incidents
   Less common: Primarily in insurance and high-volume transactions
```

### Indemnification Patterns
```
MUTUAL INDEMNIFICATION (Preferred):
Each party indemnifies the other for:
- Their own breach of the agreement
- Their own negligence or willful misconduct
- Their own IP infringement claims
- Their own violation of law

ONE-SIDED INDEMNIFICATION (Watch for):
Only one party provides indemnification. Acceptable when:
- One party bears all the risk (e.g., vendor providing a product)
- Balanced by other protections (liability cap, insurance)

BROAD INDEMNIFICATION (Red flag):
"Indemnify against any and all claims arising from or related to..."
Problem: "Related to" is extremely broad
Fix: Narrow to "arising from [party's] breach of this Agreement"
```

### Termination Provisions
```
FOR CONVENIENCE:
  Ideal: Either party, 30 days written notice
  Acceptable: 60 days written notice
  Red flag: Only one party has convenience termination right

FOR CAUSE:
  Standard: Material breach + 30-day cure period
  Acceptable: Material breach + 15-day cure period for payment, 30 days for other
  Red flag: Immediate termination without cure period (except for egregious breach)

INSOLVENCY TRIGGER:
  Standard: Right to terminate if other party becomes insolvent, files bankruptcy
  Note: Ipso facto clauses may not be enforceable in bankruptcy

EFFECT OF TERMINATION:
  Must address:
  - Payment for work performed to date
  - Return or destruction of confidential information
  - Data export / portability (especially SaaS)
  - Transition assistance (reasonable period at standard rates)
  - Wind-down of ongoing obligations
  - Survival clauses
```

### Data and Privacy Provisions
```
DATA OWNERSHIP:
  Customer data: Always ensure you retain ownership of your data
  Usage data: Clarify whether vendor can use aggregated/anonymized data
  Derived data: Who owns insights or models built from your data?

DATA PROCESSING:
  GDPR: Requires Data Processing Agreement (DPA) for EU personal data
  CCPA: Requires service provider addendum for California resident data
  HIPAA: Requires Business Associate Agreement (BAA) for health data

DATA PORTABILITY:
  Right to export: In standard, machine-readable format
  Timing: Within 30 days of termination
  Cost: At no additional charge (or at cost)
  Format: CSV, JSON, API access during transition period

DATA DELETION:
  Upon termination: Vendor must delete or return all customer data
  Timeline: Within 30-60 days of termination
  Certification: Written confirmation of deletion
  Exception: Legally required retention (must be disclosed)
```

## Risk Scoring Detailed Guide

### Scoring Each Category (1-5)

**Liability Cap**:
- 1: Mutual cap at 12+ months fees with super cap carve-outs
- 2: Mutual cap at 12 months, no carve-outs
- 3: Cap at less than 12 months, or asymmetric caps
- 4: Very low cap (3 months or less) or uncapped for one party
- 5: Unlimited liability for you, capped for them

**Indemnification**:
- 1: Mutual, limited to direct breach, with defense obligation
- 2: Mutual, slightly broader scope
- 3: Mostly mutual but with asymmetric carve-outs
- 4: One-sided or very broad "any and all claims"
- 5: Unlimited indemnification with no cap

**IP Ownership**:
- 1: You own deliverables, vendor retains tools/methods, clear license
- 2: You own deliverables but definition is slightly narrow
- 3: Shared or ambiguous ownership
- 4: Vendor retains most IP rights to deliverables
- 5: "All work product" assigned to vendor including your pre-existing IP

**Termination Rights**:
- 1: Mutual convenience + cause with reasonable cure
- 2: Mutual cause with cure, convenience one-sided but acceptable
- 3: No convenience termination, or very long notice periods
- 4: Only vendor can terminate for convenience
- 5: Locked in with no exit, or punitive early termination fees

### Weight Justification
| Criteria | Weight | Why |
|----------|--------|-----|
| Liability Cap | x3 | Financial exposure is the highest-stakes term |
| Indemnification | x3 | Can exceed liability cap in some structures |
| IP Ownership | x3 | Core value of many engagements |
| Termination Rights | x2 | Flexibility to exit is critical |
| Confidentiality | x2 | Protects competitive advantage |
| Data Privacy | x2 | Regulatory risk and reputation |
| Payment Terms | x1 | Cash flow impact, usually negotiable |
| Non-Compete | x2 | Can restrict business operations |
| Governing Law | x1 | Matters in disputes, usually low probability |
| Auto-Renewal | x1 | Calendar management mitigates risk |

## Common Negotiation Strategies

### BATNA Analysis
```
YOUR BATNA (Best Alternative to Negotiated Agreement):
  Alternative vendor:    [Name, estimated terms]
  In-house option:       [Feasibility, cost]
  Do nothing:            [Impact of not proceeding]
  BATNA strength:        [Strong / Moderate / Weak]

THEIR BATNA:
  Alternative customer:  [Their pipeline status]
  Revenue importance:    [How much they need this deal]
  Competitive pressure:  [Other vendors bidding]
  BATNA strength:        [Strong / Moderate / Weak]

ZOPA (Zone of Possible Agreement):
  Your walk-away:        [Terms you will not accept]
  Their likely floor:    [Terms they probably cannot go below]
  ZOPA exists:           [Yes / No / Unknown]
```

### Concession Planning
| Priority | Your Position | Acceptable Compromise | Walk Away |
|----------|--------------|----------------------|-----------|
| Must-have | [Your ideal] | [Minimum acceptable] | [If not met, stop] |
| Important | [Your ideal] | [Compromise] | [Reluctant concession] |
| Nice-to-have | [Your ideal] | [Easy to concede] | [Trade for must-have] |

**Rule**: Never concede a must-have to gain a nice-to-have. Use nice-to-haves as bargaining chips.

## Contract Lifecycle Management

### Key Dates to Track
For every contract, calendar these dates:
1. **Execution date**: When signed
2. **Effective date**: When obligations begin
3. **Auto-renewal notice deadline**: Usually 30-90 days before renewal date
4. **Renewal date**: When the term renews
5. **Expiration date**: When the term ends
6. **Milestone dates**: Payment milestones, deliverable dates
7. **Audit dates**: If audit rights exist, when they can be exercised
8. **Insurance renewal**: If insurance requirements, when certs expire
9. **Rate change dates**: When pricing can be adjusted
10. **Review dates**: Internal review before renewal decisions
