# End-of-Day Review Template

## Usage

Complete this template at the end of each work day. Use `end_of_day_review.py` to auto-populate task completion data from connected sources.

---

```
======================================================================
              END-OF-DAY REVIEW
              {{day_of_week}}, {{date}}
======================================================================

TODAY'S SCORECARD:
  Focus Goals Completed: {{completed_goals}}/3
  Tasks Completed: {{tasks_done}}/{{tasks_total}}
  Meetings Attended: {{meetings_attended}}/{{meetings_total}}
  Emails Processed: {{emails_processed}}

----------------------------------------------------------------------

COMPLETED TODAY:
  [x] {{completed_task_1}}
  [x] {{completed_task_2}}
  [x] {{completed_task_3}}
  [x] {{completed_task_4}}

NOT COMPLETED (rolling to tomorrow):
  [ ] {{incomplete_1}} -- Reason: {{reason_1}} -- New priority: {{new_priority_1}}
  [ ] {{incomplete_2}} -- Reason: {{reason_2}} -- New priority: {{new_priority_2}}

----------------------------------------------------------------------

WINS:
  - {{win_1}}
  - {{win_2}}

BLOCKERS:
  - {{blocker_1}} -- Action: {{blocker_action_1}}
  - {{blocker_2}} -- Action: {{blocker_action_2}}

LESSONS LEARNED:
  - {{lesson_1}}

----------------------------------------------------------------------

TOMORROW'S TOP PRIORITIES:
  1. {{tomorrow_priority_1}}
  2. {{tomorrow_priority_2}}
  3. {{tomorrow_priority_3}}

PREP NEEDED FOR TOMORROW:
  - {{prep_item_1}}
  - {{prep_item_2}}

----------------------------------------------------------------------

NOTES / IDEAS:
  {{freeform_notes}}

======================================================================
```

## Rollover Rules Applied

Tasks not completed are processed according to rollover logic:

- **P0 tasks**: Auto-rolled as P0, flagged as carried over
- **P1 tasks**: Rolled as P1 (first time) or escalated to P0 (2+ rollovers)
- **P2 tasks**: Rolled as P2 with reschedule prompt after 3 rollovers
- **P3/P4 tasks**: Not auto-rolled; moved to someday/maybe after 5 days

## Weekly Pattern

- **Monday**: Include week-ahead preview, clear weekend rollovers
- **Tuesday-Thursday**: Standard review
- **Friday**: Add weekly summary stats, clear stale items, set Monday priorities
