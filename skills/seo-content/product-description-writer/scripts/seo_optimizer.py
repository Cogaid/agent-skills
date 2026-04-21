#!/usr/bin/env python3
"""
SEO Optimizer for Product Descriptions -- Analyze and optimize product copy for search.

Usage:
    python seo_optimizer.py --title "Ergonomic Office Chair" --description "Our chair features lumbar support..." --keyword "ergonomic office chair"
    python seo_optimizer.py --input product_page.json --keywords "standing desk,adjustable desk,sit stand desk"
    python seo_optimizer.py --url-slug "ergonomic-office-chair" --title "Best Chair" --keyword "ergonomic chair" --output report.json
"""

import argparse
import json
import re
import sys
from datetime import datetime


SEO_RULES = {
    "title_length": {
        "name": "Title Tag Length",
        "min": 30,
        "max": 60,
        "weight": 10,
        "description": "Title should be 30-60 characters for optimal SERP display",
    },
    "title_keyword": {
        "name": "Keyword in Title",
        "weight": 15,
        "description": "Primary keyword should appear in the title, preferably near the start",
    },
    "meta_description_length": {
        "name": "Meta Description Length",
        "min": 120,
        "max": 160,
        "weight": 8,
        "description": "Meta description should be 120-160 characters",
    },
    "meta_keyword": {
        "name": "Keyword in Meta Description",
        "weight": 8,
        "description": "Primary keyword should appear in the meta description",
    },
    "first_100_words": {
        "name": "Keyword in First 100 Words",
        "weight": 12,
        "description": "Primary keyword should appear within the first 100 words",
    },
    "keyword_density": {
        "name": "Keyword Density",
        "min_pct": 0.5,
        "max_pct": 2.5,
        "weight": 10,
        "description": "Keyword density should be 0.5-2.5% of total words",
    },
    "url_slug": {
        "name": "URL Slug Optimization",
        "weight": 7,
        "description": "URL should contain the primary keyword, be lowercase, use hyphens",
    },
    "heading_structure": {
        "name": "Heading Structure",
        "weight": 8,
        "description": "Content should use H2/H3 subheadings with keyword variations",
    },
    "word_count": {
        "name": "Content Length",
        "min": 150,
        "recommended": 300,
        "weight": 7,
        "description": "Product descriptions should be at least 150 words, ideally 300+",
    },
    "readability": {
        "name": "Readability",
        "weight": 5,
        "description": "Short sentences and paragraphs improve readability and SEO",
    },
    "power_words": {
        "name": "Conversion Power Words",
        "weight": 5,
        "description": "Include power words that drive action and engagement",
    },
    "unique_value": {
        "name": "Unique Value Proposition",
        "weight": 5,
        "description": "Description should contain clear differentiators",
    },
}

POWER_WORDS = [
    "free", "new", "proven", "guaranteed", "exclusive", "limited",
    "premium", "save", "instant", "easy", "best", "top", "professional",
    "certified", "trusted", "secure", "fast", "simple", "powerful",
    "innovative", "award-winning", "handcrafted", "natural", "organic",
]

FILLER_WORDS = [
    "very", "really", "basically", "actually", "literally", "just",
    "simply", "stuff", "things", "nice", "good", "great",
]


def count_keyword_occurrences(text, keyword):
    """Count keyword occurrences (case-insensitive)."""
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    return len(pattern.findall(text))


def calculate_keyword_density(text, keyword):
    """Calculate keyword density as percentage of total words."""
    words = text.split()
    total_words = len(words)
    if total_words == 0:
        return 0.0
    keyword_words = len(keyword.split())
    occurrences = count_keyword_occurrences(text, keyword)
    return (occurrences * keyword_words / total_words) * 100


def analyze_readability(text):
    """Basic readability analysis."""
    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    words = text.split()

    avg_sentence_length = len(words) / max(len(sentences), 1)
    paragraphs = text.split("\n\n")
    avg_paragraph_length = len(words) / max(len(paragraphs), 1)

    long_sentences = [s for s in sentences if len(s.split()) > 25]

    return {
        "total_words": len(words),
        "total_sentences": len(sentences),
        "avg_sentence_length": round(avg_sentence_length, 1),
        "avg_paragraph_length": round(avg_paragraph_length, 1),
        "long_sentences": len(long_sentences),
        "paragraphs": len(paragraphs),
    }


def find_power_words(text):
    """Find power words present in text."""
    text_lower = text.lower()
    found = [w for w in POWER_WORDS if w in text_lower]
    return found


def find_filler_words(text):
    """Find filler words that should be replaced."""
    text_lower = text.lower()
    found = []
    for w in FILLER_WORDS:
        pattern = re.compile(r"\b" + re.escape(w) + r"\b", re.IGNORECASE)
        count = len(pattern.findall(text_lower))
        if count > 0:
            found.append({"word": w, "count": count})
    return found


def run_audit(title, description, keyword, meta_description=None, url_slug=None):
    """Run full SEO audit on product description."""
    checks = []
    total_score = 0
    max_score = 0

    # Title length
    rule = SEO_RULES["title_length"]
    max_score += rule["weight"]
    title_len = len(title)
    if rule["min"] <= title_len <= rule["max"]:
        score = rule["weight"]
        status = "PASS"
        detail = f"{title_len} chars (optimal: {rule['min']}-{rule['max']})"
    elif title_len < rule["min"]:
        score = rule["weight"] * 0.5
        status = "WARN"
        detail = f"{title_len} chars -- too short (minimum: {rule['min']})"
    else:
        score = rule["weight"] * 0.3
        status = "WARN"
        detail = f"{title_len} chars -- too long (maximum: {rule['max']}), will be truncated in SERP"
    total_score += score
    checks.append({"rule": rule["name"], "status": status, "score": round(score, 1), "max": rule["weight"], "detail": detail})

    # Title keyword
    rule = SEO_RULES["title_keyword"]
    max_score += rule["weight"]
    kw_in_title = keyword.lower() in title.lower()
    kw_starts_title = title.lower().startswith(keyword.lower())
    if kw_starts_title:
        score = rule["weight"]
        status = "PASS"
        detail = "Keyword appears at the start of title"
    elif kw_in_title:
        score = rule["weight"] * 0.7
        status = "PASS"
        detail = "Keyword appears in title (move to start for best results)"
    else:
        score = 0
        status = "FAIL"
        detail = f"Keyword '{keyword}' not found in title"
    total_score += score
    checks.append({"rule": rule["name"], "status": status, "score": round(score, 1), "max": rule["weight"], "detail": detail})

    # Meta description
    if meta_description:
        rule = SEO_RULES["meta_description_length"]
        max_score += rule["weight"]
        meta_len = len(meta_description)
        if rule["min"] <= meta_len <= rule["max"]:
            score = rule["weight"]
            status = "PASS"
        elif meta_len < rule["min"]:
            score = rule["weight"] * 0.5
            status = "WARN"
        else:
            score = rule["weight"] * 0.3
            status = "WARN"
        detail = f"{meta_len} chars (optimal: {rule['min']}-{rule['max']})"
        total_score += score
        checks.append({"rule": rule["name"], "status": status, "score": round(score, 1), "max": rule["weight"], "detail": detail})

        rule = SEO_RULES["meta_keyword"]
        max_score += rule["weight"]
        if keyword.lower() in meta_description.lower():
            score = rule["weight"]
            status = "PASS"
            detail = "Keyword found in meta description"
        else:
            score = 0
            status = "FAIL"
            detail = "Keyword not found in meta description"
        total_score += score
        checks.append({"rule": rule["name"], "status": status, "score": round(score, 1), "max": rule["weight"], "detail": detail})

    # First 100 words
    rule = SEO_RULES["first_100_words"]
    max_score += rule["weight"]
    first_100 = " ".join(description.split()[:100])
    if keyword.lower() in first_100.lower():
        score = rule["weight"]
        status = "PASS"
        detail = "Keyword appears in first 100 words"
    else:
        score = 0
        status = "FAIL"
        detail = "Keyword not found in first 100 words -- add it early"
    total_score += score
    checks.append({"rule": rule["name"], "status": status, "score": round(score, 1), "max": rule["weight"], "detail": detail})

    # Keyword density
    rule = SEO_RULES["keyword_density"]
    max_score += rule["weight"]
    density = calculate_keyword_density(description, keyword)
    if rule["min_pct"] <= density <= rule["max_pct"]:
        score = rule["weight"]
        status = "PASS"
    elif density < rule["min_pct"]:
        score = rule["weight"] * 0.3
        status = "WARN"
    else:
        score = rule["weight"] * 0.3
        status = "WARN"
    detail = f"{density:.1f}% (optimal: {rule['min_pct']}-{rule['max_pct']}%)"
    total_score += score
    checks.append({"rule": rule["name"], "status": status, "score": round(score, 1), "max": rule["weight"], "detail": detail})

    # URL slug
    if url_slug:
        rule = SEO_RULES["url_slug"]
        max_score += rule["weight"]
        slug_has_kw = keyword.lower().replace(" ", "-") in url_slug.lower()
        slug_clean = url_slug == url_slug.lower() and " " not in url_slug
        if slug_has_kw and slug_clean:
            score = rule["weight"]
            status = "PASS"
            detail = "URL slug contains keyword and is properly formatted"
        elif slug_has_kw:
            score = rule["weight"] * 0.7
            status = "WARN"
            detail = "URL contains keyword but formatting could improve"
        else:
            score = 0
            status = "FAIL"
            detail = f"URL slug should contain '{keyword.lower().replace(' ', '-')}'"
        total_score += score
        checks.append({"rule": rule["name"], "status": status, "score": round(score, 1), "max": rule["weight"], "detail": detail})

    # Word count
    rule = SEO_RULES["word_count"]
    max_score += rule["weight"]
    word_count = len(description.split())
    if word_count >= rule["recommended"]:
        score = rule["weight"]
        status = "PASS"
        detail = f"{word_count} words (recommended: {rule['recommended']}+)"
    elif word_count >= rule["min"]:
        score = rule["weight"] * 0.6
        status = "WARN"
        detail = f"{word_count} words -- acceptable but consider expanding to {rule['recommended']}+"
    else:
        score = 0
        status = "FAIL"
        detail = f"{word_count} words -- too thin (minimum: {rule['min']})"
    total_score += score
    checks.append({"rule": rule["name"], "status": status, "score": round(score, 1), "max": rule["weight"], "detail": detail})

    # Readability
    rule = SEO_RULES["readability"]
    max_score += rule["weight"]
    readability = analyze_readability(description)
    if readability["avg_sentence_length"] <= 20 and readability["long_sentences"] == 0:
        score = rule["weight"]
        status = "PASS"
    elif readability["avg_sentence_length"] <= 25:
        score = rule["weight"] * 0.6
        status = "WARN"
    else:
        score = rule["weight"] * 0.2
        status = "WARN"
    detail = f"Avg sentence: {readability['avg_sentence_length']} words, {readability['long_sentences']} long sentences"
    total_score += score
    checks.append({"rule": rule["name"], "status": status, "score": round(score, 1), "max": rule["weight"], "detail": detail})

    # Power words
    rule = SEO_RULES["power_words"]
    max_score += rule["weight"]
    power = find_power_words(description + " " + title)
    if len(power) >= 3:
        score = rule["weight"]
        status = "PASS"
    elif len(power) >= 1:
        score = rule["weight"] * 0.5
        status = "WARN"
    else:
        score = 0
        status = "WARN"
    detail = f"Found {len(power)} power words: {', '.join(power[:5])}" if power else "No power words found -- add some for conversion"
    total_score += score
    checks.append({"rule": rule["name"], "status": status, "score": round(score, 1), "max": rule["weight"], "detail": detail})

    # Filler words
    fillers = find_filler_words(description)

    # Overall score
    overall_pct = (total_score / max_score * 100) if max_score > 0 else 0

    if overall_pct >= 90:
        rating = "Excellent"
    elif overall_pct >= 75:
        rating = "Good"
    elif overall_pct >= 60:
        rating = "Fair"
    elif overall_pct >= 40:
        rating = "Needs Work"
    else:
        rating = "Poor"

    return {
        "score": round(overall_pct, 1),
        "rating": rating,
        "points": f"{round(total_score, 1)}/{max_score}",
        "checks": checks,
        "readability": readability,
        "power_words_found": power,
        "filler_words_found": fillers,
        "keyword_density": round(density, 2),
        "keyword_occurrences": count_keyword_occurrences(description, keyword),
        "recommendations": [
            c["detail"]
            for c in checks
            if c["status"] in ("FAIL", "WARN") and c["score"] < c["max"]
        ],
    }


def main():
    parser = argparse.ArgumentParser(
        description="Analyze and optimize product descriptions for SEO",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --title "Ergonomic Office Chair" --description "Our chair..." --keyword "ergonomic office chair"
  %(prog)s --input product.json --keywords "standing desk,adjustable desk"
  %(prog)s --title "Best Chair" --keyword "ergonomic chair" --url-slug "ergonomic-chair" --output report.json
        """,
    )
    parser.add_argument("--title", help="Product title / H1")
    parser.add_argument("--description", help="Product description text")
    parser.add_argument("--keyword", help="Primary target keyword")
    parser.add_argument("--keywords", help="Comma-separated target keywords (first is primary)")
    parser.add_argument("--meta-description", help="Meta description text")
    parser.add_argument("--url-slug", help="URL slug for the product page")
    parser.add_argument("--input", help="JSON file with product data")
    parser.add_argument("--output", help="Output file (default: stdout)")

    args = parser.parse_args()

    if args.input:
        with open(args.input) as f:
            data = json.load(f)
        title = data.get("title", "")
        description = data.get("description", "")
        keyword = data.get("keyword", data.get("keywords", [""])[0] if isinstance(data.get("keywords"), list) else "")
        meta_description = data.get("meta_description")
        url_slug = data.get("url_slug")
    else:
        title = args.title or ""
        description = args.description or ""
        keyword = args.keyword or (args.keywords.split(",")[0].strip() if args.keywords else "")
        meta_description = args.meta_description
        url_slug = args.url_slug

    if not title or not description or not keyword:
        parser.error("--title, --description, and --keyword are required (or use --input)")
        return

    audit = run_audit(title, description, keyword, meta_description, url_slug)

    result = {
        "audited_at": datetime.now().isoformat(),
        "input": {
            "title": title,
            "keyword": keyword,
            "description_length": len(description.split()),
        },
        "audit": audit,
    }

    output = json.dumps(result, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"SEO audit written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
