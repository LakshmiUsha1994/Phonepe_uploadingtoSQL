**Phonepe-Data-visualization-(2018-2022)**


This is the app i created to analyse Phonepe pulse data which i get through Phonepe pulse github repo


Cloning the data using git clone command into my pc


**First lets extracts datas from the github and convert it into csv files**

This is the dataset i used in my streamlit web application to visualize datas

https://github.com/PhonePe/pulse/tree/master


After cloning files from github repo i created a for loop to loop through each folder and get datas from it and then append it to a dataframe to make it easy to covert to csv for all the json files i required



**Code **
import os
import json
import pandas as pd
path = "D:\\USHA\\presentations\\phonepe\\ghData\\pulse\\data\\aggregated\\transaction\\country\\india\\state\\"
aggTransData = os.listdir(path)
#Agg_state_list
# Agg_state_list--> to get the list of states in India
#<------------------------------------------------------------------------------------------------------------------->#
# This is to extract the data's to create a dataframe
column_list = {'State': [], 'Year': [], 'Quater': [], 'Transacion_type': [],
       'Transacion_count': [], 'Transacion_amount': []}
for i in aggTransData :
    p_i = path+i+"/"
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = p_i+j+"/"
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = p_j+k
            Data = open(p_k, 'r')
            D = json.load(Data)
            try:
                for z in D['data']['transactionData']:
                    Name = z['name']
                    count = z['paymentInstruments'][0]['count']
                    amount = z['paymentInstruments'][0]['amount']
                    column_list['Transacion_type'].append(Name)
                    column_list['Transacion_count'].append(count)
                    column_list['Transacion_amount'].append(amount)
                    column_list['State'].append(i)
                    column_list['Year'].append(j)
                    column_list['Quater'].append(int(k.strip('.json')))
            except:
                pass
# Succesfully created a dataframe
Agg_Trans = pd.DataFrame(column_list)
Agg_Trans.to_csv('D:\\USHA\presentations\\test folders\\test\\Aggregated_trans.csv')
#Agg_Trans




**After extracting the data we need to upload it into Mysql**


To insert datas into Mysql i used sqlalchemy(in order to establish connection you want pymysql also)

**code**
import mysql.connector
import pandas as pd

mydb=mysql.connector.connect(
host="localhost",
user="root",
password="govdonviv_K94",
auth_plugin="mysql_native_password"
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE phonepe;")
mycursor.execute(" USE phonepe")


After connection we need to create table then we can insert csv files to Mysql database


**code:**
sq_1=text('CREATE TABLE agg_trans (MyIndex INT NOT NULL AUTO_INCREMENT,State INT,Year INT,Quater INT,Payment_Mode VARCHAR(50),Total_Transactions_count BIGINT,Total_Amount BIGINT,PRIMARY KEY (MyIndex))')
connection.execute(sq_1)
df = pd.read_csv("D:\\USHA\\presentations\\test folders\\test\\Aggregated_trans.csv")
df.to_sql('agg_trans',con=connection, if_exists= "replace",index=False, chunksize=1000)

**Then fetching the database from mysql using pandas**

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

Then after inserting all my files to Mysql database. I created a new file named main.py to create a app using streamlit.


