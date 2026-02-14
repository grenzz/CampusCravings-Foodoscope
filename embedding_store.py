import pandas as pd
import ast
import pickle
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"
EMBED_PATH = "recipe_embeddings.pkl"

model = SentenceTransformer(MODEL_NAME)


def load_full_recipes():
    df = pd.read_csv("RAW_recipes.csv")

    df = df[["name", "minutes", "ingredients"]].dropna()

    def safe_parse(x):
        try:
            return ast.literal_eval(x)
        except:
            return []

    df["ingredients"] = df["ingredients"].apply(safe_parse)

    df["text"] = df.apply(
        lambda r: r["name"] + " " + " ".join(r["ingredients"]),
        axis=1
    )

    return df


def build_embeddings():
    df = load_full_recipes()
    embeddings = model.encode(df["text"].tolist(), show_progress_bar=True)

    with open(EMBED_PATH, "wb") as f:
        pickle.dump((df, embeddings), f)


def load_embeddings():
    with open(EMBED_PATH, "rb") as f:
        return pickle.load(f)
