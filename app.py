
import streamlit as st
from config import setup_page, load_env_and_keys
from agents import init_team
from ui.company_input import company_input
from ui.competitor_tab import competitor_tab
from ui.sentiment_tab import sentiment_tab
from ui.metrics_tab import metrics_tab
from sidebar import sidebar_status

setup_page()
openai_key, firecrawl_key = load_env_and_keys()
team = init_team(openai_key, firecrawl_key)

st.title("🚀 AI Product Launch Intelligence Agent")
st.markdown("*AI-powered insights for GTM, Product Marketing & Growth Teams*")
st.divider()

company_name = company_input()
st.divider()

tabs = st.tabs(["🔍 Competitor Analysis", "💬 Market Sentiment", "📈 Launch Metrics"])
with tabs[0]:
    competitor_tab(company_name, team)
with tabs[1]:
    sentiment_tab(company_name, team)
with tabs[2]:
    metrics_tab(company_name, team)

sidebar_status(openai_key, firecrawl_key, company_name)
