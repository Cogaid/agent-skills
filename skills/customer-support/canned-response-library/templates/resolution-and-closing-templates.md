# Resolution and Closing Templates

## Resolution Templates

### RSLV-001: Issue Resolved

**Category**: Resolution
**Channel**: All
**Tone**: Positive, clear
**Personalization**: High
**Tags**: resolved, confirmation, success

#### Template

```
Hi {{customer_name}},

Great news — the issue with {{issue_summary}} has been resolved!

Here's what we did:
- {{action_taken}}

You should now be able to {{expected_outcome}}. Please give it a try and let me know if everything is working as expected.

If you need anything else, don't hesitate to reach out. We're always happy to help!
```

#### Internal Notes

**When to use**: Issue is confirmed fixed. Be specific about what was done -- never say "it's fixed" without explaining the action.

---

### RSLV-002: Issue Resolved with Compensation

**Category**: Resolution
**Channel**: All
**Tone**: Apologetic, generous
**Personalization**: High
**Tags**: resolved, compensation, goodwill, credit

#### Template

```
Hi {{customer_name}},

I'm pleased to let you know that {{issue_summary}} has been fully resolved.

I understand this caused {{impact_description}}, and I sincerely apologize for the inconvenience. As a gesture of goodwill, I've applied {{compensation_details}} to your account.

{{compensation_specifics}}

Is there anything else I can help you with today?
```

#### Internal Notes

**When to use**: Issue is resolved AND the customer experienced significant inconvenience warranting compensation. Requires manager approval for credits above $XX.

**Compensation guidelines**:
- Minor inconvenience: 10% discount on next bill
- Service disruption: 1 month credit
- Major incident: Case-by-case (manager approval)

---

### RSLV-003: Partial Resolution

**Category**: Resolution
**Channel**: All
**Tone**: Transparent, proactive
**Personalization**: High
**Tags**: partial, in-progress, workaround

#### Template

```
Hi {{customer_name}},

I wanted to update you on {{issue_summary}}. I've been able to {{partial_resolution}}, which should {{partial_benefit}}.

However, {{remaining_issue}} is still being worked on. Here's the plan:
- **Next step**: {{next_action}}
- **Timeline**: {{expected_timeline}}
- **I'll update you**: {{next_update_time}}

In the meantime, you can {{workaround_if_any}}.

Thank you for your patience -- I'm staying on this until it's fully resolved.
```

#### Internal Notes

**When to use**: Some aspects of the issue are fixed but others remain. Keep the customer informed rather than waiting for a complete fix.

---

## Closing Templates

### CLOS-001: Standard Close

**Category**: Closing
**Channel**: All
**Tone**: Warm, open
**Personalization**: Medium
**Tags**: closing, standard, end-conversation

#### Template

```
Is there anything else I can help you with today? If not, I hope you have a wonderful {{day_period}}!

If you need help in the future, we're always just a message away. Thank you for choosing {{company_name}}!
```

#### Internal Notes

**When to use**: Default closing for any resolved conversation. Always ask if there's anything else first.

---

### CLOS-002: Close with Survey

**Category**: Closing
**Channel**: Chat, Email
**Tone**: Appreciative, brief
**Personalization**: Medium
**Tags**: closing, survey, feedback, csat

#### Template

```
I'm glad I could help! Before I close out this conversation, would you mind taking a quick 30-second survey about your experience? Your feedback helps us improve.

[Survey Link: {{survey_url}}]

Thank you, {{customer_name}}, and have a great {{day_period}}!
```

#### Internal Notes

**When to use**: After positive interactions (CSAT score likely 4-5). Do not send after difficult interactions where the customer expressed frustration.

**Frequency cap**: Do not send if customer received a survey in the last 30 days.

---

### CLOS-003: Close - No Response from Customer

**Category**: Closing
**Channel**: Email, Chat
**Tone**: Understanding, open
**Personalization**: Medium
**Tags**: closing, no-response, timeout, follow-up

#### Template

```
Hi {{customer_name}},

I haven't heard back from you, so I wanted to check in. If your issue with {{issue_summary}} is resolved, I'll go ahead and close this ticket.

If you still need help, just reply to this message and I'll pick up right where we left off — no need to re-explain anything.

This ticket will auto-close in {{auto_close_days}} days if I don't hear back. You can always open a new request anytime.

Have a great {{day_period}}!
```

#### Internal Notes

**When to use**: Customer has not responded for 48+ hours after agent's last message.

**Timing**: Send after 48 hours. Auto-close after additional 5 business days.
