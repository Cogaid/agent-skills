#!/usr/bin/env python3
"""
Check SEO optimization of knowledge base articles.

Usage:
    python seo_check.py article.md --keyword "reset password"
    python seo_check.py article.md

Output: JSON with SEO metrics and suggestions
"""

import argparse
import json
import re
import sys


def extract_title(content: str) -> str:
    """Extract H1 title from markdown."""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    return match.group(1).strip() if match else ""


def extract_headers(content: str) -> dict:
    """Extract all headers from markdown."""
    headers = {"h1": [], "h2": [], "h3": []}

    for match in re.finditer(r'^(#{1,3})\s+(.+)$', content, re.MULTILINE):
        level = len(match.group(1))
        text = match.group(2).strip()
        if level == 1:
            headers["h1"].append(text)
        elif level == 2:
            headers["h2"].append(text)
        elif level == 3:
            headers["h3"].append(text)

    return headers


def extract_first_paragraph(content: str) -> str:
    """Extract first paragraph of content."""
    # Remove frontmatter
    content = re.sub(r'^---[\s\S]*?---\n', '', content)

    # Remove title
    content = re.sub(r'^#\s+.+\n', '', content)

    # Find first paragraph
    lines = content.strip().split('\n')
    paragraph = []
    for line in lines:
        line = line.strip()
        if not line:
            if paragraph:
                break
            continue
        if line.startswith('#'):
            continue
        paragraph.append(line)

    return ' '.join(paragraph)


def check_keyword_placement(content: str, keyword: str) -> dict:
    """Check keyword placement throughout article."""
    keyword_lower = keyword.lower()
    content_lower = content.lower()

    title = extract_title(content)
    headers = extract_headers(content)
    first_para = extract_first_paragraph(content)

    placements = {
        "in_title": keyword_lower in title.lower(),
        "in_first_paragraph": keyword_lower in first_para.lower(),
        "in_h2": any(keyword_lower in h.lower() for h in headers["h2"]),
        "in_h3": any(keyword_lower in h.lower() for h in headers["h3"]),
        "total_occurrences": content_lower.count(keyword_lower)
    }

    # Calculate keyword density
    words = re.findall(r'\b\w+\b', content_lower)
    if words:
        placements["density"] = round(placements["total_occurrences"] / len(words) * 100, 2)
    else:
        placements["density"] = 0

    return placements


def check_title_optimization(title: str) -> dict:
    """Analyze title SEO optimization."""
    checks = {
        "length": len(title),
        "length_ok": 30 <= len(title) <= 60,
        "starts_with_action": title.lower().startswith(('how to', 'what is', 'why', 'guide to')),
        "contains_number": bool(re.search(r'\d', title)),
        "has_colon_or_dash": ':' in title or '-' in title or '|' in title
    }

    suggestions = []
    if checks["length"] < 30:
        suggestions.append("Title too short. Add more descriptive words.")
    elif checks["length"] > 60:
        suggestions.append("Title too long. May be truncated in search results.")

    if not checks["starts_with_action"]:
        suggestions.append("Consider starting with 'How to' or action-oriented phrase.")

    checks["suggestions"] = suggestions
    return checks


def check_structure(content: str) -> dict:
    """Check article structure for SEO."""
    headers = extract_headers(content)

    # Check for proper hierarchy
    has_single_h1 = len(headers["h1"]) == 1
    has_h2s = len(headers["h2"]) > 0
    has_substructure = len(headers["h3"]) > 0

    # Check for lists
    has_numbered_list = bool(re.search(r'^\s*\d+\.', content, re.MULTILINE))
    has_bullet_list = bool(re.search(r'^\s*[-*+]\s', content, re.MULTILINE))

    # Check for links
    internal_links = len(re.findall(r'\[([^\]]+)\]\((?!http)', content))
    external_links = len(re.findall(r'\[([^\]]+)\]\(https?://', content))

    return {
        "has_single_h1": has_single_h1,
        "h2_count": len(headers["h2"]),
        "h3_count": len(headers["h3"]),
        "has_lists": has_numbered_list or has_bullet_list,
        "has_numbered_steps": has_numbered_list,
        "internal_links": internal_links,
        "external_links": external_links
    }


def generate_suggestions(title_check: dict, structure: dict, keyword_check: dict = None) -> list:
    """Generate overall SEO suggestions."""
    suggestions = []

    # Title suggestions
    suggestions.extend(title_check.get("suggestions", []))

    # Structure suggestions
    if not structure["has_single_h1"]:
        suggestions.append("Article should have exactly one H1 (title).")

    if structure["h2_count"] == 0:
        suggestions.append("Add H2 subheadings to improve scannability.")

    if not structure["has_lists"]:
        suggestions.append("Add bullet or numbered lists for better readability.")

    if structure["internal_links"] == 0:
        suggestions.append("Add internal links to related articles.")

    # Keyword suggestions
    if keyword_check:
        if not keyword_check["in_title"]:
            suggestions.append("Add primary keyword to title.")

        if not keyword_check["in_first_paragraph"]:
            suggestions.append("Include keyword in first paragraph.")

        if not keyword_check["in_h2"]:
            suggestions.append("Include keyword in at least one H2 heading.")

        if keyword_check["density"] > 3:
            suggestions.append("Keyword density too high. May appear spammy.")

        if keyword_check["total_occurrences"] < 2:
            suggestions.append("Keyword appears too few times. Add more natural occurrences.")

    return suggestions


def analyze_seo(content: str, keyword: str = None) -> dict:
    """Main SEO analysis function."""
    title = extract_title(content)
    title_check = check_title_optimization(title)
    structure = check_structure(content)

    result = {
        "title": {
            "text": title,
            "analysis": title_check
        },
        "structure": structure
    }

    if keyword:
        keyword_check = check_keyword_placement(content, keyword)
        result["keyword"] = {
            "term": keyword,
            "analysis": keyword_check
        }
        suggestions = generate_suggestions(title_check, structure, keyword_check)
    else:
        suggestions = generate_suggestions(title_check, structure)

    result["suggestions"] = suggestions
    result["issues_count"] = len(suggestions)
    result["grade"] = "GOOD" if len(suggestions) <= 2 else "NEEDS IMPROVEMENT"

    return result


def main():
    parser = argparse.ArgumentParser(description="Check article SEO")
    parser.add_argument("input", help="Markdown file path")
    parser.add_argument("--keyword", "-k", help="Primary keyword to check")
    parser.add_argument("--pretty", "-p", action="store_true", help="Pretty print")

    args = parser.parse_args()

    with open(args.input, 'r') as f:
        content = f.read()

    result = analyze_seo(content, args.keyword)

    if args.pretty:
        print(json.dumps(result, indent=2))
    else:
        print(json.dumps(result))

    sys.exit(0 if result["issues_count"] <= 2 else 1)


if __name__ == "__main__":
    main()
