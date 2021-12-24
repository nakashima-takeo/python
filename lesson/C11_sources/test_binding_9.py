from tkinter import Tk, Frame, Label, IntVar
from tkinter.font import nametofont


class CounterLabel(Label):
    def __init__(self, master=None, start=0, max_count=10, **kwarg):
        # This time we create a class that inherit from Label
        # kwarg is used to pass a variable number of named arguments
        # to the superclass __init__
        # This is how we pass the relief information
        Label.__init__(self, master, **kwarg)
        
        # This creates the text
        self.counter = start
        self.max_count = max_count
        self.set_text()

        # Bindings
        self.bind("<Button-1>", self.button_callback)
        self.bind_all("<Enter>", self.enter_callback)
       
    def set_text(self):
        self["text"] = "{}/{}".format(self.counter, self.max_count)

    def enter_callback(self, event):
        event.widget.focus_set()
        
    def button_callback(self, event):
        self.counter +=1
        if self.counter == self.max_count:
            self.quit()
        else:
            self.set_text()
   

# Create the UI
root = Tk()

default_font = nametofont("TkDefaultFont")
default_font["size"] = 32
default_font["weight"] = "bold"

root.title("Test Binding 9")

frame = Frame(root)
frame.pack()

# We instantiate our new label here
# Note that we can change named parameters to customize
# our label
label = CounterLabel(frame, relief="ridge", borderwidth=5)
label.pack(fill="x")

# Start the event loop
root.mainloop()