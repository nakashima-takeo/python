from tkinter import Tk, Frame
from first_gui_4 import FirstGUI

def main():
    root = Tk()
    main_frame = Frame(root)
    main_frame.pack()
    
    frame_1 = Frame(main_frame)
    frame_1.pack()

    frame_2 = Frame(main_frame)
    frame_2.pack()

    first_gui_1 = FirstGUI(frame_1, "Frame 1: Hello!")
    first_gui_1.pack()
    
    first_gui_2 = FirstGUI(frame_2, "Frame 2: Hello!")
    first_gui_2.pack()

    root.mainloop()

if __name__ == "__main__":
    main()