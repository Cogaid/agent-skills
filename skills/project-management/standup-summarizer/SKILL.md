---
name: standup-summarizer
description: Summarize daily standups into clear async updates for distributed teams. Use when user mentions "standup summary," "daily standup," "standup notes," "async standup," "team status update," "blockers," "what did you do yesterday."
metadata:
  version: 1.0.0
  category: project-management
---

# Standup Summarizer

Summarize daily standups into clear, actionable async updates with blocker escalation and team status tracking.

## Purpose

Daily standups keep teams aligned, but they often run long, lack structure, or fail to surface critical blockers. This skill provides formats for both synchronous and asynchronous standups, templates for summarizing updates, criteria for escalating blockers, and rollup templates for weekly digests. It ensures that standup information is captured, actionable, and accessible to all stakeholders.

## Quick Reference

### Standup Format: The Three Questions

Every standup update should answer these three questions clearly and concisely:

| Question | Focus | Time Limit |
|----------|-------|------------|
| **What did I complete yesterday?** | Finished work, merged PRs, resolved issues | 30 seconds |
| **What am I working on today?** | Planned tasks, stories in progress | 30 seconds |
| **What is blocking me?** | Dependencies, access issues, unclear requirements | 30 seconds |

### Standup Health Indicators

| Indicator | Healthy | Warning | Action Needed |
|-----------|---------|---------|---------------|
| Duration | < 15 min | 15-25 min | > 25 min |
| Blockers per day | 0-1 | 2-3 | 4+ |
| Blockers unresolved > 24h | 0 | 1 | 2+ |
| Team members reporting | 100% | 80-99% | < 80% |
| Updates with measurable progress | > 80% | 50-80% | < 50% |

## Workflow

### Synchronous Standup Flow

1. **Scrum Master opens** the standup and confirms attendees (1 min)
2. **Each team member** gives their update using the three-question format (1-2 min each)
3. **Scrum Master captures** blockers on a shared board in real time
4. **Parking lot items** noted for follow-up after standup (do not discuss in standup)
5. **Scrum Master summarizes** blockers and action items (1-2 min)
6. **Post summary** to the team channel within 15 minutes

### Async Standup Flow

1. **Team members post** updates in the designated channel by a set time (e.g., 10:00 AM local)
2. **Bot or Scrum Master** collects all updates after the deadline
3. **Summary is generated** using the template below, highlighting blockers
4. **Blockers are flagged** and assigned owners for resolution
5. **Non-reporters** are pinged with a reminder
6. **Summary posted** to the team channel and stakeholder channels

### Blocker Escalation Criteria

Use this decision tree to determine when and how to escalate blockers:

```
Is someone actively blocked from doing ANY work?
  YES --> Escalate immediately to Scrum Master / manager
  NO  --> Is the blocker > 24 hours old?
            YES --> Flag in standup summary, assign owner, set 24h deadline
            NO  --> Track in standup, owner attempts self-resolution
                    Is the blocker cross-team?
                      YES --> Notify the other team's lead
                      NO  --> Team handles internally
```

### Escalation Severity Levels

| Level | Criteria | Action | Notify |
|-------|----------|--------|--------|
| **P0 - Critical** | Team member fully blocked, no workaround | Escalate within 1 hour | Manager + dependent team leads |
| **P1 - High** | Blocker will cause sprint goal miss if unresolved in 24h | Escalate same day | Scrum Master + Product Owner |
| **P2 - Medium** | Slows progress but workaround exists | Track daily, escalate if > 48h | Scrum Master |
| **P3 - Low** | Minor inconvenience, does not affect delivery | Note in standup, no escalation | Team only |

## Templates

### Daily Standup Summary Template

```markdown
## Daily Standup Summary - [Date]

**Team:** [Team Name]
**Sprint:** Sprint [N] (Day [X] of [Y])
**Attendees:** [Names or count, e.g., 6/7 present]
**Missing:** [Names]

---

### Progress Highlights
- [Dev 1] completed [US-101] user authentication flow - ready for QA
- [Dev 2] merged PR #234 for payment integration
- [Dev 3] finished API endpoint for search - deploying to staging

### In Progress Today
- [Dev 1] starting [US-103] password reset flow
- [Dev 2] working on [US-105] invoice generation (50% complete)
- [Dev 4] continuing [BUG-78] memory leak investigation

### Blockers & Risks

| # | Blocker | Owner | Blocked Since | Severity | Action |
|---|---------|-------|---------------|----------|--------|
| 1 | Waiting for staging DB credentials | @dev3 | Apr 18 | P1 | @devops to provide by EOD |
| 2 | Design spec unclear for settings page | @dev5 | Apr 19 | P2 | @designer reviewing today |

### Action Items
- [ ] @devops: Provide staging DB credentials to @dev3 by EOD
- [ ] @designer: Clarify settings page spec and share with @dev5
- [ ] @scrum-master: Follow up on yesterday's API rate limit blocker (resolved? Y/N)

### Sprint Burndown Check
- **Planned:** 38 points | **Completed:** 18 points | **Remaining:** 20 points
- **On track:** [Yes/No/At Risk]
```

### Async Standup Individual Update Template

```markdown
**[Your Name] - [Date]**

**Done:**
- Completed [task/ticket ID]: [brief description]
- Reviewed PR #[number] for [colleague]

**Doing:**
- [Task/ticket ID]: [what you plan to accomplish today]
- [Expected completion: today/tomorrow/date]

**Blockers:**
- [None / Description of blocker, who can help, how long blocked]

**FYI:**
- [Optional: anything the team should know - OOO tomorrow, joining late, etc.]
```

### Team Status Dashboard Template

```markdown
## Team Status Dashboard - [Date]

### Team Health at a Glance

| Member | Status | Current Story | Progress | Blockers |
|--------|--------|---------------|----------|----------|
| @dev1 | :green_circle: On Track | US-103 Password Reset | 30% | None |
| @dev2 | :green_circle: On Track | US-105 Invoicing | 50% | None |
| @dev3 | :red_circle: Blocked | US-107 Search Deploy | 0% | Needs DB creds |
| @dev4 | :yellow_circle: At Risk | BUG-78 Memory Leak | 40% | Complex root cause |
| @dev5 | :green_circle: On Track | US-110 Settings Page | 20% | None |

### Summary Metrics
- **Team members reporting:** 5/5 (100%)
- **Active blockers:** 1 (P1)
- **Stories in progress:** 5
- **Stories completed today:** 1
- **Sprint progress:** 47% complete (Day 5 of 10)
```

### Weekly Rollup Template

```markdown
## Weekly Standup Rollup - Week of [Date]

**Team:** [Team Name]
**Sprint:** Sprint [N] (Week [X] of [Y])

### Week Summary
- **Stories completed:** [N] ([total points] points)
- **Stories in progress:** [N]
- **Blockers raised:** [N] | **Resolved:** [N] | **Still open:** [N]
- **Average standup duration:** [X] min
- **Participation rate:** [X]%

### Key Accomplishments
1. [Major deliverable or milestone reached]
2. [Important bug fix or improvement]
3. [Cross-team collaboration completed]

### Persistent Blockers (> 2 days)

| Blocker | Owner | Days Blocked | Impact | Escalation Status |
|---------|-------|-------------|--------|-------------------|
| [Description] | @person | 3 | Sprint goal at risk | Escalated to [manager] |

### Patterns & Observations
- [Positive pattern: e.g., "QA turnaround improved from 2 days to 1 day"]
- [Concern: e.g., "3 stories carried over - estimation accuracy needs review"]
- [Suggestion: e.g., "Consider pairing on complex bugs to reduce investigation time"]

### Next Week Focus
- [Priority 1 for next week]
- [Priority 2 for next week]
```

## Scripts & Tools

### Standup Reminder Bot Script

```bash
#!/bin/bash
# scripts/standup-reminder.sh
# Post a standup reminder to Slack channel
# Usage: ./scripts/standup-reminder.sh "#team-channel"
# Schedule via cron: 0 9 * * 1-5 ./scripts/standup-reminder.sh "#dev-team"

CHANNEL="${1:-#general}"
DATE=$(date +"%A, %B %d, %Y")

curl -X POST "https://slack.com/api/chat.postMessage" \
  -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"channel\": \"$CHANNEL\",
    \"text\": \"Good morning! Time for standup ($DATE). Please post your update:\n\n*Done:* What did you complete?\n*Doing:* What are you working on today?\n*Blockers:* Anything in your way?\n\nPlease post by 10:00 AM.\"
  }"
```

### Standup Summary Collector

```python
# scripts/standup_collector.py
# Collects async standup messages and generates a summary
# Usage: python scripts/standup_collector.py --channel "#standups" --date "2026-04-20"

import re
from datetime import date

def parse_standup(message: str) -> dict:
    """Parse a standup message into structured sections."""
    sections = {"done": [], "doing": [], "blockers": [], "fyi": []}
    current = None
    for line in message.strip().split("\n"):
        lower = line.lower().strip()
        if lower.startswith("done") or lower.startswith("**done"):
            current = "done"
        elif lower.startswith("doing") or lower.startswith("**doing"):
            current = "doing"
        elif lower.startswith("blocker") or lower.startswith("**blocker"):
            current = "blockers"
        elif lower.startswith("fyi") or lower.startswith("**fyi"):
            current = "fyi"
        elif current and line.strip().startswith("- "):
            sections[current].append(line.strip()[2:])
    return sections

def generate_summary(updates: list[dict]) -> str:
    """Generate a formatted summary from parsed updates."""
    blockers = []
    for u in updates:
        for b in u.get("blockers", []):
            if b.lower() != "none":
                blockers.append({"person": u["name"], "blocker": b})

    summary = f"## Daily Standup Summary - {date.today()}\n\n"
    summary += f"**Reporting:** {len(updates)} team members\n\n"
    summary += "### Blockers\n"
    if blockers:
        for b in blockers:
            summary += f"- **{b['person']}:** {b['blocker']}\n"
    else:
        summary += "- No blockers reported\n"
    return summary
```

## Best Practices

### Making Standups Effective

- **Timebox strictly:** 15 minutes maximum for synchronous standups
- **Stand up literally:** Standing discourages long tangents (for in-person teams)
- **Talk to the team, not the manager:** Standups are for peer coordination
- **Save discussions for after:** Use a parking lot for topics that need deeper conversation
- **Celebrate wins:** Briefly acknowledge completed work to maintain morale
- **Rotate facilitation:** Prevent single points of failure and build team ownership

### Async Standup Tips

- Set a clear deadline for posting (e.g., 10:00 AM in each timezone)
- Use a dedicated channel - do not mix standups with general conversation
- Use threaded replies for follow-up questions to keep the channel scannable
- Automate reminders for team members who have not posted
- Summarize async updates daily so latecomers and stakeholders get the highlights

### Common Pitfalls

| Pitfall | Impact | Solution |
|---------|--------|----------|
| Status reports to the manager | Team disengages, no peer coordination | Redirect: "Tell the team what they need to know" |
| Problem-solving in standup | Meeting runs 30+ minutes | Parking lot rule: "Let's take this offline" |
| Vague updates ("working on stuff") | No visibility into progress | Ask: "What specific task? What percentage done?" |
| Skipping blockers out of pride | Issues fester, sprint goal missed | Normalize asking for help; celebrate unblocking |
| No follow-up on blockers | Same blockers repeated daily | Assign owners and deadlines; track resolution |
| Inconsistent async posting | Summary is incomplete | Automated reminders + accountability pairing |
