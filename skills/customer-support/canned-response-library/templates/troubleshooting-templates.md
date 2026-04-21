# Troubleshooting Templates

## TRBL-001: Step-by-Step Instructions

**Category**: Troubleshooting
**Channel**: All
**Tone**: Helpful, clear
**Personalization**: Medium
**Tags**: steps, instructions, guided, resolution

### Template

```
Hi {{customer_name}},

I'd like to walk you through a few steps to resolve this:

1. **{{step_1_action}}**
   {{step_1_detail}}

2. **{{step_2_action}}**
   {{step_2_detail}}

3. **{{step_3_action}}**
   {{step_3_detail}}

After completing these steps, please let me know if the issue is resolved. If you run into any trouble at any step, I'm right here to help.
```

### Internal Notes

**When to use**: Issue has a known resolution path with sequential steps. Max 5 steps per message -- if more are needed, break into multiple messages.

**Formatting rules**:
- Bold the action verb in each step
- Add expected result after critical steps ("You should see...")
- If step may fail, include what to do: "If you don't see X, try Y instead"

---

## TRBL-002: Request Diagnostic Information

**Category**: Troubleshooting
**Channel**: All
**Tone**: Professional, specific
**Personalization**: Medium
**Tags**: diagnostics, information-request, technical

### Template

```
Hi {{customer_name}},

To help me diagnose this issue more quickly, could you please share the following:

- **Browser/App version**: (e.g., Chrome 120, iOS app 3.2)
- **Operating system**: (e.g., Windows 11, macOS Sonoma)
- **Error message**: (screenshot or exact text if possible)
- **When it started**: (approximate date/time)
- **Frequency**: (every time, intermittent, one-time)

This information will help me pinpoint the cause and get you a solution faster.
```

### Internal Notes

**When to use**: Issue cannot be diagnosed without additional technical context from the customer.

**When NOT to use**: If you already have this information from the ticket or can look it up in the system.

**Key principle**: Only ask for what you actually need. Remove bullet points that aren't relevant to the specific issue.

---

## TRBL-003: Known Issue Acknowledgment

**Category**: Troubleshooting
**Channel**: All
**Tone**: Transparent, empathetic
**Personalization**: Medium
**Tags**: known-issue, workaround, transparency, outage

### Template

```
Hi {{customer_name}},

Thank you for reporting this. This is a known issue that our engineering team is actively working to resolve.

**What's happening**: {{issue_description}}
**Impact**: {{impact_description}}
**Workaround**: {{workaround_steps}}
**Expected fix**: {{eta_description}}

I've added you to the notification list, so you'll receive an update as soon as this is resolved. I apologize for the inconvenience.
```

### Internal Notes

**When to use**: The customer reports an issue that is already tracked and being worked on.

**When NOT to use**: If the issue is NOT confirmed as a known issue -- do not assume.

---

## TRBL-004: Escalation to Engineering

**Category**: Troubleshooting
**Channel**: All
**Tone**: Professional, reassuring
**Personalization**: Medium
**Tags**: escalation, engineering, technical, complex

### Template

```
Hi {{customer_name}},

I've investigated this thoroughly and this requires our engineering team's expertise to resolve. I've escalated your case with all the details.

**What happens next**:
- Our engineering team will review this within {{engineering_sla}}
- I'll remain your point of contact throughout
- I'll update you as soon as I hear back, even if it's just a progress note

**Ticket reference**: #{{ticket_id}}

You don't need to take any action right now. I'll reach out with the next update by {{next_update_time}}.
```

### Internal Notes

**When to use**: After exhausting Tier 1 troubleshooting steps without resolution. Must have already attempted standard resolution.

**When NOT to use**: Before trying standard troubleshooting. This is not a shortcut.

---

## TRBL-005: Cannot Reproduce Issue

**Category**: Troubleshooting
**Channel**: All
**Tone**: Collaborative, curious
**Personalization**: Medium
**Tags**: cannot-reproduce, clarification, investigation

### Template

```
Hi {{customer_name}},

I've attempted to reproduce the issue you described, but I'm seeing normal behavior on my end. This sometimes means the issue is specific to your setup or was a temporary glitch.

Could you help me narrow it down?

1. Is the issue still happening right now?
2. Does it occur in a different browser/device?
3. Does it happen every time, or intermittently?

If it's still occurring, a short screen recording or screenshot of the error would be incredibly helpful. No worries if you can't -- we'll figure this out together.
```

### Internal Notes

**When to use**: Agent has tried to reproduce the issue and cannot. Never imply the customer is wrong.

**Tone guideline**: Frame as "help me understand" not "I can't find a problem."
