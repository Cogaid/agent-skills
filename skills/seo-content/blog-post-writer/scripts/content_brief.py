#!/usr/bin/env python3
"""
Generate content brief from keyword research.

Usage:
    python content_brief.py --keyword "email marketing tips"
    python content_brief.py --keyword "seo guide" --competitor-count 5

Output: Complete content brief for writing
"""

import argparse
import json
import re
import sys


# Content type recommendations based on keyword patterns
CONTENT_TYPE_PATTERNS = {
    "how to": {
        "type": "how-to guide",
        "structure": ["introduction", "prerequisites", "steps", "tips", "faq", "conclusion"],
        "word_count_range": [1500, 2500]
    },
    "what is": {
        "type": "explainer",
        "structure": ["definition", "importance", "how it works", "examples", "faq"],
        "word_count_range": [1200, 2000]
    },
    "best": {
        "type": "listicle/roundup",
        "structure": ["introduction", "criteria", "items", "comparison table", "how to choose"],
        "word_count_range": [2000, 4000]
    },
    "vs": {
        "type": "comparison",
        "structure": ["introduction", "what is A", "what is B", "comparison", "verdict"],
        "word_count_range": [2000, 3000]
    },
    "guide": {
        "type": "comprehensive guide",
        "structure": ["overview", "fundamentals", "implementation", "advanced", "resources"],
        "word_count_range": [3000, 6000]
    },
    "tips": {
        "type": "tips listicle",
        "structure": ["introduction", "tips", "action items", "conclusion"],
        "word_count_range": [1500, 2500]
    },
    "examples": {
        "type": "examples showcase",
        "structure": ["introduction", "examples with analysis", "key takeaways"],
        "word_count_range": [1500, 3000]
    },
    "template": {
        "type": "resource/template post",
        "structure": ["introduction", "templates", "how to use", "customization tips"],
        "word_count_range": [1200, 2000]
    }
}


def detect_search_intent(keyword):
    """Detect the search intent of a keyword."""
    keyword_lower = keyword.lower()

    intent_signals = {
        "informational": ["what", "how", "why", "guide", "learn", "tutorial", "explained"],
        "commercial": ["best", "top", "review", "vs", "comparison", "alternative"],
        "transactional": ["buy", "price", "discount", "free", "download", "sign up"],
        "navigational": ["login", "site", "official", "website"]
    }

    for intent, signals in intent_signals.items():
        if any(signal in keyword_lower for signal in signals):
            return intent

    return "informational"  # Default


def detect_content_type(keyword):
    """Detect recommended content type based on keyword."""
    keyword_lower = keyword.lower()

    for pattern, config in CONTENT_TYPE_PATTERNS.items():
        if pattern in keyword_lower:
            return config

    # Default for unmatched patterns
    return {
        "type": "blog post",
        "structure": ["introduction", "main points", "examples", "conclusion"],
        "word_count_range": [1500, 2500]
    }


def generate_outline(keyword, content_config):
    """Generate suggested outline based on keyword and content type."""
    outline = []
    keyword_clean = keyword.strip()

    content_type = content_config["type"]

    if content_type == "how-to guide":
        outline = [
            {"level": "h1", "text": f"How to {keyword_clean.replace('how to ', '').title()}: A Complete Guide"},
            {"level": "h2", "text": "What You'll Learn"},
            {"level": "h2", "text": "Before You Start"},
            {"level": "h2", "text": "Step 1: [First Action]"},
            {"level": "h2", "text": "Step 2: [Second Action]"},
            {"level": "h2", "text": "Step 3: [Third Action]"},
            {"level": "h2", "text": "Step 4: [Fourth Action]"},
            {"level": "h2", "text": "Step 5: [Fifth Action]"},
            {"level": "h2", "text": "Common Mistakes to Avoid"},
            {"level": "h2", "text": "Pro Tips"},
            {"level": "h2", "text": "Frequently Asked Questions"},
            {"level": "h2", "text": "Next Steps"},
        ]

    elif content_type == "listicle/roundup":
        outline = [
            {"level": "h1", "text": f"[Number] Best {keyword_clean.replace('best ', '').title()} in [Year]"},
            {"level": "h2", "text": "How We Selected These"},
            {"level": "h2", "text": "Quick Comparison Table"},
            {"level": "h2", "text": "1. [First Item]"},
            {"level": "h2", "text": "2. [Second Item]"},
            {"level": "h2", "text": "3. [Third Item]"},
            {"level": "h2", "text": "4. [Fourth Item]"},
            {"level": "h2", "text": "5. [Fifth Item]"},
            {"level": "h2", "text": "How to Choose the Right One"},
            {"level": "h2", "text": "Frequently Asked Questions"},
        ]

    elif content_type == "comparison":
        outline = [
            {"level": "h1", "text": f"{keyword_clean.title()}: Which One Should You Choose?"},
            {"level": "h2", "text": "Quick Verdict"},
            {"level": "h2", "text": "What is [Option A]?"},
            {"level": "h2", "text": "What is [Option B]?"},
            {"level": "h2", "text": "Feature Comparison"},
            {"level": "h2", "text": "Pricing Comparison"},
            {"level": "h2", "text": "Pros and Cons"},
            {"level": "h2", "text": "Which Should You Choose?"},
            {"level": "h2", "text": "Frequently Asked Questions"},
        ]

    elif content_type == "comprehensive guide":
        outline = [
            {"level": "h1", "text": f"The Complete Guide to {keyword_clean.replace('guide', '').title()}"},
            {"level": "h2", "text": f"What is {keyword_clean.replace('guide', '').title()}?"},
            {"level": "h2", "text": "Why It Matters"},
            {"level": "h2", "text": "How It Works"},
            {"level": "h2", "text": "Getting Started"},
            {"level": "h2", "text": "Best Practices"},
            {"level": "h2", "text": "Advanced Strategies"},
            {"level": "h2", "text": "Common Challenges and Solutions"},
            {"level": "h2", "text": "Tools and Resources"},
            {"level": "h2", "text": "Frequently Asked Questions"},
            {"level": "h2", "text": "Key Takeaways"},
        ]

    else:
        outline = [
            {"level": "h1", "text": f"{keyword_clean.title()}: What You Need to Know"},
            {"level": "h2", "text": "Introduction"},
            {"level": "h2", "text": "[Main Point 1]"},
            {"level": "h2", "text": "[Main Point 2]"},
            {"level": "h2", "text": "[Main Point 3]"},
            {"level": "h2", "text": "Key Takeaways"},
            {"level": "h2", "text": "Frequently Asked Questions"},
        ]

    return outline


def generate_paa_questions(keyword):
    """Generate likely "People Also Ask" questions."""
    keyword_clean = keyword.lower().strip()

    # Common question patterns
    questions = [
        f"What is {keyword_clean}?",
        f"How does {keyword_clean} work?",
        f"Why is {keyword_clean} important?",
        f"How do I get started with {keyword_clean}?",
        f"What are the benefits of {keyword_clean}?",
        f"Is {keyword_clean} worth it?",
        f"What are common {keyword_clean} mistakes?",
        f"How much does {keyword_clean} cost?",
    ]

    return questions[:6]  # Return top 6


def generate_brief(keyword, competitor_count=3):
    """Generate complete content brief."""
    intent = detect_search_intent(keyword)
    content_config = detect_content_type(keyword)
    outline = generate_outline(keyword, content_config)
    questions = generate_paa_questions(keyword)

    brief = {
        "target_keyword": keyword,
        "search_intent": intent,
        "recommended_content_type": content_config["type"],
        "word_count_range": {
            "minimum": content_config["word_count_range"][0],
            "recommended": sum(content_config["word_count_range"]) // 2,
            "maximum": content_config["word_count_range"][1]
        },
        "title_suggestions": [
            f"{keyword.title()}: A Complete Guide",
            f"[Number] {keyword.title()} [Tips/Strategies/Methods]",
            f"How to {keyword.title()} ([Year] Guide)",
            f"The Ultimate {keyword.title()} Guide for [Audience]"
        ],
        "suggested_outline": outline,
        "questions_to_answer": questions,
        "seo_requirements": {
            "primary_keyword_in": ["title", "h1", "first_100_words", "at_least_one_h2"],
            "title_tag_length": "50-60 characters",
            "meta_description_length": "150-160 characters",
            "recommended_h2_count": "5-10",
            "internal_links": "3-5 relevant pages",
            "external_links": "2-4 authoritative sources"
        },
        "content_guidelines": {
            "readability_target": "Grade 6-8",
            "paragraph_length": "2-3 sentences",
            "include_visuals": True,
            "include_examples": True,
            "include_data": True
        },
        "competitor_analysis": {
            "analyze_count": competitor_count,
            "note": "Analyze top ranking pages for this keyword to identify gaps and opportunities"
        },
        "checklist": [
            "[ ] Research top competitors",
            "[ ] Create detailed outline",
            "[ ] Write compelling introduction",
            "[ ] Include keyword in key locations",
            "[ ] Add relevant examples",
            "[ ] Include data/statistics",
            "[ ] Add internal links",
            "[ ] Add external links to sources",
            "[ ] Create/add images",
            "[ ] Write meta description",
            "[ ] Review readability",
            "[ ] Final SEO check"
        ]
    }

    return brief


def main():
    parser = argparse.ArgumentParser(description="Generate content brief")
    parser.add_argument("--keyword", "-k", required=True, help="Target keyword")
    parser.add_argument("--competitor-count", "-c", type=int, default=3,
                        help="Number of competitors to analyze")
    parser.add_argument("--format", "-f", choices=["json", "markdown"],
                        default="json", help="Output format")

    args = parser.parse_args()

    brief = generate_brief(args.keyword, args.competitor_count)

    if args.format == "markdown":
        print(f"\n# Content Brief: {args.keyword}\n")
        print(f"**Target Keyword:** {brief['target_keyword']}")
        print(f"**Search Intent:** {brief['search_intent']}")
        print(f"**Content Type:** {brief['recommended_content_type']}")
        print(f"**Word Count:** {brief['word_count_range']['minimum']}-{brief['word_count_range']['maximum']}")

        print("\n## Suggested Outline\n")
        for item in brief['suggested_outline']:
            indent = "  " if item['level'] == 'h2' else ""
            print(f"{indent}- {item['text']}")

        print("\n## Questions to Answer\n")
        for q in brief['questions_to_answer']:
            print(f"- {q}")

        print("\n## Checklist\n")
        for item in brief['checklist']:
            print(item)
    else:
        print(json.dumps(brief, indent=2))


if __name__ == "__main__":
    main()
