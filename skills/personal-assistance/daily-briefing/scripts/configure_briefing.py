#!/usr/bin/env python3
"""Configure briefing preferences and component selection.

Usage:
    python configure_briefing.py --components calendar,tasks,email,weather
    python configure_briefing.py --show-config
    python configure_briefing.py --work-start 09:00 --work-end 17:30
"""

import argparse
import json
import sys
from datetime import datetime

DEFAULT_CONFIG = {
    "components": {
        "calendar": {"enabled": True, "required": True},
        "tasks": {"enabled": True, "required": True},
        "overdue_items": {"enabled": True, "required": True},
        "email": {"enabled": True, "required": False},
        "weather": {"enabled": False, "required": False},
        "commute": {"enabled": False, "required": False},
        "news": {"enabled": False, "required": False},
        "daily_goals": {"enabled": True, "required": False},
        "slack_mentions": {"enabled": False, "required": False},
    },
    "schedule": {
        "morning_briefing": "08:00",
        "end_of_day_review": "17:00",
        "work_start": "08:00",
        "work_end": "17:00",
        "lunch_start": "12:00",
        "lunch_end": "13:00",
    },
    "delivery": {
        "channel": "terminal",
        "format": "markdown",
    },
    "rollover_rules": {
        "max_rolled_items_per_day": 5,
        "stuck_task_threshold": 5,
        "weekend_batch_to_monday": True,
    },
    "focus_goals": {
        "max_goals": 3,
        "carry_over_incomplete": True,
    },
}


def show_config(config: dict) -> None:
    """Display current configuration."""
    print("Current Briefing Configuration")
    print("=" * 50)
    print(json.dumps(config, indent=2))


def update_components(config: dict, components_str: str) -> dict:
    """Enable specified components, disable others (except required)."""
    requested = [c.strip() for c in components_str.split(",")]

    for name, settings in config["components"].items():
        if settings.get("required"):
            settings["enabled"] = True
        elif name in requested:
            settings["enabled"] = True
        else:
            settings["enabled"] = False

    return config


def main():
    parser = argparse.ArgumentParser(description="Configure daily briefing preferences.")
    parser.add_argument("--components", help="Comma-separated components to enable (e.g., calendar,tasks,email,weather)")
    parser.add_argument("--work-start", help="Work start time (HH:MM)")
    parser.add_argument("--work-end", help="Work end time (HH:MM)")
    parser.add_argument("--lunch-start", help="Lunch start time (HH:MM)")
    parser.add_argument("--lunch-end", help="Lunch end time (HH:MM)")
    parser.add_argument("--briefing-time", help="Morning briefing delivery time (HH:MM)")
    parser.add_argument("--review-time", help="End-of-day review time (HH:MM)")
    parser.add_argument("--channel", choices=["terminal", "email", "slack", "dashboard"], help="Delivery channel")
    parser.add_argument("--format", choices=["markdown", "json", "html"], dest="output_format", help="Output format")
    parser.add_argument("--show-config", action="store_true", help="Display current configuration")
    parser.add_argument("--reset", action="store_true", help="Reset to default configuration")

    args = parser.parse_args()
    config = DEFAULT_CONFIG.copy()

    if args.show_config or (not any([args.components, args.work_start, args.work_end, args.channel, args.output_format, args.reset])):
        show_config(config)
        return

    if args.reset:
        config = DEFAULT_CONFIG.copy()
        print("Configuration reset to defaults.")

    if args.components:
        config = update_components(config, args.components)

    if args.work_start:
        config["schedule"]["work_start"] = args.work_start
    if args.work_end:
        config["schedule"]["work_end"] = args.work_end
    if args.lunch_start:
        config["schedule"]["lunch_start"] = args.lunch_start
    if args.lunch_end:
        config["schedule"]["lunch_end"] = args.lunch_end
    if args.briefing_time:
        config["schedule"]["morning_briefing"] = args.briefing_time
    if args.review_time:
        config["schedule"]["end_of_day_review"] = args.review_time
    if args.channel:
        config["delivery"]["channel"] = args.channel
    if args.output_format:
        config["delivery"]["format"] = args.output_format

    print("Briefing configuration updated:")
    print(json.dumps(config, indent=2))


if __name__ == "__main__":
    main()
