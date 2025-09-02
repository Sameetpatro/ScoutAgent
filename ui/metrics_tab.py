import streamlit as st
from hf_utils import query_hf

def show():
    st.subheader("📊 Launch Metrics")

    product_name = st.text_input("Enter product name:")
    if st.button("Get Metrics Insights"):
        if product_name:
            with st.spinner("📈 Analyzing..."):
                metrics = query_hf(f"Provide KPIs and adoption metrics for product: {product_name}")
            st.success("✅ Done!")
            st.write(metrics)
        else:
            st.warning("Please enter a product name.")
