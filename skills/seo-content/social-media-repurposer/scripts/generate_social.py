#!/usr/bin/env python3
"""
Generate platform-specific social media posts from source content.

Usage:
    python generate_social.py --source blog-post.md --platform twitter
    python generate_social.py --source blog-post.md --platform linkedin
    python generate_social.py --source blog-post.md --platform all

Output: Platform-formatted post drafts
"""

import argparse
import json
import re
import sys


def extract_content_elements(content):
    """Extract key elements from source content."""
    # Title
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else "Untitled"

    # Headers (H2s)
    headers = re.findall(r'^##\s+(.+)$', content, re.MULTILINE)

    # Key points (H3s)
    subheaders = re.findall(r'^###\s+(.+)$', content, re.MULTILINE)

    # Statistics
    stats = re.findall(r'(\d+(?:\.\d+)?%[^.]*\.)', content)
    numbers = re.findall(r'(\d+(?:,\d{3})*\+?\s+\w+[^.]*\.)', content)

    # Quotes (bold text)
    quotes = re.findall(r'\*\*([^*]{20,})\*\*', content)

    # Lists
    bullets = re.findall(r'^\s*[-*]\s+(.+)$', content, re.MULTILINE)

    return {
        "title": title,
        "headers": headers,
        "subheaders": subheaders,
        "stats": stats[:5],
        "numbers": numbers[:5],
        "quotes": quotes[:5],
        "bullets": bullets[:15]
    }


def generate_twitter_thread(elements):
    """Generate Twitter thread from content elements."""
    thread = []

    # Hook tweet
    hook = f"Here's everything you need to know about {elements['title']}:\n\n🧵"
    thread.append({"tweet": 1, "content": hook, "type": "hook"})

    # Content tweets from headers
    for i, header in enumerate(elements['headers'][:7], 2):
        tweet_content = f"{i-1}/ {header}\n\n[Add 1-2 sentences explaining this point]"
        thread.append({"tweet": i, "content": tweet_content, "type": "point"})

    # Closing tweet
    closing = f"That's {len(elements['headers'][:7])} key points about {elements['title']}.\n\n"
    closing += "If this was helpful:\n→ Follow for more\n→ Retweet to share\n\n"
    closing += "[Optional: link to full article]"
    thread.append({"tweet": len(thread) + 1, "content": closing, "type": "cta"})

    return thread


def generate_twitter_singles(elements):
    """Generate single tweets from content elements."""
    singles = []

    # Quote tweets
    for quote in elements['quotes'][:3]:
        if len(quote) < 250:
            singles.append({
                "type": "quote",
                "content": f'"{quote}"'
            })

    # Stat tweets
    for stat in elements['stats'][:2]:
        singles.append({
            "type": "stat",
            "content": f"📊 {stat}\n\n[Add context or your take]"
        })

    # List tweet
    if elements['bullets']:
        list_tweet = f"{len(elements['bullets'][:5])} quick tips:\n\n"
        for bullet in elements['bullets'][:5]:
            list_tweet += f"• {bullet[:60]}...\n" if len(bullet) > 60 else f"• {bullet}\n"
        singles.append({
            "type": "list",
            "content": list_tweet
        })

    return singles


def generate_linkedin_post(elements):
    """Generate LinkedIn post from content elements."""
    post = f"""[HOOK: Start with attention-grabbing statement about {elements['title']}]

I spent [time] learning about {elements['title']}.

Here's what I discovered:

"""

    # Add key points
    for i, header in enumerate(elements['headers'][:5], 1):
        post += f"{i}. {header}\n   ↳ [Brief explanation]\n\n"

    post += """The biggest takeaway?

[Your main insight]

---

What's your experience with this? Drop a comment below 👇

#[topic] #[industry] #[relevant]"""

    return post


def generate_linkedin_carousel(elements):
    """Generate LinkedIn carousel slide content."""
    slides = []

    # Cover slide
    slides.append({
        "slide": 1,
        "type": "cover",
        "content": elements['title'],
        "subtitle": f"{len(elements['headers'])} Key Insights"
    })

    # Content slides
    for i, header in enumerate(elements['headers'][:6], 2):
        slides.append({
            "slide": i,
            "type": "content",
            "headline": header,
            "body": "[2-3 bullet points or brief explanation]"
        })

    # Summary slide
    slides.append({
        "slide": len(slides) + 1,
        "type": "summary",
        "content": "Key Takeaways",
        "points": elements['headers'][:5]
    })

    # CTA slide
    slides.append({
        "slide": len(slides) + 1,
        "type": "cta",
        "content": "Found this helpful?",
        "actions": ["Save this post 📌", "Follow for more", "@[handle]"]
    })

    return slides


def generate_instagram_carousel(elements):
    """Generate Instagram carousel slide content."""
    slides = []

    # Cover
    slides.append({
        "slide": 1,
        "type": "cover",
        "headline": elements['title'],
        "subtitle": "Swipe →"
    })

    # Problem/hook
    slides.append({
        "slide": 2,
        "type": "problem",
        "content": "[State the problem your audience faces]"
    })

    # Content slides
    for i, header in enumerate(elements['headers'][:5], 3):
        slides.append({
            "slide": i,
            "type": "tip",
            "number": i - 2,
            "headline": header,
            "body": "[Brief explanation with visual suggestion]"
        })

    # Summary
    slides.append({
        "slide": len(slides) + 1,
        "type": "summary",
        "content": "Quick Recap",
        "points": [h[:30] + "..." if len(h) > 30 else h for h in elements['headers'][:5]]
    })

    # CTA
    slides.append({
        "slide": len(slides) + 1,
        "type": "cta",
        "content": ["📌 Save this", "📤 Share with a friend", "👤 Follow @[handle]"]
    })

    return slides


def generate_video_script(elements):
    """Generate short-form video script."""
    script = {
        "title": elements['title'],
        "duration": "30-60 seconds",
        "sections": []
    }

    # Hook
    script["sections"].append({
        "section": "hook",
        "timing": "0-3 seconds",
        "text": f"[X] things you need to know about {elements['title']}",
        "visual": "Text on screen, face to camera"
    })

    # Points (max 3 for short video)
    for i, header in enumerate(elements['headers'][:3], 1):
        script["sections"].append({
            "section": f"point_{i}",
            "timing": f"{3 + (i-1)*12}-{3 + i*12} seconds",
            "text": f"Number {i}: {header}. [Add brief explanation]",
            "visual": f"Text overlay: '{header}'"
        })

    # CTA
    script["sections"].append({
        "section": "cta",
        "timing": "final 5 seconds",
        "text": "Follow for more tips like this",
        "visual": "Follow button animation"
    })

    return script


def generate_all(content):
    """Generate content for all platforms."""
    elements = extract_content_elements(content)

    return {
        "source": {
            "title": elements["title"],
            "headers_found": len(elements["headers"]),
            "quotes_found": len(elements["quotes"]),
            "stats_found": len(elements["stats"])
        },
        "twitter": {
            "thread": generate_twitter_thread(elements),
            "singles": generate_twitter_singles(elements)
        },
        "linkedin": {
            "post": generate_linkedin_post(elements),
            "carousel": generate_linkedin_carousel(elements)
        },
        "instagram": {
            "carousel": generate_instagram_carousel(elements)
        },
        "video": {
            "script": generate_video_script(elements)
        }
    }


def main():
    parser = argparse.ArgumentParser(description="Generate social media posts")
    parser.add_argument("--source", "-s", required=True, help="Source content file")
    parser.add_argument("--platform", "-p", default="all",
                        choices=["twitter", "linkedin", "instagram", "video", "all"],
                        help="Target platform")
    parser.add_argument("--format", "-f", choices=["json", "text"], default="json",
                        help="Output format")

    args = parser.parse_args()

    try:
        with open(args.source, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(json.dumps({"error": f"File not found: {args.source}"}))
        sys.exit(1)

    elements = extract_content_elements(content)

    if args.platform == "all":
        result = generate_all(content)
    elif args.platform == "twitter":
        result = {
            "thread": generate_twitter_thread(elements),
            "singles": generate_twitter_singles(elements)
        }
    elif args.platform == "linkedin":
        result = {
            "post": generate_linkedin_post(elements),
            "carousel": generate_linkedin_carousel(elements)
        }
    elif args.platform == "instagram":
        result = {
            "carousel": generate_instagram_carousel(elements)
        }
    elif args.platform == "video":
        result = {
            "script": generate_video_script(elements)
        }

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        # Text format for easier reading
        print(f"\n=== Social Content for: {elements['title']} ===\n")
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
