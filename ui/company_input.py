import streamlit as st
from crawler import fetch_page_text
from hf_utils import query_hf
def show():
    st.subheader("🏢 Company Input")

    company_url = st.text_input("Enter company website URL:")
    if st.button("Analyze Company"):
        if company_url:
            with st.spinner("🔎 Fetching data..."):
                page_text = fetch_page_text(company_url)
                summary = query_hf(f"Summarize the company from this text:\n{page_text}")
            
            st.success("✅ Analysis complete!")
            st.write(summary)
        else:
            st.warning("Please enter a valid URL.")
