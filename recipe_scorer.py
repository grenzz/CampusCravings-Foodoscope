# recipe_scorer.py

import numpy as np
from sentence_transformers import SentenceTransformer, util

# ---------- Load embedding model once ----------
_model = None


def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


# ============================================================
# 1️⃣ Effort score
# ============================================================

def score_effort(recipe, state):
    minutes = recipe["minutes"]

    if state["effort"] == "low":
        return max(0, 1 - minutes / 30)

    if state["effort"] == "medium":
        return 1 - abs(minutes - 30) / 30

    if state["effort"] == "high":
        return min(1, minutes / 60)

    return 0.5


# ============================================================
# 2️⃣ Budget score (proxy = ingredient count)
# ============================================================

def score_budget(recipe, state):
    n_ing = len(recipe["ingredients"])

    if state["budget"] == "low":
        return max(0, 1 - n_ing / 15)

    if state["budget"] == "medium":
        return 1 - abs(n_ing - 10) / 10

    if state["budget"] == "high":
        return min(1, n_ing / 20)

    return 0.5


# ============================================================
# 3️⃣ Nutrition score (simple protein detection)
# ============================================================

PROTEIN_WORDS = ["chicken", "egg", "paneer", "tofu", "dal", "beans", "lentil"]


def score_nutrition(recipe, state):
    ingredients_text = " ".join(recipe["ingredients"]).lower()

    has_protein = any(word in ingredients_text for word in PROTEIN_WORDS)

    if state["nutrition"] == "protein":
        return 1.0 if has_protein else 0.2

    if state["nutrition"] == "fuel":
        return 0.7

    if state["nutrition"] == "balanced":
        return 0.6

    return 0.5


# ============================================================
# 4️⃣ Emotion / comfort score (semantic similarity)
# ============================================================

EMOTION_TEXT = {
    "comfort": "warm comforting emotional home food",
    "mood_lift": "fun tasty exciting enjoyable food",
    "neutral": "regular everyday food"
}

_emotion_embeddings = None


def get_emotion_embeddings():
    global _emotion_embeddings

    if _emotion_embeddings is None:
        model = get_model()
        _emotion_embeddings = {
            k: model.encode(v, convert_to_tensor=True)
            for k, v in EMOTION_TEXT.items()
        }

    return _emotion_embeddings


def score_emotion(recipe, state):
    model = get_model()
    emotion_embeds = get_emotion_embeddings()

    text = recipe["name"]
    recipe_emb = model.encode(text, convert_to_tensor=True)

    target = emotion_embeds.get(state["emotion"], None)
    if target is None:
        return 0.5

    return float(util.cos_sim(recipe_emb, target).item())


# ============================================================
# 5️⃣ Novelty score (ingredient rarity proxy)
# ============================================================

def score_novelty(recipe, state):
    n_ing = len(recipe["ingredients"])

    if state["novelty"] == "safe":
        return max(0, 1 - n_ing / 15)

    if state["novelty"] == "variation":
        return 1 - abs(n_ing - 12) / 12

    if state["novelty"] == "experimental":
        return min(1, n_ing / 20)

    return 0.5


# ============================================================
# 6️⃣ Final weighted score
# ============================================================

WEIGHTS = {
    "effort": 0.25,
    "budget": 0.15,
    "nutrition": 0.25,
    "emotion": 0.20,
    "novelty": 0.15,
}


def score_recipe(recipe, state):
    scores = {
        "effort": score_effort(recipe, state),
        "budget": score_budget(recipe, state),
        "nutrition": score_nutrition(recipe, state),
        "emotion": score_emotion(recipe, state),
        "novelty": score_novelty(recipe, state),
    }

    final = sum(scores[k] * WEIGHTS[k] for k in scores)

    return final, scores
