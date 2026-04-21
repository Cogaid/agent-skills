#!/usr/bin/env python3
"""Generate survey configuration from parameters.

Usage:
    python scripts/design_survey.py --type csat --channel email --questions 5
    python scripts/design_survey.py --type nps --channel email --questions 3
    python scripts/design_survey.py --type ces --channel in-app --questions 2
"""

import argparse
import json
import sys
from datetime import datetime, timedelta

SURVEY_TYPES = {
    "csat": {
        "name": "Customer Satisfaction Score",
        "scale": {"min": 1, "max": 5, "labels": {
            "1": "Very Dissatisfied",
            "2": "Dissatisfied",
            "3": "Neutral",
            "4": "Satisfied",
            "5": "Very Satisfied",
        }},
        "primary_question": "How satisfied were you with the support you received today?",
        "follow_up_negative": "We're sorry to hear that. What could we have done better?",
        "follow_up_positive": "Great to hear! What did you appreciate most?",
        "threshold_negative": 3,
    },
    "nps": {
        "name": "Net Promoter Score",
        "scale": {"min": 0, "max": 10, "labels": {
            "0": "Not at all likely",
            "10": "Extremely likely",
        }},
        "primary_question": "How likely are you to recommend us to a friend or colleague?",
        "follow_up_detractor": "What is the primary reason for your score?",
        "follow_up_passive": "What would we need to do to earn a higher score?",
        "follow_up_promoter": "What do you value most about us?",
        "segments": {
            "detractor": [0, 6],
            "passive": [7, 8],
            "promoter": [9, 10],
        },
    },
    "ces": {
        "name": "Customer Effort Score",
        "scale": {"min": 1, "max": 7, "labels": {
            "1": "Strongly Disagree",
            "4": "Neither Agree nor Disagree",
            "7": "Strongly Agree",
        }},
        "primary_question": "To what extent do you agree: [Company] made it easy to handle my issue.",
        "follow_up_negative": "What made this process difficult?",
        "threshold_negative": 3,
    },
}

CHANNEL_DEFAULTS = {
    "email": {"delay_minutes": 120, "expiry_days": 7, "max_questions": 5},
    "in-app": {"delay_minutes": 0, "expiry_days": 1, "max_questions": 3},
    "post-chat": {"delay_minutes": 0, "expiry_days": 1, "max_questions": 3},
    "sms": {"delay_minutes": 60, "expiry_days": 3, "max_questions": 2},
    "ivr": {"delay_minutes": 60, "expiry_days": 1, "max_questions": 2},
}

OPTIONAL_QUESTIONS = [
    {
        "id": "effort_rating",
        "question": "How easy was it to get your issue resolved?",
        "type": "rating",
        "scale": {"min": 1, "max": 5, "labels": {"1": "Very Difficult", "5": "Very Easy"}},
    },
    {
        "id": "resolution_check",
        "question": "Was your issue fully resolved?",
        "type": "single_choice",
        "options": ["Yes", "Partially", "No"],
    },
    {
        "id": "agent_rating",
        "question": "How would you rate the agent who assisted you?",
        "type": "rating",
        "scale": {"min": 1, "max": 5, "labels": {"1": "Poor", "5": "Excellent"}},
    },
    {
        "id": "improvement_area",
        "question": "Which area matters most to you?",
        "type": "single_choice",
        "options": ["Product quality", "Customer support", "Pricing", "Ease of use", "Reliability", "Other"],
    },
]


def build_questions(survey_type_key, num_questions):
    """Build question list based on survey type and requested count."""
    survey_type = SURVEY_TYPES[survey_type_key]
    questions = []

    # Q1: Primary rating question (always included)
    questions.append({
        "id": "q1_primary",
        "question": survey_type["primary_question"],
        "type": "rating",
        "required": True,
        "scale": survey_type["scale"],
    })

    # Q2: Conditional follow-up (always included)
    if survey_type_key == "nps":
        questions.append({
            "id": "q2_followup",
            "question": "(Segment-dependent follow-up)",
            "type": "open_text",
            "required": True,
            "conditional": True,
            "branches": {
                "detractor": survey_type["follow_up_detractor"],
                "passive": survey_type["follow_up_passive"],
                "promoter": survey_type["follow_up_promoter"],
            },
            "character_limit": 1000,
        })
    else:
        questions.append({
            "id": "q2_followup",
            "question": survey_type.get("follow_up_negative", "What could we improve?"),
            "type": "open_text",
            "required": False,
            "conditional": True,
            "show_when": f"q1_primary <= {survey_type.get('threshold_negative', 3)}",
            "character_limit": 500,
        })

    # Add optional questions up to the requested count
    remaining = num_questions - len(questions)
    for i, opt_q in enumerate(OPTIONAL_QUESTIONS):
        if remaining <= 0:
            break
        questions.append({**opt_q, "id": f"q{len(questions) + 1}_{opt_q['id']}", "required": False})
        remaining -= 1

    return questions


def generate_survey_config(survey_type_key, channel, num_questions):
    """Generate complete survey configuration."""
    survey_type = SURVEY_TYPES[survey_type_key]
    channel_config = CHANNEL_DEFAULTS.get(channel, CHANNEL_DEFAULTS["email"])

    effective_questions = min(num_questions, channel_config["max_questions"])
    if effective_questions < num_questions:
        print(
            f"Note: {channel} channel supports max {channel_config['max_questions']} questions. "
            f"Adjusted from {num_questions} to {effective_questions}.",
            file=sys.stderr,
        )

    now = datetime.utcnow()
    questions = build_questions(survey_type_key, effective_questions)

    config = {
        "survey": {
            "id": f"SRV-{survey_type_key.upper()}-{now.strftime('%Y%m%d%H%M%S')}",
            "type": survey_type_key.upper(),
            "name": f"{survey_type['name']} Survey",
            "created_at": now.isoformat() + "Z",
            "status": "draft",
        },
        "delivery": {
            "channel": channel,
            "delay_minutes": channel_config["delay_minutes"],
            "expiry": (now + timedelta(days=channel_config["expiry_days"])).isoformat() + "Z",
            "frequency_cap_days": 30,
            "reminder": channel == "email",
            "reminder_delay_days": 7 if channel == "email" else None,
        },
        "questions": questions,
        "close_messages": {
            "default": "Thank you for your feedback! It helps us improve.",
            "low_score": "Thank you for your honesty. A team member may follow up on your experience.",
            "high_score": "Thank you! We're glad we could help.",
        },
        "alerts": [
            {"condition": "q1_primary <= 2", "action": "notify_team_lead", "priority": "high"},
            {"condition": "response_rate < 10%", "action": "notify_survey_ops", "priority": "medium"},
        ],
        "metadata": {
            "question_count": len(questions),
            "estimated_completion_seconds": len(questions) * 20,
            "target_response_rate": "20%",
        },
    }

    return config


def main():
    parser = argparse.ArgumentParser(
        description="Generate survey configuration from parameters"
    )
    parser.add_argument(
        "--type",
        choices=["csat", "nps", "ces"],
        required=True,
        help="Survey type: csat, nps, or ces",
    )
    parser.add_argument(
        "--channel",
        choices=["email", "in-app", "post-chat", "sms", "ivr"],
        default="email",
        help="Delivery channel (default: email)",
    )
    parser.add_argument(
        "--questions",
        type=int,
        default=3,
        help="Number of questions (default: 3, max varies by channel)",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        default=True,
        help="Pretty-print JSON output (default: True)",
    )

    args = parser.parse_args()

    config = generate_survey_config(args.type, args.channel, args.questions)
    indent = 2 if args.pretty else None
    print(json.dumps(config, indent=indent))


if __name__ == "__main__":
    main()
