from semantic_scorer import score_user_text
from state_builder import build_state
from recipes import get_recipes_from_state

print("TEST STARTED")

# ---------- TEST INPUT ----------
text = "I am exhausted, broke, and want comforting protein food"

print("\nINPUT:")
print(text)


# ---------- STEP 1: semantic scores ----------
scores = score_user_text(text)

print("\nSTATE SCORES:")
for dim, vals in scores.items():
    print(dim, ":", {k: round(v, 3) for k, v in vals.items()})


# ---------- STEP 2: build state ----------
state = build_state(scores)

print("\nFINAL STATE:")
print(state)


# ---------- STEP 3: get recipes ----------
recipes = get_recipes_from_state(state, top_k=5)

print("\nTOP RECIPES:")
for r in recipes:
    print("-", r["name"])
from recipes import get_recipes_from_state

print("\nGETTING RECIPES...")
recipes = get_recipes_from_state(state, top_k=3)

print("\nRECIPES RESULT:")
print(recipes)
