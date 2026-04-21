# Invoice Generator - Reference Documentation

## Invoice Legal Requirements by Jurisdiction

### United States
- **Federal**: No uniform federal invoice format requirement, but IRS requires records for tax deductions
- **State Sales Tax**: Each state sets its own rules; most require tax amount, rate, and taxable vs. non-taxable line items
- **EIN / Tax ID**: Required on invoices for B2B transactions and 1099 reporting
- **Record Retention**: IRS recommends keeping invoices for 3-7 years depending on the situation

### European Union (VAT Invoices)
Required fields under EU VAT Directive (2006/112/EC):
1. Sequential invoice number
2. Date of issue
3. Supplier name, address, and VAT identification number
4. Customer name, address, and VAT identification number (for B2B)
5. Description of goods or services
6. Quantity and unit price (excluding VAT)
7. VAT rate applied
8. VAT amount in the currency of the transaction
9. Total amount payable
10. Reference to any exemption or reverse charge

### United Kingdom (Post-Brexit)
- VAT invoices must include UK VAT registration number
- Simplified invoices allowed for supplies under GBP 250
- Full invoices required for higher amounts with all EU-equivalent fields
- Reverse charge applies to certain construction services

### India (GST)
- GSTIN of supplier and recipient required
- HSN/SAC codes for goods/services
- Place of supply
- CGST, SGST, IGST breakdown
- E-invoicing mandatory for businesses above turnover threshold

### Canada (GST/HST)
- GST/HST registration number required
- Provincial sales tax (PST) shown separately where applicable
- Invoice must clearly state whether prices include or exclude tax

## Payment Terms Deep Dive

### Early Payment Discounts
Early payment discount notation follows the format: `discount% / days Net total_days`

| Notation | Meaning | Effective Annual Rate |
|----------|---------|----------------------|
| 1/10 Net 30 | 1% discount if paid within 10 days, otherwise net 30 | ~18.2% |
| 2/10 Net 30 | 2% discount if paid within 10 days, otherwise net 30 | ~36.7% |
| 2/10 Net 45 | 2% discount if paid within 10 days, otherwise net 45 | ~21.3% |
| 3/10 Net 60 | 3% discount if paid within 10 days, otherwise net 60 | ~22.3% |

**Effective annual rate formula**:
```
EAR = (Discount / (1 - Discount)) x (365 / (Full_Days - Discount_Days))
```

Example: 2/10 Net 30
```
EAR = (0.02 / 0.98) x (365 / 20) = 0.0204 x 18.25 = 37.2%
```

### Days Sales Outstanding (DSO)
```
DSO = (Accounts Receivable / Total Credit Sales) x Number of Days
```

Industry benchmarks:
| Industry | Average DSO |
|----------|-------------|
| Technology / SaaS | 40-60 days |
| Manufacturing | 45-65 days |
| Professional Services | 35-55 days |
| Retail / E-commerce | 20-35 days |
| Construction | 60-90 days |
| Healthcare | 50-70 days |
| Government Contracts | 60-120 days |

## Invoice Delivery Methods

| Method | Speed | Cost | Proof of Delivery | Best For |
|--------|-------|------|-------------------|----------|
| Email (PDF) | Instant | Free | Read receipt / tracking | Standard B2B |
| Online portal | Instant | Low (platform fee) | Portal timestamp | High volume |
| E-invoicing (EDI/XML) | Instant | Medium (setup cost) | System confirmation | Enterprise |
| Postal mail | 3-7 days | $1-5 per invoice | Certified mail option | Legal requirements |
| AP automation (Coupa, Bill.com) | Near instant | Per-transaction fee | System confirmation | Mid-market+ |

## Common Invoice Disputes and Resolution

| Dispute Type | Common Cause | Prevention | Resolution |
|-------------|-------------|------------|------------|
| Amount mismatch | Rate or quantity error | PO matching before invoicing | Issue credit memo and corrected invoice |
| Duplicate invoice | System error or re-send | Unique invoice numbers, dedup checks | Void duplicate, confirm correct invoice |
| Missing PO number | Invoiced without client PO | Require PO before starting work | Obtain PO retroactively, reissue |
| Wrong billing entity | Multi-entity client | Confirm legal entity at engagement start | Void and reissue to correct entity |
| Tax calculation error | Wrong rate or jurisdiction | Tax engine or manual verification | Issue credit memo for difference |
| Scope dispute | Unclear SOW | Detailed line items matching SOW | Reference SOW, escalate if needed |
| Late delivery claim | Client claims late delivery | Delivery receipts and timestamps | Provide delivery evidence |

## Credit Memo and Adjustment Standards

A credit memo is a negative invoice that reduces the amount owed. Use when:
- Correcting an overbilling
- Applying a negotiated discount retroactively
- Returning goods or cancelling services
- Resolving a billing dispute

**Credit memo must include**:
1. Reference to original invoice number
2. Reason for credit
3. Line items being credited
4. Credit amount (shown as negative)
5. New balance due

## Accounts Receivable Aging Buckets

| Bucket | Days Outstanding | Risk Level | Action |
|--------|-----------------|------------|--------|
| Current | 0-30 days | Low | Normal follow-up |
| 30 days | 31-60 days | Medium | Send reminder, call contact |
| 60 days | 61-90 days | High | Escalate to management, formal notice |
| 90 days | 91-120 days | Very High | Final notice, consider collections |
| 120+ days | >120 days | Critical | Collections agency or write-off |

**Bad debt provision formula**:
```
Provision = Sum of (Bucket Balance x Expected Loss Rate)
Current: 1% | 30-day: 5% | 60-day: 15% | 90-day: 35% | 120+: 60%
```

## Multi-Currency Invoicing

### Exchange Rate Handling
- **Invoice date rate**: Use the exchange rate on the date the invoice is issued
- **Payment date rate**: Actual rate when payment is received
- **Contracted rate**: Fixed rate agreed in the contract (eliminates FX risk)
- **Hedging**: Forward contracts to lock in rates for large, predictable receivables

### Foreign Exchange Gain/Loss
```
FX Gain/Loss = Payment Amount (in home currency) - Invoice Amount (in home currency at invoice date rate)
```

If positive: FX gain (record as income)
If negative: FX loss (record as expense)

## Regulatory Compliance Checklist

- [ ] Invoice number is unique and sequential (no gaps)
- [ ] Seller legal name and tax ID present
- [ ] Buyer legal name and tax ID present (where required)
- [ ] Date of issue and due date clearly stated
- [ ] Line items with description, quantity, unit price
- [ ] Tax rate and amount shown per line or in summary
- [ ] Total amount due in stated currency
- [ ] Payment instructions included
- [ ] Compliant with local e-invoicing mandates (if applicable)
- [ ] Archived for required retention period
