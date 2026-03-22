---
name: task-prioritizer
description: Prioritizes tasks and manages workload using proven frameworks. Use when the user mentions "prioritize tasks," "too many things to do," "overwhelmed," "what should I focus on," "todo list," "urgent vs important," "Eisenhower matrix," or "time management."
metadata:
  version: 1.1.0
  category: personal-assistance
---

# Task Prioritizer

Prioritize tasks effectively using proven frameworks to focus on what matters most.

## Quick Start

1. **Brain dump**: List everything on your mind
2. **Apply framework**: Run `python scripts/prioritize.py --interactive`
3. **Score tasks**: Use ICE or Eisenhower
4. **Create today's list**: Maximum 3 priorities
5. **Time block**: Assign specific times to top tasks

## Prioritization Workflow

```
Progress:
- [ ] Step 1: Write down ALL tasks (brain dump)
- [ ] Step 2: Clarify each task (what does "done" look like?)
- [ ] Step 3: Apply Eisenhower matrix (urgent vs important)
- [ ] Step 4: Score with ICE if needed (impact/confidence/ease)
- [ ] Step 5: Select top 3 for today
- [ ] Step 6: Time block the top 3
- [ ] Step 7: Start with #1 (don't skip around)
```

## Eisenhower Matrix

```
              URGENT              NOT URGENT
        ┌──────────────────┬──────────────────┐
        │    DO FIRST      │    SCHEDULE      │
IMPORTANT│   Crises,        │   Planning,      │
        │   Deadlines      │   Learning       │
        ├──────────────────┼──────────────────┤
        │    DELEGATE      │    ELIMINATE     │
NOT     │   Interruptions,  │   Time wasters,  │
IMPORTANT│   Some meetings  │   Busywork       │
        └──────────────────┴──────────────────┘
```

## Quick Decision Rules

- **2-Minute Rule**: Takes <2 minutes? Do it now
- **3-Task Rule**: Max 3 must-do items per day
- **Tomorrow Test**: "Will this matter tomorrow?" If no, skip
- **Default No**: Say no unless compelling reason to say yes

## Utility Scripts

**prioritize.py**: Score and sort tasks
```bash
python scripts/prioritize.py --interactive
python scripts/prioritize.py --tasks tasks.json
# Output: Prioritized task list with scores
```

**eisenhower.py**: Categorize tasks by urgency/importance
```bash
python scripts/eisenhower.py --tasks "Task 1, Task 2, Task 3" --interactive
# Output: Tasks sorted into 4 quadrants
```

**weekly_plan.py**: Generate weekly priorities
```bash
python scripts/weekly_plan.py --goals "Finish report, Prep presentation"
# Output: Weekly plan with daily breakdown
```

## When Overwhelmed

1. **Stop** - Take a breath
2. **List** - Get everything on paper
3. **Triage** - What's truly due TODAY?
4. **Pick one** - Start with just one task
5. **Complete it** - Momentum builds confidence
6. **Repeat** - One task at a time

## Resources

- **Full framework guide**: [reference.md](reference.md)
- **Weekly planning template**: [templates/weekly.md](templates/weekly.md)
- **Daily planning template**: [templates/daily.md](templates/daily.md)
- **Delegation template**: [templates/delegate.md](templates/delegate.md)

## Related Skills

- Scheduling prioritized meetings: `meeting-scheduler`
- Writing priority emails: `email-drafting`
- Prioritizing travel prep: `travel-planner`
