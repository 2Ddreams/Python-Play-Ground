from tkinter import *
from tkinter.ttk import *

root = Tk()

slider = Scale(root, from_=0, to=100)
slider.pack()
print(slider.get())
btn = Button(root, text="SHOW VALUE", command=lambda: print(round(slider.get())))
btn.pack()

lastx, lasty = 0, 0

def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y), width=round(slider.get()))
    lastx, lasty = event.x, event.y

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)

root = Tk()

windows = Toplevel(root)

btn = Button(root, text="New Window", command = lambda: Toplevel(root))
btn.pack()
mainloop()