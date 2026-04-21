# SLA Breach Notification Template

## Notification Configuration

| Field | Value |
|-------|-------|
| **Template ID** | BREACH-NOTIFY-001 |
| **Trigger** | SLA metric exceeds 100% of allowed time |
| **Channels** | Email, Slack, PagerDuty (configurable by priority) |
| **Acknowledgment Required** | Yes, within 15 minutes |

---

## Email Notification Format

**Subject**: [SLA BREACH] {{priority}} - Ticket #{{ticket_id}} - {{customer_name}}

**Body**:

### Breach Details

| Field | Value |
|-------|-------|
| Ticket ID | #{{ticket_id}} |
| Customer | {{customer_name}} |
| Customer Tier | {{tier}} |
| Priority | {{priority}} |
| SLA Metric Breached | {{metric}} |
| Target Time | {{target_time}} |
| Actual Elapsed Time | {{actual_time}} |
| Overage | {{overage_time}} |

### Ticket Summary

{{ticket_summary}}

### Current Status

| Field | Value |
|-------|-------|
| Assigned Agent | {{agent_name}} |
| Last Update | {{last_update_time}} |
| Customer Waiting Since | {{wait_duration}} |
| Ticket Status | {{ticket_status}} |

### Required Actions

1. Acknowledge this breach within **15 minutes**
2. Contact the customer with a status update
3. Provide an estimated resolution time
4. Complete the Root Cause field in the ticket
5. Submit the breach report within **24 hours**

### Escalation Path

| Level | Contact | Method |
|-------|---------|--------|
| Team Lead | {{team_lead_name}} | {{team_lead_contact}} |
| Manager | {{manager_name}} | {{manager_contact}} |
| Director | {{director_name}} | {{director_contact}} |

---

## Slack Notification Format

```
:red_circle: *SLA BREACH*
*Ticket:* #{{ticket_id}} | *Customer:* {{customer_name}} ({{tier}})
*Metric:* {{metric}} | *Overage:* {{overage_time}}
*Agent:* {{agent_name}} | *Priority:* {{priority}}
*Action:* Acknowledge within 15 min
[View Ticket]({{ticket_url}}) | [Acknowledge]({{ack_url}})
```

---

## PagerDuty Alert Format (P1/P2 only)

```
Title: SLA Breach - {{priority}} - #{{ticket_id}}
Severity: {{pagerduty_severity}}
Details:
  Customer: {{customer_name}} ({{tier}})
  Metric: {{metric}}
  Overage: {{overage_time}}
  Agent: {{agent_name}}
Dedup Key: sla-breach-{{ticket_id}}-{{metric}}
```

---

## Notification Routing Rules

| Priority | Notification Channels | Escalation After |
|----------|----------------------|-----------------|
| P1 - Critical | Email + Slack + PagerDuty | 15 minutes if unacknowledged |
| P2 - High | Email + Slack | 30 minutes if unacknowledged |
| P3 - Medium | Email + Slack | 2 hours if unacknowledged |
| P4 - Low | Email only | 4 hours if unacknowledged |

---

## Variables

| Variable | Source | Example |
|----------|--------|---------|
| `{{ticket_id}}` | Ticketing system | "TK-45678" |
| `{{customer_name}}` | CRM | "Acme Corporation" |
| `{{tier}}` | Customer record | "Enterprise" |
| `{{priority}}` | Ticket priority | "P1 - Critical" |
| `{{metric}}` | SLA policy | "First Response Time" |
| `{{target_time}}` | SLA configuration | "15 minutes" |
| `{{actual_time}}` | Calculated | "47 minutes" |
| `{{overage_time}}` | Calculated | "32 minutes over" |
| `{{agent_name}}` | Ticket assignment | "Sarah Chen" |
| `{{ticket_url}}` | Ticketing system | URL to ticket |
| `{{ack_url}}` | Alert system | URL to acknowledge |
