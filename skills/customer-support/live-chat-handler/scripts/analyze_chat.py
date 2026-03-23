#!/usr/bin/env python3
"""
Analyze chat conversation for sentiment, urgency, and key metrics.

Usage:
    python analyze_chat.py chat_log.txt
    python analyze_chat.py chat_log.txt --format summary

Output: Analysis of chat conversation with actionable insights
"""

import argparse
import json
import re
import sys
from datetime import datetime


# Sentiment indicators
POSITIVE_WORDS = [
    'thank', 'thanks', 'great', 'awesome', 'perfect', 'excellent', 'amazing',
    'helpful', 'appreciate', 'wonderful', 'fantastic', 'love', 'happy', 'good'
]

NEGATIVE_WORDS = [
    'frustrated', 'angry', 'upset', 'terrible', 'awful', 'horrible', 'worst',
    'disappointed', 'unacceptable', 'ridiculous', 'stupid', 'hate', 'bad',
    'annoyed', 'furious', 'disgusted', 'pathetic', 'useless'
]

URGENT_WORDS = [
    'urgent', 'emergency', 'asap', 'immediately', 'critical', 'now', 'hurry',
    'deadline', 'time-sensitive', 'crucial', 'important', 'right away'
]

ESCALATION_TRIGGERS = [
    'manager', 'supervisor', 'cancel', 'refund', 'lawyer', 'legal', 'sue',
    'report', 'complaint', 'bbb', 'review', 'social media', 'twitter'
]


def parse_chat_log(content):
    """Parse chat log into messages."""
    messages = []

    # Common chat log patterns
    patterns = [
        # [timestamp] Agent: message
        r'\[([^\]]+)\]\s*(Agent|Customer|[^:]+):\s*(.+)',
        # timestamp - Agent: message
        r'(\d{1,2}:\d{2}(?::\d{2})?(?:\s*[AP]M)?)\s*-?\s*(Agent|Customer|[^:]+):\s*(.+)',
        # Agent: message (no timestamp)
        r'^(Agent|Customer):\s*(.+)',
    ]

    lines = content.strip().split('\n')

    for line in lines:
        line = line.strip()
        if not line:
            continue

        for pattern in patterns:
            match = re.match(pattern, line, re.IGNORECASE)
            if match:
                groups = match.groups()
                if len(groups) == 3:
                    timestamp, speaker, message = groups
                else:
                    timestamp = None
                    speaker, message = groups

                speaker_type = 'agent' if 'agent' in speaker.lower() else 'customer'
                messages.append({
                    'timestamp': timestamp,
                    'speaker': speaker_type,
                    'message': message.strip()
                })
                break
        else:
            # If no pattern matched, try to append to previous message
            if messages:
                messages[-1]['message'] += ' ' + line

    return messages


def analyze_sentiment(messages):
    """Analyze overall sentiment of the conversation."""
    customer_messages = [m['message'].lower() for m in messages if m['speaker'] == 'customer']
    all_customer_text = ' '.join(customer_messages)

    positive_count = sum(1 for word in POSITIVE_WORDS if word in all_customer_text)
    negative_count = sum(1 for word in NEGATIVE_WORDS if word in all_customer_text)

    # Calculate sentiment score (-100 to +100)
    total = positive_count + negative_count
    if total == 0:
        score = 0
    else:
        score = ((positive_count - negative_count) / total) * 100

    # Determine sentiment label
    if score >= 30:
        label = 'positive'
    elif score <= -30:
        label = 'negative'
    else:
        label = 'neutral'

    # Check for sentiment shift
    first_half = customer_messages[:len(customer_messages)//2]
    second_half = customer_messages[len(customer_messages)//2:]

    first_negative = sum(1 for msg in first_half for word in NEGATIVE_WORDS if word in msg)
    second_negative = sum(1 for msg in second_half for word in NEGATIVE_WORDS if word in msg)

    if first_negative > second_negative + 2:
        trend = 'improving'
    elif second_negative > first_negative + 2:
        trend = 'deteriorating'
    else:
        trend = 'stable'

    return {
        'score': round(score, 1),
        'label': label,
        'trend': trend,
        'positive_indicators': positive_count,
        'negative_indicators': negative_count
    }


def analyze_urgency(messages):
    """Analyze urgency level of the conversation."""
    customer_messages = [m['message'].lower() for m in messages if m['speaker'] == 'customer']
    all_customer_text = ' '.join(customer_messages)

    urgent_count = sum(1 for word in URGENT_WORDS if word in all_customer_text)

    # Check for urgency patterns
    has_caps = any(msg.isupper() and len(msg) > 5 for msg in customer_messages)
    has_exclamations = sum(msg.count('!') for msg in customer_messages) > 3
    has_questions = sum(msg.count('?') for msg in customer_messages) > 5

    # Calculate urgency score
    urgency_score = urgent_count * 20
    if has_caps:
        urgency_score += 30
    if has_exclamations:
        urgency_score += 20

    urgency_score = min(100, urgency_score)

    if urgency_score >= 70:
        level = 'high'
    elif urgency_score >= 40:
        level = 'medium'
    else:
        level = 'low'

    return {
        'score': urgency_score,
        'level': level,
        'indicators': {
            'urgent_words': urgent_count,
            'caps_usage': has_caps,
            'excessive_punctuation': has_exclamations
        }
    }


def detect_escalation_risk(messages):
    """Detect risk of escalation."""
    customer_messages = [m['message'].lower() for m in messages if m['speaker'] == 'customer']
    all_customer_text = ' '.join(customer_messages)

    triggers_found = [trigger for trigger in ESCALATION_TRIGGERS if trigger in all_customer_text]

    risk_score = len(triggers_found) * 25
    risk_score = min(100, risk_score)

    if risk_score >= 50:
        level = 'high'
    elif risk_score >= 25:
        level = 'medium'
    else:
        level = 'low'

    return {
        'score': risk_score,
        'level': level,
        'triggers_found': triggers_found
    }


def calculate_metrics(messages):
    """Calculate conversation metrics."""
    customer_messages = [m for m in messages if m['speaker'] == 'customer']
    agent_messages = [m for m in messages if m['speaker'] == 'agent']

    # Message counts
    total_messages = len(messages)
    customer_count = len(customer_messages)
    agent_count = len(agent_messages)

    # Average message length
    customer_avg_length = (
        sum(len(m['message'].split()) for m in customer_messages) / customer_count
        if customer_count else 0
    )
    agent_avg_length = (
        sum(len(m['message'].split()) for m in agent_messages) / agent_count
        if agent_count else 0
    )

    # Response ratio
    response_ratio = agent_count / customer_count if customer_count else 0

    return {
        'total_messages': total_messages,
        'customer_messages': customer_count,
        'agent_messages': agent_count,
        'customer_avg_word_count': round(customer_avg_length, 1),
        'agent_avg_word_count': round(agent_avg_length, 1),
        'response_ratio': round(response_ratio, 2)
    }


def extract_key_issues(messages):
    """Extract potential key issues from the conversation."""
    customer_messages = [m['message'] for m in messages if m['speaker'] == 'customer']

    issues = []

    # Common issue patterns
    issue_patterns = [
        (r"can'?t\s+(\w+)", "Unable to {0}"),
        (r"doesn'?t?\s+work", "Feature not working"),
        (r"not\s+working", "Feature not working"),
        (r"error", "Error encountered"),
        (r"charged\s+(?:twice|double|wrong)", "Billing issue"),
        (r"refund", "Refund requested"),
        (r"cancel", "Cancellation request"),
        (r"password", "Password/Login issue"),
        (r"slow", "Performance issue"),
        (r"bug", "Bug reported"),
    ]

    for msg in customer_messages:
        msg_lower = msg.lower()
        for pattern, issue_type in issue_patterns:
            if re.search(pattern, msg_lower):
                if issue_type not in issues:
                    issues.append(issue_type)

    return issues[:5]  # Top 5 issues


def generate_recommendations(sentiment, urgency, escalation_risk, issues):
    """Generate actionable recommendations."""
    recommendations = []

    if sentiment['label'] == 'negative':
        recommendations.append({
            'priority': 'high',
            'action': 'Address customer frustration with empathy',
            'reason': 'Negative sentiment detected'
        })

    if urgency['level'] == 'high':
        recommendations.append({
            'priority': 'high',
            'action': 'Prioritize immediate resolution',
            'reason': 'High urgency indicated by customer'
        })

    if escalation_risk['level'] == 'high':
        recommendations.append({
            'priority': 'high',
            'action': 'Consider proactive supervisor involvement',
            'reason': f"Escalation triggers detected: {', '.join(escalation_risk['triggers_found'])}"
        })

    if 'Refund requested' in issues:
        recommendations.append({
            'priority': 'medium',
            'action': 'Review refund policy and customer history',
            'reason': 'Refund request detected'
        })

    if sentiment['trend'] == 'deteriorating':
        recommendations.append({
            'priority': 'high',
            'action': 'Change approach - current strategy not working',
            'reason': 'Customer sentiment getting worse'
        })

    if not recommendations:
        recommendations.append({
            'priority': 'low',
            'action': 'Continue current approach',
            'reason': 'Conversation progressing normally'
        })

    return recommendations


def analyze_chat(content):
    """Perform complete chat analysis."""
    messages = parse_chat_log(content)

    if not messages:
        return {'error': 'No messages could be parsed from the chat log'}

    sentiment = analyze_sentiment(messages)
    urgency = analyze_urgency(messages)
    escalation_risk = detect_escalation_risk(messages)
    metrics = calculate_metrics(messages)
    issues = extract_key_issues(messages)
    recommendations = generate_recommendations(sentiment, urgency, escalation_risk, issues)

    return {
        'summary': {
            'sentiment': sentiment['label'],
            'urgency': urgency['level'],
            'escalation_risk': escalation_risk['level'],
            'message_count': metrics['total_messages']
        },
        'sentiment_analysis': sentiment,
        'urgency_analysis': urgency,
        'escalation_risk': escalation_risk,
        'metrics': metrics,
        'key_issues': issues,
        'recommendations': recommendations
    }


def main():
    parser = argparse.ArgumentParser(description='Analyze chat conversation')
    parser.add_argument('file', help='Chat log file to analyze')
    parser.add_argument('--format', '-f', choices=['json', 'summary'],
                        default='json', help='Output format')

    args = parser.parse_args()

    try:
        with open(args.file, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(json.dumps({'error': f'File not found: {args.file}'}))
        sys.exit(1)

    result = analyze_chat(content)

    if args.format == 'summary':
        print('\n=== Chat Analysis ===\n')
        print(f"Sentiment: {result['summary']['sentiment'].upper()}")
        print(f"Urgency: {result['summary']['urgency'].upper()}")
        print(f"Escalation Risk: {result['summary']['escalation_risk'].upper()}")
        print(f"Messages: {result['summary']['message_count']}")

        if result['key_issues']:
            print(f"\nKey Issues Detected:")
            for issue in result['key_issues']:
                print(f"  • {issue}")

        print(f"\nRecommendations:")
        for rec in result['recommendations']:
            print(f"  [{rec['priority'].upper()}] {rec['action']}")
    else:
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
