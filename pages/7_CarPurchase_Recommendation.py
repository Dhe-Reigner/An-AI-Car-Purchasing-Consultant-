import streamlit as st
from .crew import Mycrew
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    st.set_page_config(page_title='AI Car Purchase Recommendation Engine',page_icon="🚗")
    st.title('🚗 AI-Powered Car Purchase Recommendation Engine')

    st.markdown("""
Welcome to your intelligent car buying assistant.
                
                Based on your financial profile ,lifestyle, and preferences,our we recommend the best vehicles for you by analyzing:

                💰 Affodability & Loan Eligibility
                📊 Buyer Trends & Market Insights
                🛠️ Reliability & Repair History
                🛡️ Insurance Cost Factors
                 🚘New vs Used Car Value Comparison
                
                Fill in your deatils below to get started.
                
""")
    with st.sidebar:
        st.header('Buyer Profile')
        col1,col2 = st.columns(2)

        with col1:
            name = st.text_input('👤 Full Name')
            age = st.number_input('🎂Age',min_value=18,max_value=80,step=1)
            gender = st.selectbox('⚧ Gender',['Male','Female','Prefer not to say'])
            country = st.text_input('🌍 Country',placeholder='Kenya')

            annual_salary = st.number_input('💼Annual Salary ($)',min_value=0.0,step=1000.00)
            credit_card_debt = st.number_input('💳Credit Card Debt ($)', min_value=0.0, step=500.0)
            net_worth = st.number_input('🏦Net Worth ($)', min_value=0.0, step=5000.0)

        with col2:
            cibil_score = st.number_input('📊 Credit Score',min_value=300,max_value=900,step=1)
            dependents = st.number_input('👨‍👩‍👧Number of Dependents',min_value=0,step=1)
            employment_status = st.selectbox('🧑‍💼Employment Type',['Employed','Self-Employed','Business Owner'])

            loan_term = st.selectbox('🏦Preferred Loan Term (Years)',[1,3,5,7])
            budget = st.number_input('🚘Car Condition Preference',['New','Used','Either'])


if __name__=='__main__':
    main()