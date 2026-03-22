#!/usr/bin/env python3
"""
Check ticket text for red flags requiring immediate escalation.

Usage:
    python check_red_flags.py "ticket text here"
    python check_red_flags.py --file ticket.txt

Output: JSON with detected red flags and recommended actions
"""

import argparse
import json
import re
import sys

# Red flag categories and their keywords
RED_FLAGS = {
    "legal": {
        "keywords": [
            "lawyer", "attorney", "lawsuit", "sue", "legal action",
            "breach of contract", "court", "litigation", "subpoena",
            "legal team", "terms of service", "tos violation"
        ],
        "severity": "critical",
        "action": "Escalate to Legal team immediately"
    },
    "regulatory": {
        "keywords": [
            "gdpr", "hipaa", "ccpa", "compliance", "audit",
            "regulatory", "data protection", "privacy violation",
            "pci", "sox", "ferpa", "coppa"
        ],
        "severity": "critical",
        "action": "Escalate to Compliance team immediately"
    },
    "security": {
        "keywords": [
            "breach", "hacked", "exposed", "vulnerability",
            "unauthorized access", "data leak", "compromised",
            "security incident", "phishing", "malware", "ransomware"
        ],
        "severity": "critical",
        "action": "Escalate to Security team immediately"
    },
    "churn_risk": {
        "keywords": [
            "cancel", "canceling", "cancellation", "switching to",
            "competitor", "leaving", "not renewing", "looking elsewhere",
            "alternative", "replacement", "moving away"
        ],
        "severity": "high",
        "action": "Route to Customer Success for retention"
    },
    "executive_escalation": {
        "keywords": [
            "ceo", "cto", "cfo", "vp", "director", "board",
            "executive", "management", "leadership", "escalate"
        ],
        "severity": "high",
        "action": "Notify management and prioritize"
    },
    "public_threat": {
        "keywords": [
            "twitter", "social media", "review", "public",
            "tell everyone", "post about", "blog", "news",
            "journalist", "media", "facebook", "linkedin"
        ],
        "severity": "high",
        "action": "Alert PR/Communications and prioritize resolution"
    },
    "repeated_contact": {
        "patterns": [
            r"(third|3rd|fourth|4th|fifth|5th) time",
            r"already (contacted|emailed|called|reached out)",
            r"been waiting (for )?(days|weeks)",
            r"no response",
            r"follow(ing)? up again",
            r"still (waiting|no|haven't)"
        ],
        "severity": "high",
        "action": "Check ticket history and escalate if pattern confirmed"
    },
    "frustration": {
        "keywords": [
            "unacceptable", "ridiculous", "outrageous", "terrible",
            "worst", "incompetent", "useless", "pathetic", "furious"
        ],
        "severity": "medium",
        "action": "Handle with extra care, consider senior agent"
    }
}


def check_keywords(text: str, keywords: list) -> list:
    """Check for keyword matches in text."""
    text_lower = text.lower()
    return [kw for kw in keywords if kw in text_lower]


def check_patterns(text: str, patterns: list) -> list:
    """Check for regex pattern matches in text."""
    text_lower = text.lower()
    matches = []
    for pattern in patterns:
        if re.search(pattern, text_lower):
            matches.append(pattern)
    return matches


def detect_red_flags(text: str) -> dict:
    """Detect all red flags in ticket text."""
    detected = []

    for flag_name, flag_data in RED_FLAGS.items():
        matches = []

        if "keywords" in flag_data:
            matches = check_keywords(text, flag_data["keywords"])
        elif "patterns" in flag_data:
            matches = check_patterns(text, flag_data["patterns"])

        if matches:
            detected.append({
                "flag": flag_name,
                "severity": flag_data["severity"],
                "action": flag_data["action"],
                "matches": matches[:5]  # Limit matches shown
            })

    # Sort by severity
    severity_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    detected.sort(key=lambda x: severity_order.get(x["severity"], 4))

    # Determine overall severity
    if detected:
        overall_severity = detected[0]["severity"]
    else:
        overall_severity = "none"

    return {
        "has_red_flags": len(detected) > 0,
        "overall_severity": overall_severity,
        "flags_detected": len(detected),
        "flags": detected,
        "immediate_escalation_required": overall_severity == "critical"
    }


def main():
    parser = argparse.ArgumentParser(description="Check for red flags in ticket")
    parser.add_argument("text", nargs="?", help="Ticket text to check")
    parser.add_argument("--file", "-f", help="Read text from file")
    parser.add_argument("--stdin", action="store_true", help="Read from stdin")
    parser.add_argument("--pretty", "-p", action="store_true", help="Pretty print")

    args = parser.parse_args()

    # Get input text
    if args.stdin:
        text = sys.stdin.read()
    elif args.file:
        with open(args.file, 'r') as f:
            text = f.read()
    elif args.text:
        text = args.text
    else:
        parser.print_help()
        sys.exit(1)

    # Check for red flags
    result = detect_red_flags(text)

    # Output
    if args.pretty:
        print(json.dumps(result, indent=2))
    else:
        print(json.dumps(result))

    # Exit with code 1 if critical flags detected
    if result["immediate_escalation_required"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
