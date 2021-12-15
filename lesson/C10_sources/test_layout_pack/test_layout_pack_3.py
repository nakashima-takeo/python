from tkinter import Tk, Label, Toplevel
from tkinter import LEFT, RIGHT, TOP, BOTTOM

root = Tk()
root.geometry('200x50+0+0')
Label(root, text = "Main window : close to quit", bg = "#f00000", fg="#ffffff").pack()

for i, side in enumerate([LEFT, RIGHT, TOP, BOTTOM]):
        position = '+{}+{}'.format(225, i * 250)
        win = Toplevel(root)
        win.geometry('200x200'+position)
        Label(win, text = "side={}".format(side), bg = "#00f000").pack(side=side)

root.mainloop() 

