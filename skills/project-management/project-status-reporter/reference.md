# Project Status Reporter Reference

Comprehensive reference for RAG status assessment, stakeholder reporting, and project health monitoring.

## RAG Status Framework Deep Dive

### Overall RAG Determination

The overall project RAG status is determined by the worst-performing dimension, with judgment applied for context:

| Scenario | Overall RAG | Rationale |
|----------|-------------|-----------|
| All dimensions Green | GREEN | Project healthy across the board |
| One dimension Amber, rest Green | AMBER | One area needs attention |
| Two+ dimensions Amber | AMBER (trending RED) | Multiple areas under stress |
| Any dimension Red | RED | Critical intervention needed |
| Red dimension has active recovery plan | AMBER | Recovery underway, managed risk |

### RAG Transition Rules

RAG status changes should be deliberate and documented:

**Escalating (Green -> Amber -> Red):**
- Document the specific trigger that caused the change
- State the threshold that was crossed
- Include the recovery plan and timeline
- Notify stakeholders proactively (do not wait for the next report)

**De-escalating (Red -> Amber -> Green):**
- Document what was resolved and how
- Confirm the improvement is sustained (not a one-time data point)
- Keep monitoring for regression for at least 2 reporting periods
- Note lessons learned

### Quantitative RAG Thresholds

Use these benchmarks to reduce subjectivity in RAG assessment:

#### Schedule

| Metric | Green | Amber | Red |
|--------|-------|-------|-----|
| Milestone variance | +/- 3 days | 4-10 days late | > 10 days late |
| Sprint velocity vs plan | > 90% | 75-90% | < 75% |
| Critical path float | > 5 days | 1-5 days | 0 or negative |
| Carry-over rate | < 10% | 10-25% | > 25% |

#### Budget

| Metric | Green | Amber | Red |
|--------|-------|-------|-----|
| Burn rate vs plan | Within 5% | 5-15% over | > 15% over |
| EAC vs BAC | Within 5% | 5-15% over | > 15% over |
| Contingency remaining | > 50% | 20-50% | < 20% |
| Unplanned costs | < 5% of budget | 5-10% | > 10% |

#### Quality

| Metric | Green | Amber | Red |
|--------|-------|-------|-----|
| Defect escape rate | < 5% | 5-15% | > 15% |
| Critical bugs open | 0 | 1-2 | 3+ |
| Test coverage | > 80% | 60-80% | < 60% |
| Build success rate | > 95% | 85-95% | < 85% |

#### Resources

| Metric | Green | Amber | Red |
|--------|-------|-------|-----|
| Team utilization | 70-85% | 85-95% or < 60% | > 95% or < 50% |
| Open positions | 0 | 1 | 2+ or key role |
| Attrition risk | None | 1 team member | Key contributor |
| Skill coverage | All skills covered | 1 single point of failure | 2+ gaps |

## Stakeholder Communication Guide

### Tailoring Reports by Audience

#### Executive / C-Suite

**They want to know:** Is the project on track? Do I need to make a decision? What are the business risks?

- Maximum 1 page
- Lead with overall RAG and one-sentence summary
- Include only top 3 risks and top decisions needed
- Use business language, not technical jargon
- Include budget summary
- Visual: RAG dashboard, milestone timeline

#### Steering Committee

**They want to know:** Are we within governance thresholds? What risks need committee action?

- 2-3 pages maximum
- All RAG dimensions with trend arrows
- Budget actuals vs forecast with variance analysis
- Risk register summary (high and critical only)
- Change requests requiring approval
- Resource allocation overview

#### Project Team

**They want to know:** What's our progress? What should I focus on? What's blocking us?

- Full detail, no length limit
- Sprint-level metrics (velocity, burndown, carry-over)
- Detailed blocker list with owners and resolution plans
- Technical metrics (build success, test coverage, PR throughput)
- Next sprint plan

#### Client / External

**They want to know:** Is my project on schedule? When will I see deliverables? Do you need anything from me?

- Professional, polished format
- Business outcomes, not implementation details
- Clear ask for any client inputs needed
- Upcoming deliverable dates
- Budget status (high-level)
- Positive framing with honest risk disclosure

## Earned Value Management (EVM)

### Key EVM Metrics

| Metric | Formula | Interpretation |
|--------|---------|---------------|
| Planned Value (PV) | Budgeted cost of work scheduled | What we planned to spend by now |
| Earned Value (EV) | Budgeted cost of work performed | What the completed work is worth |
| Actual Cost (AC) | Actual cost of work performed | What we actually spent |
| Schedule Variance (SV) | EV - PV | Negative = behind schedule |
| Cost Variance (CV) | EV - AC | Negative = over budget |
| Schedule Performance Index (SPI) | EV / PV | < 1.0 = behind schedule |
| Cost Performance Index (CPI) | EV / AC | < 1.0 = over budget |
| Estimate at Completion (EAC) | BAC / CPI | Projected total cost |
| Estimate to Complete (ETC) | EAC - AC | Remaining cost |
| Variance at Completion (VAC) | BAC - EAC | Expected budget variance |

### EVM Status Mapping

| SPI | CPI | Status | Interpretation |
|-----|-----|--------|---------------|
| > 1.0 | > 1.0 | GREEN | Ahead of schedule, under budget |
| > 0.9 | > 0.9 | GREEN | Within acceptable range |
| 0.8-0.9 | 0.8-0.9 | AMBER | Behind/over but recoverable |
| < 0.8 | < 0.8 | RED | Significant deviation, recovery plan needed |

## Report Distribution Checklist

- [ ] RAG status verified with project lead
- [ ] Numbers cross-checked with source data
- [ ] All action items have owners and due dates
- [ ] Report reviewed for confidential information (before client distribution)
- [ ] Format matches the audience (executive = brief, team = detailed)
- [ ] Sent via agreed channel on agreed schedule
- [ ] Archived in project repository
- [ ] Follow-up scheduled for open decisions

## References

- PMI PMBOK Guide, 7th Edition - Project Performance Domain
- Earned Value Management: https://www.pmi.org/learning/library/earned-value-management-systems-analysis-8026
- RAG Status Best Practices: https://www.apm.org.uk/resources/find-a-resource/rag-status/
