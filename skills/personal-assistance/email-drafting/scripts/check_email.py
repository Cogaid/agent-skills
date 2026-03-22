#!/usr/bin/env python3
"""
Check email quality before sending.

Usage:
    python check_email.py email.txt
    python check_email.py --text "Email content here"

Output: JSON with analysis and suggestions
"""

import argparse
import json
import re
import sys


# Phrases to avoid
WEAK_PHRASES = [
    "i hope this email finds you well",
    "i just wanted to",
    "i was wondering if",
    "please don't hesitate",
    "per my last email",
    "as per our discussion",
    "i wanted to reach out",
    "i'm just following up",
    "sorry to bother you",
    "if you have a chance",
    "when you get a moment",
    "no rush",
    "at your earliest convenience",
]

WORDY_PHRASES = {
    "in order to": "to",
    "due to the fact that": "because",
    "at this point in time": "now",
    "in the event that": "if",
    "for the purpose of": "to",
    "in the near future": "soon",
    "at the present time": "currently",
    "in spite of the fact that": "although",
    "with regard to": "about",
    "in the process of": "currently",
}


def analyze_email(text):
    """Analyze email for quality issues."""

    lines = text.strip().split('\n')
    words = text.split()
    word_count = len(words)
    sentences = len(re.split(r'[.!?]+', text))

    issues = []
    suggestions = []

    # Check subject line (assume first line might be subject)
    first_line = lines[0].lower() if lines else ""
    if first_line.startswith("subject:"):
        subject = first_line.replace("subject:", "").strip()
        if len(subject) < 5:
            issues.append("Subject line too short")
        if len(subject) > 60:
            suggestions.append("Consider shortening subject line")
        if subject in ["hi", "hello", "quick question", "question", "help"]:
            issues.append("Subject line too vague")

    # Check for weak phrases
    text_lower = text.lower()
    found_weak = []
    for phrase in WEAK_PHRASES:
        if phrase in text_lower:
            found_weak.append(phrase)

    if found_weak:
        suggestions.append({
            "type": "weak_phrases",
            "message": "Consider removing these phrases",
            "phrases": found_weak
        })

    # Check for wordy phrases
    found_wordy = []
    for wordy, concise in WORDY_PHRASES.items():
        if wordy in text_lower:
            found_wordy.append({"wordy": wordy, "replace_with": concise})

    if found_wordy:
        suggestions.append({
            "type": "wordy_phrases",
            "message": "Consider these replacements",
            "replacements": found_wordy
        })

    # Check email length
    if word_count > 300:
        suggestions.append({
            "type": "length",
            "message": f"Email is {word_count} words. Consider shortening to under 300."
        })
    elif word_count < 20:
        suggestions.append({
            "type": "length",
            "message": "Email seems very short. Ensure all necessary context is included."
        })

    # Check for clear call to action
    action_words = ["please", "could you", "can you", "would you", "let me know"]
    has_cta = any(phrase in text_lower for phrase in action_words)
    question_marks = text.count("?")

    if not has_cta and question_marks == 0:
        suggestions.append({
            "type": "cta",
            "message": "No clear call-to-action found. What do you want them to do?"
        })

    # Check for deadline/date
    date_pattern = r'\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday|today|tomorrow|eod|cob|\d{1,2}[/-]\d{1,2}|\d{1,2}th|\d{1,2}st|\d{1,2}nd)\b'
    has_date = bool(re.search(date_pattern, text_lower))

    if has_cta and not has_date:
        suggestions.append({
            "type": "deadline",
            "message": "Consider adding a specific deadline for your request"
        })

    # Check readability (avg sentence length)
    avg_sentence = word_count / sentences if sentences > 0 else 0
    if avg_sentence > 25:
        suggestions.append({
            "type": "readability",
            "message": f"Average sentence is {avg_sentence:.0f} words. Consider breaking up long sentences."
        })

    # Check for attachments mentioned but might be missing
    attachment_words = ["attached", "attachment", "enclosed", "find attached"]
    mentions_attachment = any(word in text_lower for word in attachment_words)

    if mentions_attachment:
        suggestions.append({
            "type": "reminder",
            "message": "Email mentions attachment - make sure it's actually attached!"
        })

    # Calculate quality score
    score = 100
    score -= len(issues) * 15
    score -= len(suggestions) * 5
    score = max(0, min(100, score))

    # Determine status
    if issues:
        status = "NEEDS_FIXES"
    elif len(suggestions) > 3:
        status = "REVIEW_RECOMMENDED"
    else:
        status = "GOOD_TO_SEND"

    return {
        "status": status,
        "quality_score": score,
        "statistics": {
            "word_count": word_count,
            "sentence_count": sentences,
            "avg_sentence_length": round(avg_sentence, 1),
            "line_count": len(lines)
        },
        "issues": issues,
        "suggestions": suggestions
    }


def main():
    parser = argparse.ArgumentParser(description="Check email quality")
    parser.add_argument("file", nargs="?", help="Email file to check")
    parser.add_argument("--text", "-t", help="Email text directly")

    args = parser.parse_args()

    if args.text:
        text = args.text
    elif args.file:
        try:
            with open(args.file, 'r') as f:
                text = f.read()
        except FileNotFoundError:
            print(json.dumps({"error": f"File not found: {args.file}"}))
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(1)

    result = analyze_email(text)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
