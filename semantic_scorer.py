from sentence_transformers import SentenceTransformer, util
from state_schema import DIMENSIONS


# ================= LOAD MODEL =================

_model = None
_dimension_centroids = {}


def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


# ================= BUILD CENTROID EMBEDDINGS =================

def build_dimension_centroids():
    """
    For each label:
    embed all example sentences + description
    average them → centroid vector
    """
    global _dimension_centroids

    model = get_model()

    for dim, options in DIMENSIONS.items():
        _dimension_centroids[dim] = {}

        for option, data in options.items():
            texts = [data["description"]] + data["examples"]

            embeddings = model.encode(texts, convert_to_tensor=True)

            # Mean pooling → centroid
            centroid = embeddings.mean(dim=0)

            _dimension_centroids[dim][option] = centroid


# Build once at import
build_dimension_centroids()


# ================= SCORE USER TEXT =================

def score_user_text(user_text: str):
    """
    Compare user text embedding against centroid of each label.
    Returns similarity scores.
    """
    model = get_model()
    user_emb = model.encode(user_text, convert_to_tensor=True)

    scores = {}

    for dim, options in _dimension_centroids.items():
        scores[dim] = {}

        for option, centroid in options.items():
            sim = util.cos_sim(user_emb, centroid).item()
            scores[dim][option] = float(sim)

    return scores
