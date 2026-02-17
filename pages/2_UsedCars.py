import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
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

#----------Load & Cleaning Data---------
df['Price'] = pd.to_numeric(df['Price'],errors='coerce')
df['Mileage'] = pd.to_numeric(df['Mileage'],errors='coerce')
df['Year'] = pd.to_numeric(df['Year'],errors='coerce')
df['Cylinders'] = pd.to_numeric(df['Cylinders'],errors='coerce')

df.dropna(subset=['Price','Mileage','Year'], inplace=True)

#-------------Overview KPIs--------
col1,col2,col3,col4,col5 = st.columns(5)

col1.metric('Total Listings',len(filtered_df))
col2.metric('Average Price (AED)',f"{df['Price'].mean():,.0f}")
col3.metric('Median Price (AED)',f"{df['Price'].median():,.0f}")
col4.metric('Average Mileage (km)',f"{df['Mileage'].mean():,.0f}")
col5.metric('Top Make',df['Make'].mode()[0])

#-----------Brand & Body Type Analysis--------
st.subheader('🏷️ Brand & Body Type Analysis')

brand1,brand2 = st.columns(2)

with brand1:
    st.subheader('Top 10 Car Makes',divider='rainbow')
    brand1 = px.bar(
        df['Make'].value_counts().head(10)
    )
    st.plotly_chart(brand1,use_container_width=True)

with brand2:
    st.subheader('Body Type Distribution',divider='rainbow')
    brand2 = px.pie(
        filtered_df,
        names='Body Type'
    )
    st.plotly_chart(brand2,use_container_width=True)


#--------------Price & Mileage Analysis---------
st.subheader('💰 Price & Mileage Insights')

price1,price2 = st.columns(2)

with price1:
    st.subheader('Price Distribution', divider='rainbow')
    price1 = px.histogram(
        filtered_df,
        x='Price',
        nbins=50
    )
    st.plotly_chart(price1, use_container_width=True)

with price2:
    st.subheader('Price by Body Type',divider='rainbow')
    price2 = px.box(
        filtered_df,
        x='Body Type',
        y='Price'
    )
    st.plotly_chart(price2,use_container_width=True)

st.subheader('Price vs Mileage',divider='rainbow')
scatter = px.scatter(
    filtered_df,
    x='Mileage',
    y='Price',
    color='Body Type'
)
st.plotly_chart(scatter,use_container_width=True)

#----------Year-Based Trends-------------
st.subheader('📅 Time-Based Trends')

year_stats = df.groupby('Year').agg(
    Avg_Price=('Price','mean'),
    Listings=('Price','count')
).reset_index()

stats1,stats2 = st.columns(2)

with stats1:
    st.subheader('Average Price by Year',divider='rainbow')
    stats1 = px.line(
        year_stats,
        x='Year',
        y='Avg_Price'
    )
    st.plotly_chart(stats1,use_container_width=True)

with stats2:
    st.subheader('Listings Count by Year',divider='rainbow')
    stats2 = px.line(
        year_stats,
        x='Year',
        y='Listings'
    )
    st.plotly_chart(stats2,use_container_width=True)

#----------Techinical Features----------
st.subheader('⚙️ Techincal Characteristics',divider='rainbow')

tech1,tech2,tech3 = st.columns(3)

with tech1:
    st.subheader('Transmission Type',divider='rainbow')
    tech1 = px.pie(
        filtered_df
    )









# col1, col2 = st.columns(2)

# with col1:
#     st.subheader('Mileage VS Price', divider='rainbow')
#     fig = px.scatter(
#         filtered_df,
#         x='Mileage',
#         y='Price',
#         color='Make',
#         hover_data=['Model','Year']
#     )
#     st.plotly_chart(fig,use_container_width=True)

# with col2:
#     st.subheader('Most Common Car Brands')
#     brand_counts = (
#         filtered_df['Make'].
#         value_counts().
#         reset_index().
#         rename(columns={'index':'Make','Make':'Count'})
#     )
#     fig2 = px.bar(
#         brand_counts,
#         x='Make',
#         y='Count'
#     )
#     st.plotly_chart(fig2, use_container_width=True)

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
