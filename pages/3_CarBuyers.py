import streamlit as st
import pandas as pd
import plotly_express as px
from streamlit_extras.dataframe_explorer import dataframe_explorer

st.set_page_config(layout='wide')

st.title='Car Buyers Market Behaviour'
df=pd.read_csv('dataset/CarBuyers.csv')

st.subheader('List of Car Buyers with their Car Preferences')
#st.dataframe(df,use_container_width=True)

filtered_df = dataframe_explorer(df,case=True)
st.dataframe(filtered_df,use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader('Male Car Preferences',divider='rainbow')
    fig = px.bar(
        df,
        x='Model',
        y='Male',
    )
    st.plotly_chart(fig,  use_container_width=True)

with col2:
    st.subheader('Female Car Preferences',divider='rainbow')
    fig1 = px.bar(
        df,
        x='Model',
        y='Female',
    )
    st.plotly_chart(fig1,  use_container_width=True)

col11, col22 = st.columns(2)

with col11:
    st.subheader('Buyer Intent', divider='rainbow')
    fig2 = px.scatter(
        df,
        x='Model',
        y='Price',
        color='Male'
    )
    st.plotly_chart(fig2,use_container_width=True)

with col22:
    st.subheader('Buyer Intent', divider='rainbow')
    fig3 = px.scatter(
        df,
        x='Model',
        y='Price',
        color='Female'
    )
    st.plotly_chart(fig3,use_container_width=True)
