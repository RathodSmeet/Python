import tkinter
from tkinter import messagebox
win = tkinter.Tk()
win.geometry("250x250")


def btnlogin_click():
     messagebox.showinfo("Confirm","This is simple message")

lblusername = tkinter.Label(win,text="Username: ")
lblusername.place(x=10,y=50)
txtusername = tkinter.Entry(win)
txtusername.place(x=110,y=50)

lblpassword = tkinter.Label(win,text="Password: ")
lblpassword.place(x=10,y=70)
txtpassword = tkinter.Entry(win)
txtpassword.place(x=110,y=70)

btnlogin = tkinter.Button(win,text="Login",command=btnlogin_click)
btnlogin.place(x=110,y=90)
win.mainloop()



