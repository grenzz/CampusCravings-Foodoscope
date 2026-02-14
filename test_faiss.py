from scorer import score_query
from state_builder import build_state
from recipes import get_recipes_from_state


print("\n=== FAISS PIPELINE TEST ===\n")

# Test input
user_text = "I want something healthy but still tasty and satisfying"


print("INPUT:")
print(user_text)

# 1️⃣ Semantic scoring
scores = score_query(user_text)

print("\nSTATE SCORES:")
for dim, vals in scores.items():
    print(dim, ":", {k: round(v, 3) for k, v in vals.items()})

# 2️⃣ Build state
state = build_state(scores)

print("\nFINAL STATE:")
print(state)

# 3️⃣ FAISS retrieval + ranking
recipes = get_recipes_from_state(state, user_text, top_k=5)

print("\nTOP RECIPES:")
for r in recipes:
    print("-", r["name"])

print("\n=== TEST COMPLETE ===\n")
