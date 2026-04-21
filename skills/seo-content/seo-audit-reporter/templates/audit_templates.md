# SEO Audit Report Templates

Complete collection of templates for SEO audit reporting.

---

## Template 1: Executive Summary

```markdown
# SEO Audit Report: [Domain]

**Audit Date:** [Date]
**Prepared By:** [Name/Team]
**Audit Scope:** [Full site / Section / Technical only]

---

## Executive Summary

**Overall SEO Health Score: [XX]/100 -- [Rating]**

| Dimension | Score | Status | Priority Actions |
|-----------|-------|--------|-----------------|
| Technical SEO | [XX]/100 | [Good/Fair/Poor] | [1-line summary] |
| On-Page SEO | [XX]/100 | [Good/Fair/Poor] | [1-line summary] |
| Content Quality | [XX]/100 | [Good/Fair/Poor] | [1-line summary] |
| Off-Page SEO | [XX]/100 | [Good/Fair/Poor] | [1-line summary] |

### Key Findings

1. **[Critical finding]** -- [Impact and recommendation]
2. **[Important finding]** -- [Impact and recommendation]
3. **[Notable finding]** -- [Impact and recommendation]

### Estimated Impact

| Action | Est. Traffic Impact | Effort | Timeline |
|--------|-------------------|--------|----------|
| [Action 1] | +[X]% organic traffic | [Low/Med/High] | [Weeks] |
| [Action 2] | +[X]% organic traffic | [Low/Med/High] | [Weeks] |
| [Action 3] | +[X]% organic traffic | [Low/Med/High] | [Weeks] |

### Current Performance Snapshot

| Metric | Current | 3 Months Ago | Change |
|--------|---------|-------------|--------|
| Organic Sessions/Month | [X] | [X] | [+/-X%] |
| Indexed Pages | [X] | [X] | [+/-X] |
| Domain Rating | [X] | [X] | [+/-X] |
| Top 10 Rankings | [X] | [X] | [+/-X] |
| Core Web Vitals Pass | [X]% | [X]% | [+/-X pp] |
```

---

## Template 2: Technical SEO Audit

```markdown
# Technical SEO Audit: [Domain]

**Crawl Date:** [Date]
**Pages Crawled:** [Count]
**Tool Used:** [Screaming Frog / Sitebulb / etc.]

---

## Crawl Summary

| Status | Count | % of Total | Action |
|--------|-------|------------|--------|
| 200 OK | [X] | [X]% | None |
| 301 Redirect | [X] | [X]% | Review chains |
| 302 Temporary | [X] | [X]% | Convert to 301 or fix |
| 404 Not Found | [X] | [X]% | Fix or redirect |
| 5xx Server Error | [X] | [X]% | Fix immediately |
| Redirect Chains (3+) | [X] | [X]% | Simplify |
| Orphan Pages | [X] | [X]% | Add internal links |

## Indexing Status

| Metric | Count | Status |
|--------|-------|--------|
| Pages submitted in sitemap | [X] | -- |
| Pages indexed (GSC) | [X] | [Good/Issue] |
| Pages not indexed | [X] | [Review] |
| Noindex pages | [X] | [Intentional?] |
| Duplicate content pages | [X] | [Fix] |

**Index coverage issues (from GSC):**
| Issue | Pages Affected | Priority |
|-------|---------------|----------|
| [Issue type] | [X] | [High/Med/Low] |
| [Issue type] | [X] | [High/Med/Low] |

## Core Web Vitals

| Page | LCP | INP | CLS | Score | Status |
|------|-----|-----|-----|-------|--------|
| Homepage | [X]s | [X]ms | [X] | [X] | [Pass/Fail] |
| [Top page 2] | [X]s | [X]ms | [X] | [X] | [Pass/Fail] |
| [Top page 3] | [X]s | [X]ms | [X] | [X] | [Pass/Fail] |
| [Top page 4] | [X]s | [X]ms | [X] | [X] | [Pass/Fail] |
| [Top page 5] | [X]s | [X]ms | [X] | [X] | [Pass/Fail] |

**CWV Pass Rate:** [X]% of pages pass all three metrics

**Top Speed Issues:**
| Issue | Pages Affected | Impact | Fix |
|-------|---------------|--------|-----|
| [Issue] | [X] | [High/Med] | [Recommendation] |
| [Issue] | [X] | [High/Med] | [Recommendation] |
| [Issue] | [X] | [High/Med] | [Recommendation] |

## Mobile Friendliness

| Check | Status | Notes |
|-------|--------|-------|
| Mobile-friendly test | [Pass/Fail] | [Details] |
| Viewport configured | [Yes/No] | [Details] |
| Font size adequate | [Yes/No] | [Details] |
| Tap targets sized | [Yes/No] | [Details] |
| Content fits viewport | [Yes/No] | [Details] |

## Structured Data

| Schema Type | Pages | Valid | Errors |
|------------|-------|-------|--------|
| [Product/Article/etc] | [X] | [X] | [X] |
| [Organization] | [X] | [X] | [X] |
| [BreadcrumbList] | [X] | [X] | [X] |
| [FAQ] | [X] | [X] | [X] |

## Security

| Check | Status |
|-------|--------|
| HTTPS across all pages | [Pass/Fail] |
| Mixed content issues | [X] pages |
| HSTS configured | [Yes/No] |
| Certificate valid | [Yes/Expiry date] |
```

---

## Template 3: On-Page Audit

```markdown
# On-Page SEO Audit: [Domain]

---

## Title Tags

| Issue | Count | Example URLs | Recommendation |
|-------|-------|-------------|----------------|
| Missing title | [X] | [url] | Add unique titles |
| Duplicate titles | [X] | [url], [url] | Make unique |
| Too long (>60 chars) | [X] | [url] | Shorten |
| Too short (<30 chars) | [X] | [url] | Expand |
| Missing keyword | [X] | [url] | Add target keyword |

## Meta Descriptions

| Issue | Count | Example URLs | Recommendation |
|-------|-------|-------------|----------------|
| Missing | [X] | [url] | Write descriptions |
| Duplicate | [X] | [url], [url] | Make unique |
| Too long (>160) | [X] | [url] | Shorten |
| Too short (<120) | [X] | [url] | Expand |

## Heading Tags

| Issue | Count | Example URLs |
|-------|-------|-------------|
| Missing H1 | [X] | [url] |
| Multiple H1s | [X] | [url] |
| H1 duplicates title exactly | [X] | [url] |
| Skipped heading levels | [X] | [url] |

## Images

| Issue | Count | Impact | Fix |
|-------|-------|--------|-----|
| Missing alt text | [X] | Medium | Add descriptive alt text |
| Oversized images (>200KB) | [X] | High | Compress and serve WebP |
| Missing dimensions | [X] | Medium (CLS) | Add width/height |
| Non-descriptive filenames | [X] | Low | Rename to keyword-relevant |

## Internal Linking

| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| Avg. internal links per page | [X] | 5-10 | [Good/Low/High] |
| Pages with 0 internal links | [X] | 0 | [Fix] |
| Pages with 1 internal link | [X] | <5% | [Review] |
| Max click depth | [X] | 3-4 | [Good/Deep] |
| Broken internal links | [X] | 0 | [Fix] |
```

---

## Template 4: Content Audit

```markdown
# Content Quality Audit: [Domain]

---

## Content Inventory

| Category | Pages | Avg Traffic | Avg Word Count | Action |
|----------|-------|-------------|---------------|--------|
| High performers | [X] | [X]/mo | [X] | Protect & expand |
| Average performers | [X] | [X]/mo | [X] | Optimize |
| Underperformers | [X] | [X]/mo | [X] | Update or consolidate |
| No traffic (6+ months) | [X] | 0 | [X] | Prune or redirect |

## Declining Content (traffic down >20% YoY)

| Page | Current Traffic | Previous Traffic | Change | Action |
|------|----------------|-----------------|--------|--------|
| [url] | [X] | [X] | -[X]% | [Update/rewrite/consolidate] |
| [url] | [X] | [X] | -[X]% | [Update/rewrite/consolidate] |

## Keyword Cannibalization

| Keyword | Pages Competing | Best Page | Action |
|---------|----------------|-----------|--------|
| [keyword] | [url1], [url2] | [url1] | Consolidate/redirect |
| [keyword] | [url1], [url2] | [url2] | Deoptimize url1 |

## Thin Content (< 300 words)

| Page | Word Count | Traffic | Recommendation |
|------|-----------|---------|----------------|
| [url] | [X] | [X] | [Expand/merge/noindex] |
| [url] | [X] | [X] | [Expand/merge/noindex] |

## Content Freshness

| Age Bucket | Pages | Avg Traffic | Recommendation |
|-----------|-------|-------------|----------------|
| Updated < 6 months | [X] | [X] | Maintain |
| 6-12 months | [X] | [X] | Review for updates |
| 12-24 months | [X] | [X] | Refresh priority |
| > 24 months | [X] | [X] | Audit and decide |

## E-E-A-T Assessment

| Signal | Present | Notes |
|--------|---------|-------|
| Author bylines | [Yes/No] | [Details] |
| Author bio pages | [Yes/No] | [Details] |
| Author credentials | [Yes/No] | [Details] |
| Editorial process | [Yes/No] | [Details] |
| Sources cited | [Yes/No] | [Details] |
| Last updated dates | [Yes/No] | [Details] |
| Contact information | [Yes/No] | [Details] |
| Privacy policy | [Yes/No] | [Details] |
```

---

## Template 5: Prioritized Action Plan

```markdown
# SEO Action Plan: [Domain]

**Based on audit dated:** [Date]
**Overall Score:** [XX]/100

---

## Priority 1: Critical (Fix Within 2 Weeks)

| # | Issue | Pages | Impact | Effort | Owner | Due |
|---|-------|-------|--------|--------|-------|-----|
| 1 | [Issue] | [X] | High | [Est. hours] | [Team] | [Date] |
| 2 | [Issue] | [X] | High | [Est. hours] | [Team] | [Date] |

## Priority 2: High (Fix Within 1 Month)

| # | Issue | Pages | Impact | Effort | Owner | Due |
|---|-------|-------|--------|--------|-------|-----|
| 3 | [Issue] | [X] | Med-High | [Est. hours] | [Team] | [Date] |
| 4 | [Issue] | [X] | Med-High | [Est. hours] | [Team] | [Date] |

## Priority 3: Medium (Fix Within 3 Months)

| # | Issue | Pages | Impact | Effort | Owner | Due |
|---|-------|-------|--------|--------|-------|-----|
| 5 | [Issue] | [X] | Medium | [Est. hours] | [Team] | [Date] |

## Priority 4: Low (Ongoing Optimization)

| # | Issue | Pages | Impact | Effort | Owner | Due |
|---|-------|-------|--------|--------|-------|-----|
| 6 | [Issue] | [X] | Low | [Est. hours] | [Team] | [Date] |

---

## Progress Tracking

| Week | Actions Completed | Score Change | Notes |
|------|------------------|-------------|-------|
| Week 1 | | | |
| Week 2 | | | |
| Week 4 | | | |
| Week 8 | | | |
| Week 12 | | | |
```

---

## Template 6: Monthly SEO Tracking

```markdown
# Monthly SEO Report: [Domain]

**Period:** [Month Year]
**Prepared:** [Date]

---

## KPI Dashboard

| Metric | This Month | Last Month | MoM Change | YoY Change |
|--------|-----------|------------|-----------|-----------|
| Organic Sessions | [X] | [X] | [+/-X%] | [+/-X%] |
| Organic Clicks (GSC) | [X] | [X] | [+/-X%] | [+/-X%] |
| Impressions (GSC) | [X] | [X] | [+/-X%] | [+/-X%] |
| Average Position | [X] | [X] | [+/-X] | [+/-X] |
| CTR | [X]% | [X]% | [+/-X pp] | [+/-X pp] |
| Indexed Pages | [X] | [X] | [+/-X] | [+/-X] |
| Domain Rating | [X] | [X] | [+/-X] | [+/-X] |
| Referring Domains | [X] | [X] | [+/-X] | [+/-X] |
| CWV Pass Rate | [X]% | [X]% | [+/-X pp] | [+/-X pp] |
| Top 3 Rankings | [X] | [X] | [+/-X] | [+/-X] |
| Top 10 Rankings | [X] | [X] | [+/-X] | [+/-X] |
| Organic Conversions | [X] | [X] | [+/-X%] | [+/-X%] |
| Organic Revenue | $[X] | $[X] | [+/-X%] | [+/-X%] |

## Notable Ranking Changes

**Gained:**
| Keyword | Volume | Old Position | New Position | Page |
|---------|--------|-------------|-------------|------|
| [kw] | [vol] | [X] | [X] | [url] |

**Lost:**
| Keyword | Volume | Old Position | New Position | Page |
|---------|--------|-------------|-------------|------|
| [kw] | [vol] | [X] | [X] | [url] |

## Actions Taken This Month

- [Action 1] -- Result: [Observed impact]
- [Action 2] -- Result: [Observed impact]
- [Action 3] -- Result: [Pending measurement]

## Next Month Priorities

1. [Priority 1] -- Expected impact: [X]
2. [Priority 2] -- Expected impact: [X]
3. [Priority 3] -- Expected impact: [X]
```
