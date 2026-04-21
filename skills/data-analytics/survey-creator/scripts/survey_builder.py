#!/usr/bin/env python3
"""Build a survey skeleton based on type, question count, and objectives.

Usage:
    python survey_builder.py --type customer-feedback --questions 10
    python survey_builder.py --type employee-engagement --output survey.json
    python survey_builder.py --type market-research --questions 15 --output survey.json
"""

import argparse
import json
import sys
from datetime import datetime

SURVEY_TYPES = {
    "customer-feedback": {
        "name": "Customer Feedback Survey",
        "purpose": "Measure customer satisfaction and gather improvement suggestions",
        "recommended_questions": 8,
        "estimated_time": "3-4 minutes",
        "key_metrics": ["CSAT", "NPS"],
        "sections": [
            {
                "name": "Overall Satisfaction",
                "questions": [
                    {"id": "Q1", "text": "Overall, how satisfied are you with [PRODUCT/SERVICE]?", "type": "likert_5", "required": True},
                    {"id": "Q2", "text": "How likely are you to recommend [PRODUCT/SERVICE] to a friend or colleague?", "type": "nps", "required": True},
                ],
            },
            {
                "name": "Experience Details",
                "questions": [
                    {"id": "Q3", "text": "Which best describes your primary use of [PRODUCT/SERVICE]?", "type": "multiple_choice", "required": True},
                    {"id": "Q4", "text": "How long have you been using [PRODUCT/SERVICE]?", "type": "multiple_choice", "required": True},
                    {"id": "Q5", "text": "Please rate the following aspects:", "type": "matrix", "required": True, "items": ["Ease of use", "Value for money", "Reliability", "Customer support"]},
                ],
            },
            {
                "name": "Open Feedback",
                "questions": [
                    {"id": "Q6", "text": "What is the one thing we could do to improve your experience?", "type": "open_ended", "required": False},
                    {"id": "Q7", "text": "What do you value most about [PRODUCT/SERVICE]?", "type": "open_ended", "required": False},
                    {"id": "Q8", "text": "Any additional comments?", "type": "open_ended", "required": False},
                ],
            },
        ],
    },
    "employee-engagement": {
        "name": "Employee Engagement Survey",
        "purpose": "Measure employee satisfaction, motivation, and workplace culture",
        "recommended_questions": 20,
        "estimated_time": "8-10 minutes",
        "key_metrics": ["Engagement Index", "eNPS"],
        "sections": [
            {
                "name": "Engagement and Motivation",
                "questions": [
                    {"id": "Q1", "text": "I am proud to work at [COMPANY].", "type": "likert_5", "required": True},
                    {"id": "Q2", "text": "I would recommend [COMPANY] as a great place to work.", "type": "likert_5", "required": True},
                    {"id": "Q3", "text": "I see myself working here in two years.", "type": "likert_5", "required": True},
                    {"id": "Q4", "text": "I feel motivated to go beyond what is expected.", "type": "likert_5", "required": True},
                ],
            },
            {
                "name": "Management and Leadership",
                "questions": [
                    {"id": "Q5", "text": "My manager provides clear expectations.", "type": "likert_5", "required": True},
                    {"id": "Q6", "text": "I receive regular, useful feedback.", "type": "likert_5", "required": True},
                    {"id": "Q7", "text": "My manager cares about my well-being.", "type": "likert_5", "required": True},
                    {"id": "Q8", "text": "Leadership communicates a clear vision.", "type": "likert_5", "required": True},
                ],
            },
            {
                "name": "Growth and Development",
                "questions": [
                    {"id": "Q9", "text": "I have opportunities to learn and grow.", "type": "likert_5", "required": True},
                    {"id": "Q10", "text": "My career development is supported.", "type": "likert_5", "required": True},
                ],
            },
            {
                "name": "Open Feedback",
                "questions": [
                    {"id": "Q11", "text": "What is the best thing about working here?", "type": "open_ended", "required": False},
                    {"id": "Q12", "text": "What is one thing you would change?", "type": "open_ended", "required": False},
                ],
            },
        ],
    },
    "market-research": {
        "name": "Market Research Survey",
        "purpose": "Understand market awareness, preferences, and purchase behavior",
        "recommended_questions": 12,
        "estimated_time": "5-6 minutes",
        "key_metrics": ["Brand Awareness", "Purchase Intent", "Price Sensitivity"],
        "sections": [
            {
                "name": "Awareness and Usage",
                "questions": [
                    {"id": "Q1", "text": "Which brands are you aware of? (Select all)", "type": "multi_select", "required": True},
                    {"id": "Q2", "text": "Which brand do you use most often?", "type": "multiple_choice", "required": True},
                    {"id": "Q3", "text": "How often do you use [PRODUCT CATEGORY]?", "type": "multiple_choice", "required": True},
                ],
            },
            {
                "name": "Purchase Drivers",
                "questions": [
                    {"id": "Q4", "text": "Rank the following factors by importance:", "type": "ranking", "required": True, "items": ["Price", "Quality", "Brand", "Features", "Support"]},
                    {"id": "Q5", "text": "What is your typical budget?", "type": "multiple_choice", "required": True},
                ],
            },
            {
                "name": "Concept Testing",
                "questions": [
                    {"id": "Q6", "text": "How interested would you be in this product?", "type": "likert_5", "required": True},
                    {"id": "Q7", "text": "What price would you expect to pay?", "type": "open_ended", "required": True},
                ],
            },
            {
                "name": "Demographics",
                "questions": [
                    {"id": "Q8", "text": "What is your age range?", "type": "multiple_choice", "required": False},
                    {"id": "Q9", "text": "What is your role?", "type": "multiple_choice", "required": False},
                ],
            },
        ],
    },
}


def build_survey(survey_type, max_questions=None):
    """Build a survey skeleton."""
    template = SURVEY_TYPES.get(survey_type, SURVEY_TYPES["customer-feedback"])

    survey = {
        "metadata": {
            "type": template["name"],
            "purpose": template["purpose"],
            "estimated_time": template["estimated_time"],
            "key_metrics": template["key_metrics"],
            "generated_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "DRAFT",
        },
        "settings": {
            "anonymous": survey_type == "employee-engagement",
            "randomize_options": True,
            "show_progress_bar": True,
            "allow_back_navigation": True,
            "mobile_optimized": True,
        },
        "sections": template["sections"],
        "total_questions": sum(len(s["questions"]) for s in template["sections"]),
        "bias_checklist": [
            "No leading questions (check for loaded language)",
            "No double-barreled questions (one concept per question)",
            "Balanced scales (equal positive and negative options)",
            "Specific time periods stated",
            "Randomized option order where applicable",
            "Prefer not to answer option for sensitive questions",
        ],
        "distribution_plan": {
            "channel": "[Email / In-app / Link]",
            "send_date": "[DATE]",
            "reminder_1": "[DATE + 3 days]",
            "reminder_2": "[DATE + 6 days]",
            "close_date": "[DATE + 10 days]",
            "target_responses": "[NUMBER]",
        },
    }

    if max_questions:
        survey["metadata"]["note"] = f"Requested {max_questions} questions; template has {survey['total_questions']}. Adjust sections as needed."

    return survey


def main():
    parser = argparse.ArgumentParser(
        description="Build a survey skeleton based on type and configuration."
    )
    parser.add_argument(
        "--type",
        choices=list(SURVEY_TYPES.keys()),
        default="customer-feedback",
        help="Survey type (default: customer-feedback)",
    )
    parser.add_argument(
        "--questions",
        type=int,
        help="Target number of questions",
    )
    parser.add_argument(
        "--output",
        help="Output file path (default: stdout)",
    )

    args = parser.parse_args()
    survey = build_survey(survey_type=args.type, max_questions=args.questions)
    output = json.dumps(survey, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Survey skeleton written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
