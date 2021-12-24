from tkinter import Tk, Frame, Canvas, Button, Menu

class TestMenu(Menu):
    """Class defining the menu
    """
    def __init__(self, master=None):
        Menu.__init__(self, master=master)

        self.create_menu()

    def create_menu(self):
        self.add_command(label = "save", command=self.save)
        self.add_command(label = "load", command=self.load)
        self.add_command(label = "exit", command=self.exit)

    def save(self):
        print("save")
    def load(self):
        print("load")
    def exit(self):
        print("exit")


def main():
    root = Tk()
    
    root.title("Test Menu")

    frame = Frame(root)
    frame.pack()   

    Canvas(frame, width = 400, height= 300, bg = "black").pack()

    Button(frame, text = "draw", command=lambda : print("Draw")).pack()

    # instance of the custom menu
    test_menu = TestMenu(frame)

    # set the menu attribute of the window
    root.config(menu = test_menu)

    root.mainloop()

if __name__ == '__main__':
    main()