---
name: canned-response-library
description: Build and manage a library of templated customer support responses. Use when the user mentions "canned response," "templated reply," "response template," "macro," "saved reply," "quick response," "response library," "standard reply," "boilerplate response," "pre-written response," or "response management."
metadata:
  version: 1.0.0
  category: customer-support
---

# Canned Response Library

Build, organize, and maintain a library of high-quality templated responses for consistent and efficient customer communication.

## Purpose

Create a centralized response library that ensures consistency across agents, reduces response time, and maintains quality standards while allowing personalization. Covers response categories, writing guidelines, quality auditing, and A/B testing.

## Quick Reference

### Response Categories

| Category | Use Case | Personalization Level | Typical Length |
|----------|----------|----------------------|----------------|
| **Greeting** | Opening a conversation | High - use name, context | 2-3 sentences |
| **Acknowledgment** | Confirming receipt of issue | Medium - reference issue | 1-2 sentences |
| **Troubleshooting** | Step-by-step guidance | Medium - adapt to skill level | 5-10 steps |
| **Status Update** | Progress on open tickets | High - specific details | 2-4 sentences |
| **Escalation Notice** | Handing off to specialist | Medium - set expectations | 3-4 sentences |
| **Resolution** | Confirming issue resolved | High - summarize what was done | 3-5 sentences |
| **Follow-Up** | Post-resolution check-in | High - reference resolution | 2-3 sentences |
| **Closing** | Ending the conversation | Medium - warm close | 2-3 sentences |
| **Apology** | Service failure response | High - specific acknowledgment | 3-5 sentences |
| **Policy Explanation** | Explaining rules/limits | Low - standard language | 3-6 sentences |

### Writing Guidelines

| Principle | Do | Don't |
|-----------|----|----|
| **Tone** | Warm, professional, empathetic | Robotic, overly casual, dismissive |
| **Length** | Concise, scannable | Wall of text, single-word answers |
| **Personalization** | Use customer name, reference context | "Dear Valued Customer" |
| **Action clarity** | Clear next steps with ownership | Vague promises, passive voice |
| **Empathy** | Acknowledge feelings first | Jump straight to solution |
| **Jargon** | Plain language, explain terms | Technical acronyms without context |
| **Formatting** | Numbered steps, bold key info | Dense paragraphs for instructions |

## Workflow

### Response Library Management Checklist

```
Library Management:
- [ ] Audit existing responses quarterly
- [ ] Remove outdated or low-performing responses
- [ ] Update responses for new product features
- [ ] Review tone consistency across all templates
- [ ] Test variable placeholders are working
- [ ] Validate links and references in templates
- [ ] Collect agent feedback on template usability
- [ ] Run A/B tests on top 10 most-used responses
- [ ] Update categorization and tags
- [ ] Train new agents on library usage
```

### Template Structure

Every canned response must follow this structure:

```
RESPONSE TEMPLATE
ID: {{category}}-{{number}}
Name: {{descriptive_name}}
Category: {{category}}
Tags: {{tag1}}, {{tag2}}, {{tag3}}
Channel: {{all | email | chat | phone_script}}
Tone: {{formal | friendly | empathetic | neutral}}
Last Updated: {{date}}
Owner: {{team_or_person}}
Performance: {{usage_count}} uses | {{csat_score}} avg CSAT

---
SUBJECT (if email): {{subject_line}}

BODY:
{{response_text_with_variables}}

INTERNAL NOTES:
{{when_to_use}}
{{when_not_to_use}}
{{common_variations}}
```

## Templates

### Greeting Templates

**GREET-001: Standard Welcome**
```
Hi {{customer_name}},

Thank you for reaching out to {{company_name}} support! My name is {{agent_name}}, and I'll be helping you today.

I've reviewed your message about {{issue_summary}}. Let me look into this for you right away.
```

**GREET-002: Returning Customer Welcome**
```
Hi {{customer_name}},

Welcome back! I can see you've been with us since {{join_date}} — thank you for your continued trust in {{company_name}}.

I see you're reaching out about {{issue_summary}}. Let me take a look at this for you.
```

### Troubleshooting Templates

**TRBL-001: Step-by-Step Instructions**
```
Hi {{customer_name}},

I'd like to walk you through a few steps to resolve this:

1. **{{step_1_action}}**
   {{step_1_detail}}

2. **{{step_2_action}}**
   {{step_2_detail}}

3. **{{step_3_action}}**
   {{step_3_detail}}

After completing these steps, please let me know if the issue is resolved. If you run into any trouble at any step, I'm right here to help.
```

**TRBL-002: Request Diagnostic Information**
```
Hi {{customer_name}},

To help me diagnose this issue more quickly, could you please share the following:

- **Browser/App version**: (e.g., Chrome 120, iOS app 3.2)
- **Operating system**: (e.g., Windows 11, macOS Sonoma)
- **Error message**: (screenshot or exact text if possible)
- **When it started**: (approximate date/time)
- **Frequency**: (every time, intermittent, one-time)

This information will help me pinpoint the cause and get you a solution faster.
```

### Resolution Templates

**RSLV-001: Issue Resolved**
```
Hi {{customer_name}},

Great news — the issue with {{issue_summary}} has been resolved!

Here's what we did:
- {{action_taken}}

You should now be able to {{expected_outcome}}. Please give it a try and let me know if everything is working as expected.

If you need anything else, don't hesitate to reach out. We're always happy to help!
```

**RSLV-002: Issue Resolved with Compensation**
```
Hi {{customer_name}},

I'm pleased to let you know that {{issue_summary}} has been fully resolved.

I understand this caused {{impact_description}}, and I sincerely apologize for the inconvenience. As a gesture of goodwill, I've applied {{compensation_details}} to your account.

{{compensation_specifics}}

Is there anything else I can help you with today?
```

### Follow-Up Templates

**FLUP-001: Post-Resolution Check-In**
```
Hi {{customer_name}},

I wanted to follow up on the {{issue_summary}} issue we resolved on {{resolution_date}}.

Is everything still working well on your end? If you've noticed any further issues or have additional questions, please don't hesitate to reply to this message.

Thank you for your patience, and have a wonderful {{day_period}}!
```

### Closing Templates

**CLOS-001: Standard Close**
```
Is there anything else I can help you with today? If not, I hope you have a wonderful {{day_period}}!

If you need help in the future, we're always just a message away. Thank you for choosing {{company_name}}!
```

**CLOS-002: Close with Survey**
```
I'm glad I could help! Before I close out this conversation, would you mind taking a quick 30-second survey about your experience? Your feedback helps us improve.

[Survey Link: {{survey_url}}]

Thank you, {{customer_name}}, and have a great {{day_period}}!
```

### Apology Templates

**APOL-001: Service Disruption Apology**
```
Hi {{customer_name}},

I sincerely apologize for the disruption you experienced with {{service_name}}. I understand how frustrating it must be when {{impact_on_customer}}, and this is not the experience we want for you.

Our team has identified the cause as {{root_cause}}, and we've {{corrective_action}} to prevent this from happening again.

{{compensation_if_applicable}}

Thank you for your patience and understanding.
```

## Variable Placeholders Reference

| Variable | Description | Source | Example |
|----------|-------------|--------|---------|
| `{{customer_name}}` | Customer's first name | CRM | "Sarah" |
| `{{agent_name}}` | Agent's display name | Agent profile | "Mike" |
| `{{company_name}}` | Company name | Config | "Acme Inc" |
| `{{issue_summary}}` | Brief issue description | Ticket | "login errors" |
| `{{ticket_id}}` | Ticket reference number | System | "#12345" |
| `{{resolution_date}}` | Date issue was resolved | Ticket | "March 15" |
| `{{day_period}}` | Time-appropriate greeting | System clock | "afternoon" |
| `{{join_date}}` | Customer's start date | CRM | "June 2023" |
| `{{survey_url}}` | Post-interaction survey | Config | URL |

## A/B Testing Framework

### Test Setup

```
A/B TEST PLAN
Test Name: {{test_name}}
Template Being Tested: {{template_id}}
Hypothesis: {{hypothesis}}
Metric: {{primary_metric}} (e.g., CSAT, resolution rate, reply rate)
Duration: {{duration}} (minimum 2 weeks or 200 responses per variant)
Split: 50/50 random assignment

VARIANT A (Control): {{current_template}}
VARIANT B (Test): {{modified_template}}

CHANGE BEING TESTED:
- {{specific_change}} (e.g., shorter opening, different tone, added empathy)

SUCCESS CRITERIA:
- Variant B must achieve {{threshold}}% improvement in {{metric}}
- Statistical significance: p < 0.05
- No degradation in secondary metrics
```

## Quality Audit Checklist

```
Response Quality Audit (run quarterly):
- [ ] Tone matches brand voice guidelines
- [ ] Grammar and spelling are correct
- [ ] All variable placeholders resolve correctly
- [ ] No broken links or outdated references
- [ ] Response addresses the actual issue (not generic)
- [ ] Personalization elements are present
- [ ] Next steps are clear and actionable
- [ ] Response length is appropriate for channel
- [ ] Empathy statement included where appropriate
- [ ] Closing includes clear call-to-action
- [ ] No internal jargon or unexplained acronyms
- [ ] Template has been used 10+ times (else archive)
- [ ] CSAT score for this template is above team average
```

## Library Organization

```
Response Library Structure:
├── greetings/
│   ├── GREET-001-standard-welcome
│   ├── GREET-002-returning-customer
│   └── GREET-003-vip-welcome
├── troubleshooting/
│   ├── TRBL-001-step-by-step
│   ├── TRBL-002-request-diagnostics
│   └── TRBL-003-known-issue
├── resolution/
│   ├── RSLV-001-issue-resolved
│   ├── RSLV-002-resolved-with-comp
│   └── RSLV-003-partial-resolution
├── follow-up/
│   ├── FLUP-001-post-resolution
│   └── FLUP-002-no-response-check
├── closing/
│   ├── CLOS-001-standard-close
│   └── CLOS-002-close-with-survey
├── apology/
│   ├── APOL-001-service-disruption
│   └── APOL-002-billing-error
└── policy/
    ├── PLCY-001-refund-policy
    └── PLCY-002-account-security
```

## Scripts & Tools

**search_responses.py**: Find the right template for a situation
```bash
python scripts/search_responses.py --category troubleshooting --tags "login,password"
# Output: Matching templates ranked by relevance and usage
```

**audit_library.py**: Run quality audit on all templates
```bash
python scripts/audit_library.py --check-links --check-variables --report
# Output: Audit report with issues flagged per template
```

**ab_test_report.py**: Analyze A/B test results
```bash
python scripts/ab_test_report.py --test-id ABT-042 --metric csat
# Output: Statistical analysis with winner recommendation
```

## Best Practices

1. **Personalize always** - Never send a template without filling in all variables
2. **Read before sending** - Review the full response in context of the conversation
3. **Update proactively** - When products change, update templates immediately
4. **Tag thoroughly** - Good tagging makes templates findable under pressure
5. **Archive, don't delete** - Keep old templates for reference and compliance
6. **Limit library size** - 50-80 active templates per team; more causes confusion
7. **Measure performance** - Track CSAT per template to find winners and losers
8. **Empower agents** - Templates are starting points, not scripts to read verbatim

## Related Skills

- Survey after response: `csat-survey-designer`
- Escalation responses: `escalation-handler`
- Knowledge base content: `knowledge-base-writer`
