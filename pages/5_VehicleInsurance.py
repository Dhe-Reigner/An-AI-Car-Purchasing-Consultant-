import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.dataframe_explorer import dataframe_explorer

st.set_page_config(layout='wide')

st.title='Vehicle Insurance Cost Analysis'

df = pd.read_csv('dataset/VehicleInsurance.csv')
st.subheader('Handling Vehicle Insurance')
#st.dataframe(df, use_container_width=True)

filtered_df = dataframe_explorer(df,case=True)
st.dataframe(filtered_df, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader('Insurance Premium by Vehicle Type')
    fig = px.bar(
        df,
        x='TYPE_VEHICLE',
        y='PREMIUM'
    )
    st.plotly_chart(fig,use_container_width=True)

with col2:
    st.subheader('Risk Category VS Premium', divider='rainbow')
    fig2 = px.box(
        df,
        x='USAGE',
        y='PREMIUM'
    )
    st.plotly_chart(fig2,use_container_width=True)