# Incident Report Template

**INCIDENT REPORT**

**Report ID:** [INC-YYYY-MM-NNN]
**Classification:** [Data Breach / System Outage / Unauthorized Access / Malware / Configuration Error / Compliance Violation]
**Severity:** [P0 / P1 / P2 / P3 / P4]
**Status:** [Active / Contained / Resolved / Closed]

**Report Date:** [DATE]
**Incident Date:** [DATE]
**Detection Date:** [DATE]
**Resolution Date:** [DATE or "Ongoing"]

**Incident Commander:** [NAME, TITLE]
**Report Author:** [NAME, TITLE]
**Distribution:** [List of recipients]

---

## 1. Executive Summary

[2-3 sentences: what happened, what was the impact, and what is the current status.]

---

## 2. Timeline of Events

| Timestamp (UTC) | Event | Source |
|---|---|---|
| YYYY-MM-DD HH:MM | [Initial compromise/trigger event] | [Log / Alert / Report] |
| YYYY-MM-DD HH:MM | [Detection / alert fired] | [Monitoring system] |
| YYYY-MM-DD HH:MM | [Incident declared, team assembled] | [Communication channel] |
| YYYY-MM-DD HH:MM | [First containment action taken] | [Action log] |
| YYYY-MM-DD HH:MM | [Root cause identified] | [Investigation] |
| YYYY-MM-DD HH:MM | [Remediation completed] | [Action log] |
| YYYY-MM-DD HH:MM | [All-clear / incident closed] | [Incident Commander] |

---

## 3. Impact Assessment

### Data Impact

- **Records affected:** [NUMBER]
- **Data types exposed:** [PII / PHI / Financial / Credentials / None]
- **Data subjects affected:** [Customers / Employees / Partners / None]
- **Geographic scope:** [Countries / Regions affected]

### Business Impact

- **Downtime:** [DURATION]
- **Revenue impact:** [$AMOUNT or estimate]
- **Customer impact:** [Description of how customers were affected]
- **Reputational impact:** [Assessment of reputational damage]

### Regulatory Impact

- **Notification required:** [Yes / No]
- **Applicable regulations:** [GDPR / CCPA / HIPAA / PCI-DSS / SEC / State laws]
- **Notification deadline:** [DATE]
- **Notification status:** [Pending / Completed / Not Required]

---

## 4. Root Cause Analysis

### Immediate Cause

[What directly caused the incident]

### Contributing Factors

1. [Factor 1: e.g., unpatched vulnerability CVE-XXXX-XXXXX]
2. [Factor 2: e.g., missing network segmentation]
3. [Factor 3: e.g., excessive permissions on service account]

### Root Cause

[Underlying systemic issue that allowed the incident to occur]

### 5 Whys Analysis

1. Why did [incident] occur? Because [reason 1].
2. Why did [reason 1] occur? Because [reason 2].
3. Why did [reason 2] occur? Because [reason 3].
4. Why did [reason 3] occur? Because [reason 4].
5. Why did [reason 4] occur? Because [ROOT CAUSE].

---

## 5. Containment and Response

### Immediate Actions Taken

| # | Action | Timestamp | Owner |
|---|---|---|---|
| 1 | [Action description] | [UTC time] | [Name] |
| 2 | [Action description] | [UTC time] | [Name] |
| 3 | [Action description] | [UTC time] | [Name] |

### Short-Term Remediation

| # | Fix | Owner | Completion Date | Status |
|---|---|---|---|---|
| 1 | [Description] | [Name] | [Date] | [Complete/In Progress] |
| 2 | [Description] | [Name] | [Date] | [Complete/In Progress] |

---

## 6. Long-Term Remediation Plan

| # | Action Item | Owner | Priority | Deadline | Status |
|---|---|---|---|---|---|
| 1 | [Remediation action] | [Name] | P1 | [Date] | [Status] |
| 2 | [Remediation action] | [Name] | P2 | [Date] | [Status] |
| 3 | [Remediation action] | [Name] | P2 | [Date] | [Status] |

---

## 7. Lessons Learned

### What Went Well

1. [Positive observation with evidence]
2. [Positive observation with evidence]

### What Could Be Improved

1. [Issue] -> [Specific improvement action]
2. [Issue] -> [Specific improvement action]

### Detection Assessment

- **How detected:** [Automated alert / Manual discovery / External report]
- **Time to detect:** [DURATION]
- **Could detection have been faster?** [Yes/No - explanation]

### Response Assessment

- **Time to respond:** [DURATION]
- **Were runbooks followed?** [Yes / No / Partially]
- **Right people available?** [Yes / No]
- **Communication effectiveness:** [1-5 rating with explanation]

---

## 8. Appendices

### A. Evidence Inventory

| Evidence ID | Description | Date Collected | Hash (SHA-256) | Location |
|---|---|---|---|---|
| EVD-001 | [Description] | [Date] | [Hash] | [Location] |

### B. Communication Log

| Date/Time | From | To | Channel | Summary |
|---|---|---|---|---|
| [DateTime] | [Name] | [Name/Group] | [Email/Slack/Phone] | [Summary] |

### C. External Notifications

| Date | Recipient | Method | Content Summary | Status |
|---|---|---|---|---|
| [Date] | [Regulatory body / Individuals] | [Email/Portal] | [Summary] | [Sent/Pending] |

### D. Indicators of Compromise (IOCs)

| Type | Value | Context |
|---|---|---|
| IP Address | [IP] | [Source of attack / C2 server] |
| Domain | [Domain] | [Phishing / Malware distribution] |
| File Hash | [SHA-256] | [Malware sample] |
| Email Address | [Email] | [Phishing sender] |
