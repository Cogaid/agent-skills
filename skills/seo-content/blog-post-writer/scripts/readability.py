#!/usr/bin/env python3
"""
Check content readability and provide improvement suggestions.

Usage:
    python readability.py post.md
    python readability.py post.md --target-grade 8

Output: Readability analysis with suggestions
"""

import argparse
import json
import re
import sys


def count_syllables(word):
    """Count syllables in a word (simplified)."""
    word = word.lower().strip()
    if not word:
        return 0

    vowels = "aeiou"
    count = 0
    prev_was_vowel = False

    for char in word:
        is_vowel = char in vowels
        if is_vowel and not prev_was_vowel:
            count += 1
        prev_was_vowel = is_vowel

    # Handle silent e
    if word.endswith('e') and count > 1:
        count -= 1

    # Handle -le endings
    if word.endswith('le') and len(word) > 2 and word[-3] not in vowels:
        count += 1

    return max(1, count)


def extract_text(content):
    """Extract plain text from markdown."""
    # Remove code blocks
    text = re.sub(r'```[\s\S]*?```', '', content)
    text = re.sub(r'`[^`]+`', '', text)

    # Remove images
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)

    # Remove links but keep text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)

    # Remove headers markers
    text = re.sub(r'^#+\s+', '', text, flags=re.MULTILINE)

    # Remove emphasis markers
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]+)\*', r'\1', text)
    text = re.sub(r'__([^_]+)__', r'\1', text)
    text = re.sub(r'_([^_]+)_', r'\1', text)

    # Remove horizontal rules
    text = re.sub(r'^---+$', '', text, flags=re.MULTILINE)

    # Remove list markers
    text = re.sub(r'^\s*[-*+]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*\d+\.\s+', '', text, flags=re.MULTILINE)

    # Remove blockquotes
    text = re.sub(r'^\s*>\s+', '', text, flags=re.MULTILINE)

    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)

    # Clean up whitespace
    text = re.sub(r'\n\s*\n', '\n\n', text)

    return text.strip()


def get_sentences(text):
    """Split text into sentences."""
    # Basic sentence splitting
    sentences = re.split(r'[.!?]+', text)
    return [s.strip() for s in sentences if s.strip() and len(s.split()) > 2]


def get_words(text):
    """Extract words from text."""
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    return words


def calculate_flesch_kincaid(sentences, words):
    """Calculate Flesch-Kincaid Grade Level."""
    if not sentences or not words:
        return 0

    total_syllables = sum(count_syllables(word) for word in words)

    asl = len(words) / len(sentences)  # Average sentence length
    asw = total_syllables / len(words)  # Average syllables per word

    # Flesch-Kincaid Grade Level
    fk_grade = 0.39 * asl + 11.8 * asw - 15.59
    return max(0, min(20, fk_grade))


def calculate_flesch_reading_ease(sentences, words):
    """Calculate Flesch Reading Ease score."""
    if not sentences or not words:
        return 0

    total_syllables = sum(count_syllables(word) for word in words)

    asl = len(words) / len(sentences)
    asw = total_syllables / len(words)

    fre = 206.835 - 1.015 * asl - 84.6 * asw
    return max(0, min(100, fre))


def find_complex_sentences(sentences, threshold=25):
    """Find sentences that are too long."""
    complex_sentences = []
    for sentence in sentences:
        word_count = len(sentence.split())
        if word_count > threshold:
            complex_sentences.append({
                "sentence": sentence[:100] + "..." if len(sentence) > 100 else sentence,
                "word_count": word_count,
                "recommendation": "Consider breaking into 2-3 shorter sentences"
            })
    return complex_sentences


def find_complex_words(words, syllable_threshold=4):
    """Find words with many syllables."""
    complex_words = {}
    for word in words:
        syllables = count_syllables(word)
        if syllables >= syllable_threshold and len(word) > 6:
            if word not in complex_words:
                complex_words[word] = {"syllables": syllables, "count": 0}
            complex_words[word]["count"] += 1

    # Sort by frequency
    sorted_words = sorted(complex_words.items(), key=lambda x: x[1]["count"], reverse=True)
    return dict(sorted_words[:20])


def find_passive_voice(sentences):
    """Detect potential passive voice usage."""
    passive_patterns = [
        r'\b(was|were|is|are|been|being)\s+\w+ed\b',
        r'\b(was|were|is|are|been|being)\s+\w+en\b',
    ]

    passive_sentences = []
    for sentence in sentences:
        for pattern in passive_patterns:
            if re.search(pattern, sentence.lower()):
                passive_sentences.append({
                    "sentence": sentence[:100] + "..." if len(sentence) > 100 else sentence,
                    "recommendation": "Consider rewriting in active voice"
                })
                break

    return passive_sentences[:10]


def get_grade_description(grade):
    """Get human-readable description of grade level."""
    if grade <= 5:
        return "Very Easy (5th grade or below)"
    elif grade <= 6:
        return "Easy (6th grade)"
    elif grade <= 8:
        return "Fairly Easy (7th-8th grade) - Ideal for most content"
    elif grade <= 10:
        return "Standard (9th-10th grade)"
    elif grade <= 12:
        return "Fairly Difficult (11th-12th grade)"
    else:
        return "Difficult (College level)"


def analyze_readability(content, target_grade=8):
    """Perform comprehensive readability analysis."""
    text = extract_text(content)
    sentences = get_sentences(text)
    words = get_words(text)

    if not sentences or not words:
        return {"error": "Not enough content to analyze"}

    # Calculate metrics
    fk_grade = calculate_flesch_kincaid(sentences, words)
    fre_score = calculate_flesch_reading_ease(sentences, words)

    # Find issues
    complex_sentences = find_complex_sentences(sentences)
    complex_words = find_complex_words(words)
    passive_voice = find_passive_voice(sentences)

    # Calculate statistics
    word_count = len(words)
    sentence_count = len(sentences)
    avg_sentence_length = word_count / sentence_count if sentence_count else 0
    avg_word_length = sum(len(w) for w in words) / len(words) if words else 0

    # Generate recommendations
    recommendations = []

    if fk_grade > target_grade + 2:
        recommendations.append({
            "priority": "high",
            "issue": f"Grade level ({fk_grade:.1f}) is above target ({target_grade})",
            "suggestion": "Simplify vocabulary and shorten sentences"
        })

    if avg_sentence_length > 20:
        recommendations.append({
            "priority": "medium",
            "issue": f"Average sentence length ({avg_sentence_length:.1f}) is too long",
            "suggestion": "Break long sentences into shorter ones (target: 15-20 words)"
        })

    if complex_sentences:
        recommendations.append({
            "priority": "medium",
            "issue": f"Found {len(complex_sentences)} overly complex sentences",
            "suggestion": "Review and simplify flagged sentences"
        })

    if len(passive_voice) > sentence_count * 0.1:
        recommendations.append({
            "priority": "low",
            "issue": "Excessive passive voice usage",
            "suggestion": "Convert passive sentences to active voice"
        })

    # Calculate overall score
    readability_score = 100
    if fk_grade > target_grade:
        readability_score -= min(30, (fk_grade - target_grade) * 5)
    if avg_sentence_length > 20:
        readability_score -= min(20, (avg_sentence_length - 20) * 2)
    if complex_sentences:
        readability_score -= min(20, len(complex_sentences) * 2)

    readability_score = max(0, readability_score)

    return {
        "summary": {
            "readability_score": round(readability_score),
            "flesch_kincaid_grade": round(fk_grade, 1),
            "grade_description": get_grade_description(fk_grade),
            "flesch_reading_ease": round(fre_score, 1),
            "target_grade": target_grade,
            "meets_target": fk_grade <= target_grade + 1
        },
        "statistics": {
            "word_count": word_count,
            "sentence_count": sentence_count,
            "avg_sentence_length": round(avg_sentence_length, 1),
            "avg_word_length": round(avg_word_length, 1)
        },
        "issues": {
            "complex_sentences": complex_sentences[:5],
            "complex_words": complex_words,
            "passive_voice": passive_voice[:5]
        },
        "recommendations": recommendations
    }


def main():
    parser = argparse.ArgumentParser(description="Analyze content readability")
    parser.add_argument("file", help="Content file to analyze")
    parser.add_argument("--target-grade", "-t", type=int, default=8,
                        help="Target grade level (default: 8)")
    parser.add_argument("--format", "-f", choices=["json", "summary"],
                        default="json", help="Output format")

    args = parser.parse_args()

    try:
        with open(args.file, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(json.dumps({"error": f"File not found: {args.file}"}))
        sys.exit(1)

    result = analyze_readability(content, args.target_grade)

    if args.format == "summary":
        print("\n=== Readability Analysis ===\n")

        summary = result["summary"]
        print(f"Readability Score: {summary['readability_score']}/100")
        print(f"Grade Level: {summary['flesch_kincaid_grade']} ({summary['grade_description']})")
        print(f"Target Grade: {summary['target_grade']}")
        print(f"Meets Target: {'✓ Yes' if summary['meets_target'] else '✗ No'}")

        stats = result["statistics"]
        print(f"\nWord Count: {stats['word_count']}")
        print(f"Sentences: {stats['sentence_count']}")
        print(f"Avg Sentence Length: {stats['avg_sentence_length']} words")

        if result["recommendations"]:
            print("\n=== Recommendations ===\n")
            for rec in result["recommendations"]:
                print(f"[{rec['priority'].upper()}] {rec['issue']}")
                print(f"  → {rec['suggestion']}")

        if result["issues"]["complex_sentences"]:
            print(f"\n=== Complex Sentences ({len(result['issues']['complex_sentences'])} found) ===\n")
            for cs in result["issues"]["complex_sentences"][:3]:
                print(f"• {cs['sentence']}")
                print(f"  ({cs['word_count']} words)")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
