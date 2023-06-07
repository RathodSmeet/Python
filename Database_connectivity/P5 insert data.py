import mysql.connector
try :
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pythonmysql"
    )
    mycursor = mydb.cursor()
    mycursor.execute("insert into tbl1 values(5,'python','dell')")
    print("Record inserted successfully")
except :
    print("Error")
mydb.commit()