# Knowledge Base Writer Reference

## Contents
- Style Guide
- SEO Guidelines
- Article Structure
- Quality Standards

---

## Style Guide

### Voice and Tone

| Do | Don't |
|----|-------|
| "Click the Settings icon" | "You should click on the Settings icon" |
| "Enter your email" | "Please enter your email address" |
| "The file uploads" | "The file will be uploaded" |
| "You can export data" | "Users are able to export data" |

**Key principles**:
- Second person ("you") not third person ("the user")
- Active voice, not passive
- Present tense when possible
- Confident, not hedging

### Vocabulary

**Use simple words**:
| Instead of | Use |
|------------|-----|
| utilize | use |
| facilitate | help |
| leverage | use |
| implement | set up |
| terminate | end |
| prior to | before |
| in order to | to |
| functionality | feature |

### Sentence Structure

- **Average sentence length**: 15-20 words
- **Maximum sentence length**: 30 words
- **Paragraph length**: 2-3 sentences
- **One idea per paragraph**

### Formatting

**Headers**:
- Use sentence case: "How to reset your password"
- Front-load keywords: "Password reset" not "How to reset"
- H1 for title only, H2 for main sections, H3 for subsections

**Lists**:
- Numbered for sequences (steps)
- Bullets for non-sequential items
- Parallel structure within lists
- Maximum 7 items per list

**Emphasis**:
- **Bold** for UI elements: Click **Save**
- `Code formatting` for values, commands, filenames
- *Italics* sparingly for new terms

---

## SEO Guidelines

### Title Optimization

- **Length**: 50-60 characters
- **Include primary keyword**
- **Match search intent**
- **Be specific**: "Reset your password" > "Account recovery"

**Title formulas**:
```
How to [Action] [Object]
[Problem]: [Solution]
[Feature]: Getting Started Guide
[Number] Ways to [Achieve Outcome]
```

### Meta Description

- **Length**: 150-160 characters
- **Include keyword naturally**
- **Describe what reader will learn**
- **Action-oriented**

**Example**:
```
Learn how to reset your password in 3 simple steps.
Works for both web and mobile app logins.
```

### Keyword Placement

- [ ] In title (first 3 words if possible)
- [ ] In first paragraph
- [ ] In at least one H2
- [ ] In image alt text
- [ ] In URL slug

### Internal Linking

- Link to related articles
- Use descriptive anchor text
- Link from high-traffic articles to new ones
- Update old articles to link to new ones

---

## Article Structure

### How-To Article Structure

```markdown
# How to [Action] [Object]

[One sentence: what this article helps you do]

## Before you start
- [Prerequisite 1]
- [Prerequisite 2]

## Steps

1. **[Verb] [object]**
   [Brief explanation]

2. **[Verb] [object]**
   [Brief explanation]

3. **[Verb] [object]**
   [Brief explanation]

## What happens next
[What user should see when done]

## Related articles
- [Link 1]
- [Link 2]
```

### Troubleshooting Article Structure

```markdown
# [Problem statement]

[Brief description of when users see this issue]

## Symptoms
- [What user sees]
- [Error message if applicable]

## Solution

### Quick fix
[Most common solution - fast]

### Alternative solutions

#### Option 1: [Name]
[Steps]

#### Option 2: [Name]
[Steps]

## Still having trouble?
[Contact support / escalation path]
```

### FAQ Article Structure

```markdown
# [Topic] FAQ

## [Question 1]?
[Answer - direct and complete]

## [Question 2]?
[Answer]

## [Question 3]?
[Answer]

## More questions?
[Contact / related articles]
```

---

## Quality Standards

### Readability Targets

| Metric | Target |
|--------|--------|
| Flesch-Kincaid Grade | 6-8 |
| Avg. Sentence Length | 15-20 words |
| Avg. Word Length | < 5 characters |
| Passive Voice | < 10% |

### Content Checklist

**Before publishing**:
- [ ] Title is specific and searchable
- [ ] Introduction states what article covers
- [ ] Steps are numbered and start with verbs
- [ ] One action per step
- [ ] Expected outcomes are clear
- [ ] Screenshots match current UI
- [ ] Links work
- [ ] No jargon without explanation

### Maintenance Schedule

| Frequency | Action |
|-----------|--------|
| Monthly | Review high-traffic articles |
| Quarterly | Full audit of top 50 articles |
| On product release | Update affected articles |
| On support spike | Check for needed updates |

### Update Triggers

- Product UI changes
- New feature launches
- Support ticket spike on topic
- Customer feedback
- Out-of-date information detected
