from tkinter import *
import mysql.connector
from gc import freeze
from tkinter import messagebox



def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python"
    )


#print (create fun)

k=Tk()
k.geometry("600x600")
k.title("Task_TK")
k.configure(bg="gray")
k.resizable(False,False)

l_id=Label(k,text="Id :")
l_id.place(x=80,y=50)
e_id=Entry(k)
e_id.place(x=150,y=50)

l_fn=Label(k,text="Firstname :")
l_fn.place(x=80,y=80)
e_fn=Entry(k)
e_fn.place(x=150,y=80)

l_ln=Label(k,text="Lastname :")
l_ln.place(x=80,y=110)
e_ln=Entry(k)
e_ln.place(x=150,y=110)

l_eid=Label(k,text="Email_id :")
l_eid.place(x=80,y=140)
e_eid=Entry(k)
e_eid.place(x=150,y=140)

l_pn=Label(k,text="P_Number")
l_pn.place(x=80,y=170)
e_pn=Entry(k)
e_pn.place(x=150,y=170)

b1=Button(text="INSERT",bg="black",fg="white")
b1.place(x=100,y=200)

b2=Button(text="UPDATE",bg="black",fg="white")
b2.place(x=150,y=200)

b3=Button(text="DELETE",bg="black",fg="white")
b3.place(x=205,y=200)

b4=Button(text="INSERT",bg="black",fg="white")
b4.place(x=260,y=200)



k.mainloop()
