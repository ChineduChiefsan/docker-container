import mysql.connector
from mysql.connector import errorcode
import pandas as pd
import os


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

def movie_duration(d):
    if d < 60:
        return 'short movie'
    elif 60 < d <90:
        return 'avg length movie'
    elif 90<  d <5000:
        return 'really long movie'
    else:
        return 'no data'

queries = """select 
year,
genre,
title,
case when avg_vote<3 then 'bad'
when avg_vote between 4 and 6 then 'okay'
when avg_vote > 6 then 'good' end as movieRating,
duration,
avg_vote from oscarval_sql_course.imdb_movies where year between 2005 and 2010"""


df = run_query(queries)

df['watchability'] = df['duration'].apply(movie_duration)
#create filter
yr_2005 = df['year']==2005

print(df[yr_2005].head())

#get filepath
cur_path = os.getcwd()

file= 'movies_length.csv'
file_path= os.path.join(cur_path, 'Data_files', file)
#print(file_path)

df[yr_2005].to_csv(file_path,index=False)




conn.close()
