import streamlit as st
import os
from dotenv import load_dotenv

def setup_page():
    st.set_page_config(
        page_title="AI Product Intelligence Agent", 
        page_icon="🚀", 
        layout="wide",
        initial_sidebar_state="expanded"
    )

def load_env_and_keys():
    load_dotenv()

    st.sidebar.header("🔑 API Configuration")
    openai_key = st.sidebar.text_input(
        "OpenAI API Key", type="password",
        value=os.getenv("OPENAI_API_KEY", ""),
        help="Required for AI agent functionality"
    )
    firecrawl_key = st.sidebar.text_input(
        "Firecrawl API Key", type="password",
        value=os.getenv("FIRECRAWL_API_KEY", ""),
        help="Required for web search and crawling"
    )

    if openai_key: os.environ["OPENAI_API_KEY"] = openai_key
    if firecrawl_key: os.environ["FIRECRAWL_API_KEY"] = firecrawl_key

    return openai_key, firecrawl_key
