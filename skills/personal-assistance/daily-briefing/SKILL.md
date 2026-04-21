---
name: daily-briefing
description: Generate personalized daily summaries covering tasks, calendar, and priorities. Use when the user mentions "daily briefing," "morning summary," "daily digest," "day planner," "today's agenda," "daily overview," "morning routine," "daily priorities," "end-of-day review," or "daily recap."
metadata:
  version: 1.0.0
  category: personal-assistance
---

# Daily Briefing

Generate personalized daily summaries that cover tasks, calendar events, priorities, and contextual information to start or end each day with clarity.

## Purpose

Create structured daily briefings that consolidate information from multiple sources into a single, actionable summary. Covers morning briefings, priority highlighting, task rollover logic, and end-of-day reviews to maintain productivity and awareness.

## Quick Reference

### Briefing Components

| Component | Source | Priority | Time to Review |
|-----------|--------|----------|---------------|
| **Priority tasks** | Task manager | Critical | 2 minutes |
| **Calendar overview** | Calendar app | High | 1 minute |
| **Overdue/rolled items** | Task manager | High | 1 minute |
| **Email highlights** | Email inbox | Medium | 2 minutes |
| **Weather/commute** | Weather API, Maps | Low | 30 seconds |
| **News digest** | RSS/news API | Low | 2 minutes |
| **Daily goals** | User-defined | Critical | 1 minute |
| **Yesterday's carryover** | Prior briefing | Medium | 1 minute |

### Priority Classification

| Priority | Label | Criteria | Action |
|----------|-------|----------|--------|
| **P0** | Urgent + Important | Deadline today, high impact, blocked items | Do first |
| **P1** | Important | Due this week, significant outcomes | Schedule time block |
| **P2** | Standard | Regular tasks, ongoing projects | Batch process |
| **P3** | Low | Nice-to-have, no deadline | Defer or delegate |
| **P4** | Informational | FYI items, optional reading | Review if time |

## Workflow

### Morning Briefing Checklist

```
Morning Briefing Generation:
- [ ] Pull today's calendar events
- [ ] Identify tasks due today and overdue
- [ ] Flag rolled-over items from yesterday
- [ ] Classify all items by priority (P0-P4)
- [ ] Check for meeting prep needed (materials, agendas)
- [ ] Pull top 3 email threads requiring action
- [ ] Check weather and commute conditions
- [ ] Compile news headlines (optional)
- [ ] Set 3 daily focus goals
- [ ] Format and deliver briefing
```

## Templates

### Morning Briefing Template

```
╔══════════════════════════════════════════════════════════╗
║              DAILY BRIEFING                              ║
║              {{day_of_week}}, {{date}}                   ║
║              Good morning, {{name}}!                     ║
╠══════════════════════════════════════════════════════════╣

TODAY'S FOCUS (pick your top 3):
  1. {{focus_goal_1}}
  2. {{focus_goal_2}}
  3. {{focus_goal_3}}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CALENDAR ({{event_count}} events today)
  {{time_1}}  {{event_1}} {{location_1}}
              Prep: {{prep_notes_1}}
  {{time_2}}  {{event_2}} {{location_2}}
  {{time_3}}  {{event_3}} {{location_3}}

  Free blocks: {{free_block_1}}, {{free_block_2}}
  Total meeting time: {{meeting_hours}}h
  Focus time available: {{focus_hours}}h

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PRIORITY TASKS
  [P0] {{task_1}} — Due: {{due}} — {{context}}
  [P0] {{task_2}} — Due: {{due}} — {{context}}
  [P1] {{task_3}} — Due: {{due}} — {{context}}
  [P1] {{task_4}} — Due: {{due}} — {{context}}
  [P2] {{task_5}} — Due: {{due}} — {{context}}

OVERDUE / ROLLED OVER (from yesterday):
  [!] {{overdue_task_1}} — Originally due: {{original_due}}
  [!] {{overdue_task_2}} — Originally due: {{original_due}}
  Decision needed: Reschedule, delegate, or drop?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EMAIL HIGHLIGHTS ({{unread_count}} unread)
  Action Required:
    - {{email_1_sender}}: {{email_1_subject}} ({{urgency}})
    - {{email_2_sender}}: {{email_2_subject}} ({{urgency}})
  FYI:
    - {{email_3_sender}}: {{email_3_subject}}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CONDITIONS
  Weather: {{weather_summary}} | High: {{high_temp}} Low: {{low_temp}}
  Commute: {{commute_time}} ({{commute_status}})

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NEWS DIGEST (top 3 relevant):
  1. {{headline_1}} — {{source_1}}
  2. {{headline_2}} — {{source_2}}
  3. {{headline_3}} — {{source_3}}

╚══════════════════════════════════════════════════════════╝
```

### Calendar Summary Format

```
CALENDAR DETAIL: {{date}}

TIME BLOCKS:
┌──────────┬────────────────────────────────────────────────┐
│ 08:00 AM │ ░░░░░░░░ FOCUS TIME ░░░░░░░░                  │
│ 09:00 AM │ ████ {{meeting_1}} ({{duration}})              │
│ 09:30 AM │ ████ {{meeting_1}} continued                   │
│ 10:00 AM │ ░░░░░░░░ FOCUS TIME ░░░░░░░░                  │
│ 10:30 AM │ ░░░░░░░░ FOCUS TIME ░░░░░░░░                  │
│ 11:00 AM │ ████ {{meeting_2}} ({{duration}})              │
│ 11:30 AM │ ████ {{meeting_2}} continued                   │
│ 12:00 PM │ ░░░░░░░░ LUNCH ░░░░░░░░                       │
│ 01:00 PM │ ████ {{meeting_3}} ({{duration}})              │
│ 01:30 PM │ ░░░░░░░░ FOCUS TIME ░░░░░░░░                  │
│ 02:00 PM │ ░░░░░░░░ FOCUS TIME ░░░░░░░░                  │
│ 02:30 PM │ ░░░░░░░░ FOCUS TIME ░░░░░░░░                  │
│ 03:00 PM │ ████ {{meeting_4}} ({{duration}})              │
│ 03:30 PM │ ░░░░░░░░ FOCUS TIME ░░░░░░░░                  │
│ 04:00 PM │ ░░░░░░░░ FOCUS TIME ░░░░░░░░                  │
│ 04:30 PM │ ░░░░░░░░ FOCUS TIME ░░░░░░░░                  │
│ 05:00 PM │ END OF DAY                                     │
└──────────┴────────────────────────────────────────────────┘

MEETING PREP NEEDED:
- {{meeting_1}}: Review {{document}}, prepare {{deliverable}}
- {{meeting_3}}: Send agenda to {{attendees}}

CONFLICTS: {{conflict_description}} or "None detected"
```

### Task Rollover Logic

```
TASK ROLLOVER RULES:

At end of day, uncompleted tasks are processed as follows:

IF task is P0 (urgent + important):
  → Auto-roll to tomorrow as P0
  → Flag as "carried over" with original due date
  → Alert: "Critical task rolled over — needs attention"

IF task is P1 (important):
  → Roll to tomorrow as P1 (first rollover)
  → Escalate to P0 if rolled over 2+ days
  → Prompt: "Still relevant? Reschedule or delegate?"

IF task is P2 (standard):
  → Roll to tomorrow as P2 (first rollover)
  → After 3 rollovers: prompt to reschedule or drop
  → "This task has been deferred 3 times. Reschedule to {{suggested_date}}?"

IF task is P3/P4 (low/informational):
  → Do not auto-roll
  → Move to "someday/maybe" after 5 days
  → Weekly review prompt

ROLLOVER LIMITS:
- Maximum 5 rolled items per day (prevents list bloat)
- Items rolled 5+ times trigger "stuck task" review
- Weekend rollovers batch to Monday
```

### End-of-Day Review Template

```
╔══════════════════════════════════════════════════════════╗
║              END-OF-DAY REVIEW                           ║
║              {{day_of_week}}, {{date}}                   ║
╠══════════════════════════════════════════════════════════╣

TODAY'S SCORECARD:
  Focus Goals Completed: {{completed}}/3
  Tasks Completed: {{tasks_done}}/{{tasks_total}}
  Meetings Attended: {{meetings_attended}}/{{meetings_total}}

COMPLETED:
  [x] {{completed_task_1}}
  [x] {{completed_task_2}}
  [x] {{completed_task_3}}

NOT COMPLETED (rolling to tomorrow):
  [ ] {{incomplete_1}} — Reason: {{reason}} — New due: {{new_due}}
  [ ] {{incomplete_2}} — Reason: {{reason}} — New due: {{new_due}}

WINS:
  - {{win_1}}
  - {{win_2}}

BLOCKERS:
  - {{blocker_1}} — Action: {{action}}
  - {{blocker_2}} — Action: {{action}}

TOMORROW'S TOP PRIORITIES:
  1. {{tomorrow_priority_1}}
  2. {{tomorrow_priority_2}}
  3. {{tomorrow_priority_3}}

NOTES / IDEAS:
  {{freeform_notes}}

╚══════════════════════════════════════════════════════════╝
```

### Integration Points

| Integration | Data Pulled | API/Method |
|-------------|------------|------------|
| **Google Calendar** | Events, free/busy, attendees | Google Calendar API |
| **Outlook** | Events, tasks, flags | Microsoft Graph API |
| **Todoist/Asana** | Tasks, due dates, projects | REST API |
| **Gmail/Outlook Mail** | Unread count, flagged emails | IMAP or API |
| **Weather** | Forecast, alerts | OpenWeather API |
| **Maps/Commute** | Travel time, delays | Google Maps API |
| **RSS/News** | Headlines by topic | RSS feeds |
| **Slack** | Unread mentions, DMs | Slack API |

## Scripts & Tools

**generate_briefing.py**: Create morning briefing from connected sources
```bash
python scripts/generate_briefing.py --user {{user_id}} --format markdown
# Output: Formatted daily briefing with all components
```

**end_of_day_review.py**: Generate end-of-day summary
```bash
python scripts/end_of_day_review.py --user {{user_id}} --date today
# Output: Completed tasks, rollover items, tomorrow's preview
```

**rollover_tasks.py**: Process task rollovers automatically
```bash
python scripts/rollover_tasks.py --user {{user_id}} --apply-rules
# Output: Tasks rolled over with priority adjustments
```

**configure_briefing.py**: Set up briefing preferences
```bash
python scripts/configure_briefing.py --components calendar,tasks,email,weather
# Output: Saved briefing configuration
```

## Best Practices

1. **Consistent timing** - Deliver morning briefing at the same time daily (15 min before work start)
2. **Three focus goals maximum** - More than three dilutes attention
3. **Flag, don't list everything** - Surface exceptions and priorities, not the full task list
4. **Review in under 5 minutes** - If it takes longer, trim the content
5. **Include free time blocks** - Knowing when you have focus time is as important as meetings
6. **Weekly reset** - Every Monday, clear rolled-over items with a deliberate review
7. **End-of-day closes the loop** - Capture what happened while it is fresh
8. **Customize over time** - Start with all components, then remove what you skip reading

## Related Skills

- Task management: `task-prioritizer`
- Email processing: `email-organizer`
- Meeting notes: `meeting-summarizer`
- Calendar management: `meeting-scheduler`
