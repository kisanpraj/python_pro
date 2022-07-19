from multiprocessing import connection
from operator import ge
from os import curdir
from pydoc import cram
from sqlite3 import Cursor
from webbrowser import get
import mysql.connector
from tkinter import *
import tkinter.messagebox as msg





def create_con():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
    )

print(create_con())

def all_clear_fields():
    e_id.delete(0,"end")
    e_fn.delete(0,"end")
    e_ln.delete(0,"end")
    e_ph.delete(0,"end")


def clear_fields():
    e_fn.delete(0,"end")
    e_ln.delete(0,"end")
    e_ph.delete(0,"end")

#insert data
def insert_data():
    if e_fn.get() == "" or e_ln.get() == "" or e_ph.get() == "" :
        msg.showerror("Insert Error","All fields are mendatory")
    else:
        connection = create_con()
        cursor = connection.cursor()
        query = "insert into studb (firstname,lastname,pnum) values (%s, %s, %s)"
        args = (e_fn.get(), e_ln.get(), e_ph.get())
        cursor.execute(query,args)
        connection.commit()
        connection.close()
        clear_fields()
        msg.showinfo("Success","Data added successfully")

#data view
def read_data():
    
    clear_fields()

    if e_id.get() == "":
        msg.showerror("Id Missing","id is mendatory to search the data")
    else:
        connection = create_con()
        cursor = connection.cursor()
        query = "select * from studb where id=%s"
        args = (e_id.get(),)
        cursor.execute(query,args)
        rows = cursor.fetchall()
        #print(rows)
        if rows:
            for i in rows:
                e_fn.insert(0,i[1])
                e_ln.insert(0,i[2])
                e_ph.insert(0,i[3])
            connection.close()
        else:
            msg.showinfo("id Error","id not found")
            all_clear_fields()

def update_data():
    if e_id.get() == "" or e_fn.get() == "" or e_ln.get() == "" or e_ph.get() == "":
        msg.showerror("Missing Fields","Please use id to search the data and then update it")
    else:
        connection = create_con()
        cursor = connection.cursor()
        query = "update studb set firstname=%s,lastname=%s,pnum=%s where id=%s"
        args = (e_fn.get(),e_ln.get(),e_ph.get(),e_id.get())
        cursor.execute(query,args)
        connection.commit()
        connection.close()
        all_clear_fields()
        msg.showinfo("Success","Data updated successfully")

def delete_data():
    if e_id.get() == "" or e_fn.get() == "" or e_ln.get() == "" or e_ph.get() == "":
        msg.showerror("Missing Fields","Please use id to search the data and than delete it")
    else:
        connection = create_con()
        cursor = connection.cursor()
        query = "delete from studb where id=%s"
        args = (e_id.get(),)
        cursor.execute(query,args)
        connection.commit()
        connection.close()
        all_clear_fields()
        msg.showinfo("Missing","Data deleted successfully")


            
        


        

        

    
r=Tk()
r.geometry("400x400")
r.title("demo")
r.resizable(False,False)

id=Label(r,text="id")
id.place(x=20,y=20)

e_id=Entry(r)
e_id.place(x=100,y=20)

fn=Label(r,text="Firstname")
fn.place(x=20,y=50)

e_fn=Entry(r)
e_fn.place(x=100,y=50)

ln=Label(r,text="Lastname")
ln.place(x=20,y=80)

e_ln=Entry(r)
e_ln.place(x=100,y=80)

ph=Label(r,text="P_Number")
ph.place(x=20,y=120)

e_ph=Entry(r)
e_ph.place(x=100,y=120)

INSERT=Button(r,text="INSERT",command=insert_data,bg="black",fg="white")
INSERT.place(x=40,y=150)

VIEW=Button(r,text="VIEW",command=read_data,bg="black",fg="white")
VIEW.place(x=100,y=150)

UPDATE=Button(r,text="UPDATE",command=update_data,bg="black",fg="white")
UPDATE.place(x=150,y=150)

DELETE=Button(r,text="DELETE",command=delete_data,bg="black",fg="white")
DELETE.place(x=220,y=150)

r.mainloop()