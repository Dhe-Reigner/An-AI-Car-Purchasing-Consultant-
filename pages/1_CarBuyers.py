import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.dataframe_explorer import dataframe_explorer
from langchain_experimental.agents import create_csv_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os 


#-----------Page Config---------
st.set_page_config(layout='wide')
st.title='Car Buyers Market Behaviour'

#-----------Load Data------------
df=pd.read_csv('dataset/CarBuyers.csv')

#------------Analytics Section------
st.subheader('List of Car Buyers with their Car Preferences')

filtered_df = dataframe_explorer(df,case=True)
st.dataframe(filtered_df,use_container_width=True)

#---------------Overview KPIs-----------
kpi1,kpi2,kpi3,kpi4 = st.columns(4)
kpi1.metric('Total Buyers',len(filtered_df))
kpi2.metric('Average Price',f'${df['Price'].mean():,.0f}')
kpi3.metric('Top Manufacturer',df.groupby('Manufacturer')['Total'].sum().idxmax())
kpi4.metric('Top Fuel Type',df.groupby('Fuel')['Total'].sum().idxmax())

#----------Market Demand Analysis
manu_df = df.groupby("Manufacturer")['Total'].sum().reset_index()

st.subheader('Total Buyers by Manufacturer',divider='rainbow')
manu = px.bar(
    manu_df.sort_values('Total',ascending=False),
    x='Manufacturer',
    y='Total'
)
st.plotly_chart(manu,use_container_width=True)


col1, col2 = st.columns(2)

with col1:
    st.subheader('Male Car Preferences',divider='rainbow')
    fig = px.bar(
        filtered_df,
        x='Model',
        y='Male',
        title = 'Male Buyer Preference by Model'
    )
    st.plotly_chart(fig,  use_container_width=True)

with col2:
    st.subheader('Female Car Preferences',divider='rainbow')
    fig1 = px.bar(
        filtered_df,
        x='Model',
        y='Female',
        title = 'Female Buyer Preference by Model'
    )
    st.plotly_chart(fig1,  use_container_width=True)

col11, col22 = st.columns(2)

with col11:
    st.subheader('Male Buyer Price Sensitivity', divider='rainbow')
    fig2 = px.bar(
        filtered_df,
        x='Model',
        y='Price',
        color='Male',
        title='Price vs Male Buyer Interest'
    )
    st.plotly_chart(fig2,use_container_width=True)

with col22:
    st.subheader('Female Buyer Price Sensitivity', divider='rainbow')
    fig3 = px.bar(
        filtered_df,
        x='Model',
        y='Price',
        color='Female',
        title='Price vs Female Buyer Interest'
    )
    st.plotly_chart(fig3,use_container_width=True)

st.subheader('Fuel Type Distribution',divider='rainbow')
fuel_df = df.groupby('Fuel')['Total'].sum().reset_index()

fuel = px.pie(
    fuel_df,
    names='Fuel',
    values='Total'
)
st.plotly_chart(fuel,use_container_width=True)

#----------Price & Performance Analysis--------
st.subheader('Average Price vs Engine CC',divider='rainbow')
engine_price = df.groupby('Engine CC')['Price'].mean().reset_index()

engine = px.line(
    engine_price,
    x='Engine CC',
    y='Price',
    markers=True
)
st.plotly_chart(engine,use_container_width=True)

st.subheader('Price Distribution by Transmission Type',divider='rainbow')
box = px.box(
    filtered_df,
    x='Transmission',
    y='Price'
)
st.plotly_chart(box,use_container_width=True)

#--------Buyer Demographics(Gender Demand)----------
st.subheader('Gender-Based Demand by Manufacturer',divider='rainbow')

gender_df = df.groupby('Manufacturer')[['Male','Female','Unknown']].sum().reset_index()

bar = px.bar(
    gender_df,
    x='Manufacturer',
    y=['Male','Female','Unknown'],
    barmode='stack'
)
st.plotly_chart(bar,use_container_width=True)

#----------Relationship Analysis-------------
numeric_cols = [
    'Price','Engine CC','Power','Male','Female','Unknown','Total'
]

# for col in numeric_cols:
#     df[col] = pd.to_numeric(df[col],errors='coerce')

for col in numeric_cols:
    filtered_df[col] =  (
        filtered_df[col]
        .astype(str)
        .str.replace(',','',regex=True)
        .str.replace(r'[^\d.]','',regex=True)
        .astype(float)
    )
    #df[col] = pd.to_numeric(df[col],errors='coerce')

st.subheader('Power vs Price(Bubble Size = Buyers)',divider='rainbow')
scatter = px.scatter(
    filtered_df,
    x='Power',
    y='Price',
    size='Total',
    color='Fuel',
    size_max=50,
    hover_data=['Engine CC']
)
st.plotly_chart(scatter,use_container_width=True)

#--------Distribution Analysis-----------
st.subheader('Distribution of Car Prices',divider='rainbow')

histogram = px.histogram(
    filtered_df,
    x='Price',
    nbins=30
)
st.plotly_chart(histogram,use_container_width=True)


#-------------Correlation Analysis(Heatmap)--------
st.subheader('Correlation Heatmap',divider='rainbow')
corr = filtered_df[numeric_cols].corr()

show = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale='RdBu'
)
st.plotly_chart(show,use_container_width=True)


#---------------AI Interaction Section-----------
st.divider()
st.subheader(' Ask the Data(AI-Powered Insights)')

st.markdown(
    """
Try questions like:
- Which car models are preferred more by male buyers?
- Which models attract both male and female buyers?
- Are higher-priced cars preferred by a specified gender?
- Which models show balanced buyer interest?
- What pricing strategy fits each buyer segment?
"""
)

#-----------Langchain Setup-------------
load_dotenv()
api_key = os.getenv('GROQ_API_KEY')
llm = ChatGroq(model='llama-3.1-8b-instant', temperature=0.6,api_key=api_key)

user_csv= 'dataset/CarBuyers.csv'

chatcsv = create_csv_agent(llm,user_csv,allow_dangerous_code=True,verbose=True)


#-------------Chat Input-----------
user_question = st.chat_input('Ask a question about Car Buyers')

if user_question:
    with st.spinner('Analyzing buyer behavoir...'):
        response = chatcsv.run(user_question)
    st.markdown('### AI Insight')
    st.write(response)