# recipe_details.py

from embedding_store import load_embeddings
from sentence_transformers import SentenceTransformer, util
import torch

df, embeddings = load_embeddings()

model = SentenceTransformer("all-MiniLM-L6-v2")


def extract_recipe_query(user_text):
    """
    Remove filler words and keep only likely recipe query.
    """
    text = user_text.lower()

    patterns = [
        "give me more details of",
        "give me details of",
        "details of",
        "show me details of",
        "recipe of",
        "how to make",
        "tell me about",
        "give details of"
    ]

    for p in patterns:
        text = text.replace(p, "")

    return text.strip()


def get_recipe_details(user_text, last_recipes=None):
    query = extract_recipe_query(user_text)

    if not query:
        return None

    # ----------------------------------
    # STEP 1: If last recipes exist,
    # find best matching NAME only
    # ----------------------------------
    selected_name = None

    if last_recipes:
        names = [r["name"] for r in last_recipes]

        name_embeddings = model.encode(names, convert_to_tensor=True)
        query_emb = model.encode(query, convert_to_tensor=True)

        sims = util.cos_sim(query_emb, name_embeddings)[0]
        best_idx = sims.argmax().item()
        best_score = sims[best_idx].item()

        if best_score > 0.5:
            selected_name = names[best_idx]

    # ----------------------------------
    # STEP 2: Always fetch CLEAN row from df
    # ----------------------------------
    if selected_name:
        matches = df[df["name"] == selected_name]
    else:
        matches = df[
            df["name"].str.lower().str.contains(query, na=False)
        ]

    if matches.empty:
        return None

    row = matches.iloc[0].to_dict()

    # Ensure steps are list
    if isinstance(row["steps"], str):
        import ast
        try:
            row["steps"] = ast.literal_eval(row["steps"])
        except:
            row["steps"] = [row["steps"]]

    return row
