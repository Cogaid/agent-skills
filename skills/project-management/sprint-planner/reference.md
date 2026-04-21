# Sprint Planner Reference

Comprehensive reference for sprint planning ceremonies, estimation techniques, and capacity management in agile teams.

## Estimation Frameworks

### Planning Poker

Planning poker is the most common estimation technique for agile teams. The process ensures team consensus on story complexity.

**How it works:**

1. Product Owner reads the user story and acceptance criteria
2. Team members ask clarifying questions
3. Each member privately selects a card from the Fibonacci-like sequence (1, 2, 3, 5, 8, 13, 21)
4. All cards are revealed simultaneously
5. Highest and lowest estimators explain their reasoning
6. Team discusses and re-votes until consensus is reached (within one step)

**Tips for effective planning poker:**

- Use a reference story (a well-understood 3-point story) as a baseline
- If estimates differ by more than 2 steps (e.g., 3 vs 13), discussion is mandatory
- Timeboxing: spend no more than 5 minutes per story; if no consensus, defer to offline grooming
- Include QA effort in the estimate, not just development
- Avoid anchoring: do not let senior members reveal estimates first

### T-Shirt Sizing

An alternative to story points for teams that find numbers contentious. Use for roadmap-level estimation where precision is less critical.

| Size | Story Points Equivalent | Typical Duration | When to Use |
|------|------------------------|------------------|-------------|
| XS | 1 | < 2 hours | Config changes, copy updates |
| S | 2-3 | 2 hours - 1 day | Simple features, small bug fixes |
| M | 5 | 1-2 days | Standard feature with tests |
| L | 8 | 2-4 days | Complex feature, integration work |
| XL | 13 | 4-7 days | Large feature, significant unknowns |
| XXL | 21+ | > 1 week | Epic-level; must be broken down |

### Affinity Estimation

Fast estimation for large backlogs (20+ stories). Best used during backlog grooming sessions.

1. Lay out stories on a table or board (no discussion yet)
2. Team members silently place stories in relative order (smallest to largest)
3. Any member can move a story; if moved back and forth, flag for discussion
4. Once stable, draw bucket boundaries for point values
5. Discuss only the stories near bucket boundaries

**When to use:** Initial estimation of a new backlog, quarterly planning, or when you need rough estimates for 50+ stories in under an hour.

## Capacity Planning Deep Dive

### Focus Factor Benchmarks

The focus factor represents the percentage of a developer's time spent on sprint work (as opposed to meetings, email, Slack, unplanned interruptions).

| Team Situation | Typical Focus Factor | Notes |
|---------------|---------------------|-------|
| Dedicated team, mature process | 0.75 - 0.85 | Best case for experienced teams |
| Standard team | 0.65 - 0.75 | Most common range |
| Team with on-call rotation | 0.50 - 0.65 | On-call days are low-productivity |
| New team, forming stage | 0.50 - 0.60 | Onboarding, process learning |
| Team supporting production | 0.40 - 0.55 | Interrupt-driven support work |

### Adjusting for Sprint Events

Subtract sprint ceremony time from available capacity:

| Ceremony | Typical Duration (2-week sprint) | Per Person Cost |
|----------|--------------------------------|-----------------|
| Sprint Planning | 2-4 hours | 0.25-0.5 days |
| Daily Standup | 15 min x 10 days = 2.5 hours | 0.3 days |
| Sprint Review/Demo | 1-2 hours | 0.125-0.25 days |
| Retrospective | 1-1.5 hours | 0.125-0.2 days |
| Backlog Grooming | 1-2 hours | 0.125-0.25 days |
| **Total** | **7-12 hours** | **~1-1.5 days** |

### Velocity Stabilization

Velocity typically stabilizes after 3-5 sprints for a team with consistent membership. Use these guidelines:

| Sprint Count | Velocity Reliability | Recommendation |
|-------------|---------------------|----------------|
| 1 sprint | Very low | Use capacity-based planning only |
| 2-3 sprints | Low | Use conservative estimate (lowest sprint) |
| 4-5 sprints | Moderate | Use average of last 3 sprints |
| 6+ sprints | High | Use rolling average, trimming outliers |

**Velocity disruptors** (events that invalidate velocity history):
- Team member added or removed
- Significant technology change
- Major process change (e.g., switching from Kanban to Scrum)
- Long holiday or vacation period

When a disruptor occurs, reset velocity tracking and use capacity-based planning for 2-3 sprints.

## Sprint Goal Framework

### SMART Sprint Goals

Sprint goals should follow the SMART framework:

| Element | Description | Example |
|---------|-------------|---------|
| **S**pecific | Clear and unambiguous | "Complete checkout flow" not "Work on payments" |
| **M**easurable | Observable outcome | "Users can complete a purchase end-to-end" |
| **A**chievable | Realistic given capacity | Fits within team velocity |
| **R**elevant | Aligned to product strategy | Supports Q2 revenue target |
| **T**ime-bound | Achievable within the sprint | Deliverable by sprint end |

### Sprint Goal Anti-Patterns

| Anti-Pattern | Example | Better Alternative |
|-------------|---------|-------------------|
| Too vague | "Make progress on the app" | "Ship the user registration flow" |
| Too many goals | 5 separate objectives | 1 primary goal, 1-2 stretch goals |
| Not a goal, just a list | "Complete US-101, US-102, US-103" | "Enable users to search and filter products" |
| Not achievable | "Rewrite the entire backend" | "Migrate the auth module to the new framework" |
| Not valuable | "Increase test coverage to 90%" | "Reduce checkout errors by adding validation" |

## Backlog Refinement

### Definition of Ready (DoR)

A story is ready for sprint planning when it meets these criteria:

- [ ] User story follows the "As a / I want / So that" format
- [ ] Acceptance criteria are written (Given/When/Then or checklist)
- [ ] Story is estimated by the team
- [ ] Dependencies are identified and resolved (or plan exists)
- [ ] Design/UX assets are available (if applicable)
- [ ] Story fits within a single sprint (< 13 points)
- [ ] Product Owner can answer questions about the story

### Story Splitting Techniques

When a story is too large (> 13 points), split it using one of these strategies:

| Technique | Description | Example |
|-----------|-------------|---------|
| **By workflow step** | Split along process steps | "Create order" vs "Pay for order" vs "Confirm order" |
| **By business rule** | Separate simple from complex rules | "Calculate tax (domestic)" vs "Calculate tax (international)" |
| **By data variation** | Handle one data type at a time | "Import CSV" vs "Import Excel" vs "Import JSON" |
| **By interface** | Split by UI/API/batch | "Search via UI" vs "Search via API" |
| **By operation** | CRUD operations separately | "Create user" vs "Edit user" vs "Delete user" |
| **By performance** | Make it work, then make it fast | "Search returns results" vs "Search returns in < 200ms" |
| **Spike + implementation** | Research first, build second | "Evaluate payment gateways" vs "Integrate Stripe" |

## References

- Scrum Guide (2020): https://scrumguides.org/
- Mike Cohn, "Agile Estimating and Planning" (2005)
- Mountain Goat Software - Planning Poker: https://www.mountaingoatsoftware.com/agile/planning-poker
- SAFe Iteration Planning: https://scaledagileframework.com/iteration-planning/
