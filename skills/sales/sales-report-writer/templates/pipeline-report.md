# Pipeline Report Template

## Report Header

| Field | Value |
|-------|-------|
| **Report Period** | {{period}} |
| **Generated** | {{date}} |
| **Prepared By** | {{author}} |
| **Distribution** | {{audience}} |

---

## Pipeline Summary

| Metric | Value | vs. Prior Period | vs. Target |
|--------|-------|-----------------|------------|
| **Total Pipeline Value** | ${{total_value}} | {{delta}} | {{status}} |
| **Weighted Pipeline** | ${{weighted_value}} | {{delta}} | {{status}} |
| **Number of Opportunities** | {{opp_count}} | {{delta}} | {{status}} |
| **Average Deal Size** | ${{avg_deal}} | {{delta}} | {{status}} |
| **Pipeline Coverage** | {{coverage}}x quota | {{delta}} | {{status}} |
| **Median Deal Size** | ${{median_deal}} | {{delta}} | -- |

---

## Pipeline by Stage

| Stage | # Opps | Value | Weighted | % of Total | Avg Age (days) | Conv Rate |
|-------|--------|-------|----------|------------|----------------|-----------|
| **Prospecting** | {{n}} | ${{v}} | ${{wv}} | {{pct}}% | {{age}} | {{conv}}% |
| **Qualification** | {{n}} | ${{v}} | ${{wv}} | {{pct}}% | {{age}} | {{conv}}% |
| **Discovery** | {{n}} | ${{v}} | ${{wv}} | {{pct}}% | {{age}} | {{conv}}% |
| **Proposal** | {{n}} | ${{v}} | ${{wv}} | {{pct}}% | {{age}} | {{conv}}% |
| **Negotiation** | {{n}} | ${{v}} | ${{wv}} | {{pct}}% | {{age}} | {{conv}}% |
| **Total** | **{{n}}** | **${{v}}** | **${{wv}}** | **100%** | **{{age}}** | -- |

---

## Pipeline Changes This Period

| Change Type | Count | Value | % of Starting Pipeline |
|-------------|-------|-------|----------------------|
| **New opportunities added** | {{n}} | ${{v}} | {{pct}}% |
| **Opportunities advanced** | {{n}} | ${{v}} | {{pct}}% |
| **Opportunities pushed (close date moved)** | {{n}} | ${{v}} | {{pct}}% |
| **Opportunities decreased in value** | {{n}} | -${{v}} | {{pct}}% |
| **Opportunities increased in value** | {{n}} | +${{v}} | {{pct}}% |
| **Closed Won** | {{n}} | ${{v}} | {{pct}}% |
| **Closed Lost** | {{n}} | ${{v}} | {{pct}}% |
| **Net Pipeline Change** | -- | {{sign}}${{v}} | {{pct}}% |

---

## Pipeline by Rep

| Rep | Pipeline | Weighted | Coverage | # Opps | Avg Size | Largest Deal |
|-----|----------|----------|----------|--------|----------|-------------|
| {{rep_1}} | ${{val}} | ${{wt}} | {{cov}}x | {{n}} | ${{avg}} | ${{max}} |
| {{rep_2}} | ${{val}} | ${{wt}} | {{cov}}x | {{n}} | ${{avg}} | ${{max}} |
| {{rep_3}} | ${{val}} | ${{wt}} | {{cov}}x | {{n}} | ${{avg}} | ${{max}} |
| {{rep_4}} | ${{val}} | ${{wt}} | {{cov}}x | {{n}} | ${{avg}} | ${{max}} |
| **Team Total** | **${{val}}** | **${{wt}}** | **{{cov}}x** | **{{n}}** | **${{avg}}** | -- |

---

## Pipeline by Segment

| Segment | Pipeline | % of Total | # Opps | Avg Size | Avg Age |
|---------|----------|-----------|--------|----------|---------|
| **Enterprise** | ${{val}} | {{pct}}% | {{n}} | ${{avg}} | {{age}}d |
| **Mid-Market** | ${{val}} | {{pct}}% | {{n}} | ${{avg}} | {{age}}d |
| **SMB** | ${{val}} | {{pct}}% | {{n}} | ${{avg}} | {{age}}d |

---

## Pipeline by Product / Solution

| Product | Pipeline | % of Total | # Opps | Avg Size |
|---------|----------|-----------|--------|----------|
| {{product_1}} | ${{val}} | {{pct}}% | {{n}} | ${{avg}} |
| {{product_2}} | ${{val}} | {{pct}}% | {{n}} | ${{avg}} |
| {{product_3}} | ${{val}} | {{pct}}% | {{n}} | ${{avg}} |

---

## At-Risk Deals

Opportunities flagged for attention based on age, stalled progression, or missing engagement.

| Deal Name | Account | Value | Stage | Days in Stage | Last Activity | Risk Factor |
|-----------|---------|-------|-------|---------------|---------------|-------------|
| {{deal_1}} | {{acct}} | ${{val}} | {{stg}} | {{days}} | {{date}} | {{risk}} |
| {{deal_2}} | {{acct}} | ${{val}} | {{stg}} | {{days}} | {{date}} | {{risk}} |
| {{deal_3}} | {{acct}} | ${{val}} | {{stg}} | {{days}} | {{date}} | {{risk}} |
| {{deal_4}} | {{acct}} | ${{val}} | {{stg}} | {{days}} | {{date}} | {{risk}} |
| {{deal_5}} | {{acct}} | ${{val}} | {{stg}} | {{days}} | {{date}} | {{risk}} |

**Total At-Risk Pipeline:** ${{at_risk_total}} ({{pct}}% of total pipeline)

---

## Pipeline Health Indicators

| Indicator | Status | Detail |
|-----------|--------|--------|
| **Coverage** | {{Green/Yellow/Red}} | {{coverage}}x (target: 3-4x) |
| **Stage balance** | {{Green/Yellow/Red}} | {{description}} |
| **Pipeline age** | {{Green/Yellow/Red}} | Avg age {{days}}d (target: <{{target}}d) |
| **Net pipeline trend** | {{Green/Yellow/Red}} | {{growing/shrinking}} for {{n}} consecutive weeks |
| **Data quality** | {{Green/Yellow/Red}} | {{pct}}% of opps with complete required fields |

---

## Commentary and Actions

### Key Observations

1. {{observation_1}}
2. {{observation_2}}
3. {{observation_3}}

### Risks

1. {{risk_1}} -- Impact: ${{amount}} -- Mitigation: {{action}}
2. {{risk_2}} -- Impact: ${{amount}} -- Mitigation: {{action}}

### Opportunities

1. {{opportunity_1}} -- Potential: ${{amount}}
2. {{opportunity_2}} -- Potential: ${{amount}}

### Action Items

| Action | Owner | Due Date | Priority |
|--------|-------|----------|----------|
| {{action_1}} | {{owner}} | {{date}} | {{High/Medium/Low}} |
| {{action_2}} | {{owner}} | {{date}} | {{High/Medium/Low}} |
| {{action_3}} | {{owner}} | {{date}} | {{High/Medium/Low}} |
