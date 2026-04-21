# Competitor Content Analyzer -- Reference Guide

Detailed reference documentation for analyzing competitor content strategies.

## Competitor Selection Framework

### How to Choose the Right Competitors

Not all competitors deserve equal analysis time. Use this scoring matrix:

**Step 1: Identify candidates (aim for 8-10)**
- Direct business competitors (same product/service category)
- SERP competitors (rank for your target keywords)
- Aspirational competitors (content quality you want to match)
- Adjacent competitors (different product, same audience)

**Step 2: Score each candidate (0-10 per criterion)**

| Criterion | Weight | How to Score |
|-----------|--------|-------------|
| SERP overlap | 30% | % of your target keywords where they rank in top 20 |
| Audience overlap | 25% | How similar their target persona is to yours |
| Content maturity | 20% | Age and consistency of their content program |
| Business similarity | 15% | How similar their business model/positioning is |
| Aspirational quality | 10% | Quality of content you want to match or exceed |

**Step 3: Select top 3-5 for deep analysis**

Final score = (SERP * 0.30) + (Audience * 0.25) + (Maturity * 0.20) + (Business * 0.15) + (Aspirational * 0.10)

### Types of Competitive Analysis

| Type | Frequency | Depth | Output |
|------|-----------|-------|--------|
| Continuous monitoring | Weekly | Light | Alert-based (new content, ranking changes) |
| Tactical analysis | Monthly | Medium | Topic gaps, content opportunities |
| Strategic deep-dive | Quarterly | Full | Comprehensive audit with action plan |
| One-time benchmark | Once | Full | Baseline assessment for new programs |

## Content Audit Methodology

### Step-by-Step Process

**Phase 1: Data Collection (Tools + Manual)**

1. Crawl their content hub (Screaming Frog, Sitebulb, or manual)
2. Export keyword data (Ahrefs Content Explorer or SEMrush)
3. Pull social metrics (BuzzSumo or manual)
4. Catalog content by hand for quality signals

**Phase 2: Classification**

Categorize every piece of competitor content along these dimensions:

| Dimension | Categories |
|-----------|-----------|
| Topic area | [Map to your pillar structure] |
| Content type | Blog, guide, video, podcast, tool, whitepaper, case study |
| Format | How-to, listicle, comparison, opinion, news, research, interview |
| Funnel stage | TOFU (awareness), MOFU (consideration), BOFU (decision) |
| Content depth | Thin (<500w), standard (500-1500w), long-form (1500-3000w), comprehensive (3000w+) |
| Age | <3mo, 3-6mo, 6-12mo, 1-2yr, 2yr+ |
| Update frequency | Regularly updated, occasionally updated, never updated |

**Phase 3: Performance Estimation**

| Metric | Data Source | What It Tells You |
|--------|------------|-------------------|
| Estimated organic traffic | Ahrefs/SEMrush | Search performance |
| Keywords ranking | Ahrefs/SEMrush | Topic authority |
| Referring domains | Ahrefs | Link-worthiness |
| Social shares | BuzzSumo | Audience resonance |
| Comments/engagement | Manual | Community building |
| Publish date / updates | Manual / Wayback | Content freshness strategy |

**Phase 4: Pattern Recognition**

Look for patterns in what works for them:
- What topics get the most traffic?
- What formats earn the most links?
- What content gets shared most on social?
- How long is their best-performing content?
- How often do they publish?
- What's their content-to-link ratio?

## Gap Analysis Framework

### Three Types of Content Gaps

**1. Topic Gaps (they cover, you don't)**

These are keywords and topics where competitors rank but you have no content at all.

Prioritization criteria:
| Factor | Weight | How to Assess |
|--------|--------|---------------|
| Search volume | 25% | Monthly searches for the target keyword |
| Business relevance | 25% | How closely topic connects to your product |
| Keyword difficulty | 20% | Your realistic ability to rank (based on DA) |
| Competitor weakness | 15% | Quality of their existing content (beatable?) |
| Intent match | 15% | Does the search intent align with your funnel? |

**2. Depth Gaps (both cover, they go deeper)**

These are topics where you have content, but competitors cover them more thoroughly and rank higher.

Diagnosis:
- Compare word count, subtopics covered, media included
- Check which questions they answer that you don't
- Look at their heading structure vs. yours
- Compare their backlinks on that page to yours

**3. Freshness Gaps (their content is outdated)**

These are opportunities where competitor content is old, outdated, or stale. You can win by publishing fresher, more current content.

Indicators:
- Published date > 18 months ago with no updates
- Outdated statistics or references
- Dead links or discontinued products mentioned
- Missing coverage of recent developments
- Older screenshots or examples

### Content Opportunity Scoring

Score each gap opportunity (1-10) across:

```
Opportunity Score = (Volume * 0.25) + (Relevance * 0.25) + 
                   (Winnability * 0.25) + (Competitor Weakness * 0.25)
```

| Score | Priority | Action |
|-------|----------|--------|
| 8-10 | High | Create within 30 days |
| 6-7 | Medium | Plan for next quarter |
| 4-5 | Low | Add to backlog |
| 1-3 | Skip | Not worth pursuing now |

## SERP Analysis Deep Dive

### SERP Feature Ownership

Track who owns special SERP features for your target keywords:

| Feature | How to Win It | Priority |
|---------|--------------|----------|
| Featured snippet (paragraph) | Direct answer in 40-60 words, under a question heading | High |
| Featured snippet (list) | Numbered/bulleted list structure with clear steps | High |
| Featured snippet (table) | Well-structured HTML table with clear headers | Medium |
| People Also Ask | Answer related questions clearly in content | High |
| Video carousel | YouTube video optimized for the keyword | Medium |
| Image pack | Optimized images with descriptive alt text + filename | Low |
| Knowledge panel | Structured data + Wikipedia/Wikidata presence | Low |

### Search Intent Classification

For every target keyword, classify the dominant intent:

| Intent Type | SERP Signals | Content Approach |
|------------|-------------|-----------------|
| Informational | How-to articles, guides, wikis | Educational content, comprehensive guides |
| Commercial investigation | Comparisons, reviews, "best of" | Comparison pages, buyer's guides |
| Transactional | Product pages, pricing, "buy" | Product pages, landing pages |
| Navigational | Brand homepage, specific pages | Ensure your branded pages rank #1 |

## Link-Worthy Content Patterns

### What Earns Links (by content type)

| Content Type | Avg. Referring Domains | Why It Works | Your Action |
|-------------|----------------------|-------------|-------------|
| Original research/data | 50-200 | Unique data others want to cite | Conduct surveys, analyze proprietary data |
| Free tools/calculators | 30-150 | Ongoing utility value | Build tools that solve common problems |
| Comprehensive guides | 20-80 | One-stop reference | Create the definitive guide for your niche |
| Industry reports | 20-60 | Authority + fresh data | Annual/quarterly reports with proprietary data |
| Infographics with data | 15-50 | Easy to embed and share | Visualize complex data attractively |
| Expert roundups | 10-30 | Contributors share and link | Curate insights from recognized experts |
| Templates and frameworks | 10-25 | Practical utility | Create downloadable, reusable assets |

### Reverse-Engineering Competitor Links

Process for studying why a competitor page earned links:

1. Identify their top-linked pages (Ahrefs: Best by Links)
2. For each page, examine:
   - What type of content is it?
   - What makes it link-worthy? (Data? Tool? First-of-its-kind?)
   - Who links to it? (What type of sites?)
   - What anchor text do they use? (Indicates what linkers value)
3. Create something better:
   - More current data
   - More comprehensive coverage
   - Better design/UX
   - Additional formats (add video, interactive elements)
   - Unique angle or data they don't have

## Monitoring and Alerts

### What to Monitor

| Signal | Tool | Frequency | Action Trigger |
|--------|------|-----------|---------------|
| New content published | RSS, Visualping | Daily | Review for gaps/threats |
| Ranking changes (your keywords) | Ahrefs, SEMrush | Weekly | Investigate if competitor gains |
| New backlinks earned | Ahrefs alerts | Weekly | Study what earned the link |
| Social viral content | BuzzSumo alerts | Daily | Identify trending topics |
| New keywords ranking | SEMrush | Monthly | Spot new content investments |
| Site structure changes | Screaming Frog | Monthly | Understand strategic shifts |
| Traffic trend changes | SimilarWeb | Monthly | Assess overall strategy impact |

### Competitive Intelligence Sources

Beyond tools, gather intelligence from:
- **Their blog RSS feed** -- subscribe to all competitors
- **Their email newsletter** -- sign up with a personal email
- **Their social accounts** -- follow and note patterns
- **Their job postings** -- content team growth signals investment
- **Their press releases** -- product launches affect content needs
- **Their conference talks** -- reveals strategic thinking
- **Their podcast appearances** -- deep insights into strategy
- **Customer reviews (G2, Capterra)** -- reveals positioning

## Reporting Best Practices

### What Stakeholders Care About

| Stakeholder | Key Questions | Metrics to Show |
|------------|--------------|----------------|
| CMO/VP Marketing | Are we winning? Where should we invest? | Share of voice, gap size, opportunity value |
| Content Manager | What should we create? What's not working? | Topic gaps, priorities, underperforming pages |
| SEO Manager | Where are we losing ground? | Ranking changes, new competitor content, link gaps |
| Sales Team | What proof do competitors offer? | Their case studies, comparison pages, objection handling |
| Product Team | How do competitors position features? | Feature messaging, use cases highlighted, terminology |

### Deliverable Formats

| Analysis Type | Best Format | Audience | Cadence |
|-------------|-------------|----------|---------|
| Quick wins list | Prioritized table | Content team | Monthly |
| Full competitive audit | Detailed report with screenshots | Leadership | Quarterly |
| Topic gap analysis | Spreadsheet with scoring | SEO + Content | Monthly |
| Content performance comparison | Dashboard/chart | All marketing | Monthly |
| Strategic recommendations | Presentation + memo | Leadership | Quarterly |
