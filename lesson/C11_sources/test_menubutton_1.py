from tkinter import Tk, Frame, Canvas, Menu, Menubutton

root = Tk()

root.title("Test Menubutton")

frame = Frame(root)
frame.pack()   

Canvas(frame, width = 400, height= 300, bg = "black").pack()


menubutton = Menubutton(frame, text = "show menu", relief="raised")

# The menu is a child of menubutton
menu = Menu(menubutton, tearoff=0)

# create the entries
menu.add_command(label = "new", command=lambda : print("new"))
menu.add_separator()
menu.add_command(label = "save", command=lambda : print("save"))
menu.add_command(label = "load", command=lambda : print("load"))

# set the menu attribute
menubutton["menu"] = menu

menubutton.pack()

root.mainloop()

