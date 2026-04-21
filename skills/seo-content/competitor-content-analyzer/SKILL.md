---
name: competitor-content-analyzer
description: Analyze competitor content strategies to identify gaps and opportunities. Use when the user mentions "competitor content," "content analysis," "competitor blog," "content gap," "topic gap," "SERP analysis," "competitor strategy," "content benchmarking," "competitive content," or "content comparison."
metadata:
  version: 1.0.0
  category: seo-content
---

# Competitor Content Analyzer

Analyze competitor content strategies to identify gaps, benchmark performance, and uncover actionable opportunities for your content program.

## Purpose

Systematically evaluate what competitors publish, how it performs, where they earn links and engagement, and where gaps exist that you can exploit. Covers content auditing, topic gap analysis, performance estimation, backlink analysis, SERP overlap, and actionable recommendations.

## Quick Reference

### Analysis Dimensions

| Dimension | What It Reveals | Data Sources | Priority |
|-----------|----------------|-------------|----------|
| **Content volume** | Publishing frequency and capacity | Site crawl, blog index | Medium |
| **Topic coverage** | What subjects they cover | Keyword tools, manual review | High |
| **Content quality** | Depth, E-E-A-T, production value | Manual assessment | High |
| **SEO performance** | Rankings, traffic, keywords | Ahrefs, SEMrush | High |
| **Backlink profile** | Link-worthy content and sources | Ahrefs, Moz | Medium |
| **Social engagement** | Audience resonance and reach | BuzzSumo, social APIs | Medium |
| **Content format** | Blog, video, podcast, interactive | Manual audit | Medium |
| **Update frequency** | How often content is refreshed | Wayback, publish dates | Low |

### Competitor Selection Criteria

| Criterion | Weight | How to Evaluate |
|-----------|--------|----------------|
| **SERP overlap** | 30% | % of your target keywords where they rank |
| **Audience overlap** | 25% | Similar target persona and industry |
| **Content maturity** | 20% | Established content program with history |
| **Business similarity** | 15% | Similar product/service category |
| **Aspirational quality** | 10% | Content quality you want to match/exceed |

## Workflow

### Competitor Content Analysis Checklist

```
Analysis Progress:
- [ ] Step 1: Select 3-5 competitors to analyze
- [ ] Step 2: Crawl competitor blogs/content hubs
- [ ] Step 3: Catalog content by topic, type, and format
- [ ] Step 4: Estimate traffic and keyword coverage
- [ ] Step 5: Identify their top-performing content (by traffic)
- [ ] Step 6: Identify their most-linked content (by backlinks)
- [ ] Step 7: Analyze social engagement patterns
- [ ] Step 8: Map topic coverage and find gaps
- [ ] Step 9: Evaluate content quality and depth
- [ ] Step 10: Assess SERP overlap and competitive positions
- [ ] Step 11: Generate prioritized recommendations
- [ ] Step 12: Update your content calendar with opportunities
```

## Templates

### Content Audit Framework

```
COMPETITOR CONTENT AUDIT
Competitor: {{competitor_name}}
Website: {{url}}
Audit Date: {{date}}
Content Hub URL: {{blog_url}}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CONTENT INVENTORY SUMMARY:
| Metric | Value | vs. You |
|--------|-------|---------|
| Total published pages | {{count}} | {{delta}} |
| Blog posts | {{count}} | {{delta}} |
| Landing pages | {{count}} | {{delta}} |
| Case studies | {{count}} | {{delta}} |
| Videos | {{count}} | {{delta}} |
| Podcasts | {{count}} | {{delta}} |
| Guides/white papers | {{count}} | {{delta}} |
| Tools/calculators | {{count}} | {{delta}} |

PUBLISHING CADENCE:
| Period | Posts Published | Avg per Week |
|--------|---------------|-------------|
| Last 30 days | {{count}} | {{avg}} |
| Last 90 days | {{count}} | {{avg}} |
| Last 12 months | {{count}} | {{avg}} |
| Trend | {{increasing/stable/decreasing}} | — |

CONTENT BY TOPIC AREA:
| Topic | # Pages | Est. Traffic | Top Page | Top Rank |
|-------|---------|-------------|----------|----------|
| {{topic_1}} | {{n}} | {{traffic}} | {{url}} | #{{rank}} |
| {{topic_2}} | {{n}} | {{traffic}} | {{url}} | #{{rank}} |
| {{topic_3}} | {{n}} | {{traffic}} | {{url}} | #{{rank}} |
| {{topic_4}} | {{n}} | {{traffic}} | {{url}} | #{{rank}} |
| {{topic_5}} | {{n}} | {{traffic}} | {{url}} | #{{rank}} |

CONTENT FORMAT MIX:
| Format | Count | % of Total | Performance |
|--------|-------|------------|-------------|
| Long-form (2000+ words) | {{n}} | {{pct}}% | {{avg_traffic}} |
| Mid-form (800-2000) | {{n}} | {{pct}}% | {{avg_traffic}} |
| Short-form (<800) | {{n}} | {{pct}}% | {{avg_traffic}} |
| Video | {{n}} | {{pct}}% | {{avg_views}} |
| Infographic | {{n}} | {{pct}}% | {{avg_shares}} |
| Interactive/tool | {{n}} | {{pct}}% | {{avg_traffic}} |
```

### Topic Gap Analysis

```
TOPIC GAP ANALYSIS
Your Domain: {{your_domain}}
Competitor: {{competitor_domain}}

KEYWORDS THEY RANK FOR, YOU DON'T:
| Keyword | Volume | Their Rank | Their URL | Difficulty | Priority |
|---------|--------|-----------|-----------|-----------|----------|
| {{kw}} | {{vol}} | #{{rank}} | {{url}} | {{kd}} | {{p}} |
| {{kw}} | {{vol}} | #{{rank}} | {{url}} | {{kd}} | {{p}} |
| {{kw}} | {{vol}} | #{{rank}} | {{url}} | {{kd}} | {{p}} |
| {{kw}} | {{vol}} | #{{rank}} | {{url}} | {{kd}} | {{p}} |
| {{kw}} | {{vol}} | #{{rank}} | {{url}} | {{kd}} | {{p}} |

TOPICS THEY COVER DEEPLY, YOU COVER THINLY:
| Topic | Their Coverage | Your Coverage | Gap |
|-------|---------------|---------------|-----|
| {{topic}} | {{n}} pages, {{depth}} words avg | {{n}} pages, {{depth}} words avg | {{action}} |
| {{topic}} | {{n}} pages, {{depth}} words avg | {{n}} pages, {{depth}} words avg | {{action}} |

TOPICS YOU COVER, THEY DON'T (your advantage):
| Topic | Your Pages | Your Traffic | Protect? |
|-------|-----------|-------------|----------|
| {{topic}} | {{n}} | {{traffic}} | {{yes/monitor}} |

SHARED TOPICS (head-to-head):
| Topic | Your Rank | Their Rank | Your Traffic | Their Traffic | Action |
|-------|----------|-----------|-------------|-------------|--------|
| {{topic}} | #{{rank}} | #{{rank}} | {{traffic}} | {{traffic}} | {{action}} |
```

### Content Performance Estimation

```
COMPETITOR CONTENT PERFORMANCE
Competitor: {{competitor_name}}
Tool: {{ahrefs/semrush/similarweb}}

TOP PAGES BY ESTIMATED TRAFFIC:
| Rank | URL | Est. Monthly Traffic | Top Keyword | Keywords Total |
|------|-----|---------------------|-------------|---------------|
| 1 | {{url}} | {{traffic}} | {{keyword}} | {{kw_count}} |
| 2 | {{url}} | {{traffic}} | {{keyword}} | {{kw_count}} |
| 3 | {{url}} | {{traffic}} | {{keyword}} | {{kw_count}} |
| 4 | {{url}} | {{traffic}} | {{keyword}} | {{kw_count}} |
| 5 | {{url}} | {{traffic}} | {{keyword}} | {{kw_count}} |
| 6 | {{url}} | {{traffic}} | {{keyword}} | {{kw_count}} |
| 7 | {{url}} | {{traffic}} | {{keyword}} | {{kw_count}} |
| 8 | {{url}} | {{traffic}} | {{keyword}} | {{kw_count}} |
| 9 | {{url}} | {{traffic}} | {{keyword}} | {{kw_count}} |
| 10 | {{url}} | {{traffic}} | {{keyword}} | {{kw_count}} |

CONTENT THAT RECENTLY GAINED TRAFFIC (last 3 months):
| URL | Traffic Change | New Keywords | Possible Cause |
|-----|---------------|-------------|----------------|
| {{url}} | +{{delta}} | {{kw_count}} | {{reason}} |

CONTENT THAT RECENTLY LOST TRAFFIC:
| URL | Traffic Change | Keywords Lost | Possible Cause |
|-----|---------------|-------------- |----------------|
| {{url}} | -{{delta}} | {{kw_count}} | {{reason}} |

CONTENT FRESHNESS:
| Age | # Pages | Avg Traffic | Performance |
|-----|---------|------------|-------------|
| <3 months | {{n}} | {{avg}} | {{trend}} |
| 3-6 months | {{n}} | {{avg}} | {{trend}} |
| 6-12 months | {{n}} | {{avg}} | {{trend}} |
| 1-2 years | {{n}} | {{avg}} | {{trend}} |
| 2+ years | {{n}} | {{avg}} | {{trend}} |
```

### Backlink Analysis for Content

```
COMPETITOR CONTENT BACKLINK ANALYSIS
Competitor: {{competitor_name}}

MOST-LINKED CONTENT:
| URL | Referring Domains | Backlinks | Content Type | Topic |
|-----|------------------|-----------|-------------|-------|
| {{url}} | {{rd}} | {{bl}} | {{type}} | {{topic}} |
| {{url}} | {{rd}} | {{bl}} | {{type}} | {{topic}} |
| {{url}} | {{rd}} | {{bl}} | {{type}} | {{topic}} |
| {{url}} | {{rd}} | {{bl}} | {{type}} | {{topic}} |
| {{url}} | {{rd}} | {{bl}} | {{type}} | {{topic}} |

LINK-EARNING CONTENT PATTERNS:
| Pattern | Frequency | Example |
|---------|-----------|---------|
| Original research/data | {{pct}}% of top linked | {{url}} |
| How-to guides | {{pct}}% | {{url}} |
| Industry reports | {{pct}}% | {{url}} |
| Free tools | {{pct}}% | {{url}} |
| Infographics | {{pct}}% | {{url}} |
| Expert roundups | {{pct}}% | {{url}} |

LINK-BUILDING INSIGHT:
Content type most likely to earn links: {{type}}
Average referring domains for top content: {{avg_rd}}
Domains linking to them that you could also target: {{count}}
```

### Social Engagement Tracking

```
COMPETITOR SOCIAL CONTENT PERFORMANCE
Period: {{period}}

ENGAGEMENT BY PLATFORM:
| Platform | Followers | Posts/Week | Avg Engagement | Top Content Type |
|----------|----------|-----------|---------------|-----------------|
| LinkedIn | {{count}} | {{n}} | {{avg}} | {{type}} |
| Twitter/X | {{count}} | {{n}} | {{avg}} | {{type}} |
| Facebook | {{count}} | {{n}} | {{avg}} | {{type}} |
| Instagram | {{count}} | {{n}} | {{avg}} | {{type}} |
| YouTube | {{count}} | {{n}} | {{avg_views}} | {{type}} |

MOST SHARED CONTENT (last 90 days):
| Content | Platform | Shares/Engagement | Topic | Format |
|---------|----------|-------------------|-------|--------|
| {{title}} | {{platform}} | {{count}} | {{topic}} | {{format}} |
| {{title}} | {{platform}} | {{count}} | {{topic}} | {{format}} |
| {{title}} | {{platform}} | {{count}} | {{topic}} | {{format}} |

ENGAGEMENT PATTERNS:
- Best posting day: {{day}}
- Best posting time: {{time}}
- Highest-engagement format: {{format}}
- Topics that resonate most: {{topics}}
```

### SERP Overlap Analysis

```
SERP OVERLAP ANALYSIS
Your Domain: {{your_domain}}
Competitors: {{comp_1}}, {{comp_2}}, {{comp_3}}

OVERLAP SUMMARY:
| Competitor | Shared Keywords | Their Unique | Your Unique | Overlap % |
|-----------|----------------|-------------|-------------|-----------|
| {{comp1}} | {{shared}} | {{theirs}} | {{yours}} | {{pct}}% |
| {{comp2}} | {{shared}} | {{theirs}} | {{yours}} | {{pct}}% |
| {{comp3}} | {{shared}} | {{theirs}} | {{yours}} | {{pct}}% |

HEAD-TO-HEAD RANKING COMPARISON:
| Keyword | Volume | You | {{comp1}} | {{comp2}} | {{comp3}} | Leader |
|---------|--------|-----|----------|----------|----------|--------|
| {{kw}} | {{vol}} | #{{r}} | #{{r}} | #{{r}} | #{{r}} | {{who}} |
| {{kw}} | {{vol}} | #{{r}} | #{{r}} | #{{r}} | #{{r}} | {{who}} |
| {{kw}} | {{vol}} | #{{r}} | #{{r}} | #{{r}} | #{{r}} | {{who}} |

FEATURED SNIPPET OWNERSHIP:
| Keyword | Current Owner | Snippet Type | Opportunity |
|---------|-------------|-------------|-------------|
| {{kw}} | {{domain}} | {{paragraph/list/table}} | {{action}} |
```

### Actionable Recommendations Template

```
COMPETITOR CONTENT ANALYSIS — RECOMMENDATIONS
Date: {{date}}
Analyzed: {{competitors_list}}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

QUICK WINS (implement within 2 weeks):
| # | Opportunity | Source | Est. Traffic Potential | Effort |
|---|------------|--------|----------------------|--------|
| 1 | {{opportunity}} | {{competitor}} | {{traffic}} | Low |
| 2 | {{opportunity}} | {{competitor}} | {{traffic}} | Low |
| 3 | {{opportunity}} | {{traffic}} | {{traffic}} | Low |

STRATEGIC PRIORITIES (1-3 months):
| # | Opportunity | Rationale | Est. Impact | Resources |
|---|------------|-----------|-------------|-----------|
| 1 | {{opportunity}} | {{why}} | {{impact}} | {{resources}} |
| 2 | {{opportunity}} | {{why}} | {{impact}} | {{resources}} |
| 3 | {{opportunity}} | {{why}} | {{impact}} | {{resources}} |

CONTENT TO CREATE:
| Topic | Target Keyword | Volume | Competitor Weakness | Your Angle |
|-------|---------------|--------|-------------------|-----------|
| {{topic}} | {{kw}} | {{vol}} | {{weakness}} | {{angle}} |

CONTENT TO UPDATE:
| Your Page | Current Traffic | Competitor Page | Their Traffic | Update Plan |
|-----------|----------------|----------------|-------------|------------|
| {{url}} | {{traffic}} | {{comp_url}} | {{traffic}} | {{plan}} |

FORMATS TO ADOPT:
| Format | Competitor Using It | Their Results | Your Plan |
|--------|-------------------|--------------|-----------|
| {{format}} | {{competitor}} | {{result}} | {{plan}} |

DEFEND YOUR ADVANTAGES:
| Your Top Content | Current Rank | Competitor Approaching | Action |
|-----------------|-------------|----------------------|--------|
| {{url}} | #{{rank}} | {{competitor}} at #{{rank}} | {{action}} |
```

## Scripts & Tools

**analyze_competitor.py**: Run full competitor content analysis
```bash
python scripts/analyze_competitor.py --competitor example.com --depth full
# Output: Complete audit with inventory, performance, and gaps
```

**topic_gap.py**: Identify topic gaps between you and competitors
```bash
python scripts/topic_gap.py --your-domain you.com --competitors comp1.com,comp2.com
# Output: Keywords and topics they cover that you don't
```

**serp_overlap.py**: Analyze SERP overlap across competitors
```bash
python scripts/serp_overlap.py --domains you.com,comp1.com,comp2.com --keywords keywords.csv
# Output: Head-to-head ranking comparison
```

**content_performance.py**: Estimate competitor content traffic
```bash
python scripts/content_performance.py --domain example.com --top 50
# Output: Top pages by estimated traffic with keyword data
```

## Best Practices

1. **Analyze regularly** - Quarterly deep analysis; monthly top-page monitoring
2. **Focus on 3-5 competitors** - Too many dilutes insights; too few misses patterns
3. **Look at what works, not just what exists** - Volume without performance is noise
4. **Identify patterns, not just pages** - What content types and formats earn results?
5. **Gap analysis is bidirectional** - Protect your advantages, not just fill their gaps
6. **Study their link-earning content** - Replicate the formats that attract backlinks
7. **Check freshness** - Old content they rank for is vulnerable to a fresher, better piece
8. **Monitor new content** - Set alerts for competitor publishing to stay current
9. **Translate insights to action** - Every finding should map to a content calendar entry
10. **Benchmark honestly** - Acknowledge where competitors do better and learn from it

## Related Skills

- SEO auditing: `seo-audit-reporter`
- Content planning: `content-calendar`
- Keyword research: `keyword-research`
- Content optimization: `content-optimizer`
