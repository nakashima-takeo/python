from tkinter import Tk, Frame, Canvas, Button, Menu, BooleanVar, StringVar

class TestMenu(Menu):
    def __init__(self, master=None):
        Menu.__init__(self, master=master)

        self.check1 = BooleanVar(None, True)
        self.check2 = BooleanVar(None, False)
        self.color = StringVar(None, "black")

        self.create_menu()

    def create_menu(self):
        file_menu = Menu(self, tearoff = 0)

        file_menu.add_command(label = "new", command=self.new)
        file_menu.add_separator()
        file_menu.add_command(label = "save", command=self.save)
        file_menu.add_command(label = "load", command=self.load)

        self.add_cascade(label="File", menu=file_menu)

        option_menu = Menu(self, tearoff = 0)

        option_menu.add_checkbutton(label = "check 1", variable = self.check1, command=self.checkbutton_cb)
        option_menu.add_checkbutton(label = "check 2", variable = self.check2, command=self.checkbutton_cb)

        self.add_cascade(label="Option", menu=option_menu)

        color_menu = Menu(self, tearoff = 0)

        color_menu.add_radiobutton(label = "black", variable = self.color, value="black", command=self.radiobutton_cb)
        color_menu.add_radiobutton(label = "red", variable = self.color, value="red", command=self.radiobutton_cb)
        color_menu.add_radiobutton(label = "green", variable = self.color, value="green", command=self.radiobutton_cb)
        color_menu.add_radiobutton(label = "blue", variable = self.color, value="blue", command=self.radiobutton_cb)
        color_menu.add_separator()
        color_menu.add_command(label = "reset", command=lambda : self.color.set("black"))
        color_menu.add_separator()

        color_option = Menu(color_menu, tearoff = 0)
        color_option.add_command(label = "light", command = lambda : print("color option light"))
        color_option.add_command(label = "dark", command = lambda : print("color option dark"))
    
        color_menu.add_cascade(label="more options", menu=color_option)


        self.add_cascade(label="Color", menu=color_menu)

    def new(self):
        print("new")
    def save(self):
        print("save")
    def load(self):
        print("load")

    def checkbutton_cb(self):
        if self.check1.get():
            print("check 1 enable")
        else:
            print("check 1 disable")

        if self.check2.get():
            print("check 2 enable")
        else:
            print("check 2 disable")

    def radiobutton_cb(self):
        print(self.color.get())


def main():
    root = Tk()
    
    root.title("Test Menu")

    frame = Frame(root)
    frame.pack()   

    Canvas(frame, width = 400, height= 300, bg = "black").pack()

    Button(frame, text = "draw", command=lambda : print("Draw")).pack()

    test_menu = TestMenu(frame)

    root.config(menu = test_menu)

    root.mainloop()

if __name__ == '__main__':
    main()