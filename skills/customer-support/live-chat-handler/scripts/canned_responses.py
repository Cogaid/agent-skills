#!/usr/bin/env python3
"""
Get appropriate canned responses for common chat scenarios.

Usage:
    python canned_responses.py --category greeting
    python canned_responses.py --category billing --issue refund
    python canned_responses.py --search "password reset"

Output: Relevant canned response templates
"""

import argparse
import json
import sys


# Canned response library
RESPONSES = {
    "greeting": {
        "standard": {
            "template": "Hi {name}! Thanks for reaching out. I'm {agent} and I'll be helping you today. How can I assist you?",
            "variables": ["name", "agent"],
            "use_when": "Standard opening for new chat"
        },
        "returning": {
            "template": "Welcome back, {name}! Great to see you again. I'm {agent}. What can I help you with today?",
            "variables": ["name", "agent"],
            "use_when": "Customer has chatted before"
        },
        "after_wait": {
            "template": "Hi {name}, thanks for your patience! I'm {agent} and I'm ready to help. What can I do for you?",
            "variables": ["name", "agent"],
            "use_when": "Customer waited in queue"
        },
        "proactive": {
            "template": "Hi there! I noticed you've been on our {page} for a while. I'm {agent} - is there anything I can help you find?",
            "variables": ["page", "agent"],
            "use_when": "Proactive chat engagement"
        }
    },

    "hold": {
        "short": {
            "template": "Let me check that for you - one moment!",
            "variables": [],
            "use_when": "Quick lookup (<1 minute)"
        },
        "medium": {
            "template": "I'm looking into this now. It might take me a couple of minutes - I'll keep you posted!",
            "variables": [],
            "use_when": "Research needed (1-3 minutes)"
        },
        "long": {
            "template": "This is taking a bit longer than expected because {reason}. Would you prefer to wait, or should I email you the answer within the hour?",
            "variables": ["reason"],
            "use_when": "Extended research (3+ minutes)"
        },
        "update": {
            "template": "Still working on this for you! I've {progress} and I'm now {current_action}. Almost there!",
            "variables": ["progress", "current_action"],
            "use_when": "Providing status update"
        }
    },

    "billing": {
        "question": {
            "template": "Let me pull up your billing information. I can see {details}. Would you like me to explain any of these charges?",
            "variables": ["details"],
            "use_when": "Customer asking about charges"
        },
        "refund_approved": {
            "template": "Good news! I've processed a refund of ${amount}. You should see it in your account within {timeframe} business days. Is there anything else I can help with?",
            "variables": ["amount", "timeframe"],
            "use_when": "Refund has been approved and processed"
        },
        "refund_denied": {
            "template": "I'm sorry, but I'm unable to process a refund because {reason}. However, I can offer {alternative}. Would that help?",
            "variables": ["reason", "alternative"],
            "use_when": "Refund cannot be approved"
        },
        "double_charge": {
            "template": "I'm sorry about that double charge! I can see the duplicate from {date}. I'm processing a refund for ${amount} right now - you'll see it back within {timeframe} business days.",
            "variables": ["date", "amount", "timeframe"],
            "use_when": "Customer charged twice"
        }
    },

    "technical": {
        "troubleshoot_start": {
            "template": "I'm sorry you're running into this issue! Let's troubleshoot together. Can you tell me:\n1. What device/browser are you using?\n2. When did this start happening?\n3. Do you see any error messages?",
            "variables": [],
            "use_when": "Starting technical troubleshooting"
        },
        "try_this": {
            "template": "Let's try this: {steps}. Can you test that while we're chatting so I can help if anything comes up?",
            "variables": ["steps"],
            "use_when": "Providing troubleshooting steps"
        },
        "cache_clear": {
            "template": "Let's start with a quick cache clear:\n1. Press Ctrl+Shift+Delete (Cmd+Shift+Delete on Mac)\n2. Select 'Cached images and files'\n3. Click 'Clear data'\n4. Refresh the page\n\nDoes that help?",
            "variables": [],
            "use_when": "Common browser issues"
        },
        "escalate_tech": {
            "template": "This looks like it needs our technical team to investigate. I'm creating a priority ticket for them. They'll reach out to you at {contact} within {timeframe}.",
            "variables": ["contact", "timeframe"],
            "use_when": "Need engineering team"
        }
    },

    "password": {
        "reset_sent": {
            "template": "No problem! I've sent a password reset link to {email}. It should arrive within a few minutes. If you don't see it, check your spam folder.",
            "variables": ["email"],
            "use_when": "Password reset requested"
        },
        "locked_out": {
            "template": "I see your account was temporarily locked due to {reason}. I've unlocked it for you. You should be able to log in now - try using the 'Forgot Password' option to set a new password.",
            "variables": ["reason"],
            "use_when": "Account locked"
        }
    },

    "empathy": {
        "frustration": {
            "template": "I completely understand how frustrating that must be. Let me see what I can do to fix this for you right away.",
            "variables": [],
            "use_when": "Customer expressing frustration"
        },
        "apology": {
            "template": "I'm really sorry you're dealing with this - that's definitely not the experience we want you to have. Let me make this right.",
            "variables": [],
            "use_when": "Apologizing for issue"
        },
        "validation": {
            "template": "You're absolutely right to bring this up. This shouldn't have happened, and I appreciate you letting us know.",
            "variables": [],
            "use_when": "Validating customer concern"
        }
    },

    "escalation": {
        "supervisor": {
            "template": "I understand you'd like to speak with a supervisor. Let me connect you with {name} who can help further. One moment please.",
            "variables": ["name"],
            "use_when": "Transferring to supervisor"
        },
        "different_team": {
            "template": "To best help you with this, I'm going to connect you with our {team} team who specializes in {area}. I'll give them a summary so you don't have to repeat yourself.",
            "variables": ["team", "area"],
            "use_when": "Transferring to specialist team"
        }
    },

    "closing": {
        "resolved": {
            "template": "I'm glad I could help! Is there anything else you need before we wrap up?",
            "variables": [],
            "use_when": "Issue resolved, checking for more"
        },
        "goodbye": {
            "template": "Thanks so much for chatting with us today, {name}! If you ever need anything else, we're just a message away. Have a great {time_of_day}!",
            "variables": ["name", "time_of_day"],
            "use_when": "Final goodbye"
        },
        "survey": {
            "template": "Before you go - if you have 30 seconds, we'd love your feedback on this chat. Thanks again, {name}!",
            "variables": ["name"],
            "use_when": "Requesting survey completion"
        }
    },

    "retention": {
        "cancel_request": {
            "template": "I'd hate to see you go - you've been with us for {duration}. Before you decide, would you mind sharing what's driving this? I may be able to help resolve the issue.",
            "variables": ["duration"],
            "use_when": "Customer wants to cancel"
        },
        "offer": {
            "template": "I understand. What if I could offer you {offer}? Would that change things?",
            "variables": ["offer"],
            "use_when": "Making retention offer"
        }
    }
}


def get_responses_by_category(category):
    """Get all responses in a category."""
    if category not in RESPONSES:
        return None
    return RESPONSES[category]


def get_specific_response(category, issue):
    """Get specific response by category and issue."""
    if category not in RESPONSES:
        return None
    if issue not in RESPONSES[category]:
        return None
    return RESPONSES[category][issue]


def search_responses(query):
    """Search responses by keyword."""
    query_lower = query.lower()
    results = []

    for category, responses in RESPONSES.items():
        for issue, data in responses.items():
            if (query_lower in category.lower() or
                query_lower in issue.lower() or
                query_lower in data['template'].lower() or
                query_lower in data['use_when'].lower()):
                results.append({
                    'category': category,
                    'issue': issue,
                    **data
                })

    return results


def list_categories():
    """List all available categories."""
    return list(RESPONSES.keys())


def format_response(response_data, fill_variables=None):
    """Format response with variables filled in."""
    template = response_data['template']

    if fill_variables:
        for var, value in fill_variables.items():
            template = template.replace('{' + var + '}', value)

    return {
        'response': template,
        'variables_needed': response_data.get('variables', []),
        'use_when': response_data.get('use_when', '')
    }


def main():
    parser = argparse.ArgumentParser(description='Get canned chat responses')
    parser.add_argument('--category', '-c', help='Response category')
    parser.add_argument('--issue', '-i', help='Specific issue within category')
    parser.add_argument('--search', '-s', help='Search for responses')
    parser.add_argument('--list', '-l', action='store_true', help='List all categories')
    parser.add_argument('--format', '-f', choices=['json', 'text'],
                        default='text', help='Output format')

    args = parser.parse_args()

    if args.list:
        categories = list_categories()
        if args.format == 'json':
            print(json.dumps({'categories': categories}))
        else:
            print('\nAvailable Categories:')
            for cat in categories:
                issues = list(RESPONSES[cat].keys())
                print(f'  {cat}: {", ".join(issues)}')
        return

    if args.search:
        results = search_responses(args.search)
        if args.format == 'json':
            print(json.dumps({'results': results}, indent=2))
        else:
            if not results:
                print(f'No responses found for: {args.search}')
            else:
                print(f'\nFound {len(results)} response(s):\n')
                for r in results:
                    print(f"[{r['category']}/{r['issue']}]")
                    print(f"Use when: {r['use_when']}")
                    print(f"Template:\n{r['template']}")
                    if r['variables']:
                        print(f"Variables: {', '.join(r['variables'])}")
                    print()
        return

    if args.category and args.issue:
        response = get_specific_response(args.category, args.issue)
        if not response:
            print(json.dumps({'error': f'Response not found: {args.category}/{args.issue}'}))
            sys.exit(1)

        if args.format == 'json':
            print(json.dumps(response, indent=2))
        else:
            print(f"\n[{args.category}/{args.issue}]")
            print(f"Use when: {response['use_when']}")
            print(f"\nTemplate:\n{response['template']}")
            if response['variables']:
                print(f"\nVariables to fill: {', '.join(response['variables'])}")
        return

    if args.category:
        responses = get_responses_by_category(args.category)
        if not responses:
            print(json.dumps({'error': f'Category not found: {args.category}'}))
            sys.exit(1)

        if args.format == 'json':
            print(json.dumps(responses, indent=2))
        else:
            print(f'\n=== {args.category.upper()} Responses ===\n')
            for issue, data in responses.items():
                print(f"[{issue}]")
                print(f"Use when: {data['use_when']}")
                print(f"Template:\n{data['template']}\n")
        return

    # Default: show help
    parser.print_help()


if __name__ == '__main__':
    main()
