import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

st.title('Vehicle Insurance Cost Analysis')

df = pd.read_csv('pages/5.VehicleInsurance.csv')
st.subheader('Dataset Preview')
st.dataframe(df, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader('Insurance Premium by Vehicle Type')