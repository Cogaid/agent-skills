# Subscription Manager

---
name: subscription-manager
description: Handle subscription management requests including upgrades, downgrades, cancellations, and billing issues. Use when customers mention "subscription," "cancel," "billing," "payment failed," "upgrade," "downgrade," "renewal," "plan change," or "account billing."
metadata:
  version: 1.0.0
  category: customer-support
---

## Purpose

Manage subscription lifecycle efficiently - from plan changes to cancellations - while maximizing retention and customer satisfaction.

## Quick Reference

### Subscription Actions

| Action | Timing | Proration | Access Change |
|--------|--------|-----------|---------------|
| Upgrade | Immediate | Credit remaining | Immediate |
| Downgrade | End of cycle | None | End of cycle |
| Cancel | End of cycle | None | Until period end |
| Pause | Immediate | Credit or extend | Immediate |
| Reactivate | Immediate | Full charge | Immediate |

### Cancellation Save Rates

| Offer Type | Typical Save Rate |
|------------|------------------|
| Discount (20-30%) | 15-25% |
| Pause option | 20-30% |
| Downgrade to cheaper plan | 30-40% |
| Extended trial of premium | 10-15% |
| No intervention | 0% |

## Workflow

### 1. Identify Request Type

```
Subscription Request Types:
□ Plan change (upgrade/downgrade)
□ Cancellation request
□ Billing issue
□ Payment update
□ Pause/resume
□ Account access issue
□ Plan inquiry
```

### 2. Cancellation Flow (SAVE Framework)

```
S - Sympathize: Acknowledge their situation
A - Ask why: Understand the real reason
V - Validate: Confirm you understand
E - Explore options: Offer alternatives

Decision Tree:
├─→ Price concern → Offer discount or downgrade
├─→ Not using → Offer pause or training
├─→ Missing features → Check roadmap, offer feedback channel
├─→ Competitor → Understand gaps, offer transition help
├─→ Temporary need → Offer pause
└─→ Hard cancel → Process gracefully, leave door open
```

### 3. Retention Offers Matrix

| Reason | Primary Offer | Secondary Offer |
|--------|--------------|-----------------|
| Too expensive | 20% discount for 3 months | Downgrade option |
| Not using enough | Pause subscription | Training session |
| Missing features | Roadmap preview | Feedback reward |
| Switching competitor | Extended trial premium | Exit interview |
| Temporary situation | 1-3 month pause | Reduced plan |
| Poor experience | Free month + escalation | Dedicated support |

## Response Templates

### Upgrade Request
```
Hi [Name],

Great choice! Let me help you upgrade to [NEW_PLAN].

Here's what changes:
📈 New Plan: [PLAN_NAME] - $[PRICE]/[PERIOD]

New features you'll get:
✓ [Feature 1]
✓ [Feature 2]
✓ [Feature 3]

Billing details:
- Credit for remaining time: $[CREDIT]
- New charge today: $[CHARGE]
- Next billing date: [DATE]

Ready to upgrade? [Confirm link/button]

Questions? Just let me know.
```

### Downgrade Request
```
Hi [Name],

I understand you'd like to move to [NEW_PLAN]. I can help with that.

What changes with [NEW_PLAN]:
- Price: $[PRICE]/[PERIOD]
- [Feature you'll lose 1]
- [Feature you'll lose 2]

What stays the same:
✓ [Retained feature 1]
✓ [Retained feature 2]

Timing:
- Your current plan continues until [DATE]
- [NEW_PLAN] starts on [DATE]
- No action needed until then

[If applicable: Before you switch, have you tried [feature]? Many customers find it valuable for [use case].]

Ready to confirm? [Confirm link/button]
```

### Cancellation - First Response
```
Hi [Name],

I'm sorry to hear you're thinking about cancelling. I'd like to understand what's happening and see if there's anything I can do.

Before I process the cancellation, could you share what's prompting this decision?

□ Not getting enough value
□ Too expensive right now
□ Switching to another solution
□ Just not using it
□ Other: ___

Your feedback helps us improve, and I may be able to offer something that addresses your concern.
```

### Cancellation - With Offer
```
Hi [Name],

Thank you for sharing that. I completely understand [their reason].

Before you go, I wanted to offer you something:

[OFFER - e.g., "How about 30% off for the next 3 months? That brings your monthly cost down to $[PRICE]."]

This would give you [benefit] while [addressing their concern].

Would this work for you?

□ Yes, I'll take the offer
□ No thanks, please cancel
```

### Cancellation Confirmed
```
Hi [Name],

I've processed your cancellation as requested.

Here's what happens now:
📅 Access continues until: [END_DATE]
💰 No further charges
📧 You'll receive a confirmation email

What you can still do:
- Export your data before [DATE]
- Reactivate anytime at [LINK]

We're sorry to see you go. If anything changes, we'd love to have you back.

Is there anything else I can help with today?
```

### Payment Failed
```
Hi [Name],

We noticed your recent payment didn't go through.

Payment details:
💳 Card ending: [LAST4]
💰 Amount: $[AMOUNT]
📅 Attempted: [DATE]

Common reasons this happens:
- Card expired
- Insufficient funds
- Bank security hold

To keep your subscription active:
[Update payment link]

If there's an issue with your bank, give them a quick call and we can retry.

Let me know if you need help with anything.
```

## Billing Scenarios

### Proration Calculation

**Upgrade (immediate):**
```
Days remaining in current period: X
Daily rate of current plan: $A/day
Credit: X × $A

New plan daily rate: $B/day
Charge for remaining days: X × $B
Net charge today: (X × $B) - (X × $A)
```

**Downgrade (end of period):**
```
- No immediate charge
- Current plan continues until renewal
- New plan price effective on renewal date
```

### Refund Eligibility

| Scenario | Refund Policy |
|----------|--------------|
| Cancel within trial | Full refund |
| Cancel day 1-7 | Full refund |
| Cancel day 8-30 | Prorated refund |
| Cancel after 30 days | No refund, access until end |
| Payment error | Full refund within 48 hours |
| Duplicate charge | Full refund immediately |

## Pause Subscription

### Pause Options

| Duration | Billing Impact | Access |
|----------|---------------|--------|
| 1 month | Skips 1 payment | Suspended |
| 2 months | Skips 2 payments | Suspended |
| 3 months | Skips 3 payments | Suspended |
| Indefinite | No charges until resume | Suspended |

### Pause Template
```
Hi [Name],

I've paused your subscription as requested.

📅 Pause starts: [DATE]
📅 Auto-resumes: [DATE] (or when you're ready)
💳 No charges during pause

Your data is safe and waiting for you.

To resume early, just [resume link].

Enjoy the break!
```

## Scripts & Tools

| Script | Purpose |
|--------|---------|
| `scripts/subscription_manager.py` | Manage subscription actions |
| `scripts/billing_calculator.py` | Calculate prorations and refunds |

## Escalation Triggers

Escalate when:
- Customer threatens legal action
- Billing discrepancy > $100
- Account compromised
- Multiple failed retention attempts
- VIP/enterprise customer
- Media mention or public complaint

## Retention Best Practices

### Do's
- Listen first, offer second
- Personalize retention offers
- Make it easy to stay
- Thank them regardless of outcome
- Leave the door open

### Don'ts
- Make cancellation difficult
- Ignore the stated reason
- Offer same discount repeatedly
- Argue with the customer
- Take it personally

## Reference

→ See `templates/subscription_templates.md` for all response templates
→ See `reference.md` for billing policies and calculations
