import mysql.connector
from mysql.connector import  errorcode


try:
    conn = mysql.connector.connect(user='oscarval_user',
    password='learnsql123',
    host='oscarvalles.com',
    database='oscarval_sql_course',
    port=3306)
    print("connection worked")

    conn.close()


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_DB_ACCESS_DENIED_ERROR:
        print("problems with login in, check credentialls")
    else:
        print("err")

