---
name: project-status-reporter
description: Generate project status reports for stakeholders at various levels. Use when user mentions "project status," "status report," "RAG status," "executive summary," "milestone tracking," "project update," "stakeholder report."
metadata:
  version: 1.0.0
  category: project-management
---

# Project Status Reporter

Generate structured project status reports tailored to different stakeholder audiences with RAG indicators, milestone tracking, and risk summaries.

## Purpose

Project status reports are the primary communication vehicle between delivery teams and stakeholders. A good report gives the right level of detail to the right audience, highlights risks early, and drives decisions. This skill provides frameworks for RAG status assessment, templates for executive, team, and client-facing reports, and guidance on reporting cadence and escalation.

## Quick Reference

### RAG Status Framework

| Status | Color | Meaning | Criteria | Action Required |
|--------|-------|---------|----------|-----------------|
| **R** | Red | Off track | > 15% schedule/budget overrun, critical blocker, scope at risk | Immediate escalation, recovery plan needed |
| **A** | Amber | At risk | 5-15% variance, risks materializing, dependencies slipping | Mitigation in progress, management awareness |
| **G** | Green | On track | Within 5% of plan, risks managed, team stable | Continue as planned |
| **B** | Blue | Complete | Milestone or deliverable finished and accepted | Archive and celebrate |

### RAG Assessment Dimensions

| Dimension | Green | Amber | Red |
|-----------|-------|-------|-----|
| **Schedule** | On or ahead of plan | 1-2 weeks behind | > 2 weeks behind |
| **Budget** | Within 5% of forecast | 5-15% over forecast | > 15% over forecast |
| **Scope** | No unplanned changes | Minor scope adjustments | Major scope change or cut |
| **Quality** | Defect rate within norm | Rising defect trend | Critical defects in production |
| **Resources** | Team stable and sufficient | 1 role unfilled or at risk | Key roles vacant, team attrition |
| **Risks** | All risks mitigated or low | 1-2 medium risks active | High-impact risk materialized |

### Reporting Cadence Guide

| Audience | Frequency | Format | Detail Level | Key Focus |
|----------|-----------|--------|-------------|-----------|
| Executive / C-Suite | Bi-weekly or monthly | 1-page summary | High-level only | RAG, milestones, decisions needed |
| Steering Committee | Weekly or bi-weekly | 2-3 page report | Medium | RAG, risks, budget, timeline |
| Project Team | Weekly | Detailed report | Full detail | Tasks, blockers, metrics |
| Client / External | Weekly or bi-weekly | Polished report | Medium, curated | Progress, milestones, next steps |
| PMO / Portfolio | Monthly | Standardized template | Aggregated | Cross-project status, resource utilization |

## Workflow

### Status Report Generation Process

1. **Collect inputs** (Day before report due)
   - Sprint/iteration progress data
   - Blocker and risk updates from team leads
   - Budget actuals from finance
   - Milestone completion status
   - Change requests and scope updates

2. **Assess RAG status** for each dimension
   - Compare actuals to plan across schedule, budget, scope, quality, resources
   - Apply RAG criteria from the framework above
   - Document rationale for any non-Green status

3. **Draft the report** using the appropriate audience template
   - Start with overall RAG and executive summary
   - Add detail sections relevant to the audience
   - Include forward-looking items (next period plan, decisions needed)

4. **Review and validate**
   - Confirm RAG assessment with project lead
   - Verify numbers with data sources
   - Ensure action items have owners and dates

5. **Distribute**
   - Send to stakeholders via agreed channel (email, Confluence, Slack)
   - Archive in project repository
   - Follow up on decisions needed within 48 hours

## Templates

### Executive Summary Report

```markdown
## Project Status Report - Executive Summary

**Project:** [Project Name]
**Report Date:** [Date]
**Reporting Period:** [Start] - [End]
**Project Manager:** [Name]

### Overall Status: [GREEN / AMBER / RED]

| Dimension | Status | Trend | Comment |
|-----------|--------|-------|---------|
| Schedule | GREEN | --> | On track for June 15 delivery |
| Budget | AMBER | ↓ | 8% over due to infrastructure costs |
| Scope | GREEN | --> | No changes this period |
| Quality | GREEN | ↑ | Defect rate decreased 20% |
| Resources | AMBER | --> | Hiring for senior backend role |

### Key Highlights
- [Major achievement or milestone completed]
- [Important decision made or pending]
- [Notable risk or issue update]

### Milestones

| Milestone | Planned Date | Forecast Date | Status | Notes |
|-----------|-------------|---------------|--------|-------|
| Requirements Complete | Mar 1 | Mar 1 | DONE | Signed off |
| Design Complete | Apr 1 | Apr 3 | DONE | 2-day delay, absorbed |
| Development Complete | Jun 1 | Jun 1 | GREEN | On track |
| UAT Start | Jun 15 | Jun 15 | GREEN | UAT plan drafted |
| Go-Live | Jul 1 | Jul 1 | GREEN | Deployment plan pending |

### Decisions Needed

| # | Decision | Owner | Needed By | Impact if Delayed |
|---|----------|-------|-----------|-------------------|
| 1 | Approve additional cloud budget ($15K) | CTO | Apr 25 | Development blocked |
| 2 | Confirm UAT participant list | VP Product | May 1 | UAT start delayed |

### Budget Summary

| Category | Budget | Actual | Forecast | Variance |
|----------|--------|--------|----------|----------|
| Personnel | $200K | $180K | $205K | +2.5% |
| Infrastructure | $50K | $48K | $58K | +16% |
| Licenses | $20K | $20K | $20K | 0% |
| **Total** | **$270K** | **$248K** | **$283K** | **+4.8%** |
```

### Team-Level Detailed Report

```markdown
## Project Status Report - Team Detail

**Project:** [Project Name]
**Sprint:** Sprint [N] | **Report Date:** [Date]

### Sprint Progress

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Stories completed | 12 | 14 | AMBER |
| Story points delivered | 34 | 38 | AMBER |
| Bugs fixed | 5 | - | - |
| PRs merged | 18 | - | - |
| Test coverage | 82% | 80% | GREEN |
| Build success rate | 97% | 95% | GREEN |

### Work Breakdown

| Epic / Feature | Total Stories | Done | In Progress | To Do | % Complete |
|---------------|-------------|------|-------------|-------|------------|
| User Auth | 8 | 8 | 0 | 0 | 100% |
| Payment Flow | 12 | 7 | 3 | 2 | 58% |
| Search & Filter | 10 | 2 | 2 | 6 | 20% |
| Admin Dashboard | 6 | 0 | 1 | 5 | 0% |

### Active Blockers

| # | Blocker | Owner | Raised | Age | Impact | Resolution Plan |
|---|---------|-------|--------|-----|--------|----------------|
| 1 | Payment gateway sandbox down | @dev2 | Apr 17 | 3d | Cannot test payment flow | Vendor ticket #4521, ETA Apr 21 |
| 2 | Design for admin dashboard pending | @dev5 | Apr 19 | 1d | Cannot start US-120 | Design review scheduled Apr 20 |

### Technical Metrics

| Metric | Current | Previous | Trend |
|--------|---------|----------|-------|
| Avg PR review time | 4.2 hrs | 5.1 hrs | ↑ Improving |
| Deployment frequency | 3/week | 2/week | ↑ Improving |
| Incident count | 1 | 0 | ↓ Watch |
| Tech debt items | 14 | 16 | ↑ Improving |

### Next Sprint Plan
- Complete Payment Flow epic (5 remaining stories)
- Start Admin Dashboard (target 3 stories)
- Address 2 tech debt items from backlog
```

### Client-Facing Report

```markdown
## Project Progress Report

**Project:** [Project Name]
**Prepared For:** [Client Name]
**Date:** [Date]
**Period:** [Start] - [End]

### Executive Summary

The project remains on track for the planned [Go-Live Date] delivery. During this
period, we completed [key deliverable] and began work on [next phase]. One item
requires your attention regarding [decision needed].

### Overall Status: [GREEN / AMBER / RED]

### Progress This Period
- [Completed deliverable 1 - in business terms, not technical]
- [Completed deliverable 2]
- [Key progress on in-flight work]

### Upcoming Deliverables

| Deliverable | Expected Date | Dependencies |
|-------------|--------------|--------------|
| [Feature/Phase Name] | [Date] | None |
| [Feature/Phase Name] | [Date] | Client sign-off on designs |
| [Feature/Phase Name] | [Date] | Third-party API access |

### Items Requiring Your Input

| # | Item | Why It Matters | Response Needed By |
|---|------|---------------|-------------------|
| 1 | Review and approve wireframes for Phase 2 | Design work blocked | Apr 25 |
| 2 | Confirm user list for beta testing | Testing schedule at risk | May 1 |

### Risk Summary

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| [Risk in business terms] | Medium | High | [What we are doing about it] |

### Next Period Plan
- [What we will deliver next]
- [What we will start working on]
- [Any scheduled meetings or reviews]

### Budget Status
- **Spent to date:** [Amount] of [Total Budget] ([X]%)
- **Forecast at completion:** [Amount] ([On budget / X% over / X% under])
- **Change orders:** [None / Description and amount]
```

### Risk and Issue Log

```markdown
### Active Risks

| ID | Risk | Probability | Impact | Score | Owner | Mitigation | Status |
|----|------|------------|--------|-------|-------|------------|--------|
| R-01 | Key developer leaves | Medium | High | 12 | PM | Cross-training plan | Monitoring |
| R-02 | Third-party API delay | High | Medium | 12 | Tech Lead | Alternative API identified | Active |
| R-03 | Scope increase from client | Low | High | 8 | PM | Change control process | Monitoring |

### Active Issues

| ID | Issue | Severity | Owner | Raised | Target Resolution | Status |
|----|-------|----------|-------|--------|-------------------|--------|
| I-01 | Staging environment unstable | High | DevOps | Apr 15 | Apr 22 | In Progress |
| I-02 | Missing API documentation | Medium | Tech Lead | Apr 18 | Apr 25 | Open |
```

## Scripts & Tools

### Status Data Collector

```bash
#!/bin/bash
# scripts/collect-status-data.sh
# Collects sprint metrics from Jira and GitHub for status reports
# Usage: ./scripts/collect-status-data.sh --sprint "Sprint 14" --repo "org/repo"

SPRINT="${1:-current}"
echo "=== Sprint Status Data ==="
echo "Sprint: $SPRINT"
echo "Date: $(date +%Y-%m-%d)"
echo ""
echo "--- GitHub Metrics ---"
echo "PRs merged this week: $(gh pr list --repo "$2" --state merged --json number --jq length 2>/dev/null || echo 'N/A')"
echo "Open PRs: $(gh pr list --repo "$2" --state open --json number --jq length 2>/dev/null || echo 'N/A')"
echo "Open Issues: $(gh issue list --repo "$2" --state open --json number --jq length 2>/dev/null || echo 'N/A')"
```

### RAG Status Calculator

```python
# scripts/rag_calculator.py
# Usage: python scripts/rag_calculator.py

def assess_rag(dimension: str, actual: float, planned: float) -> str:
    """Assess RAG status based on variance percentage."""
    if planned == 0:
        return "GREEN"
    variance = ((actual - planned) / planned) * 100
    if dimension in ("schedule", "budget"):
        if variance > 15:
            return "RED"
        elif variance > 5:
            return "AMBER"
        return "GREEN"
    return "GREEN"

# Example usage
dimensions = {
    "schedule": {"actual": 42, "planned": 40},  # days elapsed vs planned
    "budget": {"actual": 248000, "planned": 270000},  # spend vs budget
}

for dim, values in dimensions.items():
    status = assess_rag(dim, values["actual"], values["planned"])
    variance = ((values["actual"] - values["planned"]) / values["planned"]) * 100
    print(f"{dim.title():12s} | {status:6s} | Variance: {variance:+.1f}%")
```

## Best Practices

### Writing Effective Status Reports

- **Lead with the headline:** Overall RAG status and one-sentence summary first
- **Be honest about Amber/Red:** Stakeholders lose trust if surprised by problems you knew about
- **Include trend arrows:** Show whether things are improving or declining, not just current state
- **Action items need owners and dates:** "We need to address X" is not an action item
- **Tailor to the audience:** Executives need decisions; teams need details; clients need confidence
- **Keep a consistent format:** Same template every period so readers know where to find information
- **Archive reports:** They become valuable project history for retrospectives and future planning

### Report Quality Checklist

| Check | Question |
|-------|----------|
| Accuracy | Are all numbers verified against source data? |
| Completeness | Are all dimensions (schedule, budget, scope, quality, resources) covered? |
| Actionability | Does every risk/issue have an owner and mitigation? |
| Timeliness | Is the report delivered on the agreed schedule? |
| Clarity | Can a new stakeholder understand the status without context? |
| Honesty | Does the RAG status match reality? Would the team agree with it? |
| Forward-looking | Does the report include next steps and upcoming milestones? |
| Decision-ready | Are decisions needed clearly stated with deadlines and impact? |
