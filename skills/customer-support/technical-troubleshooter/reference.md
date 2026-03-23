# Technical Troubleshooter Reference

## Diagnostic Framework

### The 5 Whys Method

Start with the symptom, ask "why" repeatedly to find root cause:

```
Problem: User can't log in
Why? → Password is being rejected
Why? → Password was changed
Why? → User didn't change it
Why? → Account was compromised
Why? → Password was too weak / phished

Root cause: Security issue, not technical
```

### Fault Isolation

```
Known Good → Test Point → Failure Point
    ↓           ↓            ↓
  Works      Narrow      Identified
              down
```

**Steps:**
1. Find something that works (baseline)
2. Find something that doesn't work
3. Test points between them
4. Isolate the failure point

---

## Common Issue Categories

### Authentication Issues

| Symptom | Possible Causes | Diagnostic Steps |
|---------|----------------|------------------|
| Can't log in | Wrong password, account locked, SSO issue | Check auth logs, test reset |
| Session expires quickly | Cookie settings, token issue | Check cookie policy, token TTL |
| 2FA not working | Time drift, wrong device | Check device time, backup codes |
| SSO redirect loop | IdP config, SAML issue | Check IdP logs, SAML response |

**Auth Troubleshooting Flow:**
```
Login fails
    │
    ├─→ Error message?
    │       ├─→ "Invalid credentials" → Password issue
    │       ├─→ "Account locked" → Too many attempts
    │       ├─→ "SSO error" → IdP issue
    │       └─→ No message → Network/server issue
    │
    ├─→ Works in incognito?
    │       ├─→ Yes → Browser cache/cookies
    │       └─→ No → Server-side issue
    │
    └─→ Works on another device?
            ├─→ Yes → Device-specific issue
            └─→ No → Account issue
```

### Performance Issues

| Symptom | Possible Causes | Diagnostic Steps |
|---------|----------------|------------------|
| Slow page load | Network, server load, large payload | Network tab, server metrics |
| Timeouts | Server overload, network issues | Check status page, ping test |
| Memory issues | Memory leaks, large data | Task manager, browser memory |
| Freezing | JS errors, infinite loops | Console errors, CPU usage |

**Performance Checklist:**
```
□ Check network tab for slow requests (>1s)
□ Check console for JavaScript errors
□ Check server status page
□ Test with different network
□ Test in incognito mode
□ Check browser memory usage
□ Test at different times of day
```

### Data Issues

| Symptom | Possible Causes | Diagnostic Steps |
|---------|----------------|------------------|
| Data missing | Sync issue, permissions, deletion | Check audit log, sync status |
| Data incorrect | Import error, formula bug | Check source data, recalculate |
| Data duplicated | Sync conflict, import issue | Check timestamps, deduplicate |
| Data not saving | API error, validation failure | Check network tab, console |

---

## Browser Troubleshooting

### Cache & Storage

**Clear Cache (All Browsers):**
- Chrome: `Ctrl+Shift+Delete` → Clear browsing data
- Firefox: `Ctrl+Shift+Delete` → Clear history
- Safari: Safari → Clear History
- Edge: `Ctrl+Shift+Delete` → Clear browsing data

**Storage Types:**
| Type | Purpose | How to Clear |
|------|---------|--------------|
| Cache | Static assets | Browser settings |
| Cookies | Session data | Browser settings |
| LocalStorage | App data | DevTools → Application |
| SessionStorage | Temp data | Close tab |
| IndexedDB | Large data | DevTools → Application |

### Browser Extensions

**Common Problematic Extensions:**
- Ad blockers (block API calls)
- Privacy extensions (block cookies)
- VPNs (route issues)
- Translation extensions (modify DOM)
- Password managers (form conflicts)

**Test without extensions:**
- Chrome: `Ctrl+Shift+N` (Incognito)
- Firefox: `Ctrl+Shift+P` (Private) or Safe Mode
- Safari: Disable all extensions
- Edge: InPrivate mode

### Developer Tools

**Console Tab:**
```javascript
// Look for:
// - Red error messages
// - Yellow warnings
// - Failed network requests
// - Stack traces
```

**Network Tab:**
```
// Check for:
// - Red failed requests
// - Slow requests (>1s)
// - 4xx/5xx status codes
// - Request size (large payloads)
```

**Application Tab:**
```
// Inspect:
// - LocalStorage
// - SessionStorage
// - Cookies
// - Service Workers
// - Cache Storage
```

---

## Network Troubleshooting

### Connectivity Tests

```bash
# Ping test
ping google.com

# DNS lookup
nslookup yourdomain.com

# Trace route
tracert yourdomain.com  # Windows
traceroute yourdomain.com  # Mac/Linux

# Check port
telnet yourdomain.com 443
```

### Common Network Issues

| Issue | Symptom | Fix |
|-------|---------|-----|
| DNS issue | ERR_NAME_NOT_RESOLVED | Flush DNS, try 8.8.8.8 |
| Firewall block | Connection refused | Check firewall rules |
| Proxy issue | Connection timeout | Check proxy settings |
| VPN conflict | Intermittent failures | Disconnect VPN |
| ISP issue | Slow/no connection | Restart router, contact ISP |

### Flush DNS Commands

**Windows:**
```cmd
ipconfig /flushdns
```

**Mac:**
```bash
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder
```

**Linux:**
```bash
sudo systemctl restart systemd-resolved
```

---

## API & Integration Issues

### Common API Errors

| Status | Meaning | User Action |
|--------|---------|-------------|
| 400 | Bad Request | Check input format |
| 401 | Unauthorized | Check API key/token |
| 403 | Forbidden | Check permissions |
| 404 | Not Found | Check endpoint URL |
| 405 | Method Not Allowed | Check HTTP method |
| 415 | Unsupported Media Type | Check Content-Type |
| 422 | Validation Error | Check request body |
| 429 | Rate Limited | Slow down requests |
| 500 | Server Error | Contact support |
| 502 | Bad Gateway | Wait and retry |
| 503 | Service Unavailable | Check status page |
| 504 | Gateway Timeout | Wait and retry |

### Integration Debugging

**OAuth Issues:**
| Error | Cause | Fix |
|-------|-------|-----|
| Invalid client | Wrong client ID | Check credentials |
| Invalid grant | Expired/used code | Request new code |
| Invalid scope | Unknown scope | Check available scopes |
| Redirect mismatch | URL not registered | Add redirect URI |

**Webhook Issues:**
| Problem | Check |
|---------|-------|
| Not receiving | URL accessible, SSL valid |
| Duplicate events | Idempotency handling |
| Missing data | Payload format |
| Timeout | Response time <30s |

---

## Mobile App Troubleshooting

### iOS Issues

| Issue | Solution |
|-------|----------|
| App crashes | Delete + reinstall |
| Won't open | Force close, restart phone |
| Slow | Clear app cache in settings |
| Sync issues | Check iCloud settings |
| Notifications broken | Check Settings → Notifications |

**iOS Reset Steps:**
1. Force close app (swipe up from app switcher)
2. Settings → General → iPhone Storage → [App] → Offload App
3. Restart iPhone (hold power + volume)
4. Reinstall from App Store

### Android Issues

| Issue | Solution |
|-------|----------|
| App crashes | Clear cache + data |
| Won't install | Check storage, clear Play Store cache |
| Battery drain | Check background restrictions |
| Permissions | Settings → Apps → [App] → Permissions |

**Android Reset Steps:**
1. Force stop: Settings → Apps → [App] → Force Stop
2. Clear cache: Settings → Apps → [App] → Storage → Clear Cache
3. Clear data: Settings → Apps → [App] → Storage → Clear Data
4. Reinstall from Play Store

---

## Error Message Reference

### Generic Error Messages

| Message | Likely Cause | Check |
|---------|-------------|-------|
| "Something went wrong" | Unhandled exception | Logs, console |
| "Request failed" | Network/API issue | Network tab |
| "Invalid request" | Malformed data | Request payload |
| "Access denied" | Auth/permissions | Token, roles |
| "Not found" | Wrong ID/URL | Resource exists |
| "Timeout" | Slow response | Server status |
| "Rate limited" | Too many requests | Slow down |

### Error Codes Pattern

| Pattern | Category | Example |
|---------|----------|---------|
| AUTH_* | Authentication | AUTH_INVALID_TOKEN |
| PERM_* | Permissions | PERM_ACCESS_DENIED |
| VAL_* | Validation | VAL_REQUIRED_FIELD |
| NET_* | Network | NET_CONNECTION_FAILED |
| SRV_* | Server | SRV_INTERNAL_ERROR |
| USER_* | User error | USER_NOT_FOUND |

---

## Escalation Guidelines

### Severity Levels

| Level | Criteria | Response Time | Examples |
|-------|----------|---------------|----------|
| P1 | System down, all users | 15 min | Site down, DB crash |
| P2 | Major feature broken | 1 hour | Payment failing |
| P3 | Feature degraded | 4 hours | Slow performance |
| P4 | Minor issue | 24 hours | UI bug |

### Information for Escalation

**Required:**
- Customer identifier (email/account ID)
- Exact error message or behavior
- Steps to reproduce
- Timestamp when issue occurred
- Browser/device details
- Screenshots/screen recordings

**Helpful:**
- Network HAR file
- Console logs
- User's previous tickets
- Account type/plan
- Number of affected users

### Escalation Path

```
Tier 1 Support
    ↓ (15 min no resolution)
Tier 2 Support
    ↓ (30 min no resolution)
Engineering On-Call
    ↓ (Critical issues)
Engineering Team Lead
    ↓ (P1 issues)
Incident Commander
```

---

## Tools & Resources

### Diagnostic Tools

| Tool | Purpose | URL |
|------|---------|-----|
| Down Detector | Check service status | downdetector.com |
| Is It Down | Quick status check | isitdownrightnow.com |
| SSL Checker | Verify SSL certificate | sslshopper.com/ssl-checker |
| DNS Checker | Check DNS propagation | dnschecker.org |
| What Is My IP | Check user's IP | whatismyip.com |

### Browser Extension Testing

| Browser | Safe Mode | Disable Extensions |
|---------|-----------|-------------------|
| Chrome | Incognito | chrome://extensions |
| Firefox | Safe Mode | about:addons |
| Safari | N/A | Preferences → Extensions |
| Edge | InPrivate | edge://extensions |

### Log Analysis

**What to look for:**
- Timestamps (when did errors start?)
- Error patterns (recurring issues?)
- User identifiers (specific accounts?)
- Request IDs (trace the request)
- Stack traces (where did it fail?)
