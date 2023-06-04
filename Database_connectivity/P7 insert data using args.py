import mysql.connector as con
try :
    mydb = con.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pythonmysql"
    )
    mycursor = mydb.cursor()
    id = input("Roll Number: ")
    nm = input("Name: ")
    city = input("City: ")
    args = (id,nm,city)
    mycursor.execute("insert into tbl1 values(%s,%s,%s)",args)
    print("Record inserted successfully")
except :
    print("Record insertion failed : Error")