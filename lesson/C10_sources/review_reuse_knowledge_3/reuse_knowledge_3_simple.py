from tkinter import Tk, Frame, Label, Button
from tkinter.font import Font 

def red_on_black():
    label["fg"] = "red"
    label["bg"] = "black"

def pink_on_blue():
    label["fg"] = "#ffc0cb"
    label["bg"] = "#0000f0"

def random_color():
    from random import randint
    label["fg"] = "#{:02x}{:02x}{:02x}".format(randint(0, 255), randint(0, 255), randint(0, 255))
    label["bg"] = "#{:02x}{:02x}{:02x}".format(randint(0, 255), randint(0, 255), randint(0, 255))

def reset_color():
    label["fg"] = "#000000"
    label["bg"] = "#F0F0F0"

root = Tk()
root.geometry("300x200")

frame = Frame(root)
frame.pack()

font = Font(family = "Helvetica",size = 36, weight = "bold")

label = Label(frame, text="Hello world!", font = font, padx = 5, pady = 5)
label.pack()

Button(frame, text="red_on_black", width = 30, command = red_on_black).pack()
Button(frame, text="pink_on_blue", width = 30, command = pink_on_blue).pack()
Button(frame, text="random", width = 30, command = random_color).pack()
Button(frame, text="reset", width = 30, command = reset_color).pack()

root.mainloop() 
