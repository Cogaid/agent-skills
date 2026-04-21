---
name: email-organizer
description: Categorize, prioritize, and organize inbox messages for efficient email management. Use when the user mentions "email organization," "inbox management," "email triage," "inbox zero," "email categorization," "email priority," "email sorting," "clean up inbox," "email labels," "email workflow," or "manage emails."
metadata:
  version: 1.0.0
  category: personal-assistance
---

# Email Organizer

Categorize and prioritize inbox messages using structured frameworks to achieve and maintain inbox zero.

## Purpose

Transform an overwhelming inbox into an organized, actionable system. Covers email categorization, priority scoring, auto-labeling rules, batch processing workflows, folder structures, and triage decision trees for efficient email handling.

## Quick Reference

### Email Categorization Framework

| Category | Description | Action Required | Target Response |
|----------|-------------|-----------------|-----------------|
| **Action Required** | Needs your response or work | Yes - you must act | Within 24 hours |
| **Waiting For** | Delegated, awaiting reply | Monitor | Check every 2-3 days |
| **FYI / Read** | Informational, no action needed | Read when convenient | Within 48 hours |
| **Delegate** | Someone else should handle this | Forward and track | Same day |
| **Archive** | Reference material, completed | File immediately | Immediate |
| **Delete/Unsubscribe** | Spam, irrelevant, noise | Remove | Immediate |

### Priority Scoring Matrix

| Factor | Weight | Score 1 (Low) | Score 3 (Medium) | Score 5 (High) |
|--------|--------|---------------|-------------------|-----------------|
| **Sender importance** | 30% | Unknown/external | Colleague/vendor | Boss/client/exec |
| **Time sensitivity** | 25% | No deadline | This week | Today/overdue |
| **Impact** | 25% | Informational | Affects your work | Affects revenue/team |
| **Effort required** | 10% | Quick read | 10-30 min task | Multi-hour project |
| **Thread activity** | 10% | Single email | 3-5 replies | 6+ replies (hot) |

**Priority Score = Sum of (Factor Score x Weight)**

| Total Score | Priority Level | Action |
|-------------|---------------|--------|
| 4.0 - 5.0 | Critical | Handle immediately |
| 3.0 - 3.9 | High | Handle within 2 hours |
| 2.0 - 2.9 | Medium | Handle within 24 hours |
| 1.0 - 1.9 | Low | Batch process end of day |

## Workflow

### Email Triage Decision Tree

```
NEW EMAIL ARRIVES
│
├── Is it spam or irrelevant?
│   └── YES → Delete / Unsubscribe → DONE
│
├── Is it an auto-notification you don't need?
│   └── YES → Create filter to skip inbox → Archive → DONE
│
├── Can you respond in under 2 minutes?
│   └── YES → Respond now → Archive → DONE
│
├── Does someone else need to handle this?
│   └── YES → Forward + brief context → Label "Waiting For" → DONE
│
├── Does it require action from you?
│   ├── YES, today → Label "Action Required" + priority tag → DONE
│   └── YES, later → Label "Action Required" + set due date → DONE
│
├── Is it informational / FYI?
│   └── YES → Label "FYI" → Read in next batch window → DONE
│
└── Is it reference material?
    └── YES → Label by topic → Archive → DONE
```

### Batch Processing Workflow

```
EMAIL BATCH PROCESSING SCHEDULE

BATCH 1: Morning Triage (15 minutes, start of day)
- [ ] Process all emails received overnight
- [ ] Apply triage decision tree to each
- [ ] Flag critical items for immediate action
- [ ] Delegate items that belong to others
- [ ] Quick-reply to anything under 2 minutes

BATCH 2: Midday Check (10 minutes, after lunch)
- [ ] Process new emails from morning
- [ ] Follow up on delegated items
- [ ] Handle medium-priority action items
- [ ] Archive completed threads

BATCH 3: End-of-Day Sweep (10 minutes, last hour)
- [ ] Process afternoon emails
- [ ] Clear remaining quick replies
- [ ] Review "Waiting For" items for follow-up
- [ ] Set tomorrow's email priorities
- [ ] Achieve inbox zero (or close to it)

WEEKLY REVIEW (15 minutes, Friday afternoon)
- [ ] Review all "Waiting For" items — nudge if stale
- [ ] Clear "FYI" items not read within 5 days
- [ ] Unsubscribe from 3+ newsletters you haven't opened
- [ ] Archive completed project threads
- [ ] Review auto-filter effectiveness
```

## Templates

### Folder/Label Structure

```
INBOX ORGANIZATION STRUCTURE

INBOX (temporary holding — target: 0 items)

ACTION LABELS:
├── @Action-Required     (tasks you need to do)
├── @Waiting-For         (delegated or pending reply)
├── @Read-Review         (articles, FYIs, digests)
└── @Scheduled           (deferred to specific date)

CATEGORY LABELS:
├── Projects/
│   ├── Project-Alpha
│   ├── Project-Beta
│   └── Project-Gamma
├── Clients/
│   ├── Client-Acme
│   ├── Client-Globex
│   └── Client-Initech
├── Internal/
│   ├── HR-Admin
│   ├── Finance
│   └── IT-Support
├── Newsletters/
│   ├── Industry-News
│   ├── Product-Updates
│   └── Learning
└── Personal/
    ├── Travel
    ├── Receipts
    └── Subscriptions

ARCHIVE (searchable, organized by year/quarter)
TRASH (auto-empty after 30 days)
```

### Auto-Label Rules

```
AUTO-LABEL CONFIGURATION

RULE 1: Executive emails
  IF sender IN [ceo@, cto@, vp-*@, {{boss_email}}]
  THEN label: @Action-Required, Priority: High
  AND star: yellow

RULE 2: Client emails
  IF sender domain IN [{{client_domains}}]
  THEN label: Clients/{{matched_client}}
  AND label: @Action-Required

RULE 3: Calendar notifications
  IF from: calendar-notification@ OR subject contains "invitation"
  THEN label: Calendar
  AND skip inbox (process via calendar app)

RULE 4: Automated reports
  IF subject matches "Daily Report*" OR "Weekly Summary*"
  THEN label: @Read-Review
  AND skip inbox

RULE 5: Newsletter/marketing
  IF header: list-unsubscribe present
  AND sender NOT IN [{{whitelist}}]
  THEN label: Newsletters/{{category}}
  AND skip inbox

RULE 6: Receipts and invoices
  IF subject contains "receipt" OR "invoice" OR "order confirmation"
  THEN label: Personal/Receipts
  AND skip inbox

RULE 7: Thread escalation
  IF thread reply count > 5
  AND you are CC'd (not TO)
  THEN label: @Read-Review (may not need your action)

RULE 8: Out-of-office auto-replies
  IF subject contains "Out of Office" OR "OOO" OR "Auto-Reply"
  THEN archive immediately
```

### Inbox Zero Methodology

```
INBOX ZERO FRAMEWORK

PRINCIPLE: Your inbox is a processing queue, not a storage system.

THE 4 D's:
┌──────────────────────────────────────────────────────┐
│                                                      │
│  DELETE    →  Does this need to exist? No? Delete.   │
│  DO        →  Under 2 minutes? Do it now.            │
│  DELEGATE  →  Someone else's job? Forward + track.   │
│  DEFER     →  Needs time? Schedule and label.        │
│                                                      │
└──────────────────────────────────────────────────────┘

DAILY TARGETS:
- Morning inbox count after triage: < 10
- End-of-day inbox count: 0-5
- Processing time per email: < 30 seconds (triage decision)
- Max time in inbox per day: 35 minutes (3 batches)

WEEKLY METRICS:
- Emails processed: {{count}}
- Average inbox count at EOD: {{avg}}
- Response time (action items): {{avg_hours}} hours
- Unsubscribes this week: {{count}}
- Filters created this week: {{count}}

ANTI-PATTERNS TO AVOID:
- Checking email every 5 minutes (batch instead)
- Using inbox as a to-do list (use task manager)
- Leaving emails "unread" as reminders (label instead)
- Replying to all when not needed
- Filing into too many folders (search is faster)
```

### Email Response Templates

```
QUICK RESPONSE: Acknowledge and defer
"Thanks for sending this, {{name}}. I'll review and get back
to you by {{date}}. Let me know if anything is urgent before then."

QUICK RESPONSE: Delegate
"Thanks, {{name}}. I'm looping in {{delegate}} who can help
with this directly. {{delegate}}, could you take a look?"

QUICK RESPONSE: Need more info
"Thanks for reaching out. Before I can help, could you
clarify: {{specific_question}}? That will help me give
you a more useful response."

QUICK RESPONSE: Decline meeting
"Thanks for the invite. I don't think I'll be able to add
value to this meeting, but I'm happy to review any notes
or decisions that come out of it. Feel free to send a summary."

QUICK RESPONSE: Close thread
"This looks resolved — closing the loop. Let me know if
anything else comes up."
```

## Scripts & Tools

**organize_inbox.py**: Scan and categorize inbox messages
```bash
python scripts/organize_inbox.py --account {{email}} --rules rules.json
# Output: Categorized emails with labels applied
```

**priority_score.py**: Score emails by priority
```bash
python scripts/priority_score.py --account {{email}} --unread-only
# Output: Prioritized list of emails with scores and recommended actions
```

**auto_filter_generator.py**: Generate filter rules from email patterns
```bash
python scripts/auto_filter_generator.py --analyze-last 500
# Output: Suggested filter rules based on sender/subject patterns
```

**inbox_metrics.py**: Track inbox management metrics
```bash
python scripts/inbox_metrics.py --period this-week
# Output: Processing time, response time, inbox count trends
```

## Best Practices

1. **Process, don't just read** - Every email gets a decision: delete, do, delegate, or defer
2. **Touch once** - Avoid reading an email without taking action on it
3. **Batch processing** - Check email 3 times per day, not continuously
4. **Two-minute rule** - If it takes less than 2 minutes, do it now
5. **Unsubscribe aggressively** - If you haven't read it in 3 weeks, unsubscribe
6. **Filters are investments** - Spending 2 minutes on a filter saves hours over time
7. **Search over folders** - Deep folder hierarchies waste more time than they save
8. **Separate action from reference** - Action items go to task manager, not inbox
9. **Weekly purge** - Every Friday, clear stale items and review waiting-for list
10. **Email is not chat** - For quick exchanges, use Slack/Teams instead

## Related Skills

- Daily overview: `daily-briefing`
- Email writing: `email-drafting`
- Task management: `task-prioritizer`
- Meeting scheduling: `meeting-scheduler`
