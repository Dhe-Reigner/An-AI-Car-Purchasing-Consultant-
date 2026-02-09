import streamlit as st
import pandas as pd
import plotly_express as px

st.set_page_config(layout='wide')

st.title('Car Buyers Market Behaviour')
df=pd.read_csv('pages/3.CarBuyers.csv')

st.subheader('Dataset Preview')
st.dataframe(df,use_container_width=True)

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
    fig = px.bar(
        df,
        x='Model',
        y='Female',
    )
    st.plotly_chart(fig,  use_container_width=True)

col11, col22 = st.columns(2)

with col11:
    st.subheader('Buyer Intent', divider='rainbow')
    fig = px.scatter(
        df,
        x='Model',
        y='Price',
        color='Male'
    )
    st.plotly_chart(fig,use_container_width=True)

with col22:
    st.subheader('Buyer Intent', divider='rainbow')
    fig = px.scatter(
        df,
        x='Model',
        y='Price',
        color='Female'
    )
    st.plotly_chart(fig,use_container_width=True)
