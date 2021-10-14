import tkinter as tk
from tkinter import messagebox 
win = tk.Tk()
win.geometry("550x500+500+200")
win.configure(background='white')
def chk():    
    # display
    if(Red.get() and Green.get() and Blue.get()):
        print("You checked Red green and Blue")
    elif(Red.get() and Green.get()):
        print("You checked Red and green")
    elif(Red.get() and Blue.get()):
        print("You checked Red and Blue")
    elif(Green.get() and Blue.get()):
        print("You checked Green and Blue")
    elif(Green.get()):
        print("You checked Green")    
    elif(Blue.get()):
        print("You checked Blue")
    elif(Red.get()):
        print("You checked Red")
    else:
        print("You Unchecked All")                 
Red = tk.BooleanVar()
Green = tk.BooleanVar()
Blue = tk.BooleanVar()
l4 = tk.Checkbutton(win,text="Red", var=Red, command=chk, selectcolor="cyan", font="elephant",fg="red",bg="gray")
l4.place(x=100,y=100)
l5 = tk.Checkbutton(win,text="green", var=Green, command=chk, bg="gray", selectcolor="cyan", font="elephant",fg="green")
l5.place(x=100,y=200)
l6 = tk.Checkbutton(win,text="Blue", var=Blue, command=chk, bg="gray", selectcolor="cyan", font="elephant",fg="blue")
l6.place(x=100,y=300)
win.mainloop()
