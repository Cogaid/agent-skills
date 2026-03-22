---
name: social-media-repurposer
description: Transforms content into engaging social media posts for multiple platforms. Use when the user mentions "repurpose content," "social media posts," "turn blog into posts," "LinkedIn post," "Twitter thread," "Instagram carousel," "social content," or "content distribution."
metadata:
  version: 1.1.0
  category: seo-content
---

# Social Media Repurposer

Transform existing content into engaging social media posts optimized for each platform.

## Quick Start

1. **Extract elements**: Run `python scripts/extract_content.py blog-post.md`
2. **Choose platform**: Use [templates/](templates/) for platform-specific formats
3. **Generate posts**: Run `python scripts/generate_social.py --source blog.md --platform twitter`
4. **Schedule**: Use [templates/calendar.md](templates/calendar.md)

## Repurposing Workflow

```
Progress:
- [ ] Step 1: Read source content thoroughly
- [ ] Step 2: Extract key elements (insights, quotes, stats, tips)
- [ ] Step 3: Map elements to platforms
- [ ] Step 4: Write platform-native versions
- [ ] Step 5: Create visuals if needed (carousels, graphics)
- [ ] Step 6: Schedule posts
- [ ] Step 7: Track performance
```

## One Piece → Many Posts

From one blog post, create:
- **Twitter**: Thread + 3-5 single tweets
- **LinkedIn**: Story post + carousel
- **Instagram**: Carousel + 3 quote graphics
- **TikTok/Reels**: 2-3 short video scripts

## Platform Quick Reference

| Platform | Length | Best Format | Frequency |
|----------|--------|-------------|-----------|
| Twitter/X | 280 chars | Threads, single insights | 3-5x/day |
| LinkedIn | 3000 chars | Story posts, carousels | 1-2x/day |
| Instagram | 2200 chars | Carousels, Reels | 1-2x/day |
| TikTok | 150 chars | 30-60s videos | 1-3x/day |

## Utility Scripts

**extract_content.py**: Extract repurposable elements
```bash
python scripts/extract_content.py blog-post.md
# Output: Stats, quotes, tips, key points
```

**generate_social.py**: Generate platform-specific posts
```bash
python scripts/generate_social.py --source blog.md --platform linkedin
# Output: Platform-formatted post drafts
```

**thread_builder.py**: Build Twitter threads
```bash
python scripts/thread_builder.py --source blog.md --max-tweets 10
# Output: Thread with hook and CTA
```

## Platform Templates

| Platform | Template |
|----------|----------|
| Twitter Thread | [templates/twitter.md](templates/twitter.md) |
| LinkedIn Post | [templates/linkedin.md](templates/linkedin.md) |
| Instagram Carousel | [templates/instagram.md](templates/instagram.md) |
| Short Video | [templates/video.md](templates/video.md) |

## Resources

- **Full repurposing guide**: [reference.md](reference.md)
- **Platform templates**: [templates/](templates/)
- **Content calendar**: [templates/calendar.md](templates/calendar.md)
- **Performance tracking**: [templates/tracking.md](templates/tracking.md)

## Related Skills

- Create source content: `blog-post-writer`
- Keyword research: `keyword-research`
- Optimize source content: `content-optimizer`
