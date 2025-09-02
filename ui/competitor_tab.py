import streamlit as st
from hf_utils import query_hf

def show():
    st.subheader("⚔️ Competitor Analysis")

    competitor_name = st.text_input("Enter competitor name:")
    if st.button("Analyze Competitor"):
        if competitor_name:
            with st.spinner("🤖 Thinking..."):
                analysis = query_hf(f"Analyze the competitor: {competitor_name}")
            st.success("✅ Done!")
            st.write(analysis)
        else:
            st.warning("Please enter a competitor name.")
