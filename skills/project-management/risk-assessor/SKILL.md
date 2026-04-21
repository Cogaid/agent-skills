---
name: risk-assessor
description: Identify and assess project risks systematically with scoring, mitigation planning, and escalation. Use when user mentions "risk assessment," "risk register," "risk matrix," "risk mitigation," "probability impact," "project risks," "risk review."
metadata:
  version: 1.0.0
  category: project-management
---

# Risk Assessor

Identify, score, and manage project risks with structured registers, probability-impact matrices, and mitigation workflows.

## Purpose

Every project faces uncertainty. The difference between projects that succeed and those that fail often comes down to how well risks are identified, assessed, and managed. This skill provides a systematic framework for risk identification, a scoring methodology, mitigation strategy selection, and ongoing risk review processes. It ensures risks are visible, prioritized, and actively managed rather than ignored until they become crises.

## Quick Reference

### Risk Scoring Formula

```
Risk Score = Probability x Impact x Detectability

Where:
  Probability   = Likelihood of occurrence (1-5 scale)
  Impact        = Severity of consequences (1-5 scale)
  Detectability = Ability to detect before impact (1-5, where 5 = hardest to detect)

Simple Score (without detectability):
  Risk Score = Probability x Impact (range: 1-25)

Priority:
  1-4   = Low (accept/monitor)
  5-9   = Medium (mitigation plan needed)
  10-15 = High (active mitigation required)
  16-25 = Critical (immediate escalation)
```

### Probability Scale

| Score | Label | Description | Frequency Guide |
|-------|-------|-------------|----------------|
| 1 | Rare | Unlikely to occur | < 10% chance |
| 2 | Unlikely | Could occur but not expected | 10-30% chance |
| 3 | Possible | Might occur at some point | 30-50% chance |
| 4 | Likely | Will probably occur | 50-80% chance |
| 5 | Almost Certain | Expected to occur | > 80% chance |

### Impact Scale

| Score | Label | Schedule Impact | Budget Impact | Quality Impact |
|-------|-------|----------------|---------------|----------------|
| 1 | Negligible | < 1 day delay | < 1% overrun | Minor cosmetic issue |
| 2 | Minor | 1-3 days delay | 1-5% overrun | Workaround available |
| 3 | Moderate | 1-2 weeks delay | 5-10% overrun | Feature degraded |
| 4 | Major | 2-4 weeks delay | 10-20% overrun | Major feature unusable |
| 5 | Severe | > 1 month delay | > 20% overrun | System failure, data loss |

### Probability-Impact Matrix

```
              Impact
              1    2    3    4    5
           ┌────┬────┬────┬────┬────┐
Prob  5    │  5 │ 10 │ 15 │ 20 │ 25 │  ← Critical (16-25)
           ├────┼────┼────┼────┼────┤
      4    │  4 │  8 │ 12 │ 16 │ 20 │  ← High (10-15)
           ├────┼────┼────┼────┼────┤
      3    │  3 │  6 │  9 │ 12 │ 15 │  ← Medium (5-9)
           ├────┼────┼────┼────┼────┤
      2    │  2 │  4 │  6 │  8 │ 10 │  ← Low (1-4)
           ├────┼────┼────┼────┼────┤
      1    │  1 │  2 │  3 │  4 │  5 │
           └────┴────┴────┴────┴────┘
```

## Workflow

### Risk Identification Techniques

Use multiple techniques to ensure comprehensive risk identification:

| Technique | Description | Best For |
|-----------|-------------|----------|
| **Brainstorming** | Open team discussion of "what could go wrong" | Early project phases |
| **Checklist Review** | Review common risks by category (see below) | All projects, quick coverage |
| **Assumption Analysis** | List project assumptions and assess validity | Complex projects |
| **SWOT Analysis** | Strengths, weaknesses, opportunities, threats | Strategic/business risks |
| **Pre-mortem** | "Imagine the project failed - why?" | Challenging blind spots |
| **Expert Interviews** | Consult experienced practitioners | Technical/domain risks |
| **Historical Review** | Review risks from similar past projects | Repeat/similar projects |

### Common Risk Categories Checklist

| Category | Example Risks |
|----------|--------------|
| **Technical** | New technology, integration complexity, performance, scalability |
| **Schedule** | Unrealistic timeline, dependency delays, estimation errors |
| **Resource** | Key person dependency, skill gaps, team attrition, hiring delays |
| **Scope** | Requirements volatility, scope creep, unclear requirements |
| **External** | Vendor delays, regulatory changes, market shifts, third-party APIs |
| **Organizational** | Priority changes, budget cuts, stakeholder turnover, restructuring |
| **Quality** | Insufficient testing, technical debt, security vulnerabilities |
| **Communication** | Distributed team issues, stakeholder misalignment, language barriers |

### Risk Review Workflow

```
Weekly Risk Review Process:

1. REVIEW existing risks (10 min)
   - Has probability or impact changed?
   - Are mitigation actions on track?
   - Can any risks be closed?

2. IDENTIFY new risks (10 min)
   - Any new risks surfaced this week?
   - Any assumptions invalidated?
   - Any new dependencies or blockers?

3. ASSESS and SCORE new risks (5 min)
   - Apply probability and impact scores
   - Calculate risk score
   - Assign risk owner

4. PLAN mitigation for high/critical risks (10 min)
   - Select mitigation strategy
   - Define actions with owners and deadlines
   - Estimate mitigation cost

5. ESCALATE as needed (5 min)
   - Critical risks → immediate escalation to sponsor
   - High risks → include in next status report
   - Update risk register
```

### Mitigation Strategy Categories

| Strategy | Description | When to Use | Example |
|----------|-------------|-------------|---------|
| **Avoid** | Eliminate the risk by changing the plan | Risk is too severe and avoidable | Use proven technology instead of experimental |
| **Transfer** | Shift risk to a third party | Risk is better managed by others | Purchase insurance, outsource to specialist vendor |
| **Mitigate** | Reduce probability or impact | Risk is manageable with effort | Add automated tests, cross-train team members |
| **Accept** | Acknowledge and monitor without action | Risk is low or cost of mitigation exceeds impact | Minor cosmetic issues, low-probability events |
| **Exploit** | Increase probability of positive risk (opportunity) | Potential upside exists | Allocate more resources to a promising approach |
| **Share** | Share risk/reward with another party | Risk and opportunity are intertwined | Joint venture, partnership agreement |

### Escalation Thresholds

| Risk Score | Level | Escalation Target | Response Time | Action |
|-----------|-------|-------------------|---------------|--------|
| 1-4 | Low | Team lead | Next review cycle | Monitor, no escalation |
| 5-9 | Medium | Project Manager | Within 1 week | Mitigation plan required |
| 10-15 | High | Program Manager / Director | Within 48 hours | Active mitigation, status report inclusion |
| 16-25 | Critical | Executive Sponsor / VP | Within 4 hours | Emergency review, recovery plan |

## Templates

### Risk Register Template

```markdown
## Project Risk Register

**Project:** [Project Name]
**Last Updated:** [Date]
**Risk Owner:** [Project Manager Name]

### Active Risks

| ID | Risk Description | Category | Prob (1-5) | Impact (1-5) | Score | Strategy | Mitigation Plan | Owner | Target Date | Status |
|----|-----------------|----------|-----------|-------------|-------|----------|----------------|-------|-------------|--------|
| R-001 | Key backend developer may leave before project completion | Resource | 3 | 4 | 12 | Mitigate | Cross-train @dev2 on payment module; document architecture decisions | PM | May 15 | In Progress |
| R-002 | Payment gateway API may not support required features | Technical | 2 | 5 | 10 | Avoid | Conduct API capability assessment in Sprint 3; identify alternative if needed | Tech Lead | Apr 30 | Open |
| R-003 | Client may request major scope changes after UAT | Scope | 4 | 3 | 12 | Mitigate | Formal change control process; weekly client demos to align early | PM | Ongoing | Monitoring |
| R-004 | Database performance under load | Technical | 3 | 3 | 9 | Mitigate | Load testing in Sprint 5; optimize queries proactively | Dev Lead | May 20 | Open |
| R-005 | Regulatory compliance requirements unclear | External | 2 | 4 | 8 | Transfer | Engage compliance consultant for review | PM | May 1 | Open |

### Closed Risks

| ID | Risk Description | Score | Outcome | Closed Date | Lessons Learned |
|----|-----------------|-------|---------|-------------|-----------------|
| R-006 | Hosting provider migration during project | 8 | Did not occur - migration postponed | Apr 10 | Early vendor communication prevented issue |

### Risk Summary

| Priority | Count | Trend |
|----------|-------|-------|
| Critical (16-25) | 0 | -- |
| High (10-15) | 3 | ↑ +1 from last week |
| Medium (5-9) | 2 | --> same |
| Low (1-4) | 0 | -- |
| **Total Active** | **5** | |
```

### Risk Assessment Worksheet

```markdown
## Risk Assessment Worksheet

**Risk ID:** R-[XXX]
**Date Identified:** [Date]
**Identified By:** [Name]

### Risk Description
[Clear, specific description of what could go wrong]

### Root Cause Analysis
- **Why might this happen?** [Underlying cause]
- **What conditions make it more likely?** [Contributing factors]
- **Has this happened before?** [Historical precedent]

### Assessment

| Factor | Score | Justification |
|--------|-------|---------------|
| Probability | [1-5] | [Why this score] |
| Impact - Schedule | [1-5] | [Estimated delay] |
| Impact - Budget | [1-5] | [Estimated cost] |
| Impact - Quality | [1-5] | [Quality effect] |
| Impact (highest) | [1-5] | [Use worst case] |
| **Risk Score** | **[P x I]** | |

### Mitigation Options

| Option | Strategy | Cost | Effort | Residual Risk | Recommended? |
|--------|----------|------|--------|---------------|-------------|
| [Option A] | Mitigate | $[X] | [days] | [score after] | Yes/No |
| [Option B] | Avoid | $[X] | [days] | [score after] | Yes/No |
| [Option C] | Accept | $0 | 0 | [unchanged] | Yes/No |

### Selected Approach
- **Strategy:** [Avoid/Transfer/Mitigate/Accept]
- **Actions:** [Specific steps]
- **Owner:** [Name]
- **Deadline:** [Date]
- **Contingency plan:** [What to do if the risk materializes despite mitigation]

### Trigger Indicators
- [Early warning sign 1]
- [Early warning sign 2]
- [Measurable threshold that indicates risk is materializing]
```

## Scripts & Tools

### Risk Score Calculator

```python
# scripts/risk_calculator.py
# Usage: python scripts/risk_calculator.py

def calculate_risk_score(probability: int, impact: int, detectability: int = 1) -> dict:
    """Calculate risk score and priority level."""
    score = probability * impact * detectability
    max_score = 25 if detectability == 1 else 125

    if detectability == 1:
        if score >= 16: level = "CRITICAL"
        elif score >= 10: level = "HIGH"
        elif score >= 5: level = "MEDIUM"
        else: level = "LOW"
    else:
        if score >= 60: level = "CRITICAL"
        elif score >= 30: level = "HIGH"
        elif score >= 12: level = "MEDIUM"
        else: level = "LOW"

    return {
        "score": score,
        "level": level,
        "probability": probability,
        "impact": impact,
        "detectability": detectability,
    }

# Example
risks = [
    {"name": "Key person leaves", "p": 3, "i": 4},
    {"name": "API incompatibility", "p": 2, "i": 5},
    {"name": "Scope creep", "p": 4, "i": 3},
]

print(f"{'Risk':<25} {'P':>3} {'I':>3} {'Score':>6} {'Level':<10}")
print("-" * 52)
for r in risks:
    result = calculate_risk_score(r["p"], r["i"])
    print(f"{r['name']:<25} {r['p']:>3} {r['i']:>3} {result['score']:>6} {result['level']:<10}")
```

### Risk Register Audit Script

```bash
#!/bin/bash
# scripts/risk-audit.sh
# Check risk register for stale or unowned risks
# Usage: ./scripts/risk-audit.sh risk-register.md

FILE="${1:-risk-register.md}"
echo "=== Risk Register Audit ==="
echo "File: $FILE"
echo "Date: $(date +%Y-%m-%d)"
echo ""
echo "Checking for risks without owners..."
grep -n "| R-" "$FILE" | grep "| |" && echo "WARNING: Found risks with empty fields" || echo "OK: All risks have data"
echo ""
echo "Total active risks: $(grep -c "| R-" "$FILE" 2>/dev/null || echo 0)"
```

## Best Practices

### Effective Risk Management

- **Identify early, update often:** The best time to find a risk is before it becomes an issue
- **Be specific:** "Something might go wrong" is not a risk; "Payment API rate limits may cause checkout failures during peak hours" is
- **Separate risks from issues:** Risks are future uncertainties; issues are current problems
- **Assign owners, not committees:** Every risk needs one accountable person
- **Review weekly:** Stale risk registers are worse than no register at all
- **Track residual risk:** After mitigation, re-score the risk to ensure it dropped to acceptable levels
- **Learn from closed risks:** Did the risk occur? Was the mitigation effective? Feed back into future projects

### Risk Register Hygiene

| Practice | Frequency | Why |
|----------|-----------|-----|
| Score recalibration | Weekly | Conditions change; scores should reflect current reality |
| New risk identification | Every sprint planning | New work brings new risks |
| Closed risk review | Monthly | Extract lessons learned |
| Register cleanup | End of phase/milestone | Remove obsolete risks, archive closed ones |
| Cross-project review | Quarterly | Identify systemic risks across the portfolio |

### Common Mistakes

| Mistake | Consequence | Prevention |
|---------|-------------|------------|
| Only tracking technical risks | Blind to organizational and external risks | Use the category checklist for every review |
| Setting and forgetting the register | Risks become stale and irrelevant | Mandatory weekly review ceremony |
| Scoring by gut feel alone | Inconsistent, biased assessments | Use the defined scales with examples |
| Mitigating everything | Wasted effort and budget | Accept low-scoring risks; focus resources on high/critical |
| No contingency plans | Scramble when risks materialize | Every High/Critical risk needs a "Plan B" |
| Treating risk review as compliance theater | Team stops engaging | Make it short (30 min), action-oriented, and valuable |
