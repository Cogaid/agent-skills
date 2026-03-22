---
name: knowledge-base-writer
description: Creates and updates help documentation, FAQs, and knowledge base articles. Use when the user mentions "write help article," "create documentation," "FAQ," "help center," "knowledge base," "support article," "how-to guide," "troubleshooting guide," "document this feature," "reduce tickets," or "self-service content." Also use for converting support tickets into documentation.
metadata:
  version: 1.1.0
  category: customer-support
---

# Knowledge Base Writer

Create clear, scannable help documentation that reduces support tickets.

## Quick Start

1. **Determine article type**: How-To, Troubleshooting, FAQ, or Reference
2. **Check readability**: Run `python scripts/check_readability.py`
3. **Optimize for search**: Run `python scripts/seo_check.py`
4. **Use template**: See [templates/](templates/) for article templates

## Article Workflow

```
KB Article Progress:
- [ ] Step 1: Identify article type and audience
- [ ] Step 2: Choose template from templates/
- [ ] Step 3: Write draft following style guide
- [ ] Step 4: Run readability check (target: grade 8 or below)
- [ ] Step 5: Run SEO check for discoverability
- [ ] Step 6: Add to appropriate category
- [ ] Step 7: Link from related articles
```

## Article Types

| Type | When to Use | Template |
|------|-------------|----------|
| **How-To** | Step-by-step tasks | [templates/howto.md](templates/howto.md) |
| **Troubleshooting** | Fixing specific problems | [templates/troubleshooting.md](templates/troubleshooting.md) |
| **FAQ** | Common questions | [templates/faq.md](templates/faq.md) |
| **Reference** | Specifications, settings | [templates/reference.md](templates/reference.md) |

## Writing Guidelines (Quick)

- **Headlines**: Use exact search terms customers use
- **Structure**: One idea per paragraph, 2-3 sentences max
- **Steps**: Number them, start with verb, one action per step
- **Tone**: Second person ("you"), active voice, confident

**Full style guide**: See [reference.md](reference.md)

## Utility Scripts

**check_readability.py**: Analyze text readability
```bash
python scripts/check_readability.py article.md
# Output: Grade level, sentence length, suggestions
```

**seo_check.py**: Check SEO optimization
```bash
python scripts/seo_check.py article.md --keyword "reset password"
# Output: Keyword placement, title optimization, suggestions
```

**convert_ticket.py**: Convert support ticket to article draft
```bash
python scripts/convert_ticket.py ticket.txt --type howto
# Output: Article draft based on ticket content
```

## Quality Checklist

Before publishing:
- [ ] Title matches search terms (< 60 chars)
- [ ] Readability score: grade 8 or below
- [ ] Steps tested and accurate
- [ ] Screenshots current (if applicable)
- [ ] Internal links added
- [ ] Category and tags assigned

## Resources

- **Style guide**: [reference.md](reference.md)
- **Article templates**: [templates/](templates/)
- **SEO guidelines**: [reference.md](reference.md#seo)

## Related Skills

- Ticket categorization: `ticket-triage`
- Feedback analysis: `customer-feedback-analyzer`
- Escalation handling: `escalation-handler`
