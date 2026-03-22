---
name: content-optimizer
description: Improves existing content for better search rankings and engagement. Use when the user mentions "optimize content," "improve rankings," "content not ranking," "refresh content," "update blog post," "SEO optimization," "on-page SEO," "content audit," or "improve existing content."
metadata:
  version: 1.1.0
  category: seo-content
---

# Content Optimizer

Improve existing content to rank higher, engage readers better, and drive more conversions.

## Quick Start

1. **Diagnose**: Run `python scripts/content_audit.py page.md --keyword "target"`
2. **Analyze competitors**: Use [templates/competitor.md](templates/competitor.md)
3. **Identify gaps**: Run `python scripts/gap_analysis.py page.md competitor.md`
4. **Apply fixes**: Follow [reference.md](reference.md#checklist)
5. **Measure**: Track changes after 2-4 weeks

## Optimization Workflow

```
Progress:
- [ ] Step 1: Diagnose the problem (traffic, rank, CTR, bounce)
- [ ] Step 2: Analyze top 3 competitors
- [ ] Step 3: Identify content gaps
- [ ] Step 4: Optimize title and meta description
- [ ] Step 5: Improve header structure (H1, H2, H3)
- [ ] Step 6: Add missing sections/topics
- [ ] Step 7: Improve internal linking
- [ ] Step 8: Add fresh data/examples
- [ ] Step 9: Check readability (grade 6-8)
- [ ] Step 10: Update publish date
```

## Common Problems & Fixes

| Problem | Likely Cause | Fix |
|---------|--------------|-----|
| Not ranking | Intent mismatch, thin content | Rewrite for intent, add depth |
| Ranking but low CTR | Weak title/meta | Improve title, add power words |
| High bounce rate | Poor UX, wrong intent | Improve structure, match intent |
| No conversions | Weak CTA, wrong audience | Add CTAs, improve targeting |

## Utility Scripts

**content_audit.py**: Full content analysis
```bash
python scripts/content_audit.py page.md --keyword "target keyword"
# Output: Scores for SEO, readability, structure
```

**gap_analysis.py**: Compare against competitors
```bash
python scripts/gap_analysis.py your-page.md competitor-page.md
# Output: Missing topics, word count gap
```

**freshness_check.py**: Check for outdated content
```bash
python scripts/freshness_check.py page.md
# Output: Outdated references, old dates, broken links
```

**ctr_optimizer.py**: Generate title/meta variations
```bash
python scripts/ctr_optimizer.py --current-title "Your Title" --keyword "target"
# Output: Alternative titles with CTR boosters
```

## Quick Optimization Checklist

### Title Tag
- [ ] 50-60 characters
- [ ] Keyword front-loaded
- [ ] Compelling (numbers, brackets, power words)

### Meta Description
- [ ] 150-160 characters
- [ ] Contains keyword
- [ ] Has clear value proposition
- [ ] Includes call-to-action

### Headers
- [ ] One H1 only (with keyword)
- [ ] H2s for main sections (keyword in 1+)
- [ ] Logical hierarchy
- [ ] Scannable

## Resources

- **Full optimization guide**: [reference.md](reference.md)
- **Audit template**: [templates/audit.md](templates/audit.md)
- **Competitor analysis**: [templates/competitor.md](templates/competitor.md)
- **Before/after tracking**: [templates/tracking.md](templates/tracking.md)

## Related Skills

- Create new content: `blog-post-writer`
- Keyword research: `keyword-research`
- Promote optimized content: `social-media-repurposer`
