# intent_classifier.py

import re

def detect_intent(user_text: str):
    text = user_text.lower()

    # Recipe detail intent
    detail_patterns = [
        "details of",
        "show details",
        "recipe of",
        "how to make",
        "ingredients of",
        "steps of",
        "tell me about"
    ]

    for pattern in detail_patterns:
        if pattern in text:
            return "recipe_detail"

    # General recommendation intent
    recommendation_patterns = [
        "suggest",
        "recommend",
        "what should i eat",
        "hungry",
        "craving",
        "want something"
    ]

    for pattern in recommendation_patterns:
        if pattern in text:
            return "recommendation"

    # Default
    return "recommendation"
