from tkinter import ttk
from tkinter import *
from tkinter.font import BOLD
from typing import Text
from tkinter import messagebox

r=Tk()

r.geometry("300x400")
r.title("LoginForm")
r.state("zoomed")
r.configure(bg="#353935")
#r.iconbitmap('IcoImage.icon')

#style
"""style=ttk.Style()
style.configure('TLabel',bg="#353935",fg="white")
"""
#ui
MainCanvas=Canvas(r,width=500,height=400)
MainCanvas.place(x=700,y=400,anchor=CENTER)

Username=ttk.Label(MainCanvas,text="Enter a Username")
Password=ttk.Label(MainCanvas,text="Enter Password")
Phonenum=ttk.Label(MainCanvas,text="Enter your Phone number")

Username.place(x=30,y=240)
Password.place(x=30,y=270)
Phonenum.place(x=30,y=300)

TakeUsername=ttk.Entry(MainCanvas, width=50)
TakePassword=ttk.Entry(MainCanvas, width=50)
TakePhonenum=ttk.Entry(MainCanvas, width=50)
TakeUsername.place(x=330,y=250, anchor=CENTER)
TakePassword.place(x=330,y=280, anchor=CENTER)
TakePhonenum.place(x=330,y=310, anchor=CENTER)



def login():
    Username=eUs.get()
    Password=ePs.get()

    if Username=="" and Password=="":
        messagebox.showinfo("","Blank Not Allowed")

    elif Username=="Anime" and Password=="admin":
        messagebox.showinfo("","Login Success")

    else:
        messagebox.showinfo("","incorrect Username and Password")

global eUs
global ePs

Us=Label(r,text="Username",fg="black").place(x=20,y=20)
Ps=Label(r,text="Password",fg="black").place(x=20,y=60)

eUs=Entry(r,bd=5)
eUs.place(x=120,y=20)

ePs=Entry(r,bd=5)
ePs.place(x=120,y=60)

b1=Button(r,text="Login",command=login,height=1,width=12,bd=6,bg="black",fg="white").place(x=80,y=100)

r.mainloop()
