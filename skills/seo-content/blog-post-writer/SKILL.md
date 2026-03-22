---
name: blog-post-writer
description: Creates engaging, SEO-optimized blog posts and long-form content. Use when the user mentions "write blog post," "blog article," "content creation," "blog outline," "content brief," "how-to article," "listicle," "pillar content," or "SEO blog."
metadata:
  version: 1.1.0
  category: seo-content
---

# Blog Post Writer

Create engaging, SEO-optimized blog posts that attract readers, provide value, and drive business results.

## Quick Start

1. **Create brief**: Run `python scripts/content_brief.py --keyword "topic"`
2. **Choose template**: Use [templates/](templates/) for your post type
3. **Write draft**: Follow the outline from the brief
4. **Check SEO**: Run `python scripts/seo_check.py post.md`
5. **Validate quality**: Run `python scripts/readability.py post.md`

## Blog Writing Workflow

```
Progress:
- [ ] Step 1: Research target keyword and intent
- [ ] Step 2: Create content brief
- [ ] Step 3: Analyze top 3 competitors
- [ ] Step 4: Write outline using template
- [ ] Step 5: Draft content (intro hook, body, conclusion)
- [ ] Step 6: Add internal/external links
- [ ] Step 7: SEO check (title, meta, headers)
- [ ] Step 8: Readability check (grade 6-8)
- [ ] Step 9: Add images with alt text
- [ ] Step 10: Final proofread
```

## Blog Post Types

| Type | Template | Best For |
|------|----------|----------|
| How-To | [templates/how-to.md](templates/how-to.md) | Teaching skills/processes |
| Listicle | [templates/listicle.md](templates/listicle.md) | Curated resources/tips |
| Ultimate Guide | [templates/guide.md](templates/guide.md) | Comprehensive coverage |
| Comparison | [templates/comparison.md](templates/comparison.md) | Buying decisions |
| Case Study | [templates/case-study.md](templates/case-study.md) | Building credibility |

## Core Principles

- **Value first**: Genuinely helpful content ranks better
- **One post, one purpose**: Clear focus beats rambling
- **Scannable structure**: Headers, bullets, short paragraphs
- **Evidence over assertions**: Back up claims with data

## Utility Scripts

**content_brief.py**: Generate content brief from keyword
```bash
python scripts/content_brief.py --keyword "email marketing tips" --competitor-count 3
# Output: Brief with intent, outline, competitor gaps
```

**seo_check.py**: Validate on-page SEO
```bash
python scripts/seo_check.py post.md --keyword "email marketing"
# Output: SEO score, missing elements, suggestions
```

**readability.py**: Check readability grade
```bash
python scripts/readability.py post.md
# Output: Flesch-Kincaid grade, sentence analysis
```

**outline_generator.py**: Generate outline from topic
```bash
python scripts/outline_generator.py --topic "remote work tips" --type listicle
# Output: Structured outline with H2s and H3s
```

## Resources

- **Full writing guide**: [reference.md](reference.md)
- **Post templates**: [templates/](templates/)
- **SEO checklist**: [reference.md](reference.md#seo-checklist)
- **E-E-A-T guidelines**: [reference.md](reference.md#eeat)

## Related Skills

- Keyword research first: `keyword-research`
- Optimize existing posts: `content-optimizer`
- Promote on social: `social-media-repurposer`
