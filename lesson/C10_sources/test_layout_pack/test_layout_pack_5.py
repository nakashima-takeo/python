from tkinter import Tk, Label, Frame
from tkinter import BOTH, X, Y, NONE

root = Tk()
root.geometry('200x200')

frame = Frame(root)
frame.pack(fill=BOTH, expand=True)

Label(frame, text = "nw", bg="red").pack(fill=None, expand=True, anchor="nw", padx=10, pady=5)
Label(frame, text = "e", bg="cyan").pack(fill=None, expand=True, anchor="e", padx=10, pady=5)
Label(frame, text = "s", bg="green").pack(fill=None, expand=True, anchor="s", padx=10, pady=5)

root.mainloop() 

