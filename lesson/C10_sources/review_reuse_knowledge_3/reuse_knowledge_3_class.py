from tkinter import Tk, Frame, Label, Button
from tkinter.font import Font 

class MyGUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.label = None
        self.create_widgets()

    def update_label_color(self, fg, bg):
        self.label["fg"] = fg
        self.label["bg"] = bg
        print(f"fg {fg} bg {bg}")

    def rand_color(self):
        from random import randint
        return "#{:02x}{:02x}{:02x}".format(randint(0, 255), randint(0, 255), randint(0, 255))        

    def pick_color(self, title, color):
        from tkinter.colorchooser import askcolor
        return askcolor(color, title=title)[1]    

    def create_widgets(self):
        font = Font(
            family = "Helvetica",
            size = 36,
            weight = "bold"
            )
        
        self.label = Label(
            self,
            text="Hello world!",
            font = font,
            padx = 5,
            pady = 5
            )

        self.label.pack()

        def f1():
            self.update_label_color("red", "black")

        Button(
            self,
            text="red_on_black",
            width = 30,
            command = f1
        ).pack()
        
        Button(
            self,
            text="pink_on_blue",
            width = 30,
            command = lambda : self.update_label_color(
             "#ffc0cb", "#0000f0"
            )
        ).pack()

        Button(
            self,
            text="random",
            width = 30,
            command = lambda : self.update_label_color(
             self.rand_color(),
             self.rand_color()
             )
         ).pack()

        Button(
            self,
            text="choose",
            width = 30,
            command = lambda : self.update_label_color(
            self.pick_color("Foreground", "#000000"),
            self.pick_color("Background", "#f0f0f0")
            )
         ).pack()

        Button(
            self,
            text="reset",
            width = 30,
            command = lambda : self.update_label_color(
                "#000000",
                "#f0f0f0"
            )
        ).pack()

def main():
    root = Tk()
    root.geometry("300x200")

    frame = Frame(root)
    frame.pack()

    MyGUI(frame).pack()

    root.mainloop() 

if __name__ == "__main__":
    main()