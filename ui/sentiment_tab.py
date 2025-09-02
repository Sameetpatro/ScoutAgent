import streamlit as st
from llm import query_ollama

def show():
    st.subheader("💬 Market Sentiment")

    topic = st.text_input("Enter topic or product name:")
    if st.button("Analyze Sentiment"):
        if topic:
            with st.spinner("🧐 Checking sentiment..."):
                sentiment = query_ollama(f"Analyze market sentiment about: {topic}")
            st.success("✅ Done!")
            st.write(sentiment)
        else:
            st.warning("Please enter a topic.")
