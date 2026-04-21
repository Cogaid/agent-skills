# Daily Briefing - Reference Guide

## Priority Classification Framework

### Eisenhower Matrix Integration

The P0-P4 priority system maps to the Eisenhower Matrix:

| Priority | Eisenhower Quadrant | Description |
|----------|---------------------|-------------|
| P0 | Q1: Urgent + Important | Crisis items, deadline today, blocked dependencies |
| P1 | Q2: Important, Not Urgent | Strategic work, due this week, high-value outcomes |
| P2 | Q3: Urgent, Not Important | Regular tasks, admin, ongoing maintenance |
| P3 | Q4: Not Urgent, Not Important | Nice-to-have, no deadline, low impact |
| P4 | Informational | FYI only, optional reading, newsletters |

### Priority Scoring Algorithm

Calculate priority score for each item:

```
Score = (Deadline_Urgency x 0.35) + (Impact x 0.30) + (Dependency_Count x 0.20) + (Effort_Inverse x 0.15)

Deadline_Urgency:
  5 = Due today or overdue
  4 = Due tomorrow
  3 = Due this week
  2 = Due this month
  1 = No deadline

Impact:
  5 = Revenue/customer affecting
  4 = Team-blocking
  3 = Individual productivity
  2 = Minor improvement
  1 = Informational only

Dependency_Count:
  5 = 4+ people/tasks blocked by this
  4 = 3 people/tasks blocked
  3 = 2 people/tasks blocked
  2 = 1 person/task blocked
  1 = No dependencies

Effort_Inverse (favor quick wins):
  5 = Under 15 minutes
  4 = 15-30 minutes
  3 = 30-60 minutes
  2 = 1-3 hours
  1 = 3+ hours
```

### Priority to Action Mapping

| Score Range | Priority | Action | Time Block |
|-------------|----------|--------|------------|
| 4.0 - 5.0 | P0 | Do immediately, first thing | First 30 min |
| 3.0 - 3.9 | P1 | Schedule a focus block today | Morning focus |
| 2.0 - 2.9 | P2 | Batch process during low-energy time | Afternoon |
| 1.0 - 1.9 | P3 | Defer to end of week or delegate | Friday batch |
| 0.0 - 0.9 | P4 | Review only if time permits | Optional |

## Task Rollover Logic - Detailed Rules

### Rollover State Machine

```
States: ACTIVE -> ROLLED_1 -> ROLLED_2 -> ROLLED_3 -> ESCALATED -> STUCK -> ARCHIVED

Transitions:
  ACTIVE + not completed at EOD -> ROLLED_1
  ROLLED_1 + not completed at EOD -> ROLLED_2 (P2+ escalate priority)
  ROLLED_2 + not completed at EOD -> ROLLED_3 (prompt: reschedule/delegate/drop)
  ROLLED_3 + not completed at EOD -> ESCALATED (auto-notify manager for P0/P1)
  ESCALATED + 2 more days -> STUCK (mandatory review)
  STUCK + user action -> ARCHIVED or rescheduled as new task
```

### Rollover Priority Escalation

| Original Priority | After 1 Rollover | After 2 Rollovers | After 3 Rollovers |
|-------------------|------------------|--------------------|--------------------|
| P0 | P0 (flagged) | P0 (alert sent) | P0 (escalate to manager) |
| P1 | P1 | P0 | P0 (alert sent) |
| P2 | P2 | P1 | P0 |
| P3 | P3 | P3 | Moved to someday/maybe |
| P4 | Dropped | - | - |

### Weekend and Holiday Handling

- Friday EOD rollovers batch to Monday morning
- Holiday rollovers batch to next business day
- Weekend tasks tagged `weekend-ok` can appear on Saturday/Sunday briefings
- Vacation mode: all rollovers freeze, batch to return date

## Briefing Customization

### Component Toggle Matrix

| Component | Default | Can Disable | Requires Integration |
|-----------|---------|-------------|---------------------|
| Priority tasks | ON | No | Task manager |
| Calendar | ON | No | Calendar API |
| Overdue items | ON | No | Task manager |
| Email highlights | ON | Yes | Email API |
| Weather | OFF | Yes | Weather API |
| Commute | OFF | Yes | Maps API |
| News digest | OFF | Yes | RSS feeds |
| Daily goals | ON | Yes | None (manual) |
| Yesterday carryover | ON | No | Prior briefing |
| Slack mentions | OFF | Yes | Slack API |

### Time-of-Day Variants

| Variant | Trigger | Components Emphasized |
|---------|---------|----------------------|
| Early morning (6-8 AM) | Auto | Weather, commute, calendar overview |
| Standard morning (8-10 AM) | Default | Full briefing, all components |
| Late start (after 10 AM) | Auto | Priority tasks only, missed items flagged |
| Mid-day catch-up | Manual | New items since morning, calendar remainder |
| End-of-day review | Manual/scheduled | Completed items, rollovers, tomorrow preview |
| Weekend | Saturday 9 AM | Personal tasks only, week-ahead preview |

## Integration Reference

### Google Calendar API

```
Endpoint: https://www.googleapis.com/calendar/v3
Auth: OAuth 2.0
Scopes: calendar.readonly, calendar.events.readonly

Key endpoints:
  GET /calendars/{calendarId}/events
    - timeMin: start of day (ISO 8601)
    - timeMax: end of day (ISO 8601)
    - singleEvents: true
    - orderBy: startTime

  GET /freeBusy
    - timeMin/timeMax for free block detection
```

### Todoist API

```
Endpoint: https://api.todoist.com/rest/v2
Auth: Bearer token

Key endpoints:
  GET /tasks
    - filter: "today | overdue"
    - Returns: task content, due date, priority, labels

  GET /tasks?filter=assigned to: me & due before: tomorrow
    - For rollover detection
```

### OpenWeather API

```
Endpoint: https://api.openweathermap.org/data/3.0
Auth: API key

Key endpoint:
  GET /onecall
    - lat, lon: user location
    - exclude: minutely,alerts
    - units: imperial or metric
    - Returns: current, hourly, daily forecasts
```

## Delivery Channels

| Channel | Format | Best For |
|---------|--------|----------|
| Email | HTML or Markdown | Async review, archivable |
| Slack DM | Markdown with blocks | Quick glance, mobile |
| Terminal | Plain text / ANSI | Developer workflow |
| Dashboard | JSON -> rendered HTML | Always-on display |
| Push notification | Short summary + link | Time-sensitive alerts |

## Metrics and Tracking

### Briefing Effectiveness Metrics

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Briefing read rate | >90% | Open/view tracking |
| Time to review | <5 minutes | Self-reported or timer |
| Tasks completed vs. planned | >70% | EOD review comparison |
| Rollover rate | <20% | Rolled items / total items |
| Focus goal completion | 2/3 daily | EOD review tracking |
| Briefing customization actions | Decreasing over time | Config change frequency |
