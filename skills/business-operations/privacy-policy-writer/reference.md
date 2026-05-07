# Privacy Policy Writer - Reference Guide

## Regulatory Framework Deep Dive

### GDPR (General Data Protection Regulation)

#### Lawful Bases for Processing (Article 6)

| Lawful Basis | Description | When to Use | Documentation Required |
|---|---|---|---|
| Consent | Freely given, specific, informed, unambiguous | Marketing emails, non-essential cookies | Consent records with timestamps |
| Contract | Necessary for contract performance | Order fulfillment, account creation | Contract terms referencing data use |
| Legal obligation | Required by law | Tax records, employment law compliance | Legal citation for each obligation |
| Vital interests | Protecting someone's life | Emergency medical situations | Justification memo |
| Public task | Official authority or public interest | Government services | Authority documentation |
| Legitimate interest | Reasonable business purpose | Fraud prevention, analytics | Legitimate Interest Assessment (LIA) |

#### Data Subject Rights (Articles 15-22)

| Right | Article | Response Deadline | Extensions | Fee Allowed |
|---|---|---|---|---|
| Access | Art. 15 | 30 days | +60 days (complex) | Free (first copy) |
| Rectification | Art. 16 | 30 days | +60 days (complex) | Free |
| Erasure | Art. 17 | 30 days | +60 days (complex) | Free |
| Restrict processing | Art. 18 | 30 days | +60 days (complex) | Free |
| Data portability | Art. 20 | 30 days | +60 days (complex) | Free |
| Object | Art. 21 | 30 days | N/A | Free |
| Automated decisions | Art. 22 | 30 days | +60 days (complex) | Free |

#### DPIA Triggers (Article 35)

A Data Protection Impact Assessment is required when processing is likely to result in high risk, including:

- Systematic and extensive profiling with significant effects
- Large-scale processing of special category data
- Systematic monitoring of publicly accessible areas
- Innovative technology use (AI, biometrics, IoT)
- Data matching or combining from multiple sources
- Processing of vulnerable individuals' data (children, employees)
- Large-scale data transfers outside the EU

### CCPA/CPRA (California Consumer Privacy Act / California Privacy Rights Act)

#### Consumer Rights Under CCPA/CPRA

| Right | CCPA | CPRA Enhancement |
|---|---|---|
| Right to know | Categories and specific pieces of PI | Extended to include data sharing |
| Right to delete | PI collected from consumer | Expanded scope to include inferences |
| Right to opt-out of sale | Sale of PI | Extended to "sharing" for cross-context behavioral advertising |
| Right to non-discrimination | Cannot discriminate for exercising rights | Financial incentive requirements tightened |
| Right to correct | N/A | New right to correct inaccurate PI |
| Right to limit sensitive PI use | N/A | New right to limit use of sensitive PI |

#### CCPA Personal Information Categories

1. Identifiers (name, address, SSN, email, IP address)
2. Customer records (financial info, medical info, insurance info)
3. Protected classifications (race, religion, sexual orientation)
4. Commercial information (purchase history, consumption tendencies)
5. Biometric information
6. Internet activity (browsing, search history)
7. Geolocation data
8. Sensory data (audio, visual, thermal)
9. Professional or employment information
10. Non-public education information
11. Inferences drawn from the above

### PIPEDA (Personal Information Protection and Electronic Documents Act)

#### 10 Fair Information Principles

| Principle | Requirement | Compliance Tip |
|---|---|---|
| Accountability | Designate a privacy officer | Name and contact in policy |
| Identifying purposes | State why data is collected | Purpose statement per collection point |
| Consent | Obtain meaningful consent | Layered consent approach |
| Limiting collection | Collect only what is needed | Data minimization audit |
| Limiting use, disclosure, retention | Use only for stated purposes | Retention schedule per data type |
| Accuracy | Keep information accurate | Correction mechanism available |
| Safeguards | Protect with appropriate security | Security measures section |
| Openness | Make policies publicly available | Published privacy policy |
| Individual access | Allow access to personal info | Access request procedure |
| Challenging compliance | Provide complaint mechanism | Contact info for complaints |

### LGPD (Lei Geral de Protecao de Dados - Brazil)

#### Legal Bases for Processing

1. Consent of the data subject
2. Legal or regulatory obligation
3. Execution of public policies
4. Research studies (anonymized when possible)
5. Contract execution
6. Exercise of rights in judicial proceedings
7. Protection of life or physical safety
8. Health protection
9. Legitimate interest
10. Credit protection

### International Transfer Mechanisms

| Mechanism | Description | Complexity | When to Use |
|---|---|---|---|
| Adequacy decision | EU Commission deems country adequate | Low | Transfers to adequate countries |
| Standard Contractual Clauses (SCCs) | Pre-approved contract terms | Medium | Most US/non-adequate transfers |
| Binding Corporate Rules (BCRs) | Intra-group transfer framework | High | Large multinationals |
| Derogations | Explicit consent, contract necessity | Medium | One-off transfers |
| Certification mechanisms | Approved certification schemes | Medium | When available for sector |

## Cookie Consent Implementation Guide

### Consent Management Platform (CMP) Requirements

| Requirement | GDPR | ePrivacy | CCPA |
|---|---|---|---|
| Prior consent for non-essential | Yes | Yes | No (opt-out model) |
| Granular category choices | Yes | Yes | Not required |
| Easy withdrawal of consent | Yes | Yes | Opt-out link required |
| Record of consent | Yes | Recommended | Recommended |
| Renewed consent periodically | Every 12 months recommended | Varies by member state | Annual policy update |

### Cookie Audit Procedure

1. **Crawl the site**: Use automated scanner to identify all cookies and tracking technologies
2. **Classify each cookie**: Map to categories (necessary, analytics, functional, advertising)
3. **Document details**: Name, provider, purpose, duration, type (first/third party)
4. **Assess legal basis**: Determine if consent is required for each cookie
5. **Implement controls**: Configure CMP to block non-essential cookies until consent
6. **Test consent flows**: Verify cookies are only set after appropriate consent
7. **Document in policy**: List all cookies in the cookie policy with accurate details

## Data Processing Agreement (DPA) Essentials

### Required Clauses (GDPR Article 28)

- Subject matter and duration of processing
- Nature and purpose of processing
- Type of personal data and categories of data subjects
- Obligations and rights of the controller
- Processing only on documented instructions
- Confidentiality obligations for personnel
- Security measures (Article 32)
- Sub-processor management (prior authorization, flow-down obligations)
- Assistance with data subject rights
- Deletion or return of data after service ends
- Audit and inspection rights
- Notification of personal data breaches

## Privacy by Design Principles

| Principle | Implementation |
|---|---|
| Proactive not reactive | Build privacy into project planning from day one |
| Privacy as default | Strictest privacy settings out of the box |
| Privacy embedded in design | Privacy is integral, not an add-on |
| Full functionality | No false trade-offs between privacy and features |
| End-to-end security | Secure lifecycle management of all data |
| Visibility and transparency | Keep practices open and verifiable |
| Respect for user privacy | Keep the user's interests paramount |

## Penalty Reference

| Regulation | Maximum Fine | Notable Enforcement Examples |
|---|---|---|
| GDPR (lower tier) | 10M EUR or 2% global revenue | Cookie consent violations |
| GDPR (upper tier) | 20M EUR or 4% global revenue | Meta: 1.2B EUR (2023), Amazon: 746M EUR (2021) |
| CCPA | $2,500 per unintentional / $7,500 per intentional violation | Sephora: $1.2M (2022) |
| HIPAA | $100 - $50,000 per violation, $1.5M annual cap per category | Anthem: $16M (2018) |
| PIPEDA | $100,000 CAD per violation | Limited enforcement history |
| LGPD | 2% of revenue, capped at 50M BRL per violation | Enforcement began 2023 |
