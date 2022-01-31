from tkinter import Tk, Frame, Canvas, Scale, DoubleVar
from tkinter import HORIZONTAL, W, E, S, N

class MovingRedDot(Frame):
    def __init__(self, master=None, width=200, height=200):
        Frame.__init__(self, master)
        self.width = width
        self.height = height

        self.offset = DoubleVar(None, self.width/2), DoubleVar(None, self.height/2)
        
        self.canvas = None
        self.red_circle = None

        self.create_ui()

    def get_bbox(self):# the scale values are reflected here with self.offset 
        return (self.offset[0].get()-10, self.offset[1].get()-10,
         self.offset[0].get()+10, self.offset[1].get()+10)

    def create_ui(self):
        self.canvas = Canvas(self, width=self.width, height=self.height, bg="black")
        self.canvas.grid(row=0,column=0, sticky=(W,E,S,N))

        # Draw a circle of radius 10
        # centered at (self.offset[0], self.offset[1])
        self.red_circle = self.canvas.create_oval(self.get_bbox(), fill="red")

        # Create vertical and horizontal scales
        # use the tkinter DoubleVar for setting the initial value
        # the move function get a value from the scale
        # but we will ignore it as we have the DoubleVar in self.offset
        Scale(self, from_=0, to=self.width, orient=HORIZONTAL,
         variable= self.offset[0], command = self.move).grid(row=1, column=0,
         sticky=(W,E,S,N))

        Scale(self, from_=0, to=self.height, variable= self.offset[1],
        command = self.move).grid(row=0,column=1, sticky=(W,E,S,N))
        
    def move(self, value): # the value is not used as we use the DoubleVar
        self.canvas.coords(self.red_circle, self.get_bbox())

root = Tk()
root.title("Test Scale 2")

frame = Frame(root)
frame.grid()   

MovingRedDot(frame).grid()

# Start event loop
root.mainloop()

