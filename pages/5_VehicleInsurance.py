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

#---------Analytics Section--------
st.subheader('Handling Vehicle Insurance')

filtered_df = dataframe_explorer(df,case=True)
st.dataframe(filtered_df, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader('Insurance Premium by Vehicle Type')
    fig = px.bar(
        filtered_df,
        x='TYPE_VEHICLE',
        y='PREMIUM'
    )
    st.plotly_chart(fig,use_container_width=True)

with col2:
    st.subheader('Risk Category VS Premium', divider='rainbow')
    fig2 = px.box(
        filtered_df,
        x='USAGE',
        y='PREMIUM'
    )
    st.plotly_chart(fig2,use_container_width=True)

#--------------AI Interaction Section-----------
st.divider()
st.subheader(' Ask the Data(AI-Powered Insights)')

st.markdown(
    """
"""
)


#------------Langchain Setup--------
load_dotenv()
api_key = os.getenv('GROQ_API_KEY')
llm = ChatGroq(model='llama-3.1-8b-instant',temperature=0.6,api_key=api_key)

user_csv = 'dataset/VehicleInsurance.csv'

chatscv = create_csv_agent(llm, user_csv,allow_dangerous_code=True,verbose=True)

#----------Chat Input--------

user_question = st.chat_input('Ask a questo=ion about Vehicle Insurance')

if user_question:
    with st.spinner('Analyzing Insurance provision... '):
        response = chatscv.run(user_question)
    st.markdown('### AI Insights')
    st.write(response)