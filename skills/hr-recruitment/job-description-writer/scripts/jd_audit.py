#!/usr/bin/env python3
"""
Job Description Audit Tool

Analyzes a job description for inclusive language, structure completeness,
readability, and SEO optimization. Outputs a JSON report with scores and
specific improvement recommendations.

Usage:
    python jd_audit.py --file job_description.txt
    python jd_audit.py --text "Your job description text here"
    python jd_audit.py --demo
"""

import argparse
import json
import re
import sys
from collections import defaultdict

# --- Inclusive Language Database ---

MASCULINE_CODED_WORDS = [
    "aggressive", "ambitious", "analytical", "assertive", "autonomous",
    "boast", "challenge", "champion", "competitive", "confident",
    "courageous", "decide", "decisive", "defend", "determined",
    "direct", "dominant", "dominate", "driven", "fearless",
    "fight", "force", "head", "headstrong", "hierarchy",
    "hostile", "impulsive", "independent", "individual", "intellectual",
    "lead", "logic", "ninja", "objective", "opinion",
    "outspoken", "persist", "principle", "reckless", "rockstar",
    "self-confident", "self-reliant", "self-sufficient", "strong", "stubborn",
    "superior", "tackle", "unreasonable", "warrior",
]

FEMININE_CODED_WORDS = [
    "agree", "affectionate", "caring", "collaborate", "committed",
    "communal", "compassionate", "connect", "considerate", "cooperative",
    "dependable", "emotional", "empathetic", "enthusiastic", "feeling",
    "gentle", "honest", "inclusive", "interpersonal", "kind",
    "kinship", "loyal", "modest", "nurture", "pleasant",
    "polite", "quiet", "responsible", "share", "submissive",
    "support", "sympathetic", "tender", "together", "trust",
    "understand", "warm", "wholeheartedly", "yield",
]

EXCLUSIONARY_TERMS = {
    "rockstar": "experienced professional",
    "ninja": "skilled specialist",
    "guru": "expert",
    "wizard": "specialist",
    "hacker": "engineer",
    "young and energetic": "motivated and enthusiastic",
    "digital native": "comfortable with technology",
    "culture fit": "culture add",
    "manpower": "workforce",
    "man-hours": "person-hours",
    "he/she": "they",
    "his/her": "their",
    "native english speaker": "fluent in English",
    "able-bodied": "[describe actual requirement]",
}

REQUIRED_SECTIONS = [
    "job title",
    "about",
    "responsibilities",
    "requirements",
    "compensation",
    "benefits",
    "equal opportunity",
]

SECTION_PATTERNS = {
    "job title": r"^#|^##|title",
    "about": r"about\s+(us|the\s+company|\[)|who\s+we\s+are|our\s+company",
    "responsibilities": r"responsibilit|what\s+you.*(do|will)|your\s+role|key\s+duties",
    "requirements": r"requirement|qualifi|what\s+we.*(look|need|seek)|must.have|you.*(have|bring)",
    "compensation": r"compensation|salary|pay\s+range|\$\d",
    "benefits": r"benefit|perk|what\s+we\s+offer|we\s+offer|total\s+rewards",
    "equal opportunity": r"equal\s+opportunity|eeo|eoe|inclusive\s+environment|do\s+not\s+discriminate",
}


def count_requirements(text):
    """Count the number of bullet-point requirements."""
    requirement_section = False
    requirement_bullets = 0
    for line in text.split("\n"):
        lower = line.lower().strip()
        if re.search(SECTION_PATTERNS["requirements"], lower):
            requirement_section = True
            continue
        if requirement_section:
            if re.match(r"^[-*\u2022]\s+", line.strip()) or re.match(r"^\d+[.)]\s+", line.strip()):
                requirement_bullets += 1
            elif re.search(r"^#{1,3}\s+", line.strip()) and not re.search(SECTION_PATTERNS["requirements"], lower):
                requirement_section = False
    return requirement_bullets


def calculate_readability(text):
    """Estimate Flesch-Kincaid grade level."""
    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 5]
    words = re.findall(r"\b[a-zA-Z]+\b", text)

    if not sentences or not words:
        return {"grade_level": 0, "score": 0}

    syllable_count = 0
    for word in words:
        word = word.lower()
        count = 0
        vowels = "aeiou"
        if word[0] in vowels:
            count += 1
        for i in range(1, len(word)):
            if word[i] in vowels and word[i - 1] not in vowels:
                count += 1
        if word.endswith("e"):
            count -= 1
        if count == 0:
            count = 1
        syllable_count += count

    avg_sentence_length = len(words) / len(sentences)
    avg_syllables_per_word = syllable_count / len(words)

    flesch_score = 206.835 - 1.015 * avg_sentence_length - 84.6 * avg_syllables_per_word
    grade_level = 0.39 * avg_sentence_length + 11.8 * avg_syllables_per_word - 15.59

    return {
        "flesch_score": round(max(0, min(100, flesch_score)), 1),
        "grade_level": round(max(0, grade_level), 1),
        "word_count": len(words),
        "sentence_count": len(sentences),
    }


def find_gendered_language(text):
    """Detect masculine and feminine coded words."""
    lower_text = text.lower()
    words_in_text = set(re.findall(r"\b[a-z]+\b", lower_text))

    masculine_found = [w for w in MASCULINE_CODED_WORDS if w in words_in_text]
    feminine_found = [w for w in FEMININE_CODED_WORDS if w in words_in_text]

    if len(masculine_found) > len(feminine_found) + 3:
        bias = "masculine-leaning"
    elif len(feminine_found) > len(masculine_found) + 3:
        bias = "feminine-leaning"
    else:
        bias = "balanced"

    return {
        "masculine_coded": masculine_found,
        "feminine_coded": feminine_found,
        "masculine_count": len(masculine_found),
        "feminine_count": len(feminine_found),
        "bias_assessment": bias,
    }


def find_exclusionary_terms(text):
    """Find exclusionary terms and suggest replacements."""
    lower_text = text.lower()
    found = []
    for term, replacement in EXCLUSIONARY_TERMS.items():
        if term in lower_text:
            found.append({"term": term, "replacement": replacement})
    return found


def check_sections(text):
    """Check which required sections are present."""
    lower_text = text.lower()
    results = {}
    for section, pattern in SECTION_PATTERNS.items():
        results[section] = bool(re.search(pattern, lower_text))
    return results


def check_salary_included(text):
    """Check if salary/compensation range is included."""
    return bool(re.search(r"\$[\d,]+\s*[-–]\s*\$[\d,]+|\$[\d,]+k?\s*[-–]\s*\$?[\d,]+k?", text, re.IGNORECASE))


def audit_jd(text):
    """Run a full audit on a job description."""
    results = {
        "structure": {},
        "inclusivity": {},
        "readability": {},
        "seo": {},
        "overall_score": 0,
        "recommendations": [],
    }

    # Structure check
    sections = check_sections(text)
    sections_present = sum(1 for v in sections.values() if v)
    sections_total = len(REQUIRED_SECTIONS)
    results["structure"]["sections"] = sections
    results["structure"]["completeness"] = f"{sections_present}/{sections_total}"
    results["structure"]["score"] = round(sections_present / sections_total * 100)

    for section, present in sections.items():
        if not present:
            results["recommendations"].append({
                "category": "structure",
                "severity": "high",
                "message": f"Missing section: {section}. Add this section to improve the JD.",
            })

    # Requirements count
    req_count = count_requirements(text)
    results["structure"]["requirement_count"] = req_count
    if req_count > 8:
        results["recommendations"].append({
            "category": "structure",
            "severity": "high",
            "message": f"Too many requirements listed ({req_count}). Cap at 6-8 must-haves. Research shows long requirement lists deter qualified candidates, especially women.",
        })
    elif req_count == 0:
        results["recommendations"].append({
            "category": "structure",
            "severity": "medium",
            "message": "Could not detect bullet-point requirements. Ensure requirements are clearly listed with bullet points.",
        })

    # Inclusivity check
    gendered = find_gendered_language(text)
    exclusionary = find_exclusionary_terms(text)
    results["inclusivity"]["gendered_language"] = gendered
    results["inclusivity"]["exclusionary_terms"] = exclusionary

    inclusivity_score = 100
    if gendered["bias_assessment"] == "masculine-leaning":
        inclusivity_score -= 20
        results["recommendations"].append({
            "category": "inclusivity",
            "severity": "high",
            "message": f"JD is masculine-coded ({gendered['masculine_count']} masculine vs {gendered['feminine_count']} feminine words). This may reduce female applicants by up to 30%. Replace: {', '.join(gendered['masculine_coded'][:5])}",
        })

    for term in exclusionary:
        inclusivity_score -= 10
        results["recommendations"].append({
            "category": "inclusivity",
            "severity": "medium",
            "message": f"Replace '{term['term']}' with '{term['replacement']}'",
        })

    results["inclusivity"]["score"] = max(0, inclusivity_score)

    # Readability
    readability = calculate_readability(text)
    results["readability"] = readability

    if readability["grade_level"] > 12:
        readability_score = 40
        results["recommendations"].append({
            "category": "readability",
            "severity": "high",
            "message": f"Reading level is grade {readability['grade_level']}. Target grade 8-10 for maximum accessibility. Use shorter sentences and simpler words.",
        })
    elif readability["grade_level"] > 10:
        readability_score = 70
        results["recommendations"].append({
            "category": "readability",
            "severity": "medium",
            "message": f"Reading level is grade {readability['grade_level']}. Consider simplifying to grade 8-10.",
        })
    else:
        readability_score = 100

    results["readability"]["score"] = readability_score

    # SEO check
    salary_included = check_salary_included(text)
    results["seo"]["salary_range_included"] = salary_included
    seo_score = 50

    if salary_included:
        seo_score += 25
    else:
        results["recommendations"].append({
            "category": "seo",
            "severity": "high",
            "message": "No salary range detected. Including compensation improves apply rates by 30% and is required by law in many jurisdictions.",
        })

    if sections.get("job title"):
        seo_score += 25

    results["seo"]["score"] = seo_score

    # Overall score (weighted)
    results["overall_score"] = round(
        results["structure"]["score"] * 0.30
        + results["inclusivity"]["score"] * 0.30
        + readability_score * 0.20
        + seo_score * 0.20
    )

    # Sort recommendations by severity
    severity_order = {"high": 0, "medium": 1, "low": 2}
    results["recommendations"].sort(key=lambda x: severity_order.get(x["severity"], 3))

    return results


DEMO_JD = """
# Senior Software Engineer - Backend

## About Us
TechCorp is a fast-growing SaaS company building the future of project management.
Founded in 2019, we serve over 10,000 teams globally. Our 150-person team is driven
by innovation and customer obsession.

## The Opportunity
We're looking for a rockstar backend engineer to join our platform team. You'll
build scalable microservices and lead architecture decisions for our core product.

## What You'll Do
- Design and build high-performance APIs and microservices
- Lead technical design reviews and mentor junior engineers
- Own the reliability and scalability of core platform services
- Collaborate with product and frontend teams
- Drive best practices for testing, monitoring, and deployment

## Requirements
- 5+ years of backend development experience
- Must have a BS in Computer Science from a top university
- Expert-level proficiency in Go or Java
- Strong experience with AWS, Kubernetes, and PostgreSQL
- Experience with microservices architecture at scale
- Excellent problem-solving skills
- Strong communication skills
- Experience with CI/CD pipelines
- Familiarity with agile development methodologies
- Must be a self-starter who can work independently
- Native English speaker
- Young and energetic team player

## Nice to Have
- Experience with event-driven architecture
- Knowledge of GraphQL
- Open-source contributions

## Benefits
- Competitive salary
- Health, dental, and vision insurance
- 401(k) with match
- Unlimited PTO
- Remote-friendly
"""


def main():
    parser = argparse.ArgumentParser(
        description="Audit a job description for inclusivity, structure, readability, and SEO."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", help="Path to a text file containing the job description")
    group.add_argument("--text", help="Job description text as a string")
    group.add_argument("--demo", action="store_true", help="Run audit on a sample job description")
    parser.add_argument("--format", choices=["json", "summary"], default="json", help="Output format (default: json)")

    args = parser.parse_args()

    if args.demo:
        text = DEMO_JD
    elif args.file:
        try:
            with open(args.file, "r") as f:
                text = f.read()
        except FileNotFoundError:
            print(json.dumps({"error": f"File not found: {args.file}"}))
            sys.exit(1)
    else:
        text = args.text

    results = audit_jd(text)

    if args.format == "summary":
        print(f"=== JD AUDIT REPORT ===")
        print(f"Overall Score: {results['overall_score']}/100")
        print(f"")
        print(f"Structure:    {results['structure']['score']}/100 ({results['structure']['completeness']} sections)")
        print(f"Inclusivity:  {results['inclusivity']['score']}/100 (Bias: {results['inclusivity']['gendered_language']['bias_assessment']})")
        print(f"Readability:  {results['readability']['score']}/100 (Grade {results['readability']['grade_level']})")
        print(f"SEO:          {results['seo']['score']}/100 (Salary: {'Yes' if results['seo']['salary_range_included'] else 'No'})")
        print(f"")
        print(f"Recommendations ({len(results['recommendations'])}):")
        for i, rec in enumerate(results["recommendations"], 1):
            severity = rec["severity"].upper()
            print(f"  {i}. [{severity}] {rec['message']}")
    else:
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
