#!/usr/bin/env python3
"""
Ad Copy Validator -- Check ad copy against platform character limits and policies.

Usage:
    python ad_validator.py --platform google --headlines "Save 50% on CRM" "Free Trial Available" "Trusted by 10K+"
    python ad_validator.py --platform facebook --primary-text "Try our tool today" --headline "Save More"
    python ad_validator.py --file ads.json
"""

import argparse
import json
import sys
from datetime import datetime

PLATFORM_LIMITS = {
    "google": {
        "headline": {"limit": 30, "min_count": 3, "max_count": 15},
        "description": {"limit": 90, "min_count": 2, "max_count": 4},
        "display_path": {"limit": 15, "max_count": 2},
    },
    "facebook": {
        "primary_text": {"limit": 125, "note": "Visible limit; 63206 max"},
        "headline": {"limit": 27, "note": "Visible on most placements"},
        "description": {"limit": 27},
    },
    "linkedin": {
        "intro_text": {"limit": 150, "note": "Visible limit; 600 max"},
        "headline": {"limit": 70, "note": "Visible limit; 200 max"},
    },
    "twitter": {
        "tweet": {"limit": 280},
    },
}

POLICY_CHECKS = {
    "excessive_caps": {
        "description": "Excessive capitalization (all caps words)",
        "platforms": ["google", "linkedin"],
    },
    "excessive_punctuation": {
        "description": "Repeated punctuation marks (!! or ??)",
        "platforms": ["google", "facebook", "linkedin"],
    },
    "phone_number": {
        "description": "Phone number in ad text (use extensions instead)",
        "platforms": ["google"],
    },
    "emoji_overuse": {
        "description": "More than 3 emojis in ad copy",
        "platforms": ["linkedin", "google"],
    },
}


def check_char_limits(text, limit, field_name):
    """Check if text is within character limit."""
    char_count = len(text)
    over_by = max(0, char_count - limit)
    return {
        "field": field_name,
        "text": text,
        "char_count": char_count,
        "limit": limit,
        "status": "PASS" if char_count <= limit else "FAIL",
        "over_by": over_by,
    }


def check_excessive_caps(text):
    """Check for excessive capitalization."""
    words = text.split()
    caps_words = [w for w in words if w.isupper() and len(w) > 2]
    ratio = len(caps_words) / max(len(words), 1)
    return {
        "check": "excessive_caps",
        "status": "WARN" if ratio > 0.3 else "PASS",
        "detail": f"{len(caps_words)} all-caps words out of {len(words)}",
        "caps_words": caps_words,
    }


def check_excessive_punctuation(text):
    """Check for repeated punctuation."""
    import re

    matches = re.findall(r"[!?]{2,}", text)
    return {
        "check": "excessive_punctuation",
        "status": "WARN" if matches else "PASS",
        "detail": f"Found: {matches}" if matches else "No repeated punctuation",
    }


def check_phone_number(text):
    """Check for phone numbers in text."""
    import re

    phone_pattern = r"[\+]?[(]?[0-9]{1,4}[)]?[-\s\./0-9]{7,}"
    matches = re.findall(phone_pattern, text)
    return {
        "check": "phone_number",
        "status": "WARN" if matches else "PASS",
        "detail": f"Found phone numbers: {matches}"
        if matches
        else "No phone numbers found",
    }


def check_emoji_count(text):
    """Check for emoji overuse."""
    import re

    emoji_pattern = re.compile(
        "[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF"
        "\U00002702-\U000027B0\U000024C2-\U0001F251]+",
        flags=re.UNICODE,
    )
    emojis = emoji_pattern.findall(text)
    total = sum(len(e) for e in emojis)
    return {
        "check": "emoji_overuse",
        "status": "WARN" if total > 3 else "PASS",
        "detail": f"{total} emojis found",
    }


def validate_google(args):
    """Validate Google Ads copy."""
    results = {"platform": "google", "checks": [], "policy_checks": []}
    limits = PLATFORM_LIMITS["google"]

    if args.headlines:
        for i, h in enumerate(args.headlines, 1):
            results["checks"].append(
                check_char_limits(h, limits["headline"]["limit"], f"headline_{i}")
            )
        if len(args.headlines) < limits["headline"]["min_count"]:
            results["checks"].append(
                {
                    "field": "headline_count",
                    "status": "FAIL",
                    "detail": f"Need at least {limits['headline']['min_count']} headlines, got {len(args.headlines)}",
                }
            )

    if args.descriptions:
        for i, d in enumerate(args.descriptions, 1):
            results["checks"].append(
                check_char_limits(
                    d, limits["description"]["limit"], f"description_{i}"
                )
            )

    all_text = " ".join(args.headlines or []) + " " + " ".join(args.descriptions or [])
    results["policy_checks"].append(check_excessive_caps(all_text))
    results["policy_checks"].append(check_excessive_punctuation(all_text))
    results["policy_checks"].append(check_phone_number(all_text))

    return results


def validate_facebook(args):
    """Validate Facebook/Meta ads copy."""
    results = {"platform": "facebook", "checks": [], "policy_checks": []}
    limits = PLATFORM_LIMITS["facebook"]

    if args.primary_text:
        results["checks"].append(
            check_char_limits(
                args.primary_text,
                limits["primary_text"]["limit"],
                "primary_text",
            )
        )

    if args.headline:
        results["checks"].append(
            check_char_limits(
                args.headline, limits["headline"]["limit"], "headline"
            )
        )

    if args.description:
        results["checks"].append(
            check_char_limits(
                args.description,
                limits["description"]["limit"],
                "description",
            )
        )

    all_text = " ".join(
        filter(None, [args.primary_text, args.headline, args.description])
    )
    results["policy_checks"].append(check_excessive_punctuation(all_text))
    results["policy_checks"].append(check_emoji_count(all_text))

    return results


def validate_linkedin(args):
    """Validate LinkedIn ads copy."""
    results = {"platform": "linkedin", "checks": [], "policy_checks": []}
    limits = PLATFORM_LIMITS["linkedin"]

    if args.primary_text:
        results["checks"].append(
            check_char_limits(
                args.primary_text, limits["intro_text"]["limit"], "intro_text"
            )
        )

    if args.headline:
        results["checks"].append(
            check_char_limits(
                args.headline, limits["headline"]["limit"], "headline"
            )
        )

    all_text = " ".join(filter(None, [args.primary_text, args.headline]))
    results["policy_checks"].append(check_excessive_caps(all_text))
    results["policy_checks"].append(check_emoji_count(all_text))

    return results


def validate_twitter(args):
    """Validate Twitter/X ads copy."""
    results = {"platform": "twitter", "checks": [], "policy_checks": []}
    limits = PLATFORM_LIMITS["twitter"]

    if args.primary_text:
        results["checks"].append(
            check_char_limits(
                args.primary_text, limits["tweet"]["limit"], "tweet"
            )
        )

    return results


def validate_from_file(filepath):
    """Validate ads from a JSON file."""
    with open(filepath) as f:
        data = json.load(f)

    all_results = []
    for ad in data.get("ads", [data]):
        platform = ad.get("platform", "unknown")
        for var in ad.get("variations", [ad]):
            result = {
                "platform": platform,
                "variant": var.get("variant", 1),
                "checks": [],
            }
            limits = PLATFORM_LIMITS.get(platform.split("_")[0], {})

            for field, spec in limits.items():
                text = var.get(field) or var.get(f"{field}s", [None])[0]
                if text and isinstance(text, str):
                    result["checks"].append(
                        check_char_limits(text, spec["limit"], field)
                    )
                elif isinstance(var.get(f"{field}s"), list):
                    for i, t in enumerate(var[f"{field}s"], 1):
                        result["checks"].append(
                            check_char_limits(t, spec["limit"], f"{field}_{i}")
                        )

            all_results.append(result)

    return all_results


def summarize(results):
    """Create a summary of validation results."""
    if isinstance(results, list):
        all_checks = [c for r in results for c in r.get("checks", [])]
        all_policy = [c for r in results for c in r.get("policy_checks", [])]
    else:
        all_checks = results.get("checks", [])
        all_policy = results.get("policy_checks", [])

    total = len(all_checks) + len(all_policy)
    passed = sum(1 for c in all_checks + all_policy if c.get("status") == "PASS")
    failed = sum(1 for c in all_checks if c.get("status") == "FAIL")
    warnings = sum(1 for c in all_policy if c.get("status") == "WARN")

    return {
        "total_checks": total,
        "passed": passed,
        "failed": failed,
        "warnings": warnings,
        "overall": "FAIL" if failed > 0 else ("WARN" if warnings > 0 else "PASS"),
    }


def main():
    parser = argparse.ArgumentParser(
        description="Validate ad copy against platform limits and policies",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --platform google --headlines "Save 50%%" "Free Trial" "Trusted by 10K+"
  %(prog)s --platform facebook --primary-text "Try today" --headline "Save More"
  %(prog)s --file ads.json
        """,
    )
    parser.add_argument(
        "--platform",
        choices=["google", "facebook", "linkedin", "twitter"],
        help="Platform to validate against",
    )
    parser.add_argument("--headlines", nargs="+", help="Headline texts (Google Ads)")
    parser.add_argument(
        "--descriptions", nargs="+", help="Description texts (Google Ads)"
    )
    parser.add_argument("--primary-text", help="Primary text / intro text")
    parser.add_argument("--headline", help="Single headline text")
    parser.add_argument("--description", help="Single description text")
    parser.add_argument("--file", help="JSON file containing ads to validate")
    parser.add_argument("--output", help="Output file path (default: stdout)")

    args = parser.parse_args()

    if args.file:
        results = validate_from_file(args.file)
    elif args.platform == "google":
        results = validate_google(args)
    elif args.platform == "facebook":
        results = validate_facebook(args)
    elif args.platform == "linkedin":
        results = validate_linkedin(args)
    elif args.platform == "twitter":
        results = validate_twitter(args)
    else:
        parser.error("Either --platform or --file is required")
        return

    output = {
        "validated_at": datetime.now().isoformat(),
        "results": results,
        "summary": summarize(results),
    }

    formatted = json.dumps(output, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(formatted)
        print(f"Validation results written to {args.output}", file=sys.stderr)
    else:
        print(formatted)


if __name__ == "__main__":
    main()
