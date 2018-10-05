import pyhdb

connection = pyhdb.connect(
    host='',
    port=30015,
    user='LINERIS',
    password=''
)

cursor = connection.cursor()
cursor.execute("SELECT partner FROM BUT000")
cursor.fetchone()
connection.close()
