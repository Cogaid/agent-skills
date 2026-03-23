# Refund Processor Reference Guide

## Contents
- Refund Policies
- Exception Handling
- Fraud Prevention
- System Procedures
- Dispute Resolution

---

## Refund Policies

### Standard Return Policy

**Window:** 30 days from delivery date

**Conditions:**
- Original packaging preferred
- Tags attached (for apparel)
- Proof of purchase required
- No signs of excessive use

**Exceptions:**
- Electronics: 15 days
- Perishables: 48 hours
- Custom items: Non-refundable
- Digital goods: Non-refundable after download

### Extended Holiday Policy

**Period:** Nov 1 - Dec 31 purchases
**Return Window:** Until Jan 31 of following year

---

## Refund Calculation

### Full Refund Components

```
Full Refund = Product Price + Original Shipping (if applicable) + Tax
```

**Include shipping in refund when:**
- Company error (wrong item, defective)
- Item never arrived
- Significant misrepresentation

### Partial Refund Calculation

```
Partial Refund = Product Price - Restocking Fee - Shipping - Damage Deduction
```

**Restocking Fees:**
| Category | Fee |
|----------|-----|
| Electronics | 15% |
| Large Items | 20% |
| Opened Software | 50% |
| Standard Items | 0% |

### Prorated Refunds

For subscription/service refunds:

```
Prorated Amount = (Unused Days / Total Days) × Total Paid
```

---

## Exception Handling

### Good Faith Exceptions

Consider approving outside policy when:
- Long-term customer (2+ years)
- First refund request ever
- Genuine hardship situation
- Small dollar amount (< $25)
- Potential for future business

**Document exception with:**
```
EXCEPTION APPROVAL
Reason: [Brief explanation]
Customer Value: [Lifetime value, loyalty status]
Business Justification: [Why approved]
Future Prevention: [N/A or action item]
Approved By: [Name/ID]
```

### Hard Limits (No Exceptions)

- Final sale items marked at purchase
- Items returned after 90 days
- Digital content fully consumed
- Clear customer abuse
- Suspected fraud

---

## Fraud Prevention

### Red Flags

**Customer Behavior:**
- Multiple refund requests in short period
- Returns only high-value items
- Different billing/shipping addresses
- New account with immediate return
- Claims items never arrived frequently

**Transaction Patterns:**
- Multiple payment methods declined
- Order value significantly above average
- Shipping to freight forwarders
- Multiple orders to same address, different names

### Fraud Investigation Steps

1. **Flag the account** - Add internal note
2. **Review history** - Check all orders and returns
3. **Verify identity** - Request additional verification
4. **Document everything** - Screenshot evidence
5. **Escalate if needed** - Send to fraud team

### Friendly Fraud (Chargebacks)

**When customer disputes with bank:**

1. Gather documentation:
   - Order confirmation
   - Shipping/delivery proof
   - Customer communications
   - Refund policy shown at purchase

2. Respond within deadline (usually 7-14 days)

3. Submit representment if evidence supports

---

## System Procedures

### Refund Processing Steps

**In Payment System:**

```
1. Access Order → [Order ID]
2. Select "Refund/Return"
3. Choose Refund Type:
   - Full Refund
   - Partial Refund (enter amount)
   - Store Credit
4. Select Reason Code
5. Add Internal Notes
6. Process Refund
7. Confirm Transaction ID
```

### Reason Codes

| Code | Description |
|------|-------------|
| RET01 | Standard return - customer preference |
| RET02 | Defective product |
| RET03 | Wrong item shipped |
| RET04 | Item not received |
| RET05 | Damaged in shipping |
| RET06 | Quality not as expected |
| RET07 | Late delivery |
| RET08 | Duplicate order |
| RET09 | Pricing error |
| RET10 | Policy exception - goodwill |

### Documentation Requirements

**All refunds must include:**
- Order number
- Refund amount
- Reason code
- Customer communication summary
- Agent ID
- Timestamp

**Exceptions additionally require:**
- Supervisor approval
- Business justification
- Customer value assessment

---

## Dispute Resolution

### Initial Denial Response

**When denying a refund:**

1. Explain policy clearly
2. Reference specific exclusion
3. Offer alternatives
4. Document thoroughly
5. Provide escalation path

### Customer Appeals

**First Level:**
- Review original decision
- Check for new information
- Consider goodwill exception
- Handled by senior agent

**Second Level:**
- Supervisor review
- Full case analysis
- Final company decision
- Must respond within 48 hours

### Legal/Regulatory Considerations

**Consumer Protection Laws:**
- Some items have mandatory return rights
- Digital goods cooling-off periods vary by region
- Credit card protections may override policy

**Document for legal:**
- Any threat of legal action
- BBB complaints
- Social media escalation threats
- Regulatory body mentions

---

## Refund Method Selection

### Decision Matrix

| Scenario | Recommended Method |
|----------|-------------------|
| Customer requests original | Original payment |
| Faster resolution needed | Store credit |
| Gift purchase | Gift card |
| Original method unavailable | Store credit → Check |
| Suspected fraud | None without approval |

### Processing Timeline by Method

**Credit/Debit Card:**
- Processing: Immediate to 24 hours
- Bank posting: 3-5 business days
- Statement reflection: Next billing cycle

**PayPal/Digital Wallets:**
- Processing: Immediate
- Account balance: 24-48 hours

**Store Credit:**
- Processing: Immediate
- Available: Instant

**Check:**
- Processing: 1-2 business days
- Mailing: 3-5 business days
- Clearance: 5-7 business days

---

## Quality Assurance

### Refund Review Checklist

- [ ] Correct customer/order identified
- [ ] Amount calculated correctly
- [ ] Tax handled appropriately
- [ ] Reason code accurate
- [ ] Notes are clear and complete
- [ ] Customer notified
- [ ] Internal documentation complete

### Audit Triggers

Refunds automatically flagged for audit:
- Amount > $500
- Third refund to same customer in 90 days
- Exception approvals
- Supervisor overrides
- Customer disputes decision

---

## Performance Standards

### Individual Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Processing Time | < 4 hours | Ticket open to close |
| Accuracy | > 99% | Correct calculations |
| Policy Adherence | 100% | Audited samples |
| Documentation | Complete | All fields filled |

### Team Metrics

| Metric | Target |
|--------|--------|
| Same-Day Processing | > 90% |
| Escalation Rate | < 10% |
| Customer Satisfaction | > 85% |
| Dispute Win Rate | > 70% |

---

## Common Scenarios

### Scenario 1: Standard Return

```
Customer: I want to return this shirt, I bought it last week.
Action: Verify within 30 days, confirm condition, process full refund
```

### Scenario 2: Outside Window

```
Customer: I bought this 45 days ago but just opened it.
Action: Explain policy, consider exception if first request, offer store credit
```

### Scenario 3: Used Product

```
Customer: This doesn't work for me, I used it twice.
Action: Accept return, consider restocking fee, partial refund
```

### Scenario 4: Defective Item

```
Customer: This was broken when I opened it.
Action: Full refund including shipping, report to quality team
```

### Scenario 5: Gift Returns

```
Customer: I received this as a gift and want to return it.
Action: Verify gift receipt, issue store credit or gift card
```
