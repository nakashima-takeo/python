from tkinter import Tk, Label, Button

# Note that we can define the function 
# before label as it is used later
def update_greetings():
    label["text"] = "Bye world!"
    
root = Tk()

label = Label(root, text="Hello world!")
label.pack()

button = Button(root, text="Change greetings", command = update_greetings)
button.pack()

root.mainloop() # The function is used "inside" the mainloop
