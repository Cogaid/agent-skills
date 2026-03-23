# Order Status Handler

---
name: order-status-handler
description: Handle order status inquiries, shipping updates, and delivery issues. Use when customers ask about "order status," "where is my order," "tracking," "shipping," "delivery," "package," or "shipment."
metadata:
  version: 1.0.0
  category: customer-support
---

## Purpose

Provide accurate, timely order status information and resolve delivery-related issues efficiently.

## Quick Reference

### Order Status Types

| Status | Description | Customer Action |
|--------|-------------|-----------------|
| Processing | Order received, preparing | Wait 1-2 business days |
| Shipped | In transit to destination | Track with provided link |
| Out for Delivery | With local carrier | Available today |
| Delivered | Confirmed delivery | Contact if not received |
| On Hold | Issue needs resolution | Contact support |
| Cancelled | Order cancelled | Refund processing |

### Common Issues & Solutions

| Issue | First Response | Escalation Trigger |
|-------|---------------|-------------------|
| Tracking not updating | Check carrier status | >5 days no update |
| Delivery attempted | Schedule redelivery | 3rd failed attempt |
| Package lost | File carrier claim | Confirmed lost |
| Wrong address | Intercept if possible | Already delivered |
| Damaged package | Photo request + replacement | High value items |

## Workflow

### 1. Identify Order
```
Required Information:
- Order number OR
- Email address + name OR
- Phone number + last 4 of card

Verify:
□ Customer identity confirmed
□ Order found in system
□ Current status retrieved
```

### 2. Status Communication

**Template: Order in Transit**
```
Hi [Name],

Great news! Your order #[ORDER] is on its way.

📦 Current Status: [STATUS]
🚚 Carrier: [CARRIER]
📍 Last Location: [LOCATION]
📅 Expected Delivery: [DATE]

Track your package: [TRACKING_LINK]

[If delayed: We apologize for the delay. Here's what we know...]

Need anything else? Just reply to this message.
```

**Template: Delivery Issue**
```
Hi [Name],

I understand you're having trouble with your delivery. Let me help.

Order #[ORDER]
Issue: [ISSUE_TYPE]

Here's what I'm doing to resolve this:
1. [ACTION_1]
2. [ACTION_2]

Next steps for you:
- [CUSTOMER_ACTION]

I'll follow up by [TIMEFRAME] with an update.
```

### 3. Issue Resolution Matrix

| Scenario | Immediate Action | Resolution Time |
|----------|-----------------|-----------------|
| Where is my order? | Provide tracking | Instant |
| Tracking stuck | Contact carrier | 24-48 hours |
| Marked delivered, not received | Verify address, check with neighbors | 24 hours |
| Package damaged | Request photos, process replacement | 1-2 days |
| Wrong item sent | Arrange return + correct shipment | 2-3 days |
| Address change needed | Check if interceptable | Same day if possible |

## Decision Tree

```
Customer Inquiry
    │
    ├─→ "Where is my order?"
    │       │
    │       ├─→ Order found → Provide status + tracking
    │       └─→ Order not found → Verify details, check alternatives
    │
    ├─→ "Package not received"
    │       │
    │       ├─→ Tracking shows delivered
    │       │       │
    │       │       ├─→ < 24 hours → Wait, check neighbors
    │       │       └─→ > 24 hours → Investigation
    │       │
    │       └─→ Tracking shows in transit
    │               │
    │               ├─→ Within delivery window → Reassure
    │               └─→ Past delivery window → Escalate to carrier
    │
    ├─→ "Package damaged"
    │       │
    │       ├─→ Visible damage → Request photos
    │       └─→ Contents damaged → Request photos + process claim
    │
    └─→ "Cancel/change order"
            │
            ├─→ Not shipped → Cancel/modify
            └─→ Already shipped → Intercept or return process
```

## Carrier-Specific Information

### Major Carriers

| Carrier | Tracking Page | Typical Transit | Contact |
|---------|--------------|-----------------|---------|
| USPS | usps.com/tracking | 2-5 days | 1-800-275-8777 |
| UPS | ups.com/track | 1-5 days | 1-800-742-5877 |
| FedEx | fedex.com/tracking | 1-5 days | 1-800-463-3339 |
| DHL | dhl.com/tracking | 2-7 days | 1-800-225-5345 |

### Status Code Reference

| Code | Meaning | Customer-Friendly |
|------|---------|-------------------|
| IT | In Transit | "On the way" |
| OFD | Out for Delivery | "Arriving today" |
| DEL | Delivered | "Delivered" |
| EXC | Exception | "Delayed - we're checking" |
| RTN | Returned to Sender | "Coming back to us" |

## Scripts & Tools

| Script | Purpose |
|--------|---------|
| `scripts/order_lookup.py` | Look up order status and tracking |
| `scripts/delivery_estimator.py` | Estimate delivery windows |

## Best Practices

### Do's
- Provide specific tracking information
- Set realistic delivery expectations
- Proactively notify of delays
- Offer solutions, not excuses
- Follow up on unresolved issues

### Don'ts
- Promise delivery dates you can't control
- Blame the carrier without verification
- Close tickets without resolution
- Ignore delivery exceptions
- Make customers repeat information

## Escalation Triggers

Escalate immediately when:
- Package confirmed lost (carrier investigation complete)
- High-value order (>$500) with issues
- Third delivery attempt failed
- Customer requests supervisor
- Potential fraud indicators
- Media/legal threats

## Reference

→ See `templates/status_templates.md` for response templates
→ See `reference.md` for carrier policies and SLAs
