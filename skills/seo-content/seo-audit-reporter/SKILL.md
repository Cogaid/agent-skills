---
name: seo-audit-reporter
description: Run and report comprehensive SEO audits covering technical, on-page, off-page, and content factors. Use when the user mentions "SEO audit," "site audit," "technical SEO," "crawl errors," "page speed," "backlink analysis," "SEO report," "search optimization," "site health," "SEO checklist," or "SEO recommendations."
metadata:
  version: 1.0.0
  category: seo-content
---

# SEO Audit Reporter

Run and report comprehensive SEO audits that cover technical infrastructure, on-page optimization, off-page signals, and content quality.

## Purpose

Systematically evaluate a website's search performance across all SEO dimensions, identify issues by priority, and deliver actionable recommendations with tracking templates for ongoing improvement.

## Quick Reference

### Audit Dimensions

| Dimension | Weight | Key Signals | Tools |
|-----------|--------|-------------|-------|
| **Technical SEO** | 30% | Crawlability, indexing, speed, structure | Screaming Frog, GSC |
| **On-Page SEO** | 25% | Titles, metas, headings, content, keywords | Ahrefs, Surfer |
| **Content Quality** | 25% | Depth, freshness, relevance, E-E-A-T | Manual + tools |
| **Off-Page SEO** | 20% | Backlinks, authority, brand signals | Ahrefs, Moz |

### SEO Health Score Rubric

| Score Range | Rating | Action Required |
|-------------|--------|-----------------|
| 90-100 | Excellent | Maintain and optimize |
| 75-89 | Good | Address minor issues |
| 60-74 | Fair | Prioritized improvements needed |
| 40-59 | Poor | Significant overhaul needed |
| 0-39 | Critical | Foundational issues present |

## Workflow

### Full Audit Checklist

```
SEO AUDIT PROGRESS:

TECHNICAL SEO:
- [ ] Crawl site with Screaming Frog (or equivalent)
- [ ] Check robots.txt and XML sitemap
- [ ] Verify indexing status in Google Search Console
- [ ] Identify crawl errors (4xx, 5xx, redirect chains)
- [ ] Test page speed (Core Web Vitals) for top 20 pages
- [ ] Check mobile-friendliness
- [ ] Verify HTTPS across all pages
- [ ] Check canonical tags and hreflang (if multilingual)
- [ ] Review structured data / schema markup
- [ ] Check internal linking structure and orphan pages

ON-PAGE SEO:
- [ ] Audit title tags (length, keyword, uniqueness)
- [ ] Audit meta descriptions (length, CTR optimization)
- [ ] Check heading hierarchy (H1-H6)
- [ ] Review URL structure
- [ ] Check image alt text and file sizes
- [ ] Analyze keyword targeting per page
- [ ] Check for thin or duplicate content
- [ ] Review internal link distribution

CONTENT QUALITY:
- [ ] Identify top 20 pages by traffic
- [ ] Identify declining pages (traffic loss >20%)
- [ ] Check content freshness (last updated dates)
- [ ] Evaluate E-E-A-T signals
- [ ] Identify content gaps vs. competitors
- [ ] Review content-to-code ratio
- [ ] Check for keyword cannibalization

OFF-PAGE SEO:
- [ ] Analyze backlink profile (total, referring domains)
- [ ] Check domain authority / domain rating
- [ ] Identify toxic/spammy backlinks
- [ ] Compare backlink profile to top 3 competitors
- [ ] Review brand mention sentiment
- [ ] Check local SEO signals (if applicable)
```

## Templates

### Technical SEO Audit Template

```
TECHNICAL SEO AUDIT
Site: {{url}}
Crawl Date: {{date}}
Pages Crawled: {{count}}
Tool: {{tool_name}}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CRAWL SUMMARY:
| Metric | Count | % of Total | Status |
|--------|-------|------------|--------|
| Total pages found | {{count}} | 100% | — |
| Pages indexed | {{count}} | {{pct}}% | {{status}} |
| Pages not indexed | {{count}} | {{pct}}% | {{status}} |
| 200 OK | {{count}} | {{pct}}% | OK |
| 301 Redirects | {{count}} | {{pct}}% | Review |
| 302 Temporary redirects | {{count}} | {{pct}}% | Fix |
| 404 Not Found | {{count}} | {{pct}}% | Fix |
| 5xx Server errors | {{count}} | {{pct}}% | Critical |
| Redirect chains (3+) | {{count}} | {{pct}}% | Fix |
| Orphan pages | {{count}} | {{pct}}% | Review |

CRAWL ERRORS BY CATEGORY:
| Error Type | Count | Example URLs | Priority |
|-----------|-------|--------------|----------|
| Broken internal links | {{n}} | {{url}} | High |
| Missing canonical | {{n}} | {{url}} | Medium |
| Duplicate title tags | {{n}} | {{url}} | Medium |
| Missing meta description | {{n}} | {{url}} | Low |
| Mixed content (HTTP/HTTPS) | {{n}} | {{url}} | High |
| Missing alt text | {{n}} | {{url}} | Low |
| Blocked by robots.txt | {{n}} | {{url}} | Review |
```

### Page Speed Analysis Template

```
CORE WEB VITALS REPORT
Date: {{date}}
Tool: PageSpeed Insights / Lighthouse

TOP PAGES PERFORMANCE:
| Page | LCP | FID/INP | CLS | Speed Score | Status |
|------|-----|---------|-----|-------------|--------|
| Homepage | {{lcp}}s | {{fid}}ms | {{cls}} | {{score}} | {{pass/fail}} |
| {{page_2}} | {{lcp}}s | {{fid}}ms | {{cls}} | {{score}} | {{pass/fail}} |
| {{page_3}} | {{lcp}}s | {{fid}}ms | {{cls}} | {{score}} | {{pass/fail}} |
| {{page_4}} | {{lcp}}s | {{fid}}ms | {{cls}} | {{score}} | {{pass/fail}} |
| {{page_5}} | {{lcp}}s | {{fid}}ms | {{cls}} | {{score}} | {{pass/fail}} |

CWV THRESHOLDS:
| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP (Largest Contentful Paint) | <2.5s | 2.5-4.0s | >4.0s |
| INP (Interaction to Next Paint) | <200ms | 200-500ms | >500ms |
| CLS (Cumulative Layout Shift) | <0.1 | 0.1-0.25 | >0.25 |

TOP SPEED ISSUES:
1. {{issue_1}} — Impact: {{high/med/low}} — Fix: {{recommendation}}
2. {{issue_2}} — Impact: {{high/med/low}} — Fix: {{recommendation}}
3. {{issue_3}} — Impact: {{high/med/low}} — Fix: {{recommendation}}
```

### Backlink Profile Assessment

```
BACKLINK PROFILE ANALYSIS
Domain: {{domain}}
Date: {{date}}

OVERVIEW:
| Metric | Value | Industry Avg | Status |
|--------|-------|-------------|--------|
| Domain Rating (DR) | {{dr}} | {{avg}} | {{status}} |
| Total Backlinks | {{total}} | {{avg}} | {{status}} |
| Referring Domains | {{rd}} | {{avg}} | {{status}} |
| Dofollow / Nofollow | {{df}}% / {{nf}}% | 70/30 | {{status}} |
| New links (30 days) | {{new}} | {{avg}} | {{status}} |
| Lost links (30 days) | {{lost}} | {{avg}} | {{status}} |

LINK QUALITY DISTRIBUTION:
| DR Range | Referring Domains | % of Total |
|----------|------------------|------------|
| DR 70-100 | {{count}} | {{pct}}% |
| DR 40-69 | {{count}} | {{pct}}% |
| DR 10-39 | {{count}} | {{pct}}% |
| DR 0-9 | {{count}} | {{pct}}% |

TOP LINKING DOMAINS:
| Domain | DR | Links | Type | Anchor |
|--------|-----|-------|------|--------|
| {{domain}} | {{dr}} | {{n}} | {{type}} | {{anchor}} |

TOXIC LINKS (review for disavow):
| Domain | Spam Score | Links | Recommendation |
|--------|-----------|-------|---------------|
| {{domain}} | {{score}} | {{n}} | {{action}} |
```

### Competitor Gap Analysis

```
COMPETITOR SEO GAP ANALYSIS
Your Domain: {{your_domain}}
Competitors: {{comp_1}}, {{comp_2}}, {{comp_3}}

DOMAIN AUTHORITY COMPARISON:
| Domain | DR | Ref. Domains | Organic Traffic | Keywords |
|--------|-----|-------------|-----------------|----------|
| {{you}} | {{dr}} | {{rd}} | {{traffic}} | {{kw}} |
| {{comp1}} | {{dr}} | {{rd}} | {{traffic}} | {{kw}} |
| {{comp2}} | {{dr}} | {{rd}} | {{traffic}} | {{kw}} |
| {{comp3}} | {{dr}} | {{rd}} | {{traffic}} | {{kw}} |

KEYWORD GAPS (they rank, you don't):
| Keyword | Volume | {{comp1}} Rank | {{comp2}} Rank | Your Rank | Opportunity |
|---------|--------|---------------|---------------|-----------|-------------|
| {{kw}} | {{vol}} | {{rank}} | {{rank}} | Not ranking | {{priority}} |

CONTENT GAPS:
| Topic | Competitor Coverage | Your Coverage | Action |
|-------|-------------------|---------------|--------|
| {{topic}} | {{comp}} has {{pages}} pages | {{your_pages}} pages | {{create/expand}} |

BACKLINK GAPS (domains linking to them, not you):
| Referring Domain | DR | Links to {{comp1}} | Links to {{comp2}} | Links to You |
|-----------------|-----|-------------------|-------------------|-------------|
| {{domain}} | {{dr}} | Yes | Yes | No |
```

### Prioritized Recommendations Format

```
SEO AUDIT RECOMMENDATIONS
Site: {{url}}
Audit Date: {{date}}
Overall Score: {{score}}/100

PRIORITY 1 — CRITICAL (fix within 2 weeks):
| # | Issue | Pages Affected | Impact | Effort | Recommendation |
|---|-------|---------------|--------|--------|---------------|
| 1 | {{issue}} | {{count}} | High | {{effort}} | {{fix}} |
| 2 | {{issue}} | {{count}} | High | {{effort}} | {{fix}} |

PRIORITY 2 — HIGH (fix within 1 month):
| # | Issue | Pages Affected | Impact | Effort | Recommendation |
|---|-------|---------------|--------|--------|---------------|
| 3 | {{issue}} | {{count}} | Med-High | {{effort}} | {{fix}} |
| 4 | {{issue}} | {{count}} | Med-High | {{effort}} | {{fix}} |

PRIORITY 3 — MEDIUM (fix within 3 months):
| # | Issue | Pages Affected | Impact | Effort | Recommendation |
|---|-------|---------------|--------|--------|---------------|
| 5 | {{issue}} | {{count}} | Medium | {{effort}} | {{fix}} |

PRIORITY 4 — LOW (ongoing optimization):
| # | Issue | Pages Affected | Impact | Effort | Recommendation |
|---|-------|---------------|--------|--------|---------------|
| 6 | {{issue}} | {{count}} | Low | {{effort}} | {{fix}} |
```

### Monthly Tracking Template

```
SEO MONTHLY TRACKING
Month: {{month}} {{year}}

| Metric | This Month | Last Month | Change | YoY Change |
|--------|-----------|------------|--------|------------|
| Organic Sessions | {{val}} | {{prior}} | {{delta}} | {{yoy}} |
| Organic Clicks (GSC) | {{val}} | {{prior}} | {{delta}} | {{yoy}} |
| Impressions (GSC) | {{val}} | {{prior}} | {{delta}} | {{yoy}} |
| Average Position | {{val}} | {{prior}} | {{delta}} | {{yoy}} |
| CTR (GSC) | {{val}}% | {{prior}}% | {{delta}} | {{yoy}} |
| Indexed Pages | {{val}} | {{prior}} | {{delta}} | {{yoy}} |
| Domain Rating | {{val}} | {{prior}} | {{delta}} | {{yoy}} |
| Referring Domains | {{val}} | {{prior}} | {{delta}} | {{yoy}} |
| Core Web Vitals Pass | {{val}}% | {{prior}}% | {{delta}} | {{yoy}} |
| Top 3 Rankings | {{val}} | {{prior}} | {{delta}} | {{yoy}} |
| Top 10 Rankings | {{val}} | {{prior}} | {{delta}} | {{yoy}} |

ISSUES FIXED THIS MONTH:
- {{issue_1}} — Impact: {{result}}
- {{issue_2}} — Impact: {{result}}

NEXT MONTH PRIORITIES:
1. {{priority_1}}
2. {{priority_2}}
3. {{priority_3}}
```

## Scripts & Tools

**run_audit.py**: Execute a full SEO audit
```bash
python scripts/run_audit.py --url https://example.com --depth full
# Output: Complete audit report across all dimensions
```

**check_speed.py**: Run Core Web Vitals analysis
```bash
python scripts/check_speed.py --url https://example.com --pages top-20
# Output: Page speed scores with specific improvement recommendations
```

**backlink_analysis.py**: Analyze backlink profile
```bash
python scripts/backlink_analysis.py --domain example.com --compare competitor.com
# Output: Backlink comparison with gap analysis
```

**track_rankings.py**: Track keyword ranking changes
```bash
python scripts/track_rankings.py --domain example.com --keywords keywords.csv
# Output: Ranking changes with trend visualization
```

## Best Practices

1. **Audit quarterly** - Full audits every quarter; technical checks monthly
2. **Prioritize by impact x effort** - Fix high-impact, low-effort issues first
3. **Track before and after** - Measure baseline before implementing changes
4. **Fix technical before content** - Crawl and index issues block all other efforts
5. **Compare to competitors** - Absolute metrics matter less than relative position
6. **Focus on Core Web Vitals** - Google uses them as ranking signals
7. **Monitor GSC weekly** - Search Console shows issues before traffic drops
8. **Document everything** - Future audits need to see what was already tried
9. **Align with business goals** - Optimize pages that drive revenue, not just traffic
10. **Stay current** - Algorithm updates change what matters; adapt accordingly

## Related Skills

- Content planning: `content-calendar`
- Keyword research: `keyword-research`
- Competitor analysis: `competitor-content-analyzer`
- Content optimization: `content-optimizer`
