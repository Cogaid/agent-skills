# Risk Assessor Reference

Comprehensive reference for risk identification, scoring, mitigation planning, and ongoing risk management.

## Risk Identification Frameworks

### Pre-Mortem Analysis

A pre-mortem is one of the most effective risk identification techniques. Instead of asking "what could go wrong?" it asks "imagine the project has already failed -- why?"

**How to run a pre-mortem:**

1. Gather the project team (5-10 people ideal)
2. Set the scene: "It is 6 months from now. The project has failed spectacularly. What happened?"
3. Silent brainstorming: each person writes down 3-5 reasons for failure (5 min)
4. Round-robin sharing: each person reads one reason at a time (10 min)
5. Cluster similar reasons into themes (5 min)
6. Prioritize: dot-vote on the most likely/impactful failure modes (5 min)
7. For the top 3-5 themes, define preventive actions (15 min)

**Why pre-mortems work better than brainstorming:**
- Prospective hindsight increases ability to identify reasons for future outcomes by 30% (Klein, 2007)
- Gives permission to be pessimistic (removes social pressure to be positive)
- Surfaces risks that team members might feel uncomfortable raising directly

### SWOT Analysis for Projects

| | Helpful | Harmful |
|---|---------|---------|
| **Internal** | **Strengths** - Team expertise, proven tech stack, executive support | **Weaknesses** - Skill gaps, tight timeline, technical debt |
| **External** | **Opportunities** - Market timing, partnership potential, new technology | **Threats** - Competitor launch, regulatory change, vendor lock-in |

### Assumption Mapping

Every project is built on assumptions. Identify and validate them:

| Category | Assumption | Confidence | Impact if Wrong | Validation Method |
|----------|-----------|-----------|----------------|-------------------|
| Technical | "The API can handle 10K concurrent users" | Medium | High | Load test in Sprint 3 |
| Business | "Users will adopt the new workflow" | Low | High | User research + beta test |
| Resource | "We can hire a senior dev by May" | Medium | Medium | Backup plan: contractor |
| Schedule | "Design will be complete by April 1" | High | High | Weekly design reviews |
| External | "Vendor API will remain stable" | Medium | Medium | Monitor changelog, have fallback |

## Advanced Scoring Methods

### Risk Priority Number (RPN) with Detectability

The RPN adds a third dimension -- how easily can the risk be detected before it causes damage?

```
RPN = Probability x Impact x Detectability

Where Detectability:
  1 = Almost certain to be detected early (automated monitoring, clear signals)
  2 = High chance of detection (regular reviews catch it)
  3 = Moderate chance of detection (might be missed without focused attention)
  4 = Low chance of detection (subtle, easy to overlook)
  5 = Very difficult to detect (hidden until impact occurs)
```

**RPN Priority Bands:**

| RPN Range | Priority | Action |
|-----------|----------|--------|
| 1-11 | Low | Accept and monitor |
| 12-29 | Medium | Mitigation plan needed |
| 30-59 | High | Active mitigation required |
| 60-125 | Critical | Immediate escalation and action |

### Monte Carlo Simulation Concepts

For schedule and budget risk, Monte Carlo simulation provides probabilistic estimates:

1. For each task, define optimistic, most likely, and pessimistic duration/cost
2. Run thousands of random simulations sampling from these ranges
3. The output is a probability distribution showing likelihood of finishing by each date

**Simplified three-point estimation:**

```
Expected = (Optimistic + 4 x Most_Likely + Pessimistic) / 6
Standard_Deviation = (Pessimistic - Optimistic) / 6

80% confidence = Expected + 0.84 x Standard_Deviation
90% confidence = Expected + 1.28 x Standard_Deviation
95% confidence = Expected + 1.65 x Standard_Deviation
```

## Mitigation Planning Guide

### Cost-Benefit Analysis for Mitigations

Before implementing a mitigation, assess whether the cost is justified:

```
Expected Loss = Probability x Impact_Cost
Mitigation Value = Expected_Loss_Before - Expected_Loss_After
Net Benefit = Mitigation_Value - Mitigation_Cost

If Net Benefit > 0, the mitigation is worth implementing.
```

**Example:**
- Risk: Key developer leaves (P=30%, Impact=$50K in delays)
- Expected Loss: 0.30 x $50,000 = $15,000
- Mitigation: Cross-training program (Cost: $5,000, reduces impact to $15K)
- Expected Loss After: 0.30 x $15,000 = $4,500
- Mitigation Value: $15,000 - $4,500 = $10,500
- Net Benefit: $10,500 - $5,000 = $5,500 (worth doing)

### Residual Risk Tracking

After mitigation, re-score the risk to determine residual risk:

| Phase | Probability | Impact | Score | Level |
|-------|------------|--------|-------|-------|
| Before mitigation | 4 | 4 | 16 | Critical |
| After mitigation | 2 | 3 | 6 | Medium |
| Residual risk accepted | | | 6 | Medium |

If residual risk is still High or Critical, consider additional mitigations or a different strategy.

## Risk Review Meeting Format

### Weekly Risk Review Agenda (30 minutes)

| Time | Activity | Who |
|------|----------|-----|
| 0-5 min | Review dashboard: open risks by severity | Facilitator |
| 5-15 min | Update existing risks: any score changes? mitigation progress? | Risk owners |
| 15-20 min | New risks: anything identified this week? | Full team |
| 20-25 min | Score and assign new risks | Full team |
| 25-30 min | Escalation decisions and action items | Facilitator |

### Risk Review Cadence

| Project Phase | Frequency | Focus |
|--------------|-----------|-------|
| Initiation | Once (comprehensive) | Full risk identification workshop |
| Planning | Weekly | Refine scores, validate assumptions |
| Execution | Weekly | Monitor triggers, mitigation progress |
| Pre-release | Daily (if needed) | Critical/High risks only |
| Closure | Once | Lessons learned, archive register |

## Common Project Risk Catalog

### Technical Risks

| Risk | Typical Probability | Typical Impact | Common Mitigations |
|------|-------------------|---------------|-------------------|
| Integration complexity | High | High | Spike early, POC, contract tests |
| Performance under load | Medium | High | Load testing, capacity planning |
| Security vulnerabilities | Medium | Very High | Security review, penetration testing |
| Data migration failures | Medium | High | Dry runs, rollback plan, parallel run |
| Technology immaturity | Medium | Medium | Spike, fallback to proven tech |

### People Risks

| Risk | Typical Probability | Typical Impact | Common Mitigations |
|------|-------------------|---------------|-------------------|
| Key person dependency | High | High | Cross-training, documentation |
| Skill gaps | Medium | Medium | Training, pairing, hiring |
| Team attrition | Low-Medium | High | Retention measures, bus factor > 2 |
| Communication breakdown | Medium | Medium | Regular syncs, clear RACI |

### External Risks

| Risk | Typical Probability | Typical Impact | Common Mitigations |
|------|-------------------|---------------|-------------------|
| Vendor dependency | Medium | High | SLA, alternative vendor identified |
| Regulatory change | Low | Very High | Legal review, compliance monitoring |
| Market shift | Low | High | MVP approach, iterative delivery |
| Third-party API change | Medium | Medium | Abstraction layer, version pinning |

## References

- PMI PMBOK Guide - Risk Management Knowledge Area
- Gary Klein, "Performing a Project Premortem" (Harvard Business Review, 2007)
- Tom DeMarco & Timothy Lister, "Waltzing with Bears: Managing Risk on Software Projects" (2003)
- ISO 31000:2018 Risk Management Guidelines
