from tkinter import Tk, Label, Frame
from tkinter import BOTH, X, Y, NONE, W, E, N, S

root = Tk()

frame = Frame(root, bg="black")
frame.grid(row=0, column=0, rowspan=1, columnspan=1, sticky=(N,S,W,E))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

for i in range(7):
    frame.rowconfigure(i, weight=1)
    for j in range(7):
        frame.columnconfigure(j, weight=1)
        if (i * 7 + j) % 2:
            color = "cyan"
        else:
            color = "green"
        Label(frame, text = f"[{i}, {j}]", bg=color).grid(
            row=i, column=j, rowspan=1, columnspan=1,
             sticky=(N,S,W,E), padx=1, pady=1)

Label(frame, text = "Span 7 columns", bg="red").grid( 
    row=7, column=0, rowspan=1, columnspan=7,
     sticky=(N,S,W,E),pady=(3,0))
frame.rowconfigure(7, weight=1)

Label(frame, text = "Span 8 rows", bg="yellow").grid(
    row=0, column=7, rowspan=8, columnspan=1,
    sticky=(N,S,W,E),padx=(3,0))
frame.columnconfigure(7, weight=1)

root.mainloop() 

