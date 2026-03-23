# Document Summarizer

---
name: document-summarizer
description: Summarize documents, articles, and reports into concise formats. Use when user mentions "summarize this," "TLDR," "key points," "summary of," "brief overview," "main takeaways," or "condense this."
metadata:
  version: 1.0.0
  category: personal-assistance
---

## Purpose

Transform long documents into clear, actionable summaries while preserving key information and insights.

## Quick Reference

### Summary Lengths

| Type | Length | Use When |
|------|--------|----------|
| One-liner | 1 sentence | Tweet, headline |
| Executive | 3-5 bullets | Leadership brief |
| Standard | 1 paragraph | Quick overview |
| Detailed | 1 page | Full understanding |
| Comprehensive | 2-3 pages | Reference document |

### Summary Approaches

| Approach | Best For | Focus |
|----------|----------|-------|
| Extractive | Facts, data | Pull key sentences |
| Abstractive | Narratives | Rewrite concisely |
| Structured | Reports | Headers + bullets |
| Comparative | Multiple docs | Side-by-side |

## Summary Framework (CORE)

| Step | Action |
|------|--------|
| **C**ontext | What is this document? |
| **O**bjective | What's the main point? |
| **R**elevant points | What matters most? |
| **E**xtract actions | What should reader do? |

## Summary Templates

### Executive Summary

```
# [Document Title] - Executive Summary

**Document:** [Title/Source]
**Date:** [Date]
**Type:** [Report/Article/Paper/etc.]

## Bottom Line
[One sentence capturing the main point]

## Key Points
• [Point 1]
• [Point 2]
• [Point 3]

## Implications
[What this means for the reader]

## Recommended Action
[What to do with this information]
```

### Article Summary

```
# Summary: [Article Title]

**Source:** [Publication]
**Author:** [Name]
**Published:** [Date]
**Reading time saved:** [X] min → [Y] min

## Main Argument
[1-2 sentences on the core thesis]

## Key Points
1. **[Point 1]**: [Brief explanation]
2. **[Point 2]**: [Brief explanation]
3. **[Point 3]**: [Brief explanation]

## Evidence/Data
• [Key statistic or fact]
• [Key statistic or fact]

## Author's Conclusion
[What the author concludes]

## My Take
[Optional: Your analysis or relevance]
```

### Report Summary

```
# [Report Title] - Summary

**Prepared by:** [Organization]
**Date:** [Date]
**Pages:** [X] (summarized to [Y])

## Purpose
[Why this report was created]

## Methodology
[How information was gathered - brief]

## Key Findings
1. [Finding 1]
2. [Finding 2]
3. [Finding 3]

## Data Highlights
| Metric | Finding |
|--------|---------|
| [Metric] | [Value] |
| [Metric] | [Value] |

## Recommendations
1. [Recommendation 1]
2. [Recommendation 2]

## Limitations
• [Limitation or caveat]

## Next Steps
[What happens after this report]
```

### Research Paper Summary

```
# [Paper Title] - Research Summary

**Authors:** [Names]
**Published:** [Journal/Conference, Date]
**Field:** [Area of study]

## Research Question
[What problem does this address?]

## Methodology
• Type: [Quantitative/Qualitative/Mixed]
• Sample: [N=X, description]
• Methods: [Brief description]

## Key Findings
1. [Finding 1 with key data]
2. [Finding 2 with key data]
3. [Finding 3 with key data]

## Significance
[Why these findings matter]

## Limitations
[What the study couldn't address]

## Practical Applications
[How to apply these findings]

## Citation
[Full citation]
```

### Book Summary

```
# [Book Title] - Summary

**Author:** [Name]
**Published:** [Year]
**Category:** [Genre/Topic]

## In One Sentence
[The book's main message]

## Core Ideas
### [Idea 1]
[Explanation in 2-3 sentences]

### [Idea 2]
[Explanation in 2-3 sentences]

### [Idea 3]
[Explanation in 2-3 sentences]

## Key Quotes
> "[Quote 1]"

> "[Quote 2]"

## Actionable Takeaways
1. [Takeaway 1]
2. [Takeaway 2]
3. [Takeaway 3]

## Who Should Read This
[Target audience]

## Related Books
• [Related book 1]
• [Related book 2]
```

### Email Thread Summary

```
# Email Thread Summary

**Subject:** [Thread subject]
**Participants:** [Names]
**Timeframe:** [First email date] - [Last email date]
**Emails:** [Number]

## Context
[Why this thread exists]

## Key Points
• [Point 1]
• [Point 2]
• [Point 3]

## Decisions Made
• [Decision 1]
• [Decision 2]

## Open Questions
• [Question still unanswered]

## Action Items
| Action | Owner | Status |
|--------|-------|--------|
| [Action] | [Name] | [Open/Done] |

## Current Status
[Where things stand now]
```

## Summarization Process

### Step 1: Scan

```
Quick scan for:
□ Title and headers
□ Introduction/abstract
□ Conclusion
□ Bold/highlighted text
□ Charts and figures
□ Lists and tables
```

### Step 2: Read

```
Active reading:
□ Identify main thesis
□ Note supporting arguments
□ Capture key data points
□ Mark important quotes
□ Flag unclear sections
```

### Step 3: Synthesize

```
Connect the dots:
□ Group related points
□ Identify themes
□ Note contradictions
□ Find implications
□ Draw conclusions
```

### Step 4: Write

```
Create summary:
□ Lead with main point
□ Support with evidence
□ Use clear structure
□ Cut unnecessary detail
□ Add value/context
```

## Length Guidelines

| Original Length | Summary Target |
|-----------------|----------------|
| <1,000 words | 2-3 sentences |
| 1,000-5,000 words | 1 paragraph |
| 5,000-10,000 words | Half page |
| 10,000-25,000 words | 1 page |
| 25,000+ words | 2-3 pages |

## Best Practices

### Do
- Preserve the author's intent
- Include key data and evidence
- Maintain logical flow
- Use your own words
- Note what's NOT in the summary
- Indicate your interpretations clearly

### Don't
- Add opinions without labeling
- Miss critical nuances
- Over-simplify complex topics
- Include every detail
- Use jargon without explaining
- Plagiarize directly

## Scripts & Tools

| Script | Purpose |
|--------|---------|
| `scripts/document_summarizer.py` | Auto-generate summaries |
| `scripts/key_points_extractor.py` | Extract main points |

## Quality Checklist

```
Before Sharing:
□ Main point is clear
□ Key facts are accurate
□ Nothing critical is missing
□ Structure is logical
□ Length is appropriate
□ Language is clear
□ Source is cited
□ Reader can act on it
```

## Reference

→ See `templates/summary_templates.md` for all formats
→ See `reference.md` for advanced techniques
