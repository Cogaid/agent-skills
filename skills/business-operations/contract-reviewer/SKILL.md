---
name: contract-reviewer
description: Review contracts for key terms, risks, and negotiation opportunities. Use when the user mentions "review contract," "contract analysis," "legal review," "red flags," "contract terms," "liability clause," "termination clause," "NDA review," "MSA review," "SLA review," "indemnification," or "contract risk."
metadata:
  version: 1.0.0
  category: finance-operations
---

# Contract Reviewer

Review contracts systematically to identify key terms, flag risks, and prepare negotiation recommendations.

## Purpose

This skill provides a structured approach to contract review for business professionals (not a substitute for legal counsel). It helps you identify critical clauses, score risk levels, flag problematic language, and prepare a summary memo for decision-makers. Always have material contracts reviewed by qualified legal counsel before signing.

## Quick Start

1. **Identify contract type**: MSA, SOW, NDA, SaaS, employment, vendor
2. **Run the checklist**: Walk through every clause category below
3. **Flag red terms**: Compare against the red flag table
4. **Score risk**: Use the risk scoring framework
5. **Draft summary memo**: Highlight findings for stakeholders
6. **Prepare negotiation points**: List changes to request

## Contract Review Checklist

```
CONTRACT REVIEW CHECKLIST
─────────────────────────────────────────
Document:     [Contract Title]
Parties:      [Party A] and [Party B]
Type:         [MSA / SOW / NDA / SaaS / Vendor / Employment]
Reviewer:     [Name]
Date:         [Date]
Review #:     [1st / 2nd / Final]

SECTION                              STATUS    RISK    NOTES
──────────────────────────────────   ──────    ────    ──────────
□ Parties & Definitions              [ ]       [ ]
□ Scope of Services / Products       [ ]       [ ]
□ Term & Renewal                     [ ]       [ ]
□ Termination Rights                 [ ]       [ ]
□ Pricing & Payment Terms            [ ]       [ ]
□ Intellectual Property              [ ]       [ ]
□ Confidentiality                    [ ]       [ ]
□ Data Privacy & Security            [ ]       [ ]
□ Representations & Warranties       [ ]       [ ]
□ Indemnification                    [ ]       [ ]
□ Limitation of Liability            [ ]       [ ]
□ Insurance Requirements             [ ]       [ ]
□ Non-Compete / Non-Solicitation     [ ]       [ ]
□ Dispute Resolution                 [ ]       [ ]
□ Governing Law & Jurisdiction       [ ]       [ ]
□ Force Majeure                      [ ]       [ ]
□ Assignment & Subcontracting        [ ]       [ ]
□ Compliance & Regulatory            [ ]       [ ]
□ Change Order Process               [ ]       [ ]
□ SLA & Performance Standards        [ ]       [ ]
□ Audit Rights                       [ ]       [ ]
□ Entire Agreement / Amendments      [ ]       [ ]
□ Notices                            [ ]       [ ]
□ Signatures & Authority             [ ]       [ ]

OVERALL RISK LEVEL:  [ ] Low  [ ] Medium  [ ] High  [ ] Critical
RECOMMENDATION:      [ ] Sign  [ ] Sign with changes  [ ] Renegotiate  [ ] Walk away
```

## Red Flag Terms Table

| Red Flag | What to Watch For | Risk Level | Recommended Response |
|----------|------------------|------------|---------------------|
| **Unlimited liability** | No cap on damages you owe | Critical | Negotiate cap (12 months of fees typical) |
| **Auto-renewal with long notice** | 60-90 day cancellation window | High | Reduce to 30 days; add reminder to calendar |
| **Broad IP assignment** | "All work product" includes pre-existing IP | Critical | Carve out pre-existing and general knowledge |
| **Unilateral amendment** | "We may modify terms at any time" | High | Require mutual written consent for changes |
| **Non-mutual NDA** | Only one party's info is protected | Medium | Make confidentiality obligations mutual |
| **Broad indemnification** | Indemnify for "any and all claims" | High | Limit to direct, caused by your breach |
| **Unlimited non-compete** | No geographic or time limit | Critical | Narrow scope, geography, and duration |
| **No termination for convenience** | Locked in for full term | High | Add 30-60 day termination for convenience |
| **Mandatory arbitration** | Waives right to court / jury | Medium | Evaluate cost; may favor larger party |
| **Most favored nation decay** | Price matching but only downward | Medium | Make MFN bidirectional or remove |
| **Audit without limits** | Unlimited audit rights, your cost | Medium | Limit frequency (annual), share costs |
| **Data ownership ambiguity** | Unclear who owns customer data | Critical | Explicitly state you own your data |
| **Consequential damages** | Liable for lost profits, etc. | High | Exclude consequential / indirect damages |
| **Survival clauses** | Obligations survive for 5+ years | Medium | Limit survival to 2-3 years max |

## Key Clause Categories

### 1. Liability & Indemnification

```
WHAT TO CHECK:
─────────────────────────────────────────
□ Is liability capped? At what amount?
  Standard: Cap at 12 months of fees paid/payable
  Aggressive: Cap at fees paid in last 3 months
  Favorable: Uncapped for IP infringement and confidentiality breach

□ Are consequential damages excluded?
  Ideal: Mutual exclusion of indirect, consequential, punitive damages
  Acceptable: Carve-outs for IP infringement and confidentiality

□ Is indemnification mutual?
  Each party indemnifies for their own breach, negligence, IP infringement

□ Defense vs. hold harmless:
  "Defend and indemnify" = they pay legal fees too
  "Indemnify" alone = may only cover damages, not defense costs
```

### 2. Termination

```
TERMINATION REVIEW:
─────────────────────────────────────────
□ For convenience: Can either party exit without cause?
  Ideal: 30-day written notice, either party
  Acceptable: 60-day notice

□ For cause: What triggers termination for breach?
  Standard: Material breach + 30-day cure period
  Watch for: Immediate termination for minor breaches

□ Effect of termination:
  - Payment for work completed?
  - Return/destruction of confidential info?
  - Transition assistance period?
  - Data export / portability?

□ Survival: Which clauses survive termination?
  Typical: Confidentiality, IP, indemnification, limitation of liability
```

### 3. Intellectual Property

```
IP REVIEW:
─────────────────────────────────────────
□ Who owns deliverables? (Work product created under the contract)
□ Who owns pre-existing IP? (Background IP each party brings)
□ Is there a license grant for pre-existing IP embedded in deliverables?
□ Are "work made for hire" provisions appropriate?
□ Does the vendor retain rights to general tools, methods, know-how?
□ Is there an IP infringement indemnification?
□ Open source: Any obligations around open source components?
```

### 4. Confidentiality

```
CONFIDENTIALITY REVIEW:
─────────────────────────────────────────
□ Is the definition of "Confidential Information" appropriate?
  Not too broad (everything is confidential)
  Not too narrow (key info excluded)
□ Are standard exclusions present?
  Public knowledge, independently developed, required by law
□ Duration: How long do obligations last? (2-5 years typical; trade secrets = indefinite)
□ Permitted disclosures: employees, contractors, advisors on need-to-know?
□ Return/destruction obligations on termination?
□ Is it mutual?
```

## Risk Scoring Framework

Score each clause category 1-5, then calculate overall risk:

| Score | Level | Meaning |
|-------|-------|---------|
| 1 | Minimal | Standard, fair, no concerns |
| 2 | Low | Minor issues, easily negotiated |
| 3 | Moderate | Requires attention, negotiate before signing |
| 4 | High | Significant risk, must be changed |
| 5 | Critical | Deal-breaker, do not sign as-is |

```
RISK SCORECARD
──────────────────────────────────────────
Clause Category              Score (1-5)    Weight    Weighted
────────────────────────     ──────────    ──────    ────────
Liability Cap                    [ ]        x3        [ ]
Indemnification                  [ ]        x3        [ ]
IP Ownership                     [ ]        x3        [ ]
Termination Rights               [ ]        x2        [ ]
Confidentiality                  [ ]        x2        [ ]
Data Privacy                     [ ]        x2        [ ]
Payment Terms                    [ ]        x1        [ ]
Non-Compete                      [ ]        x2        [ ]
Governing Law                    [ ]        x1        [ ]
Auto-Renewal                     [ ]        x1        [ ]
──────────────────────────────────────────
TOTAL WEIGHTED SCORE:            [ ] / 100

Interpretation:
  20-35:  Low risk -- proceed with minor edits
  36-55:  Moderate risk -- negotiate flagged items
  56-75:  High risk -- significant renegotiation needed
  76-100: Critical risk -- consider walking away
```

## Negotiation Points Template

```
CONTRACT NEGOTIATION MEMO
─────────────────────────────────────────
Contract:     [Title]
Counterparty: [Name]
Date:         [Date]
Priority:     [Must-have / Nice-to-have / Walk-away]

#  CLAUSE        CURRENT LANGUAGE (SUMMARY)    REQUESTED CHANGE           PRIORITY
─  ──────────    ──────────────────────────    ─────────────────────────  ────────
1  Liability     Unlimited                     Cap at 12 months fees      Must-have
2  Termination   No convenience termination    Add 30-day for convenience Must-have
3  IP            All work product assigned      Carve out pre-existing IP  Must-have
4  Auto-renew    90-day notice to cancel        30-day notice              Nice-to-have
5  Governing law Their state                    Our state or neutral       Nice-to-have

WALK-AWAY THRESHOLD:
If items 1-3 are not resolved, we should not proceed with this contract.

LEVERAGE POINTS:
• [Our strengths in this negotiation]
• [Alternatives we have]
• [Time pressure on either side]
```

## Summary Memo Format

```
CONTRACT REVIEW SUMMARY
═══════════════════════════════════════════
Contract:       [Title / Type]
Counterparty:   [Name]
Value:          $[Amount] over [Term]
Reviewer:       [Name]
Date:           [Date]

RECOMMENDATION: [Sign / Sign with Changes / Renegotiate / Decline]

KEY FINDINGS:
1. [Finding 1 -- most important]
2. [Finding 2]
3. [Finding 3]

RISK LEVEL: [Low / Medium / High / Critical] (Score: XX/100)

REQUIRED CHANGES BEFORE SIGNING:
• [Change 1]
• [Change 2]

FINANCIAL IMPACT:
• Total contract value: $XXX,XXX
• Maximum liability exposure: $XXX,XXX
• Termination cost (early exit): $XX,XXX

TIMELINE:
• Contract received: [Date]
• Review completed: [Date]
• Response deadline: [Date]
• Proposed effective date: [Date]

NEXT STEPS:
1. [Action with owner and date]
2. [Action with owner and date]
```

## Scripts & Tools

**review_contract.py**: Automated clause extraction and flagging
```bash
python scripts/review_contract.py --file contract.pdf --type msa
# Output: Extracted clauses with risk flags
```

**compare_contracts.py**: Diff two contract versions
```bash
python scripts/compare_contracts.py --original v1.pdf --revised v2.pdf
# Output: Side-by-side changes with risk impact
```

**contract_tracker.py**: Track contract deadlines and renewals
```bash
python scripts/contract_tracker.py --upcoming 90
# Output: Contracts expiring or renewing in next 90 days
```

## Best Practices

1. **Read the entire contract**: Skimming misses critical clauses buried in boilerplate
2. **Check definitions first**: Defined terms control meaning throughout the document
3. **Compare to your standard terms**: Know what you normally accept before reviewing theirs
4. **Flag, don't fix**: Note issues and let legal counsel draft the actual redline language
5. **Track versions**: Every revision should be clearly marked with date and party
6. **Calendar all deadlines**: Renewal notices, cure periods, milestones -- all go on the calendar
7. **Consider the relationship**: Aggressive terms signal how the counterparty handles disputes
8. **Get it in writing**: Side conversations and verbal agreements should be reflected in the contract
9. **Involve stakeholders early**: Technical, financial, and legal teams should all review relevant sections
10. **Never sign under pressure**: A deadline to sign is a negotiation tactic, not a legal requirement
