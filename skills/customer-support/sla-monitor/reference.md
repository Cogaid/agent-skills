# SLA Monitor - Reference Guide

## SLA Fundamentals

### What is an SLA?

A Service Level Agreement (SLA) is a formal commitment between a service provider and a customer that defines the expected level of service. In customer support, SLAs typically govern response times, resolution times, system availability, and quality standards.

### SLA vs SLO vs SLI

| Term | Full Name | Definition | Example |
|------|-----------|-----------|---------|
| **SLA** | Service Level Agreement | Contractual commitment with penalties | "99.9% uptime or 10% service credit" |
| **SLO** | Service Level Objective | Internal target (stricter than SLA) | "99.95% uptime internal goal" |
| **SLI** | Service Level Indicator | The actual measured metric | "Uptime was 99.93% this month" |

Best practice: Set SLOs stricter than SLAs so you have a buffer before breaching contractual commitments.

---

## Metric Definitions in Detail

### First Response Time (FRT)

**Definition**: The elapsed time between when a customer submits a request and when an agent sends the first substantive response.

**What counts as "first response"**:
- A human agent reply addressing the issue
- A personalized acknowledgment with expected timeline

**What does NOT count**:
- Automated acknowledgment emails ("We received your request")
- Auto-responder messages
- Bot greetings in chat

**Clock rules**:
| Scenario | Clock Behavior |
|----------|---------------|
| Ticket created during business hours | Starts immediately |
| Ticket created outside business hours | Starts at next business hours opening |
| Ticket reassigned between teams | Clock continues (does not reset) |
| Customer sends additional messages | Clock is unaffected |

**Calculation**:
```
FRT = First Agent Response Timestamp - Ticket Creation Timestamp
(adjusted for business hours if applicable)
```

---

### Resolution Time (RT)

**Definition**: The elapsed time between ticket creation and confirmed resolution (status set to "Resolved" or "Closed").

**Clock pause rules**:
| Status | Clock |
|--------|-------|
| Open / In Progress | Running |
| Waiting on Customer | Paused |
| Waiting on Third Party | Running (unless SLA excludes) |
| On Hold (internal) | Running |
| Resolved / Closed | Stopped |
| Reopened | Resumes from previous elapsed time |

**Reopen policy**: If a ticket is reopened within 72 hours, the original resolution does not count. The SLA clock resumes from where it was paused.

---

### Uptime / Availability

**Definition**: The percentage of time a system is operational and accessible within a measurement period.

**Calculation**:
```
Uptime % = ((Total Minutes in Period - Downtime Minutes) / Total Minutes in Period) x 100
```

**What the "nines" mean**:

| Uptime % | Allowed Downtime/Month | Allowed Downtime/Year |
|----------|----------------------|---------------------|
| 99.0% | 7h 18m | 3d 15h 36m |
| 99.5% | 3h 39m | 1d 19h 48m |
| 99.9% | 43m 50s | 8h 45m 36s |
| 99.95% | 21m 55s | 4h 22m 48s |
| 99.99% | 4m 23s | 52m 34s |
| 99.999% | 26s | 5m 15s |

**Exclusions** (typically):
- Scheduled maintenance (with advance notice)
- Force majeure events
- Customer-caused outages
- Third-party service failures (if documented)

---

### First Contact Resolution (FCR)

**Definition**: The percentage of issues resolved during the first customer interaction without requiring follow-up, escalation, or reopen.

**Calculation**:
```
FCR % = (Issues Resolved on First Contact / Total Issues) x 100
```

**Measurement rules**:
- Ticket must not be reopened within 72 hours
- Customer must not contact again about the same issue within 7 days
- Escalations do not count as first-contact resolution
- Transfers within the same interaction may still count (policy varies)

---

## Breach Prevention Framework

### The 70-80-90 Alert Model

Proactive alerts at percentage thresholds of elapsed SLA time prevent breaches before they happen.

| Alert Level | Threshold | Notification | Action Required |
|-------------|-----------|-------------|-----------------|
| **Green** | 0-70% elapsed | Dashboard only | Normal workflow |
| **Yellow** | 70-80% elapsed | In-app notification to agent | Prioritize this ticket |
| **Orange** | 80-90% elapsed | Email/Slack to team lead | Reassign if agent unavailable |
| **Red** | 90-100% elapsed | SMS/page to manager | Immediate intervention |
| **Critical** | 100%+ (breached) | Executive notification | Incident response process |

### Breach Root Cause Categories

When a breach occurs, categorize the root cause for trend analysis:

| Category | Description | Example |
|----------|-------------|---------|
| **Staffing** | Insufficient agents for volume | Holiday surge, unexpected absences |
| **Routing** | Ticket sent to wrong team/queue | Misclassified priority or category |
| **Complexity** | Issue required more time than expected | Multi-system debugging |
| **Dependency** | Waiting on external team/vendor | Engineering fix, vendor response |
| **Tool Failure** | System outage or performance issue | Ticketing system slow/down |
| **Process Gap** | No defined process for this scenario | New product without support docs |
| **Human Error** | Agent missed or forgot the ticket | Ticket lost in queue |

---

## SLA Negotiation Framework

### Setting Realistic Targets

**Step 1: Baseline Current Performance**
Measure actual performance for 90 days across all metrics before committing to SLA targets.

**Step 2: Set SLOs at 90th Percentile**
If 90% of tickets get first response within 2 hours, set the SLA at 2 hours (not the average).

**Step 3: Build in Buffer**
Set internal SLOs 10-20% stricter than external SLAs.

| Metric | External SLA | Internal SLO | Alert Threshold |
|--------|-------------|-------------|-----------------|
| FRT | 4 hours | 3 hours | 2.5 hours |
| RT | 24 hours | 18 hours | 14 hours |
| Uptime | 99.9% | 99.95% | Any incident |

### Penalty Structures

| Type | Description | Typical Terms |
|------|-------------|--------------|
| **Service Credits** | Discount on next invoice | 5-15% of monthly fee per breach |
| **Extended Service** | Free additional months | 1 month free per major breach |
| **Priority Bump** | Temporary tier upgrade | Enterprise treatment for 30 days |
| **Financial Penalty** | Direct payment to customer | Capped at 10-15% of contract value |

### Exclusion Clauses to Include

1. **Scheduled maintenance**: With 48+ hours advance notice, up to 4 hours/month
2. **Force majeure**: Natural disasters, government actions, pandemic
3. **Customer-caused**: Issues resulting from customer's own systems or actions
4. **Third-party failures**: When a critical vendor is the root cause (document list)
5. **Beta/preview features**: Explicitly excluded from SLA until GA

---

## Compliance Reporting Best Practices

### Daily Report
- Total tickets opened and closed
- Current SLA compliance rate (rolling 24h)
- Active breaches and at-risk tickets
- Queue depth and agent availability

### Weekly Report
- SLA compliance by metric, tier, and channel
- Breach count and root cause breakdown
- Trend comparison (this week vs. last 4 weeks)
- Top 3 improvement actions

### Monthly Report
- Full compliance breakdown with targets vs. actuals
- Breach deep-dive with root cause analysis
- Customer impact assessment
- Remediation plan progress
- Forecast for next month

### Quarterly Business Review (QBR)
- Trend analysis (3-month and 12-month)
- SLA renegotiation recommendations
- Capacity planning implications
- Customer satisfaction correlation (SLA vs. CSAT)

---

## Business Hours Configuration

### Standard Configurations

| Region | Business Hours | Timezone | Holidays |
|--------|---------------|----------|----------|
| US East | 9:00 AM - 6:00 PM Mon-Fri | America/New_York | US Federal |
| US West | 9:00 AM - 6:00 PM Mon-Fri | America/Los_Angeles | US Federal |
| EU | 9:00 AM - 6:00 PM Mon-Fri | Europe/London | UK Bank |
| APAC | 9:00 AM - 6:00 PM Mon-Fri | Asia/Singapore | SG Public |
| 24/7 | All hours, every day | UTC | None |

### Calculating SLA Time with Business Hours

```
If ticket created at Friday 5:00 PM (US East):
  Business hours end: 6:00 PM = 1 hour counted Friday
  Weekend: 0 hours counted
  Monday 9:00 AM: Clock resumes
  SLA of 4 business hours = Due Monday 12:00 PM
```

---

## Integration Points

### Common Ticketing Systems

| System | SLA Feature | API for Monitoring |
|--------|------------|-------------------|
| Zendesk | SLA Policies (native) | Zendesk API v2 `/tickets` |
| Freshdesk | SLA Policies (native) | Freshdesk API v2 `/tickets` |
| Jira Service Management | SLA Goals (native) | Jira REST API `/servicedesk` |
| Intercom | SLA Rules | Intercom API `/conversations` |
| HubSpot Service Hub | SLA settings | HubSpot API `/tickets` |
| Salesforce Service Cloud | Entitlements & Milestones | Salesforce REST API |

### Alerting Channels

| Channel | Best For | Latency |
|---------|----------|---------|
| Slack/Teams | Team-level alerts | Near real-time |
| Email | Formal notifications, reports | 1-5 minutes |
| PagerDuty/OpsGenie | Critical escalations | Immediate |
| SMS | After-hours manager alerts | Immediate |
| Dashboard | Ambient awareness | Real-time |
