from google.cloud import bigquery
import os

client = bigquery.Client(project='summer-catfish-430218-g3')

target_table = 'summer-catfish-430218-g3.sample_dataset.city_housing'


job_config = bigquery.LoadJobConfig(skip_leading_rows=1,
                                    source_format=bigquery.SourceFormat.CSV,
                                    autodetect=True,
                                    write_disposition = 'WRITE_TRUNCATE')
cur_path = os.getcwd()
file= 'city_housing.csv'

file_path= os.path.join(cur_path, 'Data_files', file)


with open(file_path, 'rb') as sourcefile:
 load_job = client.load_table_from_file(
  sourcefile,
  target_table,
  job_config = job_config
 )

 load_job.result()

 dest_table = client.get_table(target_table)

 print(f"you have {dest_table.num_rows} in your table")
