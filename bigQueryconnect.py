from google.cloud import bigquery

client = bigquery.Client(project='summer-catfish-430218-g3')

sqlquery = """select * from summer-catfish-430218-g3.sample_data.movies"""

query_job = client.query(sqlquery)

result = query_job.result()

for r in result:
    print(r.year, r.genre, r.avg_vote)
