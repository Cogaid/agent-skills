# Auto-Filter Rules Template

## Usage

Define your email filter rules below. Use `auto_filter_generator.py` to analyze your inbox and suggest additional rules based on patterns.

---

## Rule Definitions

### Rule 1: Executive Emails

```
Condition: sender IN [ceo@company.com, cto@company.com, vp-*@company.com]
Action:
  - Apply label: @Action-Required
  - Set priority: High
  - Star: yellow
  - Keep in inbox
```

### Rule 2: Client Emails

```
Condition: sender domain IN [acme.com, globex.com, initech.com]
Action:
  - Apply label: Clients/{matched_client}
  - Apply label: @Action-Required
  - Keep in inbox
```

### Rule 3: Calendar Notifications

```
Condition: from contains "calendar-notification" OR subject contains "invitation"
Action:
  - Apply label: Calendar
  - Skip inbox (process via calendar app)
  - Mark as read
```

### Rule 4: Automated Reports

```
Condition: subject matches "Daily Report*" OR "Weekly Summary*" OR "Monthly Dashboard*"
Action:
  - Apply label: @Read-Review
  - Skip inbox
```

### Rule 5: Newsletters and Marketing

```
Condition: header list-unsubscribe is present AND sender NOT IN whitelist
Action:
  - Apply label: Newsletters/{auto-categorize}
  - Skip inbox
```

### Rule 6: Receipts and Invoices

```
Condition: subject contains "receipt" OR "invoice" OR "order confirmation" OR "payment"
Action:
  - Apply label: Personal/Receipts
  - Skip inbox
  - Mark as read
```

### Rule 7: Hot Thread Detection

```
Condition: thread reply count > 5 AND you are CC (not TO)
Action:
  - Apply label: @Read-Review
  - Add note: "Hot thread - may not need your action"
```

### Rule 8: Out-of-Office Auto-Replies

```
Condition: subject contains "Out of Office" OR "OOO" OR "Auto-Reply" OR "Automatic reply"
Action:
  - Archive immediately
  - Mark as read
```

### Rule 9: CI/CD Notifications

```
Condition: from contains "github.com" OR "gitlab.com" OR "jenkins" OR "circleci"
Action:
  - Apply label: Internal/IT-Support
  - Skip inbox (unless contains "failed" or "error")
```

### Rule 10: Meeting Follow-ups

```
Condition: subject starts with "Re:" AND body contains "action items" OR "meeting notes"
Action:
  - Apply label: @Action-Required
  - Keep in inbox
```

## Whitelist (never auto-filter)

Add senders here that should always reach your inbox regardless of other rules:

```
- boss@company.com
- direct-report-1@company.com
- key-client-contact@acme.com
- spouse@personal.com
```

## Maintenance Notes

- Review filter hit counts weekly
- Disable filters with 0 hits for 30 days
- Update client/project domains when relationships change
- Add new newsletter senders to Rule 5 as they appear
