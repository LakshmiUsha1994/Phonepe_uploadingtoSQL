#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd
import pymysql
import os
import json
import sqlalchemy
from sqlalchemy import text
import socket
import numpy as np

user = 'root'
password = 'govdonviv_K94'
host = 'localhost'
port = 3306
database = 'phonepe'
connection = sqlalchemy.create_engine("mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
    user, password, host, port, database
))

# ---------------------------------------------------- Fetching datas from Mysql using pandas -----------------------------------------------
query1 = 'select * from agg_trans'
df = pd.read_sql(query1, con=connection)
query2 = 'select * from top_trans'
state = pd.read_sql(query2, con=connection)
query3 = 'select * from top_user'
districts = pd.read_sql(query3, con=connection)
query4 = 'select * from map_trans'
districts_tran = pd.read_sql(query4, con=connection)
query5 = 'select * from map_user'
app_opening = pd.read_sql(query5, con=connection)
query6 = 'select * from agg_user'
user_device = pd.read_sql(query6, con=connection)

st.balloons()
with st.container():

    st.title(":violet[PhonePe Pulse Data Visualization(2018-2022)📈]")   
    
    

with st.sidebar:
# bar diagram for aggregated transaction
    st.subheader(':violet["Overall India Analysis-State wise"]')
    choose_year=st.selectbox("Select the year", ("2018","2019","2020","2021","2022"))
    choose_quad=st.selectbox("Select the quarter",("1","2","3","4"))
    choose_state = st.selectbox('Please select State', ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                          'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                          'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                          'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                          'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                          'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                          'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                          'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                          'uttarakhand', 'west-bengal'), index=30, key='choose_state')
    trans_type = st.selectbox('Please select the values to visualize', ('Transacion_count', 'Transacion_amount'), key='trans_type')
        
    # chart representation plot for aggregated mobile usage
    st.subheader(':violet["Mobile transaction for overall India analysis-State wise"]')
    mobile_brand = st.selectbox('Please select the brand to visualize', ('Xiaomi', 'Samsung','Vivo', 'Oppo','OnePlus', 
                                                                         'Realme','Apple', 'Motorola','Lenovo', 'Huawei',
                                                                         'Tecno', 'Asus','COOLPAD', 'Gionee','HMD Global',
                                                                         'Infinix','Lava','Lyf','Micromax','Others'),
                                                                          key='mobile_brand')
    #choose_year=st.selectbox("Select the year", ("2018","2019","2020","2021","2022"))
    aggUser_quad=st.selectbox("Select the quarter",("1","2","3","4"),key='aggUser_quad')
    aggUser_state = st.selectbox('Please select State', ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                          'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                          'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                          'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                          'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                          'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                          'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                          'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                          'uttarakhand', 'west-bengal'), index=30, key='aggUser_state')
    trans_type_mobile = st.selectbox('Please select the values to visualize', ('Brand_count', 'Brand_percentage'), 
                                     key='trans_type_mobile')
    
    
    #---------------------------------
    # bar diagram representation plot for aggregated mobile usage
    st.subheader(':violet["Phonepe Registered user-State wise"]')
    Reg_user_state = st.selectbox('Please select State', ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                          'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                          'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                          'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                          'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                          'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                          'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                          'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                          'uttarakhand', 'west-bengal'), index=30, key='Reg_user_state')
    regUser_year=st.selectbox("Select the year", ("2018","2019","2020","2021","2022"),index=1,key='regUser_year')
    
    regAppOpen = st.selectbox('Please select the values to visualize', ('Registered_user', 'App_opening'), 
                                     key='regAppOpen')
    
    
with st.container(): 
    # extracting the data from aggregated user  and ploting bar graph
    scat_df=df[(df['Year']==choose_year) & (df['State']==choose_state) & (df['Quater']==choose_quad)]
    if trans_type=='Transacion_count':
        transtype=scat_df['Transacion_type']
        axisy=np.array(scat_df['Transacion_count'])
        labels=np.arange(len(transtype))
        bargraph=plt.bar(labels,list(map(int,axisy)))
            
    else:
        transtype=scat_df['Transacion_type']
        
        axisy=np.array(scat_df['Transacion_amount'])
        labels=np.arange(len(transtype))
        bargraph=plt.bar(labels,list(map(int,axisy)))

    st.bar_chart(bargraph)
    
    # aggregated user values for mobile transactions
    mobile_trans=user_device[(user_device['Brand']==mobile_brand) & (user_device['State']==aggUser_state) & (user_device['Quater']==aggUser_quad)]
    if trans_type_mobile=='Brand_count':
        transtype_mobile=np.array(mobile_trans['Year'])
        axisy2=np.array(mobile_trans['Brand_count'])
        labels2=np.arange(len(transtype_mobile))
        bargraph2=plt.bar(labels2,list(map(int,axisy2)))
    
    else:
        transtype_mobile=np.array(mobile_trans['Year'])
        axisy2=np.array(mobile_trans['Brand_percentage'])
        labels2=np.arange(len(transtype_mobile))
        bargraph2=plt.bar(labels2,list(map(int,axisy2)))
    
    st.bar_chart(bargraph2)
    
     # bar diagram representation plot for app opening or registered user in phonepe
    appOpen_trans=app_opening[(app_opening['Year']==regUser_year) & (app_opening['State']==Reg_user_state ) ]
    overall_open=appOpen_trans.groupby([ 'Quater','District']).sum()
    
    if regAppOpen=='Registered_user':
        phoneApp=np.array(overall_open['Year'])
        axisy3=np.array(overall_open['Registered_user'])
        labels3=np.arange(len(phoneApp))
        bargraph3=plt.bar(labels3,list(map(int,axisy3)))
    else:
        phoneApp=np.array(overall_open['Year'])
        axisy3=np.array(overall_open['App_opening'])
        labels3=np.arange(len(phoneApp))
        bargraph3=plt.bar(labels3,list(map(int,axisy3)))
    
    st.bar_chart(bargraph3)

