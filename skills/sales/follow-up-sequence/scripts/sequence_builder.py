#!/usr/bin/env python3
"""
Generate customized follow-up sequences for prospects.

Usage:
    python sequence_builder.py --type cold --industry saas
    python sequence_builder.py --type post_meeting --days 7
    python sequence_builder.py --interactive

Output: Complete follow-up sequence with timing and templates
"""

import argparse
import json
from datetime import datetime, timedelta


# Sequence configurations
SEQUENCE_TYPES = {
    "cold": {
        "name": "Cold Outreach",
        "touches": 6,
        "days": [0, 3, 7, 12, 16, 21],
        "channels": ["email", "email", "linkedin", "email", "phone", "email"],
        "goal": "Initial meeting"
    },
    "post_meeting": {
        "name": "Post-Meeting Follow-Up",
        "touches": 4,
        "days": [0, 2, 5, 9],
        "channels": ["email", "email", "email", "email"],
        "goal": "Move to next stage"
    },
    "re_engagement": {
        "name": "Re-Engagement",
        "touches": 4,
        "days": [0, 5, 12, 21],
        "channels": ["email", "email", "email", "email"],
        "goal": "Restart conversation"
    },
    "lost_deal": {
        "name": "Lost Deal Revival",
        "touches": 3,
        "days": [30, 60, 90],
        "channels": ["email", "email", "email"],
        "goal": "Reopen opportunity"
    }
}

# Industry-specific angles
INDUSTRY_ANGLES = {
    "saas": {
        "challenges": ["churn", "ARR growth", "customer acquisition cost", "onboarding"],
        "metrics": ["MRR", "NRR", "LTV:CAC ratio", "time-to-value"],
        "triggers": ["funding round", "new product launch", "IPO prep"]
    },
    "fintech": {
        "challenges": ["compliance", "security", "user trust", "scalability"],
        "metrics": ["AUM", "transaction volume", "compliance score"],
        "triggers": ["regulatory change", "market expansion", "partnership"]
    },
    "healthcare": {
        "challenges": ["patient outcomes", "operational efficiency", "data security"],
        "metrics": ["patient satisfaction", "cost per procedure", "readmission rate"],
        "triggers": ["new facility", "merger", "technology upgrade"]
    },
    "ecommerce": {
        "challenges": ["conversion rate", "cart abandonment", "fulfillment"],
        "metrics": ["AOV", "conversion rate", "customer lifetime value"],
        "triggers": ["peak season prep", "expansion", "platform migration"]
    },
    "default": {
        "challenges": ["growth", "efficiency", "competitive pressure"],
        "metrics": ["revenue", "cost savings", "productivity"],
        "triggers": ["company news", "hiring", "market changes"]
    }
}

# Email templates by touch
EMAIL_TEMPLATES = {
    "cold": {
        1: {
            "subject": "Quick question about {challenge}",
            "body": """Hi {name},

I noticed {company} recently {trigger}.

Companies going through similar {situation} often tell us {challenge_description}.

Curious if that's on your radar?

If so, might be worth a quick chat to share what's worked for similar companies in {industry}.

{signature}"""
        },
        2: {
            "subject": "Re: Quick question about {challenge}",
            "body": """Hi {name},

Following up on my note from earlier this week.

In the meantime, thought you might find this useful:

{resource_link}

Given {company}'s focus on {focus_area}, seemed relevant.

Happy to discuss how this applies to your situation.

{signature}"""
        },
        3: {
            "subject": "Worth 10 minutes?",
            "body": """Hi {name},

Different angle: {similar_company} was dealing with {challenge} when we started working together.

Within {timeframe}, they saw {metric_improvement}.

Would it be valuable to hear how they approached it?

{signature}"""
        },
        4: {
            "subject": "How {similar_company} solved {challenge}",
            "body": """Hi {name},

I know you're busy, so I'll keep this short.

{similar_company} came to us with {challenge}.

Here's what happened:
• {result_1}
• {result_2}
• {result_3}

If any of this sounds relevant to {company}, let's find 15 minutes to explore.

{signature}"""
        },
        5: {
            "subject": "15 minutes this week?",
            "body": """Hi {name},

I've reached out a few times – I get it, priorities.

Here's my simple ask:

15 minutes to discuss whether {challenge} is something {company} is actively working on.

If yes, I'll share exactly how we've helped similar companies and you can decide if it's worth exploring further.

Does {day_option_1} or {day_option_2} work?

{signature}"""
        },
        6: {
            "subject": "Closing the loop",
            "body": """Hi {name},

I've tried reaching you a few times about {topic}.

I'm guessing either:

a) This isn't a priority right now
b) You're the wrong person for this
c) You've been swamped

No hard feelings if any of the above.

I'll assume this isn't a fit and won't keep reaching out.

If anything changes, you know where to find me.

{signature}"""
        }
    },
    "post_meeting": {
        1: {
            "subject": "Great chatting, {name} - next steps",
            "body": """Hi {name},

Really enjoyed our conversation today about {topic}.

Key takeaways from our discussion:
1. {takeaway_1}
2. {takeaway_2}
3. {next_step}

I'll {action} by {date}.

Let me know if any questions come up.

{signature}"""
        },
        2: {
            "subject": "Resource for {challenge}",
            "body": """Hi {name},

Following up on our conversation about {challenge}.

I pulled together {resource_type} that addresses exactly what you mentioned about {specific_situation}.

The section on {section} is most relevant to what {company} is working on.

Happy to walk through it together if useful.

{signature}"""
        },
        3: {
            "subject": "Help for your internal conversation",
            "body": """Hi {name},

As you're discussing {topic} internally, thought this might help:

I've put together a one-pager that covers:
• The problem and impact
• Our approach
• Expected outcomes

Would it help if I joined that conversation? Happy to answer questions directly.

{signature}"""
        },
        4: {
            "subject": "Quick check-in on {topic}",
            "body": """Hi {name},

Wanted to check in on how conversations about {topic} are progressing.

A few things that might help:
• Any questions I can answer for stakeholders?
• Need any additional info for your evaluation?

What's the best next step?

{signature}"""
        }
    }
}


def get_industry_context(industry):
    """Get industry-specific content angles."""
    return INDUSTRY_ANGLES.get(industry, INDUSTRY_ANGLES["default"])


def calculate_send_dates(start_date, days_list):
    """Calculate actual send dates based on day offsets."""
    dates = []
    for day in days_list:
        send_date = start_date + timedelta(days=day)
        # Skip weekends
        while send_date.weekday() >= 5:  # 5=Saturday, 6=Sunday
            send_date += timedelta(days=1)
        dates.append(send_date)
    return dates


def build_sequence(
    sequence_type,
    prospect_info,
    industry="default",
    start_date=None
):
    """Build a complete follow-up sequence."""

    if sequence_type not in SEQUENCE_TYPES:
        return {"error": f"Unknown sequence type: {sequence_type}"}

    config = SEQUENCE_TYPES[sequence_type]
    industry_context = get_industry_context(industry)

    if start_date is None:
        start_date = datetime.now()
    elif isinstance(start_date, str):
        start_date = datetime.fromisoformat(start_date)

    send_dates = calculate_send_dates(start_date, config["days"])

    # Build sequence touches
    touches = []
    templates = EMAIL_TEMPLATES.get(sequence_type, EMAIL_TEMPLATES["cold"])

    for i in range(config["touches"]):
        touch_num = i + 1
        touch = {
            "touch_number": touch_num,
            "day": config["days"][i],
            "send_date": send_dates[i].strftime("%Y-%m-%d"),
            "send_time": "09:00 AM",  # Default optimal time
            "channel": config["channels"][i],
        }

        # Add template if email
        if config["channels"][i] == "email":
            template = templates.get(touch_num, {})
            touch["subject"] = template.get("subject", "Follow-up")
            touch["body"] = template.get("body", "")

            # Fill in prospect info
            for key, value in prospect_info.items():
                touch["subject"] = touch["subject"].replace("{" + key + "}", str(value))
                touch["body"] = touch["body"].replace("{" + key + "}", str(value))

            # Fill in industry context
            touch["body"] = touch["body"].replace(
                "{challenge_description}",
                industry_context["challenges"][0] if industry_context["challenges"] else "challenges"
            )

        elif config["channels"][i] == "phone":
            touch["script"] = generate_call_script(touch_num, prospect_info)

        elif config["channels"][i] == "linkedin":
            touch["message"] = generate_linkedin_message(touch_num, prospect_info)

        touches.append(touch)

    return {
        "sequence_type": sequence_type,
        "sequence_name": config["name"],
        "goal": config["goal"],
        "total_touches": config["touches"],
        "duration_days": config["days"][-1],
        "start_date": start_date.strftime("%Y-%m-%d"),
        "prospect": prospect_info,
        "industry": industry,
        "industry_context": industry_context,
        "touches": touches
    }


def generate_call_script(touch_num, prospect_info):
    """Generate phone call script."""
    name = prospect_info.get("name", "[Name]")
    company = prospect_info.get("company", "[Company]")

    return {
        "opening": f"Hi {name}, this is [Your name] from [Your company]. Do you have a quick moment?",
        "context": f"I've sent you a few emails about [topic] - wanted to connect directly since it can be relevant to what {company} is working on.",
        "value_prop": "We've helped similar companies [achieve result]. Thought it might be worth a quick conversation.",
        "ask": "Would you have 15 minutes this week to explore if there's a fit?",
        "objection_handling": {
            "busy": "Totally understand. When would be a better time to connect?",
            "not_interested": "No problem. Out of curiosity, what's the main reason?",
            "send_info": "Happy to. What specifically would be most useful to see?"
        },
        "voicemail": f"Hi {name}, this is [Your name] from [Your company]. I've sent a few emails about [topic] and wanted to connect briefly. Give me a call back at [number] or reply to my email if it's easier. Talk soon."
    }


def generate_linkedin_message(touch_num, prospect_info):
    """Generate LinkedIn message."""
    name = prospect_info.get("name", "[Name]")
    company = prospect_info.get("company", "[Company]")

    messages = {
        1: f"Hi {name} – I work with companies like {company} helping them [achieve result]. Saw [trigger] and thought we should connect. No pitch, just networking.",
        2: f"Thanks for connecting, {name}! I noticed {company} is [doing something relevant]. We've helped similar companies with [challenge]. Worth a quick chat?",
        3: f"Hi {name} – shared something relevant to your space on my feed. Also curious about [their initiative]. Open to a quick call?"
    }

    return messages.get(touch_num, messages[1])


def export_sequence(sequence, format_type="json"):
    """Export sequence in specified format."""

    if format_type == "json":
        return json.dumps(sequence, indent=2)

    elif format_type == "text":
        lines = []
        lines.append(f"\n{'='*50}")
        lines.append(f"FOLLOW-UP SEQUENCE: {sequence['sequence_name'].upper()}")
        lines.append(f"{'='*50}")
        lines.append(f"\nGoal: {sequence['goal']}")
        lines.append(f"Duration: {sequence['duration_days']} days")
        lines.append(f"Total Touches: {sequence['total_touches']}")
        lines.append(f"\nProspect: {sequence['prospect'].get('name', 'N/A')} @ {sequence['prospect'].get('company', 'N/A')}")

        for touch in sequence['touches']:
            lines.append(f"\n{'-'*40}")
            lines.append(f"TOUCH {touch['touch_number']} - Day {touch['day']} ({touch['send_date']})")
            lines.append(f"Channel: {touch['channel'].upper()}")

            if touch['channel'] == 'email':
                lines.append(f"\nSubject: {touch['subject']}")
                lines.append(f"\n{touch['body']}")
            elif touch['channel'] == 'phone':
                lines.append(f"\nScript: {touch['script']['opening']}")
            elif touch['channel'] == 'linkedin':
                lines.append(f"\nMessage: {touch['message']}")

        return "\n".join(lines)

    elif format_type == "csv":
        lines = ["touch_number,day,send_date,channel,subject"]
        for touch in sequence['touches']:
            subject = touch.get('subject', touch['channel']).replace(',', ';')
            lines.append(f"{touch['touch_number']},{touch['day']},{touch['send_date']},{touch['channel']},\"{subject}\"")
        return "\n".join(lines)

    return json.dumps(sequence, indent=2)


def interactive_mode():
    """Interactive sequence builder."""

    print("\n=== Follow-Up Sequence Builder ===\n")

    # Get sequence type
    print("Sequence Types:")
    for key, config in SEQUENCE_TYPES.items():
        print(f"  {key}: {config['name']} ({config['touches']} touches, {config['days'][-1]} days)")

    seq_type = input("\nSelect sequence type [cold]: ").strip().lower() or "cold"

    # Get prospect info
    print("\n--- Prospect Information ---")
    name = input("Prospect name: ").strip() or "[Name]"
    company = input("Company name: ").strip() or "[Company]"
    title = input("Title: ").strip() or "[Title]"
    challenge = input("Main challenge/pain point: ").strip() or "growth"

    # Get industry
    print("\nIndustries: saas, fintech, healthcare, ecommerce, default")
    industry = input("Industry [default]: ").strip().lower() or "default"

    # Build sequence
    prospect_info = {
        "name": name,
        "company": company,
        "title": title,
        "challenge": challenge,
        "industry": industry,
        "signature": "[Your signature]",
        "topic": challenge,
        "focus_area": challenge
    }

    sequence = build_sequence(seq_type, prospect_info, industry)

    # Display
    print(export_sequence(sequence, "text"))

    # Export option
    if input("\nExport to JSON? (y/n) [n]: ").strip().lower() == "y":
        print(export_sequence(sequence, "json"))


def main():
    parser = argparse.ArgumentParser(description='Build follow-up sequences')
    parser.add_argument('--type', '-t', default='cold',
                        choices=list(SEQUENCE_TYPES.keys()),
                        help='Sequence type')
    parser.add_argument('--name', '-n', help='Prospect name')
    parser.add_argument('--company', '-c', help='Company name')
    parser.add_argument('--industry', '-i', default='default',
                        help='Industry (saas, fintech, healthcare, ecommerce)')
    parser.add_argument('--start', '-s', help='Start date (YYYY-MM-DD)')
    parser.add_argument('--format', '-f', choices=['json', 'text', 'csv'],
                        default='json', help='Output format')
    parser.add_argument('--interactive', action='store_true',
                        help='Interactive mode')
    parser.add_argument('--list', '-l', action='store_true',
                        help='List sequence types')

    args = parser.parse_args()

    if args.list:
        print("\nAvailable Sequence Types:")
        for key, config in SEQUENCE_TYPES.items():
            print(f"\n  {key}:")
            print(f"    Name: {config['name']}")
            print(f"    Touches: {config['touches']}")
            print(f"    Duration: {config['days'][-1]} days")
            print(f"    Channels: {', '.join(config['channels'])}")
            print(f"    Goal: {config['goal']}")
        return

    if args.interactive:
        interactive_mode()
        return

    # Build with provided info
    prospect_info = {
        "name": args.name or "[Name]",
        "company": args.company or "[Company]",
        "challenge": "growth",
        "signature": "[Your signature]",
        "topic": "solution",
        "focus_area": "growth"
    }

    sequence = build_sequence(
        args.type,
        prospect_info,
        args.industry,
        args.start
    )

    print(export_sequence(sequence, args.format))


if __name__ == '__main__':
    main()
