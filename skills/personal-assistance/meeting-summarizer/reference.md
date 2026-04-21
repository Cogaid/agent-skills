# Meeting Summarizer - Reference Guide

## DACI Framework - Detailed

The DACI framework (Decisions, Actions, Context, Insights) provides the structure for every meeting summary:

### D - Decisions

Capture exact decisions made, including:
- What was decided
- Who made the decision (or who approved)
- What the alternatives were
- Any conditions or caveats

**Tip:** Listen for phrases like "Let's go with...", "We've decided...", "The plan is...", "I'm making the call to..."

### A - Actions

Every action item needs three elements:
1. **What** - Specific, observable deliverable
2. **Who** - Single owner (never "the team")
3. **When** - Specific due date or timeframe

**Bad:** "We'll look into the API issue"
**Good:** "@Sarah will investigate the API timeout issue and report back by Thursday EOD"

### C - Context

Summarize the discussion that led to decisions:
- Key arguments for and against
- Data or evidence cited
- Constraints mentioned
- Stakeholder concerns raised

Keep this to 2-3 paragraphs maximum. Focus on what someone who was not in the meeting needs to know.

### I - Insights

Observations that add value beyond the literal discussion:
- Relationship dynamics (team alignment, friction points)
- Risks or concerns that were implied but not explicitly stated
- Opportunities mentioned in passing
- Sentiment shifts during the meeting

## Meeting Type Guidelines

### Stand-ups / Daily Syncs (5-15 min)

**Capture:**
- Blockers (always)
- Status changes (if notable)
- Help requests

**Skip:**
- Detailed discussion (should not happen in standup)
- Task-by-task status (use project board for that)

**Format:** Bullet list, 3-5 lines max

### 1:1 Meetings (30-60 min)

**Capture:**
- Career/development notes
- Feedback given/received
- Personal blockers
- Commitments made

**Sensitivity:** 1:1 notes are often private. Confirm with both parties what should be shared.

**Format:** Structured template with check-in, wins, challenges, actions

### Project/Sprint Meetings (30-60 min)

**Capture:**
- Sprint/project status (on track, at risk, blocked)
- Completed items since last meeting
- Blockers and mitigations
- Scope changes or priority shifts
- Decisions about architecture, approach, or timeline

**Format:** Status dashboard + action items

### Client/External Meetings (30-60 min)

**Capture:**
- Client concerns and priorities
- Agreements and commitments (both sides)
- Follow-up deliverables with owners and dates
- Relationship observations (sentiment, satisfaction signals)

**Sensitivity:** Separate internal observations from what you share with the client.

**Format:** Formal summary with internal notes section

### All-Hands / Town Halls (60-90 min)

**Capture:**
- Key announcements
- Strategic direction changes
- Q&A highlights
- Action items for your team

**Format:** Executive brief (5-7 bullets)

## Note-Taking Techniques

### The Cornell Method (Adapted for Meetings)

```
+------------------+--------------------------------+
|                  |                                |
|   CUES/          |   MAIN NOTES                   |
|   QUESTIONS      |                                |
|                  |   - Discussion points           |
|   (Fill in       |   - Quotes                      |
|    after         |   - Data mentioned              |
|    meeting)      |   - Decisions                   |
|                  |   - Action items (highlight)    |
|                  |                                |
+------------------+--------------------------------+
|                                                   |
|   SUMMARY (2-3 sentences, written after meeting)  |
|                                                   |
+---------------------------------------------------+
```

### Shorthand Symbols

| Symbol | Meaning |
|--------|---------|
| -> | Action item (followed by @owner) |
| ** | Decision made |
| ?? | Question/unclear point |
| !! | Important/urgent |
| ... | Discussion continued, not captured verbatim |
| [?name] | Need to confirm who said this |
| [park] | Parking lot item for later |

### Real-Time Capture Priority

When things move fast, capture in this priority order:
1. Decisions (exact wording if possible)
2. Action items (what, who, when)
3. Numbers/dates mentioned
4. Key disagreements or concerns
5. Discussion points (fill in after meeting)

## Distribution Best Practices

### Timing

| Meeting Type | Distribute Within |
|--------------|-------------------|
| Client/External | 4 hours (shows professionalism) |
| Decision meetings | 24 hours |
| Regular team meetings | 24 hours |
| All-hands | 48 hours |
| 1:1 | Same day (private) |

### Audience Tailoring

| Audience | What They Need |
|----------|----------------|
| Attendees | Full summary (verification) |
| Manager (not present) | Decisions + actions + risks |
| Cross-functional team | Decisions that affect them + their actions |
| Executive | 3-bullet executive brief |
| Project archive | Full summary + context |

### Follow-Up Cadence

```
Day 0: Distribute summary
Day 1: Ask for corrections ("Let me know if I missed anything")
Day 3: First action item check-in (if items due this week)
Day 7: Follow-up on overdue action items
Next meeting: Review open items from prior summary
```

## Action Item Tracking

### Status Labels

| Status | Meaning | Next Step |
|--------|---------|-----------|
| Open | Assigned, not started | Owner to begin |
| In Progress | Work underway | Check at next meeting |
| Blocked | Cannot proceed | Identify blocker resolution |
| Done | Completed | Archive |
| Canceled | No longer needed | Note reason |
| Deferred | Postponed deliberately | Set new date |

### Orphan Action Prevention

An "orphan action" is an action with no clear owner. Prevent by:
1. Never write "we will" -- always "@Name will"
2. If no one volunteers, flag it: "[NEEDS OWNER] {{action}}"
3. If due date is unclear: "[NEEDS DATE] @Name will {{action}}"
4. Review all actions at meeting end for completeness

## Quality Metrics

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Distribution time | <24h | Track send time vs. meeting end |
| Correction rate | <10% | Feedback from attendees |
| Action item completion | >80% | Track at next meeting |
| Attendee satisfaction | >4/5 | Periodic survey |
| Summary length | <1 page | Word count |
