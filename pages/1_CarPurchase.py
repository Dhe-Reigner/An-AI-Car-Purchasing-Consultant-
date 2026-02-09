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

st.set_page_config(
    layout='wide'
)

st.title="Customer Car Purchasing Behavior Analysis"

df = pd.read_csv('dataset/CarPurchase.csv')

st.subheader('Car Purchase Analysis')
st.dataframe(df,use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader('Annual Salary VS Car Purchase Amount', divider='rainbow')
    fig = px.scatter(
        df,
        x='Annual Salary',
        y='Car Purchase Amount',
        color='Gender'
    )
    st.plotly_chart(fig,use_container_width=True)

with col2:
    st.subheader('Age Distribution of Buyers', divider='rainbow')
    fig2 = px.histogram(
        df,
        x='Age',
        nbins=20,
    )
    st.plotly_chart(fig2, use_container_width=True)