#import tkinter
from tkinter import *

#create a main window
r=Tk()
r.geometry("400x400")
r.title("Demon")
r.configure(bg="orange")

#adding label method
rn=Label(r,text="Roll No")
rn.place(x=20,y=20)

fn=Label(r,text="Firstname")
fn.place(x=20,y=60)

ln=Label(r,text="Lastname")
ln.place(x=20,y=100)

em=Label(r,text="Email Id")
em.place(x=20,y=140)

#adding entry method
ern=Entry()
ern.place(x=100,y=20)

frn=Entry()
frn.place(x=100,y=60)

lrn=Entry()
lrn.place(x=100,y=100)

emn=Entry()
emn.place(x=100,y=140)

#adding buttons into main method
b1=Button(r,text="Insert",bg="white")
b1.place(x=20,y=200)

b2=Button(r,text="Update",bg="white")
b2.place(x=80,y=200)

b3=Button(r,text="Delete",bg="white")
b3.place(x=140,y=200)

b4=Button(r,text="Show",bg="white")
b4.place(x=200,y=200)

r.mainloop()
