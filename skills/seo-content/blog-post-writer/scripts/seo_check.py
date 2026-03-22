#!/usr/bin/env python3
"""
Check on-page SEO for blog post content.

Usage:
    python seo_check.py post.md --keyword "target keyword"
    python seo_check.py post.md

Output: JSON with SEO score and suggestions
"""

import argparse
import json
import re
import sys


def extract_title(content):
    """Extract H1 title from content."""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    return match.group(1) if match else None


def extract_headers(content):
    """Extract all headers from content."""
    headers = {
        'h1': re.findall(r'^#\s+(.+)$', content, re.MULTILINE),
        'h2': re.findall(r'^##\s+(.+)$', content, re.MULTILINE),
        'h3': re.findall(r'^###\s+(.+)$', content, re.MULTILINE),
    }
    return headers


def extract_links(content):
    """Extract internal and external links."""
    # Markdown links: [text](url)
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)

    internal = [l for l in links if l[1].startswith('/') or l[1].startswith('#')]
    external = [l for l in links if l[1].startswith('http')]

    return {'internal': internal, 'external': external}


def check_keyword_usage(content, keyword):
    """Check keyword usage throughout content."""
    keyword_lower = keyword.lower()
    content_lower = content.lower()

    # Check various locations
    title = extract_title(content) or ""
    headers = extract_headers(content)
    first_100_words = ' '.join(content.split()[:100]).lower()

    return {
        'in_title': keyword_lower in title.lower(),
        'in_first_100_words': keyword_lower in first_100_words,
        'in_h2': any(keyword_lower in h.lower() for h in headers['h2']),
        'total_count': content_lower.count(keyword_lower),
        'keyword_density': round(
            content_lower.count(keyword_lower) / len(content.split()) * 100, 2
        ) if content.split() else 0
    }


def analyze_content(content, keyword=None):
    """Analyze content for SEO factors."""

    word_count = len(content.split())
    headers = extract_headers(content)
    links = extract_links(content)
    title = extract_title(content)

    issues = []
    suggestions = []
    score = 100

    # Title checks
    if not title:
        issues.append("Missing H1 title")
        score -= 15
    elif len(title) > 70:
        suggestions.append(f"Title is {len(title)} chars. Consider shortening to under 60.")
        score -= 5

    # Header structure
    if len(headers['h1']) > 1:
        issues.append(f"Multiple H1 tags found ({len(headers['h1'])}). Should have only one.")
        score -= 10

    if len(headers['h2']) < 2:
        suggestions.append("Consider adding more H2 subheadings for structure.")
        score -= 5

    # Word count
    if word_count < 500:
        suggestions.append(f"Content is {word_count} words. Consider expanding for comprehensiveness.")
        score -= 10
    elif word_count < 300:
        issues.append("Content appears thin. Most topics need 800+ words for depth.")
        score -= 15

    # Links
    if len(links['internal']) == 0:
        suggestions.append("No internal links found. Add links to related content.")
        score -= 5

    if len(links['external']) == 0:
        suggestions.append("No external links. Consider citing authoritative sources.")
        score -= 5

    # Keyword analysis (if keyword provided)
    keyword_analysis = None
    if keyword:
        keyword_analysis = check_keyword_usage(content, keyword)

        if not keyword_analysis['in_title']:
            issues.append(f"Target keyword '{keyword}' not found in title.")
            score -= 15

        if not keyword_analysis['in_first_100_words']:
            suggestions.append(f"Add target keyword in first 100 words.")
            score -= 10

        if not keyword_analysis['in_h2']:
            suggestions.append(f"Add target keyword to at least one H2 heading.")
            score -= 5

        if keyword_analysis['keyword_density'] > 3:
            issues.append("Keyword density too high. Reduce to avoid over-optimization.")
            score -= 10
        elif keyword_analysis['total_count'] < 2:
            suggestions.append("Keyword appears very few times. Ensure natural usage.")

    # Image alt text check (look for markdown images)
    images = re.findall(r'!\[([^\]]*)\]\([^)]+\)', content)
    images_without_alt = [img for img in images if not img.strip()]
    if images_without_alt:
        suggestions.append(f"{len(images_without_alt)} image(s) missing alt text.")
        score -= 5

    # Readability (simple check)
    sentences = len(re.split(r'[.!?]+', content))
    avg_sentence = word_count / sentences if sentences > 0 else 0
    if avg_sentence > 25:
        suggestions.append(f"Average sentence length is {avg_sentence:.0f} words. Consider shorter sentences.")

    score = max(0, min(100, score))

    # Determine grade
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    return {
        "seo_score": score,
        "grade": grade,
        "statistics": {
            "word_count": word_count,
            "h1_count": len(headers['h1']),
            "h2_count": len(headers['h2']),
            "h3_count": len(headers['h3']),
            "internal_links": len(links['internal']),
            "external_links": len(links['external']),
            "image_count": len(images)
        },
        "keyword_analysis": keyword_analysis,
        "issues": issues,
        "suggestions": suggestions
    }


def main():
    parser = argparse.ArgumentParser(description="Check on-page SEO")
    parser.add_argument("file", help="Markdown file to check")
    parser.add_argument("--keyword", "-k", help="Target keyword to check for")

    args = parser.parse_args()

    try:
        with open(args.file, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(json.dumps({"error": f"File not found: {args.file}"}))
        sys.exit(1)

    result = analyze_content(content, args.keyword)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
