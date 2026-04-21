# Email Organizer - Reference Guide

## Priority Scoring Algorithm - Detailed

### Factor Definitions

#### Sender Importance (Weight: 30%)

| Score | Category | Examples |
|-------|----------|----------|
| 5 | Executive / Key Client | CEO, CTO, VP, major client contacts |
| 4 | Direct Manager / Important Vendor | Your boss, key vendor contacts |
| 3 | Colleague / Regular Vendor | Teammates, known vendors |
| 2 | Known External | Recruiters, industry contacts |
| 1 | Unknown / Auto-generated | Marketing, unknown senders, noreply@ |

Sender importance can be configured via a sender priority list stored in `rules.json`.

#### Time Sensitivity (Weight: 25%)

| Score | Urgency | Indicators |
|-------|---------|------------|
| 5 | Due today or overdue | Keywords: "urgent", "ASAP", "by EOD", "deadline today" |
| 4 | Due tomorrow | Keywords: "by tomorrow", "first thing", deadline in 24h |
| 3 | Due this week | Keywords: "this week", "by Friday", deadline in 2-5 days |
| 2 | Due this month | Keywords: "this month", "Q1", deadline in 6-30 days |
| 1 | No deadline | No time-bound language detected |

#### Impact (Weight: 25%)

| Score | Scope | Indicators |
|-------|-------|------------|
| 5 | Revenue / Customer affecting | Keywords: "contract", "deal", "customer complaint", "SLA" |
| 4 | Team / Cross-functional | Keywords: "blocked", "dependency", "team needs", CC'd many |
| 3 | Your work directly | TO: you directly, references your projects |
| 2 | Informational for your area | CC'd, FYI about your domain |
| 1 | General informational | Newsletters, all-hands announcements |

#### Effort Required (Weight: 10%)

| Score | Time Needed | Indicators |
|-------|-------------|------------|
| 5 | Quick read/ack only | Short email, no questions asked |
| 4 | 2-minute reply | Simple question, yes/no, forward |
| 3 | 10-30 minute task | Research needed, draft response, review attachment |
| 2 | 30-60 minute task | Detailed response, create document, multi-step |
| 1 | Multi-hour project | Major deliverable, complex analysis |

Note: Lower effort scores get higher priority to favor quick wins (inverted from raw effort).

#### Thread Activity (Weight: 10%)

| Score | Activity Level | Indicators |
|-------|---------------|------------|
| 5 | Hot thread (6+ replies) | Fast-moving conversation, potential escalation |
| 4 | Active thread (4-5 replies) | Ongoing discussion, may need input |
| 3 | Normal thread (2-3 replies) | Standard back-and-forth |
| 2 | Single reply | Initial response |
| 1 | New email (no replies) | Fresh thread |

### Composite Score Calculation

```
Priority Score = (Sender x 0.30) + (Time x 0.25) + (Impact x 0.25) + (Effort x 0.10) + (Thread x 0.10)
```

Example:
- Boss sends email (Sender: 5) about a deal closing today (Time: 5, Impact: 5)
- Needs a quick approval (Effort: 4), first email in thread (Thread: 1)
- Score = (5 x 0.30) + (5 x 0.25) + (5 x 0.25) + (4 x 0.10) + (1 x 0.10) = 1.50 + 1.25 + 1.25 + 0.40 + 0.10 = **4.50** (Critical)

## Inbox Zero Methodology - Deep Dive

### The GTD-Inspired Email Workflow

David Allen's Getting Things Done maps to email processing:

1. **Capture**: All emails land in inbox (single capture point)
2. **Clarify**: Apply the triage decision tree to each email
3. **Organize**: Label and file using the folder structure
4. **Reflect**: Weekly review of waiting-for and deferred items
5. **Engage**: Work through action items by priority

### The 4 D's Extended

| Decision | Time Limit | Resulting Label | Destination |
|----------|------------|-----------------|-------------|
| **Delete** | Instant | None | Trash |
| **Do** | <2 minutes | None | Archive after done |
| **Delegate** | <2 minutes | @Waiting-For | Forwarded + tracked |
| **Defer** | <30 seconds | @Action-Required + date | Stays labeled |

### Batch Processing Science

Research shows checking email in batches (3x/day) vs. continuously results in:
- 20% less time spent on email overall
- Lower stress (cortisol) levels
- Better focus during work blocks
- Faster response times on important items (paradoxically)

Recommended batch schedule:
- **Batch 1** (8:30 AM): 15 minutes - Process overnight emails
- **Batch 2** (12:30 PM): 10 minutes - Process morning emails
- **Batch 3** (4:30 PM): 10 minutes - Clear remaining, set up tomorrow

## Auto-Filter Best Practices

### Filter Priority Order

Filters should be processed in this order (most specific first):

1. VIP senders (executives, key clients) - always surface
2. Spam and unsubscribe candidates - always suppress
3. Auto-notifications (calendar, CI/CD, monitoring) - skip inbox
4. Project-specific filters - route to correct label
5. Newsletter/digest filters - batch for read-review
6. Catch-all rules - default categorization

### Filter Maintenance Schedule

| Frequency | Action |
|-----------|--------|
| Weekly | Review filter hit counts, disable zero-hit filters |
| Monthly | Audit label usage, merge under-used labels |
| Quarterly | Full filter review, clean up stale rules |
| On change | Update filters when changing projects, clients, or roles |

### Gmail Filter Syntax Reference

```
Common operators:
  from:sender@domain.com      - Specific sender
  to:me                       - Addressed directly to you
  cc:me                       - You're CC'd
  subject:(keyword)           - Subject contains word
  has:attachment               - Has file attached
  filename:pdf                 - Specific attachment type
  is:unread                    - Unread messages
  after:2025/01/01             - Date filtering
  larger:5M                    - Size filtering
  list:listname@domain.com    - Mailing list
  -{keyword}                  - Exclude keyword

Combine with AND (space), OR, and grouping with ()
```

## Email Response Time SLAs

| Sender Category | Target Response | Escalation If Missed |
|-----------------|-----------------|----------------------|
| Executive | 2 hours | Auto-flag at 4 hours |
| Direct manager | 4 hours | Auto-flag at 8 hours |
| Client | 4 hours (business hours) | Auto-flag at 24 hours |
| Colleague | 24 hours | Weekly review catch |
| External/vendor | 48 hours | No auto-escalation |
| Newsletter/FYI | No response needed | Auto-archive after 5 days |

## Metrics Definitions

| Metric | Definition | Target |
|--------|------------|--------|
| **Inbox Zero Rate** | % of days ending with 0-5 items in inbox | >80% |
| **Processing Time** | Average seconds per email during triage | <30s |
| **Response Time** | Hours from receipt to response for action items | <24h |
| **Unsubscribe Rate** | Newsletters unsubscribed per week | 3+ until stable |
| **Filter Coverage** | % of emails auto-categorized by filters | >60% |
| **Touch Count** | Average times an email is opened before action | <2 |
