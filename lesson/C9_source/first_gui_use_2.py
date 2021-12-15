from tkinter import Tk, Frame
from first_gui_4 import FirstGUI
        
def main():
    root = Tk()
    main_frame = Frame(root)
    main_frame.pack()
    
    frames = []
    first_guis = []
    for i in range(3):
        frames.append(Frame(main_frame))
        frames[i].pack()
        first_guis.append(FirstGUI(frames[i], "Frame {}: Hello!".format(i)))
        first_guis[-1].pack()

    root.mainloop()

if __name__ == "__main__":
    main()