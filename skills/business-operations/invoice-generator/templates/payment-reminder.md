# Payment Reminder Templates

## Friendly Reminder (7 Days After Invoice)

```
Subject: Reminder: Invoice {{invoice_number}} - Due {{due_date}}

Hi {{client_contact_name}},

I hope this message finds you well. This is a friendly reminder that
invoice {{invoice_number}} for {{total_due}} was sent on {{issue_date}}
and is due on {{due_date}}.

Invoice Summary:
  Invoice #:    {{invoice_number}}
  Amount Due:   {{total_due}}
  Due Date:     {{due_date}}
  PO Number:    {{po_number}}

If payment has already been sent, please disregard this message.
Otherwise, please let me know if you have any questions or need
the invoice resent.

Payment can be made via:
{{payment_methods}}

Thank you for your business.

Best regards,
{{sender_name}}
{{sender_title}}
{{company_name}}
```

## Overdue Notice (30 Days Past Due)

```
Subject: Overdue: Invoice {{invoice_number}} - {{days_overdue}} Days Past Due

Dear {{client_contact_name}},

Our records indicate that invoice {{invoice_number}} for {{total_due}}
is now {{days_overdue}} days past due. The original due date was
{{due_date}}.

Invoice Details:
  Invoice #:       {{invoice_number}}
  Original Amount: {{total_due}}
  Due Date:        {{due_date}}
  Days Overdue:    {{days_overdue}}

Please arrange payment at your earliest convenience. If there is an
issue with this invoice or if you need to discuss payment arrangements,
please contact us immediately.

Payment can be made via:
{{payment_methods}}

Thank you for your prompt attention to this matter.

Regards,
{{sender_name}}
{{sender_title}}
{{company_name}}
```

## Final Notice (60 Days Past Due)

```
Subject: FINAL NOTICE: Invoice {{invoice_number}} - Immediate Payment Required

Dear {{client_contact_name}},

This is a final notice regarding invoice {{invoice_number}} for
{{total_due}}, which is now {{days_overdue}} days past due.

Outstanding Balance:
  Invoice #:        {{invoice_number}}
  Original Amount:  {{original_amount}}
  Late Fees:        {{late_fee_amount}}
  Total Due:        {{total_with_fees}}
  Due Date:         {{due_date}}
  Days Overdue:     {{days_overdue}}

Per our agreement, a late fee of {{late_fee_rate}} has been applied
to the outstanding balance.

If payment is not received within 15 days of this notice, we will
be forced to escalate this matter, which may include suspension of
services and referral to a collections agency.

To resolve this matter, please contact {{collections_contact}} at
{{collections_email}} or {{collections_phone}} immediately.

Regards,
{{sender_name}}
{{sender_title}}
{{company_name}}
```

## Payment Confirmation

```
Subject: Payment Received - Invoice {{invoice_number}}

Hi {{client_contact_name}},

Thank you! We have received your payment of {{payment_amount}} for
invoice {{invoice_number}}.

Payment Details:
  Invoice #:       {{invoice_number}}
  Amount Received: {{payment_amount}}
  Payment Date:    {{payment_date}}
  Payment Method:  {{payment_method}}
  Reference #:     {{payment_reference}}

  Remaining Balance: {{remaining_balance}}

A receipt is attached for your records. Thank you for your continued
business.

Best regards,
{{sender_name}}
{{company_name}}
```
