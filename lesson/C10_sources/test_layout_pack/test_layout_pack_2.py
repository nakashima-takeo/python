from tkinter import Tk, Label
from tkinter import BOTH, X, Y, NONE

root = Tk()
root.geometry('200x200')

Label(root, text = "fill=BOTH\nexpand=True", bg="red").pack(fill=BOTH, expand=True)
Label(root, text = "fill=X\nexpand=False", bg="green").pack(fill=X, expand=False)
Label(root, text = "fill=NONE\nexpand=False", bg="pink").pack(fill=NONE, expand=False)
Label(root, text = "fill=Y\nexpand=True", bg="cyan").pack(fill=Y, expand=True)
Label(root, text = "fill=BOTH\nexpand=True", bg="blue").pack(fill=BOTH, expand=True)

root.mainloop() 

