# NDA Generator - Reference Guide

## NDA Enforceability by Jurisdiction

### United States

| State | Non-Compete Enforceability | NDA Duration Limit | Key Considerations |
|---|---|---|---|
| California | Not enforceable (with narrow exceptions) | Reasonable (typically 2-5 years) | Cannot restrict mobility; focus on trade secrets |
| New York | Enforceable if reasonable | Reasonable | Narrowly tailored scope required |
| Texas | Enforceable with consideration | Reasonable | Reformation doctrine applies |
| Delaware | Enforceable | Reasonable | Most business-friendly state |
| Massachusetts | Limited (12 months max for employment) | Reasonable | Garden leave required for non-competes |
| Washington | Limited (18 months max) | Reasonable | Income threshold for enforcement |

### International

| Jurisdiction | NDA Enforceability | Special Requirements |
|---|---|---|
| United Kingdom | Strong | Must be reasonable in scope and duration |
| European Union | Strong (varies by member state) | GDPR data handling provisions may apply |
| Canada | Strong | Provincial variations; must be reasonable |
| Australia | Moderate | Must be reasonable restraint of trade |
| India | Moderate | Non-competes largely unenforceable under Sec. 27 |
| China | Moderate | Confidentiality agreements enforceable; non-compete limited |
| Japan | Moderate | Must be reasonable and compensated |

## Confidential Information Categories

### Technology and IP

| Category | Examples | Protection Level | Typical Duration |
|---|---|---|---|
| Source code | Application code, libraries, algorithms | Maximum | Indefinite (trade secret) |
| Architecture | System design, infrastructure diagrams | High | 5+ years |
| Patents (pre-filing) | Inventions, patent applications in draft | Maximum | Until filing/publication |
| Trade secrets | Proprietary processes, formulas | Maximum | Indefinite |
| Roadmap | Product plans, feature schedules | High | 2-3 years |

### Business and Financial

| Category | Examples | Protection Level | Typical Duration |
|---|---|---|---|
| Financial statements | Revenue, profit margins, burn rate | High | 3-5 years |
| Pricing | Pricing models, discount structures | High | 2-3 years |
| Customer lists | Customer names, contracts, deal sizes | High | 3-5 years |
| Business strategy | Growth plans, market entry strategy | High | 2-3 years |
| M&A activity | Acquisition targets, deal terms | Maximum | 3-5 years |

### Personnel and Operations

| Category | Examples | Protection Level | Typical Duration |
|---|---|---|---|
| Compensation data | Salary bands, equity grants, bonuses | High | 2-3 years |
| Employee records | Performance reviews, personal information | High | GDPR/applicable law |
| Vendor agreements | Contract terms, pricing from suppliers | Medium | 2 years |
| Operational processes | Internal workflows, methodologies | Medium | 2-3 years |

## Standard Exclusions Analysis

| Exclusion | Purpose | How to Document |
|---|---|---|
| Public knowledge | Information already in public domain | Cite public source and date |
| Prior knowledge | Receiving party already knew it | Written records predating disclosure |
| Independent development | Created without using confidential info | Development logs, clean room procedures |
| Third-party disclosure | Received from unrestricted third party | Written agreement from third party |
| Legal compulsion | Required by court order or regulation | Court order + notice to disclosing party |
| Residuals (optional) | General knowledge retained in memory | Define scope carefully; controversial |

## Clause Variations Reference

### Non-Solicitation Variations

**Standard Non-Solicitation (Employees):**
```
For [12] months following termination, Receiving Party shall not
directly or indirectly solicit, recruit, or hire any employee or
contractor of the Disclosing Party with whom the Receiving Party
had material contact during the relationship.
```

**Limited Non-Solicitation (Customers):**
```
For [12] months following termination, Receiving Party shall not
solicit business from any customer of the Disclosing Party whose
identity or business was learned through Confidential Information.
```

**Broad Non-Solicitation (M&A):**
```
For [24] months following the Effective Date, Receiving Party
shall not, directly or indirectly, solicit, recruit, hire, or
engage any employee, officer, or consultant of the Disclosing
Party, or induce any such person to terminate their relationship
with the Disclosing Party.
```

### Standstill Provisions (M&A NDAs)

```
For a period of [12] months from the Effective Date, without the
prior written consent of [Company], Receiving Party shall not:

(a) acquire or propose to acquire any securities or assets of
    [Company];
(b) propose any merger, business combination, or similar
    transaction with [Company];
(c) make any public announcement regarding any of the foregoing;
(d) form or participate in a group (within the meaning of
    Section 13(d)(3) of the Exchange Act) with respect to
    [Company]'s securities.
```

### Residuals Clause

```
Nothing in this Agreement shall restrict either party's use of
Residuals. "Residuals" means information retained in the
unaided memory of a party's personnel who had access to
Confidential Information, excluding any specific technical
data, source code, or financial information.

This clause does not grant a license under any intellectual
property rights.
```

## NDA Register Management

### Required Fields for NDA Tracking

| Field | Description | Example |
|---|---|---|
| NDA ID | Unique identifier | NDA-2025-042 |
| Counterparty | Other party name | Acme Corporation |
| NDA Type | Unilateral, Mutual, Multilateral | Mutual |
| Context | Reason for NDA | Partnership evaluation |
| Effective Date | When NDA takes effect | 2025-01-15 |
| Term End Date | When disclosure period ends | 2027-01-15 |
| Survival Date | When obligations end | 2030-01-15 |
| Governing Law | Applicable jurisdiction | Delaware |
| Key Restrictions | Special clauses | Non-solicitation, standstill |
| Contact | Counterparty contact person | Jane Smith, jane@acme.com |
| Internal Owner | Who manages this NDA | Legal Team |
| Status | Current state | Active / Expired / Terminated |

### Lifecycle Events to Track

| Event | When to Record | Action Required |
|---|---|---|
| Execution | NDA signed by all parties | File executed copy, add to register |
| Amendment | Any modification to terms | File amendment, update register |
| Disclosure | Material confidential info shared | Log disclosure for tracking |
| Breach suspected | Any unauthorized disclosure | Trigger incident response |
| Term expiration | Disclosure period ends | Verify no ongoing disclosures |
| Return/destruction | Per agreement terms | Obtain destruction certification |
| Survival expiration | All obligations end | Close register entry |

## Remedies and Enforcement

### Types of Remedies

| Remedy | Description | When Available |
|---|---|---|
| Injunctive relief | Court order to stop breach | Irreparable harm demonstrated |
| Temporary restraining order | Emergency stop order | Immediate threat of harm |
| Monetary damages | Compensation for losses | Quantifiable financial harm |
| Liquidated damages | Pre-agreed damage amount | Specified in NDA (if enforceable) |
| Attorney fees | Recovery of legal costs | If specified in NDA |
| Specific performance | Court-ordered compliance | Where damages are inadequate |

### Injunctive Relief Language

```
The parties acknowledge that a breach of this Agreement may cause
irreparable harm to the Disclosing Party that cannot be adequately
compensated by monetary damages alone. Accordingly, the Disclosing
Party shall be entitled to seek equitable relief, including
injunction and specific performance, in addition to all other
remedies available at law or in equity, without the necessity of
proving actual damages or posting any bond or other security.
```
