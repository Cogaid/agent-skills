# Resume Screener - Reference Guide

## Cognitive Bias Encyclopedia for Screeners

### Biases That Affect Resume Screening

| Bias | Definition | How It Manifests in Screening | Mitigation |
|------|-----------|------------------------------|------------|
| Affinity Bias | Preference for people similar to yourself | Favoring candidates from same school, company, or background | Blind screening; diverse screening panels |
| Halo Effect | One positive trait colors overall evaluation | Prestigious employer name inflates all scores | Score each criterion independently |
| Horns Effect | One negative trait colors overall evaluation | Typo on resume causes low scores across all criteria | Score each criterion independently |
| Anchoring Bias | Over-relying on first piece of information | First resume sets the benchmark for all others | Randomize resume order; calibrate with rubric first |
| Confirmation Bias | Seeking information that confirms initial impression | Reading the rest of the resume to validate first impression | Score criteria in a fixed order |
| Recency Bias | Over-weighting recent information | Last few resumes reviewed influence decisions disproportionately | Take breaks every 25-30 resumes |
| Conformity Bias | Influenced by others' opinions | Adjusting scores after hearing others' opinions | Score independently before debrief |
| Attribution Bias | Assuming behavior is caused by character, not circumstances | Attributing employment gaps to laziness rather than circumstances | Investigate before judging |
| Contrast Effect | Evaluating relative to the previous candidate, not the rubric | A mediocre resume looks great after several poor ones | Always score against the rubric, not other candidates |
| Beauty Bias | Favoring attractive candidates | Photos on resumes or LinkedIn influence evaluation | Remove photos; avoid LinkedIn during initial screen |

### Structured De-biasing Protocol

1. **Before screening:** Review the rubric. Screen a calibration resume with the hiring manager.
2. **During screening:** Score each criterion in sequence. Do not skip ahead. Do not go back and revise earlier criteria based on later information.
3. **After each batch of 25:** Take a 10-minute break. Review your score distribution for drift.
4. **After all screening:** Check your shortlist demographics. If it is homogeneous, review borderline candidates.

## ATS Systems Deep Dive

### Major ATS Platforms and Their Screening Features

| ATS | Market Segment | Key Screening Feature | Limitation |
|-----|---------------|----------------------|------------|
| Greenhouse | Mid-market to Enterprise | Structured scorecards, custom workflows | Limited AI parsing |
| Lever | Mid-market | Nurture campaigns, pipeline analytics | Fewer integrations |
| Workday Recruiting | Enterprise | Deep HRIS integration | Complex setup, expensive |
| iCIMS | Enterprise | AI-powered matching, large job board network | Steep learning curve |
| BambooHR | SMB | Simple ATS with HRIS, employee self-service | Limited advanced screening |
| Ashby | Startup to Mid-market | Analytics-first, modern UX | Newer, smaller ecosystem |
| Jobvite | Mid-market | Social recruiting, employee referrals | Dated interface |

### ATS Parsing Accuracy Issues

Common parsing failures that cause false negatives:

| Issue | Example | Impact |
|-------|---------|--------|
| Non-standard section headers | "Professional Journey" instead of "Work Experience" | Work history not parsed |
| Tables and columns | Multi-column resume layout | Content merged or lost |
| Headers and footers | Contact info in header | Name and email not captured |
| Graphics and icons | Skill bars, infographics | Skills not indexed |
| Unusual file formats | .pages, .odt, image-based PDF | Parsing fails entirely |
| Embedded fonts | Custom fonts without embedding | Text extraction fails |

**Recommendation:** Always review the original document alongside the parsed version for borderline candidates.

## Scoring Methodology

### Weighted Scoring Calculation

The weighted score is calculated as:

```
Weighted Score = Sum of (Criterion Score / 3 * Weight) for all criteria
```

Example:
| Criterion | Weight | Score (0-3) | Normalized | Weighted |
|-----------|--------|-------------|-----------|----------|
| Experience | 25% | 3 | 100% | 25.0 |
| Technical Skills | 25% | 2 | 66.7% | 16.7 |
| Education | 15% | 2 | 66.7% | 10.0 |
| Achievements | 15% | 1 | 33.3% | 5.0 |
| Domain Knowledge | 10% | 3 | 100% | 10.0 |
| Communication | 5% | 2 | 66.7% | 3.3 |
| Culture Alignment | 5% | 1 | 33.3% | 1.7 |
| **Total** | **100%** | | | **71.7%** |

Decision: Hold (60-79% range) -- review with hiring manager.

### Inter-Rater Reliability

When multiple screeners review the same resumes, measure agreement using:

- **Cohen's Kappa:** Measures agreement between two raters, adjusted for chance. Target kappa > 0.7.
- **Percentage Agreement:** Simple overlap. Target > 80%.
- **Score Variance:** Standard deviation of scores for the same candidate across raters. Target SD < 0.5 on a 3-point scale.

If reliability is low, recalibrate the rubric with the screening team.

## Legal Compliance

### EEOC Screening Documentation Requirements

The EEOC may request documentation of hiring decisions. Maintain:

1. Job description with dated approval
2. Screening criteria matrix with weights
3. Individual scorecards for every candidate reviewed
4. Rationale for every rejection
5. Shortlist demographics (aggregated, not individual)
6. Evidence of adverse impact analysis (4/5ths rule)

### The 4/5ths (80%) Rule

The selection rate for any protected group should be at least 80% of the selection rate for the group with the highest rate.

Example: If 60% of male applicants advance to interview (highest rate), then at least 48% (60% x 80%) of female applicants should advance. If fewer advance, this may indicate adverse impact.

Note: The 4/5ths rule is a guideline, not a strict legal standard. It triggers further investigation, not automatic liability.

### Ban-the-Box Laws

Many jurisdictions prohibit asking about criminal history on initial applications:

| Jurisdiction | Scope | When Criminal History Can Be Considered |
|-------------|-------|----------------------------------------|
| California | All employers | After conditional offer only |
| New York City | All employers | After conditional offer; individualized assessment required |
| Massachusetts | All employers | After interview or conditional offer |
| Illinois (Cook County) | All employers | After interview |
| Federal contractors | Executive Order 11246 | After conditional offer |
| "Fair Chance" states (30+) | Varies | Varies by state |

## Equivalent Qualifications Guide

### Degree Equivalency Matrix

| Traditional Requirement | Equivalent Qualifications |
|------------------------|--------------------------|
| Bachelor's in CS | Coding bootcamp + 2 years experience; self-taught + strong portfolio; Associate's + 4 years experience |
| MBA | 5+ years progressive management experience; executive education certificate + relevant experience |
| Master's in Data Science | Bachelor's in adjacent field + 3 years data experience; professional certifications (Google, AWS, IBM) + portfolio |
| PhD in research field | 8+ years industry research experience; published work + patents; recognized subject matter expert |

### International Credential Equivalency

| Country/Region | Credential | US Equivalent |
|---------------|-----------|---------------|
| UK | Bachelor's (Honours) | Bachelor's degree |
| UK | Master's | Master's degree |
| India | B.Tech / B.E. | Bachelor's in Engineering |
| India | MBA (IIM) | MBA (Top-tier) |
| Germany | Diplom | Master's degree |
| France | Licence | Bachelor's degree |
| France | Master | Master's degree |
| Canada | Bachelor's | Bachelor's degree (direct equivalent) |
| Australia | Bachelor's (Honours) | Bachelor's + some graduate work |

Reference: World Education Services (WES) for detailed evaluations.

## Resume Red Flag Investigation Framework

When encountering a red flag, use this investigation framework rather than auto-rejecting:

### Employment Gaps

| Gap Duration | Possible Explanations | Investigation Approach |
|-------------|----------------------|----------------------|
| 1-3 months | Job search between roles, relocation | Normal; no investigation needed |
| 3-6 months | Extended job search, travel, personal project | Note; ask in phone screen if advancing |
| 6-12 months | Caregiving, health, education, career pivot | Note; ask open-ended question in interview |
| 12+ months | All of the above + sabbatical, entrepreneurship | Note; ask about activities during gap |

**Key principle:** The gap itself is not disqualifying. What the candidate did during the gap, and whether they can perform the job now, is what matters.

### Job Hopping Analysis

| Pattern | Possible Explanation | Risk Level |
|---------|---------------------|------------|
| Multiple <1 year stints, all contractor/agency | Normal for contractors | Low |
| Progressive moves with increasing responsibility | Strategic career building | Low |
| Multiple <1 year stints at similar roles/level | May indicate performance issues | Medium |
| Left after <6 months repeatedly | May indicate poor decision-making or fit issues | Medium-High |
| One short stint among otherwise stable tenure | Likely a bad fit; isolated incident | Low |

**Key principle:** Context matters more than the pattern itself. Always look at the trajectory, not just tenure.
