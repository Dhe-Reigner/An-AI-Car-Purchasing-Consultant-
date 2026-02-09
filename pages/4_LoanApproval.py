import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.dataframe_explorer import dataframe_explorer

st.set_page_config(
    layout='wide'
)
st.title='Loan Approval Analysis'

df = pd.read_csv('dataset/LoanApproval.csv')

st.subheader('A glimpse of Bank/s Loan Approval')
#st.dataframe(df,use_container_width=True)

filtered_df = dataframe_explorer(df, case=True)
st.dataframe(filtered_df)

col1,col2 = st.columns(2)
 
with col1:
    st.subheader('Loan Amount VS Loan Status', divider='rainbow')
    fig = px.box(
        df,
        x=' loan_amount',
        y=' loan_status'
    )
    st.plotly_chart(fig,use_container_width=True)

with col2:
    st.subheader('Applicant Income Distribution')
    fig2 = px.histogram(
        df,
        x=' income_annum',
        y=' loan_status'
    )
    st.plotly_chart(fig2, use_container_width=True)