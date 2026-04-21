#!/usr/bin/env python3
"""Retro board template generator.

Generates markdown templates for various retrospective formats.
Supports Start-Stop-Continue, 4Ls, Sailboat, Mad-Sad-Glad,
Starfish, and Timeline formats.

Usage:
    python retro_board_generator.py --format ssc
    python retro_board_generator.py --format 4ls --sprint "Sprint 14"
    python retro_board_generator.py --format sailboat --goal "Ship MVP by June 1"
    python retro_board_generator.py --list
    python retro_board_generator.py --format ssc --json
"""

import argparse
import json
import sys
from datetime import date


FORMATS = {
    "ssc": {
        "name": "Start-Stop-Continue",
        "duration": "30-45 min",
        "team_size": "3-8",
        "sections": ["Start (New things to try)", "Stop (Things to drop)", "Continue (Things working well)"],
    },
    "4ls": {
        "name": "4Ls (Liked, Learned, Lacked, Longed For)",
        "duration": "45-60 min",
        "team_size": "4-10",
        "sections": ["Liked (What went well)", "Learned (What we discovered)", "Lacked (What was missing)", "Longed For (What we wish we had)"],
    },
    "sailboat": {
        "name": "Sailboat",
        "duration": "45-60 min",
        "team_size": "4-12",
        "sections": ["Island (Our Goal/Vision)", "Wind (Helping us move forward)", "Anchor (Slowing us down)", "Rocks (Risks ahead)"],
    },
    "msg": {
        "name": "Mad-Sad-Glad",
        "duration": "30-45 min",
        "team_size": "3-8",
        "sections": ["Mad (Frustrated about)", "Sad (Disappointed about)", "Glad (Happy about)"],
    },
    "starfish": {
        "name": "Starfish",
        "duration": "45-60 min",
        "team_size": "4-10",
        "sections": ["More of", "Less of", "Keep doing", "Start doing", "Stop doing"],
    },
    "timeline": {
        "name": "Timeline",
        "duration": "60-90 min",
        "team_size": "5-12",
        "sections": ["Key Events", "Positive Moments (above the line)", "Negative Moments (below the line)", "Patterns Observed"],
    },
}


def generate_board(format_key, sprint=None, goal=None):
    """Generate a retro board template in markdown."""
    if format_key not in FORMATS:
        return None

    fmt = FORMATS[format_key]
    today = date.today().isoformat()
    sprint_label = sprint or "Sprint [N]"

    lines = [
        f"# {fmt['name']} Retrospective",
        "",
        f"**Sprint:** {sprint_label}",
        f"**Date:** {today}",
        f"**Format:** {fmt['name']}",
        f"**Suggested Duration:** {fmt['duration']}",
        f"**Ideal Team Size:** {fmt['team_size']}",
        "",
        "---",
        "",
        "## Ground Rules",
        "",
        "- What is said in retro stays in retro",
        "- Focus on processes and systems, not people",
        "- Everyone participates",
        "- Be specific with examples",
        "- We commit to at least one improvement action",
        "",
        "---",
        "",
    ]

    if format_key == "sailboat" and goal:
        lines.append(f"## Island (Our Goal)")
        lines.append(f"**{goal}**")
        lines.append("")

    for section in fmt["sections"]:
        if format_key == "sailboat" and "Island" in section and goal:
            continue
        lines.append(f"## {section}")
        lines.append("")
        lines.append("- ")
        lines.append("- ")
        lines.append("- ")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## Action Items",
        "",
        "| # | Action | Owner | Deadline | Ticket |",
        "|---|--------|-------|----------|--------|",
        "| 1 | | | | |",
        "| 2 | | | | |",
        "| 3 | | | | |",
        "",
        "---",
        "",
        "## Team Mood Check (1-5)",
        "",
        "Rate your mood anonymously: 1 (bad) to 5 (great)",
        "",
        "Average: ___",
    ])

    return "\n".join(lines)


def list_formats():
    """List all available retro formats."""
    result = []
    for key, fmt in FORMATS.items():
        result.append({
            "key": key,
            "name": fmt["name"],
            "duration": fmt["duration"],
            "team_size": fmt["team_size"],
            "sections": len(fmt["sections"]),
        })
    return result


def main():
    parser = argparse.ArgumentParser(
        description="Generate retrospective board templates",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Formats:
  ssc       Start-Stop-Continue (30-45 min, 3-8 people)
  4ls       Liked-Learned-Lacked-Longed For (45-60 min, 4-10 people)
  sailboat  Sailboat metaphor (45-60 min, 4-12 people)
  msg       Mad-Sad-Glad (30-45 min, 3-8 people)
  starfish  More/Less/Keep/Start/Stop (45-60 min, 4-10 people)
  timeline  Chronological timeline (60-90 min, 5-12 people)

Examples:
  %(prog)s --format ssc
  %(prog)s --format sailboat --goal "Ship MVP by June 1"
  %(prog)s --format 4ls --sprint "Sprint 14"
  %(prog)s --list
  %(prog)s --list --json
        """,
    )
    parser.add_argument("--format", "-f", type=str, help="Retro format (ssc, 4ls, sailboat, msg, starfish, timeline)")
    parser.add_argument("--sprint", type=str, help="Sprint name")
    parser.add_argument("--goal", type=str, help="Sprint/project goal (for sailboat format)")
    parser.add_argument("--list", action="store_true", help="List available formats")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.list:
        formats = list_formats()
        if args.json:
            print(json.dumps({"formats": formats}, indent=2))
        else:
            print("AVAILABLE RETRO FORMATS")
            print("-" * 60)
            for f in formats:
                print(f"  {f['key']:<12} {f['name']:<40} {f['duration']}")
        return

    if not args.format:
        print("Specify a format with --format or use --list to see options.")
        parser.print_help()
        sys.exit(1)

    if args.format not in FORMATS:
        print(f"Unknown format: {args.format}")
        print(f"Available: {', '.join(FORMATS.keys())}")
        sys.exit(1)

    board = generate_board(args.format, sprint=args.sprint, goal=args.goal)

    if args.json:
        print(json.dumps({
            "format": args.format,
            "format_info": FORMATS[args.format],
            "board_markdown": board,
        }, indent=2))
    else:
        print(board)


if __name__ == "__main__":
    main()
