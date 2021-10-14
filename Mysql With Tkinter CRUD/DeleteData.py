import mysql.connector
import tkinter as tk
from tkinter import messagebox

def hello():
    id = e1.get()

    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="Tkinterdb")
    mycursor = mydb.cursor()
    
    sql="DELETE FROM student WHERE ID = %s"
    data=(id,)
    mycursor.execute(sql,data)
    mydb.commit()
    messagebox.showinfo("","Record Deleted Successfully")

win = tk.Tk()
win.geometry("500x500+50+50")
l1=tk.Label(win,text="Delete Record",bg="red")
l1.place(x=100,y=10)

l2=tk.Label(win,text="Roll No")
l2.place(x=100,y=100)

e1=tk.Entry(win,width=20)
e1.place(x=200,y=100)

b1 = tk.Button(win, text='Delete Data', command=hello,height=2,width=20)
b1.place(x=150,y=200)

win.mainloop()