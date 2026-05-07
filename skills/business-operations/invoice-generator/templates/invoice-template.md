# Invoice Template

## Standard Invoice

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  [COMPANY LOGO]                                             │
│                                                             │
│  {{company_name}}                                           │
│  Tax ID / EIN: {{company_tax_id}}                           │
│  {{company_address_line1}}                                  │
│  {{company_city}}, {{company_state}} {{company_zip}}        │
│  {{company_country}}                                        │
│  Phone: {{company_phone}}                                   │
│  Email: {{company_email}}                                   │
│  Website: {{company_website}}                               │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  INVOICE                                                    │
│                                                             │
│  Invoice Number:   {{invoice_number}}                       │
│  Date Issued:      {{issue_date}}                           │
│  Due Date:         {{due_date}}                             │
│  PO Number:        {{po_number}}                            │
│  Currency:         {{currency_code}}                        │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  BILL TO:                                                   │
│  {{client_company_name}}                                    │
│  Attn: {{client_contact_name}}                              │
│  {{client_address_line1}}                                   │
│  {{client_city}}, {{client_state}} {{client_zip}}           │
│  {{client_country}}                                         │
│  Tax ID / VAT: {{client_tax_id}}                            │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  #  │ Description              │ Qty  │ Rate      │ Amount │
│  ───┼──────────────────────────┼──────┼───────────┼────────│
│  1  │ {{line_item_1_desc}}     │ {{q}}│ {{rate}}  │ {{amt}}│
│  2  │ {{line_item_2_desc}}     │ {{q}}│ {{rate}}  │ {{amt}}│
│  3  │ {{line_item_3_desc}}     │ {{q}}│ {{rate}}  │ {{amt}}│
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                         Subtotal:       {{subtotal}}        │
│                         Tax ({{rate}}): {{tax_amount}}      │
│                         Discount:       -{{discount}}       │
│                         ─────────────────────────────       │
│                         TOTAL DUE:      {{total_due}}       │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PAYMENT TERMS                                              │
│  Terms: {{payment_terms}}                                   │
│  Accepted Methods: {{payment_methods}}                      │
│                                                             │
│  Bank Details:                                              │
│    Bank Name:    {{bank_name}}                              │
│    Account:      {{account_number}}                         │
│    Routing:      {{routing_number}}                         │
│    SWIFT/BIC:    {{swift_code}}                             │
│                                                             │
│  Notes: {{notes}}                                           │
│  Late Payment: {{late_fee_policy}}                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Recurring Invoice Template

```
RECURRING INVOICE SETUP
═══════════════════════════════════════════

Client:              {{client_name}}
Service Description: {{service_description}}
Amount:              {{amount}} per {{period}}
Currency:            {{currency_code}}

Frequency:           [ ] Weekly  [ ] Bi-weekly  [ ] Monthly
                     [ ] Quarterly  [ ] Annually

Start Date:          {{start_date}}
End Date:            {{end_date}} or [ ] Ongoing

Auto-send:           [ ] Yes  [ ] No (draft for review)
Payment Method:      [ ] Auto-charge on file  [ ] Invoice & wait
Escalation Clause:   [ ] Annual increase of {{escalation_pct}}%

Special Terms:
{{recurring_notes}}
```

## Credit Memo Template

```
┌─────────────────────────────────────────────────────────────┐
│  CREDIT MEMO                                                │
│                                                             │
│  Credit Memo #:    {{credit_memo_number}}                   │
│  Date:             {{credit_date}}                          │
│  Original Invoice: {{original_invoice_number}}              │
│  Original Date:    {{original_invoice_date}}                │
│                                                             │
│  REASON FOR CREDIT:                                         │
│  {{credit_reason}}                                          │
│                                                             │
│  CREDITED ITEMS:                                            │
│  #  │ Description              │ Qty │ Rate     │ Credit   │
│  ───┼──────────────────────────┼─────┼──────────┼──────────│
│  1  │ {{item_desc}}            │ {{q}}│ {{rate}} │ -{{amt}}│
│                                                             │
│                         Tax Adjustment:  -{{tax_adj}}       │
│                         TOTAL CREDIT:    -{{total_credit}}  │
│                                                             │
│  BALANCE:                                                   │
│    Original Invoice Total:    {{original_total}}            │
│    This Credit:              -{{total_credit}}              │
│    Revised Amount Due:        {{revised_total}}             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Proforma Invoice Template

```
┌─────────────────────────────────────────────────────────────┐
│  PROFORMA INVOICE                                           │
│  (This is not a tax invoice)                                │
│                                                             │
│  Proforma #:       {{proforma_number}}                      │
│  Date:             {{proforma_date}}                        │
│  Valid Until:       {{expiry_date}}                         │
│  Quote Reference:  {{quote_ref}}                            │
│                                                             │
│  [Standard header, line items, and totals as above]         │
│                                                             │
│  NOTES:                                                     │
│  - This proforma is for informational purposes only         │
│  - Prices are valid until {{expiry_date}}                   │
│  - A formal invoice will be issued upon acceptance          │
│  - Terms and conditions per MSA dated {{msa_date}}          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```
