import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.dataframe_explorer import dataframe_explorer
from langchain_groq import ChatGroq
from langchain_experimental.agents import create_csv_agent
from dotenv import load_dotenv
import os

#-----------Page Config------
st.set_page_config(layout='wide')
st.title='Vehicle Repairs Cost Analysis'

#-------------Load Data---------
df = pd.read_csv('dataset/VehicleRepairs.csv')

# Clean column names
df.columns = df.columns.str.strip().str.upper()

#------------Analytics Section--------
st.subheader('Vehicle Diagnosis & Repairs Patterns')

filtered_df = dataframe_explorer(df,case=True)
st.dataframe(filtered_df,use_container_width=True)

filtered_df.columns  =(
    filtered_df.columns
    .str.strip()
    .str.replace(" ","_")
    .str.lower()
)

#-------------Overview KPIs---------
col1,col2,col3 = st.columns(3)


col1.metric('Total Records',len(filtered_df))
col2.metric('Unique Cars',filtered_df['car_name'].nunique())
col3.metric('Unique Car Services',filtered_df['solution_used'].nunique())

col11,col12,col13,col14,col15 = st.columns(5)


col11.metric('Problem Classifications',filtered_df['problem_classification'].nunique())
col12.metric('Problem Description',filtered_df['problem_description'].nunique())
col13.metric('Problem Diagnosis',filtered_df['diagnosis'].nunique())
col14.metric('Proposed Fixes',filtered_df['how_to_fix_the_problem'].nunique())
col15.metric('Service History',filtered_df['service_history'].nunique())








col1, col2 = st.columns(2)

with col1:
    st.subheader('Most COmmon Vehicle Problems',divider='rainbow')
    problem_counts = (
        filtered_df['PROBLEM DESCRIPTION']
        .value_counts()
        .reset_index()
        .rename(columns={'index':'Problem','PROBLEM DESCRIPTION':'Count'})
    )
    fig = px.bar(
        problem_counts,
        x='Problem',
        y='Count',
        title='Frequency of Reported Vehicle Problems'
    )
    st.plotly_chart(fig,use_container_width=True)

with col2:
    st.subheader('Repair Status Distribution', divider='rainbow')
    status_counts = (
        filtered_df['REPAIR STATUS']
        .value_counts()
        .reset_index()
        .rename(columns={'index':'Status', "REPAIR STATUS":'Count'})
    )

    fig2 = px.bar(
        status_counts,
        x='Status',
        y='Count',
        color='Status',
        title='Outcome of Repair Attempts'
    )
    st.plotly_chart(fig2,use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    st.subheader('Diagnosis vs Repair Cost',divider='rainbow')
    fig3 = px.box(
        filtered_df,
        x='DIAGNOSIS',
        y='REPAIR COST',
        title='Repair Cost Distribution by Diagnosis'
    )
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader('Most Common Repair Solutions',divider='rainbow')
    solution_counts = (
        filtered_df['SOLUTION USED']
        .value_counts()
        .reset_index()
        .rename(columns={'index':'Solution', 'SOLUTION USED':'Count'})
    )
    fig4 = px.bar(
        solution_counts,
        x='Solution',
        y='Count',
        title='Frequently Applied Repair Solutions'
    )
    st.plotly_chart(fig4,use_container_width=True)


#---------------AI Interaction Section---------
st.divider()
st.subheader('🤖Ask the Data(AI-Powered Insights)')

st.markdown(
    """
You can ask questions like:
- Which problems are most expensive to fix?
- What diagnosis lead to repeated repairs?
- Which repairs are most likely to fail?
- How can buyers aviod high-maintenance vehicles?
- What repair patterns signal unrealiable cars?
"""
)

#---------Langchain Setup----------
load_dotenv()
api_key = os.getenv('GROQ_API_KEY')
llm = ChatGroq('llama-3.1-8b-instant',temperature=0.6,api_key=api_key)

user_csv = 'dataset/VehicleRepairs.csv'

chatcsv = create_csv_agent(llm,user_csv,allow_dangerous_code=True,verbose=True)

#-------Chat Input---------

user_question = st.chat_input('Ask a question about Vehicle Repairs Costs')

if user_question:
    with st.spinner(" Analyzing Repair Risks and Cost Patterns..."):
        response = chatcsv.run(user_question)
    st.write('### 🧠AI Insights')
    st.write(response)