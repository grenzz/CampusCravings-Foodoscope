# state_builder.py

def pick_label(score_dict, min_confidence=0.05):
    """
    Choose the strongest label from a score dictionary.
    Adds safety when scores are too close.
    """
    sorted_items = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)

    top_label, top_score = sorted_items[0]
    second_score = sorted_items[1][1] if len(sorted_items) > 1 else 0

    # If scores are too close → return neutral
    if abs(top_score - second_score) < min_confidence:
        return "neutral"

    return top_label


def build_state(score_output: dict):
    """
    Convert semantic scorer output → clean decision state.
    """

    state = {}

    # Effort
    state["effort"] = pick_label(score_output["effort_level"])

    # Budget
    state["budget"] = pick_label(score_output["budget_level"])

    # Emotion
    state["emotion"] = pick_label(score_output["emotion_intent"])

    # Nutrition
    state["nutrition"] = pick_label(score_output["nutrition_intent"])

    # Novelty / safety
    state["novelty"] = pick_label(score_output["novelty_level"])

    return state
