import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pythonmysql"
)
mycursor = mydb.cursor()
mycursor.execute("create table tbl1(id int(11),nm varchar(20),city varchar(10))")