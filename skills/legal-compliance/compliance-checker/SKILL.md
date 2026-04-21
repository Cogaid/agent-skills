---
name: compliance-checker
description: Check content and systems against regulatory requirements. Use when user mentions "compliance check," "audit," "regulatory review," "GDPR audit," "HIPAA compliance," "SOC2 readiness," "PCI-DSS check," "compliance gap analysis."
metadata:
  version: 1.0.0
  category: legal-compliance
---

# Compliance Checker

Evaluate content, systems, and processes against major regulatory frameworks and produce actionable compliance reports.

## Purpose

This skill assesses organizational practices against GDPR, CCPA, HIPAA, SOC 2, PCI-DSS, and other frameworks. It identifies gaps, scores compliance maturity, and generates remediation plans with prioritized action items.

## Quick Reference

### Compliance Frameworks Overview

| Framework | Domain            | Scope                          | Audit Type       | Renewal Cycle |
|-----------|-------------------|--------------------------------|------------------|---------------|
| GDPR      | Data Protection   | EU personal data processing    | Self + DPA       | Ongoing       |
| CCPA/CPRA | Data Protection   | California consumer data       | Self-assessment  | Annual        |
| HIPAA     | Healthcare        | Protected health information   | Self + OCR       | Annual        |
| SOC 2     | Security          | Service organization controls  | Independent audit| Annual        |
| PCI-DSS   | Payment           | Cardholder data environments   | QSA / SAQ        | Annual        |
| ISO 27001 | Information Security| ISMS across the organization  | Certification body| 3-year cycle  |
| SOX       | Financial         | Public company financial controls| Independent audit| Annual       |
| FERPA     | Education         | Student education records      | Self-assessment  | Ongoing       |
| FedRAMP   | Government Cloud  | Cloud services for US federal  | 3PAO assessment  | Annual + continuous |
| NIST 800-53| Security         | Federal information systems    | Self / assessor  | Ongoing       |

### Compliance Maturity Levels

| Level | Name          | Description                                     | Score Range |
|-------|---------------|-------------------------------------------------|-------------|
| 1     | Initial       | Ad hoc, no formal processes                     | 0-20%       |
| 2     | Developing    | Some processes defined but inconsistent          | 21-40%      |
| 3     | Defined       | Standardized processes, documented policies      | 41-60%      |
| 4     | Managed       | Measured and controlled, metrics tracked         | 61-80%      |
| 5     | Optimized     | Continuous improvement, proactive compliance     | 81-100%     |

## Violation Severity Matrix

| Severity | Label    | Description                                    | Response Time | Escalation      |
|----------|----------|------------------------------------------------|---------------|------------------|
| P0       | Critical | Active data breach, regulatory deadline missed | Immediate     | Executive + Legal|
| P1       | High     | Missing required controls, audit finding       | 24 hours      | Compliance Lead  |
| P2       | Medium   | Policy gaps, incomplete documentation          | 1 week        | Team Lead        |
| P3       | Low      | Minor procedural gaps, best practice deviation | 1 month       | Assigned owner   |
| P4       | Info     | Optimization opportunities, recommendations   | Next quarter  | Backlog          |

## Audit Checklist by Framework

### GDPR Audit Checklist

```
DATA MAPPING AND INVENTORY
- [ ] Complete record of processing activities (Article 30)
- [ ] Data flow diagrams for all personal data
- [ ] Third-party processor inventory with DPAs
- [ ] Cross-border transfer mechanisms documented
- [ ] Retention schedules defined per data category

LAWFUL BASIS
- [ ] Lawful basis identified for each processing activity
- [ ] Consent records maintained with timestamps
- [ ] Legitimate interest assessments documented
- [ ] Special category data processing justified

DATA SUBJECT RIGHTS
- [ ] Access request process (30-day response)
- [ ] Rectification process operational
- [ ] Erasure process with cascade to processors
- [ ] Portability in machine-readable format
- [ ] Objection handling procedure
- [ ] Automated decision-making safeguards

SECURITY (Article 32)
- [ ] Encryption at rest and in transit
- [ ] Access controls and authentication
- [ ] Regular security testing
- [ ] Incident response plan tested
- [ ] Breach notification within 72 hours

GOVERNANCE
- [ ] DPO appointed (if required)
- [ ] Privacy impact assessments for high-risk processing
- [ ] Staff training records maintained
- [ ] Policy review schedule documented
```

### HIPAA Audit Checklist

```
ADMINISTRATIVE SAFEGUARDS
- [ ] Security officer designated
- [ ] Risk analysis completed and documented
- [ ] Workforce training on PHI handling
- [ ] Sanction policy for violations
- [ ] Contingency plan (backup, disaster recovery, emergency mode)
- [ ] Business Associate Agreements with all vendors

PHYSICAL SAFEGUARDS
- [ ] Facility access controls
- [ ] Workstation use policies
- [ ] Device and media controls
- [ ] Disposal procedures for PHI media

TECHNICAL SAFEGUARDS
- [ ] Unique user identification
- [ ] Emergency access procedures
- [ ] Automatic logoff configured
- [ ] Encryption of ePHI
- [ ] Audit controls and logging
- [ ] Integrity controls for ePHI
- [ ] Transmission security (TLS/VPN)

BREACH NOTIFICATION
- [ ] Breach risk assessment procedure
- [ ] Individual notification within 60 days
- [ ] HHS notification (>500: within 60 days, <500: annual)
- [ ] Media notification for >500 in a state
```

### SOC 2 Trust Service Criteria

```
SECURITY (Common Criteria)
- [ ] CC1: Control environment
- [ ] CC2: Communication and information
- [ ] CC3: Risk assessment
- [ ] CC4: Monitoring activities
- [ ] CC5: Control activities
- [ ] CC6: Logical and physical access
- [ ] CC7: System operations
- [ ] CC8: Change management
- [ ] CC9: Risk mitigation

AVAILABILITY
- [ ] A1: System availability commitments and SLAs
- [ ] Disaster recovery plan tested annually
- [ ] Backup procedures verified

PROCESSING INTEGRITY
- [ ] PI1: Processing completeness and accuracy
- [ ] Input validation controls
- [ ] Output reconciliation

CONFIDENTIALITY
- [ ] C1: Confidential information identification
- [ ] Encryption and access restrictions
- [ ] Disposal procedures

PRIVACY
- [ ] P1-P8: Privacy criteria (if in scope)
```

## Remediation Templates

### Remediation Plan Template

```
REMEDIATION PLAN

Finding ID: [FINDING-001]
Framework: [GDPR / HIPAA / SOC2 / PCI-DSS]
Severity: [P0 / P1 / P2 / P3]
Control Reference: [Article 32 / CC6.1 / Req 3.4]

FINDING
Description: [What was identified]
Evidence: [How it was discovered]
Impact: [Business and compliance impact]

ROOT CAUSE
[Why the gap exists]

REMEDIATION STEPS
1. [Action item with owner and deadline]
2. [Action item with owner and deadline]
3. [Action item with owner and deadline]

RESOURCES REQUIRED
- [People, budget, tools]

VERIFICATION
- Test method: [How to verify remediation]
- Verification date: [When to verify]
- Verified by: [Who will verify]

STATUS TRACKING
| Date       | Status      | Notes              |
|------------|-------------|---------------------|
| [DATE]     | Identified  | Initial finding     |
| [DATE]     | In Progress | [Update]            |
| [DATE]     | Resolved    | [Verification note] |
```

## Compliance Report Format

```
COMPLIANCE ASSESSMENT REPORT

Report ID: [RPT-YYYY-MM-NNN]
Assessment Date: [DATE]
Framework: [FRAMEWORK]
Scope: [What was assessed]
Assessor: [Name / Team]

EXECUTIVE SUMMARY
- Overall maturity level: [1-5]
- Compliance score: [X%]
- Critical findings: [N]
- High findings: [N]
- Total findings: [N]

SCOPE AND METHODOLOGY
[Description of what was assessed and how]

FINDINGS SUMMARY
| ID         | Severity | Control     | Description          | Status     |
|------------|----------|-------------|----------------------|------------|
| FIND-001   | P1       | CC6.1       | [Brief description]  | Open       |
| FIND-002   | P2       | Art. 32     | [Brief description]  | Remediated |

DETAILED FINDINGS
[Full finding details with evidence and remediation plans]

RISK HEAT MAP
             Low Impact    Medium Impact    High Impact
High Likelihood    [N]          [N]             [N]
Med Likelihood     [N]          [N]             [N]
Low Likelihood     [N]          [N]             [N]

RECOMMENDATIONS
[Prioritized list of improvements]

APPENDIX
- Evidence inventory
- Interview log
- Document review list
```

## Regulatory Update Tracking

| Regulation | Last Major Update | Next Expected Change     | Monitoring Source           |
|------------|-------------------|--------------------------|-----------------------------|
| GDPR       | 2018 (enacted)    | ePrivacy Regulation TBD  | EDPB guidelines             |
| CCPA/CPRA  | Jan 2023 (CPRA)   | Ongoing rulemaking       | CA Attorney General site    |
| HIPAA      | 2013 (Omnibus)    | HIPAA Security Rule 2025 | HHS.gov                     |
| PCI-DSS    | Mar 2024 (v4.0.1) | Requirements phase-in    | PCI SSC website             |
| SOC 2      | 2022 (point of focus)| Annual updates          | AICPA Trust Services        |
| ISO 27001  | Oct 2022 (revision)| Next revision ~2028     | ISO committee               |

## Workflow

1. **Scope definition**: Identify which frameworks apply and what systems are in scope
2. **Document collection**: Gather policies, procedures, configurations, and evidence
3. **Control mapping**: Map existing controls to framework requirements
4. **Gap assessment**: Identify missing or inadequate controls
5. **Severity classification**: Rate each finding using the severity matrix
6. **Remediation planning**: Create remediation plans for each finding
7. **Report generation**: Compile the compliance assessment report
8. **Executive briefing**: Prepare summary for leadership
9. **Tracking setup**: Configure ongoing monitoring and re-assessment dates

## Scripts & Tools

**Run compliance scan**:
```bash
scripts/compliance-scan.sh --framework gdpr --scope ./policies --output report.md
```

**Generate gap analysis**:
```bash
scripts/gap-analysis.sh --framework soc2 --evidence ./evidence --output gaps.csv
```

**Remediation tracker**:
```bash
scripts/remediation-tracker.sh --report ./findings.csv --status-update --notify
```

## Best Practices

- Maintain a single source of truth for all compliance documentation.
- Automate evidence collection where possible (screenshots, configs, logs).
- Schedule quarterly mini-assessments rather than relying solely on annual audits.
- Cross-map controls across frameworks to reduce duplicate effort.
- Train all team members on compliance basics, not just the compliance team.
- Document exceptions and compensating controls with clear justification.
- Keep remediation timelines realistic and track progress weekly for P0/P1 findings.
- Maintain an evergreen risk register that feeds into compliance assessments.
