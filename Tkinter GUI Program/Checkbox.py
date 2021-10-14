import tkinter as tk
from tkinter import messagebox 
win = tk.Tk()
win.geometry("550x500+500+200")
win.configure(background='white')
def ckred():    
    # display
    if(chkvalue.get()):
        print("You checked Red")
    else:
        print("You Unchecked Red")
def ckgreen():    
    # display
    if(chkvalue1.get()):
        print("You checked Green")
    else:
        print("You Unchecked Green")
def ckblue():    
    # display
    if(chkvalue2.get()):
        print("You checked Blue")
    else:
        print("You Unchecked Blue")                
chkvalue = tk.BooleanVar()
chkvalue1 = tk.BooleanVar()
chkvalue2 = tk.BooleanVar()
l4 = tk.Checkbutton(win,text="Red", var=chkvalue, command=ckred, selectcolor="cyan", font="elephant",fg="red",bg="gray")
l4.place(x=100,y=100)
l5 = tk.Checkbutton(win,text="green", var=chkvalue1, command=ckgreen, bg="gray", selectcolor="cyan", font="elephant",fg="green")
l5.place(x=100,y=200)
l6 = tk.Checkbutton(win,text="Blue", var=chkvalue2, command=ckblue, bg="gray", selectcolor="cyan", font="elephant",fg="blue")
l6.place(x=100,y=300)
win.mainloop()