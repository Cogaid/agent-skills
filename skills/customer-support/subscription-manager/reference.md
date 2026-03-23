# Subscription Manager Reference

## Subscription Lifecycle

### States

```
Trial
  ↓
Active → Paused → Active
  ↓         ↓
Past Due → Cancelled
  ↓
Cancelled
```

### State Definitions

| State | Description | Billing | Access |
|-------|-------------|---------|--------|
| Trial | Free trial period | None | Full |
| Active | Paid, current | Recurring | Full |
| Past Due | Payment failed | Retry pending | Limited/Full |
| Paused | Customer paused | Suspended | None |
| Cancelled | Subscription ended | None | None |

---

## Billing Models

### Common Models

| Model | Description | Proration |
|-------|-------------|-----------|
| Monthly | Billed monthly | By day |
| Annual | Billed yearly | By month |
| Usage-based | Based on consumption | N/A |
| Tiered | Price changes at thresholds | By usage |
| Per-seat | Per user pricing | By user-day |

### Billing Cycles

**Monthly Billing:**
- Bill date: Same day each month
- Grace period: 3-7 days after failed payment
- Retry attempts: 3-5 over 2 weeks

**Annual Billing:**
- Bill date: Same date each year
- Renewal reminder: 30/14/7 days before
- Grace period: 14 days

---

## Proration Calculations

### Upgrade Proration

```python
# Calculate upgrade proration
current_plan_daily = current_plan_price / days_in_period
new_plan_daily = new_plan_price / days_in_period
days_remaining = period_end_date - today

credit = current_plan_daily * days_remaining
charge = new_plan_daily * days_remaining
net_charge = charge - credit
```

**Example:**
- Current plan: $30/month (30 days)
- New plan: $50/month
- 15 days remaining

```
Credit: ($30/30) × 15 = $15
Charge: ($50/30) × 15 = $25
Net: $25 - $15 = $10 charged today
```

### Downgrade Handling

**Option A: End of Period**
- No immediate change
- New plan starts at next billing
- No proration needed

**Option B: Immediate with Credit**
- Downgrade happens now
- Credit for unused time on higher plan
- Applied to future billing

---

## Payment Processing

### Failed Payment Handling

| Attempt | Timing | Action |
|---------|--------|--------|
| 1st failure | Day 0 | Email notification |
| 2nd attempt | Day 3 | Retry + SMS |
| 3rd attempt | Day 7 | Retry + final warning |
| 4th attempt | Day 10 | Last retry |
| Cancellation | Day 14 | Account cancelled |

### Dunning Email Sequence

**Day 0 - First Notice:**
```
Subject: Action needed: Payment failed for your subscription

Hi [Name],

We couldn't process your payment of $[AMOUNT].

This usually happens because:
- Card expired
- Insufficient funds
- Bank security hold

Please update your payment method to keep your subscription active:
[Update Payment Button]

If you have questions, we're here to help.
```

**Day 7 - Urgent Notice:**
```
Subject: Your subscription will be cancelled in 7 days

Hi [Name],

We've tried to process your payment several times without success.

To avoid losing access to your account:
[Update Payment Button]

Your subscription will be cancelled on [DATE] if we can't process payment.

Need help? Just reply to this email.
```

### Retry Logic

| Card Type | Best Retry Time | Notes |
|-----------|----------------|-------|
| Debit | End of day (payday) | Tue-Thu best |
| Credit | Mid-month | Avoid bill due dates |
| Prepaid | After reload detected | Variable |

---

## Cancellation Handling

### Cancellation Reasons

| Reason Code | Description | Retention Tactic |
|-------------|-------------|------------------|
| PRICE | Too expensive | Discount/downgrade |
| VALUE | Not enough value | Training/demo |
| FEATURES | Missing features | Roadmap/feedback |
| COMPETITOR | Switching | Exit interview |
| USAGE | Not using | Pause option |
| TEMP | Temporary need | Pause option |
| EXPERIENCE | Bad experience | Recovery offer |
| OTHER | Other reason | Explore |

### Retention Offer Rules

| Customer Type | Max Discount | Pause Options |
|---------------|--------------|---------------|
| New (<90 days) | 30% × 2 months | Up to 1 month |
| Regular | 25% × 3 months | Up to 3 months |
| Long-term (>1yr) | 20% × 3 months | Up to 6 months |
| Enterprise | Custom | Custom |

### Offer Stack (in order)

1. Pause subscription (if usage-related)
2. Downgrade to cheaper plan
3. Discount on current plan
4. Extended premium trial
5. Feature request acknowledgment
6. Graceful exit with return offer

---

## Plan Management

### Plan Change Matrix

| From → To | Timing | Billing Impact | Access Change |
|-----------|--------|----------------|---------------|
| Free → Paid | Immediate | New charge | Immediate |
| Basic → Pro | Immediate | Prorated charge | Immediate |
| Pro → Basic | End of period | None | End of period |
| Paid → Free | End of period | None | End of period |
| Any → Cancel | End of period | None | Until period end |
| Cancel → Paid | Immediate | Full charge | Immediate |

### Feature Access by Plan

| Feature | Free | Basic | Pro | Enterprise |
|---------|------|-------|-----|------------|
| Core features | ✓ | ✓ | ✓ | ✓ |
| Support | Community | Email | Priority | Dedicated |
| Storage | 1 GB | 10 GB | 100 GB | Unlimited |
| Users | 1 | 5 | 25 | Unlimited |
| API access | - | Basic | Full | Full + SLA |
| Analytics | - | Basic | Advanced | Custom |

---

## Refund Policies

### Standard Refund Policy

| Timeframe | Eligibility | Refund Amount |
|-----------|-------------|---------------|
| Within trial | Auto-eligible | Full (if charged) |
| 0-7 days | Request required | Full |
| 8-30 days | Request + review | Prorated |
| 31+ days | Case-by-case | Typically none |
| Annual plan | Within 30 days | Full |
| Annual plan | 31-90 days | Prorated |

### Refund Calculation

**Monthly (prorated):**
```
days_used = today - billing_start
days_in_period = billing_end - billing_start
daily_rate = amount_paid / days_in_period
refund = (days_in_period - days_used) * daily_rate
```

**Annual (prorated by month):**
```
months_used = ceil((today - billing_start) / 30)
monthly_rate = annual_price / 12
refund = (12 - months_used) * monthly_rate
```

### Non-Refundable Items

- Setup fees (after 48 hours)
- Add-on purchases
- Overages/usage charges
- Custom development
- Training sessions (after completion)

---

## Communication Templates

### Trial Ending

**Day 3 before:**
```
Subject: Your trial ends in 3 days

Hi [Name],

Your free trial of [Product] ends on [DATE].

What you've accomplished:
- [Achievement 1]
- [Achievement 2]

To continue without interruption:
[Subscribe Button]

Questions? Schedule a quick call: [Link]
```

### Renewal Reminder (Annual)

**30 days before:**
```
Subject: Your annual subscription renews on [DATE]

Hi [Name],

Your [Product] subscription renews in 30 days.

Details:
📅 Renewal date: [DATE]
💳 Payment method: Card ending [LAST4]
💰 Amount: $[AMOUNT]

Need to make changes?
- Update payment method: [Link]
- Change plans: [Link]
- Questions: [Contact]
```

### Win-Back (Post-Cancellation)

**Day 30 after cancel:**
```
Subject: We miss you, [Name]

Hi [Name],

It's been a month since you cancelled [Product].

We've made some improvements since you left:
- [New feature 1]
- [New feature 2]

Ready to give us another try? Here's 25% off your first 3 months:
[Return Offer Button]

Code: WELCOME25

No pressure - just wanted you to know.
```

---

## Metrics & Reporting

### Key Subscription Metrics

| Metric | Calculation | Benchmark |
|--------|-------------|-----------|
| Churn Rate | Cancelled / Total | <5% monthly |
| Retention Rate | 1 - Churn Rate | >95% monthly |
| MRR | Σ(monthly revenue) | Growth metric |
| ARPU | MRR / Active users | Value metric |
| LTV | ARPU × Avg lifespan | >3× CAC |
| Net Revenue Retention | (MRR + expansion - churn) / MRR | >100% |

### Cancellation Analysis

| Metric | How to Track |
|--------|--------------|
| Cancellation by reason | Tag all cancellations |
| Save rate by offer | A/B test retention offers |
| Time to cancel | Days from signup to cancel |
| Return rate | Cancelled who resubscribe |
| Voluntary vs involuntary | Payment fail vs explicit cancel |

---

## Compliance

### Subscription Laws

| Regulation | Requirement |
|------------|-------------|
| FTC | Clear disclosure of recurring charges |
| State ARL | Easy cancellation (CA, NY, etc.) |
| GDPR | Right to cancel, data deletion |
| PCI-DSS | Secure payment storage |

### Required Disclosures

- Total cost of subscription
- Billing frequency
- Renewal terms
- How to cancel
- Trial conversion terms

### Cancellation Requirements

- Online cancellation option required
- Same process as signup (CA law)
- Confirmation email required
- No unreasonable barriers
