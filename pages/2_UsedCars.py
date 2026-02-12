import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.dataframe_explorer import dataframe_explorer
from langchain_experimental.agents import create_csv_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

#-------------Page Config---------
st.set_page_config(layout='wide')
st.title='UAE Used Cars Market Analysis'

#-------------Load Data-----------
df = pd.read_csv('dataset/UsedCars.csv')

#-------------Analytics Section-------
st.subheader('Detailed Analysis of Used Cars')

filtered_df = dataframe_explorer(df, case=True)
st.dataframe(filtered_df,use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader('Mileage VS Price', divider='rainbow')
    fig = px.scatter(
        filtered_df,
        x='Mileage',
        y='Price',
        color='Make',
        hover_data=['Model','Year']
    )
    st.plotly_chart(fig,use_container_width=True)

with col2:
    st.subheader('Most Common Car Brands')
    brand_counts = (
        filtered_df['Make'].
        value_counts().
        reset_index().
        rename(columns={'index':'Make','Make':'Count'})
    )
    fig2 = px.bar(
        brand_counts,
        x='Make',
        y='Count'
    )
    st.plotly_chart(fig2, use_container_width=True)

#-----------AI Interaction Section-----------
st.divider()
st.subheader('🤖 Ask the Data(AI-Powered Insights)')

st.markdown(
    """
Ask questions such as:
- Which car brands offer the best value for money?
- How does mileage affect resale price?
- What year range has the best price-to-mileage ratio?
- Which cars are overpriced for their mileage?
- Are newer cars always more expensive?
"""
)

#------------Langchain Setup-----------
load_dotenv()
api_key = os.getenv('GROQ_API_KEY')
llm = ChatGroq(model='llama-3.1-8b-instant',temperature=0.6,api_key=api_key)

user_csv = 'dataset/UsedCars.csv'

chatcsv = create_csv_agent(llm,user_csv,allow_dangerous_code=True,verbose=True)

#--------------Chat Input----------------
user_question = st.chat_input('Ask a question about used cars market')

if user_question:
    with st.spinner('Analyzing the data...'):
        response = chatcsv.run(user_question)
    st.markdown('### AI Insight')
    st.write(response)
