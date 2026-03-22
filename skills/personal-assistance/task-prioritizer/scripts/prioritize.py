#!/usr/bin/env python3
"""
Score and prioritize tasks using ICE framework.

Usage:
    python prioritize.py --interactive
    python prioritize.py --tasks tasks.json

Output: JSON with prioritized task list
"""

import argparse
import json
import sys


def calculate_ice(impact, confidence, ease):
    """Calculate ICE score."""
    return round((impact + confidence + ease) / 3, 1)


def interactive_prioritize():
    """Interactive task prioritization."""
    print("=== Task Prioritizer (ICE Framework) ===\n")
    print("Enter tasks one at a time. Type 'done' when finished.\n")

    tasks = []

    while True:
        task_name = input(f"\nTask {len(tasks)+1} (or 'done'): ").strip()
        if task_name.lower() == 'done':
            break

        print(f"\nScoring '{task_name}' (1-10 scale):")

        try:
            impact = int(input("  Impact (value if completed): "))
            confidence = int(input("  Confidence (certainty of impact): "))
            ease = int(input("  Ease (10=very easy, 1=very hard): "))

            # Validate scores
            for score in [impact, confidence, ease]:
                if not 1 <= score <= 10:
                    print("  Scores must be between 1 and 10")
                    continue

            ice_score = calculate_ice(impact, confidence, ease)

            tasks.append({
                "name": task_name,
                "impact": impact,
                "confidence": confidence,
                "ease": ease,
                "ice_score": ice_score
            })

            print(f"  ICE Score: {ice_score}")

        except ValueError:
            print("  Invalid input, skipping task")
            continue

    return tasks


def prioritize_tasks(tasks):
    """Sort tasks by ICE score."""
    sorted_tasks = sorted(tasks, key=lambda x: x.get("ice_score", 0), reverse=True)

    # Add rank
    for i, task in enumerate(sorted_tasks, 1):
        task["rank"] = i

        # Add recommendation
        score = task.get("ice_score", 0)
        if score >= 8:
            task["priority"] = "HIGH - Do first"
        elif score >= 6:
            task["priority"] = "MEDIUM - Schedule"
        elif score >= 4:
            task["priority"] = "LOW - Delegate or defer"
        else:
            task["priority"] = "SKIP - Consider eliminating"

    return sorted_tasks


def format_output(tasks):
    """Format prioritized tasks for display."""
    result = {
        "total_tasks": len(tasks),
        "prioritized_list": tasks,
        "today_focus": [t["name"] for t in tasks[:3]] if tasks else [],
        "summary": {
            "high_priority": len([t for t in tasks if t.get("ice_score", 0) >= 8]),
            "medium_priority": len([t for t in tasks if 6 <= t.get("ice_score", 0) < 8]),
            "low_priority": len([t for t in tasks if t.get("ice_score", 0) < 6])
        }
    }
    return result


def main():
    parser = argparse.ArgumentParser(description="Prioritize tasks with ICE")
    parser.add_argument("--interactive", "-i", action="store_true",
                        help="Interactive mode")
    parser.add_argument("--tasks", "-t", help="JSON file with tasks")

    args = parser.parse_args()

    if args.interactive:
        tasks = interactive_prioritize()
    elif args.tasks:
        try:
            with open(args.tasks, 'r') as f:
                data = json.load(f)
                # Handle both array and object with "tasks" key
                tasks = data if isinstance(data, list) else data.get("tasks", [])

                # Calculate ICE scores if not present
                for task in tasks:
                    if "ice_score" not in task:
                        task["ice_score"] = calculate_ice(
                            task.get("impact", 5),
                            task.get("confidence", 5),
                            task.get("ease", 5)
                        )
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(json.dumps({"error": str(e)}))
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(1)

    if not tasks:
        print(json.dumps({"message": "No tasks to prioritize"}))
        return

    prioritized = prioritize_tasks(tasks)
    result = format_output(prioritized)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
