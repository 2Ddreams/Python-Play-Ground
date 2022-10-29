import random
from tkinter import *



root = Tk()
root.geometry("700x500")
scrollbar = Scrollbar(root)
def RNG10():

    scrollbar = Scrollbar(root)
    scrollbar.pack( side = RIGHT, fill = Y )

    mylist = Listbox(root, yscrollcommand = scrollbar.set )
    for i in range(10):
        random_num = random.randrange(1, 10)
        mylist.insert(END, "Random Number: " + f"[{random_num}]")   
    mylist.pack( side = LEFT, fill = BOTH )
def RNG100():

    scrollbar = Scrollbar(root)
    scrollbar.pack( side = RIGHT, fill = Y )

    mylist = Listbox(root, yscrollcommand = scrollbar.set )
    for i in range(100):
        random_num = random.randrange(1, 10)
        mylist.insert(END, "Random Number: " + f"[{random_num}]")
    mylist.pack( side = LEFT, fill = BOTH )

def RNG1000():
    

    scrollbar = Scrollbar(root)
    scrollbar.pack( side = RIGHT, fill = Y )
    mylist = Listbox(root, yscrollcommand = scrollbar.set )
    for i in range(1000):
        random_num = random.randrange(1, 10)
        mylist.insert(END, "Random Number: " + f"[{random_num}]")
    mylist.pack( side = LEFT, fill = BOTH )



button = Button(text="Generate 10", command=RNG10)
button1 = Button(text="Generate 100", command=RNG100)
button2 = Button(text="Generate 1000", command=RNG1000)


button.pack(side=BOTTOM)
button1.pack(side=BOTTOM)
button2.pack(side=BOTTOM)

label = Label(text="Select The Number and Press [ctrl + C] to Copy")
label.pack(side=BOTTOM)


mainloop()