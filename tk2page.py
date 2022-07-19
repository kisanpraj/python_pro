from ast import Delete
from multiprocessing import connection
from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_con():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
    )

def all_clear_fields():
    e_Pd.delete(0, "end")
    e_Eid.delete(0, "end")

def clear_fields():
    e_Eid.delete(0, "end")
    e_Pd.delete(0, "end")

print(create_con())

def insert_data():
    if e_Eid.get() == "" or e_Pd.get() == "":
        msg.showerror("Insert Error" , "All fields are mendatory")
    else:
        connection = create_con()
        cursor = connection.cursor()
        query = "insert into logindb (Username,Password) VALUES (%s,%s)"
        args = (e_Eid.get(),e_Pd.get())
        cursor.execute(query,args)
        connection.commit()
        connection.close()
        clear_fields()
        msg.showinfo("Sucess" , "Data added successfully")

def read_data():

    all_clear_fields()

    if e_Eid.get() == "":
        msg.showerror("Email Id ", "Id is Missing a Mendatory")
    else:
        connection = create_con()
        cursor = connection.cursor()
        query = "select * from logindb where Username = %s"
        args = (e_Eid.get(),)
        cursor.execute(query,args)
        rows = cursor.fetchall()
        if rows:
            for i in rows:
                e_Pd.insert(0,i[1])
            connection.close()
        else:
            msg.showinfo("Id Error","Id is missing")
            all_clear_fields()


r=Tk()
r.geometry("400x400")
r.title("MY_Demo")
r.resizable(False,False)
r.configure(bg="brown")


l_n=Label(text="LOGIN_PAGE",font="32px")
l_n.place(x=140,y=20)

l_Eid=Label(r,text="Email_Id :")
l_Eid.place(x
=120,y=70)

e_Eid=Entry(r)
e_Eid.place(x=120,y=100)

l_Pd=Label(r,text="Password :")
l_Pd.place(x=120,y=130)

e_Pd=Entry(r)
e_Pd.place(x=120,y=160)

b1=Button(text="LOGIN",command=insert_data)
b1.place(x=170,y=200)

b2=Button(text="view",command=read_data)
b2.place(x=230,y=200)

r.mainloop()