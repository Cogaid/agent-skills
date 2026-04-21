---
name: incident-report-writer
description: Write incident reports for security breaches, compliance violations, and operational failures. Use when user mentions "incident report," "breach report," "security incident," "post-mortem," "root cause analysis," "compliance violation report."
metadata:
  version: 1.0.0
  category: legal-compliance
---

# Incident Report Writer

Produce structured incident reports covering timeline, impact, root cause, remediation, and lessons learned for security, compliance, and operational incidents.

## Purpose

This skill generates thorough incident reports that satisfy regulatory notification requirements, support internal learning, and document the organization's response. It adapts format and content based on incident type and applicable regulations.

## Quick Reference

### Incident Classification Matrix

| Category           | Examples                                    | Typical Severity | Regulatory Trigger |
|--------------------|---------------------------------------------|------------------|--------------------|
| Data Breach        | Unauthorized access to personal data        | P0-P1            | GDPR, CCPA, HIPAA  |
| System Outage      | Service unavailability beyond SLA           | P1-P2            | SLA, SOC 2         |
| Unauthorized Access| Privilege escalation, credential compromise | P0-P1            | SOC 2, PCI-DSS     |
| Malware/Ransomware | Ransomware infection, trojan deployment     | P0               | All frameworks      |
| Insider Threat     | Malicious employee action, data theft       | P0-P1            | GDPR, HIPAA         |
| Phishing           | Successful phishing leading to compromise   | P1-P2            | SOC 2               |
| Configuration Error| Misconfigured access, exposed storage       | P1-P2            | PCI-DSS, SOC 2      |
| Compliance Violation| Policy breach, regulatory non-compliance   | P2-P3            | Framework-specific   |
| Physical Security  | Unauthorized facility access, theft         | P1-P2            | HIPAA, PCI-DSS       |
| Third-Party Breach | Vendor or partner data compromise           | P1-P2            | All frameworks       |

### Severity Levels

| Level | Name     | Definition                                          | Response Time | Commander Level   |
|-------|----------|-----------------------------------------------------|---------------|-------------------|
| P0    | Critical | Active breach, data exfiltration, full outage       | 15 minutes    | VP/C-Level        |
| P1    | High     | Partial breach, significant data exposure, degraded  | 1 hour        | Director          |
| P2    | Medium   | Contained incident, limited exposure, minor outage   | 4 hours       | Manager           |
| P3    | Low      | Near-miss, policy violation, no data exposure        | 24 hours      | Team Lead         |
| P4    | Info     | Suspicious activity, investigation only              | 48 hours      | Security Analyst  |

## Incident Report Template

```
INCIDENT REPORT

Report ID: [INC-YYYY-MM-NNN]
Classification: [Data Breach / Outage / Unauthorized Access / ...]
Severity: [P0 / P1 / P2 / P3 / P4]
Status: [Active / Contained / Resolved / Closed]

Report Date: [DATE]
Incident Date: [DATE]
Detection Date: [DATE]
Resolution Date: [DATE or "Ongoing"]

Incident Commander: [NAME, TITLE]
Report Author: [NAME, TITLE]
Distribution: [List of recipients]

---

1. EXECUTIVE SUMMARY
   [2-3 sentence overview: what happened, what was the impact,
   and what is the current status]

2. TIMELINE OF EVENTS

   | Timestamp (UTC)      | Event                              | Source         |
   |----------------------|------------------------------------|----------------|
   | YYYY-MM-DD HH:MM     | [Initial compromise/trigger]       | [Log/Alert]    |
   | YYYY-MM-DD HH:MM     | [Detection/alert fired]            | [Monitoring]   |
   | YYYY-MM-DD HH:MM     | [Incident declared, team assembled]| [Comms]        |
   | YYYY-MM-DD HH:MM     | [Containment action taken]         | [Action log]   |
   | YYYY-MM-DD HH:MM     | [Root cause identified]            | [Investigation]|
   | YYYY-MM-DD HH:MM     | [Remediation completed]            | [Action log]   |
   | YYYY-MM-DD HH:MM     | [All-clear / incident closed]      | [Commander]    |

3. IMPACT ASSESSMENT

   Data Impact:
   - Records affected: [NUMBER]
   - Data types exposed: [PII, PHI, financial, credentials]
   - Data subjects affected: [customers, employees, partners]
   - Geographic scope: [countries/regions]

   Business Impact:
   - Downtime: [DURATION]
   - Revenue impact: [$AMOUNT or estimate]
   - Customer impact: [description]
   - Reputational impact: [assessment]

   Regulatory Impact:
   - Notification required: [Yes/No, which regulations]
   - Notification deadline: [DATE]
   - Notification status: [Pending / Completed / Not Required]

4. ROOT CAUSE ANALYSIS

   Immediate Cause:
   [What directly caused the incident]

   Contributing Factors:
   - [Factor 1: e.g., unpatched vulnerability]
   - [Factor 2: e.g., missing monitoring]
   - [Factor 3: e.g., excessive permissions]

   Root Cause:
   [Underlying systemic issue]

   5 Whys Analysis:
   1. Why did [incident] occur? Because [reason 1]
   2. Why did [reason 1] occur? Because [reason 2]
   3. Why did [reason 2] occur? Because [reason 3]
   4. Why did [reason 3] occur? Because [reason 4]
   5. Why did [reason 4] occur? Because [root cause]

5. CONTAINMENT AND RESPONSE

   Immediate Actions Taken:
   - [Action 1 with timestamp and owner]
   - [Action 2 with timestamp and owner]
   - [Action 3 with timestamp and owner]

   Short-Term Remediation:
   - [Fix 1 with owner and completion date]
   - [Fix 2 with owner and completion date]

6. LONG-TERM REMEDIATION PLAN

   | Action Item              | Owner    | Priority | Deadline   | Status     |
   |--------------------------|----------|----------|------------|------------|
   | [Remediation action 1]   | [Name]   | P1       | [Date]     | [Status]   |
   | [Remediation action 2]   | [Name]   | P2       | [Date]     | [Status]   |
   | [Remediation action 3]   | [Name]   | P2       | [Date]     | [Status]   |

7. LESSONS LEARNED
   [See Lessons Learned Template below]

8. APPENDICES
   A. Evidence inventory
   B. Communication log
   C. External notifications sent
   D. Technical indicators of compromise (IOCs)
```

## Notification Requirements by Regulation

| Regulation | Trigger                      | Notification To         | Deadline               | Content Required           |
|------------|------------------------------|-------------------------|------------------------|----------------------------|
| GDPR       | Risk to rights and freedoms  | Supervisory Authority   | 72 hours               | Nature, categories, DPO contact, consequences, measures |
| GDPR       | High risk to individuals     | Affected Individuals    | Without undue delay    | Plain language, DPO contact, likely consequences |
| CCPA       | Unauthorized access to PII   | Affected Residents      | Most expedient time    | Type of info, entity info, steps taken |
| HIPAA      | Unsecured PHI breach         | HHS, individuals        | 60 days (individuals), 60 days or annual (HHS) | Description, types, steps to protect, investigation, contact |
| PCI-DSS    | Cardholder data compromise   | Card brands, acquirer   | Immediately            | Scope, compromised accounts, forensic report |
| SEC        | Material cybersecurity incident | SEC (Form 8-K)       | 4 business days        | Nature, scope, timing, material impact |
| State Laws | Varies by state              | State AG, individuals   | 30-90 days (varies)    | Varies by state            |

## Lessons Learned Template

```
LESSONS LEARNED

Incident: [INC-YYYY-MM-NNN]
Facilitated by: [NAME]
Date of Review: [DATE]
Participants: [LIST]

WHAT WENT WELL
1. [Positive observation with supporting evidence]
2. [Positive observation with supporting evidence]
3. [Positive observation with supporting evidence]

WHAT COULD BE IMPROVED
1. [Issue identified] -> [Specific improvement action]
2. [Issue identified] -> [Specific improvement action]
3. [Issue identified] -> [Specific improvement action]

DETECTION
- How was the incident detected? [Automated alert / Manual / External report]
- Time from occurrence to detection: [DURATION]
- Could detection have been faster? [Yes/No, how]

RESPONSE
- Time from detection to response: [DURATION]
- Were runbooks followed? [Yes / No / Partially]
- Were the right people available? [Yes / No]
- Communication effectiveness: [Rating 1-5]

PROCESS GAPS
- [ ] Missing runbook for this scenario
- [ ] Insufficient monitoring or alerting
- [ ] Unclear escalation path
- [ ] Inadequate access controls
- [ ] Missing or outdated documentation
- [ ] Training gaps identified

ACTION ITEMS FROM REVIEW
| Action                        | Owner    | Deadline   | Tracking ID |
|-------------------------------|----------|------------|-------------|
| [Improvement action 1]       | [Name]   | [Date]     | [JIRA-XXX]  |
| [Improvement action 2]       | [Name]   | [Date]     | [JIRA-XXX]  |
| [Improvement action 3]       | [Name]   | [Date]     | [JIRA-XXX]  |
```

## Post-Incident Review Format

```
POST-INCIDENT REVIEW MEETING

Duration: 60-90 minutes
Cadence: Within 5 business days of resolution

AGENDA
1. [5 min]  Opening: no-blame culture reminder
2. [15 min] Timeline walkthrough (Incident Commander)
3. [15 min] Technical deep-dive (Engineering Lead)
4. [10 min] Impact assessment (Business/Legal)
5. [20 min] Lessons learned discussion (All)
6. [10 min] Action items and owners (Facilitator)
7. [5 min]  Closing: next steps and follow-up date

GROUND RULES
- Focus on systems and processes, not individuals
- Assume good intent from all participants
- Be specific and evidence-based
- Commit to actionable improvements
- Follow up on all action items within agreed timelines

OUTPUT
- Updated incident report
- Completed lessons learned document
- Action items in project tracker
- Process/runbook updates scheduled
```

## Workflow

1. **Classify the incident**: Use the classification matrix to determine category and severity
2. **Assign incident commander**: Based on severity level
3. **Gather facts**: Collect timeline events, evidence, and impact data
4. **Draft initial report**: Use the incident report template for the first version
5. **Identify root cause**: Apply 5 Whys or fishbone analysis
6. **Assess notification requirements**: Check applicable regulations against triggers
7. **Draft notifications**: Prepare regulatory and individual notifications as needed
8. **Remediation planning**: Create short-term and long-term remediation plans
9. **Conduct post-incident review**: Facilitate the lessons learned session
10. **Finalize report**: Update with complete root cause and remediation status

## Scripts & Tools

**Generate incident report skeleton**:
```bash
scripts/incident-report.sh --severity p1 --category "data-breach" --output report.md
```

**Notification deadline calculator**:
```bash
scripts/notification-calc.sh --regulation gdpr --discovery-date "2025-01-15T14:30:00Z"
```

**Timeline builder**:
```bash
scripts/timeline-builder.sh --logs ./evidence/ --output timeline.csv
```

**Lessons learned tracker**:
```bash
scripts/lessons-tracker.sh --incident INC-2025-01-001 --status-update
```

## Best Practices

- Start the timeline clock at the moment of discovery, not occurrence. Document both.
- Use UTC timestamps throughout the report for consistency across time zones.
- Maintain a no-blame culture in post-incident reviews to encourage honest participation.
- Preserve all evidence before making changes to affected systems.
- Document every communication with external parties (regulators, customers, media).
- Assign a single incident commander for each incident regardless of severity.
- Track all remediation items in a project management tool, not just the report.
- Review and update incident response runbooks after every P0 and P1 incident.
- Conduct tabletop exercises quarterly to test the incident response process.
- Keep a running list of indicators of compromise (IOCs) for threat intelligence sharing.
