#!/usr/bin/env python3
"""
Track and organize research sources.

Usage:
    python source_tracker.py --add "Source Title" --url "https://..."
    python source_tracker.py --list sources.json
    python source_tracker.py --cite sources.json

Output: Organized source list and citations
"""

import argparse
import json
from datetime import datetime


# Source reliability tiers
RELIABILITY_TIERS = {
    1: {
        "name": "Highly Reliable",
        "examples": ["peer-reviewed journals", "government statistics", "company filings"]
    },
    2: {
        "name": "Generally Reliable",
        "examples": ["industry publications", "expert interviews", "research firms"]
    },
    3: {
        "name": "Use with Caution",
        "examples": ["blog posts", "Wikipedia", "user reviews"]
    },
    4: {
        "name": "Verification Required",
        "examples": ["anonymous sources", "unattributed claims", "social media"]
    }
}

# Source type categories
SOURCE_TYPES = [
    "academic",
    "news",
    "industry_report",
    "company_official",
    "government",
    "expert_opinion",
    "user_review",
    "blog",
    "social_media",
    "other"
]


def create_source_entry(
    title,
    url=None,
    author=None,
    publication=None,
    date=None,
    source_type="other",
    reliability=3,
    key_findings=None,
    notes=None
):
    """Create a new source entry."""

    return {
        "id": f"S{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "title": title,
        "url": url,
        "author": author,
        "publication": publication,
        "date_published": date,
        "date_accessed": datetime.now().strftime("%Y-%m-%d"),
        "type": source_type,
        "reliability_tier": reliability,
        "key_findings": key_findings or [],
        "notes": notes,
        "used": False
    }


def load_sources(file_path):
    """Load sources from JSON file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"project": "", "sources": [], "created": datetime.now().isoformat()}


def save_sources(data, file_path):
    """Save sources to JSON file."""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)


def add_source(data, source_entry):
    """Add a new source to the data."""
    data["sources"].append(source_entry)
    data["last_updated"] = datetime.now().isoformat()
    return data


def list_sources(data, filter_type=None, filter_reliability=None, filter_used=None):
    """List sources with optional filtering."""

    sources = data.get("sources", [])

    if filter_type:
        sources = [s for s in sources if s.get("type") == filter_type]

    if filter_reliability:
        sources = [s for s in sources if s.get("reliability_tier") == filter_reliability]

    if filter_used is not None:
        sources = [s for s in sources if s.get("used") == filter_used]

    return sources


def generate_citations(sources, style="apa"):
    """Generate formatted citations."""

    citations = []

    for source in sources:
        if not source.get("used", True):
            continue

        author = source.get("author", "Unknown Author")
        title = source.get("title", "Untitled")
        pub = source.get("publication", "")
        date = source.get("date_published", "n.d.")
        url = source.get("url", "")
        accessed = source.get("date_accessed", "")

        if style == "apa":
            citation = f"{author}. ({date}). {title}."
            if pub:
                citation += f" {pub}."
            if url:
                citation += f" Retrieved {accessed} from {url}"

        elif style == "mla":
            citation = f'{author}. "{title}."'
            if pub:
                citation += f" {pub},"
            citation += f" {date}."
            if url:
                citation += f" {url}. Accessed {accessed}."

        elif style == "simple":
            citation = f"{title}"
            if author and author != "Unknown Author":
                citation += f" by {author}"
            if date and date != "n.d.":
                citation += f" ({date})"
            if url:
                citation += f" - {url}"

        citations.append({
            "id": source.get("id"),
            "citation": citation
        })

    return citations


def analyze_sources(data):
    """Analyze source collection quality."""

    sources = data.get("sources", [])

    if not sources:
        return {"error": "No sources to analyze"}

    total = len(sources)
    used = sum(1 for s in sources if s.get("used", False))

    # Reliability distribution
    reliability_dist = {}
    for tier in range(1, 5):
        count = sum(1 for s in sources if s.get("reliability_tier") == tier)
        reliability_dist[f"tier_{tier}"] = count

    # Type distribution
    type_dist = {}
    for s in sources:
        stype = s.get("type", "other")
        type_dist[stype] = type_dist.get(stype, 0) + 1

    # Calculate quality score
    quality_score = 0
    for tier, count in reliability_dist.items():
        tier_num = int(tier.split("_")[1])
        # Higher tiers (1-2) add more to quality
        quality_score += count * (5 - tier_num) * 10

    if total > 0:
        quality_score = min(100, quality_score / total)

    # Generate recommendations
    recommendations = []

    if reliability_dist.get("tier_1", 0) < 2:
        recommendations.append("Add more Tier 1 sources (peer-reviewed, official)")

    if len(type_dist) < 3:
        recommendations.append("Diversify source types")

    if quality_score < 50:
        recommendations.append("Overall source quality could be improved")

    return {
        "total_sources": total,
        "sources_used": used,
        "reliability_distribution": reliability_dist,
        "type_distribution": type_dist,
        "quality_score": round(quality_score, 1),
        "recommendations": recommendations
    }


def export_sources(data, format_type="json"):
    """Export sources in various formats."""

    if format_type == "json":
        return json.dumps(data, indent=2)

    elif format_type == "text":
        lines = []
        lines.append("\n" + "=" * 60)
        lines.append("SOURCE LIST")
        lines.append("=" * 60)

        if data.get("project"):
            lines.append(f"\nProject: {data['project']}")

        lines.append(f"Total Sources: {len(data.get('sources', []))}")

        for source in data.get("sources", []):
            lines.append(f"\n--- {source['id']} ---")
            lines.append(f"Title: {source.get('title', 'N/A')}")
            lines.append(f"Author: {source.get('author', 'N/A')}")
            lines.append(f"Type: {source.get('type', 'N/A')}")
            lines.append(f"Reliability: Tier {source.get('reliability_tier', 'N/A')}")
            if source.get('url'):
                lines.append(f"URL: {source['url']}")
            if source.get('key_findings'):
                lines.append("Key Findings:")
                for finding in source['key_findings']:
                    lines.append(f"  • {finding}")

        return "\n".join(lines)

    elif format_type == "markdown":
        lines = []
        lines.append(f"# Source List")

        if data.get("project"):
            lines.append(f"\n**Project:** {data['project']}")

        lines.append(f"\n## Sources ({len(data.get('sources', []))} total)\n")

        for source in data.get("sources", []):
            lines.append(f"### {source.get('title', 'Untitled')}")
            lines.append(f"- **ID:** {source['id']}")
            lines.append(f"- **Author:** {source.get('author', 'N/A')}")
            lines.append(f"- **Type:** {source.get('type', 'N/A')}")
            lines.append(f"- **Reliability:** Tier {source.get('reliability_tier', 'N/A')}")
            if source.get('url'):
                lines.append(f"- **URL:** {source['url']}")
            if source.get('key_findings'):
                lines.append(f"- **Key Findings:**")
                for finding in source['key_findings']:
                    lines.append(f"  - {finding}")
            lines.append("")

        return "\n".join(lines)

    return json.dumps(data, indent=2)


def interactive_add():
    """Interactive source addition."""

    print("\n=== Add Source ===\n")

    title = input("Source title: ").strip()
    url = input("URL (optional): ").strip() or None
    author = input("Author (optional): ").strip() or None
    publication = input("Publication (optional): ").strip() or None
    date = input("Publication date (YYYY-MM-DD, optional): ").strip() or None

    print(f"\nSource types: {', '.join(SOURCE_TYPES)}")
    source_type = input("Type [other]: ").strip() or "other"

    print("\nReliability tiers:")
    for tier, info in RELIABILITY_TIERS.items():
        print(f"  {tier}: {info['name']}")
    try:
        reliability = int(input("Tier [3]: ").strip() or "3")
    except ValueError:
        reliability = 3

    findings = []
    print("\nKey findings (enter blank to finish):")
    while True:
        finding = input("  Finding: ").strip()
        if not finding:
            break
        findings.append(finding)

    notes = input("\nNotes (optional): ").strip() or None

    source = create_source_entry(
        title=title,
        url=url,
        author=author,
        publication=publication,
        date=date,
        source_type=source_type,
        reliability=reliability,
        key_findings=findings if findings else None,
        notes=notes
    )

    return source


def main():
    parser = argparse.ArgumentParser(description='Track research sources')
    parser.add_argument('file', nargs='?', default='sources.json',
                        help='Source file (JSON)')
    parser.add_argument('--add', '-a', action='store_true',
                        help='Add a new source (interactive)')
    parser.add_argument('--list', '-l', action='store_true',
                        help='List all sources')
    parser.add_argument('--cite', '-c', choices=['apa', 'mla', 'simple'],
                        help='Generate citations')
    parser.add_argument('--analyze', action='store_true',
                        help='Analyze source quality')
    parser.add_argument('--format', '-f', choices=['json', 'text', 'markdown'],
                        default='text', help='Output format')
    parser.add_argument('--new', '-n', help='Create new source file with project name')
    parser.add_argument('--filter-type', help='Filter by source type')
    parser.add_argument('--filter-tier', type=int, help='Filter by reliability tier')

    args = parser.parse_args()

    if args.new:
        data = {
            "project": args.new,
            "created": datetime.now().isoformat(),
            "sources": []
        }
        save_sources(data, args.file)
        print(f"Created new source file: {args.file}")
        return

    if args.add:
        data = load_sources(args.file)
        source = interactive_add()
        data = add_source(data, source)
        save_sources(data, args.file)
        print(f"\nSource added: {source['id']}")
        print(f"Saved to: {args.file}")
        return

    if args.analyze:
        data = load_sources(args.file)
        analysis = analyze_sources(data)
        if args.format == 'json':
            print(json.dumps(analysis, indent=2))
        else:
            print("\n=== Source Analysis ===")
            print(f"Total Sources: {analysis['total_sources']}")
            print(f"Quality Score: {analysis['quality_score']}/100")
            print("\nReliability Distribution:")
            for tier, count in analysis['reliability_distribution'].items():
                print(f"  {tier}: {count}")
            print("\nType Distribution:")
            for stype, count in analysis['type_distribution'].items():
                print(f"  {stype}: {count}")
            if analysis['recommendations']:
                print("\nRecommendations:")
                for rec in analysis['recommendations']:
                    print(f"  • {rec}")
        return

    if args.cite:
        data = load_sources(args.file)
        sources = [s for s in data.get("sources", []) if s.get("used", True)]
        citations = generate_citations(sources, args.cite)
        print(f"\n=== Citations ({args.cite.upper()}) ===\n")
        for i, c in enumerate(citations, 1):
            print(f"{i}. {c['citation']}\n")
        return

    if args.list or not any([args.add, args.analyze, args.cite]):
        data = load_sources(args.file)

        if args.filter_type:
            data["sources"] = [s for s in data["sources"] if s.get("type") == args.filter_type]
        if args.filter_tier:
            data["sources"] = [s for s in data["sources"] if s.get("reliability_tier") == args.filter_tier]

        print(export_sources(data, args.format))


if __name__ == '__main__':
    main()
