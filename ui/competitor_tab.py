import streamlit as st
from helpers import expand_competitor_report

def competitor_tab(company_name, team):
    st.markdown("### 🔍 Competitor Launch Analysis")
    if not company_name:
        st.info("👆 Please enter a company name above to start the analysis")
        return

    analyze_btn = st.button("🚀 Analyze Competitor Strategy", key="competitor_btn", type="primary")

    if analyze_btn and team:
        with st.spinner("Analyzing competitor strategy..."):
            bullets = team.run(
                f"Generate up to 16 evidence-based insight bullets about {company_name}'s most recent product launches..."
            )
            long_text = expand_competitor_report(bullets.content, company_name)
            st.session_state.competitor_response = long_text
            st.success("✅ Competitor analysis ready")
            st.rerun()

    if st.session_state.get("competitor_response"):
        st.divider()
        st.markdown("### 📊 Analysis Results")
        st.markdown(st.session_state.competitor_response)
