# Canned Response Library - Reference Guide

## Response Design Principles

### The CLEAR Framework

Every canned response should be evaluated against five principles:

| Principle | Definition | Checklist |
|-----------|-----------|-----------|
| **C**oncise | Shortest path to clarity | No filler words; scannable format; under 150 words for chat |
| **L**oyal to brand voice | Matches company tone | Consistent terminology; approved greetings/closings |
| **E**mpathetic | Acknowledges the customer's situation | Validates feelings before solving; uses "I understand" |
| **A**ctionable | Clear next steps with ownership | States who does what by when; no ambiguity |
| **R**elevant | Tailored to the specific scenario | Addresses the actual issue; personalized with context |

---

## Response Categories Deep Dive

### Greetings

**Purpose**: Set the tone, establish rapport, show the customer they are heard.

**Structure**:
1. Personalized greeting (use name)
2. Acknowledge their reason for contact
3. Set expectation for what happens next

**Variants needed**:
| Variant | When to Use |
|---------|------------|
| Standard welcome | First-time or unknown customer |
| Returning customer | Customer has history (reference it) |
| VIP welcome | Enterprise/premium tier customers |
| Proactive outreach | Agent initiating contact |
| Transfer greeting | Customer transferred from another agent |

**Anti-patterns**:
- "Dear Valued Customer" (impersonal)
- Greeting without acknowledging reason for contact
- Overly long introductions before getting to the point

---

### Troubleshooting

**Purpose**: Guide the customer through diagnostic or resolution steps clearly.

**Structure**:
1. Brief empathy/acknowledgment
2. Numbered steps (max 5 per message)
3. Expected outcome after each step
4. Offer to help if stuck

**Formatting rules**:
- Bold the action in each step
- Include expected result after critical steps
- Break long sequences into multiple messages (5 steps max per message)
- Include screenshots/links where applicable

**Skill-level adaptation**:
| Customer Skill | Language Style | Detail Level |
|---------------|---------------|-------------|
| Technical | Direct, uses product terms | Minimal hand-holding |
| Intermediate | Plain language, some terms | Moderate detail |
| Non-technical | Simple language, no jargon | Step-by-step with visuals |

---

### Resolution Confirmations

**Purpose**: Confirm the issue is fixed, summarize what was done, set expectations.

**Structure**:
1. Confirm resolution
2. Summarize what was done (1-2 sentences)
3. State expected behavior going forward
4. Offer additional help
5. Warm closing

**Key elements**:
- Be specific about what was resolved (not just "your issue")
- If compensation was given, detail it clearly
- If follow-up is needed, state timeline

---

### Apologies

**Purpose**: Acknowledge failure, take responsibility, offer remedy.

**The LAST Framework for Apologies**:
| Step | Description | Example |
|------|-------------|---------|
| **L**isten | Acknowledge what happened | "I understand you experienced..." |
| **A**pologize | Sincere, specific apology | "I sincerely apologize for the disruption to..." |
| **S**olve | State what's being done | "We've identified the cause and..." |
| **T**hank | Thank for patience/feedback | "Thank you for your patience while we resolved this" |

**Escalation levels**:
| Severity | Apology Level | Compensation Consideration |
|----------|-------------|---------------------------|
| Minor inconvenience | Standard empathy | No compensation |
| Service disruption (<1hr) | Formal apology | Consider goodwill gesture |
| Extended outage (1-4hr) | Senior apology + explanation | Service credit |
| Major incident (>4hr) | Executive apology | Significant credit + follow-up |
| Data/security incident | Legal-reviewed apology | Per incident response plan |

---

## Variable System

### Variable Types

| Type | Syntax | Source | Example |
|------|--------|--------|---------|
| Customer field | `{{customer_name}}` | CRM/ticket | "Sarah" |
| System field | `{{ticket_id}}` | Ticketing system | "#TK-12345" |
| Computed field | `{{day_period}}` | System clock | "afternoon" |
| Agent field | `{{agent_name}}` | Agent profile | "Mike" |
| Config field | `{{company_name}}` | Global config | "Acme Inc" |
| Conditional | `{{#if resolved}}...{{/if}}` | Ticket status | (shows/hides block) |

### Variable Resolution Order

1. Check ticket/conversation context
2. Check customer record in CRM
3. Check agent profile
4. Check global configuration
5. If unresolved: flag for manual entry (never send with raw `{{variable}}`)

### Fallback Values

| Variable | Fallback | When Used |
|----------|----------|-----------|
| `{{customer_name}}` | "there" (as in "Hi there") | Name not available |
| `{{day_period}}` | "day" (as in "have a great day") | Time unknown |
| `{{agent_name}}` | "your support team" | Agent unassigned |
| `{{resolution_date}}` | "recently" | Date unclear |

---

## A/B Testing Methodology

### What to Test

| Element | Hypothesis Example | Metric |
|---------|-------------------|--------|
| Opening line | Empathy-first vs. action-first | CSAT score |
| Response length | Short (50 words) vs. medium (100 words) | Resolution rate |
| Tone | Formal vs. conversational | CSAT + response rate |
| Closing style | Question close vs. statement close | Reopen rate |
| Formatting | Numbered steps vs. prose | Customer effort score |

### Test Protocol

1. **Minimum sample**: 200 conversations per variant
2. **Duration**: Minimum 2 weeks (captures weekly patterns)
3. **Assignment**: Random, balanced across agents and channels
4. **Primary metric**: One metric per test (e.g., CSAT)
5. **Secondary metrics**: Monitor but don't optimize for (e.g., handle time)
6. **Statistical significance**: p < 0.05 before declaring winner

### Interpreting Results

| Outcome | Action |
|---------|--------|
| Variant B wins with p < 0.05 | Replace control with variant B |
| No significant difference | Keep control (simpler is better) |
| Variant B wins on primary, loses on secondary | Review trade-offs; may need further testing |
| Variant B wins but small effect (<2%) | Keep control unless at scale the improvement justifies change |

---

## Quality Audit Framework

### Audit Frequency

| Library Size | Audit Frequency | Full vs. Sample |
|-------------|----------------|-----------------|
| < 30 templates | Quarterly | Full audit |
| 30-80 templates | Monthly | 25% sample + all flagged |
| > 80 templates | Monthly | 20% sample + all flagged; consider pruning |

### Audit Scoring Rubric

Each template is scored 1-5 on each dimension:

| Dimension | 1 (Poor) | 3 (Acceptable) | 5 (Excellent) |
|-----------|----------|----------------|---------------|
| **Clarity** | Confusing; multiple interpretations | Clear but wordy | Crystal clear; concise |
| **Empathy** | Cold/robotic | Adequate acknowledgment | Genuinely warm; specific |
| **Accuracy** | Contains errors/outdated info | Correct but generic | Accurate and specific |
| **Actionability** | No clear next step | Next step implied | Explicit, owned next step |
| **Brand voice** | Off-brand; inconsistent | Mostly on-brand | Perfect brand alignment |
| **Personalization** | No variables; generic | Has variables | Context-aware branching |

**Passing score**: Average 3.5+ across all dimensions. Below 3.0 on any single dimension triggers revision.

---

## Library Governance

### Ownership Model

| Role | Responsibilities |
|------|-----------------|
| **Library Owner** (1 person) | Final approval on new templates; quarterly audit lead; performance reporting |
| **Category Owners** (per category) | Draft new templates; update existing; respond to agent feedback |
| **Agents** (all) | Submit template requests; flag issues; provide usage feedback |
| **QA Team** | Audit scoring; A/B test analysis; compliance checking |

### Template Lifecycle

```
Request -> Draft -> Review -> Pilot (10% usage) -> Full Release -> Monitor -> Archive
```

| Stage | Duration | Exit Criteria |
|-------|----------|--------------|
| Request | 1-2 days | Approved by Library Owner |
| Draft | 2-3 days | Written by Category Owner |
| Review | 1-2 days | Passes audit rubric (3.5+ avg) |
| Pilot | 2 weeks | No negative CSAT impact; 10+ uses |
| Full Release | Ongoing | Available to all agents |
| Monitor | Quarterly | Usage count; CSAT correlation |
| Archive | When triggered | Usage < 5/month for 2 quarters |

---

## Channel-Specific Guidelines

### Chat

- Max length: 3-4 short paragraphs or 150 words
- Break long responses into multiple messages
- Use emoji sparingly (1-2 per conversation max, brand-approved only)
- Include clickable links (not raw URLs)

### Email

- Max length: 200-300 words (body, excluding signature)
- Use clear subject line that summarizes action/status
- Include ticket reference number
- Professional signature with contact info

### Phone (Script)

- Use as talking points, not verbatim script
- Include key phrases to hit (for compliance)
- Note pause points for customer response
- Include objection handling branches

### Social Media

- Platform-appropriate tone (slightly more casual)
- Move to DM for details (never share account info publicly)
- Max length: Platform limits (280 chars for X, longer for Facebook)
- Always offer to continue in private channel
