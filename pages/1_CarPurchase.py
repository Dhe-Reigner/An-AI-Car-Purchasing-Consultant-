# import pandas as pd
# import streamlit as st
# import plotly.express as px
# from streamlit_extras.dataframe_explorer import dataframe_explorer

# from streamlit_option_menu import option_menu

# #with st.sidebar:
# selected = option_menu(
#     menu_title=None,
#     options=['Car Purchase','UAE Used Cars','Car Buyers','Loan Approval','Vehicle Insurance','Car Diagnosis & Repairs','Car Purchase Reccomendation'],
#     orientation='horizontal'
# )

# if selected == 'Car Purchase':
#     st.title(f'{selected} Analysis')
# if selected == 'UAE Used Cars':
#     st.title(f'Detailed Analysis of {selected}')
# if selected == 'Car Buyers':
#     st.title(f'List of {selected} with their Car Preferences')
# if selected == 'Loan Approval':
#     st.title(f'A glimpse of Bank/s {selected}')
# if selected == 'Vehicle Insurance':
#     st.title(f"Handling {selected}")
# if selected == 'Car Diagnosis & Repairs':
#     st.title(f"For {selected}")
# if selected == 'Car Purchase Reccomendation':
#     st.title(f'Based on the Relevant, we suggest this {selected}')




# def main():
#     st.set_page_config(page_title="Car Purchase Data",page_icon=':bar_chart:',layout='wide')
#     #st.title('Car Purchase Data ')

#     df = pd.read_csv('sales.csv')
#     #st.write(df)

#     # with st.sidebar:
#     #     segment = st.sidebar.multiselect(
#     #         "Select the Segment:",
#     #         options=df['Segment'].unique(),
#     #         default=df['Segment'].unique()
#     #     )
#     #     city=st.sidebar.multiselect(
#     #         'Select City:',
#     #         options=df['City'].unique(),
#     #         default=df['City'].unique()
#     #     )
#     #     state = st.sidebar.multiselect(
#     #         "Select the State:",
#     #         options=df['State'].unique(),
#     #         default=df['State'].unique()
#     #     )
#     #     region = st.sidebar.multiselect(
#     #         'Select Region:',
#     #         options=df['Region'].unique(),
#     #         default=df['Region'].unique()
#     #     )
#     #     category = st.sidebar.multiselect(
#     #         "Select Category:",
#     #         options=df['Category'].unique(),
#     #         default=df['Category'].unique()
#     #     )
#     #     # sub_category = st.sidebar.multiselect(
#     #     #     'Select Sub-Category:',
#     #     #     options=df['Sub-Category'].unique(),
#     #     #     default=df['Sub-Category'].unique()
#     #     # )


#     # df_selection = df.query(
#     #         'Segment == @segment & City == @city & State == @state & Region == @region & Category == @category'#& Sub-Category == @sub_category
#     #     )
#     with st.expander('Filter Excel Data'):
#         df_selection = dataframe_explorer(df,case=False)
#     st.write(df_selection)

#     # ----- CALCULATIONS BASED ON FILTERED DATA ----

#     # KPIs
#     s1,s2,s3 = st.columns(3)

#     if not df_selection.empty:
#         # total_sales = df_selection['Sales'].sum()

#         # st.metric(
#         #     label='Total Sales',
#         #     value=f"${total_sales:,.2f}"
#         # )
#         # with s1:
#         #     st.subheader('Total Sales',divider='rainbow')
#         s1.metric('Total Sales',f"${df_selection['Sales'].sum():,.2f}")
        
#         # with s2:
#         #     st.subheader('Total Orders',divider='rainbow')
#         s2.metric('Total Orders', df_selection.shape[0])

#         # with s3:
#         #     st.subheader('Avg Sales/Order',divider='rainbow')
#         s3.metric('Avg Sales/Order',f'${df_selection['Sales'].mean():,.2f}')

#         col1,col2,col3,col4 = st.columns(4)

#         with col1:
#             st.header('Sales by Sud-Category',divider='rainbow')
#             sales_by_subcat = (
#                 df_selection.groupby('Sub-Category',as_index=False)['Sales'].sum().sort_values('Sales',ascending=False)
#             )

#             fig = px.bar(
#                 sales_by_subcat,
#                 x='Sub-Category',
#                 y='Sales'
#             )
#             st.plotly_chart(fig, use_container_width=True)

#         with col2:
#             st.header('Sales by Category',divider='rainbow')
#             sales_by_cat = (
#                 df_selection.groupby('Category',as_index=False)['Sales'].sum()
#             )

#             fig = px.bar(
#                 sales_by_cat,
#                 x='Category',
#                 y='Sales'
#             )
#             st.plotly_chart(fig, use_container_width=True)

#         with col3:
#             st.header('Sales by Region',divider='rainbow')
#             sales_by_reg = (
#                 df_selection.groupby('Region',as_index=False)['Sales'].sum()
#             )

#             fig = px.bar(
#                 sales_by_reg,
#                 x='Region',
#                 y='Sales',
#                 color='Region'
#             )
#             st.plotly_chart(fig, use_container_width=True)

#         with col4:
#             st.header('Sales by Segment',divider='rainbow')
#             sales_by_seg = (
#                 df_selection.groupby('Segment',as_index=False)['Sales'].sum()
#             )

#             fig = px.bar(
#                 sales_by_seg,
#                 x='Segment',
#                 y='Sales'
#             )
#             st.plotly_chart(fig, use_container_width=True)

#     else:
#         st.warning('No data available for the selected filters.')

#     col11,col22 = st.columns(2)
#     with col11:
#         st.subheader('Sales Mix by Category',divider='rainbow')
#         category_mix=(
#             df_selection.groupby('Category',as_index=False)['Sales'].sum()
#         )
#         fig = px.pie(
#             category_mix,
#             names='Category',
#             values='Sales',
#             hole=0.5
#         )
#     st.plotly_chart(fig,use_container_width=True)

#     with col22:
#         st.subheader('Sales by State',divider='rainbow')
#         sales_by_state = (
#             df_selection.groupby('State',as_index=False)['Sales'].sum().sort_values('Sales',ascending=False)
#         )
#         fig = px.bar(
#             sales_by_state,
#             x='State',
#             y='Sales'
#         )
#         st.plotly_chart(fig,use_container_width=True)
        
#     a,b = st.columns(2)
#     # with a:
#     #     st.subheader('Monthly Sales Trend',divider='rainbow')

#     #     df_selection['Order Date'] = pd.to_datetime(df_selection['Order Date']).format="%d/%m/%Y"
#     #     mon_sales_trend = (
#     #         df_selection.groupby(pd.Grouper(key='Order Date',freq='Customer Name'))['Sales']
#     #         .sum().reset_index()
#     #     )
#     #     fig = px.line(
#     #         mon_sales_trend,
#     #         x='Order Date',
#     #         y='Sales'
#     #     )
#     #     st.plotly_chart(fig, use_container_width=True)

#     with b:
#         st.subheader('Average Order Value',divider='rainbow')

#         avg_order_value = df_selection['Sales'].mean()
#         st.metric('Avg Order Value',f"${avg_order_value:,.2f}")

#     top_products = (
#         df_selection.groupby('Sub-Category',as_index=False).agg(
#             Sales = ('Sales', 'sum'),
#             Orders = ('Sales', 'count')
#             )
#             .sort_values('Sales',ascending=False)
#     )

#     top_10 = top_products.head(10)
#     bottom_10 = top_products.tail(10)

#     c1,c2 = st.columns(2)

#     with c1:
#         st.subheader('🔝Top 10 Sub-Categories')
#         st.dataframe(top_10)

#     with c2:
#         st.subheader("🔻Bottom 10 Sub-Categories")
#         st.dataframe(bottom_10)


#     if 'Profit' in top_products.columns:
#         st.subheader('Sales vs Profit Margin (Size = Orders)',divider='rainbow')
#         top_products['Profit Margin %'] = (
#             top_products['Profit']/top_products['Sales'] * 100
#         )

#         fig = px.scatter(
#             top_products,
#             x='Sales',
#             y='Profit Margin %',
#             size='Orders',
#             hover_name='Sub-Category'
#         )
#         st.plotly_chart(fig,use_container_width=True)



#     def highlight_sales(val):
#         try:
#             return 'background-color: #ffcccc' if val < 500 else ''
#         except:
#             return ''

#     styled_df = df_selection.style.applymap(
#         highlight_sales,
#         subset=['Sales']
#     )

#     st.subheader('📊Performance Heatmap')
#     st.dataframe(styled_df,use_container_width=True)

#     st.download_button(
#         label='Download Filtered Data(CSV)',
#         data = df_selection.to_csv(index=False),
#         file_name='filtered_sales_data.csv',
#         mime='text/csv'
#     )
#     #st.write(df_selection)

#     # a1,a2 = st.columns(2)
#     # with a1:



# if __name__=='__main__':
#     main()




import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_extras.dataframe_explorer import dataframe_explorer
from langchain_experimental.agents import create_csv_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

def clean_currency(col):
     return(
          col.astype(str)
          .str.replace('$','',regex=False)
          .str.replace(',','',regex=False)
          .astype(float)
     )


#----------------Page Config----------
st.set_page_config(layout='wide')
st.title="Customer Car Purchasing Behavior Analysis"

#-------------Load Data---------------
df = pd.read_csv('dataset/CarPurchase.csv')

#------------Analytics Section---------
st.subheader('Car Purchase Analysis')

filtered_df = dataframe_explorer(df, case=True)
st.dataframe(filtered_df,use_container_width=True)

money_cols = [
     'Annual Salary',
     'Credit Card Debt',
     'Net Worth',
     'Car Purchase Amount'
]
for col in money_cols:
     df[col] = clean_currency(df[col])

#-------------KPIs-------------
st.subheader('📊Key Metrics')
a1,a2,a3,a4 = st.columns(4)

a1.metric('Total Buyers',len(filtered_df))
a2.metric('Average Car Purchase($)',f"{df['Car Purchase Amount'].mean():,.0f}")
a3.metric('Average Annual Salary ($)',f'{df['Annual Salary'].mean():,.0f}')
a4.metric('Average Net Worth ($)',f"{df['Net Worth'].mean():,.0f}")

st.divider()

#----------Demographics----------
st.subheader('👥 Demographic Analysis')

demo1,demo2,demo3 = st.columns(3)

with demo1:
     st.subheader('Buyers by Country',divider='rainbow')
     fig = px.bar(df['Country'].value_counts().reset_index(name='Count'),
                  x='Country', y='Count',
                  )
     st.plotly_chart(fig,use_container_width=True)
     
with demo2:
     st.subheader('Gender Distribution',divider='rainbow')
     fig2 = px.pie(filtered_df,names='Gender')
     st.plotly_chart(fig2,use_container_width=True)

with demo3:
     st.subheader('Age Distribution',divider='rainbow')
     fig3 = px.histogram(filtered_df,x='Age',nbins=20)
     st.plotly_chart(fig3,use_container_width=True)

st.divider()

#------------Income & Purchase---------
st.subheader('💰 Income vs Car Purchase Behavior')

car1, car2 = st.columns(2)

with car1:
     st.subheader('Annual Salary vs Car Purchase Amount')
     car1 = px.scatter(
          filtered_df,
          x='Annual Salary',
          y='Car Purchase Amount',
          color='Gender',  
     )
     st.plotly_chart(car1,use_container_width=True)

with car2:
     st.subheader('Annual Salary by Gender')
     car2 = px.box(
          filtered_df,
          x='Gender',
          y='Annual Salary',
     )
     st.plotly_chart(car2,use_container_width=True)


# Line Chart
st.subheader('Average Car Purchase Amount by Age',divider='rainbow')
avg_by_age = df.groupby('Age')['Car Purchase Amount'].mean().reset_index()
avg = px.line(
     avg_by_age,
     x='Age',
     y='Car Purchase Amount'
)
st.plotly_chart(avg,use_container_width=True)

st.divider()

#-----------Debt & Wealth---------
st.subheader('📉Debt & Net Worth Analysis')

debt1, debt2 = st.columns(2)

with debt1:
     st.subheader('Credit Card Debt Distribution')
     debt1 = px.histogram(
          filtered_df,
          x='Credit Card Debt',
          nbins=30
     )
     st.plotly_chart(debt1,use_container_width=True)

with debt2:
     st.subheader('Credit Card Debt vs Car Purchase')
     debt2 = px.scatter(
          filtered_df,
          x='Credit Card Debt',
          y='Car Purchase Amount'
     )
     st.plotly_chart(debt2,use_container_width=True)

st.subheader('Net Worth Distribution by Country',divider='rainbow')
box = px.box(
     filtered_df,
     x='Country',
     y='Net Worth'
)
st.plotly_chart(box,use_container_width=True)

st.divider()

#-------------Correlation Heatmap----------
st.subheader('🧠 Correlation  Heatmap',divider='rainbow')

numeric_df = df[
     ['Age','Annual Salary','Credit Card Debt','Net Worth','Car Purchase Amount']
]

corr = numeric_df.corr()

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm',ax=ax)
st.pyplot(fig)

# col1, col2 = st.columns(2)

# with col1:
#     st.subheader('Annual Salary VS Car Purchase Amount', divider='rainbow')
#     fig = px.scatter(
#         filtered_df,
#         x='Annual Salary',
#         y='Car Purchase Amount',
#         color='Gender'
#     )
#     st.plotly_chart(fig,use_container_width=True)

# with col2:
#     st.subheader('Age Distribution of Buyers', divider='rainbow')
#     fig2 = px.histogram(
#         filtered_df,
#         x='Age',
#         nbins=20,
#     )
#     st.plotly_chart(fig2, use_container_width=True)


#------------AI Interation Section----------
st.divider()
st.subheader('🤖Ask the Data(AI-Powered Insights)')

st.markdown(
    """
You can ask questions like:
- *Which income group spends the most on cars?*
- *Do males or females spend more on averages?*
- *What age range makes the highest purchases?*
- *Is salary strongly correlated with car price?*
"""
)

#---------------LangChain Setup------------
load_dotenv()
api_key = os.getenv('GROQ_API_KEY')
llm = ChatGroq(model='llama-3.1-8b-instant',temperature=0.6,api_key=api_key)

user_csv = 'dataset/CarPurchase.csv'

chatcsv = create_csv_agent(llm,user_csv,allow_dangerous_code=True,verbose=True)


#---------------Chat Input------------
user_question = st.chat_input('Ask a question about the car purchase data')

# ANALYSIS_PROMPT = """
# You are a senior data analyst and business intelligence consultant.

# When answering:
# - Always explain *what the data shows*
# - Indentify *patterns and trends*
# - Mention *numerical evidence* (averages, percentages,ranges)
# - Highlight *busness implications*
# - Suggest *actions or decisions* where relevant

# DO NOT just return numbers.
# Always provide insight and interpretation.

# Consider using the structure below to structure the answer:

# 📌 Key Finding:
# - ...

# 📈 Data Evidence:
# - ...

# 💡 Business Insight:
# - ...

# 🎯 Recommendation:
# - ...

# User question:
# {question}
# """

if user_question:
        with st.spinner('Analyzing the data...'):
            response = chatcsv.run(user_question)

        st.markdown('### 📊 AI Insight')
        st.write(response)


