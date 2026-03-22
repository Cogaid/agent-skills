#!/usr/bin/env python3
"""
Build Twitter threads from source content.

Usage:
    python thread_builder.py --source blog-post.md
    python thread_builder.py --source blog-post.md --max-tweets 10
    python thread_builder.py --source blog-post.md --style lessons

Output: Formatted Twitter thread ready to post
"""

import argparse
import json
import re
import sys


# Thread style templates
THREAD_STYLES = {
    "lessons": {
        "hook": "I {action} for {timeframe}.\n\nHere are {count} lessons that changed everything:\n\n🧵",
        "point": "{num}/ {content}\n\n{explanation}",
        "close": "That's {count} lessons from {topic}.\n\nTL;DR:\n{summary}\n\nFollow @[handle] for more.\n\n♻️ Retweet if this helped"
    },
    "howto": {
        "hook": "How to {topic}:\n\n(Step by step)\n\n🧵",
        "point": "Step {num}: {content}\n\n{explanation}",
        "close": "That's it! {count} steps to {outcome}.\n\nSave this thread.\nFollow @[handle] for more."
    },
    "myths": {
        "hook": "{count} {topic} myths that are holding you back:\n\n(Especially #{special})\n\n🧵",
        "point": "Myth {num}: \"{content}\"\n\nReality: {explanation}",
        "close": "Stop believing myths.\nStart seeing results.\n\nRT to save someone from these myths."
    },
    "mistakes": {
        "hook": "{count} {topic} mistakes I see every day:\n\n(Are you making #{special}?)\n\n🧵",
        "point": "Mistake {num}: {content}\n\nInstead: {explanation}",
        "close": "Avoid these {count} mistakes.\n\nShare with someone who needs this."
    },
    "tips": {
        "hook": "{count} {topic} tips that actually work:\n\n🧵",
        "point": "{num}. {content}\n\n{explanation}",
        "close": "Those are {count} tips to improve your {topic}.\n\nWhich one are you trying first?\n\nFollow for more."
    }
}


def extract_thread_elements(content):
    """Extract elements for thread building."""
    # Title
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else "topic"

    # Headers as main points
    headers = re.findall(r'^##\s+(.+)$', content, re.MULTILINE)

    # Get content under each header
    sections = {}
    header_pattern = r'^##\s+(.+)$'
    parts = re.split(header_pattern, content, flags=re.MULTILINE)

    current_header = None
    for part in parts:
        if re.match(r'^[A-Z]', part.strip()) and len(part) < 100:
            current_header = part.strip()
            sections[current_header] = ""
        elif current_header:
            sections[current_header] = part.strip()[:500]  # Limit section length

    # Extract bullet points
    bullets = re.findall(r'^\s*[-*]\s+(.+)$', content, re.MULTILINE)

    # Extract quotes
    quotes = re.findall(r'\*\*([^*]{20,100})\*\*', content)

    return {
        "title": title,
        "headers": headers,
        "sections": sections,
        "bullets": bullets,
        "quotes": quotes
    }


def truncate_to_tweet_length(text, max_chars=270):
    """Truncate text to fit tweet character limit."""
    if len(text) <= max_chars:
        return text
    return text[:max_chars-3] + "..."


def build_thread(elements, style="tips", max_tweets=10):
    """Build a complete thread."""
    template = THREAD_STYLES.get(style, THREAD_STYLES["tips"])
    thread = []
    points = elements["headers"][:max_tweets - 2]  # Leave room for hook and close

    # Build hook
    hook_vars = {
        "action": "studied",
        "timeframe": "years",
        "topic": elements["title"],
        "count": len(points),
        "special": min(3, len(points))
    }
    hook = template["hook"].format(**hook_vars)
    thread.append({
        "number": 1,
        "type": "hook",
        "content": truncate_to_tweet_length(hook),
        "chars": len(hook)
    })

    # Build point tweets
    for i, header in enumerate(points, 1):
        section_content = elements["sections"].get(header, "")
        # Get first sentence or bullet as explanation
        first_sentence = re.split(r'[.!?]', section_content)
        explanation = first_sentence[0].strip() if first_sentence else "[Add explanation]"
        explanation = explanation[:150] if len(explanation) > 150 else explanation

        point_vars = {
            "num": i,
            "content": header,
            "explanation": explanation
        }
        point = template["point"].format(**point_vars)
        thread.append({
            "number": i + 1,
            "type": "point",
            "content": truncate_to_tweet_length(point),
            "chars": len(point)
        })

    # Build closing tweet
    summary = "\n".join([f"• {h[:40]}" for h in points[:5]])
    close_vars = {
        "count": len(points),
        "topic": elements["title"],
        "outcome": elements["title"].lower(),
        "summary": summary
    }
    close = template["close"].format(**close_vars)
    thread.append({
        "number": len(thread) + 1,
        "type": "close",
        "content": truncate_to_tweet_length(close, 280),
        "chars": len(close)
    })

    return thread


def format_thread_output(thread, format_type="json"):
    """Format thread for output."""
    if format_type == "json":
        return thread

    # Plain text format
    output = []
    output.append("=" * 50)
    output.append("TWITTER THREAD")
    output.append("=" * 50)

    for tweet in thread:
        output.append(f"\n--- Tweet {tweet['number']} ({tweet['type']}) [{tweet['chars']} chars] ---")
        output.append(tweet['content'])

    output.append("\n" + "=" * 50)
    output.append(f"Total tweets: {len(thread)}")
    output.append("=" * 50)

    return "\n".join(output)


def interactive_mode():
    """Interactive thread building."""
    print("\n=== Twitter Thread Builder ===\n")

    topic = input("What's the topic? ")
    print("\nAvailable styles: lessons, howto, myths, mistakes, tips")
    style = input("Which style? [tips]: ").strip() or "tips"

    points = []
    print("\nEnter your main points (empty line to finish):")
    while True:
        point = input(f"Point {len(points) + 1}: ").strip()
        if not point:
            break
        points.append(point)

    if not points:
        print("No points entered. Exiting.")
        return

    # Build simple thread
    elements = {
        "title": topic,
        "headers": points,
        "sections": {p: "" for p in points},
        "bullets": [],
        "quotes": []
    }

    thread = build_thread(elements, style, max_tweets=len(points) + 2)

    print("\n" + "=" * 50)
    print("YOUR THREAD")
    print("=" * 50)

    for tweet in thread:
        print(f"\n--- Tweet {tweet['number']} ---")
        print(tweet['content'])

    print("\n" + "=" * 50)


def main():
    parser = argparse.ArgumentParser(description="Build Twitter threads")
    parser.add_argument("--source", "-s", help="Source content file")
    parser.add_argument("--max-tweets", "-m", type=int, default=10,
                        help="Maximum number of tweets")
    parser.add_argument("--style", choices=list(THREAD_STYLES.keys()),
                        default="tips", help="Thread style")
    parser.add_argument("--format", "-f", choices=["json", "text"],
                        default="json", help="Output format")
    parser.add_argument("--interactive", "-i", action="store_true",
                        help="Interactive mode")

    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
        return

    if not args.source:
        print("Error: --source is required (or use --interactive)")
        sys.exit(1)

    try:
        with open(args.source, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(json.dumps({"error": f"File not found: {args.source}"}))
        sys.exit(1)

    elements = extract_thread_elements(content)
    thread = build_thread(elements, args.style, args.max_tweets)

    if args.format == "json":
        result = {
            "source_title": elements["title"],
            "style": args.style,
            "total_tweets": len(thread),
            "thread": thread
        }
        print(json.dumps(result, indent=2))
    else:
        print(format_thread_output(thread, "text"))


if __name__ == "__main__":
    main()
