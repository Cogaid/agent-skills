# Reminder Manager

---
name: reminder-manager
description: Create and manage reminders, follow-ups, and time-sensitive notifications. Use when user mentions "remind me," "set a reminder," "follow up," "don't forget," "remind me to," "schedule reminder," or "notify me when."
metadata:
  version: 1.0.0
  category: personal-assistance
---

## Purpose

Create effective reminders that ensure nothing falls through the cracks while avoiding reminder fatigue.

## Quick Reference

### Reminder Types

| Type | Trigger | Example |
|------|---------|---------|
| Time-based | Specific date/time | "Remind me at 3pm" |
| Recurring | Regular interval | "Every Monday at 9am" |
| Location-based | Arriving/leaving place | "When I get to office" |
| Event-based | Before/after event | "1 hour before meeting" |
| Condition-based | When X happens | "When John replies" |
| Follow-up | After waiting period | "If no response in 3 days" |

### Priority Levels

| Priority | Response Time | Examples |
|----------|---------------|----------|
| Urgent | Within hours | Time-sensitive deadlines |
| High | Same day | Important tasks |
| Normal | Within 1-2 days | Regular follow-ups |
| Low | Flexible | Nice-to-have actions |

## Reminder Templates

### Simple Reminder

```
📝 REMINDER
━━━━━━━━━━━━━━━━━━━━

What: [Action/Task]
When: [Date/Time]
Why: [Context/Reason]

[Additional details if needed]
```

### Follow-up Reminder

```
🔔 FOLLOW-UP REMINDER
━━━━━━━━━━━━━━━━━━━━

Original action: [What you did]
Date sent/done: [Date]
Waiting for: [Person/Response]
Days elapsed: [X] days

Suggested action:
[Follow-up template or action]
```

### Recurring Reminder

```
🔁 RECURRING REMINDER
━━━━━━━━━━━━━━━━━━━━

What: [Task]
Frequency: [Daily/Weekly/Monthly]
Next occurrence: [Date]

Checklist:
□ [Step 1]
□ [Step 2]
□ [Step 3]

Last completed: [Date]
```

### Deadline Reminder

```
⏰ DEADLINE APPROACHING
━━━━━━━━━━━━━━━━━━━━

Task: [What's due]
Deadline: [Date/Time]
Time remaining: [X days/hours]

Status: [Not started / In progress / Almost done]

Next steps:
1. [Step 1]
2. [Step 2]
```

## Reminder Categories

### Work Reminders

| Category | Examples | Default Lead Time |
|----------|----------|-------------------|
| Meetings | Prep, join, follow-up | 15 min / 1 day |
| Deadlines | Projects, reports | 3 days / 1 day |
| Follow-ups | Emails, calls | 3-5 days |
| Recurring | Reports, check-ins | Based on schedule |
| Manager | 1:1 prep, updates | 1 day |

### Personal Reminders

| Category | Examples | Default Lead Time |
|----------|----------|-------------------|
| Health | Appointments, meds | 1 day |
| Finance | Bills, taxes | 1 week |
| Social | Birthdays, events | 1 week |
| Home | Maintenance, errands | Same day |
| Self-care | Exercise, breaks | As scheduled |

### Follow-up Reminders

| Scenario | Wait Time | Action |
|----------|-----------|--------|
| No email reply | 3 days | Follow-up email |
| Sales outreach | 2-3 days | Second touch |
| Meeting request | 2 days | Gentle nudge |
| Invoice unpaid | 7 days | Payment reminder |
| Proposal sent | 3-5 days | Check-in |

## Smart Reminder Rules

### Lead Time Guidelines

| Task Type | Minimum Lead Time |
|-----------|-------------------|
| Quick task (<15 min) | 1 hour |
| Medium task (1-2 hours) | 1 day |
| Complex task (half day+) | 3 days |
| Project milestone | 1 week |
| Major deadline | 2 weeks |

### Escalation Patterns

```
If No Response After:

Day 1: Wait
Day 3: Gentle follow-up
Day 7: More direct follow-up
Day 14: Final attempt + escalate
Day 21: Close loop or pause
```

### Time-of-Day Rules

| Reminder Type | Best Time |
|---------------|-----------|
| Morning tasks | 8-9 AM |
| Work priorities | After daily standup |
| Personal errands | Lunch or end of day |
| Weekend tasks | Saturday morning |
| End-of-week reviews | Friday 3-4 PM |

## Workflow

### Setting a Reminder

```
1. WHAT: Be specific
   ❌ "Follow up with client"
   ✅ "Send proposal to John at Acme re: Q2 project"

2. WHEN: Set appropriate time
   - Consider their timezone
   - Choose productive hours
   - Allow buffer time

3. WHY: Add context
   - What was the original conversation?
   - What's the goal?
   - What info do you need?

4. PRIORITY: Set importance
   - How critical is the timing?
   - What's the consequence of missing?
```

### Managing Reminders

```
Daily Review:
□ Check today's reminders
□ Reschedule if needed
□ Mark complete or snooze

Weekly Review:
□ Review upcoming week
□ Adjust lead times
□ Clear stale reminders
□ Set new follow-ups
```

## Communication Templates

### Follow-up Email

```
Subject: Following up - [Topic]

Hi [Name],

I wanted to follow up on [topic] from [date/context].

[Brief reminder of what was discussed/sent]

Do you have any questions, or would you like to move forward?

Happy to jump on a quick call if that's easier.

Best,
[Name]
```

### Gentle Nudge

```
Subject: Re: [Original Subject]

Hi [Name],

Just bubbling this up - I know things get busy.

Let me know if you need anything from my end.

[Name]
```

### Final Follow-up

```
Subject: Should I close this out? - [Topic]

Hi [Name],

I've reached out a few times about [topic] but haven't heard back.

I'll assume the timing isn't right and close this out for now.

If things change, just let me know - happy to reconnect.

Best,
[Name]
```

## Reminder Organization

### Categorization System

```
Work:
├── Meetings
│   ├── Prep reminders
│   └── Follow-up reminders
├── Projects
│   ├── Milestone reminders
│   └── Deadline reminders
├── People
│   ├── Manager
│   ├── Direct reports
│   └── Clients
└── Admin
    ├── Reports
    └── Compliance

Personal:
├── Health
├── Finance
├── Social
└── Home
```

### Status Labels

| Label | Meaning |
|-------|---------|
| Pending | Not yet due |
| Due Today | Action needed today |
| Overdue | Past due date |
| Snoozed | Postponed |
| Recurring | Will repeat |
| Complete | Done |

## Best Practices

### Do
- Be specific about the action
- Include context/why
- Set appropriate lead time
- Review reminders regularly
- Snooze strategically
- Complete or delete promptly

### Don't
- Create vague reminders
- Over-remind (reminder fatigue)
- Ignore overdue items
- Set unrealistic timing
- Forget to mark complete
- Keep stale reminders

## Scripts & Tools

| Script | Purpose |
|--------|---------|
| `scripts/reminder_manager.py` | Create and manage reminders |
| `scripts/followup_tracker.py` | Track follow-up sequences |

## Reference

→ See `templates/reminder_templates.md` for all formats
→ See `reference.md` for automation ideas
