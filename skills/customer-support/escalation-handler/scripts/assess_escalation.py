#!/usr/bin/env python3
"""
Assess escalation severity and recommend approach.

Usage:
    python assess_escalation.py "ticket text here"
    python assess_escalation.py --file ticket.txt

Output: JSON with escalation level, risk factors, recommended approach
"""

import argparse
import json
import re
import sys

# Escalation level indicators
LEVEL_INDICATORS = {
    "level_3_critical": {
        "keywords": [
            "lawyer", "attorney", "lawsuit", "sue", "legal",
            "court", "litigation", "breach of contract",
            "gdpr", "hipaa", "ccpa", "compliance", "regulatory",
            "ceo", "cto", "board", "executive", "leadership",
            "twitter", "social media", "public", "press", "journalist",
            "bbb", "ftc", "complaint filed"
        ],
        "weight": 3
    },
    "level_2_angry": {
        "keywords": [
            "unacceptable", "ridiculous", "outrageous", "terrible",
            "worst", "incompetent", "useless", "furious", "angry",
            "cancel", "switching", "leaving", "refund", "demand",
            "manager", "supervisor", "escalate", "higher up",
            "been waiting", "no response", "third time", "again"
        ],
        "weight": 2
    },
    "level_1_frustrated": {
        "keywords": [
            "frustrated", "disappointed", "annoying", "confusing",
            "difficult", "unhappy", "not happy", "expected better",
            "issue", "problem", "still", "yet"
        ],
        "weight": 1
    }
}

# Risk factors
RISK_FACTORS = {
    "churn_risk": [
        "cancel", "canceling", "leave", "leaving", "switch",
        "competitor", "alternative", "looking elsewhere"
    ],
    "reputation_risk": [
        "twitter", "social media", "review", "public",
        "tell everyone", "warn others", "blog", "post"
    ],
    "legal_risk": [
        "lawyer", "attorney", "legal", "sue", "lawsuit",
        "court", "damages", "liability"
    ],
    "compliance_risk": [
        "gdpr", "hipaa", "ccpa", "pci", "compliance",
        "audit", "regulatory", "data protection"
    ],
    "financial_risk": [
        "refund", "compensation", "money back", "billing",
        "charged", "fraud", "unauthorized"
    ]
}

# Emotional intensity indicators
INTENSITY_SIGNALS = {
    "all_caps_ratio": 0.2,  # Threshold for concerning ALL CAPS
    "exclamation_threshold": 3,  # Number of ! indicating high emotion
    "question_marks_threshold": 3  # Excessive ? indicates frustration
}


def calculate_emotional_intensity(text: str) -> dict:
    """Calculate emotional intensity from text patterns."""
    # ALL CAPS ratio
    caps_chars = sum(1 for c in text if c.isupper())
    total_chars = sum(1 for c in text if c.isalpha())
    caps_ratio = caps_chars / max(total_chars, 1)

    # Punctuation patterns
    exclamation_count = text.count('!')
    question_count = text.count('?')

    # Repeated punctuation (!!!  or ???)
    repeated_punct = len(re.findall(r'[!?]{2,}', text))

    # Calculate intensity score (0-10)
    intensity = 0
    if caps_ratio > INTENSITY_SIGNALS["all_caps_ratio"]:
        intensity += 3
    if exclamation_count > INTENSITY_SIGNALS["exclamation_threshold"]:
        intensity += 2
    if question_count > INTENSITY_SIGNALS["question_marks_threshold"]:
        intensity += 1
    if repeated_punct > 0:
        intensity += 2

    # Word count can indicate venting
    word_count = len(text.split())
    if word_count > 300:  # Long message often indicates venting
        intensity += 1

    return {
        "score": min(intensity, 10),
        "caps_ratio": round(caps_ratio, 2),
        "exclamation_marks": exclamation_count,
        "question_marks": question_count,
        "is_venting": word_count > 300
    }


def detect_escalation_level(text: str) -> dict:
    """Detect escalation level based on keywords."""
    text_lower = text.lower()

    for level, data in LEVEL_INDICATORS.items():
        matches = [kw for kw in data["keywords"] if kw in text_lower]
        if matches:
            return {
                "level": level,
                "weight": data["weight"],
                "triggers": matches[:5]
            }

    return {
        "level": "level_0_normal",
        "weight": 0,
        "triggers": []
    }


def assess_risks(text: str) -> list:
    """Identify specific risk factors."""
    text_lower = text.lower()
    risks = []

    for risk_type, keywords in RISK_FACTORS.items():
        matches = [kw for kw in keywords if kw in text_lower]
        if matches:
            risks.append({
                "type": risk_type,
                "indicators": matches
            })

    return risks


def get_recommended_approach(level: str, risks: list, intensity: int) -> dict:
    """Generate recommended approach based on assessment."""

    approaches = {
        "level_3_critical": {
            "response_time": "Immediate",
            "handler": "Manager + Legal notification",
            "tone": "White-glove, formal",
            "actions": [
                "Notify management immediately",
                "Alert legal/compliance if applicable",
                "Prepare executive summary",
                "Single senior point of contact"
            ],
            "avoid": [
                "Admitting fault or liability",
                "Making promises without approval",
                "Discussing specifics in writing"
            ]
        },
        "level_2_angry": {
            "response_time": "Within 2 hours",
            "handler": "Senior agent or Team Lead",
            "tone": "Calm, empathetic, solution-focused",
            "actions": [
                "Let customer vent completely",
                "Acknowledge specific frustrations",
                "Propose concrete resolution",
                "Schedule follow-up"
            ],
            "avoid": [
                "Being defensive",
                "Blaming other teams",
                "Generic responses"
            ]
        },
        "level_1_frustrated": {
            "response_time": "Within 4 hours",
            "handler": "Experienced Tier 1 or Tier 2",
            "tone": "Understanding, helpful",
            "actions": [
                "Acknowledge the inconvenience",
                "Provide clear next steps",
                "Offer direct contact for follow-up"
            ],
            "avoid": [
                "Dismissing concerns",
                "Template responses"
            ]
        },
        "level_0_normal": {
            "response_time": "Standard SLA",
            "handler": "Standard routing",
            "tone": "Friendly, professional",
            "actions": [
                "Standard resolution process"
            ],
            "avoid": []
        }
    }

    approach = approaches.get(level, approaches["level_0_normal"]).copy()

    # Adjust for high intensity
    if intensity > 7:
        approach["additional_notes"] = [
            "High emotional intensity detected",
            "Allow extra time for customer to express concerns",
            "Use active listening techniques"
        ]

    # Add risk-specific guidance
    if risks:
        risk_notes = []
        for risk in risks:
            if risk["type"] == "churn_risk":
                risk_notes.append("Consider retention offer")
            if risk["type"] == "reputation_risk":
                risk_notes.append("Prioritize resolution to prevent public complaint")
            if risk["type"] == "legal_risk":
                risk_notes.append("Do not discuss specifics; escalate to legal")
        if risk_notes:
            approach["risk_notes"] = risk_notes

    return approach


def assess_escalation(text: str) -> dict:
    """Main assessment function."""
    level_result = detect_escalation_level(text)
    risks = assess_risks(text)
    intensity = calculate_emotional_intensity(text)

    # Get level number for easy comparison
    level_num = level_result["weight"]

    # Intensity can bump level up
    if intensity["score"] >= 7 and level_num < 2:
        level_result["level"] = "level_2_angry"
        level_result["weight"] = 2
        level_result["intensity_upgrade"] = True

    approach = get_recommended_approach(
        level_result["level"],
        risks,
        intensity["score"]
    )

    return {
        "escalation_level": level_result["level"],
        "severity_score": level_result["weight"],
        "triggers": level_result["triggers"],
        "emotional_intensity": intensity,
        "risk_factors": risks,
        "recommended_approach": approach,
        "requires_manager": level_result["weight"] >= 2,
        "requires_legal": any(r["type"] in ["legal_risk", "compliance_risk"] for r in risks)
    }


def main():
    parser = argparse.ArgumentParser(description="Assess escalation severity")
    parser.add_argument("text", nargs="?", help="Ticket text to assess")
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

    # Assess
    result = assess_escalation(text)

    # Output
    if args.pretty:
        print(json.dumps(result, indent=2))
    else:
        print(json.dumps(result))

    # Exit with level code
    sys.exit(result["severity_score"])


if __name__ == "__main__":
    main()
