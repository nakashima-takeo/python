from tkinter import Tk, Frame, Label, IntVar
from tkinter.font import nametofont

# Define callback functions for the different events
def enter_callback(event):
    event.widget.focus_set()

def button_callback(event):
    # We modify the value of the counter using an object
    # There is no assignment and we do not create a local variable
    counter.set(counter.get()+1)
    if counter.get() == max_count:
        root.quit()
    else:
        label["text"] = "{}/{}".format(counter.get(), max_count)
   
# Define parameters
max_count = 10

# Create the UI
root = Tk()

# This has to be after the tkinter main window
# is created by using Tk()
counter = IntVar(0)

default_font = nametofont("TkDefaultFont")
default_font["size"] = 32
default_font["weight"] = "bold"

root.title("Test Binding 7")

frame = Frame(root)
frame.pack()

# We create the label 
# set the text using the IntVar
# add relief
label = Label(frame, text = "{}/{}".format(counter.get(), max_count),
 relief="ridge", borderwidth=5)
label.pack(fill="x")


# Define bindings
label.bind("<Button-1>", button_callback)
root.bind_all("<Enter>", enter_callback)

# Start the event loop
root.mainloop()