# Product Description Writer -- Reference Guide

Detailed reference documentation for writing product descriptions that convert across platforms.

## FAB+E Framework Deep Dive

### Features

Features are the factual, objective attributes of the product -- what it has, what it does, what it's made of.

**How to identify features:**
- Technical specifications (dimensions, weight, capacity, speed)
- Materials and construction (100% cotton, aircraft-grade aluminum)
- Functionality (syncs with 50+ apps, handles 10K concurrent users)
- Included components (comes with charger, carrying case, 3 adapters)

**Common mistake:** Listing features without connecting them to benefits. "10-hour battery" is a feature. "Work all day without hunting for an outlet" is the benefit.

### Advantages

Advantages explain why a feature matters in practical terms -- the bridge between feature and benefit.

**Pattern:** [Feature] + "which means" + [Advantage]

Examples:
- "Weighs only 2.1 lbs" -> which means -> "lighter than any competitor in its class"
- "256-bit AES encryption" -> which means -> "the same security banks use"
- "Ships in 24 hours" -> which means -> "you'll have it by Wednesday"

### Benefits

Benefits answer the customer's core question: "What's in it for me?" They focus on outcomes and improvements to their life.

**Benefit categories:**
- **Time savings:** Get back hours in your week
- **Money savings:** Reduce costs, increase value
- **Ease/convenience:** Simpler, faster, less friction
- **Status/identity:** Look better, feel successful, signal taste
- **Peace of mind:** Reduce worry, feel protected, gain confidence
- **Performance:** Do more, do better, achieve goals

**Writing tip:** For each feature, ask "So what?" repeatedly until you reach the emotional payoff. That's the benefit.

### Emotion

Emotion is the ultimate driver of purchase decisions. Even B2B buyers are influenced by how a product makes them feel.

**Emotional triggers by product category:**

| Category | Primary Emotion | Copy Approach |
|----------|----------------|---------------|
| Luxury goods | Aspiration, status | Evocative, sensory, exclusive language |
| Health/wellness | Hope, confidence | Transformation stories, before/after |
| Technology | Empowerment, control | Capability language, future-pacing |
| Safety/security | Peace of mind | Risk reduction, protection framing |
| Productivity tools | Relief, competence | Time-back framing, mastery language |
| Fashion | Identity, belonging | Self-expression, social validation |
| Food/beverage | Pleasure, comfort | Sensory language, indulgence framing |
| Children's products | Love, protection | Safety assurance, developmental benefits |

## Platform-Specific Guidelines

### Amazon

**Title formula:** [Brand] + [Product Name] + [Key Feature] + [Use Case] + [Size/Quantity/Color]

**Title example:** "ProGrip Ergonomic Wireless Mouse - Silent Click, 3 DPI Levels - for Office & Gaming - Black"

**Bullet points (5 required):**
- Start each with a capitalized benefit phrase in brackets
- Lead with the most important benefit
- Include relevant keywords naturally
- Address the #1 customer objection in bullet 5
- Use 200-250 characters per bullet (max 500)

**A+ Content (Enhanced Brand Content):**
- Use comparison charts to show advantages
- Include lifestyle images with text overlays
- Tell your brand story
- Address FAQs visually
- Use all available modules

**Backend keywords (250 bytes):**
- No commas needed (space-separated)
- No brand names (yours or competitors)
- No ASINs
- Include misspellings, synonyms, abbreviations
- No repetition of words already in title/bullets

### Shopify / Direct E-commerce

**Above the fold (visible without scrolling):**
- Product name (H1 with primary keyword)
- Price and any sale/comparison pricing
- 1-2 sentence value proposition
- Star rating and review count
- Primary CTA button
- Key trust signals (free shipping, returns, guarantee)

**Below the fold:**
- Detailed description with benefit-led copy
- Specifications table
- Size/compatibility guide
- Customer reviews
- FAQ section
- Related/complementary products

**Mobile optimization:**
- Short paragraphs (2-3 sentences max)
- Bullet points for scannability
- Expandable/accordion sections for details
- Touch-friendly CTA buttons (min 44x44px)
- Images before text

### Etsy

**Title (140 chars):** Front-load with search terms. Include material, color, use case.
- Example: "Handmade Ceramic Coffee Mug - Speckled Blue Glaze - 12oz - Gift for Coffee Lovers - Pottery Mug"

**Description approach:**
- Open with the experience of using the product
- Emphasize handmade/unique/custom aspects
- Include all materials, dimensions, care instructions
- Reference the maker's story/process
- Use natural, warm, personal tone

**Tags (13 max):**
- Multi-word phrases perform better than single words
- Mix broad and specific: "ceramic mug" + "blue pottery gift"
- Include seasonal terms when relevant

### B2B / SaaS Product Pages

**Structure:**
1. Hero: Headline (benefit) + subhead (how) + CTA + social proof
2. Pain points: 3 problems the audience recognizes
3. Solution overview: how your product addresses each pain
4. Feature deep-dive: 3-5 key capabilities with screenshots
5. Social proof: logos, testimonials, case study snippets
6. Pricing or CTA: clear next step
7. FAQ: address objections

**Tone:** Professional but not stuffy. Confident but not arrogant. Specific, not vague.

## SEO for Product Descriptions

### Keyword Strategy

**Primary keyword:** The main term customers search for this product type.
Place in: title, H1, first paragraph, URL slug, alt text.

**Secondary keywords:** Variations, long-tail, and related terms.
Place in: subheadings, bullet points, description body.

**LSI keywords:** Semantically related terms that signal topical relevance.
Place in: naturally throughout the description.

### Schema Markup Reference

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Product Name",
  "image": "https://example.com/image.jpg",
  "description": "Short product description",
  "brand": {
    "@type": "Brand",
    "name": "Brand Name"
  },
  "sku": "SKU123",
  "mpn": "MPN123",
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/product",
    "priceCurrency": "USD",
    "price": "49.99",
    "availability": "https://schema.org/InStock",
    "seller": {
      "@type": "Organization",
      "name": "Store Name"
    }
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.7",
    "reviewCount": "234"
  }
}
```

### Image Alt Text

**Formula:** [Product Type] + [Key Attribute] + [Context/Use]

**Examples:**
- "Ergonomic wireless mouse on office desk with laptop"
- "Blue ceramic coffee mug with speckled glaze held in hands"
- "Dashboard screenshot showing analytics overview with charts"

## Conversion Optimization

### Trust Signals to Include

| Signal | Where to Place | Impact |
|--------|---------------|--------|
| Star rating + review count | Near product name | High |
| Free shipping threshold | Near price | High |
| Return policy | Near CTA | High |
| Security badges | Near payment | Medium |
| Money-back guarantee | Near CTA | High |
| Social proof (users/customers) | Below hero | Medium |
| Certifications/awards | Description body | Medium |
| Real customer photos | Reviews section | High |

### Price Presentation

- **Anchoring:** Show original price crossed out next to sale price
- **Per-unit pricing:** "$2.50/day" feels smaller than "$75/month"
- **Value framing:** "Less than your daily coffee"
- **Bundle savings:** "Save 20% with the bundle"
- **Free trial:** Remove price objection entirely

### CTA Best Practices

| Goal | CTA Text | Color | Placement |
|------|----------|-------|-----------|
| Purchase | "Add to Cart" / "Buy Now" | High-contrast (orange, green) | Above fold + sticky |
| Free trial | "Start Free Trial" | Primary brand color | Hero section |
| Learn more | "See How It Works" | Secondary/outline | Below features |
| Custom/quote | "Get Custom Quote" | Primary | After configuration |

## Writing by Product Category

### Fashion / Apparel

- Lead with the occasion or look, not the fabric
- Include fit details (true to size, runs large, size guide link)
- Mention styling suggestions
- Use aspirational but accessible language
- Reference the model's measurements for fit context

### Electronics / Tech

- Lead with what it enables, not specs
- Include compatibility information prominently
- Address setup/learning curve
- Compare to previous version or competing specs
- Include "what's in the box" list

### Food / Beverage

- Use sensory language heavily (taste, aroma, texture)
- Include sourcing/origin story
- Allergen and dietary info must be prominent
- Suggest pairing or serving ideas
- Mention freshness and packaging

### Home / Furniture

- Include dimensions prominently
- Describe the material and finish in sensory terms
- Mention assembly requirements
- Reference the room/style it fits
- Weight and shipping details matter
