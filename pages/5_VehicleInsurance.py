import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.dataframe_explorer import dataframe_explorer
from langchain_groq import  ChatGroq
from langchain_experimental.agents import create_csv_agent
from dotenv import load_dotenv
import os

#----------Page Config--------
st.set_page_config(layout='wide')
st.title='Vehicle Insurance Cost Analysis'

#------------Load Data-----------
df = pd.read_csv('dataset/VehicleInsurance.csv')

# Clean column names
df.columns = df.columns.str.strip().str.upper()

#---------Analytics Section--------
st.subheader('Handling Insurance Cost Drivers')

filtered_df = dataframe_explorer(df,case=True)
st.dataframe(filtered_df, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader('Average Insurance Premium by Vehicle Type',divider='rainbow')
    fig = px.bar(
        filtered_df,
        x='TYPE_VEHICLE',
        y='PREMIUM',
        color='TYPE_VEHICLE',
        title = 'Insurance Cost by Vehicle Category'
    )
    st.plotly_chart(fig,use_container_width=True)

with col2:
    st.subheader('Vehicle Usage vs Insurance Premium', divider='rainbow')
    fig2 = px.box(
        filtered_df,
        x='USAGE',
        y='PREMIUM',
        color='USAGE',
        title='How Usage Imapcts Insurance Pricing'
    )
    st.plotly_chart(fig2,use_container_width=True)

#--------------AI Interaction Section-----------
st.divider()
st.subheader(' Ask the Data(AI-Powered Insights)')

st.markdown(
    """
You can ask questions like:
- Which vehicle type has the highest insurance cost?
- How does commercial vs personal usage  affect premiums?
- What insurance factors should I consider for business vehicles?
- How can buyers reduce long-term insurance costs?
- Which vehicles are cheapest to insure over time?
"""
)


#------------Langchain Setup--------
load_dotenv()
api_key = os.getenv('GROQ_API_KEY')
llm = ChatGroq(model='llama-3.1-8b-instant',temperature=0.6,api_key=api_key)

user_csv = 'dataset/VehicleInsurance.csv'

chatscv = create_csv_agent(llm, user_csv,allow_dangerous_code=True,verbose=True)

#----------Chat Input--------

user_question = st.chat_input('Ask a question about Vehicle Insurance Costs')

if user_question:
    with st.spinner('Analyzing Insurance risk and cost patterns... '):
        response = chatscv.run(user_question)
    st.markdown('### 📊  AI Insights')
    st.write(response)