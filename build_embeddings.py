import torch
from sentence_transformers import SentenceTransformer
import pickle
from data_loader import load_recipes

MODEL_NAME = "all-MiniLM-L6-v2"
EMBED_PATH = "recipe_embeddings.pkl"

# ---------------------------
# 🔥 Detect GPU automatically
# ---------------------------
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

model = SentenceTransformer(MODEL_NAME, device=device)

# ---------------------------
# Load dataset
# ---------------------------
df = load_recipes()

texts = df["text"].tolist()

# ---------------------------
# 🚀 Fast encoding
# ---------------------------
embeddings = model.encode(
    texts,
    batch_size=256,                # 🚀 GPU optimized
    show_progress_bar=True,
    convert_to_numpy=True,         # faster storage
    normalize_embeddings=True      # faster cosine later
)

# ---------------------------
# Save
# ---------------------------
with open(EMBED_PATH, "wb") as f:
    pickle.dump((df, embeddings), f)

print("Embeddings built successfully.")

 