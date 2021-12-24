from tkinter import Tk, Frame, Label, Button

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.counter = 0
        self.createWidgets()

    def createWidgets(self):
        self.label = Label(self, width = 20, text=str(self.counter))
        self.label.pack()

        increment_button = Button(self, text = "Increment", command = self.increment)
        increment_button.pack()

        #Compact way to define the button
        #Button(self, text = "Reset", command = self.reset).pack()

        # Alternative way to define the button
        reset_button = Button(self)

        # Then set the "attributes"
        reset_button["text"] = "Reset"

        # Equivalent notations:
        # use dict style
        # reset_button["width"] = 10
        # Use config method
        # reset_button.config(width = 10)

        reset_button["command"] = self.reset

        # and pack
        reset_button.pack()



    def increment(self):
        self.counter += 1
        self.update_label()# Call to update the label

    def reset(self):
        self.counter = 0
        self.update_label()

    def update_label(self):
        self.label["text"] = str(self.counter)
        #Alternative way
        #self.label.config(text = str(self.counter))

def main():
    root = Tk()
    app = Application(root)
    app.mainloop()
    # The main_loop can be called from other tkinter
    # component. Here a subclass of Frame

if __name__ == "__main__":
    main()