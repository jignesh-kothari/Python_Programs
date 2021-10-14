import mysql.connector
import tkinter as tk
from tkinter import messagebox
def hello():
    mydb=mysql.connector.connect(host="localhost",user="root",password="")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE Tkinterdb")
    messagebox.showinfo("","DataBase Create Successful")

win = tk.Tk()
win.geometry("500x500+50+50")
b = tk.Button(win, text='Create DataBase', command=hello,height=2,width=20)
b.place(x=150,y=200)
win.mainloop()