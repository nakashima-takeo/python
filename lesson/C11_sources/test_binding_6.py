from tkinter import Tk, Frame, Label
from tkinter.font import nametofont

# Define callback functions for the different events
def enter_callback(event):
    event.widget.focus_set()

def button_callback(event):
    # We want to modify the counter outside the function
    # So we must tell that we use the global counter
    # Otherwise the assignment will create a local variable
    global counter 
    counter += 1 
    if counter == max_count:
        root.quit()
    else:
        label["text"] = "{}/{}".format(counter, max_count)
   
# Define parameters
counter = 0 # This is defined in the global namespace
max_count = 10

# Create the UI
root = Tk()

default_font = nametofont("TkDefaultFont")
default_font["size"] = 32
default_font["weight"] = "bold"

root.title("Test Binding 6")

frame = Frame(root)
frame.pack()

# We create the label 
# set the text
# add relief
label = Label(frame, text = "{}/{}".format(counter, max_count),
 relief="ridge", borderwidth=5)
label.pack(fill="x")


# Define bindings
label.bind("<Button-1>", button_callback)
root.bind_all("<Enter>", enter_callback)

# Start the event loop
root.mainloop()