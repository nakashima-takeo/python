from tkinter import Tk, Frame, Label, Button, Listbox, StringVar, Scrollbar
from tkinter import BROWSE, SINGLE, MULTIPLE, EXTENDED, END
from tkinter import LEFT, RIGHT
from tkinter import X, Y
from tkinter.font import nametofont

from random import randint

def random_color():
    return "#{:02x}{:02x}{:02x}".format(randint(0, 255), randint(0, 255),
         randint(0, 255))

def show_selection():
    print()
    # The current selection 
    # these are indices
    print("Selected:", lbox.curselection())
    # the indices are referring to that list
    print("All options:", lbox.get(0, END))
    # The colors are:
    for i in lbox.curselection():
        print("color {}: {}".format(i, lbox.get(0, END)[i]))

def add_color():
    # Update the list
    colors.append(random_color())
    # Update the Stringvar
    # this is reflected in the Listbox
    colors_var.set(colors)

def animate():
    # Get a list of selected colors indices   
    color_indices = lbox.curselection()

    # if not empty
    if len(color_indices)>0:
        # Get a random color index from the list
        i = randint(0, len(color_indices)-1)
        color_index = color_indices[i]

        # Get the color    
        colors_list = lbox.get(0, END)
        color = colors_list[color_index]
        print("Selected color:", color)
        
        # Update the label
        label["bg"] = color

        # Call animate again after 1000 ms
        # this loops as long as there is at least a selected color
        root.after(1000, animate)
    else:
        # No selected color => stop
        print("no selected color")

root = Tk()

# Set larger default and text font
default_font = nametofont("TkDefaultFont")
text_font = nametofont("TkTextFont")
default_font["size"] = 16
text_font["size"] = 16

root.title("Test Listbox")

frame = Frame(root)
frame.pack()   

label = Label(frame, bg="#000000")
label.pack(fill=X)

lbox_frame = Frame(frame)
lbox_frame.pack()

buttons_frame = Frame(frame)
buttons_frame.pack()

# 1 - Define a list 
colors = []
for i in range(20):
    colors.append(random_color())

# 2 - Put it in a Stringvar
colors_var = StringVar(value=colors)

# 3 - Use the Stringvar to populate the Listbox at instantiation
# Note the height parameter that displays only 3 rows
# Now we have to scroll the listbox
lbox = Listbox(lbox_frame, listvariable=colors_var, height=10, selectmode = MULTIPLE)

lbox.pack(side=LEFT)

# Atttach a scrollbar
# 1 - create
scrollbar = Scrollbar(lbox_frame)
scrollbar.pack(side=RIGHT, fill=Y)
# 2 - when scrolling in listbox 
# call the scrollbar set method
lbox.config(yscrollcommand = scrollbar.set)   
# 3 - when scrolling the scrollbar
# call the listbox yview method
scrollbar.config(command = lbox.yview) 
# You can try to comment out 2 and/or 3 to see what happens

Button(buttons_frame, text = "show selection", command = show_selection).pack(fill=X)
Button(buttons_frame, text = "add color", command = add_color).pack(fill=X)
Button(buttons_frame, text = "animate", command = animate).pack(fill=X)

root.mainloop()

