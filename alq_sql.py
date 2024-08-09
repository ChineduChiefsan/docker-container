import os
from google.cloud import bigquery
from sqlalchemy import create_engine
import pandas as pd

proj = 'summer-catfish-430218-g3'
dataset = 'sample_dataset'
target_table = 'annual_movie_summary_df'
table_id= f"{proj}.{dataset}.{target_table}"

#connections

connect_string = 'mysql+pymysql://oscarval_user:learnsql123@oscarvalles.com:3306/oscarval_sql_course'

conn=create_engine(connect_string)


client = bigquery.Client (project=proj)

#create sql

sql_query = """select year, count(imdb_title_id) as movie_count,
avg(duration) as avg_movie_duration,
avg(avg_vote) as avg_rating 
from oscarval_sql_course.imdb_movies group by year"""

def run_query(query):
    return pd.read_sql_query(query,conn)

df = run_query(sql_query)

#transform data

def avg_rating(avg_rating):
    if avg_rating <= 5.65:
        return 'bad movie year'
    elif avg_rating <= 5.9:
        return 'okay movie year'
    elif avg_rating <=10:
        return 'good movie year'
    else:
        return 'not rated'


df['avg_rating'] = df['avg_rating'].apply(avg_rating)

#load data

job_config = bigquery.LoadJobConfig(

    autodetect = True,
    write_disposition='WRITE_TRUNCATE')

load_job = client.load_table_from_dataframe(df,table_id, job_config = job_config)

load_job.result()
#check records

dest_table = client.get_table(table_id)
print(f"you have {dest_table.num_rows} in your table")
