from scorer import score_query
from state_builder import build_state

text = "I have no money and I just want the cheapest filling food"




scores = score_query(text)
state = build_state(scores)

print("SCORES:\n", scores)
print("\nSTATE:\n", state)
