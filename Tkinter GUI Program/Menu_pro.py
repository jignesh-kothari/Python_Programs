import tkinter as tk
import subprocess as sp
win = tk.Tk() 
win.geometry("500x500")

def hello():
    programName = "notepad.exe"
    sp.Popen(programName)
def hello1():
    programName = "explorer.exe"
    sp.Popen(programName)
b1=tk.Button(win,text="Open Notepad",command=hello)
b1.place(x=100,y=100)
b2=tk.Button(win,text="Open Explorer",command=hello1)
b2.place(x=200,y=100)
win.mainloop()