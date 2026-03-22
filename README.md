# MakerClaw Agent Skills

A comprehensive collection of AI agent skills for **MakerClaw** - a feature of [Makersfuel](https://makersfuel.com), developed by **Cogaid Solutions Private Limited**.

These skills enable AI agents to perform specialized tasks across Customer Support, Sales, Personal Assistance, and SEO/Content domains.

## About MakerClaw

MakerClaw is an AI-powered feature within Makersfuel that leverages skills to perform complex, domain-specific tasks with consistency and expertise. Skills are modular instruction sets that teach AI agents how to complete specific workflows.

## Repository Structure

```
agent-skills/
├── skills/
│   ├── customer-support/     # Customer support workflows
│   │   ├── ticket-triage/
│   │   ├── escalation-handler/
│   │   ├── knowledge-base-writer/
│   │   └── customer-feedback-analyzer/
│   ├── sales/                # Sales enablement skills
│   │   ├── discovery-call/
│   │   ├── objection-handler/
│   │   ├── proposal-writer/
│   │   └── lead-qualifier/
│   ├── personal-assistance/  # Personal productivity skills
│   │   ├── meeting-scheduler/
│   │   ├── email-drafting/
│   │   ├── task-prioritizer/
│   │   └── travel-planner/
│   └── seo-content/          # SEO and content skills
│       ├── blog-post-writer/
│       ├── keyword-research/
│       ├── content-optimizer/
│       └── social-media-repurposer/
├── README.md
└── LICENSE
```

## Skill Categories

### Customer Support (4 skills)

| Skill | Description |
|-------|-------------|
| `ticket-triage` | Categorize, prioritize, and route support tickets |
| `escalation-handler` | Handle escalated issues with empathy and resolution |
| `knowledge-base-writer` | Create and update help documentation |
| `customer-feedback-analyzer` | Analyze feedback for insights and trends |

### Sales (4 skills)

| Skill | Description |
|-------|-------------|
| `discovery-call` | Conduct effective discovery conversations using SPIN methodology |
| `objection-handler` | Address and overcome sales objections using LAER framework |
| `proposal-writer` | Create compelling, data-driven sales proposals |
| `lead-qualifier` | Qualify leads using BANT/MEDDIC/ICE frameworks |

### Personal Assistance (4 skills)

| Skill | Description |
|-------|-------------|
| `meeting-scheduler` | Schedule and coordinate meetings across time zones |
| `email-drafting` | Draft professional emails for various contexts |
| `task-prioritizer` | Prioritize tasks using Eisenhower matrix and ICE scoring |
| `travel-planner` | Plan and organize travel itineraries |

### SEO/Content (4 skills)

| Skill | Description |
|-------|-------------|
| `blog-post-writer` | Write SEO-optimized blog content with readability checks |
| `keyword-research` | Research, analyze, and prioritize target keywords |
| `content-optimizer` | Audit and optimize existing content for search |
| `social-media-repurposer` | Repurpose long-form content across social platforms |

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

## Acknowledgments & Attributions

### Content Generation

This repository was generated with assistance from **Claude** (Anthropic's AI assistant). All content, templates, and scripts were created specifically for this project.

### Inspirations & References

The skills in this repository incorporate well-established industry frameworks and methodologies:

| Framework/Methodology | Source | Used In |
|----------------------|--------|---------|
| **SPIN Selling** | Neil Rackham | `discovery-call` |
| **LAER Framework** | Carew International | `objection-handler` |
| **BANT Qualification** | IBM (1960s) | `lead-qualifier` |
| **MEDDIC/MEDDPICC** | PTC/Jack Napoli | `lead-qualifier` |
| **ICE Scoring** | Sean Ellis | `lead-qualifier`, `task-prioritizer` |
| **Eisenhower Matrix** | Dwight D. Eisenhower | `task-prioritizer` |
| **Flesch-Kincaid Readability** | Rudolf Flesch & J. Peter Kincaid | `readability.py`, `content_audit.py` |
| **E-E-A-T Guidelines** | Google Search Quality Rater Guidelines | `blog-post-writer`, `content-optimizer` |

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
