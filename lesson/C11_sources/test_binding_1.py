from tkinter import Tk, Frame, Label, Button
from tkinter.font import nametofont

# Define callback functions for the different events
def keypress_callback(event):
    print("Widget {} pressed {} at [{},{}]".format(event.widget.winfo_name(),
     event.keysym, event.x, event.y))

def enter_callback(event):
    print("Entered Widget {} at [{},{}]".format(event.widget.winfo_name(),
     event.x, event.y))
    event.widget.focus_set() # This set the focus

def button_1_callback(event):
    print("Clicked Widget {} at [{},{}]".format(event.widget.winfo_name(),
     event.x, event.y))

# Create the UI
root = Tk()

default_font = nametofont("TkDefaultFont")
default_font["size"] = 32
default_font["weight"] = "bold"

root.title("Test Binding 1")

frame1 = Frame(root, name="frame1")
frame1.pack()

label1 = Label(frame1, name="label1", text = "label1", relief="ridge",
 borderwidth=5)
label1.pack(fill="x")

label2 = Label(frame1, name="label2", text = "label2", relief="ridge",
 borderwidth=5)
label2.pack(fill="x")

button1 = Button(frame1, text="button1", name="button1", relief="raised",
 borderwidth=5, command=lambda : print("Clicked button1"))
button1.pack(fill="x") 


# Define bindings
label2.bind("<KeyPress>", keypress_callback)
root.bind_class("Label", "<Button-1>", button_1_callback)
root.bind_all("<Enter>", enter_callback)

# Start the event loop
root.mainloop()