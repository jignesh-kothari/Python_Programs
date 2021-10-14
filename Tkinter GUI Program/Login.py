import tkinter as tk
from tkinter import messagebox

def hello():
    l1 = tk.Label(win, bg="yellow",text=msg, width=20)
    l1.place(x = 50, y = 250)
win = tk.Tk()
win.geometry("500x500+50+50")
l2 = tk.Label(win, bg="yellow",text="username", width=20)
l2.place(x = 50, y = 50)
l3 = tk.Label(win, bg="yellow",text="password", width=20)
l3.place(x = 50, y = 100)
e1 = tk.Entry(win, bg="yellow",width=20)
e1.place(x = 250, y = 50)
e2 = tk.Entry(win, bg="yellow",width=20)
e2.place(x = 250, y = 100)  
b1 = tk.Button(win, text = "Login ", command=hello, bg="red", fg="yellow", activebackground="green",  width=10)
b1.place(x = 70, y = 150)
b2 = tk.Button(win, text = "Cancel ", command=hello, bg="red", fg="yellow", activebackground="green",  width=10)
b2.place(x = 270, y = 150)

win.mainloop()