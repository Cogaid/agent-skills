# Incident Report Writer - Reference Guide

## Incident Classification Deep Dive

### Data Breach Subtypes

| Subtype | Description | Typical Severity | Regulatory Trigger |
|---|---|---|---|
| Exfiltration | Data copied outside organization | P0 | All frameworks |
| Unauthorized access | Access by unauthorized individual | P0-P1 | GDPR Art. 33, HIPAA |
| Accidental disclosure | Sent to wrong recipient | P1-P2 | GDPR (if personal data) |
| Lost/stolen device | Device with unencrypted data | P1-P2 | HIPAA, PCI-DSS |
| Ransomware | Data encrypted, possibly exfiltrated | P0 | All frameworks |
| Insider theft | Employee deliberately steals data | P0 | All frameworks |
| API exposure | Data exposed via misconfigured API | P1-P2 | SOC 2, PCI-DSS |
| Cloud misconfiguration | Storage bucket or service exposed | P1-P2 | All frameworks |

### System Outage Classification

| Duration | Severity | SLA Impact | Typical Response |
|---|---|---|---|
| < 5 minutes | P3-P4 | Usually within SLA | Monitor, log |
| 5-30 minutes | P2-P3 | May breach SLA | Investigate, communicate |
| 30 min - 2 hours | P1-P2 | Likely SLA breach | Incident commander, status page |
| 2-8 hours | P1 | SLA breach, credits | War room, executive comms |
| > 8 hours | P0 | Major SLA breach | All hands, customer comms |

## Root Cause Analysis Methods

### 5 Whys Framework

```
Incident: Production database became unresponsive

Why 1: Database ran out of connections
  -> Connection pool was exhausted

Why 2: Connection pool was exhausted
  -> A long-running query held connections open

Why 3: A long-running query held connections
  -> New report query lacked a timeout and scanned full table

Why 4: Query lacked timeout
  -> No query timeout policy enforced at the application layer

Why 5: No query timeout policy
  -> Database access patterns were never codified into standards

ROOT CAUSE: Lack of database query standards and timeout enforcement
```

### Fishbone (Ishikawa) Diagram Categories

| Category | Examples of Contributing Factors |
|---|---|
| People | Training gaps, staffing levels, communication failures |
| Process | Missing runbooks, unclear escalation, no change management |
| Technology | System bugs, capacity limits, missing monitoring |
| Environment | Network issues, cloud provider outage, physical damage |
| Policy | Outdated policies, missing controls, unclear ownership |
| Third Party | Vendor failure, supply chain compromise, API change |

### Fault Tree Analysis

Used for complex incidents with multiple failure paths:

```
                    [Incident Occurred]
                    /                  \
           [Path A Failed]        [Path B Failed]
           /            \              |
    [Control 1     [Control 2    [Control 3
     Missing]       Bypassed]     Failed]
```

## Notification Requirements Detail

### GDPR Article 33 - Notification to Supervisory Authority

**Deadline:** 72 hours from awareness
**Required content:**
1. Nature of the breach including categories and approximate numbers
2. Name and contact details of DPO or other contact point
3. Description of likely consequences
4. Description of measures taken or proposed

**Template notification:**
```
To: [Supervisory Authority]
Date: [DATE AND TIME]

We are writing to notify you of a personal data breach pursuant
to Article 33 of the GDPR.

Nature of breach: [DESCRIPTION]
Date of breach: [DATE]
Date of discovery: [DATE]
Categories of data subjects: [LIST]
Approximate number of data subjects: [NUMBER]
Categories of personal data: [LIST]
Approximate number of records: [NUMBER]

DPO Contact: [NAME, EMAIL, PHONE]

Likely consequences: [DESCRIPTION]

Measures taken: [DESCRIPTION OF RESPONSE AND REMEDIATION]

[We will provide additional information as our investigation
continues.]
```

### GDPR Article 34 - Notification to Data Subjects

**Trigger:** High risk to rights and freedoms
**Required content:**
1. Clear and plain language description of the breach
2. DPO or contact point details
3. Description of likely consequences
4. Description of measures taken and recommended protective steps

### HIPAA Breach Notification

**Individual notification:** Within 60 days of discovery
**HHS notification:** Within 60 days if 500+ individuals; annual if fewer
**Media notification:** Required if 500+ in a single state/jurisdiction

**Required content:**
1. Brief description of what happened, including dates
2. Types of information involved
3. Steps individuals should take to protect themselves
4. What the entity is doing to investigate and mitigate
5. Contact information for questions

### SEC Form 8-K (Item 1.05)

**Deadline:** 4 business days after determining materiality
**Required content:**
1. Nature of the incident
2. Scope of the incident
3. Timing of the incident
4. Material impact or reasonably likely material impact

## Incident Response Team Roles

| Role | Responsibilities | Skills Required |
|---|---|---|
| Incident Commander | Overall coordination, decisions, communications | Leadership, crisis management |
| Technical Lead | Investigation, containment, remediation | System administration, security |
| Communications Lead | Internal and external messaging | PR, legal awareness |
| Legal Counsel | Regulatory assessment, notification decisions | Privacy law, litigation |
| Scribe/Recorder | Timeline documentation, evidence logging | Detail-oriented, organized |
| Executive Sponsor | Business decisions, resource allocation | Authority, business context |
| Forensics Analyst | Evidence preservation, technical analysis | Digital forensics |
| Customer Success | Customer communications, impact assessment | Customer relationships |

## Evidence Preservation Checklist

- [ ] Take system images/snapshots before making changes
- [ ] Preserve log files (access, application, system, network)
- [ ] Screenshot relevant dashboards and alert states
- [ ] Record network traffic captures if available
- [ ] Preserve email communications related to the incident
- [ ] Document the chain of custody for all evidence
- [ ] Note timestamps in UTC for all evidence
- [ ] Hash all evidence files for integrity verification
- [ ] Store evidence in a read-only, access-controlled location
- [ ] Maintain an evidence inventory with descriptions and locations

## Communication Templates

### Internal Stakeholder Update

```
INCIDENT UPDATE - [INC-ID] - [STATUS]
Time: [UTC TIMESTAMP]
Commander: [NAME]

SITUATION: [1-2 sentences on current state]

WHAT WE KNOW:
- [Key fact 1]
- [Key fact 2]

WHAT WE ARE DOING:
- [Action 1 with owner]
- [Action 2 with owner]

NEXT UPDATE: [TIME]
QUESTIONS: Contact [NAME] at [CHANNEL]
```

### Customer Communication

```
Subject: [Service Name] - Incident Update

Dear [Customer],

We are writing to inform you of [brief description of incident]
that occurred on [DATE].

WHAT HAPPENED:
[Clear, non-technical explanation]

WHAT WE ARE DOING:
[Steps taken and planned]

WHAT YOU CAN DO:
[Recommended actions for the customer]

We will provide another update by [TIME/DATE].

For questions, please contact [SUPPORT CHANNEL].

Sincerely,
[NAME, TITLE]
```

## Metrics for Incident Response Effectiveness

| Metric | Definition | Target | Benchmark |
|---|---|---|---|
| Mean Time to Detect (MTTD) | Time from incident to detection | < 1 hour | Industry avg: 207 days (breaches) |
| Mean Time to Respond (MTTR) | Time from detection to containment | < 4 hours | Industry avg: 73 days (breaches) |
| Mean Time to Resolve | Time from detection to full resolution | < 24 hours (P1) | Varies by severity |
| Detection rate | Incidents detected internally vs externally | > 80% internal | Industry avg: ~60% |
| False positive rate | Alerts that are not actual incidents | < 20% | Varies by tooling |
| Post-incident review rate | % of P0-P1 incidents with PIR completed | 100% | Best practice |
| Action item closure rate | % of PIR actions completed on time | > 90% | Best practice |
