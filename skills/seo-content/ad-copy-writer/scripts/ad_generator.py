#!/usr/bin/env python3
"""
Ad Copy Generator -- Generate ad copy variations for multiple platforms.

Usage:
    python ad_generator.py --platform google --product "CRM Software" --benefit "Close 30% more deals" --cta "Start Free Trial"
    python ad_generator.py --platform facebook --product "AI Writing Tool" --benefit "Write 10x faster" --audience "marketers"
    python ad_generator.py --platform all --product "Project Management" --benefit "Ship 2x faster" --cta "Try Free" --output results.json
"""

import argparse
import json
import sys
from datetime import datetime

PLATFORM_SPECS = {
    "google": {
        "headline_limit": 30,
        "headline_count": 3,
        "description_limit": 90,
        "description_count": 2,
        "display_path_limit": 15,
    },
    "google_rsa": {
        "headline_limit": 30,
        "headline_count": 15,
        "description_limit": 90,
        "description_count": 4,
    },
    "facebook": {
        "primary_text_limit": 125,
        "headline_limit": 27,
        "description_limit": 27,
    },
    "linkedin": {
        "intro_limit": 150,
        "headline_limit": 70,
    },
    "twitter": {
        "tweet_limit": 280,
    },
}

HEADLINE_TEMPLATES = [
    "{benefit}",
    "Get {product} Free",
    "{benefit} Today",
    "Try {product} Free",
    "{social_proof}",
    "Save Time With {product}",
    "{benefit} - {product}",
    "Why {audience} Love {product}",
    "How to {benefit}",
    "{product}: {benefit}",
    "Stop Wasting Time",
    "{benefit} Guaranteed",
    "Free Trial - {product}",
    "{product} for {audience}",
    "Award-Winning {product}",
]

DESCRIPTION_TEMPLATES = [
    "{product} helps you {benefit_lower}. {cta} today and see results fast.",
    "Join thousands who already {benefit_lower}. {cta} - no credit card required.",
    "Rated #1 by industry experts. {product} makes it easy to {benefit_lower}. {cta}.",
    "{audience} trust {product} to {benefit_lower}. See why. {cta} now.",
]

FACEBOOK_PRIMARY_TEMPLATES = [
    "{benefit}.\n\n{product} helps {audience} achieve more in less time. See how it works.\n\n{cta} -->",
    "Tired of the old way? {product} lets you {benefit_lower} without the headache.\n\nJoin 10,000+ {audience} who switched.\n\n{cta} -->",
    "What if you could {benefit_lower}?\n\nThat's exactly what {product} does for {audience} every day.\n\n{cta} to see for yourself.",
]

LINKEDIN_INTRO_TEMPLATES = [
    "{audience} using {product} report {benefit_lower}. See the data behind the results. {cta}.",
    "New research: teams that adopt {product} see measurable improvement. {benefit}. Download the report.",
    "Is your team still doing this manually? {product} automates the process so you can {benefit_lower}. {cta}.",
]

TWITTER_TEMPLATES = [
    "Still doing it the hard way? {product} helps you {benefit_lower}. {cta}: {{link}}",
    "{benefit}. That's what {audience} get with {product}. {cta} {{link}}",
    "How {audience} {benefit_lower} -- without the busywork. {cta}: {{link}}",
    "We asked 500+ {audience} what tool changed their workflow. #1 answer: {product}. {cta} {{link}}",
]


def truncate(text, limit):
    """Truncate text to character limit."""
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."


def generate_google_ads(product, benefit, cta, audience, social_proof):
    """Generate Google Search Ad variations."""
    specs = PLATFORM_SPECS["google"]
    variations = []

    context = {
        "product": product,
        "benefit": benefit,
        "benefit_lower": benefit[0].lower() + benefit[1:] if benefit else "",
        "cta": cta,
        "audience": audience,
        "social_proof": social_proof,
    }

    for i in range(3):
        headlines = []
        for j in range(specs["headline_count"]):
            idx = (i * specs["headline_count"] + j) % len(HEADLINE_TEMPLATES)
            h = HEADLINE_TEMPLATES[idx].format(**context)
            headlines.append(truncate(h, specs["headline_limit"]))

        descriptions = []
        for j in range(specs["description_count"]):
            idx = (i * specs["description_count"] + j) % len(DESCRIPTION_TEMPLATES)
            d = DESCRIPTION_TEMPLATES[idx].format(**context)
            descriptions.append(truncate(d, specs["description_limit"]))

        variation = {
            "variant": i + 1,
            "headlines": headlines,
            "descriptions": descriptions,
            "headline_chars": [len(h) for h in headlines],
            "description_chars": [len(d) for d in descriptions],
            "within_limits": all(
                len(h) <= specs["headline_limit"] for h in headlines
            )
            and all(len(d) <= specs["description_limit"] for d in descriptions),
        }
        variations.append(variation)

    return {"platform": "google_search", "ad_type": "standard", "variations": variations}


def generate_facebook_ads(product, benefit, cta, audience, social_proof):
    """Generate Facebook/Meta ad variations."""
    specs = PLATFORM_SPECS["facebook"]
    variations = []

    context = {
        "product": product,
        "benefit": benefit,
        "benefit_lower": benefit[0].lower() + benefit[1:] if benefit else "",
        "cta": cta,
        "audience": audience,
        "social_proof": social_proof,
    }

    for i, template in enumerate(FACEBOOK_PRIMARY_TEMPLATES):
        primary = template.format(**context)
        headline = truncate(f"{benefit}", specs["headline_limit"])
        description = truncate(f"Try {product} Free", specs["description_limit"])

        variation = {
            "variant": i + 1,
            "primary_text": primary,
            "headline": headline,
            "description": description,
            "primary_text_chars": len(primary),
            "headline_chars": len(headline),
            "within_limits": len(headline) <= specs["headline_limit"]
            and len(description) <= specs["description_limit"],
        }
        variations.append(variation)

    return {"platform": "facebook", "ad_type": "single_image", "variations": variations}


def generate_linkedin_ads(product, benefit, cta, audience, social_proof):
    """Generate LinkedIn ad variations."""
    specs = PLATFORM_SPECS["linkedin"]
    variations = []

    context = {
        "product": product,
        "benefit": benefit,
        "benefit_lower": benefit[0].lower() + benefit[1:] if benefit else "",
        "cta": cta,
        "audience": audience,
        "social_proof": social_proof,
    }

    for i, template in enumerate(LINKEDIN_INTRO_TEMPLATES):
        intro = truncate(template.format(**context), specs["intro_limit"])
        headline = truncate(
            f"How {audience} {context['benefit_lower']} With {product}",
            specs["headline_limit"],
        )

        variation = {
            "variant": i + 1,
            "intro_text": intro,
            "headline": headline,
            "intro_chars": len(intro),
            "headline_chars": len(headline),
            "within_limits": len(intro) <= specs["intro_limit"]
            and len(headline) <= specs["headline_limit"],
        }
        variations.append(variation)

    return {
        "platform": "linkedin",
        "ad_type": "sponsored_content",
        "variations": variations,
    }


def generate_twitter_ads(product, benefit, cta, audience, social_proof):
    """Generate Twitter/X ad variations."""
    specs = PLATFORM_SPECS["twitter"]
    variations = []

    context = {
        "product": product,
        "benefit": benefit,
        "benefit_lower": benefit[0].lower() + benefit[1:] if benefit else "",
        "cta": cta,
        "audience": audience,
        "social_proof": social_proof,
    }

    for i, template in enumerate(TWITTER_TEMPLATES):
        tweet = template.format(**context)

        variation = {
            "variant": i + 1,
            "tweet_text": tweet,
            "char_count": len(tweet),
            "within_limits": len(tweet) <= specs["tweet_limit"],
        }
        variations.append(variation)

    return {"platform": "twitter", "ad_type": "promoted_tweet", "variations": variations}


GENERATORS = {
    "google": generate_google_ads,
    "facebook": generate_facebook_ads,
    "linkedin": generate_linkedin_ads,
    "twitter": generate_twitter_ads,
}


def main():
    parser = argparse.ArgumentParser(
        description="Generate ad copy variations for digital platforms",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --platform google --product "CRM Software" --benefit "Close 30%% more deals" --cta "Start Free Trial"
  %(prog)s --platform facebook --product "AI Writer" --benefit "Write 10x faster" --audience "marketers"
  %(prog)s --platform all --product "Analytics" --benefit "Ship 2x faster" --output results.json
        """,
    )
    parser.add_argument(
        "--platform",
        required=True,
        choices=["google", "facebook", "linkedin", "twitter", "all"],
        help="Target advertising platform",
    )
    parser.add_argument("--product", required=True, help="Product or service name")
    parser.add_argument(
        "--benefit", required=True, help="Primary benefit statement"
    )
    parser.add_argument(
        "--cta", default="Get Started", help="Call to action text (default: Get Started)"
    )
    parser.add_argument(
        "--audience",
        default="teams",
        help="Target audience descriptor (default: teams)",
    )
    parser.add_argument(
        "--social-proof",
        default="Trusted by 10,000+ Users",
        help="Social proof element",
    )
    parser.add_argument("--output", help="Output file path (default: stdout)")
    parser.add_argument(
        "--format",
        choices=["json", "text"],
        default="json",
        help="Output format (default: json)",
    )

    args = parser.parse_args()

    platforms = list(GENERATORS.keys()) if args.platform == "all" else [args.platform]

    results = {
        "generated_at": datetime.now().isoformat(),
        "input": {
            "product": args.product,
            "benefit": args.benefit,
            "cta": args.cta,
            "audience": args.audience,
            "social_proof": args.social_proof,
        },
        "ads": [],
    }

    for platform in platforms:
        generator = GENERATORS[platform]
        ad_set = generator(
            args.product, args.benefit, args.cta, args.audience, args.social_proof
        )
        results["ads"].append(ad_set)

    total_variants = sum(len(ad["variations"]) for ad in results["ads"])
    results["summary"] = {
        "platforms": len(platforms),
        "total_variations": total_variants,
    }

    if args.format == "json":
        output = json.dumps(results, indent=2)
    else:
        lines = [f"Ad Copy Generated: {results['generated_at']}", ""]
        for ad_set in results["ads"]:
            lines.append(f"=== {ad_set['platform'].upper()} ({ad_set['ad_type']}) ===")
            for var in ad_set["variations"]:
                lines.append(f"\n--- Variant {var['variant']} ---")
                for key, val in var.items():
                    if key in ("variant", "within_limits"):
                        continue
                    if isinstance(val, list):
                        for i, item in enumerate(val, 1):
                            lines.append(f"  {key}[{i}]: {item}")
                    else:
                        lines.append(f"  {key}: {val}")
                status = "PASS" if var["within_limits"] else "OVER LIMIT"
                lines.append(f"  limits_check: {status}")
            lines.append("")
        output = "\n".join(lines)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Output written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
