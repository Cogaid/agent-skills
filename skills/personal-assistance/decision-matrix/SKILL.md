---
name: decision-matrix
description: Structure complex decisions with weighted criteria and systematic evaluation. Use when the user mentions "decision matrix," "decision framework," "weighted criteria," "pros and cons," "decision analysis," "compare options," "which should I choose," "evaluate alternatives," "trade-off analysis," "RAPID framework," or "group decision."
metadata:
  version: 1.0.0
  category: personal-assistance
---

# Decision Matrix

Structure complex decisions using weighted criteria, scoring rubrics, and systematic evaluation frameworks to make confident, defensible choices.

## Purpose

Transform ambiguous decisions into clear, structured analyses. Covers weighted decision matrices, multiple evaluation frameworks, sensitivity analysis, group decision facilitation, and documentation templates for decisions that need to withstand scrutiny.

## Quick Reference

### When to Use Each Framework

| Framework | Best For | Complexity | Participants | Time Required |
|-----------|----------|------------|-------------|---------------|
| **Weighted Matrix** | Multi-criteria comparison | Medium | 1-5 | 30-60 min |
| **Pros/Cons** | Simple binary decisions | Low | 1-3 | 10-15 min |
| **RAPID** | Organizational decisions | High | 5-15 | 1-3 hours |
| **Decision Tree** | Sequential choices | Medium | 1-3 | 30-60 min |
| **Six Thinking Hats** | Creative/brainstorm decisions | Medium | 3-8 | 45-90 min |
| **Eisenhower Matrix** | Prioritization decisions | Low | 1 | 5-10 min |
| **Cost-Benefit** | Financial decisions | Medium | 1-5 | 30-60 min |

### Decision Quality Checklist

```
Before finalizing any decision, verify:
- [ ] Problem is clearly defined (what are we deciding?)
- [ ] All viable options are identified (minimum 3)
- [ ] Criteria reflect what actually matters (not just easy to measure)
- [ ] Weights are agreed upon before scoring
- [ ] Scoring is based on evidence, not gut feeling
- [ ] Sensitivity analysis done on close results
- [ ] Key stakeholders have input
- [ ] Reversibility is understood (one-way vs. two-way door)
- [ ] Decision is documented with rationale
- [ ] Review date is set
```

## Templates

### Weighted Decision Matrix

```
DECISION MATRIX
Decision: {{decision_question}}
Date: {{date}}
Decision Maker: {{name}}
Options: {{option_count}}

STEP 1: Define Criteria and Weights (must sum to 100%)
| # | Criterion | Weight | Rationale |
|---|-----------|--------|-----------|
| 1 | {{criterion_1}} | {{weight}}% | {{why_this_matters}} |
| 2 | {{criterion_2}} | {{weight}}% | {{why_this_matters}} |
| 3 | {{criterion_3}} | {{weight}}% | {{why_this_matters}} |
| 4 | {{criterion_4}} | {{weight}}% | {{why_this_matters}} |
| 5 | {{criterion_5}} | {{weight}}% | {{why_this_matters}} |
| | TOTAL | 100% | |

STEP 2: Score Each Option (1-5 scale)
| Criterion (Weight) | Option A | Option B | Option C |
|---------------------|----------|----------|----------|
| {{c1}} ({{w1}}%) | {{score}} | {{score}} | {{score}} |
| {{c2}} ({{w2}}%) | {{score}} | {{score}} | {{score}} |
| {{c3}} ({{w3}}%) | {{score}} | {{score}} | {{score}} |
| {{c4}} ({{w4}}%) | {{score}} | {{score}} | {{score}} |
| {{c5}} ({{w5}}%) | {{score}} | {{score}} | {{score}} |

STEP 3: Calculate Weighted Scores
| Criterion (Weight) | Option A | Option B | Option C |
|---------------------|----------|----------|----------|
| {{c1}} ({{w1}}%) | {{s x w}} | {{s x w}} | {{s x w}} |
| {{c2}} ({{w2}}%) | {{s x w}} | {{s x w}} | {{s x w}} |
| {{c3}} ({{w3}}%) | {{s x w}} | {{s x w}} | {{s x w}} |
| {{c4}} ({{w4}}%) | {{s x w}} | {{s x w}} | {{s x w}} |
| {{c5}} ({{w5}}%) | {{s x w}} | {{s x w}} | {{s x w}} |
|---------------------|----------|----------|----------|
| **TOTAL** | **{{total_a}}** | **{{total_b}}** | **{{total_c}}** |
| **RANK** | **{{rank}}** | **{{rank}}** | **{{rank}}** |

RECOMMENDATION: {{winning_option}}
Confidence: {{high/medium/low}}
Margin: {{winner_score - runner_up_score}} points
```

### Scoring Rubric

```
SCORING RUBRIC (use consistently across all criteria)

| Score | Label | Definition | Evidence Standard |
|-------|-------|------------|-------------------|
| 5 | Excellent | Fully meets or exceeds the criterion | Clear, documented evidence |
| 4 | Good | Mostly meets the criterion, minor gaps | Reasonable evidence |
| 3 | Adequate | Partially meets, some concerns | Mixed evidence |
| 2 | Poor | Significant gaps or weaknesses | Limited evidence |
| 1 | Unacceptable | Fails to meet the criterion | No evidence or negative |

SCORING GUIDANCE:
- Score based on evidence, not preference
- If unsure between two scores, go with the lower one
- Document the reasoning for each score
- Have multiple people score independently, then discuss
- Avoid "3" as a default — it should mean genuinely adequate
```

### Criteria Weighting Methodology

```
CRITERIA WEIGHTING METHODS

METHOD 1: Direct Assignment
- Allocate 100 points across all criteria
- More important criteria get more points
- Quick but can be biased by anchoring

METHOD 2: Pairwise Comparison
Compare each criterion against every other:
       C1    C2    C3    C4    C5    Score  Weight
C1     --    C1    C3    C1    C1    3      30%
C2     C1    --    C3    C2    C2    2      20%
C3     C3    C3    --    C3    C3    4      40%
C4     C1    C2    C3    --    C5    0      0%
C5     C1    C2    C3    C5    --    1      10%
                                    10     100%

METHOD 3: Swing Weighting
1. Set worst possible level for all criteria
2. Ask: which criterion would you most want to improve?
3. That gets the highest weight
4. Repeat for remaining criteria
5. Normalize to 100%

METHOD 4: MoSCoW
- Must Have: 40% total weight split among must-haves
- Should Have: 30% split among should-haves
- Could Have: 20% split among could-haves
- Won't Have: 10% (tracked but minimal weight)
```

### Sensitivity Analysis

```
SENSITIVITY ANALYSIS
Purpose: Test if the decision changes when assumptions shift

TEST 1: Weight Sensitivity
What if we change the most important criterion's weight by +/- 10%?

| Scenario | Weight Change | Winner | Score Gap |
|----------|--------------|--------|-----------|
| Base case | As defined | {{winner}} | {{gap}} |
| +10% on {{top_criterion}} | {{new_weight}} | {{winner}} | {{gap}} |
| -10% on {{top_criterion}} | {{new_weight}} | {{winner}} | {{gap}} |

Decision is {{robust / sensitive}} to weight changes.

TEST 2: Score Sensitivity
What if the runner-up scores 1 point higher on its weakest criterion?

| Scenario | Changed Score | Winner | Score Gap |
|----------|--------------|--------|-----------|
| Base case | As scored | {{winner}} | {{gap}} |
| Runner-up +1 on {{criterion}} | {{new_score}} | {{winner}} | {{gap}} |
| Winner -1 on {{criterion}} | {{new_score}} | {{winner}} | {{gap}} |

Decision is {{robust / sensitive}} to score changes.

TEST 3: Option Elimination
Remove each option and re-rank. Does the relative order change?
If yes, there may be a rank reversal problem — reconsider criteria.

CONCLUSION:
{{sensitivity_summary}}
```

### Pros/Cons Framework

```
PROS/CONS ANALYSIS
Decision: {{decision_question}}
Options: {{option_a}} vs. {{option_b}}

OPTION A: {{option_a}}
┌─────────────────────────┬─────────────────────────┐
│         PROS            │         CONS            │
├─────────────────────────┼─────────────────────────┤
│ + {{pro_1}}             │ - {{con_1}}             │
│   Weight: {{H/M/L}}     │   Weight: {{H/M/L}}     │
│ + {{pro_2}}             │ - {{con_2}}             │
│   Weight: {{H/M/L}}     │   Weight: {{H/M/L}}     │
│ + {{pro_3}}             │ - {{con_3}}             │
│   Weight: {{H/M/L}}     │   Weight: {{H/M/L}}     │
└─────────────────────────┴─────────────────────────┘

OPTION B: {{option_b}}
┌─────────────────────────┬─────────────────────────┐
│         PROS            │         CONS            │
├─────────────────────────┼─────────────────────────┤
│ + {{pro_1}}             │ - {{con_1}}             │
│   Weight: {{H/M/L}}     │   Weight: {{H/M/L}}     │
│ + {{pro_2}}             │ - {{con_2}}             │
│   Weight: {{H/M/L}}     │   Weight: {{H/M/L}}     │
│ + {{pro_3}}             │ - {{con_3}}             │
│   Weight: {{H/M/L}}     │   Weight: {{H/M/L}}     │
└─────────────────────────┴─────────────────────────┘

VERDICT: {{option}} wins because {{rationale}}
```

### RAPID Decision Framework

```
RAPID FRAMEWORK
Decision: {{decision_question}}
Timeline: Decision by {{deadline}}

ROLE ASSIGNMENTS:
| Role | Person | Responsibility |
|------|--------|---------------|
| R - Recommend | {{name}} | Proposes the decision, gathers input, drives analysis |
| A - Agree | {{name}} | Must agree; has veto power (use sparingly) |
| P - Perform | {{name}} | Executes once decision is made |
| I - Input | {{name}} | Provides information, expertise, perspective |
| D - Decide | {{name}} | Makes the final call; one person only |

PROCESS:
1. R (Recommend) completes analysis and proposes option
2. I (Input) provides feedback and data within {{timeframe}}
3. R revises recommendation based on input
4. A (Agree) reviews and either agrees or escalates concerns
5. D (Decide) makes the final decision
6. P (Perform) executes the decision

DECISION LOG:
- Recommendation: {{recommendation}}
- Key inputs received: {{input_summary}}
- Concerns raised: {{concerns}}
- Final decision: {{decision}}
- Rationale: {{rationale}}
- Decided on: {{date}}
- Review date: {{review_date}}
```

### Group Decision Facilitation Guide

```
GROUP DECISION FACILITATION

PRE-MEETING (Facilitator prep):
- [ ] Define the decision question clearly
- [ ] Identify all options (minimum 3, including status quo)
- [ ] Select criteria and propose weights
- [ ] Share pre-read materials 48 hours in advance
- [ ] Ask participants to score independently before meeting

MEETING AGENDA (60-90 minutes):
1. [5 min] Frame the decision — what we are deciding and why now
2. [10 min] Confirm criteria and weights — adjust if group disagrees
3. [15 min] Review each option — facts only, no opinions yet
4. [20 min] Individual scoring — silent, independent scoring
5. [15 min] Discuss outliers — where scores differ by 2+ points
6. [10 min] Re-score if needed — after discussion
7. [5 min] Calculate results and announce recommendation
8. [5 min] Confirm decision and assign next steps

FACILITATION TIPS:
- Keep discussion fact-based ("what evidence supports that score?")
- Address the loudest-voice problem: collect scores silently first
- If two options are within 5% of each other, discuss qualitative factors
- Document dissent — it's valuable for future reviews
- Set a review date to evaluate the decision's outcome
```

### Decision Documentation Template

```
DECISION RECORD
ID: DEC-{{number}}
Date: {{date}}
Decision: {{decision_question}}

CONTEXT: {{why_this_decision_needed_now}}

OPTIONS CONSIDERED:
1. {{option_1}} — {{brief_description}}
2. {{option_2}} — {{brief_description}}
3. {{option_3}} — {{brief_description}}

DECISION: {{chosen_option}}

RATIONALE:
{{why_this_option_was_chosen}}

KEY TRADE-OFFS:
- Accepted: {{trade_off_accepted}}
- Mitigated by: {{mitigation}}

DISSENTING VIEWS:
{{who_disagreed_and_why}}

REVERSIBILITY: {{one_way_door / two_way_door}}
REVIEW DATE: {{date_to_evaluate_outcome}}
OUTCOME (filled in at review): {{actual_outcome}}
```

## Scripts & Tools

**build_matrix.py**: Create and calculate a weighted decision matrix
```bash
python scripts/build_matrix.py --criteria 5 --options 3 --interactive
# Output: Guided matrix builder with calculated scores
```

**sensitivity_check.py**: Run sensitivity analysis on a completed matrix
```bash
python scripts/sensitivity_check.py --matrix matrix.json --scenarios all
# Output: Sensitivity report showing decision robustness
```

**facilitate_decision.py**: Generate facilitation materials for group decisions
```bash
python scripts/facilitate_decision.py --participants 6 --method weighted-matrix
# Output: Pre-read packet, scoring sheets, agenda
```

## Best Practices

1. **Define the question first** - "Which vendor to choose" is better than "should we change vendors"
2. **Always include status quo** - Doing nothing is always an option worth scoring
3. **Separate criteria from scoring** - Agree on what matters before evaluating options
4. **Weight before you score** - Prevents reverse-engineering weights to match a preferred answer
5. **Score independently** - Group scoring introduces anchoring and conformity bias
6. **Document dissent** - Minority opinions are valuable for future decision reviews
7. **Set a review date** - Every decision should be revisited after enough data is available
8. **Beware of analysis paralysis** - Perfect information does not exist; decide with 70% confidence
9. **One-way vs. two-way doors** - Spend more time on irreversible decisions
10. **Close the loop** - Record the actual outcome to improve future decision quality

## Related Skills

- Priority management: `task-prioritizer`
- Research support: `research-assistant`
- Meeting facilitation: `meeting-summarizer`
