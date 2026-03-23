---
name: live-chat-handler
description: Handle real-time customer chat conversations effectively. Use when the user mentions "live chat," "chat support," "real-time chat," "customer chat," "chat conversation," "instant messaging support," or "chat response."
metadata:
  version: 1.0.0
  category: customer-support
---

# Live Chat Handler

Handle real-time customer chat conversations with speed, empathy, and effective resolution.

## Quick Start

1. **Greet promptly**: Respond within 30 seconds
2. **Identify issue**: Ask clarifying questions
3. **Resolve or escalate**: Provide solution or transfer appropriately
4. **Close professionally**: Confirm resolution and offer further help

## Chat Handling Workflow

```
Progress:
- [ ] Step 1: Greet customer (within 30 seconds)
- [ ] Step 2: Identify customer and issue
- [ ] Step 3: Acknowledge the problem
- [ ] Step 4: Investigate/troubleshoot
- [ ] Step 5: Provide solution or escalate
- [ ] Step 6: Confirm resolution
- [ ] Step 7: Close chat professionally
- [ ] Step 8: Log interaction
```

## Response Time Standards

| Priority | First Response | Resolution Target |
|----------|---------------|-------------------|
| Urgent (payment, outage) | < 15 seconds | < 5 minutes |
| High (feature broken) | < 30 seconds | < 10 minutes |
| Medium (how-to questions) | < 45 seconds | < 15 minutes |
| Low (general inquiry) | < 60 seconds | < 20 minutes |

## Chat Opening Templates

**Standard Greeting:**
```
Hi [Name]! Thanks for reaching out. I'm [Agent] and I'll be helping you today. How can I assist you?
```

**Returning Customer:**
```
Welcome back, [Name]! Great to see you again. I'm [Agent]. What can I help you with today?
```

**After Wait:**
```
Hi [Name], thanks for your patience! I'm [Agent] and I'm here to help. I see you've been waiting - let me prioritize getting this resolved for you.
```

## Utility Scripts

**analyze_chat.py**: Analyze chat for sentiment and urgency
```bash
python scripts/analyze_chat.py chat_log.txt
# Output: Sentiment score, urgency level, suggested actions
```

**canned_responses.py**: Get appropriate canned response
```bash
python scripts/canned_responses.py --category "billing" --issue "refund"
# Output: Suggested response templates
```

## Quick Response Guide

| Customer Says | Response Approach |
|--------------|-------------------|
| "This is urgent!" | Acknowledge urgency, prioritize immediately |
| "I've been waiting forever" | Apologize sincerely, expedite resolution |
| "This happened before" | Pull history, escalate if pattern |
| "I want to cancel" | Understand why, offer retention options |
| "Let me speak to a manager" | Try to resolve, escalate if needed |

## Multitasking Guidelines

- Handle maximum **3 concurrent chats**
- Use canned responses for common questions
- Set expectations if you need time to research
- Never leave a customer waiting >2 minutes without update

## Resources

- **Full chat guide**: [reference.md](reference.md)
- **Response templates**: [templates/responses.md](templates/responses.md)
- **Escalation procedures**: [templates/escalation.md](templates/escalation.md)

## Related Skills

- Escalate complex issues: `escalation-handler`
- Log feedback: `customer-feedback-analyzer`
- Create KB from common questions: `knowledge-base-writer`
