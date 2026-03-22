---
name: customer-feedback-analyzer
description: Analyzes customer feedback, identifies trends, and extracts insights from support data. Use when the user mentions "analyze feedback," "customer insights," "survey results," "NPS analysis," "CSAT trends," "support ticket analysis," "voice of customer," "feedback themes," "sentiment analysis," "churn signals," "common complaints," "feature requests analysis," or "support metrics."
metadata:
  version: 1.1.0
  category: customer-support
---

# Customer Feedback Analyzer

Extract actionable insights from customer feedback to drive improvements.

## Quick Start

1. **Gather data**: Collect feedback from tickets, surveys, reviews
2. **Run sentiment analysis**: `python scripts/analyze_sentiment.py`
3. **Extract themes**: `python scripts/extract_themes.py`
4. **Calculate NPS**: `python scripts/calculate_nps.py` (if applicable)
5. **Generate report**: Use [templates/report.md](templates/report.md)

## Analysis Workflow

```
Feedback Analysis Progress:
- [ ] Step 1: Collect feedback data (export from sources)
- [ ] Step 2: Run sentiment analysis (analyze_sentiment.py)
- [ ] Step 3: Extract themes and categories (extract_themes.py)
- [ ] Step 4: Calculate metrics (NPS, CSAT if applicable)
- [ ] Step 5: Identify patterns and trends
- [ ] Step 6: Generate insights report
- [ ] Step 7: Create action recommendations
```

## Analysis Types

| Analysis | Script | Output |
|----------|--------|--------|
| Sentiment | `analyze_sentiment.py` | Positive/negative/neutral scores |
| Themes | `extract_themes.py` | Categorized feedback themes |
| NPS | `calculate_nps.py` | NPS score with breakdown |
| Trends | `analyze_trends.py` | Time-series patterns |

## Utility Scripts

**analyze_sentiment.py**: Score feedback sentiment
```bash
python scripts/analyze_sentiment.py feedback.csv --output results.json
# Output: Sentiment scores per entry and aggregate
```

**extract_themes.py**: Categorize feedback into themes
```bash
python scripts/extract_themes.py feedback.csv
# Output: Themed categories with counts
```

**calculate_nps.py**: Calculate NPS from survey data
```bash
python scripts/calculate_nps.py survey.csv --score-column rating
# Output: NPS score, promoter/passive/detractor breakdown
```

**generate_report.py**: Create executive summary
```bash
python scripts/generate_report.py results.json --format markdown
# Output: Formatted insights report
```

## Quick Reference

### Sentiment Scoring
| Score | Indicators |
|-------|-----------|
| Very Negative (-2) | "terrible," "worst," "hate" |
| Negative (-1) | "frustrated," "disappointed" |
| Neutral (0) | Factual statements |
| Positive (+1) | "good," "helpful," "works well" |
| Very Positive (+2) | "love," "amazing," "excellent" |

### NPS Score Interpretation
| Score Range | Rating |
|-------------|--------|
| 50+ | Excellent |
| 30-49 | Good |
| 0-29 | Needs improvement |
| Below 0 | Critical |

## Resources

- **Analysis frameworks**: [reference.md](reference.md)
- **Report templates**: [templates/](templates/)
- **Metric definitions**: [reference.md](reference.md#metrics)

## Related Skills

- Ticket categorization: `ticket-triage`
- Escalation handling: `escalation-handler`
- Help documentation: `knowledge-base-writer`
