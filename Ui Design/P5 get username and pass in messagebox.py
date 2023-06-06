import tkinter
from tkinter import messagebox
win = tkinter.Tk()
win.geometry("250x250")


def btnlogin_click():
    v_user = v_username.get()
    v_pass = v_password.get()
    messagebox.showinfo("Confirm",v_user)
    messagebox.showinfo("Confirm",v_pass)

v_username = tkinter.StringVar()
v_password = tkinter.StringVar()

lblusername = tkinter.Label(win,text="Username: ")
lblusername.place(x=10,y=10)
txtusername = tkinter.Entry(win,textvariable=v_username)
txtusername.place(x=110,y=50)

lblpassword = tkinter.Label(win,text="Password: ")
lblpassword.place(x=10,y=70)
txtpassword = tkinter.Entry(win,textvariable=v_password)
txtpassword.place(x=110,y=70)

btnlogin = tkinter.Button(win,text="Login",command=btnlogin_click)
btnlogin.place(x=110,y=90)
win.mainloop()



