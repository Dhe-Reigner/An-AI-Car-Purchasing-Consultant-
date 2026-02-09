import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    layout='wide'
)
st.title('UAE Used Cars Market Analysis')

df = pd.read_csv('pages/2.UsedCars.csv')

st.subheader('Dataset Preview')
st.dataframe(df,use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader('Mileage VS Price', divider='rainbow')
    fig = px.scatter(
        df,
        x='Mileage',
        y='Price',
        color='Model'
    )
    st.plotly_chart(fig,use_container_width=True)

with col2:
    st.subheader('Most Common Car Brands')
    fig2 = px.bar(
        df['Make'].value_counts().reset_index(),
        x='Year',
        y='Make'
    )
    st.plotly_chart(fig2, use_container_width=True)
