# Compliance Checker - Reference Guide

## Framework Deep Dive

### GDPR Control Mapping

#### Article 30 - Records of Processing Activities

| Field | Description | Example |
|---|---|---|
| Processing purpose | Why data is processed | Customer account management |
| Data categories | Types of personal data | Name, email, payment info |
| Data subjects | Whose data is processed | Customers, employees, prospects |
| Recipients | Who receives the data | Payment processor, CRM vendor |
| Transfers | Cross-border transfers | US cloud provider (SCC basis) |
| Retention | How long data is kept | 3 years after account closure |
| Security measures | Technical/org safeguards | Encryption, access controls |

#### Article 32 - Security of Processing

| Measure | Implementation | Evidence |
|---|---|---|
| Pseudonymization | Data masking in non-prod environments | Configuration documentation |
| Encryption at rest | AES-256 for databases and file storage | Encryption policy + audit |
| Encryption in transit | TLS 1.2+ for all connections | SSL certificate inventory |
| Confidentiality | Role-based access controls | RBAC matrix documentation |
| Integrity | Input validation, checksums | Code review records |
| Availability | Backup and DR procedures | DR test results |
| Resilience | Load balancing, failover | Architecture documentation |
| Testing | Regular security assessments | Pen test reports |

### SOC 2 Trust Service Criteria Detail

#### CC6 - Logical and Physical Access Controls

| Criteria | Description | Common Controls |
|---|---|---|
| CC6.1 | Logical access security software | SSO, MFA, password policies |
| CC6.2 | New user registration and authorization | Onboarding checklist, approval workflow |
| CC6.3 | User access modification and removal | Role change process, offboarding |
| CC6.4 | Physical access restrictions | Badge access, visitor logs |
| CC6.5 | Data transmission protection | TLS, VPN, encrypted email |
| CC6.6 | Access boundary protection | Firewalls, network segmentation |
| CC6.7 | Data input and output controls | Validation, sanitization |
| CC6.8 | Unauthorized software prevention | Endpoint protection, app whitelisting |

#### CC7 - System Operations

| Criteria | Description | Common Controls |
|---|---|---|
| CC7.1 | Detect and monitor anomalies | SIEM, IDS, log monitoring |
| CC7.2 | Monitor system components | Infrastructure monitoring, alerting |
| CC7.3 | Evaluate security events | Incident classification, triage |
| CC7.4 | Respond to incidents | Incident response plan, runbooks |
| CC7.5 | Recover from incidents | DR plan, backup restoration |

### PCI-DSS v4.0 Requirements

| Requirement | Category | Key Controls |
|---|---|---|
| 1 | Network controls | Firewalls, network segmentation |
| 2 | Secure configurations | Hardening standards, no defaults |
| 3 | Protect stored data | Encryption, key management, masking |
| 4 | Encrypt transmissions | TLS for cardholder data |
| 5 | Anti-malware | Endpoint protection, scanning |
| 6 | Secure development | SDLC, code review, patching |
| 7 | Restrict access | Need-to-know, RBAC |
| 8 | Identity and authentication | MFA, strong passwords |
| 9 | Physical access | Badge access, media destruction |
| 10 | Logging and monitoring | Audit trails, SIEM, NTP |
| 11 | Security testing | Vulnerability scans, pen tests |
| 12 | Organizational policies | Security policy, training, risk assessment |

### HIPAA Security Rule Categories

#### Administrative Safeguards (45 CFR 164.308)

| Standard | Implementation | Required/Addressable |
|---|---|---|
| Security management | Risk analysis, sanctions, review | Required |
| Assigned security responsibility | Security officer designation | Required |
| Workforce security | Authorization, clearance, termination | Addressable |
| Information access management | Access authorization, establishment | Required |
| Security awareness training | Reminders, malware, login monitoring | Addressable |
| Security incident procedures | Response and reporting | Required |
| Contingency plan | Backup, DR, emergency mode | Required |
| Evaluation | Periodic assessment | Required |
| BAA requirements | Contracts with business associates | Required |

#### Technical Safeguards (45 CFR 164.312)

| Standard | Implementation | Required/Addressable |
|---|---|---|
| Access control | Unique ID, emergency access, auto logoff, encryption | Mixed |
| Audit controls | Hardware/software/process logging | Required |
| Integrity | ePHI alteration/destruction protections | Addressable |
| Person authentication | Verify identity of users | Required |
| Transmission security | Integrity controls, encryption | Addressable |

## Cross-Framework Control Mapping

| Control Area | GDPR | SOC 2 | HIPAA | PCI-DSS | ISO 27001 |
|---|---|---|---|---|---|
| Access control | Art. 32 | CC6.1-6.3 | 164.312(a) | Req 7-8 | A.9 |
| Encryption | Art. 32 | CC6.5 | 164.312(a)(2)(iv) | Req 3-4 | A.10 |
| Incident response | Art. 33-34 | CC7.3-7.4 | 164.308(a)(6) | Req 12.10 | A.16 |
| Risk assessment | Art. 35 | CC3.1-3.4 | 164.308(a)(1) | Req 12.2 | A.8 |
| Logging/monitoring | Art. 30 | CC7.1-7.2 | 164.312(b) | Req 10 | A.12.4 |
| Training | Art. 39 | CC1.4 | 164.308(a)(5) | Req 12.6 | A.7.2.2 |
| Vendor management | Art. 28 | CC9.2 | 164.308(b)(1) | Req 12.8 | A.15 |
| Data retention | Art. 5(1)(e) | C1.2 | 164.530(j) | Req 3.1 | A.8.3 |
| Backup/recovery | Art. 32 | A1.2 | 164.308(a)(7) | Req 12.10 | A.12.3 |

## Maturity Assessment Criteria

### Level 1 - Initial (0-20%)

- No formal policies or procedures
- Ad hoc responses to compliance requirements
- No designated compliance roles
- Limited awareness of regulatory requirements

### Level 2 - Developing (21-40%)

- Basic policies exist but are inconsistently followed
- Some compliance training provided
- Reactive approach to compliance issues
- Limited documentation of processes

### Level 3 - Defined (41-60%)

- Standardized policies and procedures documented
- Regular compliance training schedule
- Designated compliance roles and responsibilities
- Consistent process execution with some gaps

### Level 4 - Managed (61-80%)

- Metrics tracked for compliance activities
- Regular internal audits and assessments
- Automated controls where possible
- Continuous monitoring of key controls

### Level 5 - Optimized (81-100%)

- Continuous improvement processes in place
- Proactive identification of emerging requirements
- Cross-framework control optimization
- Industry-leading practices adopted

## Evidence Collection Guide

| Evidence Type | Examples | Storage Requirements |
|---|---|---|
| Policies | Security policy, privacy policy, AUP | Version-controlled document repository |
| Procedures | Incident response plan, onboarding process | Documented with review dates |
| Configuration | Firewall rules, access control lists | Automated configuration exports |
| Logs | Access logs, change logs, audit trails | Immutable log storage, retention policy |
| Certifications | SOC 2 report, ISO certificate | Secure document management |
| Training records | Completion dates, scores, attestations | HR/LMS system with export capability |
| Test results | Pen test report, vulnerability scan | Dated reports with remediation tracking |
| Contracts | DPAs, BAAs, vendor agreements | Legal document management system |
| Risk assessments | Risk register, DPIA, LIA | Reviewed and updated quarterly |
