from tkinter import Tk, Frame, Label, IntVar
from tkinter.font import nametofont


class CounterLabel(Frame):
    def __init__(self, master=None, start=0, max_count=10):
        # This class inherit from Frame
        Frame.__init__(self, master)
        
        self.counter = start
        self.max_count = max_count

        # We have a child label in the ui
        self.label = None
        self.create_ui()

        # update the text
        self.set_text()

        # bindings
        self.label.bind("<Button-1>", self.button_callback)
        self.label.bind_all("<Enter>", self.enter_callback)

    def create_ui(self):
        # We create and place the child Label with relief
        self.label = Label(self, relief="ridge", borderwidth=5)
        self.label.pack(fill="x")

    def set_text(self):
        # Update the text of the label
        self.label["text"] = "{}/{}".format(self.counter, self.max_count)

    # callbacks
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

root.title("Test Binding 8")

frame = Frame(root)
frame.pack()

# We instantiate a class
CounterLabel(frame).pack(fill="x")


# Start the event loop
root.mainloop()