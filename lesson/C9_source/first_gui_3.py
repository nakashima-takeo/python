from tkinter import Tk, Frame, Label

class FirstGUI():
    def __init__(self, frame, text):
        label = Label(frame, text=text)
        label.pack()

def main():
    root = Tk()
    main_frame = Frame(root)
    main_frame.pack()
    
    FirstGUI(main_frame, "Hello world!")

    root.mainloop()

if __name__ == "__main__":
    main()