import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.dataframe_explorer import dataframe_explorer
from langchain_experimental.agents import create_csv_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

#--------------Page Config-------
st.set_page_config(layout='wide')
st.title='Loan Approval Analysis'

#--------------Load Data---------
df = pd.read_csv('dataset/LoanApproval.csv')

# clean column names
df.columns = df.columns.str.strip()

#-----------Analytics Section--------
st.subheader('Overview of Bank Loan Approval Decisions')

filtered_df = dataframe_explorer(df, case=True)
st.dataframe(filtered_df,use_container_width=True)


numeric_cols = [
    'loan_id', ' no_of_dependents', ' education', ' self_employed',
       ' income_annum', ' loan_amount', ' loan_term', ' cibil_score',
       ' residential_assets_value', ' commercial_assets_value',
       ' luxury_assets_value', ' bank_asset_value', ' loan_status'
]
for col in numeric_cols:
    filtered_df[col] = (
        filtered_df[col]
        .astype(str)
        .str.replace(',','',regex=True)
        .str.replace(r'[^\d.]','',regex=True)
        .astype(float)
    )

col1,col2,col3,col4,col5 = st.columns(5)

approval_rate = (df[' loan_status'] == ' Approved').mean() * 100

col1.metric('Total Applicants',len(filtered_df))
col2.metric('Approval Rate (%)',round(approval_rate,2))
col3.metric('Average Income'f'${df[' income_annum'].mean():,.0f}')
col4.metric('Average Loan Amount',f"${df[' loan_amount'].mean():,.0f}")
col5.metric('Average CIBIL Score',round(df[' cibil_score'].mean(),1))



col1,col2 = st.columns(2)
 
with col1:
    st.subheader('Loan Amount Distribution by Approval Status', divider='rainbow')
    fig = px.box(
        filtered_df,
        x='loan_status',
        y='loan_amount',
        color='loan_status',
        title='Loan Amount vs Approval Outcome'
    )
    st.plotly_chart(fig,use_container_width=True)

with col2:
    st.subheader('Applicant Income Distribution by Loan Status', divider='rainbow')
    fig2 = px.histogram(
        filtered_df,
        x='income_annum',
        color='loan_status',
        barmode='overlay',
        nbins=30,
        title='Income Distribution for Approved vs Rejected Loans'
    )
    st.plotly_chart(fig2, use_container_width=True)

#-------------AI Interaction Section----------
st.divider()
st.subheader(' Ask the Data(AI-Powered Insights)')

st.markdown(
    """
You can ask questions like:
- What income range has the hihgest loan approval rate?
- Are higher loan amounts more likely to be rejected?
- What factors most influence loan approval?
- What applicant profile has the best approval chances?
- How should banks reduce loan dafault risk?
"""
)

#---------------Langchain Setup------------
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model='llama-3.1-8b-instant',temperature=0.6,api_key=api_key)

user_csv = 'dataset/LoanApproval.csv'

chatcsv = create_csv_agent(llm,user_csv,allow_dangerous_code=True,verbose=True)

#-------------Chat Input--------------
user_question = st.chat_input('Ask a question about Loan/s Approval')

if user_question:
    with st.spinner('Analyzing loan risk patterns...'):
        response = chatcsv.run(user_question)
    st.markdown('### AI Insight')
    st.write(response)