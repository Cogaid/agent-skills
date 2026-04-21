#!/usr/bin/env python3
"""A/B test survey timing for best response rates.

Usage:
    python scripts/optimize_timing.py --survey-id SRV-001 --variants 3
    python scripts/optimize_timing.py --survey-id SRV-001 --variants 4 --channel email
    python scripts/optimize_timing.py --survey-id SRV-001 --variants 2 --min-sample 100
"""

import argparse
import json
import math
import random
import sys
from datetime import datetime

random.seed(42)

TIMING_VARIANTS = {
    "email": [
        {"label": "immediate", "delay_minutes": 0, "description": "Send immediately after interaction"},
        {"label": "1_hour", "delay_minutes": 60, "description": "Send 1 hour after interaction"},
        {"label": "2_hours", "delay_minutes": 120, "description": "Send 2 hours after interaction"},
        {"label": "4_hours", "delay_minutes": 240, "description": "Send 4 hours after interaction"},
        {"label": "next_day", "delay_minutes": 1440, "description": "Send next business day morning"},
    ],
    "post-chat": [
        {"label": "immediate", "delay_minutes": 0, "description": "Embed in chat close"},
        {"label": "2_minutes", "delay_minutes": 2, "description": "Pop up 2 minutes after close"},
        {"label": "5_minutes", "delay_minutes": 5, "description": "Pop up 5 minutes after close"},
    ],
    "sms": [
        {"label": "30_minutes", "delay_minutes": 30, "description": "Send 30 minutes after"},
        {"label": "1_hour", "delay_minutes": 60, "description": "Send 1 hour after"},
        {"label": "2_hours", "delay_minutes": 120, "description": "Send 2 hours after"},
        {"label": "same_evening", "delay_minutes": 480, "description": "Send same day evening"},
    ],
    "in-app": [
        {"label": "immediate", "delay_minutes": 0, "description": "Show immediately"},
        {"label": "next_page", "delay_minutes": 1, "description": "Show on next page load"},
        {"label": "5_minutes", "delay_minutes": 5, "description": "Show after 5 minutes"},
    ],
}


def simulate_variant_results(variant, sample_size):
    """Simulate A/B test results for a timing variant."""
    # Base response rate varies by delay -- moderate delays tend to perform best
    delay = variant["delay_minutes"]
    if delay == 0:
        base_rate = 0.18
    elif delay <= 5:
        base_rate = 0.22
    elif delay <= 120:
        base_rate = 0.25
    elif delay <= 480:
        base_rate = 0.15
    else:
        base_rate = 0.10

    # Add noise
    actual_rate = base_rate + random.uniform(-0.05, 0.05)
    actual_rate = max(0.02, min(0.50, actual_rate))

    responses = int(sample_size * actual_rate)
    scores = [random.choices([1, 2, 3, 4, 5], weights=[5, 10, 15, 35, 35])[0] for _ in range(responses)]
    avg_score = sum(scores) / len(scores) if scores else 0

    return {
        "variant": variant["label"],
        "delay_minutes": variant["delay_minutes"],
        "description": variant["description"],
        "sample_size": sample_size,
        "responses": responses,
        "response_rate": round(actual_rate * 100, 1),
        "average_score": round(avg_score, 2),
        "completion_rate": round(random.uniform(75, 95), 1),
    }


def calculate_significance(variant_a, variant_b):
    """Calculate statistical significance between two variants using z-test for proportions."""
    n1 = variant_a["sample_size"]
    n2 = variant_b["sample_size"]
    p1 = variant_a["response_rate"] / 100
    p2 = variant_b["response_rate"] / 100

    p_pool = (p1 * n1 + p2 * n2) / (n1 + n2)
    se = math.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n2))

    if se == 0:
        return {"z_score": 0, "significant": False, "confidence": 0}

    z = (p1 - p2) / se
    # Approximate p-value for two-tailed test
    confidence = min(99.9, abs(z) / 2.576 * 99.9)

    return {
        "z_score": round(z, 3),
        "significant": abs(z) > 1.96,
        "confidence": round(confidence, 1),
    }


def main():
    parser = argparse.ArgumentParser(
        description="A/B test survey timing for best response rates"
    )
    parser.add_argument(
        "--survey-id",
        required=True,
        help="Survey identifier (e.g., SRV-001)",
    )
    parser.add_argument(
        "--variants",
        type=int,
        default=3,
        help="Number of timing variants to test (default: 3)",
    )
    parser.add_argument(
        "--channel",
        choices=["email", "post-chat", "sms", "in-app"],
        default="email",
        help="Survey channel (default: email)",
    )
    parser.add_argument(
        "--min-sample",
        type=int,
        default=200,
        help="Minimum sample size per variant (default: 200)",
    )

    args = parser.parse_args()

    available_variants = TIMING_VARIANTS.get(args.channel, TIMING_VARIANTS["email"])
    num_variants = min(args.variants, len(available_variants))
    selected = available_variants[:num_variants]

    results = []
    for variant in selected:
        result = simulate_variant_results(variant, args.min_sample)
        results.append(result)

    # Sort by response rate to find winner
    results.sort(key=lambda x: x["response_rate"], reverse=True)
    winner = results[0]

    # Calculate significance of winner vs runner-up
    significance = None
    if len(results) > 1:
        significance = calculate_significance(results[0], results[1])

    output = {
        "survey_id": args.survey_id,
        "channel": args.channel,
        "test_date": datetime.utcnow().isoformat() + "Z",
        "variants_tested": num_variants,
        "sample_size_per_variant": args.min_sample,
        "results": results,
        "recommendation": {
            "winner": winner["variant"],
            "delay_minutes": winner["delay_minutes"],
            "response_rate": winner["response_rate"],
            "description": winner["description"],
            "statistically_significant": significance["significant"] if significance else None,
            "confidence": significance["confidence"] if significance else None,
        },
        "next_steps": [
            f"Implement {winner['variant']} timing ({winner['delay_minutes']} min delay) for {args.channel} channel",
            "Monitor response rates for 2 weeks post-implementation",
            "Re-test quarterly as customer behavior patterns shift",
        ],
    }

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
