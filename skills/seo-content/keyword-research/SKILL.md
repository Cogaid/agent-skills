---
name: keyword-research
description: Researches and analyzes keywords for SEO and content strategy. Use when the user mentions "keyword research," "find keywords," "search terms," "what to rank for," "keyword analysis," "search volume," "keyword difficulty," "long-tail keywords," or "keyword strategy."
metadata:
  version: 1.1.0
  category: seo-content
---

# Keyword Research

Research and analyze keywords to find the best opportunities for ranking and driving qualified traffic.

## Quick Start

1. **Generate seeds**: Run `python scripts/seed_keywords.py --topic "your topic"`
2. **Expand keywords**: Run `python scripts/expand_keywords.py --seed "seed keyword"`
3. **Analyze intent**: Run `python scripts/analyze_intent.py keywords.json`
4. **Prioritize**: Run `python scripts/prioritize_keywords.py keywords.json`
5. **Build clusters**: Use [templates/cluster.md](templates/cluster.md)

## Keyword Research Workflow

```
Progress:
- [ ] Step 1: Define business goals and target audience
- [ ] Step 2: Generate seed keywords (brainstorm, competitors)
- [ ] Step 3: Expand with modifiers and variations
- [ ] Step 4: Collect data (volume, difficulty, CPC)
- [ ] Step 5: Analyze search intent for each
- [ ] Step 6: Group into topical clusters
- [ ] Step 7: Prioritize by opportunity score
- [ ] Step 8: Map keywords to content types
- [ ] Step 9: Create content calendar
```

## Core Principles

- **Intent over volume**: 100 high-intent searches beat 10,000 irrelevant
- **Competition matters**: Ranking potential is relative to your authority
- **Long-tail wins early**: Specific keywords are easier to rank
- **Cluster thinking**: Build topical authority through related content

## Search Intent Types

| Intent | Signals | Content Type |
|--------|---------|--------------|
| **Informational** | "what is," "how to," "why" | Blog posts, guides |
| **Navigational** | Brand names, specific pages | Home page, product pages |
| **Commercial** | "best," "vs," "review" | Comparisons, reviews |
| **Transactional** | "buy," "discount," "near me" | Product pages, landing pages |

## Utility Scripts

**seed_keywords.py**: Generate seed keywords from topic
```bash
python scripts/seed_keywords.py --topic "email marketing"
# Output: Categorized seed keywords
```

**expand_keywords.py**: Expand with modifiers
```bash
python scripts/expand_keywords.py --seed "email marketing" --modifiers all
# Output: Long-tail variations
```

**analyze_intent.py**: Classify keywords by intent
```bash
python scripts/analyze_intent.py keywords.json
# Output: Keywords with intent classification
```

**prioritize_keywords.py**: Score and rank keywords
```bash
python scripts/prioritize_keywords.py keywords.json --weights business:2,volume:1
# Output: Prioritized keyword list
```

## Long-Tail Strategy

| Short-Tail | Long-Tail |
|------------|-----------|
| "running shoes" | "best running shoes for flat feet women" |
| High volume | Lower volume |
| High competition | Lower competition |
| Vague intent | Clear intent |
| Hard to rank | Easier to rank |

## Resources

- **Full research guide**: [reference.md](reference.md)
- **Seed keyword template**: [templates/seeds.md](templates/seeds.md)
- **Cluster template**: [templates/cluster.md](templates/cluster.md)
- **Competitor analysis**: [templates/competitor.md](templates/competitor.md)

## Related Skills

- Writing content from keywords: `blog-post-writer`
- Optimizing existing content: `content-optimizer`
- Promoting keyword-targeted content: `social-media-repurposer`
