# Job Description Writer - Reference Guide

## Inclusive Language Deep Dive

### Gender-Coded Language Research

Studies by Gaucher, Friesen, and Kay (2011) in the Journal of Personality and Social Psychology demonstrated that gendered wording in job advertisements affects the appeal of the position to men and women differently. Specifically:

- Job ads with masculine-coded language were perceived as having more male employees, making women less likely to apply.
- The effect was asymmetric: feminine-coded words did not significantly deter male applicants.
- Common masculine-coded words include: competitive, dominant, leader, assertive, analytical, determined, independent, objective, individual, decisive.
- Common feminine-coded words include: collaborative, cooperative, supportive, understanding, interpersonal, committed, responsible, connected, loyal, enthusiastic.

### Augmented Writing Tools

Several commercial and open-source tools exist for analyzing inclusive language in job descriptions:

| Tool | Type | Key Feature |
|------|------|-------------|
| Textio | Commercial SaaS | Real-time inclusive language scoring with predictive fill rates |
| Gender Decoder | Free / Open Source | Checks for masculine and feminine coded words based on Gaucher et al. research |
| Hemingway Editor | Free / Commercial | Readability scoring (aim for Grade 8-10) |
| Grammarly Business | Commercial | Inclusive language suggestions and tone detection |
| Ongig Text Analyzer | Commercial | JD-specific bias detection and SEO optimization |

### Readability Standards

The Flesch-Kincaid readability test measures how difficult a passage in English is to understand. For job descriptions:

| Score | Grade Level | Interpretation |
|-------|-------------|----------------|
| 90-100 | 5th grade | Very easy to read |
| 80-89 | 6th grade | Easy to read |
| 70-79 | 7th grade | Fairly easy |
| 60-69 | 8th-9th grade | Target range for JDs |
| 50-59 | 10th-12th grade | Acceptable upper bound |
| 30-49 | College | Too complex for job descriptions |
| 0-29 | Graduate | Far too complex |

Formula: 206.835 - 1.015 x (total words / total sentences) - 84.6 x (total syllables / total words)

## SEO Optimization Framework

### Job Board Algorithm Insights

Each major job board uses different ranking algorithms. Key factors:

**Indeed**
- Title match weight is highest
- First 150 characters of description are indexed for snippets
- Location specificity improves local search ranking
- Salary information boosts visibility by 30%
- Freshness matters: repost or refresh every 14 days

**LinkedIn**
- Standard job titles match LinkedIn's taxonomy for better distribution
- Skills listed in the JD are matched against candidate profiles
- Company page followers see jobs first
- Easy Apply increases application rate by 4x
- Remote-friendly tags expand candidate pool significantly

**Google for Jobs**
- Structured data (JSON-LD schema) is required for indexing
- datePosted and validThrough fields affect ranking
- Salary info (baseSalary) is a strong ranking signal
- Clear location or remote designation required
- Duplicate postings across boards are de-duplicated

### O*NET Standard Occupational Classification

The Occupational Information Network (O*NET) maintained by the US Department of Labor provides standardized job titles and descriptions. Using O*NET-aligned titles improves:

- Cross-board search visibility
- ATS parsing accuracy
- Compensation benchmarking alignment
- Legal defensibility of role requirements

Reference: https://www.onetonline.org/

## Legal Compliance by Jurisdiction

### United States Federal Requirements

| Law | Requirement | Impact on JD |
|-----|-------------|-------------|
| Title VII (Civil Rights Act) | No discrimination based on race, color, religion, sex, national origin | Avoid language that implies preference for protected classes |
| ADA (Americans with Disabilities Act) | Reasonable accommodation required | List essential functions; avoid unnecessary physical requirements |
| ADEA (Age Discrimination) | No age-based discrimination for 40+ | Avoid terms like "digital native," graduation year requirements |
| Equal Pay Act | Equal pay for equal work | Ensure JD accurately reflects duties for pay equity analysis |
| GINA (Genetic Information) | No genetic information discrimination | Do not request family medical history |

### State-Specific Salary Transparency Laws (as of 2025)

| State / City | Requirement |
|-------------|-------------|
| California | Pay range required in posting |
| Colorado | Pay range and benefits required in posting |
| Connecticut | Pay range on request or in posting |
| Maryland | Pay range on request |
| Nevada | Pay range after interview |
| New York (NYC) | Pay range required in posting |
| New York (State) | Pay range required in posting |
| Washington | Pay range and benefits required in posting |
| Rhode Island | Pay range on request or in posting |
| Jersey City | Pay range required in posting |

### EEOC-Compliant EEO Statements

**Standard:**
```
[Company Name] is an Equal Opportunity Employer. All qualified applicants will
receive consideration for employment without regard to race, color, religion,
sex, sexual orientation, gender identity, national origin, disability, veteran
status, or any other characteristic protected by law.
```

**Extended (recommended):**
```
[Company Name] is committed to building a diverse and inclusive workplace. We
are an equal opportunity employer and do not discriminate on the basis of race,
color, religion, sex, sexual orientation, gender identity or expression,
national origin, age, disability, genetic information, veteran status, or any
other legally protected characteristic. We actively encourage applications from
people of all backgrounds, experiences, abilities, and perspectives.

If you need a reasonable accommodation during the application or interview
process, please contact [email/phone].
```

## Requirements Prioritization Matrix

### The "Must-Have" Test

For each requirement, ask these five questions. If the answer to any is "no," move it to nice-to-have:

1. Can a candidate succeed in this role without this qualification?
2. Could this requirement be learned in the first 90 days?
3. Is this requirement truly distinct from another listed requirement?
4. Does this requirement predict job performance based on evidence?
5. Would removing this requirement allow access to a meaningfully larger candidate pool?

### Degree Requirements Analysis

Research from Harvard Business School ("Dismissed by Degrees," 2017) found:

- 61% of employers required a bachelor's degree for roles that previously did not require one
- Degree inflation excludes qualified candidates, particularly from underrepresented groups
- Skills-based hiring produces equivalent or better job performance outcomes

**Recommended language:**
- Instead of: "Bachelor's degree in Computer Science required"
- Use: "Bachelor's degree in Computer Science or equivalent practical experience"
- Even better: "Strong foundation in computer science fundamentals, demonstrated through education, work experience, or portfolio"

## Compensation Benchmarking Sources

| Source | Type | Best For |
|--------|------|----------|
| levels.fyi | Free / Crowdsourced | Tech compensation by company and level |
| Glassdoor | Free / Crowdsourced | Broad market salary data |
| Payscale | Freemium | Role-specific compensation reports |
| Radford (Aon) | Commercial | Enterprise compensation surveys |
| Mercer | Commercial | Global compensation benchmarking |
| Carta Total Comp | Commercial | Startup equity benchmarking |
| Bureau of Labor Statistics | Free / Government | Occupational Employment and Wage Statistics |
| LinkedIn Salary Insights | Free with Premium | Market rate by title, location, experience |
