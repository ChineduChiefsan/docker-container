import mysql.connector
from mysql.connector import errorcode
import pandas as pd
import os
import csv


#pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

conn = mysql.connector.connect(user='oscarval_user',
                               password='learnsql123',
                               host='oscarvalles.com',
                               database='oscarval_sql_course',
                               port=3306)

def run_query(query):
    return pd.read_sql_query(query,conn)

# def create_state(str):
#         return str[:2]

cur_path = os.getcwd()
file= 'city_housing.csv'
file_path= os.path.join(cur_path, 'Data_files', file)

house_prices = """ select
*
from
city_house_prices """

df = run_query(house_prices)

#pivot table date,city,price Data transformation

df.set_index('Date', inplace=True)
df= df.stack().reset_index()

df.columns = ['date', 'city', 'price']
test= df['city'].values

print(test)

df.to_csv(file_path,index=False)
