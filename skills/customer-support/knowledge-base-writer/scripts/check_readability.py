#!/usr/bin/env python3
"""
Check readability of knowledge base articles.

Usage:
    python check_readability.py article.md
    python check_readability.py "article text here"
    cat article.md | python check_readability.py --stdin

Output: JSON with readability metrics and suggestions
"""

import argparse
import json
import re
import sys
from collections import Counter


def count_syllables(word: str) -> int:
    """Estimate syllable count for a word."""
    word = word.lower().strip()
    if len(word) <= 3:
        return 1

    # Remove silent e at end
    if word.endswith('e'):
        word = word[:-1]

    # Count vowel groups
    vowels = "aeiouy"
    count = 0
    prev_vowel = False

    for char in word:
        is_vowel = char in vowels
        if is_vowel and not prev_vowel:
            count += 1
        prev_vowel = is_vowel

    return max(1, count)


def extract_text(content: str) -> str:
    """Extract plain text from markdown."""
    # Remove code blocks
    text = re.sub(r'```[\s\S]*?```', '', content)
    text = re.sub(r'`[^`]+`', '', text)

    # Remove headers (keep text)
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)

    # Remove links but keep text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)

    # Remove images
    text = re.sub(r'!\[[^\]]*\]\([^)]+\)', '', text)

    # Remove horizontal rules
    text = re.sub(r'^[-*_]{3,}$', '', text, flags=re.MULTILINE)

    # Remove bullet points and list markers
    text = re.sub(r'^\s*[-*+]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*\d+\.\s+', '', text, flags=re.MULTILINE)

    # Remove bold/italic markers
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]+)\*', r'\1', text)

    # Clean up extra whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()

    return text


def get_sentences(text: str) -> list:
    """Split text into sentences."""
    # Simple sentence splitting
    sentences = re.split(r'[.!?]+', text)
    return [s.strip() for s in sentences if s.strip() and len(s.strip()) > 5]


def get_words(text: str) -> list:
    """Extract words from text."""
    return re.findall(r'\b[a-zA-Z]+\b', text.lower())


def calculate_flesch_kincaid(words: list, sentences: list, syllables: int) -> float:
    """Calculate Flesch-Kincaid Grade Level."""
    if not sentences or not words:
        return 0

    words_per_sentence = len(words) / len(sentences)
    syllables_per_word = syllables / len(words)

    grade = 0.39 * words_per_sentence + 11.8 * syllables_per_word - 15.59
    return round(max(0, grade), 1)


def calculate_flesch_reading_ease(words: list, sentences: list, syllables: int) -> float:
    """Calculate Flesch Reading Ease score."""
    if not sentences or not words:
        return 0

    words_per_sentence = len(words) / len(sentences)
    syllables_per_word = syllables / len(words)

    score = 206.835 - 1.015 * words_per_sentence - 84.6 * syllables_per_word
    return round(max(0, min(100, score)), 1)


def find_complex_words(words: list) -> list:
    """Find words with 3+ syllables."""
    complex_words = []
    for word in set(words):
        if count_syllables(word) >= 3 and len(word) >= 7:
            complex_words.append(word)
    return sorted(complex_words)[:10]


def find_long_sentences(sentences: list) -> list:
    """Find sentences longer than 25 words."""
    long = []
    for sent in sentences:
        word_count = len(sent.split())
        if word_count > 25:
            long.append({
                "sentence": sent[:100] + "..." if len(sent) > 100 else sent,
                "word_count": word_count
            })
    return long[:5]


def check_passive_voice(sentences: list) -> list:
    """Detect potential passive voice constructions."""
    passive_patterns = [
        r'\b(was|were|is|are|been|being|be)\s+\w+ed\b',
        r'\b(was|were|is|are|been|being|be)\s+\w+en\b'
    ]

    passive_sentences = []
    for sent in sentences:
        for pattern in passive_patterns:
            if re.search(pattern, sent.lower()):
                passive_sentences.append(sent[:80] + "..." if len(sent) > 80 else sent)
                break

    return passive_sentences[:5]


def analyze_readability(content: str) -> dict:
    """Main analysis function."""
    text = extract_text(content)
    sentences = get_sentences(text)
    words = get_words(text)

    total_syllables = sum(count_syllables(w) for w in words)

    # Calculate metrics
    fk_grade = calculate_flesch_kincaid(words, sentences, total_syllables)
    fre_score = calculate_flesch_reading_ease(words, sentences, total_syllables)
    avg_sentence_length = round(len(words) / max(len(sentences), 1), 1)
    avg_word_length = round(sum(len(w) for w in words) / max(len(words), 1), 1)

    # Find issues
    complex_words = find_complex_words(words)
    long_sentences = find_long_sentences(sentences)
    passive_voice = check_passive_voice(sentences)

    # Generate suggestions
    suggestions = []

    if fk_grade > 8:
        suggestions.append(f"Readability is grade {fk_grade}. Target grade 6-8 for KB articles.")

    if avg_sentence_length > 20:
        suggestions.append(f"Average sentence length is {avg_sentence_length} words. Target 15-20.")

    if long_sentences:
        suggestions.append(f"Found {len(long_sentences)} sentences over 25 words. Consider splitting.")

    if complex_words:
        suggestions.append(f"Consider simpler alternatives for: {', '.join(complex_words[:5])}")

    if passive_voice:
        suggestions.append(f"Found {len(passive_voice)} potential passive voice sentences. Use active voice.")

    # Determine pass/fail
    passed = fk_grade <= 8 and avg_sentence_length <= 20

    return {
        "metrics": {
            "flesch_kincaid_grade": fk_grade,
            "flesch_reading_ease": fre_score,
            "average_sentence_length": avg_sentence_length,
            "average_word_length": avg_word_length,
            "total_sentences": len(sentences),
            "total_words": len(words)
        },
        "issues": {
            "complex_words": complex_words,
            "long_sentences": long_sentences,
            "passive_voice": passive_voice
        },
        "suggestions": suggestions,
        "passed": passed,
        "grade": "PASS" if passed else "NEEDS IMPROVEMENT"
    }


def main():
    parser = argparse.ArgumentParser(description="Check article readability")
    parser.add_argument("input", nargs="?", help="Markdown file or text")
    parser.add_argument("--stdin", action="store_true", help="Read from stdin")
    parser.add_argument("--pretty", "-p", action="store_true", help="Pretty print")

    args = parser.parse_args()

    # Get input
    if args.stdin:
        content = sys.stdin.read()
    elif args.input:
        if args.input.endswith('.md') or args.input.endswith('.txt'):
            with open(args.input, 'r') as f:
                content = f.read()
        else:
            content = args.input
    else:
        parser.print_help()
        sys.exit(1)

    result = analyze_readability(content)

    if args.pretty:
        print(json.dumps(result, indent=2))
    else:
        print(json.dumps(result))

    sys.exit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
