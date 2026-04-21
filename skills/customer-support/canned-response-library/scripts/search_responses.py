#!/usr/bin/env python3
"""Find the right template for a situation.

Usage:
    python scripts/search_responses.py --category troubleshooting --tags "login,password"
    python scripts/search_responses.py --query "customer angry about billing"
    python scripts/search_responses.py --category apology --channel email
"""

import argparse
import json
import sys
from datetime import datetime

# Sample template library
TEMPLATE_LIBRARY = [
    {
        "id": "GREET-001",
        "name": "Standard Welcome",
        "category": "greeting",
        "tags": ["first-contact", "general", "opening"],
        "channel": "all",
        "tone": "friendly",
        "usage_count": 1523,
        "avg_csat": 4.3,
        "keywords": ["hello", "welcome", "new", "first time", "help"],
    },
    {
        "id": "GREET-002",
        "name": "Returning Customer Welcome",
        "category": "greeting",
        "tags": ["returning", "loyalty", "rapport"],
        "channel": "all",
        "tone": "warm",
        "usage_count": 892,
        "avg_csat": 4.5,
        "keywords": ["welcome back", "returning", "loyal", "history"],
    },
    {
        "id": "TRBL-001",
        "name": "Step-by-Step Instructions",
        "category": "troubleshooting",
        "tags": ["steps", "instructions", "guided", "resolution"],
        "channel": "all",
        "tone": "helpful",
        "usage_count": 2341,
        "avg_csat": 4.1,
        "keywords": ["steps", "instructions", "how to", "guide", "fix"],
    },
    {
        "id": "TRBL-002",
        "name": "Request Diagnostic Information",
        "category": "troubleshooting",
        "tags": ["diagnostics", "information-request", "technical"],
        "channel": "all",
        "tone": "professional",
        "usage_count": 1876,
        "avg_csat": 3.9,
        "keywords": ["browser", "error", "screenshot", "version", "device", "diagnostics"],
    },
    {
        "id": "TRBL-003",
        "name": "Known Issue Acknowledgment",
        "category": "troubleshooting",
        "tags": ["known-issue", "workaround", "transparency", "outage"],
        "channel": "all",
        "tone": "transparent",
        "usage_count": 654,
        "avg_csat": 3.8,
        "keywords": ["known issue", "outage", "working on it", "workaround", "engineering"],
    },
    {
        "id": "TRBL-004",
        "name": "Login/Password Reset Guide",
        "category": "troubleshooting",
        "tags": ["login", "password", "reset", "access", "authentication"],
        "channel": "all",
        "tone": "helpful",
        "usage_count": 3102,
        "avg_csat": 4.2,
        "keywords": ["login", "password", "reset", "can't log in", "locked out", "access"],
    },
    {
        "id": "RSLV-001",
        "name": "Issue Resolved",
        "category": "resolution",
        "tags": ["resolved", "confirmation", "success"],
        "channel": "all",
        "tone": "positive",
        "usage_count": 2987,
        "avg_csat": 4.6,
        "keywords": ["resolved", "fixed", "done", "working", "confirmed"],
    },
    {
        "id": "RSLV-002",
        "name": "Issue Resolved with Compensation",
        "category": "resolution",
        "tags": ["resolved", "compensation", "goodwill", "credit"],
        "channel": "all",
        "tone": "apologetic",
        "usage_count": 456,
        "avg_csat": 4.4,
        "keywords": ["resolved", "credit", "compensation", "refund", "goodwill"],
    },
    {
        "id": "APOL-001",
        "name": "Service Disruption Apology",
        "category": "apology",
        "tags": ["apology", "disruption", "outage", "incident"],
        "channel": "all",
        "tone": "empathetic",
        "usage_count": 321,
        "avg_csat": 3.7,
        "keywords": ["sorry", "disruption", "outage", "down", "unavailable"],
    },
    {
        "id": "APOL-002",
        "name": "Billing Error Apology",
        "category": "apology",
        "tags": ["apology", "billing", "overcharge", "refund", "financial"],
        "channel": "email",
        "tone": "serious",
        "usage_count": 198,
        "avg_csat": 4.0,
        "keywords": ["billing", "overcharge", "charge", "invoice", "payment", "refund", "angry"],
    },
    {
        "id": "APOL-003",
        "name": "Delayed Response Apology",
        "category": "apology",
        "tags": ["apology", "delay", "slow-response", "SLA"],
        "channel": "all",
        "tone": "accountable",
        "usage_count": 543,
        "avg_csat": 3.9,
        "keywords": ["late", "delay", "slow", "waiting", "sorry for the wait"],
    },
    {
        "id": "CLOS-001",
        "name": "Standard Close",
        "category": "closing",
        "tags": ["closing", "standard", "end-conversation"],
        "channel": "all",
        "tone": "warm",
        "usage_count": 4521,
        "avg_csat": 4.3,
        "keywords": ["anything else", "close", "goodbye", "end"],
    },
    {
        "id": "FLUP-001",
        "name": "Post-Resolution Check-In",
        "category": "follow-up",
        "tags": ["follow-up", "check-in", "post-resolution"],
        "channel": "email",
        "tone": "caring",
        "usage_count": 876,
        "avg_csat": 4.5,
        "keywords": ["follow up", "check in", "still working", "any issues"],
    },
]


def search_templates(category=None, tags=None, query=None, channel=None):
    """Search templates by category, tags, and/or keyword query."""
    results = TEMPLATE_LIBRARY.copy()

    # Filter by category
    if category:
        results = [t for t in results if t["category"] == category]

    # Filter by channel
    if channel:
        results = [t for t in results if t["channel"] in [channel, "all"]]

    # Filter by tags
    if tags:
        tag_list = [t.strip().lower() for t in tags.split(",")]
        results = [
            t for t in results
            if any(tag in [x.lower() for x in t["tags"]] for tag in tag_list)
        ]

    # Score by query relevance
    if query:
        query_words = query.lower().split()
        scored = []
        for t in results:
            score = 0
            all_text = " ".join(t["keywords"] + t["tags"] + [t["name"].lower(), t["category"]])
            for word in query_words:
                if word in all_text:
                    score += 1
            if score > 0:
                scored.append((t, score))
        scored.sort(key=lambda x: (-x[1], -x[0]["usage_count"]))
        results = [t for t, _ in scored]
    else:
        # Sort by usage count (most popular first)
        results.sort(key=lambda x: -x["usage_count"])

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Find the right template for a situation"
    )
    parser.add_argument(
        "--category",
        choices=["greeting", "troubleshooting", "resolution", "follow-up", "closing", "apology", "policy"],
        help="Filter by category",
    )
    parser.add_argument(
        "--tags",
        help="Comma-separated tags to filter by (e.g., 'login,password')",
    )
    parser.add_argument(
        "--query",
        help="Free-text search query (e.g., 'customer angry about billing')",
    )
    parser.add_argument(
        "--channel",
        choices=["email", "chat", "phone", "all"],
        help="Filter by channel",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=5,
        help="Maximum results to return (default: 5)",
    )

    args = parser.parse_args()

    if not any([args.category, args.tags, args.query, args.channel]):
        parser.error("At least one search criterion is required (--category, --tags, --query, or --channel)")

    results = search_templates(args.category, args.tags, args.query, args.channel)
    limited = results[:args.limit]

    output = {
        "query": {
            "category": args.category,
            "tags": args.tags,
            "text_query": args.query,
            "channel": args.channel,
        },
        "total_matches": len(results),
        "showing": len(limited),
        "results": [
            {
                "id": t["id"],
                "name": t["name"],
                "category": t["category"],
                "tags": t["tags"],
                "channel": t["channel"],
                "tone": t["tone"],
                "usage_count": t["usage_count"],
                "avg_csat": t["avg_csat"],
            }
            for t in limited
        ],
    }

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
