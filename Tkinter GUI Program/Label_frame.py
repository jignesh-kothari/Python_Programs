import tkinter as tk 
  
win = tk.Tk()  
win.geometry("500x300")  
  
labelframe1 = tk.LabelFrame(win, text="Frame 1")  
labelframe1.pack()  #fill="both", expand="yes" this is the properties of pack
  
toplabel = tk.Label(labelframe1, text="First frame")  
toplabel.pack()  
b1 = tk.Button(labelframe1,text="Click me")
b1.pack()

labelframe2 = tk.LabelFrame(win, text = "Frame 2")  
labelframe2.pack()  
  
bottomlabel = tk.Label(labelframe2,text = "Second frame")  
bottomlabel.pack()
b2 = tk.Button(labelframe2,text="click me")
b2.pack()  
  
win.mainloop()  