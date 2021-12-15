from tkinter import Tk, Frame, Label

class FirstGUI(Frame):
    def __init__(self, master=None, text="No text"):
        Frame.__init__(self, master)
        self.createWidget(text)

    def createWidget(self, text):
        label = Label(self, text=text)
        label.pack()

def main():
    root = Tk()
       
    first_gui = FirstGUI(root, text="Hello world!")
    first_gui.pack()

    root.mainloop()

if __name__ == "__main__":
    main()