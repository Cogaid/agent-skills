# Greeting Templates

## GREET-001: Standard Welcome

**Category**: Greeting
**Channel**: All
**Tone**: Friendly
**Personalization**: High
**Tags**: first-contact, general, opening

### Template

```
Hi {{customer_name}},

Thank you for reaching out to {{company_name}} support! My name is {{agent_name}}, and I'll be helping you today.

I've reviewed your message about {{issue_summary}}. Let me look into this for you right away.
```

### Internal Notes

**When to use**: Default opening for any new conversation where the customer's issue is clear from their initial message.

**When NOT to use**: VIP customers (use GREET-003), returning customers with history (use GREET-002), transfers from another agent.

**Variations**:
- If issue is unclear: Replace last sentence with "Could you share a few more details about what you're experiencing?"
- If high priority: Add "I can see this is urgent, and I'm prioritizing this now."

---

## GREET-002: Returning Customer Welcome

**Category**: Greeting
**Channel**: All
**Tone**: Warm, appreciative
**Personalization**: High
**Tags**: returning, loyalty, rapport

### Template

```
Hi {{customer_name}},

Welcome back! I can see you've been with us since {{join_date}} — thank you for your continued trust in {{company_name}}.

I see you're reaching out about {{issue_summary}}. Let me take a look at this for you.
```

### Internal Notes

**When to use**: Customer has been with the company 6+ months and this is not their first support interaction.

**When NOT to use**: New customers, customers with recent negative experiences (they may not appreciate "welcome back" during frustration).

---

## GREET-003: VIP/Enterprise Welcome

**Category**: Greeting
**Channel**: All
**Tone**: Professional, premium
**Personalization**: Very High
**Tags**: vip, enterprise, premium, priority

### Template

```
Hello {{customer_name}},

Thank you for contacting {{company_name}} priority support. I'm {{agent_name}}, your dedicated support specialist today.

I've reviewed your request regarding {{issue_summary}} and I'm making this my top priority. I'll have an update for you within {{sla_target}}.
```

### Internal Notes

**When to use**: Enterprise or premium tier customers. Always reference SLA commitment.

**When NOT to use**: Standard or basic tier customers.

---

## GREET-004: Transfer Greeting

**Category**: Greeting
**Channel**: Chat, Phone
**Tone**: Reassuring
**Personalization**: High
**Tags**: transfer, handoff, escalation

### Template

```
Hi {{customer_name}},

I'm {{agent_name}} from our {{department}} team. {{previous_agent}} has brought me up to speed on your {{issue_summary}}.

I have all the context from your conversation so far — no need to repeat anything. Let me continue working on this for you.
```

### Internal Notes

**When to use**: When a customer has been transferred from another agent or team.

**When NOT to use**: If the agent does NOT actually have context (be honest and ask).

**Key principle**: Never make the customer repeat themselves. If context was lost, acknowledge it honestly.

---

## GREET-005: Proactive Outreach

**Category**: Greeting
**Channel**: Email, Chat
**Tone**: Helpful, proactive
**Personalization**: Medium
**Tags**: proactive, outreach, follow-up, check-in

### Template

```
Hi {{customer_name}},

I'm {{agent_name}} from {{company_name}} support. I'm reaching out because {{outreach_reason}}.

I wanted to check in and make sure everything is working well for you. Is there anything I can help with?
```

### Internal Notes

**When to use**: Agent-initiated contact (not customer-initiated). Examples: post-incident follow-up, onboarding check-in, feature adoption outreach.

**When NOT to use**: Customer has opted out of proactive communications.
