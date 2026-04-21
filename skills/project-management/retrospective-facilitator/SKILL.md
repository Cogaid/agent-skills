---
name: retrospective-facilitator
description: Facilitate and summarize sprint retrospectives with structured formats and action tracking. Use when user mentions "retrospective," "retro," "sprint retro," "start stop continue," "what went well," "lessons learned," "team improvement."
metadata:
  version: 1.0.0
  category: project-management
---

# Retrospective Facilitator

Run structured sprint retrospectives, capture insights, and track improvement actions across iterations.

## Purpose

Retrospectives are the engine of continuous improvement in agile teams. Without structure and follow-through, they devolve into venting sessions or get skipped entirely. This skill provides multiple facilitation formats, templates for capturing outcomes, workflows for tracking action items, and techniques for keeping retros engaging and productive over time.

## Quick Reference

### Retro Format Selector

| Format | Best For | Duration | Team Size | Energy Level |
|--------|----------|----------|-----------|-------------|
| Start-Stop-Continue | Quick check-in, new teams | 30-45 min | 3-8 | Low-Medium |
| 4Ls (Liked, Learned, Lacked, Longed For) | Balanced reflection | 45-60 min | 4-10 | Medium |
| Sailboat | Visual teams, stale retros | 45-60 min | 4-12 | Medium-High |
| Mad-Sad-Glad | Emotional check-in, after tough sprints | 30-45 min | 3-8 | Medium |
| Timeline | Long sprints, many events | 60-90 min | 5-12 | High |
| Starfish (More/Less/Keep/Start/Stop) | Nuanced feedback, mature teams | 45-60 min | 4-10 | Medium |

### Facilitation Timeline

| Phase | Activity | Duration | Facilitator Action |
|-------|----------|----------|--------------------|
| Opening | Set the stage, safety check | 5 min | Welcome, ground rules, icebreaker |
| Data Gathering | Individual brainstorming | 10 min | Silent writing on sticky notes / cards |
| Grouping | Cluster similar items | 5-10 min | Group reads and organizes themes |
| Discussion | Discuss top themes | 15-25 min | Dot-vote to prioritize, discuss top 3-5 |
| Action Items | Define improvements | 10 min | SMART actions with owners and deadlines |
| Closing | Wrap up, feedback on retro | 5 min | Thank team, share summary plan |

## Workflow

### Pre-Retro Preparation

1. **Choose the format** based on team needs (use the selector above)
2. **Book the room/call** for the full duration plus 10 min buffer
3. **Prepare the board** (physical or digital: Miro, FigJam, Retrium)
4. **Gather sprint data** to share at the start:
   - Velocity and burndown
   - Stories completed vs. planned
   - Blocker count and resolution time
   - Action items from last retro (were they done?)
5. **Send a reminder** 1 day before with the format and any pre-work

### During the Retro

**Ground Rules (share at the start of every retro):**
- What is said in retro stays in retro (psychological safety)
- No blame - focus on systems and processes, not individuals
- Everyone participates - no spectators
- Be specific - examples help more than generalities
- We commit to acting on at least one improvement

### Retro Format Details

#### Format 1: Start-Stop-Continue

Three columns for capturing team feedback:

```
┌─────────────────┬─────────────────┬─────────────────┐
│     START        │      STOP       │    CONTINUE     │
│  (New things     │  (Things that   │  (Things that   │
│   we should      │   aren't        │   are working   │
│   try)           │   working)      │   well)         │
├─────────────────┼─────────────────┼─────────────────┤
│ - Pair on        │ - Skipping      │ - Daily code    │
│   complex bugs   │   code reviews  │   reviews       │
│ - Document       │ - Late standup  │ - Sprint demos  │
│   decisions in   │   starts        │   to stakeholders│
│   ADRs           │ - Overloading   │ - Friday        │
│                  │   sprint        │   knowledge     │
│                  │                 │   sharing       │
└─────────────────┴─────────────────┴─────────────────┘
```

#### Format 2: 4Ls (Liked, Learned, Lacked, Longed For)

```
┌─────────────────┬─────────────────┐
│     LIKED        │    LEARNED      │
│  What went well? │  What did we    │
│                  │  discover?      │
├─────────────────┼─────────────────┤
│ - Great team     │ - New testing   │
│   collaboration  │   framework     │
│ - Client loved   │ - Better way to │
│   the demo       │   handle errors │
├─────────────────┼─────────────────┤
│     LACKED       │   LONGED FOR    │
│  What was        │  What do we     │
│  missing?        │  wish we had?   │
├─────────────────┼─────────────────┤
│ - Clear design   │ - Automated     │
│   specs early    │   deployment    │
│ - Time for       │ - Dedicated QA  │
│   tech debt      │   environment   │
└─────────────────┴─────────────────┘
```

#### Format 3: Sailboat

A visual metaphor where the team is a sailboat:

```
        ☀ ISLAND (Goal/Vision)
        What are we sailing toward?
        "Ship the MVP by June 1"

  ⛵ SAILBOAT (The Team)

  💨 WIND (Helping us)           ⚓ ANCHOR (Slowing us down)
  - Strong QA process            - Manual deployments
  - Good team communication      - Unclear priorities
  - Helpful product owner        - Technical debt in auth module

  🪨 ROCKS (Risks ahead)
  - Key developer PTO in May
  - Third-party API deprecation
  - Client stakeholder change
```

#### Format 4: Mad-Sad-Glad

Emotion-based categories for honest reflection:

```
┌─────────────────┬─────────────────┬─────────────────┐
│      MAD         │      SAD        │      GLAD       │
│  (Frustrated     │  (Disappointed  │  (Happy about,  │
│   about)         │   about)        │   grateful for) │
├─────────────────┼─────────────────┼─────────────────┤
│ - Repeated       │ - Missed the    │ - Zero          │
│   context        │   sprint goal   │   production    │
│   switching      │ - Lost a team   │   incidents     │
│ - Requirements   │   member        │ - Great         │
│   changing       │ - Technical     │   mentoring     │
│   mid-sprint     │   debt growing  │   from seniors  │
│                  │                 │ - Client        │
│                  │                 │   feedback was   │
│                  │                 │   positive       │
└─────────────────┴─────────────────┴─────────────────┘
```

### Post-Retro Follow-Up Workflow

1. **Within 1 hour:** Post retro summary to team channel
2. **Within 24 hours:** Create tickets for action items in the backlog
3. **Next sprint planning:** Include retro action items in sprint backlog
4. **Next retro opening:** Review action item completion status
5. **Monthly:** Review improvement trends across retros

## Templates

### Retro Summary Template

```markdown
## Sprint [N] Retrospective Summary

**Date:** [Date]
**Facilitator:** [Name]
**Attendees:** [Names] ([X]/[Y] team members)
**Format Used:** [Start-Stop-Continue / 4Ls / Sailboat / Mad-Sad-Glad]
**Duration:** [X] minutes

### Top Themes (by vote count)

1. **[Theme 1]** (8 votes)
   - [Specific feedback item]
   - [Specific feedback item]
   - **Discussion notes:** [Key points from the conversation]

2. **[Theme 2]** (6 votes)
   - [Specific feedback item]
   - [Specific feedback item]
   - **Discussion notes:** [Key points from the conversation]

3. **[Theme 3]** (4 votes)
   - [Specific feedback item]
   - **Discussion notes:** [Key points from the conversation]

### What Went Well
- [Positive item 1]
- [Positive item 2]
- [Positive item 3]

### What Needs Improvement
- [Improvement area 1]
- [Improvement area 2]
- [Improvement area 3]

### Action Items

| # | Action | Owner | Deadline | Priority | Ticket |
|---|--------|-------|----------|----------|--------|
| 1 | [Specific, measurable action] | @person | [Date] | High | [JIRA-XXX] |
| 2 | [Specific, measurable action] | @person | [Date] | Medium | [JIRA-XXX] |
| 3 | [Specific, measurable action] | @person | [Date] | Medium | [JIRA-XXX] |

### Previous Action Item Review

| # | Action (from Sprint [N-1]) | Owner | Status | Notes |
|---|---------------------------|-------|--------|-------|
| 1 | [Action from last retro] | @person | Done | [Impact observed] |
| 2 | [Action from last retro] | @person | In Progress | [Updated plan] |
| 3 | [Action from last retro] | @person | Not Started | [Reason, carry forward?] |

### Team Mood (anonymous poll)

| Mood | Count |
|------|-------|
| Great | 2 |
| Good | 3 |
| Okay | 1 |
| Struggling | 0 |

### Facilitator Notes
- [Any observations about team dynamics]
- [Suggestions for next retro format]
```

### Improvement Trend Tracker

```markdown
## Retrospective Improvement Trends

**Team:** [Team Name]
**Tracking Period:** [Start] - [End]

### Action Item Completion Rate

| Sprint | Actions Created | Completed | Carried Over | Dropped | Rate |
|--------|----------------|-----------|-------------|---------|------|
| Sprint 10 | 3 | 2 | 1 | 0 | 67% |
| Sprint 11 | 4 | 3 | 1 | 0 | 75% |
| Sprint 12 | 3 | 3 | 0 | 0 | 100% |
| Sprint 13 | 2 | 1 | 1 | 0 | 50% |
| Sprint 14 | 3 | 2 | 0 | 1 | 67% |
| **Average** | **3.0** | **2.2** | | | **72%** |

### Recurring Themes

| Theme | Times Raised | Status | Resolution |
|-------|-------------|--------|------------|
| Deployment friction | 4 | Resolved | CI/CD pipeline implemented in Sprint 12 |
| Unclear requirements | 3 | In Progress | Added grooming session, PO writing ACs |
| Context switching | 2 | Monitoring | WIP limits introduced |

### Team Mood Over Time

| Sprint | Avg Mood (1-5) | Trend | Notable Events |
|--------|---------------|-------|----------------|
| Sprint 10 | 3.2 | -- | Team member left |
| Sprint 11 | 3.5 | ↑ | New hire onboarded |
| Sprint 12 | 4.0 | ↑ | Successful release |
| Sprint 13 | 3.8 | ↓ | Scope change mid-sprint |
| Sprint 14 | 4.1 | ↑ | Completed CI/CD improvement |
```

## Scripts & Tools

### Retro Board Generator

```bash
#!/bin/bash
# scripts/retro-board.sh
# Generate a retro board template for the chosen format
# Usage: ./scripts/retro-board.sh [format]
# Formats: ssc, 4ls, sailboat, msg

FORMAT="${1:-ssc}"

case "$FORMAT" in
  ssc)
    echo "# Start-Stop-Continue Retro - $(date +%Y-%m-%d)"
    echo ""
    echo "## Start (New things to try)"
    echo "- "
    echo ""
    echo "## Stop (Things to drop)"
    echo "- "
    echo ""
    echo "## Continue (Things working well)"
    echo "- "
    ;;
  4ls)
    echo "# 4Ls Retro - $(date +%Y-%m-%d)"
    echo ""
    echo "## Liked"
    echo "- "
    echo "## Learned"
    echo "- "
    echo "## Lacked"
    echo "- "
    echo "## Longed For"
    echo "- "
    ;;
  sailboat)
    echo "# Sailboat Retro - $(date +%Y-%m-%d)"
    echo ""
    echo "## Island (Our Goal)"
    echo "- "
    echo "## Wind (Helping Us)"
    echo "- "
    echo "## Anchor (Slowing Us Down)"
    echo "- "
    echo "## Rocks (Risks Ahead)"
    echo "- "
    ;;
  msg)
    echo "# Mad-Sad-Glad Retro - $(date +%Y-%m-%d)"
    echo ""
    echo "## Mad (Frustrated about)"
    echo "- "
    echo "## Sad (Disappointed about)"
    echo "- "
    echo "## Glad (Happy about)"
    echo "- "
    ;;
esac
```

### Action Item Tracker

```python
# scripts/retro_action_tracker.py
# Track action item completion across retros
# Usage: python scripts/retro_action_tracker.py

from dataclasses import dataclass
from datetime import date

@dataclass
class ActionItem:
    sprint: str
    description: str
    owner: str
    status: str  # "done", "in_progress", "not_started", "dropped"
    created: str
    completed: str = ""

def completion_rate(items: list[ActionItem]) -> float:
    if not items:
        return 0.0
    done = sum(1 for i in items if i.status == "done")
    return (done / len(items)) * 100

def report(items: list[ActionItem]) -> None:
    sprints = sorted(set(i.sprint for i in items))
    print(f"{'Sprint':<12} {'Created':>8} {'Done':>6} {'Rate':>6}")
    print("-" * 36)
    for sprint in sprints:
        sprint_items = [i for i in items if i.sprint == sprint]
        rate = completion_rate(sprint_items)
        done = sum(1 for i in sprint_items if i.status == "done")
        print(f"{sprint:<12} {len(sprint_items):>8} {done:>6} {rate:>5.0f}%")
```

## Best Practices

### Keeping Retros Fresh

- **Rotate formats** every 3-4 sprints to prevent staleness
- **Rotate facilitators** so the Scrum Master is not always driving
- **Use icebreakers** to set a positive tone (1-2 minutes, keep it light)
- **Change the environment** occasionally: different room, outdoor, coffee shop
- **Bring data:** Show velocity trends, incident counts, or PR review times
- **Limit to 3 action items:** More than 3 rarely get completed

### Participation Tips

| Challenge | Solution |
|-----------|----------|
| Quiet team members | Silent brainstorming first, then share; use anonymous input tools |
| One person dominates | Round-robin sharing; facilitator redirects |
| "Everything is fine" | Use a provocative format (pre-mortem); share specific data points |
| Remote/hybrid team | Digital board with simultaneous editing; camera on; breakout rooms |
| Retro fatigue | Change format, shorten duration, skip one occasionally, celebrate wins |
| No follow-through | Review last retro's actions first; make action items sprint backlog items |

### Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | What to Do Instead |
|-------------|-------------|-------------------|
| Blame game | Destroys psychological safety | Focus on processes and systems, not people |
| No action items | Retro becomes venting with no improvement | Always close with 1-3 concrete actions |
| Manager-led retro | Team self-censors | Have a peer facilitate; manager participates as equal |
| Skipping retros when "busy" | Improvement stops; problems accumulate | Shorten to 15 min rather than skip |
| Same format every time | Team gets bored, participation drops | Rotate formats every 3-4 sprints |
| Too many action items | Nothing gets done | Limit to 3 max; prioritize ruthlessly |
| Never reviewing past actions | No accountability, no progress | Always start by reviewing last retro's action items |
