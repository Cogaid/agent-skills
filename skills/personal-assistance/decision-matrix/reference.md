# Decision Matrix - Reference Guide

## Framework Deep Dives

### Weighted Decision Matrix - Theory

A weighted decision matrix (also called Pugh matrix or prioritization matrix) is a quantitative technique for evaluating multiple options against multiple criteria. It removes emotional bias by forcing explicit tradeoffs.

**When to use:**
- 3+ options to compare
- 3+ criteria matter
- Stakeholders disagree on the best choice
- Decision needs to be defensible and documented

**When NOT to use:**
- Binary yes/no decisions (use pros/cons instead)
- Decisions with a single dominant criterion (just optimize that)
- Emergency decisions requiring speed over precision

### Scoring Scale Reference

#### 5-Point Scale (Default)

| Score | Label | Definition |
|-------|-------|------------|
| 5 | Excellent | Fully meets or exceeds criterion. Clear, documented evidence. |
| 4 | Good | Mostly meets criterion with minor gaps. Reasonable evidence. |
| 3 | Adequate | Partially meets criterion. Mixed evidence, some concerns. |
| 2 | Poor | Significant gaps or weaknesses. Limited evidence. |
| 1 | Unacceptable | Fails to meet criterion. No evidence or negative indicators. |

#### 10-Point Scale (For finer granularity)

| Range | Label | Use When |
|-------|-------|----------|
| 9-10 | Exceptional | Best-in-class, exceeds requirements |
| 7-8 | Strong | Clearly meets requirements, minor gaps |
| 5-6 | Adequate | Meets minimum requirements |
| 3-4 | Weak | Below requirements, significant gaps |
| 1-2 | Failing | Does not meet requirements |

### Criteria Weighting Methods - Detailed

#### Method 1: Direct Assignment (100 Points)

Distribute exactly 100 points across all criteria. Simple and intuitive but susceptible to anchoring bias.

```
Example (5 criteria):
  Cost:         30 points (30%)
  Quality:      25 points (25%)
  Timeline:     20 points (20%)
  Risk:         15 points (15%)
  Team fit:     10 points (10%)
  TOTAL:       100 points (100%)
```

#### Method 2: Pairwise Comparison (AHP-inspired)

Compare every criterion pair. The winner gets a point. Totals become weights. More rigorous than direct assignment.

```
Comparison matrix (5 criteria):
       Cost  Qual  Time  Risk  Fit   WINS  WEIGHT
Cost    --   Cost  Cost  Cost  Cost   4     40%
Qual   Cost   --   Qual  Qual  Qual   3     30%
Time   Cost  Qual   --   Time  Time   2     20%
Risk   Cost  Qual  Time   --   Risk   1     10%
Fit    Cost  Qual  Time  Risk   --    0      0%
                                     10    100%
```

For ties, award 0.5 points to each.

#### Method 3: Swing Weighting

1. Imagine all criteria at their worst possible level
2. Which criterion would you most want to "swing" from worst to best?
3. That gets weight 100
4. For each remaining criterion, assign a weight relative to the first
5. Normalize to 100%

```
Example:
  Quality: swing from worst to best is most valuable -> 100
  Cost: nearly as important -> 90
  Timeline: important but less so -> 60
  Risk: moderate concern -> 40
  Team fit: nice to have -> 20
  
  Total raw: 310
  Normalized: Quality 32%, Cost 29%, Timeline 19%, Risk 13%, Fit 6%
```

#### Method 4: MoSCoW Allocation

```
Must Have criteria: share 40% of total weight
Should Have criteria: share 30% of total weight
Could Have criteria: share 20% of total weight
Won't Have (tracked): share 10% of total weight

Example with 6 criteria:
  Must Have: Cost (20%), Quality (20%)          = 40%
  Should Have: Timeline (15%), Risk (15%)       = 30%
  Could Have: Team fit (10%), Scalability (10%) = 20%
  Won't Have: Brand prestige (10%)              = 10%
```

### Sensitivity Analysis - Methods

#### Weight Sensitivity

Test if the decision changes when the most influential weight shifts by +/- 10 percentage points.

```
Base case:    Cost 30%, Quality 25%, Timeline 20%, Risk 15%, Fit 10%
Scenario A:   Cost 40%, Quality 20%, Timeline 17%, Risk 13%, Fit 10%
Scenario B:   Cost 20%, Quality 30%, Timeline 23%, Risk 17%, Fit 10%

If the winner changes: decision is SENSITIVE to cost weighting
If winner stays same: decision is ROBUST
```

#### Score Sensitivity

Test if the runner-up could win by improving on its weakest criterion.

```
Winner:     Option A with score 3.85
Runner-up:  Option B with score 3.60
Gap:        0.25 points

What if Option B scores 1 point higher on its weakest criterion?
  If B overtakes A: decision is SENSITIVE -- consider more evidence
  If A still wins: decision is ROBUST
```

#### Break-Even Analysis

Find the exact weight change needed to flip the decision.

```
At what weight for "Cost" does Option B overtake Option A?
  - Increase Cost weight from 30% to 45% -> B wins
  - That is a 15 percentage point swing
  - If stakeholders consider >10% swing unlikely: ROBUST
  - If stakeholders consider it plausible: SENSITIVE
```

### RAPID Framework - Detailed

| Role | Definition | Key Questions | Count |
|------|-----------|---------------|-------|
| **R** Recommend | Drives the analysis and proposes a recommendation | What data supports this? What are the tradeoffs? | 1-2 |
| **A** Agree | Has formal veto power. Use sparingly. | Does this violate any constraints? Legal/compliance OK? | 0-2 |
| **P** Perform | Executes the decision once made | Can we execute this? What resources are needed? | 1+ |
| **I** Input | Provides expertise, data, or perspective | What does the data show? What are the risks? | 2-10 |
| **D** Decide | Makes the final call. ONE person only. | Given all input, what is the decision? | 1 |

Common mistakes:
- Too many A's (Agree) slows decisions. Aim for 0-1.
- No clear D (Decide) means decisions stall.
- R (Recommend) should not also be D (Decide) -- separation prevents bias.

### Six Thinking Hats - Quick Reference

| Hat | Color | Focus | Question |
|-----|-------|-------|----------|
| White | Facts | Data and information | What do we know? What data is missing? |
| Red | Feelings | Emotions and intuition | What does my gut say? How do I feel about this? |
| Black | Caution | Risks and problems | What could go wrong? What are the downsides? |
| Yellow | Optimism | Benefits and value | What is the best case? What value does this create? |
| Green | Creativity | New ideas and alternatives | Are there other options? What if we did X? |
| Blue | Process | Control and summary | What is the decision process? What have we concluded? |

### Decision Documentation Standards

Every decision record (DEC-###) should include:

1. **Context**: Why this decision is needed now
2. **Options considered**: Minimum 3 (including status quo)
3. **Evaluation method**: Which framework was used
4. **Decision**: What was chosen
5. **Rationale**: Why, with reference to scores/analysis
6. **Tradeoffs accepted**: What downsides were knowingly accepted
7. **Dissenting views**: Who disagreed and why
8. **Reversibility**: One-way door (hard to undo) vs. two-way door (easy to change)
9. **Review date**: When to evaluate the outcome
10. **Outcome**: Filled in later -- was the decision good?

### Cognitive Biases to Watch For

| Bias | Description | Mitigation |
|------|-------------|------------|
| Anchoring | Over-relying on the first piece of information | Score criteria before seeing options |
| Confirmation | Seeking evidence that supports preferred option | Have a devil's advocate evaluate the runner-up |
| Sunk cost | Considering past investment in current decision | Frame each option as if starting fresh |
| Status quo | Preferring the current state | Always score "do nothing" as an explicit option |
| Groupthink | Team converging on same answer without debate | Score independently before discussion |
| Availability | Overweighting recent or memorable events | Use data, not anecdotes, for scoring |
| Framing | Decision changes based on how it is presented | Present options in multiple framings |
