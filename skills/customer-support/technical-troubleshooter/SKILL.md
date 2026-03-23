# Technical Troubleshooter

---
name: technical-troubleshooter
description: Diagnose and resolve technical issues through systematic troubleshooting. Use when customers mention "error," "not working," "bug," "issue," "problem," "crash," "won't load," "can't access," "broken," or specific error codes.
metadata:
  version: 1.0.0
  category: customer-support
---

## Purpose

Guide users through systematic technical troubleshooting to identify root causes and resolve issues efficiently.

## Quick Reference

### Troubleshooting Methodology (ISOLATE)

| Step | Action | Purpose |
|------|--------|---------|
| **I**dentify | Define the exact issue | Clarify symptoms |
| **S**cope | Determine who/what is affected | Assess impact |
| **O**bserve | Gather error messages, logs | Collect evidence |
| **L**ocalize | Narrow down components | Find fault area |
| **A**nalyze | Test hypotheses | Identify root cause |
| **T**roubleshoot | Apply fixes systematically | Resolve issue |
| **E**valuate | Confirm resolution | Verify fix |

### Issue Priority Matrix

| Impact | Urgency | Priority | Response |
|--------|---------|----------|----------|
| System down | Immediate | P1 - Critical | 15 min |
| Major feature broken | Same day | P2 - High | 1 hour |
| Feature degraded | Next day | P3 - Medium | 4 hours |
| Minor issue | This week | P4 - Low | 24 hours |

## Workflow

### 1. Issue Identification

```
Initial Questions:
□ What were you trying to do?
□ What happened instead?
□ When did this start happening?
□ Any error messages? (screenshot helps)
□ What device/browser are you using?
□ Has it ever worked before?
□ Any recent changes on your end?
```

### 2. Information Gathering Template

```
Issue Report:
- Description: [User's description]
- Expected behavior: [What should happen]
- Actual behavior: [What is happening]
- Error message: [Exact text or screenshot]
- Frequency: [Always/Sometimes/Once]
- Device: [Desktop/Mobile/Tablet]
- OS: [Windows/Mac/iOS/Android + version]
- Browser: [Chrome/Firefox/Safari + version]
- Account: [Email/ID]
- Steps to reproduce:
  1. [Step 1]
  2. [Step 2]
  3. [Step 3]
```

### 3. Common Issue Decision Tree

```
User reports issue
    │
    ├─→ Login/Access Issues
    │       │
    │       ├─→ Forgot password → Reset flow
    │       ├─→ Account locked → Unlock + security check
    │       ├─→ SSO failing → Check IdP status
    │       └─→ 2FA issue → Backup codes or reset
    │
    ├─→ Performance Issues
    │       │
    │       ├─→ Slow loading → Cache, network, server
    │       ├─→ Timeouts → Server status, connectivity
    │       └─→ Freezing → Browser, memory, conflicts
    │
    ├─→ Feature Not Working
    │       │
    │       ├─→ Button doesn't respond → JS errors, browser
    │       ├─→ Data not saving → API errors, validation
    │       ├─→ Display issues → CSS, resolution, browser
    │       └─→ Integration failing → API keys, permissions
    │
    ├─→ Error Messages
    │       │
    │       ├─→ 400 errors → User input issue
    │       ├─→ 401/403 errors → Authentication/permissions
    │       ├─→ 404 errors → Resource not found
    │       ├─→ 500 errors → Server-side issue
    │       └─→ Specific error code → Lookup in KB
    │
    └─→ Data Issues
            │
            ├─→ Data missing → Sync, permissions, deletion
            ├─→ Data incorrect → Import, formula, bug
            └─→ Data corrupted → Recovery, restore
```

## Troubleshooting Scripts

### Standard First-Response Checks

```
Basic Troubleshooting Steps:
1. Clear browser cache and cookies
2. Try incognito/private mode
3. Try a different browser
4. Disable browser extensions
5. Check internet connection
6. Try a different device
7. Check system status page
```

### Browser-Specific Issues

| Browser | Common Fixes |
|---------|--------------|
| Chrome | Clear cache, disable extensions, update |
| Firefox | Refresh Firefox, safe mode, clear storage |
| Safari | Clear history, disable content blockers |
| Edge | Reset settings, clear browsing data |

### Device-Specific Issues

| Platform | Common Fixes |
|----------|--------------|
| Windows | Restart, update drivers, check firewall |
| Mac | Restart, check permissions, update OS |
| iOS | Force close app, reinstall, check iOS version |
| Android | Clear app cache, reinstall, check permissions |

## Response Templates

### Initial Response
```
Hi [Name],

I'm sorry you're experiencing this issue. Let me help you troubleshoot.

To get started, could you provide:
1. What exactly happens when you try to [action]?
2. Do you see any error messages?
3. What browser and device are you using?

In the meantime, try these quick fixes:
1. Clear your browser cache (Ctrl+Shift+Delete)
2. Try opening in an incognito/private window
3. Try a different browser

Let me know what you find!
```

### Requesting More Information
```
Hi [Name],

Thanks for those details. I have a few more questions to pinpoint the issue:

1. [Specific question about their environment]
2. [Question about steps to reproduce]
3. [Question about when it started]

Also, could you share:
- A screenshot of the error (if there is one)
- Your browser version (Help → About)

This will help me identify exactly what's happening.
```

### Providing Solution
```
Hi [Name],

I found the issue! Here's how to fix it:

**The Problem:**
[Brief explanation of what's happening]

**The Fix:**
1. [Step 1 with specific instructions]
2. [Step 2 with specific instructions]
3. [Step 3 with specific instructions]

[Screenshot or GIF if helpful]

**Why This Happened:**
[Brief explanation - optional]

Try these steps and let me know if it resolves the issue.
```

### Escalating to Engineering
```
Hi [Name],

I've investigated this thoroughly and need to involve our engineering team.

What I've confirmed:
- [Finding 1]
- [Finding 2]
- [Finding 3]

I'm escalating this as a [priority] issue. Here's what happens next:
- Engineering will investigate within [timeframe]
- I'll update you every [frequency]
- Reference number: [TICKET_ID]

In the meantime, [workaround if available].

I apologize for the inconvenience and will keep you updated.
```

## Error Code Reference

### HTTP Status Codes

| Code | Meaning | User Message | Action |
|------|---------|--------------|--------|
| 400 | Bad Request | "Check your input" | Validate user data |
| 401 | Unauthorized | "Please log in again" | Re-authenticate |
| 403 | Forbidden | "Access denied" | Check permissions |
| 404 | Not Found | "Page not found" | Check URL |
| 408 | Timeout | "Request timed out" | Retry |
| 429 | Rate Limited | "Too many requests" | Wait and retry |
| 500 | Server Error | "Something went wrong" | Escalate |
| 502 | Bad Gateway | "Service unavailable" | Check status |
| 503 | Service Unavailable | "Temporarily down" | Wait or escalate |

### Common Application Errors

| Error Pattern | Likely Cause | First Check |
|---------------|--------------|-------------|
| ERR_CONNECTION_REFUSED | Server down | Status page |
| ERR_SSL_PROTOCOL | Certificate issue | Date/time settings |
| ERR_CACHE_MISS | Cache corruption | Clear cache |
| ERR_NAME_NOT_RESOLVED | DNS issue | Flush DNS |
| ERR_NETWORK_CHANGED | Network switch | Reconnect |

## Escalation Criteria

### Escalate Immediately When:
- System-wide outage
- Security breach suspected
- Data loss reported
- Multiple users affected
- Issue persists after standard troubleshooting
- Error involves sensitive data
- Customer is enterprise/VIP

### Escalation Template
```
ESCALATION: [Brief Issue Summary]

Customer: [Name/Account]
Priority: [P1/P2/P3/P4]
Affected: [Scope - one user/team/all users]

Issue Description:
[Clear description]

Troubleshooting Completed:
- [Step 1] - Result: [outcome]
- [Step 2] - Result: [outcome]
- [Step 3] - Result: [outcome]

Error Details:
- Error message: [exact text]
- Error code: [if any]
- Logs: [attached/linked]

Environment:
- Browser: [version]
- OS: [version]
- Account type: [plan]

Impact:
- [How this affects the user's work]

Recommended Next Steps:
- [Suggestion for engineering]
```

## Scripts & Tools

| Script | Purpose |
|--------|---------|
| `scripts/troubleshoot_guide.py` | Interactive troubleshooting wizard |
| `scripts/error_lookup.py` | Look up error codes and solutions |

## Best Practices

### Do's
- Ask clarifying questions before suggesting fixes
- Document all troubleshooting steps
- Provide exact steps, not vague instructions
- Use screenshots/GIFs for complex steps
- Follow up to confirm resolution
- Update knowledge base with new issues

### Don'ts
- Assume user's technical level
- Skip basic troubleshooting steps
- Make users feel stupid
- Leave issues unresolved
- Forget to document workarounds
- Ignore patterns of similar issues

## Reference

→ See `templates/troubleshooting_templates.md` for response templates
→ See `reference.md` for error code reference and common fixes
