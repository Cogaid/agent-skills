# Retrospective Facilitator Reference

Comprehensive reference for facilitating effective retrospectives, managing action items, and tracking team improvement over time.

## Retro Format Deep Dives

### Start-Stop-Continue

**Best for:** Quick check-ins, new teams, when time is short.

Three simple categories that map directly to actionable changes:

| Column | Question | Action Type |
|--------|----------|-------------|
| **Start** | What should we begin doing? | New experiments, process additions |
| **Stop** | What should we stop doing? | Process removals, anti-pattern elimination |
| **Continue** | What should we keep doing? | Reinforcement, acknowledgment of good practices |

**Facilitation tips:**
- Start with "Continue" to set a positive tone
- Limit to 3-5 items per column
- "Stop" items often feel personal; remind the team to focus on processes, not people

### 4Ls: Liked, Learned, Lacked, Longed For

**Best for:** Balanced reflection that captures both positive and aspirational feedback.

| Quadrant | Focus | Example Items |
|----------|-------|--------------|
| **Liked** | What went well that we want to acknowledge? | Great collaboration on the search feature |
| **Learned** | What new knowledge or insight did we gain? | Learned that the new testing framework cuts test time by 40% |
| **Lacked** | What was missing that hurt us? | Lacked clear design specs for the settings page |
| **Longed For** | What do we wish we had? | Longed for a dedicated QA environment |

**Facilitation tips:**
- "Learned" and "Longed For" often reveal the most actionable items
- Pair "Lacked" items with specific improvements (do not just list complaints)

### Sailboat

**Best for:** Visual teams, when you want a metaphor to make discussion more engaging.

| Element | Metaphor | Maps To |
|---------|----------|---------|
| Island | Destination | Sprint/project goal or vision |
| Wind | Pushing the boat forward | Things helping the team succeed |
| Anchor | Dragging the boat back | Things slowing the team down |
| Rocks | Hidden dangers ahead | Upcoming risks or concerns |

**Facilitation tips:**
- Draw the sailboat on a whiteboard or use a digital template
- Start with the Island (goal) to align the team
- Wind and Anchor are the core discussion; Rocks are forward-looking
- Great for stakeholder-present retros since it is less confrontational

### Mad-Sad-Glad

**Best for:** After tough sprints, when emotional processing is needed.

| Category | Emotion | What It Surfaces |
|----------|---------|-----------------|
| **Mad** | Frustration, anger | Process failures, repeated problems, systemic issues |
| **Sad** | Disappointment, regret | Missed opportunities, team changes, unmet goals |
| **Glad** | Happiness, gratitude | Wins, positive collaboration, growth moments |

**Facilitation tips:**
- Create psychological safety first; this format requires trust
- Validate emotions without trying to "fix" them immediately
- Transition from emotions to actions: "What would reduce the 'Mad' items?"
- End on "Glad" to close positively

### Starfish (More/Less/Keep/Start/Stop)

**Best for:** Mature teams that want more nuance than Start-Stop-Continue.

| Category | Meaning | Action |
|----------|---------|--------|
| **More of** | Good things we should increase | Scale up what works |
| **Less of** | Things we should reduce (but not eliminate) | Dial back without stopping |
| **Keep doing** | Things at the right level | Maintain status quo |
| **Start doing** | New things to try | Experiment with new practices |
| **Stop doing** | Things to eliminate | Remove practices that do not add value |

### Timeline

**Best for:** Long sprints, lots of events, when context matters.

1. Draw a timeline of the sprint on a wall or digital board
2. Mark key events (releases, incidents, meetings, decisions)
3. Team members add sticky notes above (positive) or below (negative) the timeline at the relevant point
4. Walk through chronologically, discussing clusters
5. Identify patterns: did problems cluster around a specific event?

## Psychological Safety

### The Foundation of Effective Retros

Without psychological safety, retros become performative. Team members share only safe observations and the real issues stay hidden.

**Signs of low psychological safety:**
- Only positive feedback is shared
- Same person always raises problems
- Items are vague ("communication could be better")
- Team looks at the manager before speaking
- Silence when asked about problems

**Building psychological safety:**

| Technique | How | Impact |
|-----------|-----|--------|
| Anonymous input | Use tools like Retrium, slido, or anonymous forms | Removes fear of attribution |
| Manager steps back | Manager participates as equal, does not lead | Reduces power dynamic |
| Facilitator rotation | Different person facilitates each retro | Distributes ownership |
| Ground rules | Read them at every retro, not just the first | Normalizes the expectations |
| Follow through | Actually implement action items | Proves that speaking up leads to change |
| Celebrate vulnerability | Thank people who raise difficult topics | Reinforces the behavior |

### The Prime Directive

Read this at the start of every retrospective:

> "Regardless of what we discover, we understand and truly believe that everyone did the best job they could, given what they knew at the time, their skills and abilities, the resources available, and the situation at hand."
> -- Norm Kerth, "Project Retrospectives"

## Action Item Management

### SMART Action Items

Every retro action item should be SMART:

| Element | Bad Example | Good Example |
|---------|-------------|-------------|
| **S**pecific | "Improve testing" | "Add integration tests for the checkout flow" |
| **M**easurable | "Test more" | "Increase test coverage from 72% to 80%" |
| **A**ssignable | "Someone should fix this" | "@alice will implement the solution" |
| **R**ealistic | "Achieve 100% test coverage" | "Add tests for the 3 most critical paths" |
| **T**ime-bound | "Soon" | "By end of Sprint 15 (Apr 28)" |

### Action Item Lifecycle

```
CREATED (in retro) -> TICKETED (within 24h) -> SPRINT BACKLOG (next planning)
       -> IN PROGRESS -> DONE -> VERIFIED (at next retro)
```

**Rules for action items:**
- Maximum 3 per retro (more than 3 rarely get completed)
- Each must have a single owner (not a committee)
- Create a Jira/Linear ticket within 24 hours
- Include in the next sprint backlog
- Review completion status at the start of the next retro

### Tracking Improvement Over Time

Track these metrics across retros to measure improvement:

| Metric | How to Measure | Target |
|--------|---------------|--------|
| Action completion rate | Done / Created per retro | > 70% |
| Repeat themes | Times the same issue is raised | Decreasing |
| Team mood score | Anonymous 1-5 poll at retro end | Stable or improving |
| Participation rate | Attendees / Team size | > 90% |
| Items per person | Total items / Attendees | 2-4 (balanced participation) |

## Icebreaker Ideas

Use a 1-2 minute icebreaker to set the tone:

| Icebreaker | Time | Energy Level |
|-----------|------|-------------|
| "One word to describe this sprint" | 1 min | Low |
| "Rate the sprint 1-5 with your fingers" | 30 sec | Low |
| "What was your highlight this sprint?" | 2 min | Medium |
| "If this sprint were a movie, what would the title be?" | 2 min | High |
| "Two truths and a lie about your sprint" | 3 min | High |
| "Weather report: what's your emotional forecast?" | 1 min | Medium |

## References

- Norm Kerth, "Project Retrospectives: A Handbook for Team Reviews" (2001)
- Esther Derby & Diana Larsen, "Agile Retrospectives: Making Good Teams Great" (2006)
- Amy Edmondson, "The Fearless Organization" (2018) - on psychological safety
- Retromat (retro activity generator): https://retromat.org/
- FunRetrospectives: https://www.funretrospectives.com/
