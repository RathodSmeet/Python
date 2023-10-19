import tkinter
win = tkinter.Tk()
win.geometry("250x250")

lblusername = tkinter.Label(win,text="Username: ")
lblusername.place(x=10,y=50)
txtusername = tkinter.Entry(win)
txtusername.place(x=110,y=50)

lblpassword = tkinter.Label(win,text="Password: ")
lblpassword.place(x=10,y=70)
txtpassword = tkinter.Entry(win)
txtpassword.place(x=110,y=70)

btnlogin = tkinter.Button(win,text="Login")
btnlogin.place(x=110,y=90)
win.mainloop()