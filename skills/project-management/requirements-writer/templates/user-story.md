# User Story: [Story Title]

**ID:** [US-XXX]
**Epic:** [Parent Epic Name]
**Priority:** [Must Have / Should Have / Could Have / Won't Have]
**Points:** [Estimate]
**Author:** [Name]
**Date:** [Date]

---

## Story

As a [type of user],
I want [goal or action],
So that [benefit or value].

---

## Acceptance Criteria

### Scenario 1: [Happy path - descriptive name]

```gherkin
Given [precondition or initial state]
  And [additional context if needed]
When [action or trigger performed by the user]
  And [additional action if needed]
Then [expected outcome]
  And [additional expected outcome]
```

### Scenario 2: [Alternative path - descriptive name]

```gherkin
Given [different precondition]
When [action]
Then [different expected outcome]
```

### Scenario 3: [Error case - descriptive name]

```gherkin
Given [precondition]
When [invalid action or error condition]
Then [error handling: message shown, state preserved, etc.]
  And [system remains in valid state]
```

---

## Additional Criteria (Checklist)

- [ ] [Performance criterion: loads within X seconds]
- [ ] [Accessibility: keyboard navigable, screen reader compatible]
- [ ] [Mobile responsive: works on viewport >= 320px]
- [ ] [Analytics: event tracked for [specific action]]

---

## Design

- **Wireframe/Mockup:** [Link to design file]
- **Interaction notes:** [Key interaction details]

---

## Technical Notes

- [Implementation guidance or constraints, if any]
- [Known technical risks or dependencies]
- [Suggested approach (optional, negotiable)]

---

## Dependencies

| Dependency | Type | Status | Blocker? |
|-----------|------|--------|----------|
| [Dependency] | [Story/API/Design/Data] | [Ready/Pending] | [Yes/No] |

---

## Out of Scope

- [Explicitly state what this story does NOT cover]
- [Future enhancement to handle separately]

---

## INVEST Checklist

- [ ] **I**ndependent: Can be built and deployed independently
- [ ] **N**egotiable: Implementation approach is flexible
- [ ] **V**aluable: Delivers clear value to the user
- [ ] **E**stimable: Team can estimate effort
- [ ] **S**mall: Completable within one sprint
- [ ] **T**estable: QA can verify with concrete tests
