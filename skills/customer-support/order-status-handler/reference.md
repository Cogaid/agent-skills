# Order Status Handler Reference

## Shipping & Delivery Standards

### Shipping Methods

| Method | Transit Time | Cost Tier | Tracking |
|--------|-------------|-----------|----------|
| Economy | 5-7 business days | Free/$low | Basic |
| Standard | 3-5 business days | Medium | Full |
| Express | 2-3 business days | High | Full + updates |
| Overnight | 1 business day | Premium | Real-time |
| Same Day | Same day | Premium+ | Real-time |

### Processing Times

| Order Type | Processing | Ships By |
|------------|------------|----------|
| In-stock | 1-2 business days | Next business day |
| Pre-order | After release date | 1-2 days post-release |
| Backorder | When available | 1-2 days after restock |
| Custom/Personalized | 3-5 business days | After production |
| International | 2-3 business days | After customs clearance |

---

## Carrier Policies

### USPS

**Service Levels:**
| Service | Transit | Tracking | Insurance |
|---------|---------|----------|-----------|
| First Class | 2-5 days | Yes | Up to $100 |
| Priority | 1-3 days | Yes | Up to $100 |
| Priority Express | 1-2 days | Yes | Up to $100 |
| Ground Advantage | 2-5 days | Yes | Up to $100 |

**Exception Handling:**
- Undeliverable: Held at local post office for 15 days
- Return to sender: After 15 days or address issue
- Claims: File within 60 days of mailing date

### UPS

**Service Levels:**
| Service | Transit | Tracking | Insurance |
|---------|---------|----------|-----------|
| Ground | 1-5 days | Yes | Declared value |
| 3 Day Select | 3 days | Yes | Declared value |
| 2nd Day Air | 2 days | Yes | Declared value |
| Next Day Air | 1 day | Yes | Declared value |

**Exception Handling:**
- 3 delivery attempts before return
- Package hold available at UPS Store
- Claims: File within 60 days

### FedEx

**Service Levels:**
| Service | Transit | Tracking | Insurance |
|---------|---------|----------|-----------|
| Ground | 1-5 days | Yes | Declared value |
| Express Saver | 3 days | Yes | Declared value |
| 2Day | 2 days | Yes | Declared value |
| Priority Overnight | 1 day | Yes | Declared value |

**Exception Handling:**
- 3 delivery attempts
- Hold at FedEx location available
- Claims: File within 21 days (domestic)

---

## Status Definitions

### Order Lifecycle

```
Order Placed
    ↓
Payment Confirmed
    ↓
Processing ←→ On Hold (if issues)
    ↓
Shipped
    ↓
In Transit
    ↓
Out for Delivery
    ↓
Delivered
```

### Detailed Status Codes

| Status | System Code | Customer Message |
|--------|-------------|------------------|
| Order Received | ORD_RCV | "We've received your order" |
| Payment Pending | PAY_PND | "Awaiting payment confirmation" |
| Payment Failed | PAY_FAIL | "Payment issue - please update" |
| Processing | PROC | "Preparing your order" |
| On Hold - Stock | HOLD_STK | "Item temporarily unavailable" |
| On Hold - Address | HOLD_ADDR | "Please verify shipping address" |
| On Hold - Fraud | HOLD_FRD | "Order under review" |
| Ready to Ship | RTS | "Ready for pickup by carrier" |
| Shipped | SHIP | "Your order is on the way!" |
| In Transit | TRNS | "Package in transit" |
| Out for Delivery | OFD | "Arriving today" |
| Delivery Attempted | DEL_ATT | "Delivery attempted" |
| Delivered | DEL | "Delivered" |
| Returned to Sender | RTS | "Package returning to us" |
| Cancelled | CANC | "Order cancelled" |

---

## Exception Handling

### Delivery Exceptions

| Exception | Cause | Resolution |
|-----------|-------|------------|
| Address Unknown | Invalid address | Verify with customer |
| Business Closed | After hours delivery | Reschedule or hold |
| Customer Not Available | No one to receive | Leave notice, reattempt |
| Weather Delay | Severe weather | Wait, no action needed |
| Mechanical Delay | Vehicle issues | Wait, no action needed |
| Customs Hold | International clearance | Provide documentation |
| Damaged in Transit | Package damaged | File claim, reship |
| Lost in Transit | Cannot locate | Investigation + reship |

### Resolution Timeframes

| Issue | Investigation | Resolution |
|-------|---------------|------------|
| Tracking not updating | 24-48 hours | Contact carrier |
| Delivery exception | Same day | Carrier callback |
| Missing package | 3-5 business days | Replacement/refund |
| Damaged package | 1-2 business days | Replacement/refund |
| Wrong item | Same day | Correct item shipped |

---

## Investigation Process

### Missing Package Protocol

**Day 0 (Reported):**
1. Verify delivery address
2. Check tracking details
3. Confirm delivery attempt/completion
4. Ask customer to check:
   - All entrances
   - With neighbors
   - Building mailroom/office
   - Behind bushes/hidden areas

**Day 1-2:**
1. Contact carrier for GPS verification
2. Request driver statement
3. Check delivery photo (if available)

**Day 3-5:**
1. File official carrier claim
2. Process replacement order OR
3. Issue refund

### Damaged Package Protocol

**Immediate:**
1. Request photos of:
   - Outer packaging
   - Inner packaging
   - Damaged product
   - Shipping label
2. Determine damage extent

**Resolution:**
| Damage Level | Action |
|--------------|--------|
| Minor cosmetic | Partial refund (10-25%) |
| Functional but damaged | Replacement or 50% refund |
| Non-functional | Full replacement |
| Dangerous (broken glass, etc.) | Immediate replacement + disposal instructions |

---

## Communication Templates

### Proactive Notifications

**Shipped:**
```
Subject: Your order is on the way! 📦

Hi [Name],

Great news! Order #[ORDER] just shipped.

Tracking: [TRACKING_NUMBER]
Carrier: [CARRIER]
Expected: [DATE_RANGE]

Track your package: [LINK]
```

**Delivery Exception:**
```
Subject: Update on your delivery

Hi [Name],

There's been a small delay with order #[ORDER].

What happened: [EXCEPTION_REASON]
New expected delivery: [NEW_DATE]

[ACTION_IF_NEEDED]

We're monitoring this closely.
```

**Delivered:**
```
Subject: Your order has arrived! 🎉

Hi [Name],

Order #[ORDER] was delivered today at [TIME].

Delivered to: [LOCATION]

Not received? Let us know within 24 hours.
```

---

## Metrics & SLAs

### Response Time SLAs

| Channel | First Response | Resolution |
|---------|---------------|------------|
| Chat | < 1 minute | Same session |
| Email | < 4 hours | 24 hours |
| Phone | < 2 minutes hold | Same call |
| Social | < 1 hour | 4 hours |

### Key Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| WISMO rate | < 15% of contacts | Track "where is my order" |
| First contact resolution | > 80% | Resolved without escalation |
| Shipping accuracy | > 99.5% | Correct items, addresses |
| Delivery success | > 98% | First attempt delivery |
| Claims rate | < 0.5% | Claims filed / orders |

---

## International Shipping

### Customs & Duties

| Destination Type | Duties Paid By | Typical Delay |
|------------------|----------------|---------------|
| DDP (Delivered Duty Paid) | Seller | None |
| DDU (Delivered Duty Unpaid) | Buyer | 1-3 days |

### Common Customs Issues

| Issue | Resolution |
|-------|------------|
| Documentation missing | Provide commercial invoice |
| Value dispute | Provide purchase receipt |
| Prohibited item | Cannot ship, refund |
| Held for inspection | Wait for clearance |

### Transit Time by Region

| Region | Economy | Express |
|--------|---------|---------|
| Canada | 5-10 days | 2-4 days |
| Europe | 7-14 days | 3-5 days |
| Asia Pacific | 10-20 days | 4-7 days |
| Latin America | 10-21 days | 5-10 days |
| Middle East | 10-21 days | 5-8 days |

---

## Fraud Prevention

### Red Flags

| Indicator | Risk Level | Action |
|-----------|------------|--------|
| Rush shipping to new address | Medium | Verify customer |
| Multiple failed payment attempts | High | Hold order |
| Shipping ≠ billing address | Low-Medium | Verify if high value |
| International high-value | Medium | Additional verification |
| Repeated "not received" claims | High | Flag account |

### Verification Steps

1. Confirm email matches account
2. Check order history
3. Verify payment method ownership
4. Call customer if high risk
5. Hold shipment if unverified
