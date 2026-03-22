#!/usr/bin/env python3
"""
Audit content for SEO and quality issues.

Usage:
    python content_audit.py page.md --keyword "target keyword"

Output: JSON with comprehensive audit results
"""

import argparse
import json
import re
import sys


def calculate_readability(content):
    """Calculate simple readability metrics."""
    words = content.split()
    sentences = len(re.split(r'[.!?]+', content))
    syllables = sum(count_syllables(word) for word in words)

    if sentences == 0 or len(words) == 0:
        return {"error": "Not enough content to analyze"}

    # Flesch-Kincaid Grade Level (simplified)
    asl = len(words) / sentences  # Average sentence length
    asw = syllables / len(words)  # Average syllables per word

    fk_grade = 0.39 * asl + 11.8 * asw - 15.59
    fk_grade = max(0, min(20, fk_grade))  # Clamp to reasonable range

    # Flesch Reading Ease
    fre = 206.835 - 1.015 * asl - 84.6 * asw
    fre = max(0, min(100, fre))

    return {
        "flesch_kincaid_grade": round(fk_grade, 1),
        "flesch_reading_ease": round(fre, 1),
        "avg_sentence_length": round(asl, 1),
        "avg_syllables_per_word": round(asw, 2),
        "total_words": len(words),
        "total_sentences": sentences
    }


def count_syllables(word):
    """Count syllables in a word (simplified)."""
    word = word.lower()
    vowels = "aeiou"
    count = 0
    prev_was_vowel = False

    for char in word:
        is_vowel = char in vowels
        if is_vowel and not prev_was_vowel:
            count += 1
        prev_was_vowel = is_vowel

    # Handle silent e
    if word.endswith('e'):
        count -= 1

    return max(1, count)


def extract_structure(content):
    """Extract content structure."""
    return {
        'h1': re.findall(r'^#\s+(.+)$', content, re.MULTILINE),
        'h2': re.findall(r'^##\s+(.+)$', content, re.MULTILINE),
        'h3': re.findall(r'^###\s+(.+)$', content, re.MULTILINE),
        'lists': len(re.findall(r'^\s*[-*]\s', content, re.MULTILINE)),
        'images': len(re.findall(r'!\[', content)),
        'links': len(re.findall(r'\[([^\]]+)\]\(', content)),
    }


def check_keyword(content, keyword):
    """Check keyword usage."""
    if not keyword:
        return None

    keyword_lower = keyword.lower()
    content_lower = content.lower()
    words = content.split()

    # Extract title
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1).lower() if title_match else ""

    # First 100 words
    first_100 = ' '.join(words[:100]).lower()

    # H2 headers
    h2s = re.findall(r'^##\s+(.+)$', content, re.MULTILINE)
    h2_text = ' '.join(h2s).lower()

    count = content_lower.count(keyword_lower)
    density = (count / len(words) * 100) if words else 0

    return {
        "keyword": keyword,
        "total_count": count,
        "density_percent": round(density, 2),
        "in_title": keyword_lower in title,
        "in_first_100_words": keyword_lower in first_100,
        "in_h2": keyword_lower in h2_text,
    }


def identify_issues(content, structure, readability, keyword_analysis):
    """Identify content issues."""
    issues = []
    suggestions = []
    scores = {
        "seo": 100,
        "readability": 100,
        "structure": 100
    }

    # SEO issues
    if keyword_analysis:
        if not keyword_analysis["in_title"]:
            issues.append("Target keyword not in title")
            scores["seo"] -= 20

        if not keyword_analysis["in_first_100_words"]:
            suggestions.append("Add target keyword to first 100 words")
            scores["seo"] -= 10

        if not keyword_analysis["in_h2"]:
            suggestions.append("Add target keyword to at least one H2")
            scores["seo"] -= 10

        if keyword_analysis["density_percent"] > 3:
            issues.append("Keyword density too high (over-optimization)")
            scores["seo"] -= 15

    # Structure issues
    if len(structure['h1']) == 0:
        issues.append("Missing H1 heading")
        scores["structure"] -= 20
    elif len(structure['h1']) > 1:
        issues.append(f"Multiple H1 headings ({len(structure['h1'])})")
        scores["structure"] -= 15

    if len(structure['h2']) < 3:
        suggestions.append("Add more H2 subheadings for better structure")
        scores["structure"] -= 10

    if structure['images'] == 0:
        suggestions.append("Add images to improve engagement")
        scores["structure"] -= 5

    if structure['links'] < 2:
        suggestions.append("Add more internal/external links")
        scores["seo"] -= 10

    # Readability issues
    if readability.get("flesch_kincaid_grade", 0) > 12:
        issues.append("Content too complex (grade level too high)")
        scores["readability"] -= 20
    elif readability.get("flesch_kincaid_grade", 0) > 10:
        suggestions.append("Consider simplifying language for broader audience")
        scores["readability"] -= 10

    if readability.get("avg_sentence_length", 0) > 25:
        suggestions.append("Shorten sentences for better readability")
        scores["readability"] -= 10

    # Word count
    word_count = readability.get("total_words", 0)
    if word_count < 500:
        issues.append(f"Content too short ({word_count} words)")
        scores["seo"] -= 15
    elif word_count < 800:
        suggestions.append("Consider expanding content for more depth")

    # Calculate overall score
    overall = round((scores["seo"] + scores["readability"] + scores["structure"]) / 3)

    return {
        "issues": issues,
        "suggestions": suggestions,
        "scores": {
            "seo": max(0, scores["seo"]),
            "readability": max(0, scores["readability"]),
            "structure": max(0, scores["structure"]),
            "overall": max(0, overall)
        }
    }


def audit_content(content, keyword=None):
    """Perform full content audit."""

    structure = extract_structure(content)
    readability = calculate_readability(content)
    keyword_analysis = check_keyword(content, keyword)
    analysis = identify_issues(content, structure, readability, keyword_analysis)

    return {
        "summary": {
            "overall_score": analysis["scores"]["overall"],
            "word_count": readability.get("total_words", 0),
            "reading_grade": readability.get("flesch_kincaid_grade", 0),
            "issues_count": len(analysis["issues"]),
            "suggestions_count": len(analysis["suggestions"])
        },
        "scores": analysis["scores"],
        "structure": structure,
        "readability": readability,
        "keyword_analysis": keyword_analysis,
        "issues": analysis["issues"],
        "suggestions": analysis["suggestions"]
    }


def main():
    parser = argparse.ArgumentParser(description="Audit content")
    parser.add_argument("file", help="Content file to audit")
    parser.add_argument("--keyword", "-k", help="Target keyword")

    args = parser.parse_args()

    try:
        with open(args.file, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(json.dumps({"error": f"File not found: {args.file}"}))
        sys.exit(1)

    result = audit_content(content, args.keyword)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
