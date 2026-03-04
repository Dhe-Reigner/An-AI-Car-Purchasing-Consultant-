import streamlit as st
from streamlit_extras.dataframe_explorer import dataframe_explorer
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv
import os

#-----------Load Dataset------
df = pd.read_csv('sales.csv')
filtered_df = dataframe_explorer(df,case=True)
st.write(filtered_df)

#----------KPIs-------
st.subheader('KPIs',divider='rainbow')
st.metric('Total Sales',len(filtered_df))
st.divider()

#----------Demographics-----------
st.subheader('Demogrphics',divider='rainbow')

country1,country2,country3,country4 = st.columns(4)

with country1:
    st.subheader('Sales by Country',divider='rainbow')
    country = df['Country'].value_counts().reset_index(name='Count')
    country1 = px.bar(country,
                    x='Country',
                    y='Count'
                    )
    st.plotly_chart(country1,use_container_width=True)

with country2:
    st.subheader('Region',divider='rainbow')
    country2 = px.pie(filtered_df,
                      names='Region',
                      color='Sales'
                      )
    st.plotly_chart(country2,use_container_width=True)

with country3:
    st.subheader('Region & Category',divider='rainbow')
    country3 = px.box(filtered_df,
                          x='Region',
                          y='Category'
                          )
    st.plotly_chart(country3,use_container_width=True)

with country4:
    st.subheader('Region & Sub-Category',divider='rainbow')