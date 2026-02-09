import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.dataframe_explorer import dataframe_explorer

st.set_page_config(
    layout='wide'
)

df = pd.read_csv('dataset/VehicleRepairs.csv')

st.subheader('Vehicle Diagnosis & Repairs')
#st.dataframe(df,use_container_width=True)

filtered_df = dataframe_explorer(df,case=True)
st.dataframe(filtered_df)

col1, col2 = st.columns(2)

with col1:
    st.subheader('Problem Description vs Repair Status')
    fig = px.bar(
        df.groupby('Problem Description')['Repair Status'].mean().reset_index(),
        x = 'Problem Description',
        y = 'Repair Status'
    )
    st.plotly_chart(fig,use_container_width=True)

with col1:
    st.subheader('Problem Description vs Repair Status')
    fig2 = px.box(
        df.groupby('Diagnosis')['Solution Used'].mean().reset_index(),
        x = 'Diagnosis',
        y = 'Solution Used'
    )
    st.plotly_chart(fig2,use_container_width=True)