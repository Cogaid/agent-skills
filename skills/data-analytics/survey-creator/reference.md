# Survey Creator - Reference Guide

## Survey Design Methodology

### BRUSO Framework Deep Dive

| Principle | Good Example | Bad Example | Fix |
|---|---|---|---|
| **Brief** | "How satisfied are you with our service?" | "Thinking about all aspects of the service you received, including quality, timeliness, and communication, how would you rate your overall level of satisfaction?" | Split into multiple focused questions |
| **Relevant** | "How often do you use Feature X?" (for feature feedback survey) | "What is your favorite color?" (in a product feedback survey) | Remove questions not tied to research objectives |
| **Unambiguous** | "How many times did you contact support in the past 30 days?" | "Do you regularly contact support?" | Add specific timeframe and measurable criteria |
| **Specific** | "In the past 7 days, how many hours did you spend using the app?" | "How much time do you spend on the app?" | Define the time period and unit |
| **Objective** | "How would you rate the new dashboard?" | "How much do you love the new dashboard?" | Remove leading/emotional language |

### Question Writing Rules

1. **One concept per question** -- never use "and" in a question stem
2. **Avoid negatives** -- "Which features are NOT useful?" confuses respondents
3. **Use balanced scales** -- equal positive and negative options
4. **Include an escape hatch** -- "N/A" or "Prefer not to answer" for sensitive questions
5. **Specify the time period** -- "In the past 30 days" vs "recently"
6. **Avoid absolute terms** -- "always," "never," "all" force unrealistic answers
7. **Use natural language** -- match how respondents actually speak
8. **Order options logically** -- alphabetical, chronological, or by scale

### Scale Selection Guide

#### Likert Scales

| Points | Labels | When to Use |
|---|---|---|
| 5-point agreement | Strongly Disagree, Disagree, Neutral, Agree, Strongly Agree | Employee engagement, attitudes |
| 5-point satisfaction | Very Dissatisfied, Dissatisfied, Neutral, Satisfied, Very Satisfied | CSAT surveys, service feedback |
| 5-point frequency | Never, Rarely, Sometimes, Often, Always | Behavioral frequency |
| 5-point quality | Poor, Fair, Good, Very Good, Excellent | Quality ratings |
| 7-point agreement | Strongly Disagree ... Neutral ... Strongly Agree | Academic research, nuanced attitudes |
| 4-point (forced choice) | Strongly Disagree, Disagree, Agree, Strongly Agree | When you need a directional answer |

#### NPS Scale (0-10)

| Score Range | Category | Label | Follow-Up |
|---|---|---|---|
| 0-6 | Detractors | Unhappy customers | "What could we improve?" |
| 7-8 | Passives | Satisfied but unenthusiastic | "What would make you rate us higher?" |
| 9-10 | Promoters | Loyal enthusiasts | "What do you value most?" |

**NPS Score** = % Promoters - % Detractors (range: -100 to +100)

### Skip Logic Patterns

| Pattern | Description | Example |
|---|---|---|
| Simple branch | One question determines next section | Q: "Do you use Feature X?" Yes -> Feature X questions, No -> Skip |
| Multi-branch | Answer routes to one of several paths | Q: "Which product do you use?" -> Product-specific sections |
| Qualification | Screen out ineligible respondents | Q: "Are you 18 or older?" No -> End survey |
| Conditional display | Show question only if condition met | Show pricing questions only if respondent is a decision-maker |
| Loop | Repeat section for each selected item | For each product selected, ask rating questions |

## Survey Types Reference

### Customer Satisfaction (CSAT)

| Aspect | Recommendation |
|---|---|
| Timing | Immediately after interaction or within 24 hours |
| Length | 3-5 questions |
| Key metric | CSAT score (% satisfied / total responses) |
| Benchmark | >80% is good, >90% is excellent |
| Follow-up | Open-ended "why" for low scores |

### Employee Engagement

| Aspect | Recommendation |
|---|---|
| Timing | Quarterly or bi-annually |
| Length | 15-25 questions |
| Key metric | Engagement index (mean of core questions) |
| Benchmark | >3.8/5.0 is healthy |
| Anonymity | Must be anonymous for honest responses |

### Market Research

| Aspect | Recommendation |
|---|---|
| Timing | Before product launch or market entry |
| Length | 10-15 questions |
| Key metric | Purchase intent, brand awareness |
| Sample size | 400+ for 95% confidence, +/-5% margin |
| Incentive | Usually required for adequate response rate |

### Product Feedback

| Aspect | Recommendation |
|---|---|
| Timing | After feature release or during beta |
| Length | 5-10 questions |
| Key metric | Feature satisfaction, usability rating |
| In-app | Intercept surveys get higher response rates |
| Segmentation | By user type, plan tier, usage frequency |

## Statistical Requirements

### Sample Size Calculator

| Confidence Level | Margin of Error | Population 1K | Population 10K | Population 100K+ |
|---|---|---|---|---|
| 95% | +/-5% | 278 | 370 | 384 |
| 95% | +/-3% | 517 | 965 | 1,067 |
| 95% | +/-1% | 906 | 4,900 | 9,513 |
| 99% | +/-5% | 400 | 623 | 664 |
| 99% | +/-3% | 665 | 1,557 | 1,849 |

### Analysis Methods by Question Type

| Question Type | Primary Analysis | Advanced Analysis |
|---|---|---|
| Likert scale | Mean, median, mode | Factor analysis, t-tests |
| Multiple choice | Frequency distribution | Chi-square, cross-tabulation |
| NPS | NPS score calculation | Regression on drivers |
| Open-ended | Thematic coding | Sentiment analysis, word clouds |
| Ranking | Mean rank, top-N | Conjoint analysis |
| Matrix | Item-level means | Correlation matrix |

## Response Rate Benchmarks

| Survey Type | Channel | Good Rate | Excellent Rate |
|---|---|---|---|
| Customer email | Email | 15-25% | >30% |
| In-app survey | In-app | 20-40% | >40% |
| Employee engagement | Email/intranet | 60-70% | >80% |
| Post-purchase | Email | 10-20% | >25% |
| Market research (panel) | Panel | 30-50% | >50% |
| Post-support interaction | Email/in-app | 20-30% | >35% |
