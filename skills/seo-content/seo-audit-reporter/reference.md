# SEO Audit Reporter -- Reference Guide

Detailed reference documentation for conducting comprehensive SEO audits.

## Technical SEO Deep Dive

### Crawlability and Indexing

**robots.txt best practices:**
- Allow all important pages and resources (CSS, JS, images)
- Block admin, staging, duplicate, and thin-content directories
- Reference XML sitemap(s) at the bottom
- Keep rules simple -- complex logic is error-prone
- Test changes in Google Search Console before deploying

**Common robots.txt mistakes:**
| Mistake | Impact | Fix |
|---------|--------|-----|
| Blocking CSS/JS | Pages render incorrectly for Googlebot | Allow /css/ and /js/ |
| Blocking images | Lose image search traffic | Allow /images/ and /media/ |
| Wildcard overblocking | Important pages excluded | Use specific paths |
| Blocking sitemap path | Sitemap not discovered | Ensure sitemap path is accessible |
| Forgetting staging subdomain | Staging pages indexed | Add noindex + robots block |

**XML Sitemap requirements:**
- Maximum 50,000 URLs per sitemap (use sitemap index for larger sites)
- Maximum 50MB uncompressed file size
- Include only canonical, indexable, 200-status pages
- Update `<lastmod>` when content changes (not on every crawl)
- Remove 404, 301, and noindex pages
- Submit in Google Search Console and Bing Webmaster Tools

**Index management signals (priority order):**
1. `noindex` meta tag (strongest -- Googlebot will respect)
2. Canonical tag (consolidates signals to preferred URL)
3. robots.txt disallow (prevents crawling, not indexing if linked)
4. X-Robots-Tag HTTP header (for non-HTML resources)
5. URL parameter handling in GSC (deprecated but still partially active)

### Core Web Vitals

**Largest Contentful Paint (LCP) -- Loading performance:**

| Rating | Threshold | Target |
|--------|-----------|--------|
| Good | < 2.5s | < 2.0s |
| Needs Improvement | 2.5-4.0s | -- |
| Poor | > 4.0s | -- |

Common LCP issues and fixes:
| Issue | Diagnosis | Fix |
|-------|-----------|-----|
| Slow server response | TTFB > 600ms | CDN, server optimization, caching |
| Render-blocking resources | Large CSS/JS in head | Critical CSS inline, defer JS |
| Slow resource load | Large hero image | Optimize images, use WebP/AVIF, preload |
| Client-side rendering | Blank until JS executes | SSR or pre-rendering |

**Interaction to Next Paint (INP) -- Responsiveness:**

| Rating | Threshold | Target |
|--------|-----------|--------|
| Good | < 200ms | < 100ms |
| Needs Improvement | 200-500ms | -- |
| Poor | > 500ms | -- |

Common INP issues:
| Issue | Diagnosis | Fix |
|-------|-----------|-----|
| Long tasks | Main thread blocked > 50ms | Break up tasks, use web workers |
| Excessive DOM size | > 1500 nodes | Virtualize lists, lazy-load content |
| Heavy event handlers | Slow click/input response | Debounce, optimize handlers |
| Layout thrashing | Forced reflows in loops | Batch DOM reads/writes |

**Cumulative Layout Shift (CLS) -- Visual stability:**

| Rating | Threshold | Target |
|--------|-----------|--------|
| Good | < 0.1 | < 0.05 |
| Needs Improvement | 0.1-0.25 | -- |
| Poor | > 0.25 | -- |

Common CLS issues:
| Issue | Fix |
|-------|-----|
| Images without dimensions | Always set width/height or aspect-ratio |
| Ads/embeds without reserved space | Use min-height containers |
| Web fonts causing FOUT | font-display: swap + preload |
| Dynamic content above fold | Reserve space, use CSS containment |
| Late-loading banners/modals | Load above-fold content first |

### Site Architecture

**Internal linking best practices:**
- Every important page should be reachable within 3 clicks from homepage
- Flat architecture is preferred for SEO (fewer directory levels)
- Use descriptive anchor text (not "click here")
- Distribute link equity: link from high-authority pages to priority pages
- Identify and fix orphan pages (no internal links pointing to them)
- Use breadcrumbs for hierarchical navigation

**URL structure guidelines:**
- Use hyphens (not underscores) to separate words
- Keep URLs short (under 75 characters ideal)
- Include target keyword in the URL path
- Use lowercase only
- Avoid parameters when possible (use path-based URLs)
- Maintain consistent patterns (/blog/post-title, /products/category/product)

### HTTPS and Security

**HTTPS checklist:**
- [ ] Valid SSL certificate (not expired, correct domain)
- [ ] All pages serve over HTTPS (no HTTP versions accessible)
- [ ] Mixed content resolved (no HTTP resources on HTTPS pages)
- [ ] HTTP to HTTPS redirects in place (301, not 302)
- [ ] HSTS header configured
- [ ] Internal links use HTTPS
- [ ] Canonical tags use HTTPS
- [ ] Sitemap uses HTTPS URLs

## On-Page SEO Deep Dive

### Title Tag Optimization

**Best practices:**
- 50-60 characters (Google displays ~580px width)
- Primary keyword first (or as early as possible)
- Each page has a unique title
- Include brand name (usually at end, separated by | or -)
- Compelling for clicks (not just keyword-stuffed)

**Title tag formulas:**
| Type | Formula | Example |
|------|---------|---------|
| How-to | How to [Keyword]: [Benefit] | How to Write SEO Titles: Get More Clicks |
| Listicle | [Number] [Keyword] [Modifier] in [Year] | 15 Best SEO Tools for Small Business in 2025 |
| Product | [Brand] [Product] - [Benefit] | Ahrefs Site Audit - Find SEO Issues Fast |
| Comparison | [A] vs [B]: [Differentiator] | Ahrefs vs SEMrush: Which SEO Tool Wins? |
| Guide | [Keyword] Guide: [Scope] | Technical SEO Guide: From Beginner to Expert |

### Meta Description Optimization

**Best practices:**
- 150-160 characters (Google displays ~920px width)
- Include primary keyword (will be bolded in SERP)
- Include a clear CTA or value proposition
- Unique per page
- Accurately represent page content
- Use active voice

### Heading Hierarchy

**Rules:**
- One H1 per page (matching or closely related to title tag)
- H2s for main sections (can include keyword variations)
- H3s for subsections
- Never skip levels (H1 -> H3 without H2)
- Use headings for structure, not just styling
- Include keywords naturally (not forced)

### Content Quality Signals

**E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness):**

| Signal | How to Demonstrate |
|--------|-------------------|
| Experience | First-hand experience, original photos, personal insights |
| Expertise | Author credentials, accurate information, depth of coverage |
| Authoritativeness | Backlinks from trusted sources, citations, brand recognition |
| Trustworthiness | HTTPS, clear contact info, accurate claims, editorial process |

**Content freshness signals:**
- Publish date visible on page
- "Last updated" date when content is refreshed
- Regular publishing cadence (shows active site)
- Timely references (current year, recent data)
- No outdated information (dead links, old screenshots)

## Off-Page SEO Deep Dive

### Backlink Quality Assessment

**High-quality link characteristics:**
- From a topically relevant site
- From a page with real traffic
- Editorial placement (not paid, not automated)
- Surrounded by relevant content
- From a unique referring domain (diversity matters)
- Dofollow (passes PageRank)
- From a high-DR/DA domain

**Toxic link indicators:**
| Indicator | Concern Level | Action |
|-----------|--------------|--------|
| Spam score > 60 | High | Consider disavow |
| Site-wide footer/sidebar links | Medium | Monitor |
| Irrelevant foreign language sites | High | Consider disavow |
| PBN patterns (similar templates, no traffic) | High | Disavow |
| Paid link networks | High | Disavow |
| Excessive exact-match anchors | Medium | Diversify anchor profile |
| Links from penalized sites | High | Disavow |

### Link Building Opportunities

**By content type:**
| Content Type | Avg. Links Earned | Effort | Timeline |
|-------------|------------------|--------|----------|
| Original research/data | 50-200 | High | 4-8 weeks |
| Interactive tools | 30-100 | High | 6-12 weeks |
| Comprehensive guides | 20-50 | Medium | 3-6 weeks |
| Infographics | 10-30 | Medium | 2-4 weeks |
| Expert roundups | 10-25 | Low | 2-3 weeks |
| Resource pages/lists | 5-20 | Low | 1-2 weeks |
| Broken link reclamation | 5-15 | Low | 1-2 weeks |
| Guest posting | 1-3 per post | Low | 1-2 weeks |

## Scoring Methodology

### How to Calculate the SEO Health Score

The SEO Health Score (0-100) is a weighted composite:

```
Score = (Technical * 0.30) + (On-Page * 0.25) + (Content * 0.25) + (Off-Page * 0.20)
```

Each dimension is scored 0-100 based on the percentage of checks passed:

**Technical SEO (30% weight):**
| Check | Points | Criteria |
|-------|--------|----------|
| Crawlability | 15 | robots.txt correct, no critical blocks |
| Indexing | 15 | >90% target pages indexed |
| Page speed | 20 | Core Web Vitals pass rate |
| Mobile | 15 | Mobile-friendly test pass |
| HTTPS | 10 | Full HTTPS, no mixed content |
| Structure | 15 | Clean URLs, proper canonicals, schema |
| Errors | 10 | <1% 4xx/5xx pages |

**On-Page SEO (25% weight):**
| Check | Points | Criteria |
|-------|--------|----------|
| Title tags | 20 | Unique, correct length, keyword present |
| Meta descriptions | 15 | Unique, correct length, keyword present |
| Headings | 15 | Proper hierarchy, H1 unique per page |
| URLs | 10 | Clean, keyword-rich, no parameters |
| Images | 15 | Alt text present, optimized file size |
| Internal links | 15 | No orphans, good distribution |
| Content uniqueness | 10 | No duplicate or thin content |

**Content Quality (25% weight):**
| Check | Points | Criteria |
|-------|--------|----------|
| Depth/word count | 20 | Competitive word count per topic |
| Freshness | 15 | Updated within 12 months |
| E-E-A-T signals | 20 | Author pages, credentials, citations |
| Keyword targeting | 20 | Clear intent match, no cannibalization |
| Engagement | 15 | Low bounce, good time on page |
| Coverage | 10 | No major topic gaps vs. competitors |

**Off-Page SEO (20% weight):**
| Check | Points | Criteria |
|-------|--------|----------|
| Domain authority | 25 | DR competitive with industry peers |
| Referring domains | 25 | Growing or stable referring domain count |
| Link quality | 20 | High DR links, low toxic percentage |
| Anchor diversity | 15 | Natural anchor text distribution |
| Brand signals | 15 | Brand mentions, branded search volume |

## Tool Recommendations

### Free Tools

| Tool | Use Case |
|------|----------|
| Google Search Console | Index status, search performance, Core Web Vitals |
| Google PageSpeed Insights | Page speed + Core Web Vitals per page |
| Google Rich Results Test | Structured data validation |
| Bing Webmaster Tools | Additional search engine perspective |
| Screaming Frog (free tier) | Crawl up to 500 pages |
| GTmetrix | Performance waterfall analysis |

### Paid Tools

| Tool | Best For | Price Range |
|------|----------|-------------|
| Ahrefs | Backlinks, keywords, competitor analysis | $99-$999/mo |
| SEMrush | All-in-one SEO + PPC | $120-$450/mo |
| Screaming Frog (paid) | Full technical crawls | $259/year |
| Surfer SEO | On-page content optimization | $69-$219/mo |
| Moz Pro | Domain authority, local SEO | $99-$599/mo |
| BuzzSumo | Content performance, social shares | $119-$999/mo |

## Reporting Cadence

| Report Type | Frequency | Audience | Focus |
|------------|-----------|----------|-------|
| Full audit | Quarterly | Marketing leadership | All dimensions, strategic |
| Technical check | Monthly | Dev + SEO team | Errors, speed, indexing |
| Rankings report | Weekly | SEO team | Position tracking, new keywords |
| Content performance | Monthly | Content team | Traffic, engagement, gaps |
| Backlink monitoring | Monthly | SEO team | New/lost links, toxic cleanup |
| Competitor update | Quarterly | Strategy team | Gap analysis, opportunities |
