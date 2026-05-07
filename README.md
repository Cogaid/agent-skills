# MakerClaw Agent Skills

A comprehensive collection of AI agent skills for **MakerClaw** - a feature of [Makersfuel](https://makersfuel.com), developed by **Cogaid Solutions Private Limited**.

These skills enable AI agents to perform specialized tasks across 9 domains: Customer Support, Sales, Personal Assistance, SEO/Content, HR & Recruitment, Project Management, Finance & Operations, Legal & Compliance, and Data & Analytics.

## About MakerClaw

MakerClaw is an AI-powered feature within Makersfuel that leverages skills to perform complex, domain-specific tasks with consistency and expertise. Skills are modular instruction sets that teach AI agents how to complete specific workflows.

## Repository Structure

```
agent-skills/
├── MCP_TOOLS.md
├── skills/
│   ├── customer-support/        # Customer support workflows (12 skills)
│   │   ├── ticket-triage/
│   │   ├── escalation-handler/
│   │   ├── knowledge-base-writer/
│   │   ├── customer-feedback-analyzer/
│   │   ├── live-chat-handler/
│   │   ├── refund-processor/
│   │   ├── order-status-handler/
│   │   ├── subscription-manager/
│   │   ├── technical-troubleshooter/
│   │   ├── csat-survey-designer/
│   │   ├── sla-monitor/
│   │   └── canned-response-library/
│   ├── sales/                   # Sales enablement skills (14 skills)
│   │   ├── sales-orchestrator/      # Main routing skill
│   │   ├── sales-prospect/          # 5-agent parallel prospect audit
│   │   ├── sales-research/          # Company research & firmographics
│   │   ├── sales-qualify/           # Lead qualification (BANT + MEDDIC)
│   │   ├── sales-contacts/         # Decision maker intelligence
│   │   ├── sales-outreach/         # Cold outreach sequences
│   │   ├── sales-followup/         # Follow-up sequences
│   │   ├── sales-prep/             # Meeting preparation briefs
│   │   ├── sales-proposal/         # Sales proposal generator
│   │   ├── sales-objections/       # Objection handling playbook
│   │   ├── sales-icp/              # Ideal Customer Profile builder
│   │   ├── sales-competitors/      # Competitive intelligence
│   │   ├── sales-report/           # Pipeline report generator
│   │   └── sales-report-pdf/       # PDF report generator
│   ├── personal-assistance/     # Personal productivity skills (12 skills)
│   │   ├── meeting-scheduler/
│   │   ├── email-drafting/
│   │   ├── task-prioritizer/
│   │   ├── travel-planner/
│   │   ├── research-assistant/
│   │   ├── expense-tracker/
│   │   ├── meeting-summarizer/
│   │   ├── document-summarizer/
│   │   ├── reminder-manager/
│   │   ├── daily-briefing/
│   │   ├── email-organizer/
│   │   └── decision-matrix/
│   ├── seo-content/             # SEO and content skills (12 skills)
│   │   ├── blog-post-writer/
│   │   ├── keyword-research/
│   │   ├── content-optimizer/
│   │   ├── social-media-repurposer/
│   │   ├── landing-page-writer/
│   │   ├── email-newsletter-writer/
│   │   ├── product-description-writer/
│   │   ├── case-study-writer/
│   │   ├── ad-copy-writer/
│   │   ├── seo-audit-reporter/
│   │   ├── content-calendar/
│   │   └── competitor-content-analyzer/
│   ├── hr-recruitment/          # HR and recruitment skills (7 skills)
│   │   ├── job-description-writer/
│   │   ├── resume-screener/
│   │   ├── interview-question-generator/
│   │   ├── offer-letter-writer/
│   │   ├── onboarding-checklist/
│   │   ├── employee-feedback-writer/
│   │   └── exit-interview-analyzer/
│   ├── project-management/      # Project management skills (7 skills)
│   │   ├── sprint-planner/
│   │   ├── standup-summarizer/
│   │   ├── project-status-reporter/
│   │   ├── risk-assessor/
│   │   ├── retrospective-facilitator/
│   │   ├── requirements-writer/
│   │   └── changelog-writer/
│   ├── finance-operations/      # Finance and operations skills (7 skills)
│   │   ├── invoice-generator/
│   │   ├── financial-report-writer/
│   │   ├── budget-planner/
│   │   ├── contract-reviewer/
│   │   ├── sow-writer/
│   │   ├── pricing-strategy/
│   │   └── vendor-evaluator/
│   ├── legal-compliance/        # Legal and compliance skills (5 skills)
│   │   ├── privacy-policy-writer/
│   │   ├── terms-of-service-writer/
│   │   ├── compliance-checker/
│   │   ├── nda-generator/
│   │   └── incident-report-writer/
│   └── data-analytics/          # Data and analytics skills (5 skills)
│       ├── report-generator/
│       ├── survey-creator/
│       ├── dashboard-narrator/
│       ├── competitive-analyst/
│       └── kpi-tracker/
├── README.md
└── LICENSE
```

## Skill Categories

### Customer Support (12 skills)

| Skill | Description |
|-------|-------------|
| `ticket-triage` | Categorize, prioritize, and route support tickets |
| `escalation-handler` | Handle escalated issues with empathy and resolution |
| `knowledge-base-writer` | Create and update help documentation |
| `customer-feedback-analyzer` | Analyze feedback for insights and trends |
| `live-chat-handler` | Handle real-time customer chats with CARE methodology |
| `refund-processor` | Process refund requests efficiently and fairly |
| `order-status-handler` | Handle order inquiries, tracking, and delivery issues |
| `subscription-manager` | Manage subscriptions, renewals, upgrades, and cancellations |
| `technical-troubleshooter` | Diagnose and resolve technical issues systematically |
| `csat-survey-designer` | Design post-interaction satisfaction surveys (CSAT, NPS, CES) |
| `sla-monitor` | Monitor and report SLA compliance with breach alerts |
| `canned-response-library` | Build and manage templated response libraries |

### Sales (14 skills)

| Skill | Description |
|-------|-------------|
| `sales-orchestrator` | Main routing skill that orchestrates all sales sub-skills |
| `sales-prospect` | Full prospect audit with 5 parallel analysis agents |
| `sales-research` | Deep company research across 8 firmographic dimensions |
| `sales-qualify` | Lead qualification using BANT + MEDDIC frameworks |
| `sales-contacts` | Decision maker intelligence and buying committee mapping |
| `sales-outreach` | Personalized 5-email cold outreach sequences with LinkedIn |
| `sales-followup` | Post-engagement follow-up sequences (5 scenarios) |
| `sales-prep` | 11-section meeting preparation briefs with cheat sheet |
| `sales-proposal` | Professional 11-section sales proposals with follow-up |
| `sales-objections` | 15 universal objections with word-for-word response scripts |
| `sales-icp` | Ideal Customer Profile builder with scoring rubric |
| `sales-competitors` | Competitive intelligence and battle card generation |
| `sales-report` | Pipeline report synthesizing all prospect analyses |
| `sales-report-pdf` | Professional PDF reports with charts and color-coded scores |

### Personal Assistance (12 skills)

| Skill | Description |
|-------|-------------|
| `meeting-scheduler` | Schedule and coordinate meetings across time zones |
| `email-drafting` | Draft professional emails for various contexts |
| `task-prioritizer` | Prioritize tasks using Eisenhower matrix and ICE scoring |
| `travel-planner` | Plan and organize travel itineraries |
| `research-assistant` | Conduct research using GATHER methodology |
| `expense-tracker` | Track, categorize, and report expenses |
| `meeting-summarizer` | Create actionable meeting summaries using DACI framework |
| `document-summarizer` | Summarize documents and reports using CORE framework |
| `reminder-manager` | Create and manage reminders and follow-ups |
| `daily-briefing` | Generate personalized daily summaries of tasks and priorities |
| `email-organizer` | Categorize and prioritize inbox with triage workflows |
| `decision-matrix` | Structure complex decisions with weighted criteria |

### SEO/Content (12 skills)

| Skill | Description |
|-------|-------------|
| `blog-post-writer` | Write SEO-optimized blog content with readability checks |
| `keyword-research` | Research, analyze, and prioritize target keywords |
| `content-optimizer` | Audit and optimize existing content for search |
| `social-media-repurposer` | Repurpose long-form content across social platforms |
| `landing-page-writer` | Create high-converting landing page copy using proven frameworks |
| `email-newsletter-writer` | Write engaging email newsletters that drive opens and clicks |
| `product-description-writer` | Write compelling product descriptions using FAB+E framework |
| `case-study-writer` | Create persuasive case studies using SCQA+R framework |
| `ad-copy-writer` | Write high-converting ad copy for digital platforms |
| `seo-audit-reporter` | Run comprehensive SEO audits with prioritized recommendations |
| `content-calendar` | Plan and manage content publishing schedules |
| `competitor-content-analyzer` | Analyze competitor content strategies and find gaps |

### HR & Recruitment (7 skills)

| Skill | Description |
|-------|-------------|
| `job-description-writer` | Write inclusive, compelling job descriptions with SEO |
| `resume-screener` | Screen resumes against job criteria with scoring rubrics |
| `interview-question-generator` | Create role-specific interview questions by competency |
| `offer-letter-writer` | Draft offer letters and compensation packages |
| `onboarding-checklist` | Create 30-60-90 day onboarding plans |
| `employee-feedback-writer` | Write performance reviews using SBI framework |
| `exit-interview-analyzer` | Analyze exit interview data for retention insights |

### Project Management (7 skills)

| Skill | Description |
|-------|-------------|
| `sprint-planner` | Plan sprint goals, capacity, and story points |
| `standup-summarizer` | Summarize daily standups into async updates |
| `project-status-reporter` | Generate RAG status reports for stakeholders |
| `risk-assessor` | Identify and assess risks with probability-impact matrix |
| `retrospective-facilitator` | Facilitate and summarize sprint retrospectives |
| `requirements-writer` | Write PRDs, user stories, and acceptance criteria |
| `changelog-writer` | Generate changelogs and release notes from commits |

### Finance & Operations (7 skills)

| Skill | Description |
|-------|-------------|
| `invoice-generator` | Create professional invoices with payment terms |
| `financial-report-writer` | Write financial summaries and variance reports |
| `budget-planner` | Create and manage budgets with forecasting |
| `contract-reviewer` | Review contracts for key terms and risks |
| `sow-writer` | Write statements of work for service engagements |
| `pricing-strategy` | Analyze and recommend pricing models |
| `vendor-evaluator` | Compare and evaluate vendors with weighted scoring |

### Legal & Compliance (5 skills)

| Skill | Description |
|-------|-------------|
| `privacy-policy-writer` | Write GDPR/CCPA compliant privacy policies |
| `terms-of-service-writer` | Draft terms of service documents |
| `compliance-checker` | Check content against regulatory requirements |
| `nda-generator` | Generate non-disclosure agreements |
| `incident-report-writer` | Write incident reports for security and compliance |

### Data & Analytics (5 skills)

| Skill | Description |
|-------|-------------|
| `report-generator` | Create data-driven reports with actionable insights |
| `survey-creator` | Design effective surveys and questionnaires |
| `dashboard-narrator` | Narrate dashboard data into written insights |
| `competitive-analyst` | Analyze competitors using Porter's Five Forces and SWOT |
| `kpi-tracker` | Define and track KPIs with traffic light scoring |

## Skill Structure

Each skill follows a consistent structure:

```
skill-name/
├── SKILL.md           # Main skill definition with YAML frontmatter
├── reference.md       # Detailed reference documentation
├── templates/         # Reusable templates and formats
│   └── *.md
└── scripts/           # Python utility scripts
    └── *.py
```

### SKILL.md Format

```markdown
---
name: skill-name
description: Clear description of what this skill does and trigger phrases
metadata:
  version: 1.0.0
  category: domain-name
---

# Skill Name

[Skill content with workflow, quick reference, and script usage]
```

## Usage

### With MakerClaw

Skills are automatically loaded by MakerClaw when relevant tasks are detected. The AI agent will:

1. Identify the appropriate skill based on user intent
2. Load the skill's instructions and templates
3. Execute the workflow with available utility scripts
4. Deliver consistent, high-quality output

### Standalone Usage

Skills can also be used independently:

```bash
# Run a utility script
python skills/seo-content/blog-post-writer/scripts/seo_check.py article.md

# Use templates as reference
cat skills/sales/proposal-writer/templates/executive-summary.md
```

## MCP Tools

For AI agents to effectively execute these skills, they need access to external services via MCP (Model Context Protocol) tools.

See **[MCP_TOOLS.md](MCP_TOOLS.md)** for a comprehensive list of recommended MCP tools organized by domain, including:

| Domain | Key MCP Tools |
|--------|---------------|
| Customer Support | Zendesk, Freshdesk, Stripe, Intercom, Chatwoot |
| Sales | Salesforce, HubSpot, Apollo.io, LinkedIn, PandaDoc |
| Personal Assistance | Google Calendar, Gmail, Todoist, Otter.ai |
| SEO/Content | Ahrefs, SEMrush, WordPress, Buffer, Mailchimp |
| HR & Recruitment | Greenhouse, Lever, BambooHR, LinkedIn Recruiter |
| Project Management | Jira, Linear, Asana, Notion, ClickUp |
| Finance & Operations | QuickBooks, Xero, Stripe, DocuSign, Brex |
| Legal & Compliance | DocuSign, Ironclad, OneTrust, Vanta |
| Data & Analytics | Google Analytics, Mixpanel, Tableau, Looker |

## Acknowledgments & Attributions

### Content Generation

This repository was generated with assistance from **Claude** (Anthropic's AI assistant). All content, templates, and scripts were created specifically for this project.

### Inspirations & References

The skills in this repository incorporate well-established industry frameworks and methodologies:

| Framework/Methodology | Source | Used In |
|----------------------|--------|---------|
| **BANT Qualification** | IBM (1960s) | `sales-qualify` |
| **MEDDIC/MEDDPICC** | PTC/Jack Napoli | `sales-qualify` |
| **Feel-Felt-Found** | Sales Methodology | `sales-objections` |
| **Acknowledge-Bridge-Close** | Sales Methodology | `sales-objections` |
| **ICE Scoring** | Sean Ellis | `task-prioritizer` |
| **Eisenhower Matrix** | Dwight D. Eisenhower | `task-prioritizer` |
| **Flesch-Kincaid Readability** | Rudolf Flesch & J. Peter Kincaid | `readability.py`, `content_audit.py` |
| **E-E-A-T Guidelines** | Google Search Quality Rater Guidelines | `blog-post-writer`, `content-optimizer` |
| **CARE Methodology** | Customer Service Industry Standard | `live-chat-handler` |
| **AIDA-P Outreach** | Sales Copywriting Standard | `sales-outreach` |
| **GATHER Method** | Research Best Practices | `research-assistant` |
| **AIDA/PAS Copywriting** | Marketing Copywriting Standards | `landing-page-writer`, `ad-copy-writer`, `sales-proposal` |
| **CAN-SPAM/GDPR** | Email Marketing Compliance | `email-newsletter-writer` |
| **CRAAP Test** | California State University | `research-assistant` |
| **SAVE Framework** | Customer Retention Methodology | `subscription-manager` |
| **ISOLATE Method** | Technical Support Best Practices | `technical-troubleshooter` |
| **DACI Framework** | Decision-Making Framework | `meeting-summarizer` |
| **CORE Framework** | Document Analysis Method | `document-summarizer` |
| **FAB+E Framework** | Product Marketing | `product-description-writer` |
| **SCQA+R Framework** | Strategic Communication | `case-study-writer` |
| **SBI Framework** | Center for Creative Leadership | `employee-feedback-writer` |
| **STAR Method** | Behavioral Interview Standard | `interview-question-generator` |
| **30-60-90 Day Plan** | Onboarding Best Practices | `onboarding-checklist` |
| **RAG Status** | Project Management Standard | `project-status-reporter` |
| **MoSCoW Prioritization** | Dai Clegg / Oracle | `requirements-writer` |
| **Keep a Changelog** | Olivier Lacan | `changelog-writer` |
| **Semantic Versioning** | Tom Preston-Werner | `changelog-writer` |
| **Start-Stop-Continue** | Agile Retrospective Practice | `retrospective-facilitator` |
| **Porter's Five Forces** | Michael Porter | `competitive-analyst`, `pricing-strategy` |
| **SWOT Analysis** | Albert Humphrey | `competitive-analyst` |
| **SMART Criteria** | George T. Doran | `kpi-tracker` |
| **RAPID Framework** | Bain & Company | `decision-matrix` |
| **Inbox Zero** | Merlin Mann | `email-organizer` |
| **BRUSO Framework** | Survey Design Best Practices | `survey-creator` |

### Skill Structure Pattern

The skill structure (SKILL.md with YAML frontmatter, progressive disclosure pattern) is inspired by:

- [Anthropic's Claude Code Skills Documentation](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Agent Skills Standard](http://agentskills.io)

## Contributing

1. Fork this repository
2. Create your skill in the appropriate category
3. Follow the existing skill structure
4. Ensure scripts have proper documentation
5. Submit a pull request

## License

MIT License - See [LICENSE](LICENSE) for details.

Copyright (c) 2025 Cogaid Solutions Private Limited

---

## About Cogaid Solutions

**Cogaid Solutions Private Limited** is the company behind Makersfuel and MakerClaw.

- **Product**: [Makersfuel](https://makersfuel.com)
- **Feature**: MakerClaw (AI Agent Skills)

## Support

For questions or support regarding these skills:

- Open an issue in this repository
- Contact Cogaid Solutions through [Makersfuel](https://makersfuel.com)

---

*Built with ❤️ by Cogaid Solutions Private Limited*
