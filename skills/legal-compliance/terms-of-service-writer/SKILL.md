---
name: terms-of-service-writer
description: Draft terms of service documents for websites, apps, and platforms. Use when user mentions "terms of service," "terms and conditions," "user agreement," "ToS," "acceptable use policy," "service agreement."
metadata:
  version: 1.0.0
  category: legal-compliance
---

# Terms of Service Writer

Draft clear, enforceable terms of service documents tailored to your business model, jurisdiction, and platform type.

## Purpose

This skill generates terms of service that protect the business while remaining fair and transparent to users. It covers SaaS, e-commerce, marketplace, mobile app, and API contexts with jurisdiction-appropriate clauses.

## Quick Reference

### ToS Types by Business Model

| Business Model | Key Focus Areas                          | Special Clauses Needed              |
|----------------|------------------------------------------|-------------------------------------|
| SaaS           | Subscription, SLA, data ownership        | Uptime guarantees, API limits       |
| E-commerce     | Returns, shipping, payment terms         | Product liability, refund policy    |
| Marketplace    | Buyer/seller rules, commissions, escrow  | Dispute resolution between parties  |
| Mobile App     | In-app purchases, app store compliance   | Push notification consent           |
| API/Platform   | Rate limits, usage quotas, redistribution| Developer obligations, versioning   |
| Freemium       | Feature tiers, upgrade/downgrade rules   | Free tier limitations               |
| Content/Media  | Licensing, UGC ownership, takedowns      | DMCA process, content standards     |

### Key Clause Categories

| Clause Category     | Risk Level | Required | Notes                               |
|---------------------|------------|----------|-------------------------------------|
| Acceptance of Terms | Low        | Yes      | Click-wrap or browse-wrap           |
| User Eligibility    | Low        | Yes      | Age requirements, jurisdiction      |
| Account Terms       | Medium     | Yes      | Credentials, security, termination  |
| Acceptable Use      | High       | Yes      | Prohibited conduct, enforcement     |
| Intellectual Property| High      | Yes      | Ownership, licenses granted         |
| Limitation of Liability| Critical| Yes      | Caps, exclusions, disclaimers       |
| Dispute Resolution  | Critical   | Yes      | Arbitration, jurisdiction, class action|
| Termination         | Medium     | Yes      | For cause, for convenience, effects |
| Modifications       | Medium     | Yes      | Notice period, material changes     |
| Indemnification     | High       | Recommended| User obligations to defend         |
| Governing Law       | Medium     | Yes      | Choice of law, forum selection      |

## ToS Structure Template

```
TERMS OF SERVICE

Effective Date: [DATE]
Last Updated: [DATE]

1. ACCEPTANCE OF TERMS
   - Agreement formation (click-wrap vs. browse-wrap)
   - Binding nature of the agreement
   - Capacity to enter agreement

2. DEFINITIONS
   - "Service" - what is provided
   - "User," "Customer," "You"
   - "Content" - user-generated and platform content
   - "Account" - registration details

3. ELIGIBILITY
   - Minimum age (13 COPPA / 16 GDPR / 18 contracts)
   - Geographic restrictions
   - Entity representations

4. ACCOUNT REGISTRATION
   - Accurate information requirement
   - Account security responsibilities
   - One account per person policy
   - Account sharing restrictions

5. THE SERVICE
   - Description of what is provided
   - Service availability and modifications
   - Beta features and experimental functionality
   - Third-party integrations

6. FEES AND PAYMENT
   - Pricing and billing cycles
   - Payment methods accepted
   - Taxes and fees
   - Refund policy
   - Price change notification
   - Failed payment handling

7. ACCEPTABLE USE POLICY
   - Permitted uses
   - Prohibited activities list
   - Rate limits and fair usage
   - Enforcement actions

8. INTELLECTUAL PROPERTY
   - Platform IP ownership
   - User content license grant
   - Feedback and suggestions
   - Trademark usage

9. USER CONTENT
   - Content ownership
   - License granted to platform
   - Content moderation rights
   - DMCA/takedown procedures
   - Content backup responsibilities

10. PRIVACY
    - Reference to Privacy Policy
    - Data processing summary

11. THIRD-PARTY SERVICES
    - Links and integrations
    - No endorsement disclaimer

12. DISCLAIMERS
    - "As is" and "as available"
    - No warranty of uninterrupted service
    - Accuracy disclaimers

13. LIMITATION OF LIABILITY
    - Cap on damages
    - Excluded damages (consequential, incidental)
    - Essential purpose preservation

14. INDEMNIFICATION
    - User's obligation to defend
    - Scope of indemnification
    - Control of defense

15. DISPUTE RESOLUTION
    - Informal resolution first
    - Arbitration clause (if applicable)
    - Class action waiver
    - Small claims exception
    - Governing law
    - Venue/jurisdiction

16. TERMINATION
    - Termination by user
    - Termination by platform (for cause)
    - Termination by platform (for convenience)
    - Effect of termination
    - Surviving provisions
    - Data export period

17. MODIFICATIONS TO TERMS
    - Right to modify
    - Notice period (30 days recommended)
    - Material vs. non-material changes
    - Continued use as acceptance

18. GENERAL PROVISIONS
    - Entire agreement
    - Severability
    - Waiver
    - Assignment
    - Force majeure
    - Notices

19. CONTACT INFORMATION
```

## SaaS-Specific Addendum

```
SAAS TERMS ADDENDUM

A. SERVICE LEVEL AGREEMENT (SLA)
   - Uptime commitment: [99.9%]
   - Measurement period: monthly
   - Excluded downtime: maintenance windows, force majeure
   - Service credits calculation:
     | Uptime %      | Credit           |
     |---------------|------------------|
     | 99.0 - 99.9%  | 10% monthly fee  |
     | 95.0 - 99.0%  | 25% monthly fee  |
     | Below 95.0%   | 50% monthly fee  |
   - Credit request procedure
   - Maximum credit cap: one month's fees

B. DATA OWNERSHIP AND PORTABILITY
   - Customer retains all rights to their data
   - Platform license limited to service provision
   - Data export in standard formats (CSV, JSON, API)
   - Post-termination data retention: 30 days
   - Data deletion upon request

C. SUBSCRIPTION TERMS
   - Billing frequency (monthly/annual)
   - Auto-renewal and cancellation
   - Proration on plan changes
   - Volume licensing terms

D. API TERMS
   - Rate limits by plan tier
   - API versioning and deprecation policy
   - Redistribution restrictions
   - Uptime for API endpoints
```

## E-Commerce-Specific Addendum

```
E-COMMERCE TERMS ADDENDUM

A. PRODUCT INFORMATION
   - Accuracy of descriptions and images
   - Pricing errors and corrections
   - Product availability and backorders

B. ORDERS AND FULFILLMENT
   - Order acceptance and confirmation
   - Processing times
   - Shipping terms and carriers
   - Risk of loss transfer point
   - International shipping and customs

C. RETURNS AND REFUNDS
   - Return window: [30] days
   - Condition requirements
   - Return shipping responsibility
   - Refund method and timeline
   - Non-returnable items list
   - Defective product handling

D. WARRANTIES
   - Manufacturer warranty pass-through
   - Platform warranty (if any)
   - Warranty claim procedure
```

## Jurisdiction Considerations

| Jurisdiction | Key Requirements                                        |
|--------------|---------------------------------------------------------|
| USA          | COPPA (children), state consumer protection laws, CAN-SPAM |
| EU/EEA       | Consumer Rights Directive (14-day withdrawal), GDPR     |
| UK           | Consumer Rights Act 2015, UK GDPR                       |
| California   | Auto-renewal law (clear disclosure, easy cancel)         |
| Australia    | Australian Consumer Law, no unfair contract terms        |
| Canada       | Consumer protection varies by province, CASL for email   |

## Update Notification Requirements

| Change Type     | Minimum Notice | Notification Method            | User Action Required |
|-----------------|----------------|-------------------------------|----------------------|
| Material change | 30 days        | Email + in-app banner          | Affirmative consent  |
| Minor change    | 14 days        | Email or in-app notification   | Continued use = acceptance |
| Security fix    | Immediate      | Email + changelog              | None                 |
| Price increase  | 30 days        | Email (direct)                 | Opt-in to new pricing|

## Workflow

1. **Identify business model**: SaaS, e-commerce, marketplace, API, mobile app
2. **Determine jurisdictions**: Where the business operates and where users are located
3. **Select applicable addenda**: SaaS terms, e-commerce terms, API terms
4. **Customize clauses**: Adjust limitation of liability caps, dispute resolution, governing law
5. **Plain language review**: Ensure readability without sacrificing enforceability
6. **Compliance cross-check**: Validate against jurisdiction-specific requirements
7. **Format and deliver**: Produce final document with table of contents and effective date

## Scripts & Tools

**Generate ToS skeleton**:
```bash
scripts/generate-tos.sh --model saas --jurisdiction us,eu --output terms.md
```

**Clause library lookup**:
```bash
scripts/clause-library.sh --category "limitation-of-liability" --jurisdiction california
```

**Readability score**:
```bash
scripts/readability-check.sh --input terms.md --target-grade 8
```

## Best Practices

- Use click-wrap (checkbox + click) rather than browse-wrap for stronger enforceability.
- Keep language at an 8th-grade reading level where possible.
- Provide a human-readable summary alongside the full legal text.
- Highlight material changes in bold or with a change summary at the top.
- Include a version history table at the end of the document.
- Review terms annually and after any significant product or business model changes.
- Ensure arbitration clauses comply with the jurisdiction's requirements and include opt-out windows.
- Never hide important terms in dense paragraphs; use headers and numbered lists.
- Consider offering a "key terms" sidebar for the most important clauses.
