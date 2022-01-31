from tkinter import Tk, Frame, Button, Spinbox, StringVar
from tkinter import BROWSE, SINGLE, MULTIPLE, EXTENDED, END
from tkinter.font import nametofont

def show_info():
    print("spinbox1:", spinval1.get())
    print("spinbox2:", spinval2.get())

root = Tk()

# Set larger default and text font
default_font = nametofont("TkDefaultFont")
text_font = nametofont("TkTextFont")
default_font["size"] = 16
text_font["size"] = 16

root.title("Test Listbox")

frame = Frame(root)
frame.pack()

spinval1 = StringVar()
sbox1 = Spinbox(frame, from_=1.0, to=10.0, textvariable=spinval1)
sbox1.pack()

colors = ["black", "white", "red", "green", "blue"]
spinval2 = StringVar()
sbox2 = Spinbox(frame, values=colors, textvariable=spinval2)
sbox2.pack()

Button(frame, text="Get", command=show_info).pack()


root.mainloop()

