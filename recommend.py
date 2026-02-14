from retriever import retrieve
from ranker import final_score

def recommend(user_text, state, top_k=5):
    df, sims = retrieve(user_text)

    scored = []

    # FIX: use enumerate
    for idx, (_, row) in enumerate(df.iterrows()):
        s = final_score(row, sims[idx], state)
        scored.append((s, row))

    scored.sort(reverse=True, key=lambda x: x[0])

    return [r[1] for r in scored[:top_k]]

