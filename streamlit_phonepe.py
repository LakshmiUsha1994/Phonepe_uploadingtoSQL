import streamlit as st
import pandas_profiling
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot 
import plotly.express as px
import plotly.graph_objs as go

from streamlit_pandas_profiling import st_profile_report
#st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout="wide")


st.title(":violet[PhonePe Pulse Data Visualization(2018-2022)📈]")
st.write('  ') #To create space between title and slect box
#________________________________________________________________________________________________________________#
    ### Map transactions statewise
st.header(':blue[Phonepe app opened user for all the states from the year 2018 - 2023]')
map_data =pd.read_csv("D:\\USHA\\presentations\\test folders\\test\\map_user.csv")
col1, col2 = st.columns(2)
years = map_data['Year'].unique()#extracting years from dataframe
Quarters = map_data['Quater'].unique()#extracting quarters from dataframe
#select box to choose year and state
with col1:
    year_choice = st.selectbox('Year', years, key=10)
with col2:
    choose_state = st.selectbox('Please select State', ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                          'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                          'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                          'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                          'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                          'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                          'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                          'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                          'uttarakhand', 'west-bengal'), index=30, key='choose_state')
    
st.write(' ')
st.write(' ')
col1, col2 = st.columns((3,1), gap='large') 
mapUser_df1 = map_data[(map_data ['Year'] == year_choice) & (map_data['State']==choose_state)]
select_map=mapUser_df1[['Quater','Registered_user']]
grouped=select_map.groupby('Quater').sum()

with col1:
    st.line_chart(data=grouped)

with col2:
    st.subheader(':violet[Observations]')
    st.write(':violet[*  overall the app_opening user increses for every quater for all the specified year and states] ')
    st.write(':violet[* Also the the number of user increses in all states from the previous year]')
#________________________________________________________________________________________________________________#    
### Map transactions statewise

st.header(':blue[Transaction count for Districts of Specified year, State, and quater]')
top_states=pd.read_csv("D:\\USHA\\presentations\\test folders\\test\\Top_Trans.csv")
col1, col2, col3= st.columns(3)
years = top_states['Year'].unique()#extracting years from dataframe

Quarters = top_states['Quater'].unique()#extracting quarters from dataframe

#select box to choose year, state and quarter


with col1:
    year_choice = st.selectbox('Year', years, key=2)

with col2:
    quarter_choice = st.selectbox('Quater', Quarters, key=3)
                       
with col3:
    topTrans_state = st.selectbox('Please select State', ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                          'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                          'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                          'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                          'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                          'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                          'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                          'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                          'uttarakhand', 'west-bengal'), index=30, key='topTrans_state')
    

st.write(' ')
st.write(' ')
col1, col2 = st.columns((2,1), gap='large')

with col1:
    # Filtering the DataFrame to include only data for the selected Quater,state and year
    topTrans_df = top_states[(top_states['Quater'] == quarter_choice) & (top_states['Year'] == year_choice) & (top_states['State'] == topTrans_state)]
    # Select only the "Districts", Transacion_count 
    select_trans=topTrans_df[['District','Transacion_count']]
    
    st.bar_chart(data=select_trans, x='District', y='Transacion_count')
    
    # Select only the "Districts", Transacion_amount 
    select_transAmt=topTrans_df[['District','Transacion_amount']]
    
    st.bar_chart(data=select_transAmt, x='District', y='Transacion_amount')

with col2:
    
    st.subheader(':violet[Observations]')
    st.write(':violet[* Bengaluru urban almost consistently tops the list. ]')
    st.write(':violet[* In 2022, Hyderabad crosses Bengaluru urban in both Amount transferred and Transactions made.]')
    st.write(':violet[* There is a overall increase in trend for both Amount transferred and Transactions.]')
#________________________________________________________________________________________________________________#
### aggregated Transaction statewise

st.header(':blue[Aggregated Transaction Statewise]')
agg_Trans=pd.read_csv("D:\\USHA\\presentations\\test folders\\test\\Aggregated_trans.csv")
col1, col2, col3= st.columns(3)
years = top_states['Year'].unique()#extracting years from dataframe

Quarters = top_states['Quater'].unique()#extracting quarters from dataframe

#select box to choose year, district and quarter


with col1:
    year_agg = st.selectbox('Year', years, key=4)

with col2:
    quarter_agg = st.selectbox('Quater', Quarters, key=5)
                       
with col3:
    state_agg = st.selectbox('Please select State', ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                          'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                          'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                          'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                          'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                          'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                          'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                          'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                          'uttarakhand', 'west-bengal'), index=30, key='state_agg')
    

st.write(' ')
st.write(' ')
col1, col2 = st.columns((2,1), gap='large')

with col1:
    # Filtering the DataFrame to include only data for the selected district and year
    aggregated_df = agg_Trans[(agg_Trans['Quater'] == quarter_agg) & (agg_Trans['Year'] == year_agg) & (agg_Trans['State'] == state_agg)]
    # Select only the "Districts", Transacion_count
    select_aggre=aggregated_df[['Transacion_type','Transacion_count']]
    labels = select_aggre['Transacion_type']
    sizes = select_aggre['Transacion_count']
    fig3 = go.Figure(data=[go.Pie(labels=labels, values=sizes, hole=.5, hovertext= select_aggre['Transacion_count'],
                                hovertemplate='<b>%{label}</b><br>' + 'Transacion_count: %{value}<br>' )])
    
    fig3.update_layout( height=600, width=800)

    st.plotly_chart(fig3)
    
with col2:
    
    st.subheader(':violet[Observations]')
    st.write(':violet[* Peer-to-peer payments had the highest transaction count in every quarter from 2018 to 2020, followed by Recharge & bill payments and Merchant payments.]')
    st.write(':violet[* Merchant payments increased their count from second quarter of 2022 and topped the transactions crossing peer to peer transactions.]')
    st.write(' :violet[*Overall, the transaction count for all payment types increased from 2018 to 2022.]')
#________________________________________________________________________________________________________________#  
 # aggregated user statewise/Mobile brands

st.header(':blue[Phonepe use based on Mobile brands]')
agg_user=pd.read_csv("D:\\USHA\\presentations\\test folders\\test\\aggregated_user.csv")
col1, col2, col3= st.columns(3)
years = agg_user['Year'].unique()#extracting years from dataframe

Quarters = agg_user['Quater'].unique()#extracting quarters from dataframe

#select box to choose year, district and quarter


with col1:
    year_mobile = st.selectbox('Year', years, key=6)

with col2:
    quarter_mobile = st.selectbox('Quater', Quarters, key=7)
                       
with col3:
    state_mobile = st.selectbox('Please select State', ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                          'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                          'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                          'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                          'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                          'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                          'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                          'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                          'uttarakhand', 'west-bengal'), index=30, key='state_mobile')
    

st.write(' ')
st.write(' ')
col1, col2 = st.columns((2,1), gap='large')

with col1:
    # Filtering the DataFrame to include only data for the selected district and year
    mobile_df = agg_user[(agg_user['Quater'] == quarter_mobile) & (agg_user['Year'] == year_mobile) & (agg_user['State'] == state_mobile)]
    # Select only the "Districts", Transacion_count
    select_mobile=mobile_df[['Brand','Brand_count']]
    st.bar_chart(data=select_mobile, x='Brand', y='Brand_count')
    # generating the profile report for the mobile brand
    pr = select_mobile.profile_report()
    st_profile_report(pr)
 
    

with col2:
    
    st.subheader(':violet[Observations]')
    st.write(':violet[* Xiaomi ranks first in all the quarter from the year 2018-2021 for phonepe installation.]')
    st.write(':violet[* Vivo and Samsung ranks second and third alternatively followed by Xiaomi.]')
    st.write(':violet[* Overall, the transaction count for all mobile brands increased from 2018 to 2021.]')
#________________________________________________________________________________________________________________#    
###Top states


st.header('Top 10 transactions for States')
top_states=pd.read_csv("D:\\USHA\\presentations\\test folders\\test\\top_states.csv")
col1, col2 = st.columns(2)
years = top_states['Year'].unique()#extracting years from dataframe

Quarters = top_states['Quarters'].unique()#extracting quarters from dataframe

#select box to choose year, district and quarter


with col1:
    year_choice = st.selectbox('Year', years, key=8)

with col2:
    quarter_choice = st.selectbox('Quarter', Quarters, key=9)

st.write(' ')
st.write(' ')
col1, col2, col3 = st.columns((1,2,1), gap='large')

with col1:
    # Filtering the DataFrame to include only data for the selected district and year
    selected_df = top_states[(top_states['Quarters'] == quarter_choice) & (top_states['Year'] == year_choice)]

    # Select only the "Districts", "Amount" and "count" columns
    amount_df = selected_df[['States', 'Amount in Millions', 'Transaction_count']]
    #selected_df.index = selected_df.reset_index().index + 1
    #selected_df = selected_df.sort_values('Transaction_count', ascending=True)
    amount_df.index = amount_df.reset_index().index + 1
    amount_df.drop(columns='Transaction_count', inplace=True)

    # Display the resulting DataFrame
    st.write(amount_df)
    

with col2:
    st.bar_chart(data=selected_df, x='States', y='Transaction_count')

with col3:
    st.subheader(':violet[Observations]')
    st.write(':violet[* Telangana and Maharashtra are consistently the top two states in terms of amount in millions across all years.]')
    st.write(':violet[* The total amount in millions for all states increases each year, which indicate overall growth of digital payments in India.]')
    st.write(':violet[* Karnataka, Andhra Pradesh, Rajasthan, Uttar Pradesh, Madhya Pradesh, Bihar and Delhi appear in the top ten states with the highest amount of transactions in multiple years.]')
