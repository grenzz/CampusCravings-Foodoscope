# scorer.py
# This is a clean bridge between semantic scorer and the rest of the system.

from semantic_scorer import score_user_text


def score_query(text: str):
    """
    Public function used by test_state.py and future pipeline.
    Simply forwards to semantic scorer.
    """
    return score_user_text(text)


# Optional local test
if __name__ == "__main__":
    print(score_query("I am tired and broke and want comfort food"))
