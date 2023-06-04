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
    sql = "update tbl1 set nm=%s,city=%s where id=%s"
    mycursor.execute(sql,args)
    print("Record updated successfully")
except:
    print("Record updated failed:Error")