# SOW Templates

## Full SOW Template

```
STATEMENT OF WORK

SOW #:            {{sow_number}}
Reference MSA:    {{msa_reference}}
Client:           {{client_name}}
Provider:         {{provider_name}}
Effective Date:   {{effective_date}}
SOW Expiration:   {{expiration_date}}
Prepared by:      {{preparer_name}}, {{preparer_title}}

================================================================

1. OVERVIEW & OBJECTIVES
----------------------------------------------------------------
{{project_overview}}

Project Objectives:
a. {{objective_1}}
b. {{objective_2}}
c. {{objective_3}}

2. SCOPE OF SERVICES
----------------------------------------------------------------
2.1 In Scope:
    - {{in_scope_1}}
    - {{in_scope_2}}
    - {{in_scope_3}}
    - {{in_scope_4}}

2.2 Out of Scope:
    - {{out_scope_1}}
    - {{out_scope_2}}
    - {{out_scope_3}}

    Note: Any work not explicitly listed in Section 2.1 is out
    of scope and requires a Change Order (see Section 8).

3. DELIVERABLES
----------------------------------------------------------------
#   Deliverable           Format        Milestone   Due Date
--  --------------------  ----------    ---------   ----------
D1  {{deliverable_1}}     {{format_1}}  M1          {{date_1}}
D2  {{deliverable_2}}     {{format_2}}  M2          {{date_2}}
D3  {{deliverable_3}}     {{format_3}}  M3          {{date_3}}
D4  {{deliverable_4}}     {{format_4}}  M4          {{date_4}}
D5  {{deliverable_5}}     {{format_5}}  M5          {{date_5}}

4. TIMELINE & MILESTONES
----------------------------------------------------------------
Phase 1: {{phase_1_name}} ({{phase_1_dates}})
  M1: {{milestone_1}}                    {{m1_date}}
  - {{task_1_1}}
  - {{task_1_2}}

Phase 2: {{phase_2_name}} ({{phase_2_dates}})
  M2: {{milestone_2}}                    {{m2_date}}
  - {{task_2_1}}
  - {{task_2_2}}

Phase 3: {{phase_3_name}} ({{phase_3_dates}})
  M3: {{milestone_3}}                    {{m3_date}}
  - {{task_3_1}}
  - {{task_3_2}}

TOTAL DURATION: {{total_duration}}
BUFFER: {{buffer_description}}

5. ACCEPTANCE CRITERIA & PROCESS
----------------------------------------------------------------
1. Provider submits deliverable with completion notice
2. Client has {{review_days}} business days to review
3. Client responds: ACCEPTED / ACCEPTED WITH COMMENTS / REJECTED
4. If rejected, Provider has {{remedy_days}} days to remedy
5. Maximum {{max_rounds}} rounds of revision per deliverable
6. Deemed accepted if no response within review period

Acceptance Criteria per Deliverable:
D1: {{d1_criteria}}
D2: {{d2_criteria}}
D3: {{d3_criteria}}

6. PAYMENT SCHEDULE
----------------------------------------------------------------
Engagement Type: {{engagement_type}}
Total Contract Value: ${{total_value}}

Payment    Trigger                     Amount      % of Total
-------    -------------------------   --------    ----------
1          SOW execution (deposit)     ${{p1}}     {{p1_pct}}%
2          {{trigger_2}}               ${{p2}}     {{p2_pct}}%
3          {{trigger_3}}               ${{p3}}     {{p3_pct}}%
4          {{trigger_4}}               ${{p4}}     {{p4_pct}}%

Payment Terms: {{payment_terms}}
Late Payment: {{late_payment_policy}}
Expenses: {{expense_policy}}

7. ASSUMPTIONS & DEPENDENCIES
----------------------------------------------------------------
Assumptions:
1. {{assumption_1}}
2. {{assumption_2}}
3. {{assumption_3}}

Dependencies:
1. {{dependency_1}}
2. {{dependency_2}}

8. CHANGE ORDER PROCESS
----------------------------------------------------------------
All scope changes require a written Change Order including:
- Description of change
- Impact on schedule, cost, and resources
- Approval signatures from both parties
Work begins only after written approval.

9. ROLES & RESPONSIBILITIES
----------------------------------------------------------------
Provider Responsibilities:
- {{provider_resp_1}}
- {{provider_resp_2}}

Client Responsibilities:
- {{client_resp_1}}
- {{client_resp_2}}
- {{client_resp_3}}

10. GOVERNANCE & COMMUNICATION
----------------------------------------------------------------
Status Reports:     {{report_frequency}}
Status Meetings:    {{meeting_schedule}}
Escalation Path:    {{escalation_path}}
Tools:              {{tools}}

SIGNATURES
----------------------------------------------------------------
Provider: ________________  Date: ________  Title: ____________
Client:   ________________  Date: ________  Title: ____________
```

## Change Order Template

```
CHANGE ORDER
=============================================
Change Order #:    CO-{{sow_number}}-{{co_number}}
SOW Reference:     {{sow_number}}
Date Requested:    {{request_date}}
Requested by:      {{requestor}}, {{requestor_company}}

DESCRIPTION OF CHANGE:
{{change_description}}

REASON FOR CHANGE:
{{change_reason}}

IMPACT ASSESSMENT:
  Schedule Impact:     +{{schedule_impact}}
  Cost Impact:         +${{cost_impact}}
  Resource Impact:     {{resource_impact}}
  Risk Impact:         {{risk_impact}}
  Deliverable Impact:  {{deliverable_impact}}

REVISED TOTALS:
  Original SOW Value:    ${{original_value}}
  Previous COs:          ${{previous_cos}}
  This Change Order:     +${{this_co}}
  New Total:             ${{new_total}}

APPROVAL:
Provider: ________________  Date: ________
Client:   ________________  Date: ________
```

## Scope Matrix Template

```
SCOPE MATRIX - {{project_name}}

Feature / Activity            MoSCoW    Phase    Est. Hours   Notes
----------------------------  ------    -----    ----------   --------
{{feature_1}}                 Must       1        {{hrs}}     {{notes}}
{{feature_2}}                 Must       1        {{hrs}}     {{notes}}
{{feature_3}}                 Must       2        {{hrs}}     {{notes}}
{{feature_4}}                 Should     2        {{hrs}}     {{notes}}
{{feature_5}}                 Should     1        {{hrs}}     {{notes}}
{{feature_6}}                 Could      3        {{hrs}}     {{notes}}
{{feature_7}}                 Won't      --       --          {{notes}}
----------------------------  ------    -----    ----------
TOTAL (In Scope)                                  {{total}}

Must Have:   {{must_hrs}} hrs ({{must_pct}}%)
Should Have: {{should_hrs}} hrs ({{should_pct}}%)
Could Have:  {{could_hrs}} hrs ({{could_pct}}%)
```
