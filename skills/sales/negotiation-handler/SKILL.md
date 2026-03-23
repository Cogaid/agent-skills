# Negotiation Handler

---
name: negotiation-handler
description: Navigate sales negotiations to reach mutually beneficial outcomes. Use when user mentions "negotiation," "pricing discussion," "discount request," "contract terms," "deal structure," "closing price," or "final offer."
metadata:
  version: 1.0.0
  category: sales
---

## Purpose

Guide sales negotiations strategically to close deals while protecting value and building long-term relationships.

## Quick Reference

### Negotiation Principles

| Principle | Description |
|-----------|-------------|
| Prepare | Know your BATNA, their BATNA, and walk-away point |
| Listen | Understand their real needs, not just positions |
| Create Value | Expand the pie before dividing it |
| Trade | Never give without getting something in return |
| Document | Confirm everything in writing |

### Common Negotiation Requests

| Request | Default Response | Trade For |
|---------|------------------|-----------|
| Discount | Multi-year commitment | Contract length |
| Payment terms | Net 30 standard | Larger deal size |
| Free months | Added services | Case study rights |
| Custom features | Roadmap consideration | Reference customer |
| Rush implementation | Priority fee | Larger contract |

## Negotiation Framework (PREP)

### P - Prepare

```
Know Before Negotiating:
□ Your walk-away point (minimum acceptable)
□ Your target outcome (ideal)
□ Your BATNA (best alternative)
□ Their likely BATNA
□ Their budget constraints
□ Their timeline pressure
□ Decision-maker dynamics
□ Competitive alternatives they have
□ Value you've demonstrated
□ Items you can trade
```

### R - Respond Strategically

```
When They Ask for Discount:
1. Pause - Don't react immediately
2. Acknowledge - "I understand budget matters"
3. Explore - "Help me understand the constraint"
4. Reframe - Focus on value, not price
5. Trade - "If I could do X, would you do Y?"
```

### E - Exchange Value

```
Trading Framework:
"If you [their concession], I can [your concession]"

Examples:
- "If you sign a 2-year contract, I can offer 15% off"
- "If you pay annually upfront, I can include onboarding"
- "If you commit by Friday, I can lock in current pricing"
```

### P - Protect the Deal

```
Closing Tactics:
□ Summarize agreements
□ Address remaining concerns
□ Create urgency (real, not fake)
□ Get commitment in writing
□ Set next steps
□ Remove risk with guarantees
```

## Discount Guidelines

### Discount Authority

| Discount Level | Approval Needed | Typical Justification |
|----------------|-----------------|----------------------|
| 0-10% | Sales rep | Multi-year, volume |
| 11-20% | Sales manager | Strategic account |
| 21-30% | VP Sales | Enterprise, competitive |
| 30%+ | C-level | Exceptional cases |

### What to Trade for Discounts

| Discount | Trade Requirement |
|----------|-------------------|
| 5-10% | Annual prepayment |
| 10-15% | 2-year commitment |
| 15-20% | 3-year commitment |
| 20%+ | Strategic value (logo, reference, expansion) |

### Alternative to Discounts

Instead of lowering price, offer:
- Extended trial period
- Free onboarding/training
- Additional users/seats
- Premium support tier
- Early access to features
- Quarterly business reviews
- Dedicated success manager

## Response Templates

### Handling Discount Requests

**Initial Response:**
```
"I appreciate you being upfront about budget. Let me understand better -
is this about the total investment, or the timing of payments?"

[Listen to response]

"Got it. Here's what I can do: [trade-based offer]"
```

**When Pushed Further:**
```
"I wish I could go lower, but at [price], we're already at a point where
I need to ensure we can deliver the value you're expecting.

What I CAN do is [alternative value add].

Would that work?"
```

**Final Offer:**
```
"Let me be transparent - [X] is the best I can do on price.

What I can add is [value add] which typically costs [value].

This is genuinely my best offer. Can we move forward on this?"
```

### Handling "Competitor is Cheaper"

```
"Thanks for sharing that. A few questions:

1. Are they offering the same scope?
2. What's included in their implementation?
3. How does their support compare?

[Pause for response]

Our customers often find that [specific differentiator] saves them
[time/money] compared to alternatives.

Can I share a case study from [similar company]?"
```

### Handling "Need to Think About It"

```
"Of course - this is an important decision.

To help you think it through:
- What questions are still unanswered?
- What would make this an easy yes?
- Is there anyone else who should be involved?

[Pause]

Would it help if I [offered specific action]?"
```

### Handling "Budget is Set"

```
"I understand budgets are fixed. Let me ask:

- Is this budget for this quarter or fiscal year?
- Is there flexibility if we phase the implementation?
- Could we start smaller and expand?

[Based on response]

Here's what I'd suggest: [phased approach / smaller initial scope]"
```

## Negotiation Tactics Reference

### Tactics They Might Use

| Tactic | How to Recognize | How to Counter |
|--------|------------------|----------------|
| Anchoring | Extreme first offer | Re-anchor with data |
| Good cop/bad cop | One supportive, one hostile | Address both directly |
| Silence | Uncomfortable pause | Wait them out |
| Deadline pressure | "Decide by Friday" | Test if real |
| Limited authority | "I need to check" | Get commitment anyway |
| Nibbling | Last-minute asks | "Let's finalize everything" |
| Walk away | Threaten to leave | Call bluff or let go |

### Tactics You Can Use

| Tactic | When to Use | Example |
|--------|-------------|---------|
| Bracket | Set the range | "Typically $X-$Y depending on..." |
| Trial balloon | Test positions | "What if we..." |
| Split the difference | Near close | "Meet in the middle?" |
| Summarize | Gain momentum | "So we've agreed on..." |
| Future promise | Maintain relationship | "If you grow to X, we'll revisit" |
| Scarcity | Create urgency | "Pricing changes next month" |

## Decision Tree

```
Discount Request
    │
    ├─→ Budget Issue
    │       │
    │       ├─→ Real constraint → Offer payment terms, phased approach
    │       └─→ Negotiating tactic → Stand firm, emphasize value
    │
    ├─→ Competitive Pressure
    │       │
    │       ├─→ Real alternative → Differentiate, offer strategic discount
    │       └─→ Bluffing → Call bluff gently, maintain position
    │
    ├─→ Internal Politics
    │       │
    │       ├─→ Need to show win → Give small visible concession
    │       └─→ Multiple stakeholders → Understand each need
    │
    └─→ Standard Ask
            │
            ├─→ High value account → Trade for commitment
            └─→ Standard account → Small concession or hold
```

## Scripts & Tools

| Script | Purpose |
|--------|---------|
| `scripts/deal_calculator.py` | Calculate deal scenarios and margins |
| `scripts/negotiation_planner.py` | Prepare negotiation strategy |

## Best Practices

### Do's
- Prepare thoroughly before every negotiation
- Listen more than you talk
- Focus on interests, not positions
- Always trade, never give away
- Document all agreements
- Know when to walk away
- Build long-term relationships

### Don'ts
- Never negotiate against yourself
- Don't cave to pressure
- Avoid lying or misleading
- Don't show desperation
- Never insult their position
- Avoid ultimatums (unless real)
- Don't forget the big picture

## Reference

→ See `templates/negotiation_scripts.md` for word-for-word responses
→ See `reference.md` for advanced negotiation techniques
