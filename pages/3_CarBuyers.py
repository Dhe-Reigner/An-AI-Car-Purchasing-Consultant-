import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.dataframe_explorer import dataframe_explorer
from langchain_experimental.agents import create_csv_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os 


#-----------Page Config---------
st.set_page_config(layout='wide')
st.title='Car Buyers Market Behaviour'

#-----------Load Data------------
df=pd.read_csv('dataset/CarBuyers.csv')

#------------Analytics Section------
st.subheader('List of Car Buyers with their Car Preferences')

filtered_df = dataframe_explorer(df,case=True)
st.dataframe(filtered_df,use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader('Male Car Preferences',divider='rainbow')
    fig = px.bar(
        filtered_df,
        x='Model',
        y='Male',
        title = 'Male Buyer Preference by Model'
    )
    st.plotly_chart(fig,  use_container_width=True)

with col2:
    st.subheader('Female Car Preferences',divider='rainbow')
    fig1 = px.bar(
        filtered_df,
        x='Model',
        y='Female',
        title = 'Female Buyer Preference by Model'
    )
    st.plotly_chart(fig1,  use_container_width=True)

col11, col22 = st.columns(2)

with col11:
    st.subheader('Male Buyer Price Sensitivity', divider='rainbow')
    fig2 = px.bar(
        filtered_df,
        x='Model',
        y='Price',
        color='Male',
        title='Price vs Male Buyer Interest'
    )
    st.plotly_chart(fig2,use_container_width=True)

with col22:
    st.subheader('Female Buyer Price Sensitivity', divider='rainbow')
    fig3 = px.bar(
        filtered_df,
        x='Model',
        y='Price',
        color='Female',
        title='Price vs Female Buyer Interest'
    )
    st.plotly_chart(fig3,use_container_width=True)

#---------------AI Interaction Section-----------
st.divider()
st.subheader(' Ask the Data(AI-Powered Insights)')

st.markdown(
    """
Try questions like:
- Which car models are preferred more by male buyers?
- Which models attract both male and female buyers?
- Are higher-priced cars preferred by a specified gender?
- Which models show balanced buyer interest?
- What pricing strategy fits each buyer segment?
"""
)

#-----------Langchain Setup-------------
load_dotenv()
api_key = os.getenv('GROQ_API_KEY')
llm = ChatGroq(model='llama-3.1-8b-instant', temperature=0.6,api_key=api_key)

user_csv= 'dataset/CarBuyers.csv'

chatcsv = create_csv_agent(llm,user_csv,allow_dangerous_code=True,verbose=True)


#-------------Chat Input-----------
user_question = st.chat_input('Ask a question about Car Buyers')

if user_question:
    with st.spinner('Analyzing buyer behavoir...'):
        response = chatcsv.run(user_question)
    st.markdown('### AI Insight')
    st.write(response)