import mysql.connector
import tkinter as tk
from tkinter import messagebox
def hello():
    id=e1.get()
    name=e2.get()
    city=e3.get()
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="Tkinterdb")
    mycursor = mydb.cursor()
    sql = "UPDATE student SET name = %s, city = %s WHERE id = %s"
    data = (name,city,id)
    mycursor.execute(sql,data)
    mydb.commit()
    messagebox.showinfo("","Record Update Successful")
    exit()


win = tk.Tk()
win.geometry("500x500+100+100")
l1=tk.Label(win,text="Insert Record",bg="yellow")
l1.place(x=200,y=10)
l2=tk.Label(win,text="id",bg="yellow")
l2.place(x=100,y=100)
l3=tk.Label(win,text="Name",bg="yellow")
l3.place(x=100,y=200)
l4=tk.Label(win,text="City",bg="yellow")
l4.place(x=100,y=300)
e1=tk.Entry(win,width=20)
e1.place(x=200,y=100)
e2=tk.Entry(win,width=20)
e2.place(x=200,y=200)
e3=tk.Entry(win,width=20)
e3.place(x=200,y=300)
b = tk.Button(win, text='Update', command=hello,height=2,width=20)
b.place(x=200,y=340)
win.mainloop()