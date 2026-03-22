# Ticket Triage Reference

## Contents
- Priority Definitions
- Categories
- Routing Rules
- Red Flag Keywords
- Customer Tier Modifiers

---

## Priority Definitions

### P1 - Critical

**Response time**: < 1 hour
**Escalation**: Immediate manager notification

**Criteria**:
- Service completely down for multiple users
- Security breach or data exposure suspected
- Revenue-impacting outage (checkout broken, payments failing)
- Legal/compliance deadlines at immediate risk
- Data loss occurring

**Example tickets**:
- "Our entire company cannot access the platform since 9am"
- "We found customer data exposed publicly"
- "Payment processing is failing for all transactions"

**Keywords**: `outage`, `down`, `breach`, `exposed`, `data loss`, `can't access anything`, `entire company`, `all users`

---

### P2 - High

**Response time**: < 4 hours
**Escalation**: Daily standup mention

**Criteria**:
- Feature broken for subset of users
- Significant workflow disruption with no workaround
- VIP/Enterprise customer issues (any severity)
- Degraded performance affecting productivity
- Integration failures blocking business processes

**Example tickets**:
- "The export feature returns an error for large datasets"
- "SSO login failing for our engineering team"
- "API returning 500 errors intermittently"

**Keywords**: `broken`, `error`, `failing`, `can't complete`, `blocking`, `urgent`, `enterprise`, `VIP`

---

### P3 - Normal

**Response time**: < 24 hours
**Escalation**: Weekly review if unresolved

**Criteria**:
- Single user issues with workarounds available
- Feature requests from active paying users
- Configuration and setup questions
- Non-blocking bugs
- "How do I" questions not in documentation

**Example tickets**:
- "How do I change the date format in reports?"
- "The mobile app crashes when I rotate my phone"
- "Would be great if you could add dark mode"

**Keywords**: `how do I`, `would be nice`, `sometimes`, `occasionally`, `one user`, `workaround`

---

### P4 - Low

**Response time**: < 72 hours
**Escalation**: None unless pattern emerges

**Criteria**:
- General questions answered in documentation
- Feature suggestions without business case
- Minor UI/UX issues
- Non-urgent feedback
- "Nice to have" improvements

**Example tickets**:
- "Can you make the button a different color?"
- "What's your roadmap for next year?"
- "The font looks different on Firefox"

**Keywords**: `suggestion`, `feedback`, `would be cool`, `minor`, `cosmetic`, `just wondering`

---

## Categories

### Technical Categories

| Category | Subcategories | Keywords |
|----------|---------------|----------|
| **Bug Report** | Crash, Logic Error, UI Bug, Data Issue | "doesn't work," "error," "broken," "crash," "unexpected," "wrong result" |
| **Performance** | Speed, Timeout, Memory, Load Time | "slow," "timeout," "lag," "hanging," "loading forever," "takes too long" |
| **Integration** | API, Webhook, Sync, OAuth, Third-party | "API," "webhook," "sync," "connection," "Salesforce," "Slack," "integration" |
| **Access/Auth** | Login, Password, SSO, Permissions, MFA | "can't login," "password," "locked out," "permissions," "SSO," "access denied" |
| **Infrastructure** | Uptime, SSL, DNS, Email Delivery | "down," "certificate," "email not arriving," "DNS," "server" |

### Non-Technical Categories

| Category | Subcategories | Keywords |
|----------|---------------|----------|
| **Billing** | Charges, Invoices, Refunds, Pricing | "charge," "invoice," "payment," "subscription," "refund," "pricing," "cost" |
| **Account** | Upgrade, Downgrade, Cancel, Transfer | "upgrade," "cancel," "transfer," "merge," "close account," "change plan" |
| **How-To** | Setup, Configuration, Usage, Features | "how do I," "where is," "can I," "tutorial," "help with," "set up" |
| **Feature Request** | New Feature, Enhancement, Improvement | "would be nice," "suggestion," "wish," "please add," "feature request" |
| **Feedback** | Praise, Complaint, General Comment | "love it," "hate it," "feedback," "comment," "thought you should know" |

---

## Routing Rules

| Route To | Criteria | SLA |
|----------|----------|-----|
| **Tier 1 Support** | Standard how-to, common issues, first contact, documentation questions | First response: 4h |
| **Tier 2 Support** | Complex technical issues, requires investigation, repeated T1 contact | First response: 2h |
| **Engineering** | Confirmed bugs, requires code changes, infrastructure issues | Acknowledgment: 1h |
| **Billing Team** | Payment issues, refund requests, invoice disputes, plan changes | First response: 4h |
| **Security Team** | Security concerns, data exposure, compliance questions | Immediate |
| **Success Manager** | Enterprise escalations, churn risk, expansion opportunity | Same business day |
| **Product Team** | Feature requests with business case, UX feedback patterns | Weekly review |

---

## Red Flag Keywords

### Immediate Escalation Required

**Legal/Compliance**:
```
lawyer, attorney, lawsuit, sue, legal action, breach of contract,
GDPR, HIPAA, CCPA, compliance violation, audit, regulatory, subpoena
```

**Security**:
```
breach, hacked, exposed, vulnerability, unauthorized access,
data leak, compromised, security incident
```

**Churn Risk**:
```
cancel, switching to, competitor, leaving, not renewing,
disappointed, frustrated, last straw, final warning
```

**Public Threat**:
```
Twitter, social media, review, public, tell everyone,
post about, blog, news, journalist
```

**VIP Indicators**:
```
CEO, CTO, VP, Director, enterprise, strategic account,
[Check against enterprise customer list]
```

---

## Customer Tier Modifiers

| Tier | Priority Adjustment | Routing Override |
|------|--------------------| ----------------|
| **Enterprise** | +1 priority level (P3→P2) | Always CC Success Manager |
| **Pro/Business** | Standard priority | Standard routing |
| **Free/Trial** | -1 priority level (P2→P3) | No escalation path |
| **Churned** | Case-by-case | Route to Success for win-back |

### Tier Identification

Check account metadata for:
- Plan name (Enterprise, Pro, Free)
- ARR/MRR value
- Account age
- Strategic account flag
- Success Manager assignment
