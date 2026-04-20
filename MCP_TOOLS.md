# MCP Tools for Agent Skills

This document lists Model Context Protocol (MCP) tools that enable AI agents to effectively execute skills in each domain.

## Overview

MCP tools provide agents with the ability to interact with external services, APIs, and platforms. The tools below are organized by domain and mapped to relevant skills.

---

## Customer Support

### Ticketing & Help Desk

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Zendesk** | Enterprise ticketing, knowledge base, chat | ticket-triage, escalation-handler, knowledge-base-writer, live-chat-handler |
| **Freshdesk** | Ticketing, automation, knowledge base | ticket-triage, escalation-handler, knowledge-base-writer |
| **Jira Service Management** | IT service desk, incident management | ticket-triage, escalation-handler, technical-troubleshooter |
| **Intercom** | Live chat, ticketing, customer data | live-chat-handler, ticket-triage, customer-feedback-analyzer |
| **Help Scout** | Shared inbox, knowledge base, chat | ticket-triage, knowledge-base-writer, live-chat-handler |
| **Chatwoot** | Open-source live chat and support | live-chat-handler, ticket-triage |
| **Front** | Shared inbox, collaboration | ticket-triage, escalation-handler |
| **HubSpot Service Hub** | Ticketing, knowledge base, feedback | ticket-triage, knowledge-base-writer, customer-feedback-analyzer |

### Live Chat & Messaging

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Crisp** | Live chat, chatbot, CRM | live-chat-handler |
| **Drift** | Conversational marketing, chat | live-chat-handler |
| **Tawk.to** | Free live chat | live-chat-handler |
| **LiveChat** | Live chat, ticketing | live-chat-handler, ticket-triage |

### Order & Subscription Management

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Stripe** | Payments, subscriptions, billing | refund-processor, subscription-manager, order-status-handler |
| **Chargebee** | Subscription billing, revenue ops | subscription-manager, refund-processor |
| **Recurly** | Subscription management | subscription-manager, refund-processor |
| **Shopify** | E-commerce, orders, inventory | order-status-handler, refund-processor |
| **WooCommerce** | E-commerce orders | order-status-handler, refund-processor |
| **PayPal** | Payments, refunds | refund-processor |

### Shipping & Logistics

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **ShipStation** | Shipping management, tracking | order-status-handler |
| **Shippo** | Shipping API, tracking | order-status-handler |
| **AfterShip** | Shipment tracking | order-status-handler |
| **EasyPost** | Shipping API | order-status-handler |

### Feedback & Surveys

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Typeform** | Surveys, forms | customer-feedback-analyzer |
| **SurveyMonkey** | Surveys, feedback collection | customer-feedback-analyzer |
| **Delighted** | NPS, customer feedback | customer-feedback-analyzer |
| **Hotjar** | Feedback, heatmaps | customer-feedback-analyzer |

### Knowledge & Documentation

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Confluence** | Documentation, knowledge base | knowledge-base-writer, technical-troubleshooter |
| **Notion** | Docs, knowledge management | knowledge-base-writer |
| **GitBook** | Documentation platform | knowledge-base-writer |
| **Slite** | Team knowledge base | knowledge-base-writer |

### Communication

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Slack** | Team messaging, notifications | All customer support skills |
| **Microsoft Teams** | Team collaboration | All customer support skills |
| **Gmail** | Email communication | escalation-handler, ticket-triage |
| **Twilio** | SMS, voice communication | live-chat-handler, order-status-handler |

---

## Sales

### CRM Platforms

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Salesforce** | Enterprise CRM, pipeline management | All sales skills |
| **HubSpot CRM** | CRM, marketing, sales automation | All sales skills |
| **Pipedrive** | Sales pipeline CRM | discovery-call, lead-qualifier, account-manager |
| **Close** | Sales CRM for SMBs | discovery-call, follow-up-sequence, cold-outreach-writer |
| **Copper** | Google-native CRM | lead-qualifier, account-manager |
| **Zoho CRM** | CRM suite | All sales skills |

### Sales Engagement & Outreach

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Apollo.io** | Prospecting, sequences, enrichment | cold-outreach-writer, lead-qualifier, follow-up-sequence |
| **Outreach** | Sales engagement platform | cold-outreach-writer, follow-up-sequence |
| **Salesloft** | Sales engagement, cadences | cold-outreach-writer, follow-up-sequence |
| **Lemlist** | Cold email, personalization | cold-outreach-writer, follow-up-sequence |
| **Reply.io** | Sales automation | cold-outreach-writer, follow-up-sequence |
| **Mailshake** | Email outreach | cold-outreach-writer |
| **Instantly** | Cold email at scale | cold-outreach-writer |

### Lead Intelligence & Enrichment

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **ZoomInfo** | B2B contact database | lead-qualifier, cold-outreach-writer |
| **Clearbit** | Data enrichment | lead-qualifier, cold-outreach-writer |
| **LinkedIn Sales Navigator** | Professional network, prospecting | lead-qualifier, cold-outreach-writer, discovery-call |
| **Lusha** | Contact data | lead-qualifier |
| **Cognism** | B2B data, compliance | lead-qualifier |
| **6sense** | Intent data, ABM | lead-qualifier |

### Scheduling & Meetings

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Calendly** | Meeting scheduling | discovery-call, demo-presenter |
| **Cal.com** | Open-source scheduling | discovery-call, demo-presenter |
| **Chili Piper** | Inbound scheduling, routing | discovery-call, lead-qualifier |
| **SavvyCal** | Scheduling links | discovery-call |

### Proposals & Documents

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **PandaDoc** | Proposals, contracts, e-sign | proposal-writer, negotiation-handler |
| **DocuSign** | E-signatures, contracts | proposal-writer, negotiation-handler |
| **Proposify** | Proposal software | proposal-writer |
| **Qwilr** | Interactive proposals | proposal-writer |
| **Better Proposals** | Proposal builder | proposal-writer |

### Video & Demo

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Loom** | Async video recording | demo-presenter, follow-up-sequence |
| **Vidyard** | Video for sales | demo-presenter |
| **Zoom** | Video meetings | discovery-call, demo-presenter |
| **Google Meet** | Video conferencing | discovery-call, demo-presenter |
| **Demodesk** | Screen sharing, demo platform | demo-presenter |

### Revenue Intelligence

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Gong** | Conversation intelligence | discovery-call, objection-handler, negotiation-handler |
| **Chorus** | Call recording, insights | discovery-call, objection-handler |
| **Clari** | Revenue operations | account-manager, lead-qualifier |

### Communication

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Gmail** | Email | All sales skills |
| **Outlook** | Email, calendar | All sales skills |
| **Slack** | Internal communication | All sales skills |
| **LinkedIn** | Professional messaging | cold-outreach-writer, lead-qualifier |

---

## Personal Assistance

### Calendar & Scheduling

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Google Calendar** | Calendar management | meeting-scheduler, reminder-manager |
| **Outlook Calendar** | Microsoft calendar | meeting-scheduler, reminder-manager |
| **Calendly** | External scheduling | meeting-scheduler |
| **Cal.com** | Open-source scheduling | meeting-scheduler |
| **Reclaim.ai** | Smart calendar management | meeting-scheduler, task-prioritizer |

### Email

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Gmail** | Email management | email-drafting, reminder-manager |
| **Outlook** | Microsoft email | email-drafting, reminder-manager |
| **Superhuman** | Fast email client | email-drafting |
| **Spark** | Smart email | email-drafting |

### Task & Project Management

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Todoist** | Task management | task-prioritizer, reminder-manager |
| **Asana** | Project management | task-prioritizer |
| **Linear** | Issue tracking | task-prioritizer |
| **ClickUp** | All-in-one productivity | task-prioritizer, reminder-manager |
| **Notion** | Notes, tasks, docs | task-prioritizer, document-summarizer |
| **Trello** | Kanban boards | task-prioritizer |
| **Things 3** | Personal task manager | task-prioritizer |

### Notes & Documents

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Notion** | Notes, wikis, docs | document-summarizer, meeting-summarizer, research-assistant |
| **Google Docs** | Document editing | document-summarizer, meeting-summarizer |
| **Obsidian** | Knowledge management | research-assistant, document-summarizer |
| **Evernote** | Note-taking | document-summarizer, research-assistant |
| **Confluence** | Team documentation | document-summarizer |
| **Dropbox Paper** | Collaborative docs | document-summarizer |

### Meeting Tools

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Otter.ai** | Meeting transcription | meeting-summarizer |
| **Fireflies.ai** | Meeting notes, transcription | meeting-summarizer |
| **Grain** | Meeting recording, highlights | meeting-summarizer |
| **tl;dv** | Meeting recorder | meeting-summarizer |
| **Zoom** | Video meetings | meeting-scheduler, meeting-summarizer |
| **Google Meet** | Video conferencing | meeting-scheduler, meeting-summarizer |
| **Microsoft Teams** | Collaboration, meetings | meeting-scheduler, meeting-summarizer |

### Travel

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Google Flights** | Flight search | travel-planner |
| **Kayak** | Travel search | travel-planner |
| **Skyscanner** | Flight comparison | travel-planner |
| **Booking.com** | Hotel booking | travel-planner |
| **Airbnb** | Accommodation | travel-planner |
| **TripIt** | Itinerary management | travel-planner |
| **Google Maps** | Directions, places | travel-planner |
| **Rome2Rio** | Multi-modal travel | travel-planner |

### Finance & Expenses

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Expensify** | Expense management | expense-tracker |
| **QuickBooks** | Accounting | expense-tracker |
| **Xero** | Accounting | expense-tracker |
| **Brex** | Corporate cards, expenses | expense-tracker |
| **Ramp** | Expense management | expense-tracker |
| **Wave** | Free accounting | expense-tracker |

### Research

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Perplexity** | AI research assistant | research-assistant |
| **Google Search** | Web search | research-assistant |
| **Wikipedia** | Encyclopedia | research-assistant |
| **Arxiv** | Academic papers | research-assistant |
| **Semantic Scholar** | Academic search | research-assistant |
| **Pocket** | Save articles | research-assistant |
| **Instapaper** | Read later | research-assistant, document-summarizer |

### Reminders & Automation

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Apple Reminders** | iOS reminders | reminder-manager |
| **Google Tasks** | Task reminders | reminder-manager |
| **Zapier** | Workflow automation | reminder-manager |
| **Make (Integromat)** | Automation | reminder-manager |
| **IFTTT** | Simple automation | reminder-manager |

---

## SEO/Content

### SEO & Analytics

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Ahrefs** | SEO, backlinks, keywords | keyword-research, content-optimizer, blog-post-writer |
| **SEMrush** | SEO suite, competitive analysis | keyword-research, content-optimizer, blog-post-writer |
| **Moz** | SEO tools, domain authority | keyword-research, content-optimizer |
| **Google Search Console** | Search performance | content-optimizer, blog-post-writer |
| **Google Analytics** | Website analytics | content-optimizer, landing-page-writer |
| **Screaming Frog** | Technical SEO crawler | content-optimizer |
| **Ubersuggest** | Keyword research | keyword-research |
| **AnswerThePublic** | Question research | keyword-research, blog-post-writer |

### Content Management

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **WordPress** | CMS, blogging | blog-post-writer, content-optimizer, landing-page-writer |
| **Ghost** | Publishing platform | blog-post-writer |
| **Webflow** | Visual CMS | landing-page-writer, blog-post-writer |
| **Contentful** | Headless CMS | blog-post-writer, product-description-writer |
| **Sanity** | Structured content | blog-post-writer, product-description-writer |
| **Strapi** | Open-source headless CMS | blog-post-writer |
| **Shopify** | E-commerce CMS | product-description-writer |
| **Medium** | Publishing platform | blog-post-writer |

### Writing & Editing

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Grammarly** | Grammar, style checking | All content skills |
| **Hemingway** | Readability | blog-post-writer, landing-page-writer |
| **ProWritingAid** | Writing assistant | All content skills |
| **Google Docs** | Document editing | All content skills |
| **Notion** | Writing, collaboration | All content skills |

### Social Media

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Buffer** | Social scheduling | social-media-repurposer |
| **Hootsuite** | Social management | social-media-repurposer |
| **Later** | Visual social scheduling | social-media-repurposer |
| **Sprout Social** | Social suite | social-media-repurposer |
| **LinkedIn** | Professional posting | social-media-repurposer |
| **Twitter/X** | Microblogging | social-media-repurposer |
| **Facebook/Meta** | Social posting | social-media-repurposer |
| **Instagram** | Visual social | social-media-repurposer |

### Email Marketing

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Mailchimp** | Email marketing | email-newsletter-writer |
| **ConvertKit** | Creator email marketing | email-newsletter-writer |
| **Klaviyo** | E-commerce email | email-newsletter-writer, product-description-writer |
| **Beehiiv** | Newsletter platform | email-newsletter-writer |
| **Substack** | Newsletter publishing | email-newsletter-writer |
| **ActiveCampaign** | Email automation | email-newsletter-writer |
| **SendGrid** | Transactional email | email-newsletter-writer |
| **Constant Contact** | Email marketing | email-newsletter-writer |

### Advertising Platforms

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Google Ads** | Search, display advertising | ad-copy-writer |
| **Meta Ads (Facebook)** | Social advertising | ad-copy-writer |
| **LinkedIn Ads** | B2B advertising | ad-copy-writer |
| **Twitter/X Ads** | Social advertising | ad-copy-writer |
| **TikTok Ads** | Short-form video ads | ad-copy-writer |
| **Microsoft Ads** | Bing advertising | ad-copy-writer |

### Design & Visual

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Canva** | Graphic design | social-media-repurposer, ad-copy-writer |
| **Figma** | Design collaboration | landing-page-writer |
| **Unsplash** | Stock photos | blog-post-writer, social-media-repurposer |
| **Pexels** | Free stock media | blog-post-writer |

### Case Studies & Testimonials

| MCP Tool | Description | Relevant Skills |
|----------|-------------|-----------------|
| **Testimonial.to** | Video testimonials | case-study-writer |
| **G2** | Software reviews | case-study-writer |
| **Capterra** | Software reviews | case-study-writer |
| **TrustRadius** | B2B reviews | case-study-writer |

---

## Cross-Domain Tools

These MCP tools are useful across multiple domains:

### Communication & Collaboration

| MCP Tool | Description |
|----------|-------------|
| **Slack** | Team messaging |
| **Microsoft Teams** | Collaboration suite |
| **Discord** | Community communication |
| **Zoom** | Video conferencing |
| **Google Meet** | Video calls |

### Productivity & Notes

| MCP Tool | Description |
|----------|-------------|
| **Notion** | All-in-one workspace |
| **Google Workspace** | Docs, Sheets, Slides |
| **Microsoft 365** | Office suite |
| **Airtable** | Database/spreadsheet hybrid |

### Automation

| MCP Tool | Description |
|----------|-------------|
| **Zapier** | App integration |
| **Make (Integromat)** | Workflow automation |
| **n8n** | Open-source automation |
| **Pipedream** | Developer workflows |

### Storage & Files

| MCP Tool | Description |
|----------|-------------|
| **Google Drive** | Cloud storage |
| **Dropbox** | File sync |
| **OneDrive** | Microsoft storage |
| **Box** | Enterprise storage |

---

## Priority MCP Tools by Domain

### Customer Support - Essential MCPs
1. **Zendesk** or **Freshdesk** - Ticketing
2. **Stripe** - Payments/Subscriptions
3. **Intercom** or **Chatwoot** - Live chat
4. **Confluence** or **Notion** - Knowledge base
5. **Slack** - Internal communication

### Sales - Essential MCPs
1. **Salesforce** or **HubSpot CRM** - CRM
2. **Apollo.io** or **Outreach** - Sales engagement
3. **LinkedIn Sales Navigator** - Prospecting
4. **Calendly** - Scheduling
5. **PandaDoc** - Proposals

### Personal Assistance - Essential MCPs
1. **Google Calendar** / **Outlook** - Calendar
2. **Gmail** / **Outlook** - Email
3. **Todoist** or **Notion** - Tasks
4. **Otter.ai** - Meeting transcription
5. **Google Maps** - Travel/Location

### SEO/Content - Essential MCPs
1. **Ahrefs** or **SEMrush** - SEO
2. **WordPress** or **Webflow** - CMS
3. **Google Search Console** - Performance
4. **Buffer** or **Hootsuite** - Social
5. **Mailchimp** or **ConvertKit** - Email

---

## Notes

- **Open-source alternatives** are included where available (Chatwoot, Cal.com, n8n, Strapi)
- **Priority** should be given to tools that cover multiple skills within a domain
- **Integration capabilities** between tools should be considered when selecting
- Some tools offer **MCP servers** directly, while others may need custom implementation

---

*This list is not exhaustive and should be updated as new MCP tools become available.*
