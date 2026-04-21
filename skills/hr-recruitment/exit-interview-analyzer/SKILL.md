---
name: exit-interview-analyzer
description: Analyze exit interview data to identify retention risks and generate actionable insights. Use when user mentions "exit interview," "why employees leave," "attrition analysis," "turnover insights," "retention strategy," "exit survey," "analyze departures."
metadata:
  version: 1.0.0
  category: hr-recruitment
---

# Exit Interview Analyzer

Systematically collect, categorize, and analyze exit interview data to surface attrition drivers, identify retention risks, and generate actionable recommendations.

## Purpose

Every departing employee holds intelligence about organizational health. Exit interviews, when properly structured and analyzed, reveal systemic issues before they cause cascading attrition. This skill provides the complete framework from conducting effective exit interviews through pattern analysis and executive reporting, turning individual departures into organizational learning.

## Quick Reference

### Exit Interview Question Bank

#### Core Questions (Ask Every Departing Employee)

| # | Question | Category | Data Type |
|---|----------|----------|-----------|
| 1 | What prompted you to begin looking for a new opportunity? | Root Cause | Open-ended |
| 2 | How would you describe your relationship with your direct manager? | Management | Scale (1-5) + Open |
| 3 | Did you feel you had opportunities for growth and advancement here? | Career Development | Scale (1-5) + Open |
| 4 | How would you rate your total compensation relative to market? | Compensation | Scale (1-5) |
| 5 | Did you feel your work was meaningful and valued? | Engagement | Scale (1-5) + Open |
| 6 | How would you describe the team culture and work environment? | Culture | Open-ended |
| 7 | Were there adequate tools, resources, and support to do your job well? | Resources | Scale (1-5) |
| 8 | How was your workload and work-life balance? | Wellbeing | Scale (1-5) + Open |
| 9 | Would you consider returning to this organization in the future? | Boomerang Potential | Yes/No + Open |
| 10 | What could we have done differently to keep you? | Retention | Open-ended |

#### Deep-Dive Questions (Use Selectively Based on Context)

| Category | Question |
|----------|----------|
| Management | "Can you describe a specific instance where your manager helped or hindered your work?" |
| Management | "How effectively did your manager communicate expectations and provide feedback?" |
| Career | "What career development conversations did you have, and how actionable were they?" |
| Career | "Did you see a clear path to promotion? Why or why not?" |
| Compensation | "What components of your compensation package were most and least competitive?" |
| Compensation | "Was pay equity a concern for you?" |
| Culture | "Did you feel psychologically safe to speak up, disagree, or take risks?" |
| Culture | "How inclusive did you find the workplace? Any specific examples?" |
| Role | "How closely did your day-to-day work match what you expected when you joined?" |
| Role | "Were your skills being fully utilized?" |
| Onboarding | "Looking back, was your onboarding effective? What was missing?" |
| Future | "What does your new opportunity offer that we did not?" |
| Future | "What advice would you give your replacement?" |

### Response Categorization Framework

| Category Code | Category | Description | Example Responses |
|--------------|----------|-------------|-------------------|
| MGT | Management Issues | Problems with direct manager or leadership | "My manager never gave feedback," "Leadership is disconnected" |
| CMP | Compensation | Pay, benefits, equity concerns | "Below market," "No raise in 2 years," "Benefits are worse than competitors" |
| CDV | Career Development | Lack of growth, promotion, or learning | "No promotion path," "Stagnant skills," "No mentorship" |
| CUL | Culture | Organizational culture and values | "Toxic team dynamics," "Values not practiced," "Poor DEI" |
| WLB | Work-Life Balance | Workload, burnout, flexibility | "Constant overtime," "No remote option," "Unsustainable pace" |
| ROL | Role Misalignment | Job does not match expectations or skills | "Not what I signed up for," "Underutilized," "Scope creep" |
| REC | Recognition | Lack of appreciation or visibility | "Work goes unnoticed," "No public recognition," "Credit taken by others" |
| REL | Relocation / Personal | Non-work reasons for departure | "Spouse relocated," "Going back to school," "Family reasons" |
| OPP | External Opportunity | Pulled by a better external offer | "Dream company," "Exciting new challenge," "Startup opportunity" |
| RES | Resources / Tools | Inadequate support to do the job | "Outdated tools," "No budget," "Understaffed team" |

### Attrition Risk Indicators

Watch for these patterns in exit data and current employee signals.

| Risk Level | Indicator | Data Source |
|-----------|-----------|-------------|
| Critical | 3+ departures from same team in 6 months | Exit data |
| Critical | Manager cited as reason in 50%+ of exits | Exit interviews |
| High | Compensation below market in 30%+ of exits | Exit interviews + market data |
| High | Average tenure declining quarter over quarter | HRIS data |
| High | Engagement survey scores dropping in specific teams | Survey data |
| Medium | Career development cited in 40%+ of exits | Exit interviews |
| Medium | Voluntary attrition rate exceeds industry benchmark | HRIS data |
| Medium | Boomerang willingness below 30% | Exit interviews |
| Low | Departures concentrated in one tenure band (e.g., 18-24 months) | HRIS data |
| Low | Work-life balance concerns rising | Exit interviews + surveys |

## Workflow

### Phase 1: Conduct Exit Interviews

- [ ] Schedule the interview 1-2 weeks before the last day
- [ ] Use a neutral interviewer (HR, not the direct manager)
- [ ] Explain confidentiality and how data will be used
- [ ] Follow the structured question bank (core + selective deep-dive)
- [ ] Record responses accurately (with permission) or take detailed notes
- [ ] Allow 45-60 minutes for the conversation
- [ ] Thank the employee and confirm any outstanding administrative items

### Phase 2: Code and Categorize Responses

- [ ] Assign each response to a category code (MGT, CMP, CDV, etc.)
- [ ] Rate the intensity of each theme (1=mentioned, 2=emphasized, 3=primary driver)
- [ ] Tag whether the reason is push (internal issue) or pull (external attraction)
- [ ] Record structured data (scale ratings) in the tracking system
- [ ] Flag any urgent issues requiring immediate action (harassment, safety, legal)

### Phase 3: Aggregate and Analyze

- [ ] Combine data across all exits for the analysis period
- [ ] Calculate frequency of each category code
- [ ] Segment by department, level, tenure, and demographics (if available)
- [ ] Identify statistically significant patterns and trends
- [ ] Compare to prior periods (quarter-over-quarter, year-over-year)
- [ ] Cross-reference with engagement survey data
- [ ] Calculate the cost of attrition for the period

### Phase 4: Generate Insights and Recommendations

- [ ] Identify the top 3-5 attrition drivers
- [ ] Determine which drivers are addressable vs. external
- [ ] Draft specific, actionable retention recommendations
- [ ] Estimate impact and effort for each recommendation
- [ ] Prioritize recommendations by ROI
- [ ] Prepare the executive report

### Phase 5: Present and Act

- [ ] Present findings to leadership with data visualization
- [ ] Propose retention initiatives with timelines and owners
- [ ] Track implementation of approved recommendations
- [ ] Measure the impact of retention interventions over time

## Trend Analysis Template

```
EXIT INTERVIEW TREND ANALYSIS

Period: [Q1 2026] vs. [Q4 2025] vs. [Q3 2025]
Total Departures: [Current] | [Prior 1] | [Prior 2]
Voluntary Attrition Rate: [X]% | [X]% | [X]%

CATEGORY FREQUENCY (% of exits citing this as a factor)

| Category | Q3 2025 | Q4 2025 | Q1 2026 | Trend | Alert |
|----------|---------|---------|---------|-------|-------|
| Management (MGT) | __% | __% | __% | [up/down/flat] | [Y/N] |
| Compensation (CMP) | __% | __% | __% | [up/down/flat] | [Y/N] |
| Career Dev (CDV) | __% | __% | __% | [up/down/flat] | [Y/N] |
| Culture (CUL) | __% | __% | __% | [up/down/flat] | [Y/N] |
| Work-Life (WLB) | __% | __% | __% | [up/down/flat] | [Y/N] |
| Role Mismatch (ROL) | __% | __% | __% | [up/down/flat] | [Y/N] |
| Recognition (REC) | __% | __% | __% | [up/down/flat] | [Y/N] |
| Personal (REL) | __% | __% | __% | [up/down/flat] | [Y/N] |
| External Opp (OPP) | __% | __% | __% | [up/down/flat] | [Y/N] |
| Resources (RES) | __% | __% | __% | [up/down/flat] | [Y/N] |

SEGMENTATION ANALYSIS

By Department:
| Department | Attrition Rate | Top Reason | Second Reason |
|-----------|---------------|------------|---------------|
| | | | |
| | | | |
| | | | |

By Tenure Band:
| Tenure | % of Departures | Top Reason | Insight |
|--------|----------------|------------|---------|
| 0-6 months | __% | | Onboarding/role fit issue |
| 6-18 months | __% | | Growth/development gap |
| 18-36 months | __% | | Promotion/compensation ceiling |
| 36+ months | __% | | Burnout/stagnation |

By Level:
| Level | Attrition Rate | Top Reason | Cost Impact |
|-------|---------------|------------|-------------|
| Junior | __% | | Lower replacement cost |
| Mid | __% | | Moderate replacement cost |
| Senior | __% | | High replacement cost |
| Leadership | __% | | Critical replacement cost |

PUSH vs. PULL ANALYSIS
Push Factors (Internal): __% of departures
Pull Factors (External): __% of departures
Both: __% of departures

KEY FINDING:
_______________________________________________
_______________________________________________
```

### Cost of Attrition Calculator

| Cost Component | Calculation | Amount |
|---------------|-------------|--------|
| Recruiting costs | Agency fee or internal recruiter time | $ |
| Interviewing costs | Interviewer hours x hourly rate x # interviews | $ |
| Onboarding and training | Training hours x cost + materials | $ |
| Lost productivity (role vacant) | Revenue per employee x vacancy months | $ |
| Ramp-up time for replacement | Reduced productivity for 3-6 months | $ |
| Knowledge loss | Estimated value of institutional knowledge | $ |
| Team impact | Remaining team overtime/morale cost | $ |
| **Total Cost Per Departure** | | **$** |
| **Period Total (all departures)** | Total x number of departures | **$** |

Rule of thumb: Total cost of replacing an employee is 50-200% of annual salary depending on level.

## Retention Recommendation Templates

### Template: Compensation Adjustment Recommendation

```
RETENTION RECOMMENDATION: COMPENSATION

Issue: [X]% of departing employees cited below-market compensation
as a primary factor. Market data confirms [X]% pay gap for [roles].

Impact: Estimated cost of attrition driven by compensation: $[X]
Cost of market adjustment: $[X]
ROI of adjustment: [X]x

Recommendation:
1. Conduct market compensation study for [affected roles/levels]
2. Adjust salaries to [Xth] percentile of market
3. Implement annual market adjustment cycle
4. Improve total compensation communication (many employees
   undervalue their benefits package)

Timeline: [X] weeks for study, [X] weeks for implementation
Owner: [Compensation team / VP People]
Success Metric: Reduce comp-related attrition by [X]% in [timeframe]
```

### Template: Manager Development Recommendation

```
RETENTION RECOMMENDATION: MANAGEMENT QUALITY

Issue: [X]% of departing employees cited their manager as a key
factor. Teams under managers [X, Y, Z] show attrition rates [X]x
above company average.

Impact: Manager-driven attrition costs an estimated $[X] annually.

Recommendation:
1. Implement mandatory management training for all people managers
   (feedback delivery, 1:1 effectiveness, career conversations)
2. Add manager effectiveness to performance review criteria
3. Launch skip-level conversations for at-risk teams
4. Consider management changes for chronic high-attrition teams

Timeline: Training launch in [X] weeks, full rollout in [X] months
Owner: [L&D / VP People]
Success Metric: Manager satisfaction scores improve by [X] points;
attrition in affected teams decreases by [X]%
```

### Template: Career Development Recommendation

```
RETENTION RECOMMENDATION: CAREER DEVELOPMENT

Issue: [X]% of exits cite lack of growth opportunities. Average
tenure at departure is [X] months, suggesting a [X]-month
development ceiling.

Impact: Career-driven attrition disproportionately affects
[mid-level / high-performing] employees with the highest
replacement cost.

Recommendation:
1. Define clear career ladders for all major role families
2. Mandate quarterly career development conversations
3. Create internal mobility program (internal job board, rotation)
4. Establish a learning budget of $[X] per employee
5. Launch a mentorship matching program

Timeline: Career ladders in [X] months, programs in [X] months
Owner: [L&D / Talent Development / VP People]
Success Metric: Career development satisfaction increases by [X]
points on engagement survey; attrition in 18-36 month tenure
band decreases by [X]%
```

## Reporting Format

### Executive Summary Template

```
EXIT INTERVIEW ANALYSIS - EXECUTIVE SUMMARY

Period: [Date Range]
Prepared By: [Name]
Date: [Date]

HEADLINE METRICS
- Total Departures: [X] ([X]% voluntary attrition rate)
- Industry Benchmark: [X]%
- Estimated Cost of Attrition: $[X]
- Boomerang Willingness: [X]% would consider returning

TOP 3 ATTRITION DRIVERS
1. [Category]: [X]% of exits, trending [up/down], [brief insight]
2. [Category]: [X]% of exits, trending [up/down], [brief insight]
3. [Category]: [X]% of exits, trending [up/down], [brief insight]

HOTSPOT TEAMS
- [Team/Department]: [X]% attrition rate (company avg: [X]%)
  Primary driver: [Category]

KEY INSIGHT
[One paragraph connecting the data to a strategic narrative]

RECOMMENDED ACTIONS (Priority Order)
| # | Action | Impact | Effort | Owner | Timeline |
|---|--------|--------|--------|-------|----------|
| 1 | | High/Med/Low | High/Med/Low | | |
| 2 | | High/Med/Low | High/Med/Low | | |
| 3 | | High/Med/Low | High/Med/Low | | |

APPENDIX: Full data tables and individual interview summaries
available upon request.
```

## Scripts & Tools

### Usage: Analyze Exit Interview Data

```
Input: Set of exit interview responses (structured and open-ended)
Process: Categorize responses -> Calculate frequencies -> Identify trends -> Segment analysis -> Generate insights
Output: Trend analysis with visualizations and prioritized recommendations
```

### Usage: Conduct an Exit Interview

```
Input: Departing employee's role, tenure, department, known context
Process: Select questions from bank -> Customize for context -> Conduct interview -> Code responses -> Flag urgent issues
Output: Completed exit interview record with categorized responses
```

### Usage: Calculate Attrition Cost

```
Input: Number of departures, average salary by level, vacancy duration, recruiting costs
Process: Apply cost model to each departure -> Aggregate by category -> Compare to retention intervention cost
Output: Cost of attrition report with ROI projections for retention initiatives
```

### Usage: Generate Retention Report

```
Input: Exit interview data for analysis period + prior period data for comparison
Process: Run trend analysis -> Segment by team/level/tenure -> Identify hotspots -> Draft recommendations -> Format executive summary
Output: Complete retention report with executive summary and detailed appendix
```

## Best Practices

1. **Use a neutral interviewer.** Employees will not be candid with their direct manager. Use HR or an external consultant.
2. **Separate the interview from administrative offboarding.** The exit interview is a data-gathering exercise, not a paperwork session.
3. **Ask "What could we have done differently?" last.** Build rapport with easier questions first.
4. **Look for patterns, not individual complaints.** One person's feedback is anecdotal. Five people saying the same thing is a signal.
5. **Cross-reference with engagement data.** Exit interviews explain why people leave; engagement surveys predict who might leave next.
6. **Track boomerang willingness.** A low rate indicates systemic cultural or relationship issues, not just competitive pulls.
7. **Segment relentlessly.** Company-wide averages hide team-level crises. Always analyze by department, manager, level, and tenure.
8. **Act visibly on findings.** If employees see no change after colleagues leave, the remaining team loses faith. Communicate what you are doing.
9. **Calculate the cost.** Executives respond to dollars. Translate attrition patterns into financial impact.
10. **Maintain confidentiality rigorously.** If departing employees cannot trust the process, data quality collapses and the entire program becomes worthless.
