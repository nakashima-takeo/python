from tkinter import Tk, Frame, Label, Button, Entry, StringVar
from tkinter.font import nametofont

# Define callback function
def return_callback(event):
    label1["text"] = entry1_value.get()
    
# Create the UI
root = Tk()

default_font = nametofont("TkDefaultFont")
default_font["size"] = 36
default_font["weight"] = "bold"
text_font = nametofont("TkTextFont")
text_font["size"] = 12
text_font["weight"] = "normal"

root.title("Test Binding 2")

frame1 = Frame(root, name="frame1")
frame1.pack(fill="x")

label1 = Label(frame1, name="label1", text = "")
label1.pack(fill="x")

entry1_value = StringVar(None, "Type here")
entry1 = Entry(frame1, textvariable=entry1_value)
entry1.pack(fill="x")

# Define binding
entry1.bind("<Return>", return_callback)

# Start the event loop
root.mainloop()