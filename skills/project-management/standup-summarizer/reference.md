# Standup Summarizer Reference

Comprehensive reference for running effective daily standups, async standup workflows, blocker management, and weekly rollup generation.

## Standup Formats Compared

### Synchronous vs Asynchronous Standups

| Dimension | Synchronous | Asynchronous |
|-----------|-------------|-------------|
| **Best for** | Co-located teams, teams needing high coordination | Distributed teams across timezones |
| **Scheduling** | Fixed time, all attend | Deadline-based, post by X:00 |
| **Duration** | 15 min max | N/A (read at your pace) |
| **Blocker detection** | Immediate, real-time discussion | Delayed, requires follow-up thread |
| **Participation** | Can be dominated by loud voices | Equal voice for all |
| **Accountability** | Visible absence | May go unnoticed |
| **Documentation** | Requires note-taker | Self-documenting |
| **Team bonding** | Higher (face-to-face interaction) | Lower (text-based) |

### Hybrid Model

For teams split across 2-3 timezones:

1. Each timezone cluster has a synchronous standup
2. Cluster summaries are posted to a shared async channel
3. A global rollup is generated daily combining all clusters
4. Cross-cluster blockers are flagged and assigned within 2 hours

## Blocker Management Framework

### Blocker Classification

| Type | Description | Resolution Path | SLA |
|------|-------------|----------------|-----|
| **Technical** | Code issue, environment failure, tooling problem | Team-internal fix | 4-8 hours |
| **Dependency** | Waiting on another team, external API, vendor | Cross-team coordination | 24-48 hours |
| **Information** | Missing spec, unclear requirements, pending decision | Product Owner / stakeholder | 24 hours |
| **Access** | Missing credentials, permissions, environment access | DevOps / IT | 4-8 hours |
| **Resource** | Person unavailable, skill gap, capacity issue | Manager / Scrum Master | 24-48 hours |

### Blocker Lifecycle

```
IDENTIFIED -> ASSIGNED -> IN PROGRESS -> RESOLVED -> VERIFIED
     |            |            |              |
     v            v            v              v
  Logged in    Owner         Active        Blocker
  standup     notified     resolution     removed,
  summary                   work          person
                                          unblocked
```

**Metrics to track:**
- Mean time to assign (target: < 2 hours)
- Mean time to resolve (target: < 24 hours for P1)
- Repeat blocker rate (target: < 10%)
- Blocker aging (% resolved within SLA)

### Escalation Matrix

| Condition | Escalate To | Method | Timeline |
|-----------|------------|--------|----------|
| Blocker unresolved > 24h | Scrum Master | Slack DM + standup flag | Immediate |
| Blocker impacts sprint goal | Product Owner + Scrum Master | Meeting request | Within 4 hours |
| Cross-team blocker > 48h | Engineering Manager | Email + Slack | Within 2 hours |
| Blocker impacts release date | Director / VP Engineering | Escalation email | Within 1 hour |
| Multiple team members blocked | Scrum Master + Eng Manager | Emergency sync | Immediate |

## Standup Quality Metrics

### What Good Looks Like

| Metric | Target | How to Measure |
|--------|--------|---------------|
| Duration (sync) | < 15 min | Timer |
| Participation rate | > 95% | Count reporters / team size |
| Updates with specifics | > 90% | Audit: does update mention ticket IDs or specific tasks? |
| Blockers surfaced early | > 80% within first mention | Track when blocker was first reported vs when it started |
| Blocker resolution rate | > 85% within 24h | Track resolution timestamps |
| Summary posted on time | 100% | Check channel post time |

### Standup Anti-Patterns

| Anti-Pattern | Symptom | Root Cause | Fix |
|-------------|---------|-----------|-----|
| Status report to manager | Updates directed at SM, not team | Power dynamic | SM steps back; team talks to each other |
| Problem-solving in standup | Runs 30+ min; two people deep-diving | Lack of parking lot discipline | Strict parking lot; facilitator interrupts |
| "Working on the same thing" | Same update 3 days in a row | Story too large or person stuck | Break down story; check if actually blocked |
| Ghost updates | "Nothing to report" or missing entirely | Disengagement or unclear expectations | 1:1 with team member; clarify standup purpose |
| Blocker graveyard | Same blockers listed for a week | No follow-through on resolution | Assign owners; daily escalation check |
| Status theater | Elaborate updates with no substance | Performative culture | Ask for ticket IDs and % complete |

## Weekly Rollup Best Practices

### What to Include

A weekly rollup serves stakeholders who do not attend daily standups. It should provide:

1. **Velocity snapshot** - Points completed vs planned
2. **Key accomplishments** - Top 3-5 things shipped or completed
3. **Active blockers** - Only those still unresolved (do not list resolved ones)
4. **Risk flags** - Anything that might affect the sprint goal
5. **Team health** - Participation rate, mood check
6. **Next week focus** - Top priorities for the coming week

### What NOT to Include

- Individual daily task lists (too granular)
- Resolved blockers that had no lasting impact
- Internal process discussions
- Complaints or blame

## Tool Integration Patterns

### Slack Bot Integration

Recommended Slack workflow for async standups:

1. **9:00 AM** - Bot posts reminder in #standups channel
2. **10:00 AM** - Bot collects all threaded replies
3. **10:15 AM** - Bot generates summary and posts to #team-updates
4. **10:30 AM** - Bot DMs non-reporters with reminder
5. **11:00 AM** - Final summary with participation stats

### Jira/Linear Integration

Enrich standup summaries with ticket data:

- Pull in-progress tickets for each team member
- Show ticket age (days in current status)
- Flag tickets with no activity in 2+ days
- Auto-link ticket IDs mentioned in standup updates

## References

- Jason Yip, "It's Not Just Standing Up" (2006): https://www.martinfowler.com/articles/itsNotJustStandingUp.html
- Scrum Guide - Daily Scrum: https://scrumguides.org/
- Atlassian - Running Effective Standups: https://www.atlassian.com/agile/scrum/standups
