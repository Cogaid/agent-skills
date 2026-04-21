#!/usr/bin/env python3
"""Extract main points from a document using heuristic analysis.

Usage:
    python key_points_extractor.py --text "Your text here" --max-points 5
    python key_points_extractor.py --file document.txt --format json
    python key_points_extractor.py --example
"""

import argparse
import json
import re
import sys
from datetime import datetime

SAMPLE_TEXT = """
The global semiconductor industry is undergoing a fundamental restructuring driven by
geopolitical tensions and supply chain resilience concerns. In 2024, worldwide chip
revenue reached $580 billion, a 15% increase from the previous year, largely driven
by AI accelerator demand.

The United States passed the CHIPS Act, allocating $52 billion to domestic semiconductor
manufacturing. This represents the largest federal investment in chip manufacturing in
US history. Intel, TSMC, and Samsung have all announced major US fabrication facility
plans, with combined investment exceeding $100 billion through 2030.

However, significant challenges remain. The talent gap is critical: the industry needs
an estimated 70,000 additional engineers by 2027, but US universities are producing only
40,000 relevant graduates annually. Immigration policy will play a key role in bridging
this gap.

Advanced packaging technology has emerged as the next battleground. Chiplet architectures
allow companies to combine specialized dies, improving yield and reducing costs by up to
30%. TSMC's CoWoS and Intel's Foveros are leading competing approaches.

Meanwhile, China's semiconductor self-sufficiency push has accelerated. SMIC achieved
7nm production capability despite US export controls, though at significantly lower yields
and higher costs than TSMC. China now accounts for 30% of global chip purchases but only
7% of advanced chip production.

Industry analysts project that by 2030, the semiconductor market will reach $1 trillion,
with AI chips comprising 25% of total revenue. The companies that master advanced packaging,
secure talent pipelines, and navigate geopolitical complexity will define the next era of
computing.
"""


def extract_key_points(text: str, max_points: int = 5) -> dict:
    """Extract key points using heuristic sentence scoring."""
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if len(s.strip()) > 30]

    scored = []
    for sentence in sentences:
        score = 0.0

        # Position scoring: first and last sentences of paragraphs score higher
        if sentences.index(sentence) < 3:
            score += 2.0
        if sentences.index(sentence) >= len(sentences) - 3:
            score += 1.5

        # Numeric data presence
        numbers = re.findall(r'\$?\d+[\d,.]*\s*(?:billion|million|%|trillion)', sentence, re.IGNORECASE)
        score += len(numbers) * 2.0

        # Key indicator phrases
        indicators = ["however", "critical", "significant", "key", "major", "largest",
                       "emerged", "despite", "project", "estimated", "reached", "leading"]
        for indicator in indicators:
            if indicator.lower() in sentence.lower():
                score += 1.0

        # Named entity density (simple heuristic: capitalized words)
        capitals = re.findall(r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b', sentence)
        score += len(capitals) * 0.3

        # Length preference (medium-length sentences)
        word_count = len(sentence.split())
        if 15 <= word_count <= 35:
            score += 1.0

        scored.append({"sentence": sentence.strip(), "score": round(score, 2), "word_count": word_count})

    scored.sort(key=lambda x: x["score"], reverse=True)
    top_points = scored[:max_points]

    # Re-sort by original position for logical flow
    for point in top_points:
        point["original_position"] = sentences.index(point["sentence"])
    top_points.sort(key=lambda x: x["original_position"])

    # Extract statistics
    all_numbers = re.findall(r'\$?\d+[\d,.]*\s*(?:billion|million|%|trillion|thousand)', text, re.IGNORECASE)

    return {
        "total_sentences": len(sentences),
        "total_words": len(text.split()),
        "points_extracted": len(top_points),
        "key_points": [p["sentence"] for p in top_points],
        "scored_points": top_points,
        "statistics_found": all_numbers,
        "compression_ratio": f"{len(text.split()) // max(1, sum(len(p['sentence'].split()) for p in top_points))}:1",
    }


def main():
    parser = argparse.ArgumentParser(description="Extract main points from a document.")
    parser.add_argument("--text", help="Text to analyze")
    parser.add_argument("--file", help="Path to text file")
    parser.add_argument("--max-points", type=int, default=5, help="Maximum number of key points (default: 5)")
    parser.add_argument("--example", action="store_true", help="Run with example text")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format")

    args = parser.parse_args()

    if args.file:
        with open(args.file) as f:
            text = f.read()
    elif args.text:
        text = args.text
    else:
        text = SAMPLE_TEXT

    result = extract_key_points(text, args.max_points)
    result["extracted_at"] = datetime.now().isoformat()

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print("Key Points Extraction")
        print("=" * 60)
        print(f"  Source: {result['total_words']} words, {result['total_sentences']} sentences")
        print(f"  Points extracted: {result['points_extracted']}")
        print(f"  Compression: {result['compression_ratio']}")
        print()
        print("KEY POINTS:")
        for i, point in enumerate(result["key_points"], 1):
            print(f"  {i}. {point}")
        print()
        if result["statistics_found"]:
            print("STATISTICS FOUND:")
            for stat in result["statistics_found"]:
                print(f"  - {stat}")
        print()
        print("SCORED DETAIL:")
        for p in result["scored_points"]:
            print(f"  [{p['score']:.1f}] {p['sentence'][:80]}...")
        print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
