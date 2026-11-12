import streamlit as st
import ollama

MODEL = "gemma4:e4b"

SYSTEM_PROMPT = """You are a usability expert. You are given a screenshot of a user
interface. Critique it against Nielsen's 10 usability heuristics. For each issue:
- name the heuristic it violates,
- describe the problem in one sentence,
- suggest one concrete fix.
Only comment on what you can actually see. If the image is unclear, say so."""

st.title("🔍 Instant Usability Critic")
st.caption(f"Powered by a local LLM ({MODEL}) — runs entirely on your laptop.")

uploaded = st.file_uploader("Upload a screenshot of a UI", type=["png", "jpg", "jpeg"])

if uploaded:
    st.image(uploaded, caption="Your screenshot", use_container_width=True)

    if st.button("Critique this interface"):
        with st.spinner("Looking at your screenshot… (local models are slow, hang on)"):
            response = ollama.chat(
                model=MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": "Critique this interface.",
                        "images": [uploaded.getvalue()],
                    },
                ],
            )
        st.markdown("### Critique")
        st.markdown(response["message"]["content"])

        st.info(
            "⚠️ This came from a small local model. Treat it as a *prompt for your own "
            "thinking*, not ground truth — it can miss issues and invent others."
        )