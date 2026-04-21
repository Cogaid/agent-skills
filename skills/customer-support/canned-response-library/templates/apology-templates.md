# Apology Templates

## APOL-001: Service Disruption Apology

**Category**: Apology
**Channel**: All
**Tone**: Empathetic, accountable
**Personalization**: High
**Tags**: apology, disruption, outage, incident

### Template

```
Hi {{customer_name}},

I sincerely apologize for the disruption you experienced with {{service_name}}. I understand how frustrating it must be when {{impact_on_customer}}, and this is not the experience we want for you.

Our team has identified the cause as {{root_cause}}, and we've {{corrective_action}} to prevent this from happening again.

{{compensation_if_applicable}}

Thank you for your patience and understanding.
```

### Internal Notes

**When to use**: Service disruption affected the customer's workflow. Must have root cause identified.

**When NOT to use**: If root cause is unknown, use APOL-004 (investigating) instead.

---

## APOL-002: Billing Error Apology

**Category**: Apology
**Channel**: Email, Chat
**Tone**: Serious, immediate action
**Personalization**: High
**Tags**: apology, billing, overcharge, refund, financial

### Template

```
Hi {{customer_name}},

I owe you an apology. I can confirm that {{billing_error_description}}, and I completely understand your concern.

I've taken immediate action:
- {{correction_action}} (effective {{effective_date}})
- {{refund_details}} will appear in your account within {{refund_timeline}}

Here's your corrected billing summary:
- Original charge: {{original_amount}}
- Correct amount: {{correct_amount}}
- Refund/Credit: {{refund_amount}}

I've also flagged this internally to ensure it doesn't happen again. Please don't hesitate to reach out if you notice anything else on your account.
```

### Internal Notes

**When to use**: Confirmed billing error (overcharge, double-charge, incorrect plan pricing).

**Required before sending**: Verify the error is confirmed. Never admit billing error without verification.

**Compliance note**: Include specific amounts and dates for audit trail.

---

## APOL-003: Delayed Response Apology

**Category**: Apology
**Channel**: All
**Tone**: Accountable, action-oriented
**Personalization**: Medium
**Tags**: apology, delay, slow-response, SLA

### Template

```
Hi {{customer_name}},

I want to sincerely apologize for the delay in getting back to you. You deserved a faster response, and I'm sorry we fell short.

I've now reviewed your issue in full, and here's where we stand:
{{current_status_or_resolution}}

I'm prioritizing your case to make up for lost time. {{next_steps}}

Thank you for your patience — I appreciate you sticking with us.
```

### Internal Notes

**When to use**: Response time exceeded SLA or customer expressed frustration about wait time.

**Key principle**: Don't just apologize — immediately provide value (status, next step, or resolution) in the same message.

---

## APOL-004: Issue Under Investigation

**Category**: Apology
**Channel**: All
**Tone**: Transparent, committed
**Personalization**: Medium
**Tags**: apology, investigating, unknown-cause, in-progress

### Template

```
Hi {{customer_name}},

I'm sorry for the trouble you're experiencing with {{issue_summary}}. I want to be transparent — we haven't identified the root cause yet, but our team is actively investigating.

**What we know so far**: {{known_facts}}
**What we're doing**: {{investigation_steps}}
**Next update by**: {{next_update_time}}

I understand this is frustrating, especially without a clear timeline. I'll keep you updated even if it's just to say "still working on it" — you won't be left in the dark.
```

### Internal Notes

**When to use**: Issue is confirmed but root cause is unknown. Transparency is better than silence.

**Update commitment**: If you promise an update time, deliver on it. Set reminders.

---

## APOL-005: Agent Error Apology

**Category**: Apology
**Channel**: All
**Tone**: Humble, corrective
**Personalization**: High
**Tags**: apology, agent-error, incorrect-information, correction

### Template

```
Hi {{customer_name}},

I need to correct something from our previous conversation. I provided incorrect information about {{incorrect_info_topic}}.

**What I said**: {{incorrect_statement}}
**What's actually correct**: {{correct_information}}

I apologize for any confusion this caused. {{impact_mitigation_if_needed}}

If you took any action based on my earlier guidance, please let me know and I'll help make it right.
```

### Internal Notes

**When to use**: Agent (current or previous) gave wrong information. Own the mistake clearly.

**Key principle**: Never blame the previous agent by name. Use "we" or "I" regardless of who made the error.
