---
name: survey-creator
description: Design effective surveys and questionnaires with best practices for unbiased data collection. Use when user mentions "create survey," "questionnaire," "feedback form," "NPS survey," "customer survey," "employee engagement survey," "market research survey."
metadata:
  version: 1.0.0
  category: data-analytics
---

# Survey Creator

Design well-structured surveys and questionnaires that yield reliable, actionable data through proper question design, bias avoidance, and response rate optimization.

## Purpose

This skill creates surveys that produce high-quality data by applying research-backed design principles. It covers question type selection, survey flow, bias mitigation, and analysis planning for customer feedback, employee engagement, market research, and other survey purposes.

## Quick Reference

### Question Types

| Type              | Best For                         | Response Format                  | Analysis Type    |
|-------------------|----------------------------------|----------------------------------|------------------|
| Likert Scale      | Attitudes, satisfaction          | 5 or 7 point agree/disagree     | Mean, median     |
| Multiple Choice   | Categorical data, preferences    | Select one or many               | Frequency, %     |
| NPS (0-10)        | Loyalty, likelihood to recommend | 0-10 numeric scale               | NPS score        |
| Open-Ended        | Qualitative insights, "why"      | Free text                        | Thematic coding  |
| Matrix/Grid       | Multiple items on same scale     | Rows=items, Cols=scale           | Item comparison  |
| Ranking           | Priority ordering                | Drag-and-drop or numbered        | Rank order       |
| Slider            | Continuous measurement           | Numeric range                    | Distribution     |
| Semantic Differential| Brand perception, attitudes   | Opposing adjective pairs         | Mean positioning |
| Dichotomous       | Yes/No decisions                 | Binary choice                    | Proportions      |
| Dropdown          | Long lists (country, category)   | Select from list                 | Frequency        |

### Scale Design Guidance

| Scale Points | When to Use                           | Label Strategy                    |
|-------------|---------------------------------------|-----------------------------------|
| 5-point     | Simple satisfaction, agreement         | Label all points                  |
| 7-point     | More nuanced attitudes, academic       | Label endpoints + midpoint        |
| 10-point    | NPS, detailed satisfaction             | Label endpoints only              |
| 4-point     | Force a direction (no neutral)         | Label all points                  |
| Binary      | Clear yes/no decisions                 | Yes/No or Agree/Disagree          |

## Survey Design Principles

### The BRUSO Framework

| Principle     | Description                                     | Example Violation                    |
|---------------|-------------------------------------------------|--------------------------------------|
| Brief         | Keep questions short and focused                | Paragraph-long question stems        |
| Relevant      | Every question serves the research objective    | Demographic overload at the start    |
| Unambiguous   | One interpretation only                         | "Do you like the price and quality?" |
| Specific      | Concrete timeframe and context                  | "Do you often use our product?"      |
| Objective     | No leading language                             | "How great was your experience?"     |

### Survey Flow Structure

```
RECOMMENDED SURVEY FLOW

1. INTRODUCTION (1 screen)
   - Purpose of the survey
   - Estimated completion time
   - Anonymity/confidentiality statement
   - Incentive details (if applicable)

2. SCREENING QUESTIONS (1-3 questions)
   - Qualify/disqualify respondents
   - Route to appropriate survey path

3. WARM-UP QUESTIONS (2-3 questions)
   - Easy, non-threatening questions
   - Build engagement before complex topics
   - Behavioral questions (what they do)

4. CORE QUESTIONS (5-15 questions)
   - Most important research questions
   - Group by topic with section headers
   - Progress from general to specific
   - Mix question types to maintain engagement

5. SENSITIVE QUESTIONS (if needed)
   - Place after rapport is established
   - Include "prefer not to answer" option

6. DEMOGRAPHICS (3-5 questions)
   - Place at the end (unless needed for screening)
   - Only collect what you will actually analyze
   - Include inclusive options

7. CLOSING
   - Open-ended feedback opportunity
   - Thank you message
   - Next steps or follow-up information
```

## Bias Avoidance Checklist

| Bias Type              | Description                            | Prevention Strategy                  |
|------------------------|----------------------------------------|--------------------------------------|
| Leading questions      | Suggests a "correct" answer            | Use neutral wording, remove adjectives|
| Double-barreled        | Asks about two things in one question  | Split into separate questions        |
| Acquiescence bias      | Tendency to agree with any statement   | Mix positive and negative framings   |
| Social desirability    | Answers to look good, not truthfully   | Emphasize anonymity, indirect questions|
| Order effects          | Earlier questions influence later ones | Randomize question and option order  |
| Anchoring              | First option influences selection      | Randomize choice order               |
| Recency bias           | Better recall of recent events         | Specify concrete time periods        |
| Loaded language        | Emotionally charged terms              | Use neutral, objective language      |
| Non-response bias      | Certain groups skip the survey         | Keep it short, offer incentives      |
| Sampling bias          | Survey reaches non-representative sample| Use stratified sampling             |

### Before/After Examples

| Biased Version                                    | Corrected Version                              |
|---------------------------------------------------|------------------------------------------------|
| "How much did you enjoy our service?"             | "How would you rate your experience with our service?" |
| "Don't you agree that the new feature is helpful?"| "How useful do you find the new feature?"      |
| "How often do you exercise?"                      | "In the past 7 days, how many times did you exercise for 30+ minutes?" |
| "Rate the quality and speed of service"           | Split: "Rate the quality of service" + "Rate the speed of service" |

## Response Rate Optimization

| Strategy                 | Expected Impact | Implementation                         |
|--------------------------|-----------------|----------------------------------------|
| Keep under 5 minutes     | +20-30%         | Limit to 10-15 questions               |
| Personalized invitation  | +10-15%         | Use name, reference relationship       |
| Mobile-optimized         | +15-25%         | Responsive design, large tap targets   |
| Progress bar             | +5-10%          | Show completion percentage             |
| Incentive offered        | +10-20%         | Gift card, discount, donation          |
| Multiple reminders       | +15-25%         | 2-3 reminders at 3-day intervals       |
| Clear purpose statement  | +5-10%          | Explain how feedback will be used      |
| Optimal send time        | +5-10%          | Tue-Thu, 10am-2pm local time           |
| Branded sender           | +5-10%          | Recognizable from name and domain      |

## Survey Templates

### Customer Feedback Survey (CSAT + NPS)

```
CUSTOMER FEEDBACK SURVEY
Estimated time: 3 minutes

Q1. Overall, how satisfied are you with [Product/Service]?
    ( ) Very Dissatisfied  ( ) Dissatisfied  ( ) Neutral
    ( ) Satisfied  ( ) Very Satisfied

Q2. How likely are you to recommend [Product/Service] to a
    friend or colleague? (0-10 scale)
    [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10]

Q3. Which of the following best describes your primary use
    of [Product/Service]? (Select one)
    ( ) [Use case 1]  ( ) [Use case 2]  ( ) [Use case 3]
    ( ) Other: ___________

Q4. Please rate the following aspects:
    |                    | Poor | Fair | Good | Very Good | Excellent |
    | Ease of use        |  ( ) | ( )  | ( )  |    ( )    |    ( )    |
    | Value for money    |  ( ) | ( )  | ( )  |    ( )    |    ( )    |
    | Customer support   |  ( ) | ( )  | ( )  |    ( )    |    ( )    |
    | Reliability        |  ( ) | ( )  | ( )  |    ( )    |    ( )    |

Q5. What is the one thing we could do to improve your experience?
    [Free text]

Q6. Any additional comments?
    [Free text]
```

### Employee Engagement Survey

```
EMPLOYEE ENGAGEMENT SURVEY
Estimated time: 8 minutes | Anonymous

ENGAGEMENT & MOTIVATION
Q1. I am proud to work at [Company].
    Strongly Disagree [1] [2] [3] [4] [5] Strongly Agree

Q2. I would recommend [Company] as a great place to work.
    Strongly Disagree [1] [2] [3] [4] [5] Strongly Agree

Q3. I see myself working here in 2 years.
    Strongly Disagree [1] [2] [3] [4] [5] Strongly Agree

MANAGEMENT & LEADERSHIP
Q4. My manager provides clear expectations.
    Strongly Disagree [1] [2] [3] [4] [5] Strongly Agree

Q5. I receive regular, useful feedback on my work.
    Strongly Disagree [1] [2] [3] [4] [5] Strongly Agree

Q6. Leadership communicates a clear vision for the company.
    Strongly Disagree [1] [2] [3] [4] [5] Strongly Agree

GROWTH & DEVELOPMENT
Q7. I have opportunities to learn and grow in my role.
    Strongly Disagree [1] [2] [3] [4] [5] Strongly Agree

Q8. I feel my career development is supported.
    Strongly Disagree [1] [2] [3] [4] [5] Strongly Agree

WORK ENVIRONMENT
Q9. I have the tools and resources I need to do my job well.
    Strongly Disagree [1] [2] [3] [4] [5] Strongly Agree

Q10. I feel my workload is manageable.
    Strongly Disagree [1] [2] [3] [4] [5] Strongly Agree

OPEN FEEDBACK
Q11. What is the best thing about working here?
    [Free text]

Q12. What is one thing you would change?
    [Free text]
```

### Market Research Survey

```
MARKET RESEARCH SURVEY
Estimated time: 5 minutes

AWARENESS & USAGE
Q1. Which of the following [product category] brands are
    you aware of? (Select all that apply)
    [ ] [Brand A]  [ ] [Brand B]  [ ] [Brand C]
    [ ] [Brand D]  [ ] None of the above

Q2. Which brand do you currently use most often?
    ( ) [Brand A]  ( ) [Brand B]  ( ) [Brand C]
    ( ) [Brand D]  ( ) I don't use any

Q3. How often do you use [product category]?
    ( ) Daily  ( ) Weekly  ( ) Monthly
    ( ) Rarely  ( ) Never

PURCHASE DRIVERS
Q4. Rank the following factors by importance when choosing
    a [product category]: (1 = most important)
    ___ Price  ___ Quality  ___ Brand reputation
    ___ Features  ___ Ease of use  ___ Customer support

Q5. What is your typical budget for [product category]?
    ( ) Under $X  ( ) $X-$Y  ( ) $Y-$Z  ( ) Over $Z

CONCEPT TESTING
Q6. [Show concept] How interested would you be in this product?
    ( ) Not at all  ( ) Slightly  ( ) Moderately
    ( ) Very  ( ) Extremely

Q7. What price would you expect to pay for this product?
    [$___________]

DEMOGRAPHICS
Q8-Q10. [Age range, role, company size]
```

## Analysis Guide

| Metric               | Calculation                                    | Benchmark           |
|----------------------|------------------------------------------------|----------------------|
| NPS Score            | % Promoters (9-10) minus % Detractors (0-6)   | >50 excellent        |
| CSAT Score           | % satisfied (4-5) / total responses            | >80% good            |
| Response Rate        | Completed / Invited * 100                      | >30% acceptable      |
| Completion Rate      | Completed / Started * 100                      | >80% good            |
| Engagement Index     | Mean of engagement questions                   | >3.8/5.0 healthy     |
| Statistical Significance | p < 0.05 for group comparisons             | Use chi-square or t-test |

## Workflow

1. **Define objectives**: What decisions will this data inform?
2. **Identify audience**: Who should respond, how many, how to reach them
3. **Select template**: Choose the closest template and customize
4. **Write questions**: Apply BRUSO framework, check for bias
5. **Design flow**: Order questions logically, add skip logic
6. **Pilot test**: Test with 5-10 people, measure time and confusion
7. **Launch**: Send with personalized invitations at optimal time
8. **Monitor**: Track response rate, send reminders
9. **Analyze**: Calculate metrics, segment results, identify themes
10. **Report**: Present findings with recommendations

## Scripts & Tools

**Generate survey skeleton**:
```bash
scripts/survey-builder.sh --type customer-feedback --questions 10 --output survey.json
```

**Bias checker**:
```bash
scripts/bias-check.sh --input survey.json --output bias-report.md
```

**Response analysis**:
```bash
scripts/survey-analyze.sh --responses responses.csv --type nps --output analysis.md
```

## Best Practices

- Test every survey on mobile before launching; over 60% of responses come from mobile devices.
- Limit surveys to 10-15 questions or 5 minutes, whichever comes first.
- Always include a "prefer not to answer" option for sensitive questions.
- Use consistent scales throughout the survey; do not mix 5-point and 7-point scales.
- Randomize option order for multiple choice questions to avoid position bias.
- Pilot test with a small group to identify confusing questions before full launch.
- Plan your analysis before writing questions; every question should map to an insight.
- Send reminders at 3-day intervals, up to a maximum of 3 reminders.
- Report results back to respondents to build trust for future surveys.
