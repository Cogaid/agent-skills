# Meeting Summarizer

---
name: meeting-summarizer
description: Create clear, actionable meeting summaries and notes. Use when user mentions "meeting notes," "meeting summary," "summarize meeting," "recap meeting," "meeting minutes," or "action items from meeting."
metadata:
  version: 1.0.0
  category: personal-assistance
---

## Purpose

Transform meeting content into clear, actionable summaries that capture decisions, action items, and key insights.

## Quick Reference

### Summary Types

| Type | Use When | Length |
|------|----------|--------|
| Executive Brief | For leadership, busy stakeholders | 3-5 bullets |
| Standard Summary | Regular meetings | 1 page |
| Detailed Minutes | Formal/legal requirements | Full transcript |
| Action-Focused | Project/task meetings | Actions + owners |

### Key Elements to Capture

| Element | Priority | Always Include |
|---------|----------|----------------|
| Decisions made | Critical | Yes |
| Action items | Critical | Yes |
| Key discussions | High | Yes |
| Attendees | High | Yes |
| Follow-ups | High | Yes |
| Open questions | Medium | If applicable |
| Parking lot items | Low | If applicable |

## Summary Framework (DACI)

### Structure

| Section | Content |
|---------|---------|
| **D**ecisions | What was decided |
| **A**ctions | Tasks with owners and dates |
| **C**ontext | Key discussion points |
| **I**nsights | Important takeaways |

## Summary Template

### Standard Meeting Summary

```
# Meeting Summary: [Meeting Name]
📅 Date: [Date]
⏰ Duration: [X] minutes
👥 Attendees: [Names]

## 🎯 Key Decisions
1. [Decision 1]
2. [Decision 2]
3. [Decision 3]

## ✅ Action Items
| Action | Owner | Due Date |
|--------|-------|----------|
| [Task 1] | [Name] | [Date] |
| [Task 2] | [Name] | [Date] |
| [Task 3] | [Name] | [Date] |

## 📝 Discussion Summary
[2-3 paragraph summary of main topics discussed]

## ❓ Open Questions
- [Question 1]
- [Question 2]

## 📅 Next Steps
- Next meeting: [Date/Time]
- [Other follow-ups]
```

### Executive Brief

```
# [Meeting Name] - Executive Brief
[Date] | [Duration]

**DECISIONS:**
• [Key decision 1]
• [Key decision 2]

**ACTIONS (requires your attention):**
• [Action needing exec input] - Due: [Date]

**KEY INSIGHT:**
[One-sentence most important takeaway]

**NEXT:** [Next meeting/checkpoint]
```

### Action-Focused Summary

```
# Action Items from [Meeting Name]
[Date]

## Immediate (This Week)
- [ ] [Action] - @[Owner] - Due: [Date]
- [ ] [Action] - @[Owner] - Due: [Date]

## This Sprint/Month
- [ ] [Action] - @[Owner] - Due: [Date]
- [ ] [Action] - @[Owner] - Due: [Date]

## Backlog/Future
- [ ] [Action] - @[Owner] - No date set

## Decisions Made
• [Decision 1]
• [Decision 2]

## Blocked/Needs Input
• [Blocked item] - Waiting on: [Person/Thing]
```

## Meeting Types

### 1:1 Meeting Summary

```
# 1:1: [Manager] ↔ [Report]
[Date]

## Check-in
- How they're doing: [Brief]
- Energy level: [High/Medium/Low]

## Wins Since Last Time
- [Win 1]
- [Win 2]

## Challenges/Blockers
- [Challenge 1]
  - Support needed: [What]
- [Challenge 2]

## Discussion Points
- [Topic 1]: [Outcome]
- [Topic 2]: [Outcome]

## Actions
- [Name]: [Action] by [Date]
- [Name]: [Action] by [Date]

## Career/Development
- [Notes on growth, feedback, etc.]

## Next 1:1: [Date]
```

### Sprint/Project Meeting

```
# [Sprint/Project] Meeting - [Date]

## Sprint/Project Status
- Overall: 🟢 On Track / 🟡 At Risk / 🔴 Blocked
- Completion: [X]%

## Completed Since Last Meeting
- [Item 1] ✓
- [Item 2] ✓

## In Progress
| Item | Owner | Status | Blocker |
|------|-------|--------|---------|
| [Task] | [Name] | [X]% | [If any] |

## Blockers/Risks
- [Blocker 1]: [Mitigation]
- [Risk 1]: [Plan]

## Decisions Needed
- [Decision 1] - Decided: [Outcome]
- [Decision 2] - Decided: [Outcome]

## Next Sprint/Phase
- Focus: [Main focus]
- Key deliverables: [List]

## Actions
- [Action] - @[Owner] - Due: [Date]
```

### Client/External Meeting

```
# Client Meeting: [Client Name]
[Date] | [Location/Call]

## Attendees
Internal: [Names]
Client: [Names + Titles]

## Meeting Purpose
[Why this meeting was held]

## Client Updates
- [Update 1]
- [Update 2]

## Our Updates
- [Update 1]
- [Update 2]

## Key Discussion Points
1. [Topic]: [Summary]
2. [Topic]: [Summary]

## Agreements/Decisions
- [Agreement 1]
- [Agreement 2]

## Action Items
| Action | Owner | Due |
|--------|-------|-----|
| [Client action] | [Client] | [Date] |
| [Our action] | [Us] | [Date] |

## Follow-up
- Next meeting: [Date]
- Deliverables due: [What by When]

## Notes/Insights
[Any observations about relationship, opportunities, concerns]
```

## Best Practices

### During the Meeting

```
Capture:
□ Who said what (for attribution)
□ Exact wording of decisions
□ Specific numbers/dates mentioned
□ Action items as they're assigned
□ Questions that weren't answered
□ Tone/sentiment if relevant
```

### After the Meeting

```
Process:
□ Review and fill gaps within 2 hours
□ Clarify unclear points
□ Assign owners to orphan actions
□ Add due dates where missing
□ Format for readability
□ Distribute within 24 hours
```

### Writing Tips

| Do | Don't |
|----|-------|
| Use bullet points | Write paragraphs |
| Include context | Assume reader was there |
| Name owners explicitly | Say "we will" |
| Add specific dates | Say "soon" or "later" |
| Highlight decisions | Bury important items |
| Use consistent format | Change structure |

## Scripts & Tools

| Script | Purpose |
|--------|---------|
| `scripts/meeting_summarizer.py` | Generate summary from notes |
| `scripts/action_extractor.py` | Extract action items |

## Distribution Template

```
Subject: [Meeting Name] Summary - [Date]

Hi all,

Here's the summary from today's [meeting name].

[Paste summary]

Please review the action items and let me know if I missed
anything or got something wrong.

Next meeting: [Date/Time]

Thanks,
[Name]
```

## Reference

→ See `templates/meeting_templates.md` for all formats
→ See `reference.md` for meeting facilitation tips
