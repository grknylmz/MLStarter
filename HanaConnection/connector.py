import pyhdb

connection = pyhdb.connect(
    host='172.111.10.72',
    port=30015,
    user='LINERIS',
    password='ASD12345asd'
)

cursor = connection.cursor()
cursor.execute("SELECT partner FROM BUT000")
cursor.fetchone()
connection.close()