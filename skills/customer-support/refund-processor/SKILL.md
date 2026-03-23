# Refund Processor

---
name: refund-processor
description: Process customer refund requests efficiently and fairly. Use when the user mentions "refund request," "money back," "process refund," "refund policy," "refund approval," "chargeback," or "payment reversal."
metadata:
  version: 1.0.0
  category: customer-support
---

## Purpose

Handle refund requests with consistency, fairness, and efficiency while maintaining customer relationships and following company policies.

## Quick Reference

### Refund Decision Framework

| Factor | Weight | Consider |
|--------|--------|----------|
| **Time Since Purchase** | High | Within policy window? |
| **Product Condition** | High | Used, damaged, or as-is? |
| **Customer History** | Medium | Previous refunds, loyalty level |
| **Reason Given** | Medium | Defect vs. preference |
| **Order Value** | Low | Cost-benefit of approval |

### Standard Refund Timelines

| Method | Processing Time | Customer Visibility |
|--------|-----------------|---------------------|
| Original Payment | 3-5 business days | Bank statement |
| Store Credit | Instant | Account balance |
| Gift Card | 1 business day | Email delivery |
| Check | 7-10 business days | Mail |

## Workflow Checklist

### 1. Request Intake
- [ ] Verify customer identity
- [ ] Locate order/transaction
- [ ] Document refund reason
- [ ] Check within policy window
- [ ] Note product condition (if applicable)

### 2. Eligibility Assessment
- [ ] Review refund policy applicability
- [ ] Check for exceptions (final sale, digital goods)
- [ ] Calculate eligible refund amount
- [ ] Consider restocking fees if applicable
- [ ] Check shipping cost responsibility

### 3. Decision & Approval
- [ ] Determine approval level needed
- [ ] Document decision rationale
- [ ] Get supervisor approval if required
- [ ] Calculate final refund amount

### 4. Processing
- [ ] Select refund method
- [ ] Process in payment system
- [ ] Generate refund confirmation
- [ ] Update inventory (if return)
- [ ] Send customer notification

### 5. Follow-Up
- [ ] Verify refund posted
- [ ] Handle any issues
- [ ] Document case closure
- [ ] Update customer record

## Refund Categories

### Full Refund Scenarios
- Product defect/malfunction
- Wrong item shipped
- Item never received
- Significant description discrepancy
- Within unconditional return window

### Partial Refund Scenarios
- Minor issues with product
- Late delivery (service credit)
- Missing components
- Used but within policy
- Customer preference change

### Refund Denial Scenarios
- Outside return window
- Final sale items
- Digital goods accessed
- Customer damage
- Policy exclusions apply

## Communication Templates

→ See `templates/refund_templates.md` for approval, denial, and partial refund templates

## Policy Reference

→ See `reference.md` for detailed refund policies and exception handling

## Scripts & Tools

| Script | Purpose |
|--------|---------|
| `scripts/process_refund.py` | Calculate refund amounts and generate documentation |
| `scripts/refund_analyzer.py` | Analyze refund patterns and identify trends |

## Escalation Triggers

Escalate to supervisor when:
- Refund amount exceeds $500
- Customer disputes denial
- Third refund request in 90 days
- Potential fraud indicators
- Policy exception requested
- Chargeback threat

## Key Metrics

| Metric | Target |
|--------|--------|
| Processing Time | < 24 hours |
| First Contact Resolution | > 85% |
| Policy Adherence | 100% |
| Customer Satisfaction | > 80% |
| Fraud Prevention Rate | > 95% |
