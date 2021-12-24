from tkinter import Tk, Frame, Label
from tkinter import Button, Checkbutton, Radiobutton
from tkinter import BooleanVar, StringVar
from tkinter.font import Font, nametofont
from tkinter import LEFT, W 

class TestButtons(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=master)
        self.info_label = None

        self.font = None
        
        self.is_bold = BooleanVar(None, False)

        self.color = StringVar(None, "black")

        self.create_ui()

    def create_ui(self):
        # Create the font
        # we need it to modify the size and weight
        self.font = Font(family="Times",size=32, weight="normal")
        self.info_label = Label(self, text = "Hello button test!",
            font = self.font, fg=self.color.get())
        self.info_label.grid(row=0, column=0)

        # These two buttons use the same method in their callback
        # The lambda function let us give a different parameter to the callback
        Button(self, text = "bigger", 
        command=lambda : self.button_callback("bigger")).grid(row=1,
         column=0)
        Button(self, text = "smaller",
        command=lambda : self.button_callback("smaller")).grid(row=2,
         column=0)

        Checkbutton(self, text = "bold", variable = self.is_bold, 
        onvalue = True, offvalue = False, command=self.check_callback).grid(
            row=3, column=0)

        # The frame is not necessary
        # it is just a way to indicate graphically that the 3 radiobuttons 
        # belong of the same group
        radio_frame = Frame(self, borderwidth=3, bg="#c0c0c0")
        radio_frame.grid(row=4, column=0)

        Radiobutton(radio_frame, text = "black", justify = LEFT, bg="#c0c0c0", 
        var = self.color, value = "black", command = self.radio_button_callback
        ).grid(row=0, column=0, sticky=W)

        Radiobutton(radio_frame, text = "red", justify = LEFT, bg="#c0c0c0", 
        var = self.color, value = "red", command = self.radio_button_callback
        ).grid(row=1, column=0, sticky=W)

        Radiobutton(radio_frame, text = "blue", justify = LEFT, bg="#c0c0c0",
        var = self.color, value = "blue", command = self.radio_button_callback
        ).grid(row=2, column=0, sticky=W)

    def button_callback(self, command):
        if command == "smaller":
            self.font["size"] -= 1
        elif command == "bigger":
            self.font["size"] += 1

    def check_callback(self):
        if self.is_bold.get():
            self.font["weight"] = "bold"
        else:
            self.font["weight"] = "normal"

    def radio_button_callback(self):
        self.info_label["fg"] = self.color.get()


def main():
    root = Tk()

    # This is a way to set the parameter of the default font
    # 1) create a variable to access it
    default_font = nametofont("TkDefaultFont")
    # 2) change its attribute
    default_font["size"] = 16

    root.title("Test Buttons")

    TestButtons(root).grid()

    root.mainloop()

if __name__ == '__main__':
    main()