import os
from google.cloud import bigquery
import mysql.connector
import pandas as pd

cur_path = os.getcwd()
load_file = 'mysql_export.csv'
load_file = os.path.join(cur_path, 'Data_files', load_file)
proj = 'summer-catfish-430218-g3'
dataset = 'sample_dataset'
target_table = 'annual_movie_summary'
table_id= f"{proj}.{dataset}.{target_table}"
print(table_id)

#connections

conn = mysql.connector.connect(user='oscarval_user',
                               password='learnsql123',
                               host='oscarvalles.com',
                               database='oscarval_sql_course',
                               port=3306)


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

df.to_csv(load_file, index=False)

#load data

job_config = bigquery.LoadJobConfig(skip_leading_rows = 1,
                                    source_format = bigquery.SourceFormat.CSV,
                                    autodetect = True,
                                    write_disposition='WRITE_TRUNCATE')

with open(load_file, 'rb') as file:
    load_job = client.load_table_from_file(file,table_id, job_config = job_config)


load_job.result()


#check records

dest_table = client.get_table(table_id)
print(f"you have {dest_table.num_rows} in your table")
