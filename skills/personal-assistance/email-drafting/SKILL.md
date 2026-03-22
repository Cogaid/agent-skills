---
name: email-drafting
description: Writes clear, professional emails for any business context. Use when the user mentions "write email," "draft message," "reply to email," "follow-up email," "thank you email," "introduction email," "apology email," "decline email," or "professional tone."
metadata:
  version: 1.1.0
  category: personal-assistance
---

# Email Drafting

Write clear, professional, and effective emails that get results.

## Quick Start

1. **Clarify purpose**: What action do you need?
2. **Choose template**: Use [templates/](templates/)
3. **Draft email**: Run `python scripts/draft_email.py`
4. **Check quality**: Run `python scripts/check_email.py`
5. **Send**: After final review

## Email Writing Workflow

```
Progress:
- [ ] Step 1: Define goal (inform, request, follow-up)
- [ ] Step 2: Identify audience and tone
- [ ] Step 3: Write subject line (specific, clear)
- [ ] Step 4: Front-load the main point
- [ ] Step 5: Add only necessary context
- [ ] Step 6: Include clear call-to-action
- [ ] Step 7: Proofread (especially names!)
- [ ] Step 8: Check recipients (To/CC/BCC)
```

## Email Structure

```
Subject: [Clear, specific subject]

[Greeting],

[Purpose - why you're writing in 1-2 sentences]

[Context - only what's necessary]

[Request/Information - be specific]

[Next steps - what happens now]

[Closing],
[Your name]
```

## Before Writing, Ask

1. **What's the goal?** Inform, request, follow-up?
2. **Who's the audience?** Exec, peer, external?
3. **What action needed?** Reply, approval, FYI?
4. **What's the deadline?** If time-sensitive
5. **What tone?** Formal, professional, casual?

## Utility Scripts

**draft_email.py**: Generate email from parameters
```bash
python scripts/draft_email.py --type request --to "manager" --topic "budget approval"
# Output: Draft email with template applied
```

**check_email.py**: Validate email before sending
```bash
python scripts/check_email.py email.txt
# Output: Word count, readability, suggestions
```

**shorten_email.py**: Condense verbose emails
```bash
python scripts/shorten_email.py verbose_email.txt
# Output: Shortened version with cut suggestions
```

## Common Email Types

| Type | Template | Key Elements |
|------|----------|--------------|
| Request | [templates/request.md](templates/request.md) | Specific ask, deadline, context |
| Follow-up | [templates/followup.md](templates/followup.md) | Reference original, add value |
| Introduction | [templates/introduction.md](templates/introduction.md) | Both parties' context, BCC self |
| Thank you | [templates/thankyou.md](templates/thankyou.md) | Specific about what, impact |
| Decline | [templates/decline.md](templates/decline.md) | Clear no, brief reason, alternative |

## Resources

- **Full writing guide**: [reference.md](reference.md)
- **All email templates**: [templates/](templates/)
- **Subject line formulas**: [reference.md](reference.md#subject-lines)
- **Tone adjustments**: [reference.md](reference.md#tone)

## Related Skills

- Meeting scheduling emails: `meeting-scheduler`
- Prioritizing responses: `task-prioritizer`
- Travel coordination emails: `travel-planner`
