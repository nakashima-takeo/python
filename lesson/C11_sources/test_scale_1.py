from tkinter import Tk, Frame, Canvas, Scale, DoubleVar
from tkinter import HORIZONTAL, W, E, S, N

def move(value): # the value is not used as we use h_offset and v_offset
    nc = h_offset.get()-10, v_offset.get()-10, h_offset.get()+10, v_offset.get()+10
    canvas.coords(red_circle, nc)

root = Tk()
root.title("Test Scale 1")

frame = Frame(root)
frame.grid()   

# Define tkinter variable for the scales
v_offset = DoubleVar(None, 100.0)
h_offset = DoubleVar(None, 100.0)

# Create canvas
canvas = Canvas(frame, width=200, height=200, bg="black")
canvas.grid(row=0,column=0, sticky=(W,E,S,N))

# Draw a circle of radius 10 centered at (h_offset, v_offset)
# We keep the object id in a variable for easy access
red_circle = canvas.create_oval(h_offset.get()-10, v_offset.get()-10,
 h_offset.get()+10, v_offset.get()+10, fill="red")

# Create vertical and horizontal scales
# use the tkinter DoubleVar for setting the initial value
# the move function get a value from the scale
# but we will ignore it as we have the DoubleVar
v_scale = Scale(frame, from_=0, to=200, variable= v_offset, command = move)
v_scale.grid(row=0,column=1, sticky=(W,E,S,N))
 
h_scale = Scale(frame, from_=0, to=200, orient=HORIZONTAL, variable= h_offset,
 command = move)
h_scale.grid(row=1,column=0, sticky=(W,E,S,N))

# Start event loop
root.mainloop()

