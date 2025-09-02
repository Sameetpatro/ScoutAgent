import streamlit as st

def display_agent_response(resp):
    if hasattr(resp, "content") and resp.content:
        st.markdown(resp.content)
    elif hasattr(resp, "messages"):
        for m in resp.messages:
            if m.role == "assistant" and m.content:
                st.markdown(m.content)
    else:
        st.markdown(str(resp))
