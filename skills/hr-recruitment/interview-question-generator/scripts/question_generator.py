#!/usr/bin/env python3
"""
Interview Question Generator

Generates calibrated interview questions based on role level, competencies,
and question types. Produces interview guides with scoring rubrics.

Usage:
    python question_generator.py --demo
    python question_generator.py --role "Senior Software Engineer" --level senior --competencies "problem_solving,collaboration,technical"
    python question_generator.py --role "Product Manager" --level mid --round phone_screen --count 4
"""

import argparse
import json
import random
import sys

# --- Question Bank ---

QUESTION_BANK = {
    "problem_solving": {
        "behavioral": {
            "junior": [
                {
                    "question": "Describe a challenging assignment from school or an early work experience. How did you break it down and work through it?",
                    "probes": ["What was the hardest part?", "What would you do differently?", "How did you know you were done?"],
                    "rubric": {"1": "Vague description, no clear process", "2": "Clear scenario with some structured approach", "3": "Specific example with methodical breakdown and quantified outcome"},
                },
                {
                    "question": "Tell me about a time you had to learn something new quickly to complete a task. How did you approach it?",
                    "probes": ["What resources did you use?", "How did you verify your understanding?", "How long did it take?"],
                    "rubric": {"1": "Passive learning approach", "2": "Active learning with some structure", "3": "Systematic approach with validation and application"},
                },
            ],
            "mid": [
                {
                    "question": "Tell me about a time you solved a problem that had no obvious solution. What was your process?",
                    "probes": ["What alternatives did you consider?", "How did you validate your solution?", "What was the outcome?"],
                    "rubric": {"1": "Jumped to solution without analysis", "2": "Explored options systematically", "3": "Structured framework, tested hypotheses, measured results"},
                },
                {
                    "question": "Describe a situation where you identified a problem before anyone else noticed it. What did you do?",
                    "probes": ["What signals alerted you?", "How did you convince others it was a real problem?", "What happened?"],
                    "rubric": {"1": "Noticed issue but did not act proactively", "2": "Identified and raised the issue with a solution", "3": "Anticipated impact, proposed solution, drove resolution"},
                },
            ],
            "senior": [
                {
                    "question": "Describe a situation where you had to make a critical decision with incomplete information. What framework did you use?",
                    "probes": ["What were the trade-offs?", "How did you manage the risk?", "What would you do differently?"],
                    "rubric": {"1": "Made decision without structured approach", "2": "Clear framework with trade-off analysis", "3": "Sophisticated reasoning, stakeholder alignment, risk mitigation, and learning"},
                },
                {
                    "question": "Tell me about a time you had to rethink a solution after your initial approach failed. What happened?",
                    "probes": ["How did you recognize the failure?", "What changed in your approach?", "How did you communicate the pivot?"],
                    "rubric": {"1": "Reluctant to change course", "2": "Adapted approach with reasoning", "3": "Quick recognition, transparent communication, improved outcome"},
                },
            ],
        },
        "situational": {
            "mid": [
                {
                    "question": "Imagine you discover a critical bug in production on a Friday afternoon. Your team is unavailable. What do you do?",
                    "probes": ["How do you assess severity?", "Who do you communicate with?", "How do you balance speed vs. thoroughness?"],
                    "rubric": {"1": "Panics or waits for Monday", "2": "Assesses and escalates appropriately", "3": "Systematic triage, clear communication, fixes or mitigates with documentation"},
                },
            ],
            "senior": [
                {
                    "question": "You inherit a system with significant technical debt. Leadership wants new features, but the team is frustrated with reliability issues. How do you approach this?",
                    "probes": ["How do you prioritize?", "How do you communicate trade-offs to leadership?", "How do you keep the team motivated?"],
                    "rubric": {"1": "Picks one side without balance", "2": "Proposes a balanced plan", "3": "Data-driven prioritization, stakeholder alignment, team engagement strategy"},
                },
            ],
        },
    },
    "collaboration": {
        "behavioral": {
            "junior": [
                {
                    "question": "Describe a group project where you worked with people who had different working styles. How did you navigate that?",
                    "probes": ["What was your role?", "How did you handle disagreements?", "What was the outcome?"],
                    "rubric": {"1": "Avoided conflict or dominated", "2": "Adapted to others with some flexibility", "3": "Proactively facilitated collaboration, leveraged differences"},
                },
            ],
            "mid": [
                {
                    "question": "Tell me about a time you had to influence someone without direct authority to get a project moving.",
                    "probes": ["What was their resistance?", "What approach did you use?", "Did the relationship improve or suffer?"],
                    "rubric": {"1": "Escalated or gave up", "2": "Persuaded through logic or relationship", "3": "Built a coalition, understood motivations, achieved lasting alignment"},
                },
            ],
            "senior": [
                {
                    "question": "Give an example of a cross-functional initiative you led. How did you align stakeholders with competing priorities?",
                    "probes": ["How many teams were involved?", "What was the biggest point of contention?", "How did you measure success?"],
                    "rubric": {"1": "Managed one team, limited cross-functional impact", "2": "Coordinated multiple teams with some alignment", "3": "Drove consensus across organization, balanced competing needs, delivered measurable outcome"},
                },
            ],
        },
    },
    "leadership": {
        "behavioral": {
            "junior": [
                {
                    "question": "Tell me about a time you took initiative on something beyond your assigned responsibilities.",
                    "probes": ["What motivated you?", "How was it received?", "What did you learn?"],
                    "rubric": {"1": "Did extra work when asked", "2": "Self-identified an opportunity and acted", "3": "Proactively identified high-impact opportunity, executed, and created lasting value"},
                },
            ],
            "mid": [
                {
                    "question": "Describe a project you owned end-to-end. What went well and what would you do differently?",
                    "probes": ["How did you manage scope?", "What was the biggest risk?", "How did you communicate progress?"],
                    "rubric": {"1": "Managed tasks but not strategy", "2": "Owned delivery with clear accountability", "3": "Strategic ownership, proactive risk management, stakeholder communication, and reflection"},
                },
            ],
            "senior": [
                {
                    "question": "Tell me about a time you mentored someone through a significant challenge. What was your approach and what was the outcome?",
                    "probes": ["How did you adapt to their learning style?", "What was the most difficult moment?", "How did you measure their growth?"],
                    "rubric": {"1": "Gave advice but did not follow through", "2": "Structured mentoring with check-ins", "3": "Personalized approach, measurable growth, mentee became independent"},
                },
            ],
        },
    },
    "adaptability": {
        "behavioral": {
            "junior": [
                {
                    "question": "Tell me about a time you received critical feedback. How did you respond?",
                    "probes": ["What was the feedback?", "What changed?", "How do you seek feedback now?"],
                    "rubric": {"1": "Defensive or did not change", "2": "Accepted and made some changes", "3": "Embraced feedback, made visible changes, and sought more feedback"},
                },
            ],
            "mid": [
                {
                    "question": "Describe a situation where project requirements changed significantly midstream. How did you handle it?",
                    "probes": ["How did you re-plan?", "How did the team react?", "What was the outcome?"],
                    "rubric": {"1": "Frustrated, slow to adapt", "2": "Adapted with reasonable plan", "3": "Quickly re-prioritized, communicated clearly, delivered despite change"},
                },
            ],
            "senior": [
                {
                    "question": "Tell me about a time you had to pivot a team's direction due to a major change in strategy or market conditions.",
                    "probes": ["How did you communicate the change?", "How did you manage morale?", "What was the result?"],
                    "rubric": {"1": "Struggled to lead through change", "2": "Managed transition adequately", "3": "Turned disruption into opportunity, maintained team performance, achieved better outcome"},
                },
            ],
        },
    },
    "technical": {
        "technical": {
            "junior": [
                {
                    "question": "Explain the difference between a relational database and a NoSQL database. When would you choose each?",
                    "probes": ["Give a specific example for each", "What are the trade-offs?", "How do you decide?"],
                    "rubric": {"1": "Can define but not compare", "2": "Understands trade-offs with examples", "3": "Nuanced comparison with real-world application and edge cases"},
                },
            ],
            "mid": [
                {
                    "question": "Design a URL shortening service. Walk me through your architecture decisions.",
                    "probes": ["How do you handle collisions?", "How does it scale?", "What about analytics?"],
                    "rubric": {"1": "Basic CRUD design only", "2": "Handles scale, encoding, and storage", "3": "End-to-end design with caching, analytics, availability, and trade-off reasoning"},
                },
            ],
            "senior": [
                {
                    "question": "You receive a report that API latency has increased 5x in the last hour. Walk me through your investigation process.",
                    "probes": ["What metrics do you check first?", "How do you narrow down the root cause?", "How do you communicate during the incident?"],
                    "rubric": {"1": "Checks one or two things linearly", "2": "Systematic approach with monitoring tools", "3": "Expert triage: dashboards, logs, traces, rollback consideration, communication plan"},
                },
            ],
        },
    },
    "culture_add": {
        "culture_add": {
            "all": [
                {
                    "question": "What kind of work environment brings out your best work?",
                    "probes": ["Can you give a specific example?", "What about the opposite -- what drains you?"],
                    "rubric": {"1": "Generic answer", "2": "Thoughtful with self-awareness", "3": "Specific, authentic, and connects to our values"},
                },
                {
                    "question": "What is something you believe about your field that most people disagree with?",
                    "probes": ["How did you arrive at that view?", "How do you handle disagreement on this?"],
                    "rubric": {"1": "Conventional opinion", "2": "Genuinely contrarian with reasoning", "3": "Original thinking backed by evidence and openness to counter-arguments"},
                },
                {
                    "question": "Tell me about a time you brought a unique perspective that changed how a team approached a problem.",
                    "probes": ["What was unique about your perspective?", "How did the team react initially?", "What was the outcome?"],
                    "rubric": {"1": "Agreed with consensus", "2": "Offered a different view that was considered", "3": "Unique perspective that was adopted and improved the outcome"},
                },
            ],
        },
    },
}

COMPETENCY_NAMES = {
    "problem_solving": "Problem Solving",
    "collaboration": "Collaboration & Communication",
    "leadership": "Leadership & Ownership",
    "adaptability": "Adaptability & Resilience",
    "technical": "Technical Depth",
    "culture_add": "Culture Add",
}

ROUND_FOCUS = {
    "phone_screen": {"types": ["behavioral"], "competencies": ["problem_solving", "collaboration", "culture_add"], "count": 4},
    "technical": {"types": ["technical", "behavioral"], "competencies": ["technical", "problem_solving"], "count": 3},
    "behavioral": {"types": ["behavioral", "situational"], "competencies": ["leadership", "collaboration", "adaptability"], "count": 4},
    "culture_add": {"types": ["culture_add", "behavioral"], "competencies": ["culture_add", "collaboration"], "count": 3},
    "hiring_manager": {"types": ["situational", "behavioral"], "competencies": ["leadership", "problem_solving", "adaptability"], "count": 3},
}


def get_questions(competency, question_type, level, count=2):
    """Retrieve questions from the bank."""
    questions = []

    comp_bank = QUESTION_BANK.get(competency, {})
    type_bank = comp_bank.get(question_type, {})

    # Try exact level, then fall back to "all"
    level_questions = type_bank.get(level, []) + type_bank.get("all", [])

    if level_questions:
        selected = random.sample(level_questions, min(count, len(level_questions)))
        for q in selected:
            questions.append({
                "competency": COMPETENCY_NAMES.get(competency, competency),
                "type": question_type,
                "level": level,
                **q,
            })

    return questions


def generate_interview_guide(role, level, competencies, round_name=None, count=None):
    """Generate a complete interview guide."""
    guide = {
        "role": role,
        "level": level,
        "interview_round": round_name or "general",
        "questions": [],
        "illegal_question_reminders": [
            "Do NOT ask about: age, race, religion, family status, disability, gender, pregnancy, arrest record, salary history",
            "Instead ask about: ability to perform essential functions, schedule availability, compensation expectations",
        ],
    }

    if round_name and round_name in ROUND_FOCUS:
        focus = ROUND_FOCUS[round_name]
        target_types = focus["types"]
        target_competencies = [c for c in focus["competencies"] if c in competencies] or focus["competencies"]
        target_count = count or focus["count"]
    else:
        target_types = ["behavioral", "situational", "technical", "culture_add"]
        target_competencies = competencies
        target_count = count or 5

    questions_per_competency = max(1, target_count // len(target_competencies))

    for comp in target_competencies:
        for qtype in target_types:
            found = get_questions(comp, qtype, level, questions_per_competency)
            guide["questions"].extend(found)
            if len(guide["questions"]) >= target_count:
                break
        if len(guide["questions"]) >= target_count:
            break

    # Trim to target count
    guide["questions"] = guide["questions"][:target_count]
    guide["total_questions"] = len(guide["questions"])
    guide["estimated_duration_minutes"] = len(guide["questions"]) * 10

    return guide


def main():
    parser = argparse.ArgumentParser(
        description="Generate calibrated interview questions with scoring rubrics."
    )
    parser.add_argument("--role", help="Job title (e.g., 'Senior Software Engineer')")
    parser.add_argument("--level", choices=["junior", "mid", "senior"], help="Role level")
    parser.add_argument(
        "--competencies",
        help="Comma-separated competencies: problem_solving,collaboration,leadership,adaptability,technical,culture_add",
    )
    parser.add_argument(
        "--round",
        choices=["phone_screen", "technical", "behavioral", "culture_add", "hiring_manager"],
        help="Interview round (determines question mix)",
    )
    parser.add_argument("--count", type=int, help="Number of questions to generate")
    parser.add_argument("--demo", action="store_true", help="Generate a sample interview guide")
    parser.add_argument("--format", choices=["json", "summary"], default="json", help="Output format")

    args = parser.parse_args()

    if args.demo:
        role = "Senior Backend Engineer"
        level = "senior"
        competencies = ["problem_solving", "collaboration", "leadership", "technical"]
        round_name = "behavioral"
        count = 4
    elif args.role and args.level:
        role = args.role
        level = args.level
        competencies = args.competencies.split(",") if args.competencies else ["problem_solving", "collaboration", "leadership"]
        round_name = args.round
        count = args.count
    else:
        parser.error("Either --demo or --role and --level are required")
        sys.exit(1)

    guide = generate_interview_guide(role, level, competencies, round_name, count)

    if args.format == "summary":
        print(f"=== INTERVIEW GUIDE ===")
        print(f"Role: {guide['role']}")
        print(f"Level: {guide['level']}")
        print(f"Round: {guide['interview_round']}")
        print(f"Questions: {guide['total_questions']}")
        print(f"Estimated Duration: {guide['estimated_duration_minutes']} minutes")
        print()
        for i, q in enumerate(guide["questions"], 1):
            print(f"--- Question {i} ---")
            print(f"Competency: {q['competency']}")
            print(f"Type: {q['type']}")
            print(f"Question: {q['question']}")
            print(f"Follow-up Probes:")
            for probe in q["probes"]:
                print(f"  - {probe}")
            print(f"Scoring Rubric:")
            for score, desc in q["rubric"].items():
                print(f"  {score}: {desc}")
            print()
        print(f"REMINDERS:")
        for reminder in guide["illegal_question_reminders"]:
            print(f"  * {reminder}")
    else:
        print(json.dumps(guide, indent=2))


if __name__ == "__main__":
    main()
