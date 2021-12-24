from tkinter import Tk, Frame, Button, Listbox
from tkinter import BROWSE, SINGLE, MULTIPLE, EXTENDED, END
from tkinter.font import nametofont

def show_selection():
    print("Selected:", lbox.curselection())
    print("All options:", lbox.get(0, END))

root = Tk()

# Set larger default and text font
default_font = nametofont("TkDefaultFont")
text_font = nametofont("TkTextFont")
default_font["size"] = 16
text_font["size"] = 16

root.title("Test Listbox")

frame = Frame(root)
frame.pack()   

# Try the different selection modes: BROWSE, SINGLE, MULTIPLE, EXTENDED
lbox = Listbox(frame, selectmode = MULTIPLE)
lbox.insert(0, "black")
lbox.insert(1, "white")
lbox.insert(2, "red")
lbox.insert(3, "green")
lbox.insert(4, "blue")

lbox.pack()

Button(frame, text = "show selection", command = show_selection).pack()

root.mainloop()

