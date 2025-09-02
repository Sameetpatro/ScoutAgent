import streamlit as st

def company_input():
    st.subheader("🏢 Company Analysis")
    col1, col2 = st.columns([3, 1])

    with col1:
        company_name = st.text_input(
            label="Company Name",
            placeholder="Enter company name (e.g., OpenAI, Tesla)",
            help="This company will be analyzed",
            label_visibility="collapsed"
        )
    with col2:
        if company_name:
            st.success(f"✓ Ready to analyze **{company_name}**")

    return company_name
