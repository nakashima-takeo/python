from tkinter import Tk, Label, Toplevel
from tkinter import BOTH, X, Y, NONE

root = Tk()
root.geometry('200x50+0+0')
Label(root, text = "Main window : close to quit", bg = "#f00000", fg="#ffffff").pack()

for i, fill in enumerate([NONE, X, Y, BOTH]):
    for j, expand in enumerate([False, True]):
        position = '+{}+{}'.format(225 + j * 225, i * 250)
        win = Toplevel(root)
        win.geometry('200x200'+position)
        Label(win, text = "fill={}\nexpand={}".format(fill, expand),
         bg = "#00f000").pack(fill=fill, expand = expand)

root.mainloop() 

