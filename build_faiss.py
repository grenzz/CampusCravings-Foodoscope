import pandas as pd
import ast
import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer


# ================= LOAD & CLEAN =================
def load_recipes():
    print("Loading CSV...")
    df = pd.read_csv("RAW_recipes.csv")

    df = df[["name", "minutes", "ingredients"]]
    df = df.dropna()
    df = df[df["minutes"] < 240]

    def safe_parse(x):
        try:
            return ast.literal_eval(x)
        except:
            return []

    print("Parsing ingredients...")
    df["ingredients"] = df["ingredients"].apply(safe_parse)

    print("Recipes loaded:", len(df))
    return df


# ================= BUILD TEXT FOR EMBEDDING =================
def recipe_to_text(row):
    ingredients = ", ".join(row["ingredients"])
    minutes = row["minutes"]

    return f"""
    Recipe: {row['name']}.
    Cooking time: {minutes} minutes.
    Ingredients: {ingredients}.
    This is a simple home-style student meal.
    """



# ================= MAIN =================
def main():
    df = load_recipes()

    print("Loading embedding model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("Creating recipe texts...")
    texts = df.apply(recipe_to_text, axis=1).tolist()

    print("Encoding recipes (this takes a few minutes ONCE)...")
    embeddings = model.encode(texts, show_progress_bar=True, batch_size=64)

    embeddings = np.array(embeddings).astype("float32")

    print("Building FAISS index...")
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    print("Saving index + metadata...")

    faiss.write_index(index, "recipes.index")

    with open("recipes_meta.pkl", "wb") as f:
        pickle.dump(df.to_dict("records"), f)

    print("✅ FAISS build complete!")
    print("You never run this again unless dataset changes.")


if __name__ == "__main__":
    main()
