from tkinter import Tk, Label

root = Tk()

label = Label(root, text="Hello World!")
label.pack()

print(dir(root))
print(dir(label))

root.mainloop()