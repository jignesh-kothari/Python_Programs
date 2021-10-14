import mysql.connector
import tkinter as tk
from tkinter import messagebox
def hello():
    name=e1.get()
    city=e2.get()
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="Tkinterdb")
    mycursor = mydb.cursor()
    sql="INSERT INTO student(name,city) VALUES (%s,%s)"
    data=(name,city)
    mycursor.execute(sql,data)
    mydb.commit()
    messagebox.showinfo("","Record Inserted Successful")
    exit()


win = tk.Tk()
win.geometry("500x500+100+100")
l1=tk.Label(win,text="Insert Record",bg="yellow")
l1.place(x=200,y=10)
l2=tk.Label(win,text="Name",bg="yellow")
l2.place(x=100,y=100)
l3=tk.Label(win,text="City",bg="yellow")
l3.place(x=100,y=200)
e1=tk.Entry(win,width=20)
e1.place(x=200,y=100)
e2=tk.Entry(win,width=20)
e2.place(x=200,y=200)
b = tk.Button(win, text='Insert', command=hello,height=2,width=20)
b.place(x=150,y=340)
win.mainloop()