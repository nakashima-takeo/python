from tkinter import Tk, Frame, Label

root = Tk()

main_frame = Frame(root)
main_frame.pack()

label = Label(main_frame, text="Hello World!")
label.pack()

root.mainloop()