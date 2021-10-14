import mysql.connector
import tkinter as tk
from tkinter import messagebox
def hello():
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="Tkinterdb")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),city VARCHAR(255))")
    messagebox.showinfo("","Table Create Successful")

win = tk.Tk()
win.geometry("500x500+50+50")
b = tk.Button(win, text='Create Table', command=hello,height=2,width=20)
b.place(x=150,y=200)
win.mainloop()