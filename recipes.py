import pandas as pd
import ast
import numpy as np
from sentence_transformers import SentenceTransformer, util
from embedding_store import load_embeddings
from ranker import score_recipe

model = SentenceTransformer("all-MiniLM-L6-v2")

df, embeddings = load_embeddings()



# ================= LOAD & CLEAN DATA =================
def load_recipes():
    df = pd.read_csv("RAW_recipes.csv")

    # Keep only useful columns
    df = df[["name", "minutes", "ingredients"]]

    # Remove weird / missing
    df = df.dropna()
    df = df[df["minutes"] < 240]  # remove extreme recipes

    # Convert ingredients string → list
    def safe_parse(x):
        try:
            return ast.literal_eval(x)
        except:
            return []

    df["ingredients"] = df["ingredients"].apply(safe_parse)

    return df


# ================= STATE-AWARE FILTERING =================
def filter_by_state(df, state: dict):
    """
    Filter recipes based on semantic STATE from ML pipeline.
    """

    # Effort → cooking time
    if state["effort"] == "low":
        df = df[df["minutes"] <= 20]

    elif state["effort"] == "medium":
        df = df[df["minutes"] <= 60]

    # Budget → cheap ingredients heuristic
    if state["budget"] == "low":
        cheap_keywords = ["rice", "egg", "potato", "onion", "dal", "beans"]

        df = df[
            df["ingredients"].apply(
                lambda ing: any(k in str(ing).lower() for k in cheap_keywords)
            )
        ]

    # Nutrition → protein focus
    if state["nutrition"] == "protein":
        protein_keywords = ["chicken", "egg", "paneer", "tofu", "dal", "beans"]

        df = df[
            df["ingredients"].apply(
                lambda ing: any(k in str(ing).lower() for k in protein_keywords)
            )
        ]

    return df


# ================= PUBLIC FUNCTION =================
def get_recipes_from_state(state: dict, user_text: str, top_k=3):
    query_emb = model.encode(user_text, convert_to_tensor=True)

    sims = util.cos_sim(query_emb, embeddings)[0].cpu().numpy()

    scored = []

    for idx, row in df.iterrows():
        final = score_recipe(row, sims[idx], state)
        scored.append((final, row))

    scored.sort(reverse=True, key=lambda x: x[0])

    return [r[1].to_dict() for r in scored[:top_k]]