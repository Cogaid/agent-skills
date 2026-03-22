---
name: meeting-scheduler
description: Schedules, coordinates, and manages meetings across time zones. Use when the user mentions "schedule meeting," "find time," "set up call," "book appointment," "coordinate calendars," "availability," "reschedule," "meeting invite," or "time zone."
metadata:
  version: 1.1.0
  category: personal-assistance
---

# Meeting Scheduler

Schedule and coordinate meetings efficiently across time zones and busy calendars.

## Quick Start

1. **Check if meeting needed**: Could this be async?
2. **Gather requirements**: Run `python scripts/meeting_planner.py --interactive`
3. **Find overlap**: Run `python scripts/timezone_converter.py`
4. **Create invite**: Use [templates/invite.md](templates/invite.md)
5. **Send and confirm**: Get explicit acceptance

## Scheduling Workflow

```
Progress:
- [ ] Step 1: Confirm meeting is necessary (not an email)
- [ ] Step 2: Identify required vs optional attendees
- [ ] Step 3: Determine duration (default shorter)
- [ ] Step 4: Check availability across time zones
- [ ] Step 5: Propose 2-3 specific options
- [ ] Step 6: Get confirmation
- [ ] Step 7: Send calendar invite with agenda
- [ ] Step 8: Add video link and pre-work
```

## Meeting Duration Guide

| Meeting Type | Suggested Duration |
|--------------|-------------------|
| Quick sync | 15 min |
| Status update | 25 min |
| Decision meeting | 30-50 min |
| Brainstorm | 45-60 min |
| Workshop | 90 min max |

**Rule**: Most 1-hour meetings can be 30 min. Most 30-min can be 15.

## Before Scheduling, Ask

1. **Is this a meeting?** Could it be email, Slack, or Loom?
2. **Who must attend?** Required vs Optional vs FYI
3. **What's the outcome?** Decision, alignment, brainstorm?
4. **What's the deadline?** When must this be scheduled by?

## Utility Scripts

**meeting_planner.py**: Plan meeting logistics
```bash
python scripts/meeting_planner.py --attendees "john@co.com,jane@co.com" --duration 30
# Output: Recommended times based on typical availability
```

**timezone_converter.py**: Convert times across zones
```bash
python scripts/timezone_converter.py --time "10:00 AM" --from-tz "America/New_York" --to-tz "Europe/London,Asia/Tokyo"
# Output: Equivalent times in each zone
```

**check_overlap.py**: Find overlap windows for global teams
```bash
python scripts/check_overlap.py --zones "PT,ET,CET,IST"
# Output: Best overlap windows
```

## Resources

- **Full scheduling guide**: [reference.md](reference.md)
- **Calendar invite templates**: [templates/invite.md](templates/invite.md)
- **Reschedule/cancel templates**: [templates/changes.md](templates/changes.md)
- **Meeting type examples**: [templates/agendas.md](templates/agendas.md)

## Related Skills

- Follow-up emails: `email-drafting`
- Prioritizing meetings: `task-prioritizer`
- Travel meeting coordination: `travel-planner`
