import numpy as np
import pickle
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("recipe_embeddings.pkl", "rb") as f:
    df, embeddings = pickle.load(f)

def retrieve(user_text, top_k=30):
    query_emb = model.encode(user_text, convert_to_tensor=True)

    scores = util.cos_sim(query_emb, embeddings)[0].cpu().numpy()

    idx = np.argsort(scores)[-top_k:][::-1]

    return df.iloc[idx], scores[idx]
