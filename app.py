import streamlit as st
from ollama_utils import query_ollama  # your function in ollama_utils.py

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="🚀 Product Launch Intelligence",
    page_icon="✨",
    layout="wide"
)

# ---------------------------
# Custom Styling (Dark Purple Theme)
# ---------------------------
st.markdown("""
    <style>
    body {
        background-color: #0f0f1a;
        color: #e0e0ff;
        font-family: "Segoe UI", sans-serif;
    }
    .stTextInput > div > div > input {
        background-color: #1c1c2b;
        color: #ffffff;
        border-radius: 12px;
        padding: 10px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #1c1c2b;
        color: #e0e0ff;
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        font-weight: 500;
    }
    .stTabs [aria-selected="true"] {
        background-color: #5a189a;
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------
# Header
# ---------------------------
st.title("🚀 Product Launch Intelligence")
st.caption("AI-powered insights for product marketing & GTM teams")

# ---------------------------
# Company URL Input
# ---------------------------
company_url = st.text_input("🔗 Enter Company URL:", placeholder="https://example.com")

# ---------------------------
# Tabs (always visible)
# ---------------------------
tabs = st.tabs(["📊 Launch Insights", "💬 Market Sentiment", "📈 Metrics"])

# ---------------------------
# Tab Logic
# ---------------------------
if company_url:
    with tabs[0]:
        st.subheader("📊 Launch Insights")
        if st.button("Run Analysis", key="insights_btn"):
            with st.spinner("Analyzing product launch..."):
                prompt = f"Analyze the product launch strategy for {company_url}"
                result = query_ollama(prompt)
            st.markdown(f"**Analysis:**\n\n{result}")

    with tabs[1]:
        st.subheader("💬 Market Sentiment")
        if st.button("Run Sentiment", key="sentiment_btn"):
            with st.spinner("Checking sentiment..."):
                prompt = f"Analyze market sentiment for {company_url}"
                result = query_ollama(prompt)
            st.markdown(f"**Sentiment:**\n\n{result}")

    with tabs[2]:
        st.subheader("📈 Metrics & KPIs")
        if st.button("Run Metrics", key="metrics_btn"):
            with st.spinner("Evaluating metrics..."):
                prompt = f"Analyze adoption metrics & KPIs for {company_url}"
                result = query_ollama(prompt)
            st.markdown(f"**Metrics:**\n\n{result}")
else:
    with tabs[0]:
        st.info("👆 Enter a company URL above to get launch insights.")
    with tabs[1]:
        st.info("👆 Enter a company URL above to analyze market sentiment.")
    with tabs[2]:
        st.info("👆 Enter a company URL above to explore metrics & KPIs.")
