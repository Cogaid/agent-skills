---
name: invoice-generator
description: Create professional invoices with proper formatting, tax calculations, and payment terms. Use when the user mentions "create invoice," "generate invoice," "billing," "send invoice," "invoice template," "payment terms," "recurring invoice," "invoice numbering," "late fees," or "accounts receivable."
metadata:
  version: 1.0.0
  category: finance-operations
---

# Invoice Generator

Create professional, compliant invoices with proper formatting, tax handling, and payment terms.

## Purpose

This skill helps you generate accurate invoices for clients and customers. It covers everything from one-time project invoices to recurring billing, handles multiple currencies and tax jurisdictions, and ensures your invoices include all legally required fields.

## Quick Start

1. **Gather client details**: Confirm billing entity, address, and tax ID
2. **Select invoice type**: One-time, recurring, milestone, or retainer
3. **Apply template**: Use the structure below with all required fields
4. **Calculate totals**: Line items + tax - discounts = amount due
5. **Set payment terms**: Choose Net 15/30/60/90 and late fee policy
6. **Generate & send**: Run `python scripts/generate_invoice.py`

## Invoice Structure Template

```
┌─────────────────────────────────────────────────────────┐
│  [YOUR COMPANY LOGO]                                    │
│  Company Name | Tax ID / EIN                            │
│  Address Line 1                                         │
│  City, State, ZIP | Country                             │
│  Phone | Email | Website                                │
├─────────────────────────────────────────────────────────┤
│  INVOICE                                                │
│  Invoice #: INV-2026-0042                               │
│  Date Issued: 2026-04-20                                │
│  Due Date: 2026-05-20                                   │
│  PO Number: PO-8871 (if applicable)                     │
├─────────────────────────────────────────────────────────┤
│  BILL TO:                                               │
│  Client Company Name                                    │
│  Attn: Contact Name                                     │
│  Address Line 1                                         │
│  City, State, ZIP | Country                             │
│  Tax ID / VAT (if applicable)                           │
├─────────────────────────────────────────────────────────┤
│  # │ Description          │ Qty │ Rate    │ Amount      │
│  ──┼──────────────────────┼─────┼─────────┼─────────────│
│  1 │ Web Design Services  │  40 │ $150.00 │  $6,000.00  │
│  2 │ Hosting (Monthly)    │   1 │  $99.00 │     $99.00  │
│  3 │ Domain Registration  │   1 │  $15.00 │     $15.00  │
├─────────────────────────────────────────────────────────┤
│                              Subtotal:      $6,114.00   │
│                              Tax (8.5%):      $519.69   │
│                              Discount (5%):  -$305.70   │
│                              ─────────────────────────  │
│                              TOTAL DUE:     $6,327.99   │
├─────────────────────────────────────────────────────────┤
│  Payment Terms: Net 30                                  │
│  Accepted Methods: Bank Transfer, Credit Card, PayPal   │
│                                                         │
│  Bank Details:                                          │
│    Bank Name: First National Bank                       │
│    Account: XXXX-XXXX-1234                              │
│    Routing: XXXXX-4567                                  │
│    SWIFT: FNBKUS33 (for international)                  │
│                                                         │
│  Notes: Thank you for your business!                    │
│  Late Payment: 1.5% monthly interest after due date     │
└─────────────────────────────────────────────────────────┘
```

## Required Fields Checklist

```
Invoice Completeness Check:
- [ ] Sender: Company name, address, tax/EIN number
- [ ] Recipient: Client name, billing address, contact
- [ ] Invoice number (unique, sequential)
- [ ] Issue date and due date
- [ ] PO number (if client requires)
- [ ] Line items with descriptions, quantities, rates
- [ ] Subtotal, tax breakdown, discounts, total due
- [ ] Currency clearly stated
- [ ] Payment methods and bank details
- [ ] Payment terms and late fee policy
- [ ] Notes or special instructions
```

## Payment Terms Reference

| Term | Due Date | Typical Use | Discount Offered |
|------|----------|-------------|------------------|
| **Due on Receipt** | Immediately | Small jobs, new clients | None |
| **Net 15** | 15 days | Ongoing services, contractors | 2/10 (2% if paid in 10 days) |
| **Net 30** | 30 days | Standard B2B, most common | 2/10 Net 30 |
| **Net 45** | 45 days | Mid-market enterprise | 1/15 |
| **Net 60** | 60 days | Large enterprise, government | Negotiable |
| **Net 90** | 90 days | Government, large procurement | Rare |
| **50/50** | 50% upfront, 50% on delivery | Projects, milestones | None |
| **Milestone** | Per deliverable | Complex projects | None |

## Currency Formatting Guide

| Currency | Symbol | Format Example | Decimal | Thousands |
|----------|--------|----------------|---------|-----------|
| USD | $ | $1,234.56 | . (dot) | , (comma) |
| EUR | € | €1.234,56 | , (comma) | . (dot) |
| GBP | £ | £1,234.56 | . (dot) | , (comma) |
| JPY | ¥ | ¥1,234 | None | , (comma) |
| INR | ₹ | ₹1,23,456.78 | . (dot) | , (comma) + lakh grouping |
| CAD | CA$ | CA$1,234.56 | . (dot) | , (comma) |
| AUD | A$ | A$1,234.56 | . (dot) | , (comma) |

**Rule**: Always display the ISO currency code (e.g., USD) alongside the symbol when invoicing internationally.

## Tax Calculation Guidance

| Scenario | Tax Treatment | Notes |
|----------|--------------|-------|
| Domestic B2B | Apply local sales tax / GST | Verify state/province rules |
| Domestic B2C | Apply sales tax | Consumer rate may differ |
| International B2B (with VAT ID) | Reverse charge (0%) | Client self-assesses; note on invoice |
| International B2C | Apply destination country VAT | May require registration |
| Tax-exempt client | 0% with exemption reference | Keep exemption cert on file |
| Digital services (EU) | Apply buyer's country VAT | OSS/IOSS rules apply |

**Tax line item format**: Always show tax rate, taxable amount, and tax amount separately.

```
Subtotal (taxable):    $5,000.00
Subtotal (non-tax):      $500.00
Sales Tax (8.5%):        $425.00
──────────────────────────────────
Total:                 $5,925.00
```

## Late Payment Terms

| Late Fee Model | Terms | Example Language |
|----------------|-------|-----------------|
| **Percentage per month** | 1-2% monthly on outstanding | "A late fee of 1.5% per month will be applied..." |
| **Flat fee** | Fixed amount per late period | "A $50 late fee applies after the due date..." |
| **Tiered** | Escalating fees | "1% after 30 days, 2% after 60 days..." |
| **Interest (APR)** | Annual rate, calculated daily | "18% APR applied daily on overdue balances..." |
| **Collection escalation** | After 90 days | "Accounts 90+ days overdue referred to collections" |

**Recommended clause**:
> Payment is due within [N] days of invoice date. A late fee of 1.5% per month (18% APR) will be assessed on balances unpaid after the due date. Client is responsible for all collection costs, including reasonable attorney fees.

## Invoice Numbering Conventions

| Convention | Format | Example | Best For |
|------------|--------|---------|----------|
| Sequential | INV-0001 | INV-0042 | Small businesses |
| Year-prefixed | INV-YYYY-NNNN | INV-2026-0042 | Easy annual tracking |
| Client-coded | INV-CLI-NNNN | INV-ACM-0012 | Multi-client businesses |
| Project-coded | PRJ-NNNN-INV-NN | PRJ-0015-INV-03 | Project-based billing |
| Date-based | INV-YYYYMMDD-NN | INV-20260420-01 | High-volume billing |

**Rules**: Never reuse numbers. Never leave gaps unexplained. Store the sequence in your accounting system.

## Recurring Invoice Setup

```
Recurring Invoice Configuration:
─────────────────────────────────
Client:           [Client Name]
Service:          [Description]
Amount:           $[X,XXX.XX] per [period]
Frequency:        [ ] Weekly  [ ] Bi-weekly  [ ] Monthly
                  [ ] Quarterly  [ ] Annually
Start Date:       [YYYY-MM-DD]
End Date:         [YYYY-MM-DD] or [ ] Ongoing
Auto-send:        [ ] Yes  [ ] No (draft for review)
Payment Method:   [ ] Auto-charge on file  [ ] Invoice & wait
Escalation:       [ ] Annual rate increase of ____%
Notes:            [Special terms for recurring billing]
```

## Scripts & Tools

**generate_invoice.py**: Create an invoice from parameters
```bash
python scripts/generate_invoice.py --client "Acme Corp" --items items.json --terms net30
# Output: PDF invoice saved to invoices/INV-2026-0042.pdf
```

**send_invoice.py**: Email invoice to client
```bash
python scripts/send_invoice.py --invoice INV-2026-0042 --email billing@acme.com
# Output: Invoice emailed with tracking confirmation
```

**invoice_status.py**: Check payment status across all invoices
```bash
python scripts/invoice_status.py --status overdue
# Output: Table of overdue invoices with aging (30/60/90 days)
```

**recurring_setup.py**: Configure recurring invoices
```bash
python scripts/recurring_setup.py --client "Acme Corp" --amount 2500 --frequency monthly
# Output: Recurring invoice scheduled, next: 2026-05-01
```

## Best Practices

1. **Send promptly**: Invoice within 24 hours of delivery or month-end
2. **Be specific**: Detailed line items reduce disputes and speed payment
3. **Match PO numbers**: Always reference the client's purchase order if one exists
4. **Track everything**: Log invoice sent date, follow-up dates, payment received
5. **Follow up systematically**: Day 1 (send), Day 7 (reminder), Day 30 (overdue notice), Day 60 (final notice)
6. **Keep copies**: Store all invoices with a consistent naming convention for audit readiness
7. **Separate taxable items**: Some line items may be tax-exempt; break them out clearly
8. **Offer early payment discounts**: 2/10 Net 30 accelerates cash flow significantly
9. **Automate recurring billing**: Reduce manual work and late sends with automation
10. **Review before sending**: Typos in amounts or addresses erode professionalism
