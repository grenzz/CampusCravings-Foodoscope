from sentence_transformers import SentenceTransformer
import pickle
from data_loader import load_recipes

model = SentenceTransformer("all-MiniLM-L6-v2")

df = load_recipes()

embeddings = model.encode(df["text"].tolist(), show_progress_bar=True)

with open("recipe_embeddings.pkl", "wb") as f:
    pickle.dump((df, embeddings), f)

print("Embeddings built.")
 