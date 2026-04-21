# Morning Briefing Template

## Usage

Fill in the placeholders (marked with `{{ }}`) to generate a personalized morning briefing. Use `generate_briefing.py` to auto-populate from connected sources.

---

```
======================================================================
              DAILY BRIEFING
              {{day_of_week}}, {{date}}
              Good morning, {{name}}!
======================================================================

TODAY'S FOCUS (pick your top 3):
  1. {{focus_goal_1}}
  2. {{focus_goal_2}}
  3. {{focus_goal_3}}

----------------------------------------------------------------------

CALENDAR ({{event_count}} events today)

  {{time_1}}  {{event_1}}
              Location: {{location_1}}
              Prep: {{prep_notes_1}}

  {{time_2}}  {{event_2}}
              Location: {{location_2}}

  {{time_3}}  {{event_3}}
              Location: {{location_3}}

  Free blocks: {{free_block_1}}, {{free_block_2}}
  Total meeting time: {{meeting_hours}}h
  Focus time available: {{focus_hours}}h

----------------------------------------------------------------------

PRIORITY TASKS

  [P0] {{task_p0_1}} -- Due: {{due_1}} -- {{context_1}}
  [P0] {{task_p0_2}} -- Due: {{due_2}} -- {{context_2}}
  [P1] {{task_p1_1}} -- Due: {{due_3}} -- {{context_3}}
  [P1] {{task_p1_2}} -- Due: {{due_4}} -- {{context_4}}
  [P2] {{task_p2_1}} -- Due: {{due_5}} -- {{context_5}}

OVERDUE / ROLLED OVER (from yesterday):
  [!] {{overdue_task_1}} -- Originally due: {{original_due_1}}
  [!] {{overdue_task_2}} -- Originally due: {{original_due_2}}
  Decision needed: Reschedule, delegate, or drop?

----------------------------------------------------------------------

EMAIL HIGHLIGHTS ({{unread_count}} unread)

  Action Required:
    - {{email_1_sender}}: {{email_1_subject}} ({{urgency_1}})
    - {{email_2_sender}}: {{email_2_subject}} ({{urgency_2}})

  FYI:
    - {{email_3_sender}}: {{email_3_subject}}

----------------------------------------------------------------------

CONDITIONS
  Weather: {{weather_summary}} | High: {{high_temp}} Low: {{low_temp}}
  Commute: {{commute_time}} ({{commute_status}})

----------------------------------------------------------------------

NEWS DIGEST (top 3 relevant):
  1. {{headline_1}} -- {{source_1}}
  2. {{headline_2}} -- {{source_2}}
  3. {{headline_3}} -- {{source_3}}

======================================================================
```

## Customization Notes

- Remove sections you do not use by deleting the block between dividers
- Weather and News are optional; disable in config with `--components`
- Free blocks are calculated by subtracting meetings from working hours (default 8am-5pm)
- Priority tasks are sorted by P-level then due date
- Overdue section only appears when rolled items exist
