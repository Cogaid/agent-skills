# Product Description Writer

---
name: product-description-writer
description: Write compelling product descriptions that drive conversions. Use when user mentions "product description," "product copy," "e-commerce copy," "listing description," "product page," "Amazon listing," or "product features."
metadata:
  version: 1.0.0
  category: seo-content
---

## Purpose

Create product descriptions that inform, persuade, and convert browsers into buyers.

## Quick Reference

### Description Lengths

| Platform | Title | Short Desc | Full Desc |
|----------|-------|------------|-----------|
| E-commerce | 60-80 chars | 150-200 chars | 300-500 words |
| Amazon | 200 chars | 5 bullets | 2000 chars |
| Shopify | 70 chars | 160 chars | Unlimited |
| Etsy | 140 chars | N/A | 1000 chars |

### Conversion Elements

| Element | Purpose | Priority |
|---------|---------|----------|
| Headline | Capture attention | Critical |
| Benefits | Show value | Critical |
| Features | Provide details | High |
| Social proof | Build trust | High |
| CTA | Drive action | High |
| Objections | Remove barriers | Medium |

## Product Description Framework (FAB+E)

### Structure

| Element | Focus | Example |
|---------|-------|---------|
| **F**eatures | What it has | "10-hour battery life" |
| **A**dvantages | Why it matters | "Lasts all day without charging" |
| **B**enefits | How it helps them | "Work worry-free anywhere" |
| **E**motion | How it makes them feel | "Feel confident and untethered" |

## Templates

### Standard E-commerce Description

```
# [Product Name]

[Compelling headline that captures the main benefit]

[Opening paragraph: Paint a picture of the problem or desire, then introduce the product as the solution. 2-3 sentences.]

## Why You'll Love It

✓ **[Benefit 1]** — [Brief explanation]
✓ **[Benefit 2]** — [Brief explanation]
✓ **[Benefit 3]** — [Brief explanation]
✓ **[Benefit 4]** — [Brief explanation]

## What's Included

• [Item 1]
• [Item 2]
• [Item 3]

## Specifications

| Feature | Detail |
|---------|--------|
| [Spec 1] | [Value] |
| [Spec 2] | [Value] |
| [Spec 3] | [Value] |

## Perfect For

[Describe ideal customer or use case]

[Trust element: Warranty, guarantee, or social proof]

[CTA: Clear call to action]
```

### Amazon Listing Format

```
TITLE (200 chars max):
[Brand] [Product Name] - [Key Benefit] - [Key Feature] - [Size/Quantity]

BULLET POINTS (5 bullets):
• 【KEY BENEFIT 1】[Feature that delivers this benefit] - [Why it matters to customer]
• 【KEY BENEFIT 2】[Feature that delivers this benefit] - [Why it matters to customer]
• 【KEY BENEFIT 3】[Feature that delivers this benefit] - [Why it matters to customer]
• 【KEY BENEFIT 4】[Feature that delivers this benefit] - [Why it matters to customer]
• 【SATISFACTION GUARANTEE】[Trust element - warranty, return policy, support]

PRODUCT DESCRIPTION (2000 chars):
[Brand Story - 1-2 sentences]

[Problem/Solution - What problem does this solve?]

[Features + Benefits - Expand on bullet points]

[Social Proof - Reviews, awards, certifications]

[CTA - Why buy now]
```

### Short Description (150-200 chars)

```
[Primary benefit] + [Key feature] + [Target audience]

Examples:
"Stay productive all day with 10-hour battery life. Lightweight design perfect for travelers and remote workers."

"Achieve salon-quality results at home. Professional-grade ingredients for all hair types."
```

### Luxury/Premium Product

```
# [Product Name]

[Evocative headline that conveys prestige]

[Opening: Set the scene, create desire. Focus on craftsmanship, exclusivity, or heritage.]

## The [Brand] Difference

[Explain what makes this product exceptional. Use sensory language and specific details.]

## Crafted For

[Describe the discerning customer this is made for]

## Features

• [Feature 1]: [Elegant description]
• [Feature 2]: [Elegant description]
• [Feature 3]: [Elegant description]

## Materials & Care

[Quality materials and maintenance]

## The Details

[Dimensions, weight, specifications in refined presentation]

[Heritage or story element]

[Subtle CTA]
```

### Technical/B2B Product

```
# [Product Name]

**[Clear value proposition for business]**

## Overview

[2-3 sentences explaining what it is and who it's for]

## Key Capabilities

### [Capability 1]
[Explanation with specific metric or outcome]

### [Capability 2]
[Explanation with specific metric or outcome]

### [Capability 3]
[Explanation with specific metric or outcome]

## Technical Specifications

| Specification | Value |
|---------------|-------|
| [Spec] | [Value] |
| [Spec] | [Value] |

## Integrations

Compatible with: [List]

## Use Cases

• **[Use case 1]**: [Brief description]
• **[Use case 2]**: [Brief description]

## Support & Compliance

[Security, certifications, support options]

[CTA: Demo, trial, contact]
```

## Writing Guidelines

### Power Words by Category

| Category | Words |
|----------|-------|
| Quality | Premium, handcrafted, artisan, precision |
| Value | Free, bonus, exclusive, limited |
| Ease | Simple, effortless, instant, automatic |
| Results | Proven, guaranteed, professional, effective |
| Safety | Secure, protected, certified, trusted |
| Innovation | Revolutionary, breakthrough, cutting-edge |

### Sensory Language

| Sense | Examples |
|-------|----------|
| Visual | Sleek, vibrant, stunning, crystal-clear |
| Tactile | Soft, smooth, lightweight, ergonomic |
| Auditory | Crisp, silent, rich, immersive |
| Olfactory | Fresh, aromatic, clean, natural |
| Gustatory | Rich, smooth, bold, delicate |

### Words to Avoid

| Avoid | Use Instead |
|-------|-------------|
| Very | [More specific adjective] |
| Good | Excellent, superior, outstanding |
| Nice | Elegant, refined, attractive |
| Thing | [Specific noun] |
| Stuff | Materials, components, features |
| Really | [Remove or use specific qualifier] |

## SEO Optimization

### Keyword Placement

| Location | Priority | Example |
|----------|----------|---------|
| Title | Critical | Primary keyword first |
| First 100 words | High | Natural inclusion |
| Subheadings | Medium | Variations/related |
| Bullet points | Medium | Features + keywords |
| Image alt text | High | Descriptive + keyword |

### Schema Markup

```json
{
  "@type": "Product",
  "name": "[Product Name]",
  "description": "[Short description]",
  "brand": "[Brand]",
  "sku": "[SKU]",
  "offers": {
    "@type": "Offer",
    "price": "[Price]",
    "priceCurrency": "USD"
  }
}
```

## Quality Checklist

```
Before Publishing:
□ Benefits clear and compelling
□ Features support benefits
□ Keywords naturally included
□ Correct length for platform
□ Mobile-friendly formatting
□ No spelling/grammar errors
□ CTA is clear
□ Images referenced match
□ Pricing/availability correct
□ Brand voice consistent
```

## Scripts & Tools

| Script | Purpose |
|--------|---------|
| `scripts/description_generator.py` | Generate product descriptions |
| `scripts/seo_optimizer.py` | Optimize for search |

## Reference

→ See `templates/product_templates.md` for all formats
→ See `reference.md` for platform-specific guidelines
