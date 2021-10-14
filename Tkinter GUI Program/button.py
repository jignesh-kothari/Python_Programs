import tkinter as tk
from tkinter import messagebox

def hello():
    msg = e1.get()
    l1 = tk.Label(win, bg="yellow",text=msg, width=20)
    l1.place(x = 50, y = 250)
win = tk.Tk()
win.geometry("500x500+50+50")
e1 = tk.Entry(win, bg="yellow",width=20)
e1.place(x = 50, y = 50)  
b1 = tk.Button(win, text = "Click Me", command=hello, bg="red", fg="yellow", activebackground="green", height=5, width=20)
b1.place(x = 50, y = 100)

win.mainloop()