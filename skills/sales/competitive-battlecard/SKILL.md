---
name: competitive-battlecard
description: Create competitive comparison battlecards for sales teams. Use when the user mentions "battlecard," "competitive analysis," "competitor comparison," "win/loss analysis," "competitive positioning," "objection handling against competitor," "feature comparison," "compete against," or "competitive intelligence."
metadata:
  version: 1.0.0
  category: sales
---

# Competitive Battlecard

Create and maintain competitive battlecards that arm sales reps with the intelligence needed to win against specific competitors.

## Purpose

Build structured competitive comparison documents that cover positioning, feature comparisons, pricing intelligence, objection responses, and trap-setting questions. Designed for rapid consumption during live sales conversations.

## Quick Reference

### Battlecard Structure Overview

| Section | Purpose | Update Cadence |
|---------|---------|---------------|
| **Competitor Snapshot** | Quick overview of competitor | Monthly |
| **Positioning Matrix** | Where they sit vs. us | Quarterly |
| **Feature Comparison** | Side-by-side capabilities | Monthly |
| **Pricing Intelligence** | Known pricing and packaging | Quarterly |
| **Win/Loss Themes** | Patterns from closed deals | Monthly |
| **Objection Responses** | Ready-made counter-arguments | As needed |
| **Trap Questions** | Questions that expose weakness | Quarterly |
| **Landmines** | What they say about us | Monthly |
| **Customer References** | Wins against this competitor | As available |

### Competitive Positioning Matrix

```
                    HIGH PRICE
                        │
         Enterprise     │     Premium Niche
         Legacy         │     Specialist
                        │
   LOW ─────────────────┼───────────────── HIGH
   CAPABILITY           │           CAPABILITY
                        │
         Budget         │     Best Value
         Basic          │     (Target Position)
                        │
                    LOW PRICE
```

## Workflow

### Battlecard Creation Checklist

```
Battlecard Build Progress:
- [ ] Step 1: Gather competitor intel (website, G2, Gartner, earnings)
- [ ] Step 2: Interview 3+ reps who have competed against them
- [ ] Step 3: Review last 10 win/loss records against this competitor
- [ ] Step 4: Complete feature comparison matrix
- [ ] Step 5: Document known pricing and packaging
- [ ] Step 6: Draft objection responses (minimum 5)
- [ ] Step 7: Create trap-setting questions (minimum 5)
- [ ] Step 8: Document their landmines about us
- [ ] Step 9: Collect 2-3 customer win stories
- [ ] Step 10: Review with sales leadership
- [ ] Step 11: Distribute to team with training session
- [ ] Step 12: Set update cadence reminders
```

## Templates

### Full Battlecard Template

```
╔══════════════════════════════════════════════════════════╗
║            COMPETITIVE BATTLECARD                        ║
║            vs. {{competitor_name}}                        ║
║            Last Updated: {{date}}                        ║
╠══════════════════════════════════════════════════════════╣

COMPETITOR SNAPSHOT
━━━━━━━━━━━━━━━━━━
Company: {{competitor_name}}
Founded: {{year}}
Headquarters: {{location}}
Employees: {{headcount}}
Revenue: {{revenue_estimate}}
Key Customers: {{customer_1}}, {{customer_2}}, {{customer_3}}
Recent Funding/News: {{recent_news}}
Target Market: {{target_segments}}
Strengths: {{strength_1}}, {{strength_2}}, {{strength_3}}
Weaknesses: {{weakness_1}}, {{weakness_2}}, {{weakness_3}}

THEIR PITCH (What they say about themselves):
"{{their_positioning_statement}}"

OUR COUNTER-POSITIONING:
"{{our_counter_positioning}}"

WHY WE WIN:
1. {{differentiator_1}}
2. {{differentiator_2}}
3. {{differentiator_3}}

WHY WE LOSE:
1. {{loss_reason_1}} → Mitigation: {{mitigation_1}}
2. {{loss_reason_2}} → Mitigation: {{mitigation_2}}
3. {{loss_reason_3}} → Mitigation: {{mitigation_3}}
╚══════════════════════════════════════════════════════════╝
```

### Feature Comparison Table

```
FEATURE COMPARISON: {{our_product}} vs. {{competitor_name}}

| Feature Area | {{our_product}} | {{competitor}} | Advantage | Notes |
|-------------|-----------------|----------------|-----------|-------|
| {{feature_1}} | ✅ Full | ⚠️ Partial | Us | {{note}} |
| {{feature_2}} | ✅ Full | ✅ Full | Tie | {{note}} |
| {{feature_3}} | ⚠️ Partial | ✅ Full | Them | {{note}} |
| {{feature_4}} | ✅ Full | ❌ None | Us | {{note}} |
| {{feature_5}} | ❌ Roadmap Q3 | ✅ Full | Them (temp) | {{note}} |

Legend: ✅ Full support | ⚠️ Partial/limited | ❌ Not available | 🔜 On roadmap

SCORING SUMMARY:
Us Leading: {{count}} features
Tied: {{count}} features
Them Leading: {{count}} features
```

### Pricing Comparison Template

```
PRICING INTELLIGENCE: {{competitor_name}}
Confidence Level: {{high | medium | low}}
Source: {{source}} (Date: {{date}})

| Tier | {{competitor}} Price | Our Price | Delta | Notes |
|------|---------------------|-----------|-------|-------|
| Starter | {{price}}/mo | {{price}}/mo | {{diff}} | {{note}} |
| Professional | {{price}}/mo | {{price}}/mo | {{diff}} | {{note}} |
| Enterprise | {{price}}/mo | {{price}}/mo | {{diff}} | {{note}} |

PRICING TACTICS THEY USE:
- {{tactic_1}} (e.g., "First year discount of 40%")
- {{tactic_2}} (e.g., "Per-seat pricing that scales fast")
- {{tactic_3}} (e.g., "Hidden implementation fees")

OUR PRICING RESPONSE:
- If they undercut: {{response}}
- If they bundle: {{response}}
- TCO argument: {{tco_talking_point}}
```

### Objection Response Cards

```
OBJECTION RESPONSES vs. {{competitor_name}}

OBJECTION 1: "{{competitor}} has {{feature}} and you don't."
RESPONSE: "Great question. While {{competitor}} approaches this with
{{their_approach}}, our customers have found that {{our_approach}}
actually delivers better results because {{reason}}. For example,
{{customer_example}} saw {{specific_result}}."

OBJECTION 2: "{{competitor}} is cheaper."
RESPONSE: "I understand budget is important. When you look at total
cost of ownership, our customers typically see {{tco_advantage}}
because {{reason}}. {{competitor}}'s pricing doesn't include
{{hidden_cost_1}} and {{hidden_cost_2}}, which adds {{amount}}
to the real cost. Would it be helpful to build a side-by-side
TCO analysis for your specific use case?"

OBJECTION 3: "We're already using {{competitor}}."
RESPONSE: "That's actually a great starting point — you already
understand the category. Many of our best customers, like
{{customer_name}}, switched from {{competitor}} because
{{switch_reason}}. They saw {{improvement_metric}} within
{{timeframe}}. What are the top 2-3 things you wish
{{competitor}} did better?"

OBJECTION 4: "{{competitor}} has more market share / is bigger."
RESPONSE: "{{competitor}} was an early mover, which is why they
have broader adoption. But the market has evolved. Our platform
was built for {{modern_requirement}} from the ground up, while
{{competitor}} is retrofitting legacy architecture. That's why
we're growing {{growth_rate}} year-over-year and why analysts
like {{analyst}} rank us {{ranking}}."

OBJECTION 5: "We've heard {{competitor}} is easier to use."
RESPONSE: "Ease of use is critical — that's why we invest heavily
in UX. Our average time-to-value is {{time_to_value}}, compared
to {{competitor}}'s {{their_ttv}}. On G2, our ease-of-use rating
is {{our_rating}} vs. their {{their_rating}}. But don't take my
word for it — I'd love to show you a quick demo so you can
judge for yourself."
```

### Trap-Setting Questions

```
TRAP QUESTIONS (Questions that expose {{competitor}}'s weaknesses)

Use these during discovery or when the prospect is evaluating both:

1. "How important is {{capability_they_lack}} to your workflow?"
   → Leads to: They can't deliver this; we can.

2. "What's your expected timeline for implementation?"
   → Leads to: Their implementation takes {{longer_time}} vs. our {{shorter_time}}.

3. "Have you looked into the total cost including {{hidden_cost}}?"
   → Leads to: Exposes hidden fees they don't mention upfront.

4. "How does your team currently handle {{use_case}}?"
   → Leads to: Reveals a pain point where we excel and they struggle.

5. "What happens when you need to {{scale_scenario}}?"
   → Leads to: Their architecture doesn't scale well for this.

6. "Who owns {{function}} in your current process?"
   → Leads to: Shows our automation advantage vs. their manual process.

IMPORTANT: Ask these naturally during discovery. Never frame them
as attacks on the competitor — frame them as genuine curiosity
about the prospect's needs.
```

### Win/Loss Analysis Framework

```
WIN/LOSS ANALYSIS vs. {{competitor_name}}
Period: {{start_date}} to {{end_date}}

SUMMARY:
Total Opportunities: {{total}}
Wins: {{wins}} ({{win_rate}}%)
Losses: {{losses}} ({{loss_rate}}%)
No Decision: {{no_decision}} ({{nd_rate}}%)

WIN THEMES (why we won):
| Theme | Frequency | Example |
|-------|-----------|---------|
| {{theme}} | {{count}} deals | "{{quote}}" |

LOSS THEMES (why we lost):
| Theme | Frequency | Mitigation |
|-------|-----------|------------|
| {{theme}} | {{count}} deals | {{action}} |

DEAL CHARACTERISTICS:
- Average deal size (wins): {{avg_win_size}}
- Average deal size (losses): {{avg_loss_size}}
- Average sales cycle (wins): {{avg_win_cycle}}
- Average sales cycle (losses): {{avg_loss_cycle}}
- Win rate by segment: Enterprise {{ent_rate}}% | Mid-Market {{mm_rate}}% | SMB {{smb_rate}}%
```

## Update Cadence

| Component | Frequency | Owner | Trigger |
|-----------|-----------|-------|---------|
| Feature comparison | Monthly | Product Marketing | Product releases |
| Pricing intel | Quarterly | Competitive Intel | Pricing changes |
| Objection responses | As needed | Sales Enablement | New objections from field |
| Win/loss data | Monthly | Sales Ops | Deal close |
| Trap questions | Quarterly | Sales Leadership | Strategy review |
| Customer references | As available | Customer Success | New wins |

## Scripts & Tools

**generate_battlecard.py**: Create battlecard from competitor data
```bash
python scripts/generate_battlecard.py --competitor "Acme Corp" --template full
# Output: Formatted battlecard with placeholder prompts
```

**win_loss_analysis.py**: Analyze CRM data for win/loss patterns
```bash
python scripts/win_loss_analysis.py --competitor "Acme Corp" --period last-6-months
# Output: Win/loss themes, rates, and deal characteristics
```

**compare_features.py**: Generate feature comparison from product data
```bash
python scripts/compare_features.py --competitor "Acme Corp" --categories all
# Output: Feature-by-feature comparison matrix
```

## Best Practices

1. **Keep it scannable** - Reps need answers in 10 seconds during a call
2. **Lead with "why we win"** - Confidence matters more than completeness
3. **Be honest about gaps** - Reps lose trust if the card oversells
4. **Include proof points** - Customer quotes and data beat assertions
5. **Update relentlessly** - A stale battlecard is worse than none
6. **Train, don't just distribute** - Role-play objection handling with the team
7. **Source from the field** - Best intel comes from reps in active deals
8. **Track usage** - Measure which cards are used and correlate with win rates

## Related Skills

- ROI arguments: `roi-calculator`
- Proposal writing: `proposal-writer`
- Objection handling: `objection-handler`
- Discovery calls: `discovery-call`
