from tkinter import Tk, Frame, Label, Button, Text
from tkinter import END
from tkinter.font import nametofont

def show_info():
    print(text.get(1.0, END))

root = Tk()

# Set larger default and fixed font
default_font = nametofont("TkDefaultFont")
fixed_font = nametofont("TkFixedFont")
default_font["size"] = 16
fixed_font["size"] = 16

root.title("Test Text")

frame = Frame(root)
frame.pack()   

Label(frame, text="Type your text and submit:").pack()

# Create a text box
text = Text(frame, width=30, height=10)
text.pack()

Button(frame, text="Submit", command=show_info).pack()


root.mainloop()

