import mysql.connector as con

mydb = con.connect(
    host = "localhost",
    username = "root",
    password = "",
    database = "pythonmysql"
)
def insert(id,name,city):
    try :
        mycursor = mydb.cursor()
        args = (id,name,city)
        mycursor.execute("insert into tbl1 values(%s,%s,%s)",args)
        mydb.commit()
        return True
    except:
        return False
    
def delete(id):
    try :
        mycursor = mydb.cursor()
        args = (id,)
        mycursor.execute("delete from tbl1 where id=%s",args)
        mydb.commit()
        return True
    except:
        return False