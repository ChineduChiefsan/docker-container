import mysql.connector
from mysql.connector import errorcode

conn = mysql.connector.connect(user='oscarval_user',
                               password='learnsql123',
                               host='oscarvalles.com',
                               database='oscarval_sql_course',
                               port=3306)

cursor = conn.cursor()

query = """select year,title,genre from oscarval_sql_course.imdb_movies limit 7"""



cursor.execute(query)


for (year, title, genre) in cursor:
    print(f"year:{year}, title: {title}, type: {genre}")
conn.close()
