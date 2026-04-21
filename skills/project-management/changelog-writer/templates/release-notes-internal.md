# Internal Release Notes - v[Version]

**Release Date:** [Date]
**Release Manager:** [Name]
**Deploy Window:** [Time and timezone]
**Rollback Deadline:** [Time - when rollback becomes complex]

---

## Summary

[1-2 sentence summary of what this release contains and why it matters.]

---

## Changes Requiring Ops Attention

| Change | Action Required | When | Rollback Plan |
|--------|----------------|------|---------------|
| [Database migration] | [Run before/after deploy] | [Pre/Post-deploy] | [Reverse migration script location] |
| [New environment variable] | [Add to config] | [Pre-deploy] | [Graceful degradation if missing] |
| [Cache schema change] | [Clear cache] | [Post-deploy] | [N/A] |
| [New service dependency] | [Verify connectivity] | [Pre-deploy] | [Feature flag to disable] |

---

## Feature Flags

| Flag Name | Default State | Description | Who Can Enable |
|-----------|--------------|-------------|----------------|
| [flag_name] | OFF | [What it controls] | [Role/team] |
| [flag_name] | ON (specific tier) | [What it controls] | [Role/team] |

---

## Deploy Checklist

### Pre-Deploy

- [ ] Backup database
- [ ] Run migrations in staging and verify
- [ ] Confirm environment variables are set in production
- [ ] Notify on-call team of deploy window
- [ ] Verify feature flags are in correct state

### Deploy

- [ ] Deploy to production
- [ ] Verify health check endpoint returns 200
- [ ] Run smoke tests

### Post-Deploy

- [ ] Monitor error rate for 30 minutes
- [ ] Verify [specific feature] works in production
- [ ] Check background job queue depth
- [ ] Confirm metrics are flowing to dashboard
- [ ] Post deploy confirmation to [channel]

---

## Monitoring

### Key Metrics to Watch

| Metric | Normal Range | Alert Threshold | Dashboard Link |
|--------|-------------|----------------|----------------|
| Error rate | < 0.1% | > 1% | [link] |
| Response time P95 | < 200ms | > 500ms | [link] |
| Background job queue | < 100 | > 500 | [link] |
| [Feature-specific metric] | [Range] | [Threshold] | [link] |

---

## Known Issues

- [Issue description] - [severity: non-blocking/blocking] - [fix planned in vX.Y.Z]

---

## Support FAQ

| Question | Answer |
|----------|--------|
| "How do I [common question]?" | [Answer or link to docs] |
| "Why did [visible change]?" | [Explanation] |
| "Can I still [deprecated feature]?" | [Yes until vX.Y.Z / No, use [alternative]] |

---

## Rollback Instructions

If critical issues are found post-deploy:

1. [Step 1: how to revert the deploy]
2. [Step 2: reverse migrations if needed]
3. [Step 3: clear caches if needed]
4. [Step 4: notify stakeholders]

**Previous stable version:** v[X.Y.Z]
**Rollback complexity:** [Simple/Medium/Complex]
**Data implications:** [None / Requires data fix / Irreversible changes]
