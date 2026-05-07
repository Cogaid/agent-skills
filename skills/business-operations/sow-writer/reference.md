# SOW Writer - Reference Documentation

## Engagement Types Deep Dive

### Fixed-Price Engagements
**How it works**: Total price agreed upfront for defined scope and deliverables.
**Payment trigger**: Milestone acceptance, not time elapsed.
**Risk allocation**: Provider bears risk of cost overruns; client bears risk of reduced flexibility.

**When to use**:
- Scope is well-defined and unlikely to change significantly
- Both parties have experience with similar projects
- Client wants budget certainty
- Provider can accurately estimate effort

**Pricing formula**:
```
Fixed Price = (Estimated Hours x Blended Rate) x (1 + Risk Buffer %)
Risk Buffer: 15-25% for well-defined scope, 30-50% for ambiguous scope
```

**Margin protection strategies**:
1. Define scope precisely with explicit exclusions
2. Limit revision rounds per deliverable (typically 2)
3. Include change order process for anything out of scope
4. Tie payments to client-dependent milestones (client delays = timeline adjustment)
5. Include "deemed acceptance" clause (no response = accepted)

### Time & Materials (T&M) Engagements
**How it works**: Client pays for actual time spent at agreed hourly/daily rates.
**Payment trigger**: Monthly or bi-weekly invoicing based on timesheets.
**Risk allocation**: Client bears cost risk; provider bears utilization risk.

**When to use**:
- Scope is evolving or hard to define upfront
- Client wants maximum flexibility
- Discovery or R&D work
- Staff augmentation or ongoing support

**Rate structures**:
```
Standard Rate Card:
  Junior / Associate:     $100-150/hr
  Mid-level:              $150-225/hr
  Senior / Lead:          $200-300/hr
  Architect / Principal:  $275-400/hr
  Project Manager:        $150-250/hr

Blended Rate:
  Blended Rate = Sum of (Role Rate x Estimated % of effort) for all roles
```

**Client protections for T&M**:
1. Weekly or monthly hour caps (not-to-exceed)
2. Rate lock for contract duration
3. Minimum experience levels per role
4. Right to approve team composition changes
5. Regular budget check-ins (weekly status with hours consumed vs. estimate)

### Retainer Engagements
**How it works**: Client pays a fixed monthly fee for reserved capacity.
**Payment trigger**: Monthly, typically in advance.
**Key terms**: Hours included, rollover policy, overage rates.

```
Retainer Structure:
  Monthly Fee:        ${{amount}}
  Hours Included:     {{hours}} hours/month
  Rollover:           [ ] No rollover  [ ] Up to {{max_rollover}} hours
  Overage Rate:       ${{overage_rate}}/hr (typically 110-125% of blended rate)
  Minimum Term:       {{months}} months
  Notice to Cancel:   {{notice_days}} days
```

### Hybrid Models
Common combinations:
- **Fixed + T&M**: Fixed price for defined scope, T&M for support/maintenance
- **T&M with Cap**: T&M billing with a not-to-exceed ceiling
- **Retainer + Project**: Monthly retainer for ongoing work + fixed-price for projects
- **Phase-based**: Fixed for discovery, T&M for build, retainer for support

## MoSCoW Prioritization Framework

### Detailed Definitions
| Priority | Meaning | Test | SOW Treatment |
|----------|---------|------|---------------|
| **Must Have** | Project fails without this | Would we cancel/delay without it? | In scope, priced, mandatory |
| **Should Have** | Important, not showstopper | Can we ship without it temporarily? | In scope, may be deferred |
| **Could Have** | Enhances value | Is it "nice to have"? | In scope only if time/budget allows |
| **Won't Have** | Agreed exclusion | Did we consider and reject it? | Explicitly listed as out of scope |

### How to run a MoSCoW session
1. List all requested features/activities
2. Stakeholders independently categorize each item
3. Discuss disagreements (especially Must vs. Should)
4. Confirm: Must Haves should be ~60% of estimated effort
5. Should Haves: ~20% of effort
6. Could Haves: ~20% of effort (these are your buffer)
7. Won't Haves: documented for future phases

## Acceptance Criteria Writing Guide

### SMART Criteria
Every acceptance criterion should be:
- **Specific**: Clear, unambiguous condition
- **Measurable**: Can be verified objectively
- **Achievable**: Technically feasible within scope
- **Relevant**: Directly related to the deliverable
- **Time-bound**: Has a defined review/test period

### Bad vs. Good Criteria

| Bad (Vague) | Good (Testable) |
|-------------|-----------------|
| "System is fast" | "Page load time < 3 seconds on 4G connection" |
| "User-friendly interface" | "New users complete core workflow in < 5 minutes without help" |
| "Handles high traffic" | "System supports 1,000 concurrent users with <500ms response time" |
| "Client is satisfied" | "All Must Have features pass UAT checklist with zero critical bugs" |
| "Mobile responsive" | "Layout renders correctly on viewports 320px-1440px (Chrome, Safari, Firefox)" |
| "Secure" | "Passes OWASP Top 10 security scan with zero high/critical findings" |

## Change Order Management

### When to Issue a Change Order
A change order is required when:
1. Client requests work not in the original scope
2. Assumptions documented in the SOW prove incorrect
3. Client delays impact the project timeline
4. Third-party dependencies change
5. Regulatory or compliance requirements emerge during the project
6. Technology constraints require a different approach

### Change Order Impact Assessment
```
IMPACT ASSESSMENT WORKSHEET
--------------------------------------
Change Description: {{description}}

Schedule:
  Current end date:          {{current_end}}
  New estimated end date:    {{new_end}}
  Schedule impact:           +{{days}} days

Cost:
  Estimated additional hours: {{hours}}
  Rate:                       ${{rate}}/hr
  Additional cost:            ${{cost}}
  Revised total:              ${{new_total}}

Resources:
  Additional resources needed: {{resources}}
  Resource availability:       {{availability}}

Risk:
  New risks introduced:        {{new_risks}}
  Impact on existing work:     {{impact}}

Dependencies:
  New dependencies:            {{dependencies}}
  Blocked items:               {{blockers}}
```

### Change Order Approval SLA
| Change Size | Approval Authority | Target Turnaround |
|------------|-------------------|-------------------|
| < $5,000 | Project sponsor | 2 business days |
| $5,000 - $25,000 | Department head | 5 business days |
| $25,000 - $100,000 | VP / Director | 10 business days |
| > $100,000 | C-level / Board | Negotiated |

## Milestone Payment Best Practices

### Payment Milestone Design Rules
1. **Front-load deposits**: 15-25% on SOW execution protects against client default
2. **Tie to acceptance, not dates**: Payment earned when deliverable is accepted, not when calendar says so
3. **Progressive billing**: Payments should roughly match effort invested to date
4. **Hold-back**: Keep 5-10% for post-launch support/warranty period
5. **Never leave more than 30% at the end**: Too much leverage for the client if they dispute final deliverables

### Sample Payment Distributions
```
LOW RISK (known client, clear scope):
  25% at signing | 25% at midpoint | 40% at delivery | 10% at 30-day review

MEDIUM RISK (new client, defined scope):
  30% at signing | 20% at design approval | 30% at development complete | 20% at go-live

HIGH RISK (new client, evolving scope):
  40% at signing | 20% at each of 3 milestones
```

## Governance and Communication

### RACI Matrix Template
```
                  Provider PM | Client PM | Provider Dev | Client SME | Exec Sponsor
Status Report        R/A      |    I      |     C        |    I       |     I
Scope Decision       C        |    R      |     I        |    C       |     A
Technical Decision   A        |    I      |     R        |    C       |     I
Budget Approval      C        |    R      |     I        |    I       |     A
Deliverable Review   R        |    A      |     C        |    R       |     I
Change Order         R        |    A      |     C        |    C       |     A

R = Responsible | A = Accountable | C = Consulted | I = Informed
```

### Escalation Matrix
| Level | Trigger | Who | Response Time |
|-------|---------|-----|---------------|
| 1 | Day-to-day issue | Project Managers | Same business day |
| 2 | Unresolved after 3 days | Department Heads | 2 business days |
| 3 | Budget/scope/timeline dispute | VP / Director | 5 business days |
| 4 | Relationship or contract-level | C-level executives | 10 business days |

## Risk Register Template
```
#  Risk                    Probability  Impact   Score   Mitigation              Owner
-  ----------------------  ----------   ------   -----   --------------------    -----
1  Client delays feedback  High         High     9       Buffer in timeline      PM
2  API not available       Medium       High     6       Identify alternatives   Dev Lead
3  Scope creep             High         Medium   6       Strict change orders    PM
4  Key person leaves       Low          High     3       Document + cross-train  PM
5  Tech doesn't scale      Low          Medium   2       POC in Phase 1          Architect
```
