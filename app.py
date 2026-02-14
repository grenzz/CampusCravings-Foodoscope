import streamlit as st

from semantic_scorer import score_user_text
from state_builder import build_state
from recommend import recommend
from feedback import log_feedback
from user_memory import update_profile
from intent_classifier import detect_intent
from recipe_details import get_recipe_details


st.set_page_config(page_title="Foodoscope AI")
st.title("🍜 Foodoscope AI")

if "last_state" not in st.session_state:
    st.session_state.last_state = None

if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_recipes" not in st.session_state:
    st.session_state.last_recipes = None

if "last_input" not in st.session_state:
    st.session_state.last_input = None

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("How are you feeling today?")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    intent = detect_intent(user_input)

    # ================= DETAIL INTENT =================
    if intent == "recipe_detail":
        details = get_recipe_details(
            user_input,
            st.session_state.get("last_recipes")
        )

        if details:
            ingredient_list = "\n".join(
                [f"- {i}" for i in details["ingredients"]]
            )

            step_list = "\n".join(
                [f"{idx+1}. {s}" for idx, s in enumerate(details["steps"])]
            )

            reply = f"""
## {details['name']} ({details['minutes']} min)

### Ingredients:
{ingredient_list}

### Steps:
{step_list}
            """
        else:
            reply = "Sorry, I couldn't find that recipe."

        st.session_state.messages.append({"role": "assistant", "content": reply})

        with st.chat_message("assistant"):
            st.markdown(reply)

    # ================= RECOMMENDATION INTENT =================
    else:
        scores = score_user_text(user_input)
        state = build_state(scores)

        st.session_state.last_state = state
        st.session_state.last_input = user_input

        recipes = recommend(user_input, state)
        st.session_state.last_recipes = recipes

        if not recipes:
            reply = "I couldn't find a good recipe 😅 Try describing your mood differently."
        else:
            recipe_list = "\n".join(
                [f"- **{r['name']}** ({r['minutes']} min)" for r in recipes]
            )

            reply = (
                "Here are some recipes for you:\n\n"
                f"{recipe_list}\n\n"
                "_Hope this helps 😄_"
            )

        st.session_state.messages.append({"role": "assistant", "content": reply})

        with st.chat_message("assistant"):
            st.markdown(reply)

# 🔥 FEEDBACK SECTION
if st.session_state.last_recipes:
    feedback = st.radio(
        "Was this recommendation helpful?",
        ["👍 Yes", "😐 Somewhat", "👎 No"],
        horizontal=True
    )

    if feedback:
        log_feedback(
            st.session_state.last_input,
            st.session_state.last_state,
            st.session_state.last_recipes,
            feedback
        )

        update_profile(st.session_state.last_recipes, feedback)

        st.success("Thanks! Foodoscope is learning from you 🤖")

print("NEW PIPELINE IS BEING IMPLEMENTED")
