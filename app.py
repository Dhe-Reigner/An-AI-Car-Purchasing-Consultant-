import streamlit as st

st.set_page_config(
    page_title="AI Car Purchasing Consultant",
    page_icon="🚗",
    layout='wide'
    )

st.title('🚗 AI Car Purchasing Consultant')

st.markdown(
    """
Welcome to the **AI Car Purchasing Consultant**.

This application helps buyers make **financially optimal, explainable and risk-aware vehicle purchase decisions** by combining:
- Buyer financial behavior
- Vehicle market data
- Loan feasibility
- Insurance & repair costs
- Agent-based reasoning

👉 Use the navigation bar to navigate through the analysis and recommendation pages.
"""
)