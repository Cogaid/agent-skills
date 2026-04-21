# Weighted Decision Matrix Template

## Usage

Fill in the placeholders to build a complete weighted decision matrix. Use `build_matrix.py --interactive` for guided creation.

---

## Decision: {{decision_question}}

**Date:** {{date}}
**Decision Maker:** {{name}}
**Method:** Weighted Decision Matrix
**Options:** {{option_count}}

### Step 1: Define Criteria and Weights (must sum to 100%)

| # | Criterion | Weight | Rationale |
|---|-----------|--------|-----------|
| 1 | {{criterion_1}} | {{weight_1}}% | {{why_this_matters}} |
| 2 | {{criterion_2}} | {{weight_2}}% | {{why_this_matters}} |
| 3 | {{criterion_3}} | {{weight_3}}% | {{why_this_matters}} |
| 4 | {{criterion_4}} | {{weight_4}}% | {{why_this_matters}} |
| 5 | {{criterion_5}} | {{weight_5}}% | {{why_this_matters}} |
| | **TOTAL** | **100%** | |

### Step 2: Score Each Option (1-5 scale)

| Criterion (Weight) | Option A: {{name_a}} | Option B: {{name_b}} | Option C: {{name_c}} |
|---------------------|----------------------|----------------------|----------------------|
| {{c1}} ({{w1}}%) | {{score}} | {{score}} | {{score}} |
| {{c2}} ({{w2}}%) | {{score}} | {{score}} | {{score}} |
| {{c3}} ({{w3}}%) | {{score}} | {{score}} | {{score}} |
| {{c4}} ({{w4}}%) | {{score}} | {{score}} | {{score}} |
| {{c5}} ({{w5}}%) | {{score}} | {{score}} | {{score}} |

### Step 3: Calculate Weighted Scores

| Criterion (Weight) | Option A | Option B | Option C |
|---------------------|----------|----------|----------|
| {{c1}} ({{w1}}%) | {{score x weight}} | {{score x weight}} | {{score x weight}} |
| {{c2}} ({{w2}}%) | {{score x weight}} | {{score x weight}} | {{score x weight}} |
| {{c3}} ({{w3}}%) | {{score x weight}} | {{score x weight}} | {{score x weight}} |
| {{c4}} ({{w4}}%) | {{score x weight}} | {{score x weight}} | {{score x weight}} |
| {{c5}} ({{w5}}%) | {{score x weight}} | {{score x weight}} | {{score x weight}} |
| **TOTAL** | **{{total_a}}** | **{{total_b}}** | **{{total_c}}** |
| **RANK** | **{{rank_a}}** | **{{rank_b}}** | **{{rank_c}}** |

### Recommendation

**Winner:** {{winning_option}}
**Confidence:** {{High / Medium / Low}}
**Score Margin:** {{winner_score - runner_up_score}} points
**Sensitivity:** {{Robust / Sensitive}} to weight changes

### Key Tradeoffs

- Accepted: {{tradeoff_accepted}}
- Mitigated by: {{mitigation_strategy}}

### Notes

{{additional_context_or_caveats}}
