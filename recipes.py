import pandas as pd
import ast


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
def get_recipes_from_state(state: dict, top_k: int = 3):
    """
    Main entry used by Streamlit app.
    Returns top_k recipe names.
    """

    df = load_recipes()
    df = filter_by_state(df, state)

    # Fallback if too strict filtering
    if len(df) == 0:
        df = load_recipes().head(50)

    return df.head(top_k).to_dict("records")
