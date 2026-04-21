---
name: sprint-planner
description: Plan sprint goals, capacity, and stories for agile teams. Use when user mentions "sprint planning," "plan the sprint," "sprint capacity," "story points," "sprint backlog," "velocity tracking," "sprint goal."
metadata:
  version: 1.0.0
  category: project-management
---

# Sprint Planner

Plan and organize agile sprints with structured goals, capacity calculations, story estimation, and backlog management.

## Purpose

Sprint planning is the ceremony that sets a team up for a successful iteration. This skill provides frameworks for calculating team capacity, estimating stories, setting meaningful sprint goals, and building a balanced backlog. It covers the full planning workflow from pre-planning preparation through commitment and kickoff.

## Quick Reference

### Sprint Planning Checklist

| Phase | Activity | Owner | Duration |
|-------|----------|-------|----------|
| Pre-Planning | Groom and prioritize backlog | Product Owner | 1-2 days before |
| Pre-Planning | Review previous sprint velocity | Scrum Master | 1 day before |
| Pre-Planning | Confirm team availability | Scrum Master | 1 day before |
| Part 1 | Define sprint goal | Product Owner + Team | 30-45 min |
| Part 1 | Select candidate stories | Product Owner | 15-20 min |
| Part 2 | Task breakdown and estimation | Dev Team | 60-90 min |
| Part 2 | Capacity check and commitment | Dev Team | 15-20 min |
| Wrap-up | Confirm sprint backlog | Full Team | 10 min |

### Story Point Reference Scale

| Points | Complexity | Uncertainty | Effort | Example |
|--------|-----------|-------------|--------|---------|
| 1 | Trivial | None | < 2 hrs | Fix a typo, update a config value |
| 2 | Low | Minimal | 2-4 hrs | Add a field to an existing form |
| 3 | Moderate | Low | 0.5-1 day | Build a new API endpoint (known pattern) |
| 5 | Significant | Some | 1-2 days | Implement a new feature with tests |
| 8 | High | Moderate | 2-4 days | Integrate a third-party service |
| 13 | Very High | High | 4-7 days | Redesign a subsystem |
| 21 | Extreme | Very High | 1-2 weeks | Spike; consider breaking down further |

## Workflow

### Step 1: Calculate Team Capacity

Use this formula to determine how many story points the team can handle:

```
Available Capacity = Team Size x Sprint Days x Focus Factor x Availability

Where:
  Team Size       = Number of developers
  Sprint Days     = Working days in the sprint (typically 10 for 2-week sprints)
  Focus Factor    = Percentage of time on sprint work (typically 0.6-0.8)
  Availability    = Per-person adjustment for PTO, meetings, on-call

Example:
  5 developers x 10 days x 0.7 focus x 0.9 availability = 31.5 ideal days
```

### Capacity Tracking Table

| Team Member | Sprint Days | PTO Days | On-Call Days | Available Days | Focus Factor | Effective Days |
|-------------|------------|----------|--------------|----------------|--------------|----------------|
| Dev 1 | 10 | 0 | 0 | 10 | 0.7 | 7.0 |
| Dev 2 | 10 | 2 | 0 | 8 | 0.7 | 5.6 |
| Dev 3 | 10 | 0 | 2 | 8 | 0.5 | 4.0 |
| Dev 4 | 10 | 0 | 0 | 10 | 0.7 | 7.0 |
| Dev 5 | 10 | 1 | 0 | 9 | 0.7 | 6.3 |
| **Total** | | | | | | **29.9** |

### Step 2: Review Velocity History

Track the last 3-5 sprints to establish a reliable velocity range:

| Sprint | Planned Points | Completed Points | Carry-Over | Notes |
|--------|---------------|------------------|------------|-------|
| Sprint N-4 | 34 | 30 | 4 | Holiday week |
| Sprint N-3 | 38 | 36 | 2 | Stable sprint |
| Sprint N-2 | 40 | 38 | 2 | Good flow |
| Sprint N-1 | 42 | 35 | 7 | Unplanned incident |
| **Average** | **38.5** | **34.75** | **3.75** | |

**Recommended commitment:** Use the average completed points (34-35) as target, not the best sprint.

### Step 3: Define Sprint Goal

### Step 4: Select and Commit to Stories

Prioritize stories in this order:
1. Carry-over stories from previous sprint
2. Stories supporting the sprint goal
3. High-priority bugs and tech debt
4. Other backlog items by priority

### Step 5: Task Breakdown

For each story, break into tasks of 0.5-2 days maximum. If a task exceeds 2 days, decompose further.

## Templates

### Sprint Goal Template

```markdown
## Sprint [N] Goal

**Sprint Duration:** [Start Date] - [End Date]
**Sprint Theme:** [One phrase summarizing the focus]

**Primary Goal:**
[One clear, measurable sentence describing what the team will deliver]

**Success Criteria:**
- [ ] [Specific deliverable or outcome 1]
- [ ] [Specific deliverable or outcome 2]
- [ ] [Specific deliverable or outcome 3]

**Stretch Goals (if capacity allows):**
- [ ] [Nice-to-have item 1]
- [ ] [Nice-to-have item 2]

**Dependencies / Risks:**
- [External dependency or known risk]

**Team Capacity:** [X] story points (based on [Y] available developer-days)
**Committed Points:** [Z] story points
**Buffer:** [N]% under capacity for unplanned work
```

### Sprint Backlog Template

```markdown
## Sprint [N] Backlog

### Committed Stories

| ID | Story Title | Priority | Points | Assignee | Status |
|----|-------------|----------|--------|----------|--------|
| US-101 | [Story title] | P0 | 5 | @dev1 | To Do |
| US-102 | [Story title] | P0 | 3 | @dev2 | To Do |
| US-103 | [Story title] | P1 | 8 | @dev3 | To Do |
| BUG-45 | [Bug title] | P0 | 2 | @dev1 | To Do |
| TD-12 | [Tech debt item] | P2 | 3 | @dev4 | To Do |

**Total Committed:** 21 points
**Team Capacity:** 25 points
**Buffer:** 4 points (16%)

### Stretch Stories

| ID | Story Title | Priority | Points | Notes |
|----|-------------|----------|--------|-------|
| US-104 | [Story title] | P2 | 5 | Pull in if ahead of schedule |

### Carry-Over from Sprint [N-1]

| ID | Story Title | Points | Remaining | Reason |
|----|-------------|--------|-----------|--------|
| US-098 | [Story title] | 8 | 3 | Blocked by API dependency |
```

## Scripts & Tools

### Velocity Calculator Script

```bash
# Calculate average velocity from recent sprints
# Usage: ./scripts/velocity-calc.sh <completed_points_csv>
# Example: ./scripts/velocity-calc.sh "30,36,38,35"

points="$1"
IFS=',' read -ra arr <<< "$points"
sum=0
for p in "${arr[@]}"; do sum=$((sum + p)); done
avg=$((sum / ${#arr[@]}))
echo "Sprints analyzed: ${#arr[@]}"
echo "Average velocity: $avg points/sprint"
echo "Recommended commitment: $((avg * 85 / 100))-$avg points"
```

### Capacity Calculator

```python
# scripts/capacity_calc.py
# Usage: python scripts/capacity_calc.py

team = [
    {"name": "Dev 1", "days": 10, "pto": 0, "oncall": 0, "focus": 0.7},
    {"name": "Dev 2", "days": 10, "pto": 2, "oncall": 0, "focus": 0.7},
]

total = 0
for member in team:
    available = member["days"] - member["pto"] - member["oncall"]
    effective = available * member["focus"]
    total += effective
    print(f"{member['name']}: {effective:.1f} effective days")

print(f"\nTotal team capacity: {total:.1f} effective days")
```

## Best Practices

### Do

- Keep a 15-20% buffer for unplanned work and interruptions
- Use yesterday's weather (past velocity) as the primary planning input
- Break stories larger than 13 points before bringing them into a sprint
- Ensure every story has clear acceptance criteria before commitment
- Assign at least one story per developer to maintain ownership
- Include at least one tech debt item per sprint to prevent accumulation

### Common Anti-Patterns

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| Overcommitting | Team burns out, carry-over increases | Use velocity average, not best sprint |
| No sprint goal | Work feels disconnected, no focus | Always define a single clear theme |
| Skipping estimation | Cannot track velocity or plan | Estimate even if rough; calibrate over time |
| Hero dependency | Single point of failure | Cross-assign stories, pair on complex work |
| Scope creep mid-sprint | Sprint goal at risk | Protect the sprint; new items go to backlog |
| No buffer | Zero slack for surprises | Reserve 15-20% capacity for unplanned work |
| Estimation by seniority | Junior voices excluded | Use planning poker for team consensus |
| Ignoring tech debt | Velocity degrades over time | Allocate 10-20% of capacity to tech debt |

### Sprint Length Guidelines

| Team Maturity | Recommended Length | Reason |
|--------------|-------------------|--------|
| New team / new product | 1 week | Faster feedback loops, quicker course correction |
| Established team | 2 weeks | Balance of predictability and flexibility |
| Stable product, large features | 3 weeks | Allows for larger stories without splitting |
| Maintenance mode | 1-2 weeks | Short cycles for quick bug fixes and patches |
