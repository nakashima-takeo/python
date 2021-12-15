from tkinter import Tk, Label, Button

def red_on_black():
    label["fg"] = "red"
    label["bg"] = "black"

root = Tk()

label = Label(root, text="Hello world!")
label.pack()

Button(root, text="red on black", command = red_on_black).pack()

root.mainloop() 