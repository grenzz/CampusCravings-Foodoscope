import faiss
import pickle
import numpy as np

from sentence_transformers import SentenceTransformer
from recipe_scorer import score_recipe


# ================= LOAD FAISS + METADATA =================

_index = None
_recipes = None
_model = None


def load_faiss():
    global _index, _recipes, _model

    if _index is None:
        print("Loading FAISS index...")
        _index = faiss.read_index("recipes.index")

        print("Loading recipe metadata...")
        with open("recipes_meta.pkl", "rb") as f:
            _recipes = pickle.load(f)

        print("Loading embedding model...")
        _model = SentenceTransformer("all-MiniLM-L6-v2")

        print("FAISS system ready!")

    return _index, _recipes, _model


# ================= FAST SEMANTIC RETRIEVAL =================

def retrieve_candidates(user_text: str, k: int = 200):
    """
    Use FAISS to get top-k semantically similar recipes.
    """

    index, recipes, model = load_faiss()

    query_vec = model.encode([user_text])
    query_vec = np.array(query_vec).astype("float32")

    distances, indices = index.search(query_vec, k)

    candidates = [recipes[i] for i in indices[0]]
    return candidates


# ================= FINAL RANKING =================

def get_recipes_from_state(state: dict, user_text: str, top_k: int = 3):
    """
    Full hybrid pipeline:
    FAISS retrieval → deep scoring → best recipes
    """

    candidates = retrieve_candidates(user_text, k=200)

    scored = []

    for recipe in candidates:
        final_score, _ = score_recipe(recipe, state)
        scored.append((final_score, recipe))

    scored.sort(key=lambda x: x[0], reverse=True)

    return [r for _, r in scored[:top_k]]
