---
name: nda-generator
description: Generate non-disclosure agreements for various business contexts. Use when user mentions "NDA," "non-disclosure agreement," "confidentiality agreement," "mutual NDA," "unilateral NDA," "trade secret protection."
metadata:
  version: 1.0.0
  category: legal-compliance
---

# NDA Generator

Generate tailored non-disclosure agreements for employee, vendor, partner, and investor relationships with appropriate confidentiality protections.

## Purpose

This skill produces NDAs calibrated to the relationship type, risk level, and jurisdiction. It supports mutual, unilateral, and multilateral agreements and includes clause libraries for specialized contexts such as M&A due diligence, technology licensing, and employment.

## Quick Reference

### NDA Types

| Type          | Parties Protected | Common Use Cases                            | Complexity |
|---------------|-------------------|---------------------------------------------|------------|
| Unilateral    | One party         | Employment, vendor onboarding, consulting   | Low        |
| Mutual (Bilateral) | Both parties | Partnerships, joint ventures, vendor eval   | Medium     |
| Multilateral  | Three+ parties    | Consortium projects, multi-party deals      | High       |

### Context-Specific Guidance

| Context       | Term Length  | Key Focus                          | Special Considerations             |
|---------------|-------------|------------------------------------|------------------------------------|
| Employee      | Employment + 2 years | Trade secrets, IP, customer lists | Non-compete interaction, at-will   |
| Vendor        | Contract + 1 year    | Technical specs, pricing, processes | Subcontractor flow-down           |
| Partner       | 3-5 years            | Joint IP, business plans, strategy | Mutual disclosure, ownership      |
| Investor      | 2-3 years            | Financials, projections, cap table | Carve-outs for portfolio companies|
| M&A           | 2-3 years            | All business information           | Standstill, non-solicitation      |
| Technology    | 5+ years             | Source code, algorithms, patents   | Reverse engineering prohibition   |

### Enforceability Factors

| Factor              | Strengthens NDA                    | Weakens NDA                        |
|---------------------|------------------------------------|------------------------------------|
| Definition scope    | Specific, clearly bounded          | Vague, overly broad                |
| Duration            | Reasonable (2-5 years)             | Perpetual or excessive             |
| Consideration       | Mutual benefit or compensation     | No consideration provided          |
| Exclusions          | Standard carve-outs present        | No exclusions listed               |
| Remedies            | Injunctive relief + damages        | Only monetary damages              |
| Jurisdiction        | Clear choice of law                | Silent on jurisdiction             |

## NDA Template: Mutual Agreement

```
MUTUAL NON-DISCLOSURE AGREEMENT

Effective Date: [DATE]
Agreement Number: [NDA-YYYY-NNN]

PARTIES
Disclosing/Receiving Party 1: [COMPANY A]
  Address: [ADDRESS]
  Contact: [NAME, TITLE, EMAIL]

Disclosing/Receiving Party 2: [COMPANY B]
  Address: [ADDRESS]
  Contact: [NAME, TITLE, EMAIL]

PURPOSE
The parties wish to explore [DESCRIPTION OF BUSINESS PURPOSE]
(the "Purpose") and in connection therewith may disclose
Confidential Information to each other.

1. DEFINITION OF CONFIDENTIAL INFORMATION
"Confidential Information" means any information disclosed by
either party ("Disclosing Party") to the other ("Receiving Party"),
whether orally, in writing, electronically, or by inspection,
that is designated as confidential or that a reasonable person
would understand to be confidential given the nature of the
information and circumstances of disclosure. This includes but
is not limited to:

   a) Technical information: software, source code, algorithms,
      designs, specifications, architectures, prototypes
   b) Business information: strategies, plans, financials,
      pricing, customer lists, supplier agreements
   c) Product information: roadmaps, features, release plans
   d) Any derivatives, notes, analyses, or summaries containing
      or reflecting Confidential Information

2. EXCLUSIONS FROM CONFIDENTIAL INFORMATION
Confidential Information does not include information that:
   a) Is or becomes publicly available through no fault of
      the Receiving Party
   b) Was known to the Receiving Party prior to disclosure,
      as documented by written records
   c) Is independently developed by the Receiving Party
      without use of Confidential Information
   d) Is disclosed to the Receiving Party by a third party
      without restriction on disclosure
   e) Is required to be disclosed by law, regulation, or
      court order, provided the Receiving Party gives prompt
      notice and cooperates to obtain protective orders

3. OBLIGATIONS OF THE RECEIVING PARTY
   a) Use Confidential Information solely for the Purpose
   b) Restrict access to those with a need to know who are
      bound by confidentiality obligations at least as
      protective as these terms
   c) Protect Confidential Information with at least the
      same degree of care used for its own confidential
      information, but no less than reasonable care
   d) Not reverse engineer, decompile, or disassemble any
      Confidential Information
   e) Promptly notify the Disclosing Party of any
      unauthorized disclosure or use

4. TERM AND DURATION
   a) This Agreement is effective from the Effective Date
      and continues for [2] years ("Term")
   b) Confidentiality obligations survive for [3] years
      after the last disclosure of Confidential Information
   c) Trade secret protections continue for as long as the
      information qualifies as a trade secret under
      applicable law

5. RETURN OR DESTRUCTION
Upon termination or request by the Disclosing Party:
   a) Return or destroy all Confidential Information
   b) Provide written certification of destruction
   c) Exception: retain one archival copy for legal
      compliance purposes, subject to ongoing obligations

6. REMEDIES
   a) The parties acknowledge that breach may cause
      irreparable harm not adequately compensated by
      monetary damages
   b) The Disclosing Party is entitled to seek injunctive
      relief without posting bond
   c) Remedies are cumulative and not exclusive

7. NO LICENSE OR WARRANTY
   a) No license under any patent, copyright, or other IP
      is granted by this Agreement
   b) Confidential Information is provided "as is" without
      warranty of any kind

8. GOVERNING LAW AND JURISDICTION
   a) This Agreement is governed by the laws of [STATE/COUNTRY]
   b) Courts of [JURISDICTION] have exclusive jurisdiction

9. GENERAL PROVISIONS
   a) Entire Agreement: supersedes all prior agreements
   b) Amendments: must be in writing signed by both parties
   c) Assignment: not assignable without written consent
   d) Severability: invalid provisions do not affect remainder
   e) Waiver: failure to enforce is not a waiver
   f) Counterparts: may be executed in counterparts
   g) Notices: written notice to addresses above

SIGNATURES

_________________________    _________________________
[NAME]                       [NAME]
[TITLE], [COMPANY A]         [TITLE], [COMPANY B]
Date: ___________            Date: ___________
```

## Clause Variations by Context

### Employee NDA Additions

```
EMPLOYEE-SPECIFIC CLAUSES

A. WORK PRODUCT ASSIGNMENT
   All inventions, discoveries, and works of authorship
   created during employment and related to the company's
   business are the exclusive property of the Company.

B. NON-SOLICITATION
   For [12] months following termination, Employee shall
   not solicit any customer, client, or employee of the
   Company.

C. PRIOR INVENTIONS
   Employee has listed all prior inventions in Exhibit A.
   These remain Employee's property.

D. EXIT OBLIGATIONS
   Upon termination, Employee shall:
   - Return all company property and materials
   - Delete company data from personal devices
   - Participate in an exit interview
   - Sign a separation acknowledgment
```

### Investor NDA Additions

```
INVESTOR-SPECIFIC CLAUSES

A. PORTFOLIO COMPANY CARVE-OUT
   Investor's confidentiality obligations do not prevent
   sharing information with portfolio companies, provided
   they are bound by similar obligations and the information
   is not shared with direct competitors.

B. INVESTMENT DECISION
   Investor may use Confidential Information solely to
   evaluate a potential investment and shall not use it
   for any trading purpose.

C. CO-INVESTOR SHARING
   Investor may share Confidential Information with
   potential co-investors, subject to their execution
   of a substantially similar NDA.
```

### Vendor NDA Additions

```
VENDOR-SPECIFIC CLAUSES

A. SUBCONTRACTOR FLOW-DOWN
   Vendor shall ensure all subcontractors with access to
   Confidential Information are bound by obligations at
   least as protective as this Agreement.

B. DATA HANDLING
   Vendor shall handle all data in accordance with the
   Company's data handling policy (Exhibit B) and applicable
   data protection regulations.

C. AUDIT RIGHTS
   Company may audit Vendor's compliance with this Agreement
   upon [30] days written notice, no more than once per year.

D. INSURANCE
   Vendor shall maintain cyber liability insurance with
   coverage of at least [$X] million.
```

## Term and Duration Guidance

| Relationship     | Agreement Term | Survival Period | Trade Secrets     |
|------------------|----------------|-----------------|-------------------|
| Employee         | During employment | 2 years post-termination | Indefinite |
| Contractor       | During engagement | 2 years post-termination | Indefinite |
| Vendor           | Contract term  | 1-2 years post-termination | Indefinite |
| Partner          | Project term   | 3 years post-termination | Indefinite |
| Investor         | 2 years        | 2-3 years post-termination | Indefinite |
| M&A Due Diligence| 1-2 years      | 2-3 years post-termination | Indefinite |

## Workflow

1. **Determine NDA type**: Unilateral, mutual, or multilateral
2. **Identify context**: Employee, vendor, partner, investor, M&A
3. **Select template**: Base template plus context-specific addenda
4. **Customize clauses**: Adjust definitions, term, jurisdiction, remedies
5. **Add special provisions**: Non-solicitation, carve-outs, audit rights as needed
6. **Review enforceability**: Check against jurisdiction-specific requirements
7. **Generate document**: Produce final NDA with signature blocks

## Scripts & Tools

**Generate NDA**:
```bash
scripts/generate-nda.sh --type mutual --context vendor --jurisdiction delaware --output nda.md
```

**Clause library**:
```bash
scripts/nda-clauses.sh --list-all
scripts/nda-clauses.sh --category "employee" --clause "non-solicitation"
```

**Compare NDAs**:
```bash
scripts/nda-compare.sh --file1 their-nda.pdf --file2 our-template.md --output diff-report.md
```

## Best Practices

- Always define "Confidential Information" specifically; overly broad definitions reduce enforceability.
- Include standard exclusions (public knowledge, prior knowledge, independent development, third-party disclosure, legal compulsion) in every NDA.
- Match the term length to the business relationship and sensitivity of information.
- Specify return or destruction obligations clearly, including certification requirements.
- Include injunctive relief language to enable courts to issue immediate protection.
- For employee NDAs, ensure compatibility with local non-compete and employment laws.
- Have the receiving party's legal counsel review any NDA before signing.
- Maintain a central NDA register tracking all active agreements, expiration dates, and key terms.
- Consider including a residuals clause for general knowledge retained in unaided memory, especially in technology contexts.
