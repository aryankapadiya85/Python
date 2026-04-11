import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",   
    database="college_Python"
)

cursor = con.cursor()
cursor.execute("select * from student")

row = cursor.fetchone()

while row is not None:
    print(row)
    row = cursor.fetchone()

con.close()
