import streamlit as st

from semantic_scorer import score_user_text

from state_builder import build_state
from recipes import get_recipes_from_state


# ================= UI SETUP =================
st.set_page_config(page_title="Student Culinary AI")
st.title("🍜 Student Culinary AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("How are you feeling today?")


# ================= MAIN PIPELINE =================
if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # ---------- 1️⃣ Semantic scoring ----------
    scores = score_user_text(user_input)


    # ---------- 2️⃣ Build student state ----------
    state = build_state(scores)

    # ---------- 3️⃣ Get recipes from state ----------
    recipes = get_recipes_from_state(state, top_k=3)

    # ---------- 4️⃣ Build reply ----------
    if not recipes:
        reply = "I couldn't find a good recipe 😅 Try describing your mood differently."
    else:
        recipe_list = "\n".join([f"- **{r['name']}**" for r in recipes])

        reply = (
            "Here are a few recipes that might suit you:\n\n"
            f"{recipe_list}\n\n"
            "_Hope this helps your student hunger 😄_"
        )

    # ---------- 5️⃣ Show reply ----------
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
