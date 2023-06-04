import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pythonmysql"
)
mycursor = mydb.cursor()
mycursor.execute("select * from tbl1")
rows = mycursor.fetchall() # rows is list type collection
for row in rows: # row is tuple type collection
    print(row[0],"\t",row[1],"\t",row[2]) 