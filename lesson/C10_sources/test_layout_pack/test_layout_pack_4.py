from tkinter import Tk, Label, Frame
from tkinter import BOTH, X, Y, NONE
from tkinter import LEFT, RIGHT, TOP, BOTTOM

root = Tk()
root.geometry('200x200')

top_frame = Frame(root)
top_frame.pack(side=TOP, fill=BOTH, expand=True)
middle_frame = Frame(root)
middle_frame.pack(fill=BOTH, expand=False)
bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM, fill=X, expand=False)

Label(top_frame, text = "fill=BOTH\nexpand=True", bg="red").pack(side=TOP, fill=BOTH, expand=True)
Label(top_frame, text = "fill=NONE\nexpand=True", bg="yellow").pack(side=TOP, fill=NONE, expand=True)


Label(middle_frame, text = "fill=X\nexpand=False", bg="cyan").pack(side=LEFT, fill=X, expand=False)
Label(middle_frame, text = "fill=X\nexpand=True", bg="green").pack(side=RIGHT, fill=X, expand=True)

Label(bottom_frame, text = "fill=X\nexpand=False", bg="blue").pack(side=LEFT, fill=X, expand=False)
Label(bottom_frame, text = "fill=X\nexpand=False", bg="blue").pack(side=RIGHT, fill=X, expand=False)
Label(bottom_frame, text = "fill=X\nexpand=True", bg="yellow").pack(side=RIGHT, fill=X, expand=True)

root.mainloop() 

