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
    args = (id,)
    sql = "delete from tbl1 where id=%s"
    mycursor.execute(sql,args)
    print("Record deleted successfully")
except:
    print("Unable to delete:Error")