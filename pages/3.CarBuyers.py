import streamlit as st
import pandas as pd
import plotly_express as px

st.set_page_config(layout='wide')

st.title('Car Buyers Market Behaviour')
df=pd.read_csv('pages/3.CarBuyers.csv')

st.subheader('Dataset Preview')
st.dataframe(df,use_container_width=True)




