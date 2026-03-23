#!/usr/bin/env python3
"""
Interactive troubleshooting guide.

Usage:
    python troubleshoot_guide.py --issue "login"
    python troubleshoot_guide.py --category performance
    python troubleshoot_guide.py --interactive

Output: Guided troubleshooting steps based on issue type
"""

import argparse
import json


# Issue categories and troubleshooting flows
TROUBLESHOOTING_FLOWS = {
    "login": {
        "name": "Login/Authentication Issues",
        "initial_questions": [
            "What error message do you see (if any)?",
            "Are you using social login (Google, Facebook) or email/password?",
            "Have you tried resetting your password?",
            "Does the issue happen on all devices or just one?"
        ],
        "steps": [
            {
                "step": 1,
                "action": "Try password reset",
                "instructions": "Go to the login page and click 'Forgot Password'. Enter your email and follow the reset link.",
                "success": "Password reset email received → Reset and try logging in",
                "failure": "No email received → Check spam folder, verify email address"
            },
            {
                "step": 2,
                "action": "Clear browser data",
                "instructions": "Clear cookies and cache for the site. In Chrome: Ctrl+Shift+Delete → Select 'Cookies' and 'Cache' → Clear",
                "success": "Login works → Browser data was corrupted",
                "failure": "Still can't login → Proceed to next step"
            },
            {
                "step": 3,
                "action": "Try incognito mode",
                "instructions": "Open an incognito/private window and try logging in",
                "success": "Works in incognito → Browser extension conflict",
                "failure": "Fails in incognito → Not a browser issue"
            },
            {
                "step": 4,
                "action": "Try different browser",
                "instructions": "Install or use a different browser (Chrome, Firefox, Safari, Edge)",
                "success": "Works in different browser → Original browser issue",
                "failure": "Fails everywhere → Account or server issue"
            },
            {
                "step": 5,
                "action": "Check account status",
                "instructions": "Contact support to verify account is active and not locked",
                "success": "Account unlocked → Security lock was triggered",
                "failure": "Account looks fine → Escalate to engineering"
            }
        ],
        "common_causes": [
            "Incorrect password",
            "Account locked due to failed attempts",
            "Browser cache/cookie issue",
            "SSO/OAuth configuration problem",
            "Account deleted or suspended"
        ]
    },
    "performance": {
        "name": "Performance/Loading Issues",
        "initial_questions": [
            "Is the entire site slow or just specific pages?",
            "When did this start happening?",
            "What's your internet connection speed?",
            "Does it happen at specific times of day?"
        ],
        "steps": [
            {
                "step": 1,
                "action": "Check system status",
                "instructions": "Visit the status page (status.example.com) to check for known issues",
                "success": "Known issue identified → Wait for resolution",
                "failure": "No known issues → Continue troubleshooting"
            },
            {
                "step": 2,
                "action": "Test internet speed",
                "instructions": "Go to speedtest.net and run a test. Share the results (download/upload speeds)",
                "success": "Speed is good (>10 Mbps) → Not an internet issue",
                "failure": "Speed is slow (<5 Mbps) → Contact ISP or use different network"
            },
            {
                "step": 3,
                "action": "Clear browser cache",
                "instructions": "Clear all browsing data including cache, cookies, and history",
                "success": "Performance improves → Cache was bloated/corrupted",
                "failure": "Still slow → Continue troubleshooting"
            },
            {
                "step": 4,
                "action": "Disable extensions",
                "instructions": "Disable all browser extensions and reload the page",
                "success": "Performance improves → Extension is causing issue",
                "failure": "Still slow → Not extension-related"
            },
            {
                "step": 5,
                "action": "Try different device",
                "instructions": "Test on a different device (phone, tablet, another computer)",
                "success": "Works fine elsewhere → Original device issue",
                "failure": "Slow everywhere → Server-side issue, escalate"
            }
        ],
        "common_causes": [
            "Slow internet connection",
            "Server under heavy load",
            "Browser extensions blocking/slowing",
            "Large amount of data in account",
            "Outdated browser"
        ]
    },
    "feature": {
        "name": "Feature Not Working",
        "initial_questions": [
            "Which specific feature is not working?",
            "What happens when you try to use it?",
            "Did it work before? When did it stop?",
            "Any error messages?"
        ],
        "steps": [
            {
                "step": 1,
                "action": "Verify permissions",
                "instructions": "Check if your account/plan has access to this feature. Go to Settings → Plan",
                "success": "Feature is included → Continue troubleshooting",
                "failure": "Feature not in plan → Upgrade needed"
            },
            {
                "step": 2,
                "action": "Try hard refresh",
                "instructions": "Press Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac) to force reload",
                "success": "Feature works → Cached JavaScript was outdated",
                "failure": "Still broken → Continue troubleshooting"
            },
            {
                "step": 3,
                "action": "Check browser console",
                "instructions": "Press F12 → Console tab. Look for red error messages",
                "success": "No errors → Not a JavaScript issue",
                "failure": "Errors present → Screenshot and escalate"
            },
            {
                "step": 4,
                "action": "Test in different browser",
                "instructions": "Try the feature in a different browser",
                "success": "Works in different browser → Browser compatibility issue",
                "failure": "Broken everywhere → Bug or server issue"
            },
            {
                "step": 5,
                "action": "Document and escalate",
                "instructions": "Record exact steps to reproduce, error messages, and browser info. Escalate to engineering",
                "success": "Bug confirmed and reported",
                "failure": "N/A"
            }
        ],
        "common_causes": [
            "Missing permissions/plan access",
            "Browser compatibility issue",
            "JavaScript error",
            "Server-side bug",
            "Feature temporarily disabled"
        ]
    },
    "data": {
        "name": "Data/Sync Issues",
        "initial_questions": [
            "Is data missing, incorrect, or not syncing?",
            "When was the data last seen correctly?",
            "Are you using multiple devices or team members?",
            "Any recent imports or bulk changes?"
        ],
        "steps": [
            {
                "step": 1,
                "action": "Force sync",
                "instructions": "Log out and log back in, or use manual sync option if available",
                "success": "Data appears → Sync was delayed",
                "failure": "Data still missing → Continue investigation"
            },
            {
                "step": 2,
                "action": "Check trash/archive",
                "instructions": "Look in Trash, Archive, or Recently Deleted folders",
                "success": "Data found → Restore from trash",
                "failure": "Not in trash → May be permanently deleted"
            },
            {
                "step": 3,
                "action": "Check activity log",
                "instructions": "Review activity/audit log for recent deletions or changes",
                "success": "Found the change → Identify who/what caused it",
                "failure": "No record → May be server-side issue"
            },
            {
                "step": 4,
                "action": "Check permissions",
                "instructions": "Verify you have permission to view this data",
                "success": "Permission issue identified → Request access",
                "failure": "Permissions look fine → Escalate"
            },
            {
                "step": 5,
                "action": "Request data recovery",
                "instructions": "Contact support with details for potential data recovery from backups",
                "success": "Data recovered from backup",
                "failure": "Data unrecoverable"
            }
        ],
        "common_causes": [
            "Accidental deletion",
            "Sync conflict between devices",
            "Permission changes",
            "Import/export error",
            "Database issue"
        ]
    },
    "error": {
        "name": "Error Messages",
        "initial_questions": [
            "What is the exact error message or code?",
            "What were you doing when the error appeared?",
            "Does the error happen every time?",
            "Screenshot of the error?"
        ],
        "steps": [
            {
                "step": 1,
                "action": "Document the error",
                "instructions": "Take a screenshot of the error. Note the exact message and any error codes",
                "success": "Error documented",
                "failure": "N/A"
            },
            {
                "step": 2,
                "action": "Try again",
                "instructions": "Wait 30 seconds and try the action again",
                "success": "Works now → Temporary glitch",
                "failure": "Error repeats → Continue troubleshooting"
            },
            {
                "step": 3,
                "action": "Check status page",
                "instructions": "Visit status page for known issues",
                "success": "Known issue → Wait for resolution",
                "failure": "No known issues → Continue"
            },
            {
                "step": 4,
                "action": "Try different approach",
                "instructions": "If possible, try a different way to accomplish the same task",
                "success": "Alternative works → Workaround found",
                "failure": "Still failing → Escalate"
            },
            {
                "step": 5,
                "action": "Escalate with details",
                "instructions": "Report to support with: error message, steps to reproduce, browser info, screenshots",
                "success": "Ticket created",
                "failure": "N/A"
            }
        ],
        "common_causes": [
            "Server-side error",
            "Invalid input",
            "Network connectivity",
            "Session expired",
            "Bug in application"
        ]
    }
}


def get_troubleshooting_flow(issue_type):
    """Get troubleshooting flow for an issue type."""

    # Try exact match
    if issue_type.lower() in TROUBLESHOOTING_FLOWS:
        return TROUBLESHOOTING_FLOWS[issue_type.lower()]

    # Try keyword match
    keywords = {
        "login": ["login", "signin", "sign in", "password", "authentication", "auth", "access"],
        "performance": ["slow", "loading", "timeout", "performance", "speed", "lag"],
        "feature": ["feature", "button", "click", "not working", "broken", "doesn't work"],
        "data": ["data", "missing", "sync", "lost", "deleted", "incorrect"],
        "error": ["error", "message", "code", "failed", "exception"]
    }

    issue_lower = issue_type.lower()
    for flow_type, words in keywords.items():
        for word in words:
            if word in issue_lower:
                return TROUBLESHOOTING_FLOWS[flow_type]

    return None


def interactive_troubleshoot():
    """Interactive troubleshooting session."""

    print("\n" + "=" * 50)
    print("INTERACTIVE TROUBLESHOOTING GUIDE")
    print("=" * 50)

    print("\nWhat type of issue are you experiencing?")
    for i, (key, flow) in enumerate(TROUBLESHOOTING_FLOWS.items(), 1):
        print(f"  {i}. {flow['name']}")

    choice = input("\nSelect (1-5) or describe issue: ").strip()

    # Handle numeric choice
    if choice.isdigit() and 1 <= int(choice) <= len(TROUBLESHOOTING_FLOWS):
        flow_key = list(TROUBLESHOOTING_FLOWS.keys())[int(choice) - 1]
        flow = TROUBLESHOOTING_FLOWS[flow_key]
    else:
        flow = get_troubleshooting_flow(choice)
        if not flow:
            print("Couldn't identify issue type. Using general error flow.")
            flow = TROUBLESHOOTING_FLOWS["error"]

    print(f"\n--- {flow['name'].upper()} ---")

    # Ask initial questions
    print("\nFirst, let me gather some information:")
    responses = []
    for q in flow["initial_questions"]:
        response = input(f"\n  {q}\n  → ").strip()
        responses.append({"question": q, "answer": response})

    # Go through steps
    print("\n" + "=" * 50)
    print("TROUBLESHOOTING STEPS")
    print("=" * 50)

    for step in flow["steps"]:
        print(f"\n--- Step {step['step']}: {step['action']} ---")
        print(f"\n{step['instructions']}")

        result = input("\nDid this work? (y/n/skip): ").strip().lower()

        if result == 'y':
            print(f"\n✓ {step['success']}")
            if input("\nIssue resolved? (y/n): ").strip().lower() == 'y':
                print("\nGreat! Issue resolved at step", step['step'])
                return {
                    "resolved": True,
                    "resolution_step": step['step'],
                    "action": step['action']
                }
        elif result == 'n':
            print(f"\n→ {step['failure']}")
        else:
            print("\nSkipping to next step...")

    # If we get here, issue wasn't resolved
    print("\n" + "=" * 50)
    print("ISSUE NOT RESOLVED")
    print("=" * 50)

    print("\nCommon causes for this issue type:")
    for cause in flow["common_causes"]:
        print(f"  • {cause}")

    print("\nRecommendation: Escalate to engineering support with the following:")
    print("  1. Steps you tried")
    print("  2. Error messages/screenshots")
    print("  3. Browser and device info")

    return {
        "resolved": False,
        "steps_tried": len(flow["steps"]),
        "common_causes": flow["common_causes"]
    }


def format_flow(flow, format_type="text"):
    """Format troubleshooting flow for display."""

    if format_type == "json":
        return json.dumps(flow, indent=2)

    lines = []
    lines.append("\n" + "=" * 50)
    lines.append(f"TROUBLESHOOTING: {flow['name'].upper()}")
    lines.append("=" * 50)

    lines.append("\n--- Initial Questions ---")
    for q in flow["initial_questions"]:
        lines.append(f"  • {q}")

    lines.append("\n--- Troubleshooting Steps ---")
    for step in flow["steps"]:
        lines.append(f"\n  Step {step['step']}: {step['action']}")
        lines.append(f"    Instructions: {step['instructions']}")
        lines.append(f"    ✓ If works: {step['success']}")
        lines.append(f"    ✗ If fails: {step['failure']}")

    lines.append("\n--- Common Causes ---")
    for cause in flow["common_causes"]:
        lines.append(f"  • {cause}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description='Interactive troubleshooting guide')
    parser.add_argument('--issue', '-i', help='Issue description or type')
    parser.add_argument('--category', '-c',
                        choices=list(TROUBLESHOOTING_FLOWS.keys()),
                        help='Issue category')
    parser.add_argument('--list', '-l', action='store_true',
                        help='List all troubleshooting categories')
    parser.add_argument('--interactive', action='store_true',
                        help='Start interactive troubleshooting')
    parser.add_argument('--format', '-f', choices=['json', 'text'],
                        default='text', help='Output format')

    args = parser.parse_args()

    if args.list:
        print("\nAvailable Troubleshooting Categories:\n")
        for key, flow in TROUBLESHOOTING_FLOWS.items():
            print(f"  {key}: {flow['name']}")
            print(f"    Steps: {len(flow['steps'])}")
        return

    if args.interactive:
        result = interactive_troubleshoot()
        print(f"\n{json.dumps(result, indent=2)}")
        return

    if args.category:
        flow = TROUBLESHOOTING_FLOWS[args.category]
        print(format_flow(flow, args.format))
        return

    if args.issue:
        flow = get_troubleshooting_flow(args.issue)
        if flow:
            print(format_flow(flow, args.format))
        else:
            print(f"No specific troubleshooting flow for: {args.issue}")
            print("Use --list to see available categories")
        return

    parser.print_help()


if __name__ == '__main__':
    main()
