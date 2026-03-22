#!/usr/bin/env python3
"""
Extract repurposable elements from long-form content.

Usage:
    python extract_content.py blog-post.md
    python extract_content.py blog-post.md --format json

Output: Key elements for social media repurposing
"""

import argparse
import json
import re
import sys


def extract_title(content):
    """Extract H1 title."""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    return match.group(1) if match else None


def extract_headers(content):
    """Extract H2 headers as key topics."""
    return re.findall(r'^##\s+(.+)$', content, re.MULTILINE)


def extract_statistics(content):
    """Extract statistics and numbers."""
    # Look for percentages and numbers
    stats = []

    # Percentages
    percentages = re.findall(r'(\d+(?:\.\d+)?%[^.]*\.)', content)
    stats.extend(percentages)

    # Numbers with context (e.g., "10,000 users", "5x improvement")
    numbers = re.findall(r'(\d+(?:,\d{3})*(?:\.\d+)?(?:x|X)?\s+\w+[^.]*\.)', content)
    stats.extend(numbers)

    return list(set(stats))[:10]  # Dedupe and limit


def extract_quotes(content):
    """Extract quotable sentences."""
    quotes = []

    # Sentences in bold
    bold = re.findall(r'\*\*([^*]+)\*\*', content)
    quotes.extend([b for b in bold if len(b.split()) > 5])

    # Sentences with strong words
    strong_words = ['never', 'always', 'best', 'worst', 'secret', 'key', 'critical']
    sentences = re.split(r'[.!?]', content)
    for sentence in sentences:
        if any(word in sentence.lower() for word in strong_words):
            clean = sentence.strip()
            if 10 < len(clean.split()) < 30:
                quotes.append(clean)

    return list(set(quotes))[:10]


def extract_lists(content):
    """Extract list items."""
    # Bullet points
    bullets = re.findall(r'^\s*[-*]\s+(.+)$', content, re.MULTILINE)

    # Numbered items
    numbered = re.findall(r'^\s*\d+[\.\)]\s+(.+)$', content, re.MULTILINE)

    return {
        "bullet_points": bullets[:15],
        "numbered_items": numbered[:15]
    }


def extract_tips(content):
    """Extract tips and actionable advice."""
    tips = []

    # Look for tip indicators
    tip_patterns = [
        r'(?:tip|pro tip|hint|advice):\s*([^.]+\.)',
        r'(?:you should|try to|make sure to|remember to)\s+([^.]+\.)',
        r'(?:the key is to|the secret is to)\s+([^.]+\.)',
    ]

    for pattern in tip_patterns:
        found = re.findall(pattern, content, re.IGNORECASE)
        tips.extend(found)

    return list(set(tips))[:10]


def extract_questions(content):
    """Extract questions that could become engagement posts."""
    questions = re.findall(r'([^.]*\?)', content)
    # Filter to reasonable length questions
    return [q.strip() for q in questions if 5 < len(q.split()) < 20][:10]


def generate_social_ideas(title, headers, stats, quotes):
    """Generate social media post ideas."""
    ideas = {
        "twitter_thread": {
            "hook": f"Here's everything you need to know about {title}:" if title else None,
            "points": headers[:7],
            "cta": "Follow for more insights like this."
        },
        "linkedin_carousel": {
            "title": title,
            "slides": headers[:8],
            "cta": "Save this for later!"
        },
        "quote_graphics": quotes[:5],
        "stat_posts": stats[:5],
        "engagement_questions": [
            f"What's your experience with {title}?" if title else None,
            f"Which of these {len(headers)} tips resonates most?"
        ]
    }

    return ideas


def extract_content(content):
    """Extract all repurposable elements."""
    title = extract_title(content)
    headers = extract_headers(content)
    stats = extract_statistics(content)
    quotes = extract_quotes(content)
    lists = extract_lists(content)
    tips = extract_tips(content)
    questions = extract_questions(content)

    # Count words
    word_count = len(content.split())

    # Generate ideas
    social_ideas = generate_social_ideas(title, headers, stats, quotes)

    return {
        "metadata": {
            "title": title,
            "word_count": word_count,
            "header_count": len(headers),
            "stat_count": len(stats),
            "quote_count": len(quotes)
        },
        "extractable_elements": {
            "headers_as_topics": headers,
            "statistics": stats,
            "quotable_sentences": quotes,
            "tips_and_advice": tips,
            "list_items": lists,
            "questions": questions
        },
        "social_media_ideas": social_ideas,
        "repurposing_potential": {
            "twitter_threads": max(1, len(headers) // 3),
            "linkedin_carousels": max(1, len(headers) // 5),
            "quote_graphics": len(quotes),
            "single_posts": len(stats) + len(quotes)
        }
    }


def main():
    parser = argparse.ArgumentParser(description="Extract content for repurposing")
    parser.add_argument("file", help="Content file to extract from")
    parser.add_argument("--format", "-f", choices=["json", "summary"],
                        default="json", help="Output format")

    args = parser.parse_args()

    try:
        with open(args.file, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(json.dumps({"error": f"File not found: {args.file}"}))
        sys.exit(1)

    result = extract_content(content)

    if args.format == "summary":
        print(f"\n=== Content Extraction Summary ===\n")
        print(f"Title: {result['metadata']['title']}")
        print(f"Word Count: {result['metadata']['word_count']}")
        print(f"\nRepurposing Potential:")
        for key, value in result['repurposing_potential'].items():
            print(f"  - {key}: {value}")
        print(f"\nKey Topics ({len(result['extractable_elements']['headers_as_topics'])}):")
        for topic in result['extractable_elements']['headers_as_topics'][:5]:
            print(f"  • {topic}")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
