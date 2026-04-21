# SaaS Terms Addendum Template

**[COMPANY NAME]**
**SaaS Service Terms Addendum**

_This addendum supplements the Terms of Service and governs use of the [SERVICE NAME] SaaS platform._

---

## A. Service Level Agreement (SLA)

### Uptime Commitment

[COMPANY NAME] commits to [99.9]% monthly uptime for the Service, measured as:

```
Uptime % = ((Total Minutes in Month - Downtime Minutes) / Total Minutes in Month) x 100
```

### Excluded Downtime

The following are excluded from uptime calculations:

- Scheduled maintenance windows (announced [48] hours in advance)
- Force majeure events
- Issues caused by customer's infrastructure or third-party services
- Emergency security patches

### Service Credits

| Monthly Uptime | Service Credit |
|---|---|
| 99.0% - 99.9% | 10% of monthly fee |
| 95.0% - 99.0% | 25% of monthly fee |
| Below 95.0% | 50% of monthly fee |

**Maximum credit per month:** One month's fees.
**How to claim:** Submit a credit request to [EMAIL] within [30] days of the downtime event.

---

## B. Data Ownership and Portability

1. **Customer Data Ownership:** You retain all rights, title, and interest in your data. We claim no ownership over data you submit to the Service.

2. **Limited License:** You grant us a limited license to process your data solely to provide and improve the Service.

3. **Data Export:** You may export your data at any time in [CSV, JSON, and/or API] formats through the Service dashboard.

4. **Post-Termination:** Your data will be available for export for [30] days after termination. After that period, we will securely delete your data within [30] additional days.

5. **Data Deletion:** Upon written request, we will delete your data within [30] days and provide written confirmation.

---

## C. Subscription Terms

### Billing

- **Monthly plans:** Billed at the start of each monthly period.
- **Annual plans:** Billed at the start of each annual period with a [20]% discount.
- **All fees are non-refundable** except as required by applicable law.

### Plan Changes

- **Upgrades:** Effective immediately, prorated for the current billing period.
- **Downgrades:** Effective at the start of the next billing period.

### Auto-Renewal

Subscriptions auto-renew unless cancelled at least [30] days before the renewal date. You may cancel through [SETTINGS PAGE / EMAIL].

### Volume Licensing

For organizations with [50]+ seats, contact [SALES EMAIL] for volume pricing.

---

## D. API Terms

### Rate Limits

| Plan | Requests per Minute | Requests per Day | Concurrent Connections |
|---|---|---|---|
| Starter | 60 | 10,000 | 5 |
| Professional | 300 | 100,000 | 25 |
| Enterprise | Custom | Custom | Custom |

### API Versioning

- We will support each API version for a minimum of [12] months after deprecation notice.
- Deprecation notices will be posted in the API documentation and communicated via email.

### Restrictions

- You may not redistribute API access to third parties without written authorization.
- API access must not be used to build a competing product.
- We may throttle or suspend API access that degrades service for other customers.

---

## E. Support Terms

| Plan | Support Channels | Response Time (Business Hours) | Hours |
|---|---|---|---|
| Starter | Email | 24 hours | Mon-Fri 9am-5pm [TZ] |
| Professional | Email, Chat | 8 hours | Mon-Fri 9am-5pm [TZ] |
| Enterprise | Email, Chat, Phone | 4 hours (P1: 1 hour) | 24/7 for P1 |

---

## F. Security

We implement and maintain security measures including:

- Encryption in transit (TLS 1.2+) and at rest (AES-256)
- SOC 2 Type II certification [if applicable]
- Annual penetration testing by independent third party
- Role-based access controls
- Audit logging of administrative actions
- Incident response plan with [72]-hour notification

Our security practices are detailed in our [Security Whitepaper / Trust Center].
