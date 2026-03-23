# Expense Tracker

---
name: expense-tracker
description: Track and categorize expenses for budgeting and reimbursement. Use when the user mentions "expense," "receipt," "spending," "budget tracking," "reimbursement," "expense report," or "cost tracking."
metadata:
  version: 1.0.0
  category: personal-assistance
---

## Purpose

Track, categorize, and analyze expenses for personal budgeting, business reimbursements, and financial planning.

## Quick Reference

### Expense Categories

| Category | Examples | Tax Deductible? |
|----------|----------|-----------------|
| Travel | Flights, hotels, transport | Usually yes |
| Meals | Client dinners, team lunches | Partially |
| Office | Supplies, equipment | Usually yes |
| Software | Subscriptions, licenses | Usually yes |
| Marketing | Ads, events, swag | Usually yes |
| Professional | Training, conferences | Usually yes |
| Utilities | Phone, internet | Partially |
| Other | Miscellaneous | Varies |

### Quick Entry Format

```
[Date] | [Amount] | [Category] | [Description] | [Vendor]
```

Example:
```
2025-01-15 | $45.00 | Meals | Client lunch | Cafe Milano
```

## Workflow Checklist

### 1. Capture
- [ ] Record date of expense
- [ ] Note amount (including tax/tip)
- [ ] Save receipt (photo/PDF)
- [ ] Identify category
- [ ] Add description/notes

### 2. Categorize
- [ ] Assign expense category
- [ ] Flag if reimbursable
- [ ] Mark tax-deductible items
- [ ] Note payment method
- [ ] Link to project/client if applicable

### 3. Document
- [ ] Attach receipt image
- [ ] Add business purpose
- [ ] Note attendees (for meals)
- [ ] Record approval (if needed)

### 4. Review
- [ ] Verify amounts match receipts
- [ ] Check categorization accuracy
- [ ] Ensure all required fields
- [ ] Submit for approval/reimbursement

### 5. Report
- [ ] Generate expense summary
- [ ] Export for accounting
- [ ] Track reimbursement status
- [ ] Archive completed reports

## Expense Entry Fields

### Required Fields
- **Date**: When expense occurred
- **Amount**: Total including tax/tip
- **Category**: Expense type
- **Description**: What it was for

### Optional Fields
- **Vendor**: Where purchased
- **Payment Method**: Card, cash, etc.
- **Project/Client**: If billable
- **Attendees**: For meal expenses
- **Receipt**: Image/PDF attachment
- **Notes**: Additional context

## Budget Tracking

### Monthly Budget Template

| Category | Budget | Spent | Remaining | % Used |
|----------|--------|-------|-----------|--------|
| Travel | $500 | | | |
| Meals | $200 | | | |
| Office | $100 | | | |
| Software | $150 | | | |
| **Total** | | | | |

## Expense Templates

→ See `templates/expense_templates.md` for expense reports and receipts

## Reference Guide

→ See `reference.md` for policies, tax deductions, and best practices

## Scripts & Tools

| Script | Purpose |
|--------|---------|
| `scripts/expense_manager.py` | Track and categorize expenses |
| `scripts/expense_report.py` | Generate expense reports |

## Best Practices

### Do's
- Record expenses immediately
- Always save receipts
- Use consistent categories
- Note business purpose
- Review weekly

### Don'ts
- Wait to record expenses
- Throw away receipts
- Mix personal/business
- Estimate amounts
- Skip documentation

## Reimbursement Tips

- Submit within policy timeframe
- Include all required fields
- Attach clear receipt images
- Add business justification
- Follow approval chain
