# Reminder Manager - Reference Guide

## Reminder System Architecture

### Reminder Data Model

```
Reminder {
  id:           unique identifier
  type:         time-based | recurring | location-based | event-based | condition-based | follow-up
  title:        short description of what to do
  context:      why this reminder exists (original conversation, goal)
  priority:     urgent | high | normal | low
  status:       pending | due | overdue | snoozed | complete | canceled
  created_at:   timestamp
  trigger:      when/where/condition to fire
  snooze_count: number of times snoozed
  category:     work | personal | health | finance | social
  tags:         [list of tags for filtering]
}
```

### Trigger Types - Detailed

#### Time-Based Triggers

| Trigger | Specification | Example |
|---------|--------------|---------|
| Exact time | ISO datetime | 2025-01-20T15:00:00 |
| Relative | Duration from now | "in 2 hours", "in 3 days" |
| Time of day | HH:MM with recurrence | "every day at 9:00 AM" |
| Business hours | Weekday-aware | "next business day at 10 AM" |

#### Recurring Triggers

| Pattern | Specification | Example |
|---------|--------------|---------|
| Daily | Every N days | "every day at 9 AM" |
| Weekly | Specific days | "every Monday and Thursday at 10 AM" |
| Monthly | Day of month | "1st of every month", "last Friday of month" |
| Custom interval | Every N units | "every 2 weeks", "every 90 days" |
| Business days only | Skip weekends/holidays | "every weekday at 8:30 AM" |

#### Event-Based Triggers

| Trigger | Specification | Example |
|---------|--------------|---------|
| Before event | N minutes/hours/days before | "1 hour before next meeting with John" |
| After event | N minutes/hours/days after | "2 days after invoice sent" |
| On event start | When event begins | "when weekly standup starts" |
| On event end | When event ends | "after sprint review ends" |

#### Condition-Based Triggers

| Trigger | Specification | Example |
|---------|--------------|---------|
| Email received | From specific sender | "when John replies to my email" |
| Status change | Task/ticket status | "when JIRA-123 moves to Done" |
| Threshold | Value crosses boundary | "when account balance drops below $1000" |
| Weather | Condition met | "when rain forecast for tomorrow" |

### Follow-Up Escalation Framework

#### Standard Escalation Sequence

```
Day 0: Original action taken (email sent, request made)
Day 1-2: Wait (give reasonable response time)
Day 3: Gentle follow-up
  Template: "Just following up on [topic] from [date]..."
Day 7: More direct follow-up
  Template: "Wanted to check in again on [topic]..."
Day 14: Final follow-up with deadline
  Template: "Final check on [topic]. I'll close this out by [date] if I don't hear back..."
Day 21: Close loop
  Template: "Closing this out. Feel free to reopen if needed."
```

#### Escalation by Relationship Type

| Relationship | Initial Wait | Follow-up Interval | Max Attempts | Escalation Path |
|--------------|-------------|-------------------|-------------|-----------------|
| Client | 2 days | 3 days | 3 | Escalate to account manager |
| Boss/Manager | 1 day | 2 days | 2 | In-person/Slack DM |
| Peer/Colleague | 3 days | 5 days | 3 | CC their manager |
| Vendor | 3 days | 5 days | 3 | Try alternate contact |
| External/Cold | 5 days | 7 days | 3 | Different channel |
| Direct report | 1 day | 2 days | 2 | Verbal reminder |

### Smart Scheduling Rules

#### Time-of-Day Optimization

| Reminder Category | Best Time | Rationale |
|-------------------|-----------|-----------|
| Morning routines | 6:30-7:00 AM | Before day starts |
| Work priorities | 8:30-9:00 AM | After settling in |
| Meeting prep | 15 min before meeting | Just-in-time |
| Follow-ups to send | 10:00-11:00 AM | Optimal email send time |
| Afternoon tasks | 1:30-2:00 PM | Post-lunch energy dip reminder |
| End-of-day review | 4:30-5:00 PM | Before leaving |
| Personal errands | 5:30-6:00 PM | After work |
| Weekend tasks | Saturday 9:00 AM | Fresh start |
| Week planning | Sunday 7:00 PM | Prep for Monday |

#### Conflict Avoidance Rules

- Do not fire reminders during calendar meetings
- Defer non-urgent reminders if in focus/DND mode
- Batch low-priority reminders to designated check-in times
- Never fire reminders between 10 PM and 7 AM unless urgent
- Weekend reminders only fire for items tagged "weekend-ok"

### Snooze Strategy

| Snooze Count | Default Snooze Duration | Action |
|--------------|------------------------|--------|
| 1st snooze | 1 hour | Normal |
| 2nd snooze | 3 hours | Normal |
| 3rd snooze | Next day, same time | Prompt: "Still relevant?" |
| 4th snooze | N/A | Force decision: Do, Reschedule, or Delete |

### Reminder Fatigue Prevention

| Rule | Implementation |
|------|---------------|
| Max 5 reminders per hour | Queue excess, deliver at next slot |
| Max 15 reminders per day | Consolidate low-priority into daily digest |
| No identical reminders within 1 hour | Deduplicate |
| Recurring + snoozed = review | After 3 snoozes on a recurring item, suggest canceling |
| Stale reminders auto-archive | If snoozed 5+ times or 30 days old without action |

### Category-Specific Lead Times

#### Work Reminders

| Task Type | Lead Time | Reminder Count |
|-----------|-----------|---------------|
| Quick email reply (<5 min) | 1 hour | 1 |
| Document review (30 min) | 1 day | 2 (day before + morning of) |
| Presentation prep (2+ hours) | 3 days | 3 (3 days, 1 day, morning of) |
| Major deadline | 1 week | 4 (week, 3 days, 1 day, morning) |
| Quarterly review | 2 weeks | 3 (2 weeks, 1 week, 3 days) |

#### Personal Reminders

| Task Type | Lead Time | Reminder Count |
|-----------|-----------|---------------|
| Take medication | Exact time daily | 1 (with snooze enabled) |
| Doctor appointment | 1 day + 1 hour | 2 |
| Bill payment | 3 days before due | 2 (3 days, 1 day) |
| Birthday/Anniversary | 1 week + 1 day | 2 |
| Home maintenance | 1 day | 1 |
| Subscription renewal | 1 week | 2 (1 week, 2 days) |

### Integration Points

| System | Trigger Support | Action Support |
|--------|----------------|----------------|
| Google Calendar | Event-based triggers | Create events, send invites |
| Slack | Message triggers | Send DMs, channel posts |
| Email | Receive triggers | Send follow-up emails |
| Todoist/Asana | Task status triggers | Create/complete tasks |
| IFTTT/Zapier | Any webhook trigger | Any webhook action |
| iOS/Android | Location triggers | Push notifications |

### Metrics and Health

| Metric | Healthy Range | Action if Out of Range |
|--------|--------------|------------------------|
| Completion rate | >70% | Review if reminders are actionable |
| Snooze rate | <30% | Adjust timing or reduce volume |
| Active reminders | <25 | Archive stale, consolidate similar |
| Overdue count | <5 | Triage overdue items |
| Daily reminder count | 5-15 | Reduce if fatigue, increase if missing things |
