# Email Folder/Label Structure Template

## Usage

Use this template to set up your email label hierarchy. Adapt the project and client names to your context. Apply using `organize_inbox.py --setup-labels`.

---

## Recommended Label Structure

```
INBOX (temporary holding -- target: 0 items)

ACTION LABELS:
+-- @Action-Required       Tasks you need to complete
+-- @Waiting-For           Delegated or awaiting reply
+-- @Read-Review           Articles, FYIs, digests to read
+-- @Scheduled             Deferred to a specific date

CATEGORY LABELS:

Projects/
+-- Project-Alpha          Active project #1
+-- Project-Beta           Active project #2
+-- Project-Gamma          Active project #3
+-- Project-Archive        Completed projects (searchable)

Clients/
+-- Client-Acme            Key client communications
+-- Client-Globex          Key client communications
+-- Client-Initech         Key client communications

Internal/
+-- HR-Admin               Benefits, policies, onboarding
+-- Finance                Budgets, expenses, invoices
+-- IT-Support             Tickets, system notices
+-- Leadership             Exec communications, strategy

Newsletters/
+-- Industry-News          Sector news and analysis
+-- Product-Updates        Tools and services you use
+-- Learning               Courses, tutorials, reading lists

Personal/
+-- Travel                 Bookings, confirmations, itineraries
+-- Receipts               Purchase confirmations, invoices
+-- Subscriptions          Personal service emails

ARCHIVE (searchable, organized by year/quarter)
TRASH (auto-empty after 30 days)
```

## Setup Checklist

- [ ] Create all action labels (@Action-Required, @Waiting-For, @Read-Review, @Scheduled)
- [ ] Create project labels for current active projects
- [ ] Create client labels for active client relationships
- [ ] Create internal category labels
- [ ] Set up nested label structure (Projects/, Clients/, etc.)
- [ ] Configure label colors for quick visual scanning
- [ ] Archive or remove labels for completed projects quarterly

## Color Coding Recommendation

| Label Type | Suggested Color | Rationale |
|------------|----------------|-----------|
| @Action-Required | Red | Demands attention |
| @Waiting-For | Yellow/Orange | Monitoring needed |
| @Read-Review | Blue | Low urgency, informational |
| @Scheduled | Purple | Deferred, time-bound |
| Projects/* | Green shades | Active work |
| Clients/* | Teal shades | External relationships |
| Internal/* | Gray shades | Administrative |
| Newsletters/* | Light blue | Optional reading |
