import tkinter as tk
win = tk.Tk()
win.geometry("500x500+50+50")

C = tk.Canvas(win, bg="white", height=300, width=300)

coord = 10, 10, 300, 300
arc = C.create_arc(coord, start=0, extent=150, fill="red")
arc1 = C.create_arc(coord, start=150, extent=210, fill="Yellow")

C.pack()
win.mainloop()