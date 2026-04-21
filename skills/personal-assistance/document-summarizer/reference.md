# Document Summarizer - Reference Guide

## CORE Framework - Detailed

The CORE framework provides a systematic approach to summarization:

### C - Context

Establish what the document is before summarizing it.

| Question | Why It Matters |
|----------|---------------|
| What type of document is this? | Determines summary structure |
| Who wrote it and when? | Establishes authority and timeliness |
| Who is the intended audience? | Adjusts summary depth and jargon level |
| What is the publication context? | Provides background for interpretation |

### O - Objective

Identify the document's main point or thesis.

| Document Type | How to Find the Objective |
|--------------|--------------------------|
| Research paper | Abstract, last paragraph of introduction |
| Business report | Executive summary, first paragraph |
| News article | Lead paragraph (inverted pyramid) |
| Book | Introduction/preface, back cover |
| Email thread | Subject line, first email in thread |
| Legal document | Recitals section, purpose clause |

### R - Relevant Points

Extract supporting arguments, evidence, and key data.

Relevance filters:
1. Does this point support or challenge the main objective?
2. Would the reader's understanding change without this point?
3. Is this a fact, opinion, or interpretation?
4. Is this point unique to this document or common knowledge?

### E - Extract Actions

Identify what the reader should do with the information.

| Action Type | Examples |
|-------------|----------|
| Direct action | "Approve by Friday", "Review section 3" |
| Implied action | Market shift suggests strategy change |
| No action | Purely informational, for awareness only |
| Decision required | Multiple options presented, choice needed |

## Summary Approaches - Deep Dive

### Extractive Summarization

Pull the most important sentences directly from the source.

**When to use:** Technical documents, legal text, anything where exact wording matters.

**Technique:**
1. Score each sentence by: position (first/last paragraphs weighted higher), keyword density, named entity presence
2. Select top N sentences by score
3. Reorder in original document order
4. Add transitions if needed

**Strengths:** Preserves original language, verifiable against source
**Weaknesses:** Can feel choppy, may miss implied meaning

### Abstractive Summarization

Rewrite the content in your own words, synthesizing meaning.

**When to use:** Narratives, complex arguments, when the audience differs from the original.

**Technique:**
1. Read the full document
2. Close the document
3. Write what you remember as the key points
4. Verify against original for accuracy
5. Fill in missed critical points

**Strengths:** More natural reading flow, can adjust complexity level
**Weaknesses:** Risk of misinterpretation, harder to verify

### Structured Summarization

Organize content into a predefined structure with headers and bullets.

**When to use:** Reports, research papers, meeting notes, any document that will be skimmed.

**Technique:**
1. Define the output structure before reading
2. Map document sections to output sections
3. Fill in each section with extracted or abstracted content
4. Ensure no critical information falls between sections

### Comparative Summarization

Summarize multiple documents side by side.

**When to use:** Literature reviews, vendor comparisons, competitive analysis.

**Technique:**
1. Identify common dimensions across documents
2. Create a comparison matrix
3. Note where documents agree, disagree, or are silent
4. Synthesize overall findings

## Length Calibration Guide

### Word Count Targets

| Original Length | Summary Type | Target Words | Compression Ratio |
|-----------------|-------------|-------------|-------------------|
| Under 500 words | One-liner | 15-25 | 20:1 |
| 500-1,000 words | Executive | 50-100 | 10:1 |
| 1,000-5,000 words | Standard | 150-300 | 10:1 to 15:1 |
| 5,000-10,000 words | Detailed | 300-600 | 15:1 |
| 10,000-25,000 words | Comprehensive | 500-1,000 | 20:1 |
| 25,000+ words (book) | Comprehensive | 1,000-2,000 | 25:1+ |

### Audience-Based Adjustment

| Audience | Adjustment |
|----------|------------|
| Executive / C-suite | Shortest possible. Bottom line first. Actions highlighted. |
| Manager | Standard length. Context + implications + actions. |
| Peer / Colleague | Standard to detailed. Include methodology and evidence. |
| External stakeholder | Standard. Avoid internal jargon. Include background context. |
| Archival / Reference | Comprehensive. Preserve all key data points. |

## Quality Assurance Checklist

### Accuracy Check

- [ ] Main point is correctly stated
- [ ] Key statistics and data are accurate
- [ ] No claims are attributed to wrong sources
- [ ] Nuances and caveats are preserved
- [ ] Nothing is presented out of context

### Completeness Check

- [ ] All major topics are covered
- [ ] Critical data points are included
- [ ] Counter-arguments or limitations are noted
- [ ] Action items are captured
- [ ] Source is properly cited

### Clarity Check

- [ ] Summary can be understood without reading the original
- [ ] Technical terms are explained or audience-appropriate
- [ ] Structure follows a logical flow
- [ ] No ambiguous pronouns or references
- [ ] Length is appropriate for the audience

### Bias Check

- [ ] Summary reflects the document's position, not the summarizer's
- [ ] Interpretations are clearly labeled as such
- [ ] Both sides of arguments are represented
- [ ] Selective quoting does not distort meaning

## Common Pitfalls

| Pitfall | Description | Prevention |
|---------|-------------|------------|
| Cherry-picking | Only including points that support a view | Summarize the full argument arc |
| Over-compression | Losing critical nuance | Match length to complexity |
| Jargon creep | Using terms the audience doesn't know | Define or simplify technical terms |
| Missing the "so what" | Stating facts without implications | Always include an implications/action section |
| Stale summaries | Summarizing outdated information | Always note the document date and recency |
| Paragraph copying | Taking large chunks verbatim | Use extractive approach intentionally, not lazily |

## Citation Formats

| Style | Format |
|-------|--------|
| Inline | According to [Author] ([Year])... |
| Footnote | Main claim.[1] |
| APA | Author, A. A. (Year). Title. Source. |
| Link | [Title](URL) - accessed [Date] |
