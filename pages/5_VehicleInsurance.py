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

#-------------Overview KPIs----------
col1,col2,col3,col4 = st.columns(4)

col1.metric('Total Policies',len(filtered_df))
col2.metric('Total Premium', f'{filtered_df['PREMIUM'].sum():,.0f}')
col3.metric('Average Insured Value',f'{filtered_df['INSURED_VALUE'].mean():,.0f}')
col4.metric('Claim Ratio',f'{filtered_df['CLAIM_PAID'].sum()/df['PREMIUM'].sum():.2%}')

#------------Demographic & Policy Analysis------------
st.subheader('Policies by Gender',divider='rainbow')

gender_df = filtered_df['SEX'].value_counts().reset_index(name='count')

bar = px.bar(
    gender_df,
    x='PREMIUM',
    y='count',
    labels={'index':'Gender','count':'Policies'}
)
st.plotly_chart(bar,use_container_width=True)


st.subheader('Vehicle Usage Distribution',divider='rainbow')

usage_df = filtered_df['USAGE'].value_counts().reset_index(name='count')

pie = px.pie(
    usage_df,
    names='index',
    values='count'
)
st.plotly_chart(pie,use_container_width=True)

#----------Vehicle & Premium Analysis--------
st.subheader('Premium Trend Over Years',divider='rainbow')

yearly = df.groupby('EFFECTIVE_YR')['PREMIUM'].sum().reset_index()

line = px.line(
    yearly,
    x='EFFECTIVE_YR',
    y='PREMIUM'
)
st.plotly_chart(line,use_container_width=True)

st.subheader('Insured Value Distribution',divider='rainbow')

histogram = px.histogram(
    filtered_df,
    x='INSURED_VALUE',
    nbins=40
)
st.plotly_chart(histogram,use_container_width=True)

#-------------Risk & Claims Analysis--------
st.subheader('Insured Value vs Premium',divider='rainbow')

scatter = px.scatter(
    filtered_df,
    x='INSURED_VALUE',
    y='PREMIUM',
    color='TYPE_VEHICLE'
)
st.plotly_chart(scatter,use_container_width=True)

st.subheader('Premium Distribution by Vehicle Type',divider='rainbow')

box = px.box(
    filtered_df,
    x='TYPE_VEHICLE',
    y='PREMIUM'
)
st.plotly_chart(box,use_container_width=True)

#-----------Correlation Analysis------------
st.subheader('Correlation Heatmap',divider='rainbow')

numeric_cols = [
    'INSURED_VALUE',
    'PREMIUM',
    'CLAIM_PAID',
    'SEATS_NUM',
    'CCM_TON'
]
corr = filtered_df[numeric_cols].corr()

imshow = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale='RdBu'
)
st.plotly_chart(imshow,use_container_width=True)

#------------Claims Insight-----------
st.subheader('Top 10 Makes by Claims Paid',divider='rainbow')

claims_make = filtered_df.groupby('MAKE')['CLAIM_PAID'].sum().reset_index()

bar = px.bar(
    claims_make.sort_values('CLAIM_PAID', ascending=False).head(10),
    x='MAKE',
    y='CLAIM_PAID'
)
st.plotly_chart(bar,use_container_width=True)


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