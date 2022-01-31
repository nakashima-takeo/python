from tkinter import Tk, Frame, Canvas, Scale, IntVar, DoubleVar
from tkinter import HORIZONTAL, W, E, S, N
from random import randint

class MovingColoredDot(Frame):
    def __init__(self, master=None, width=200, height=200):
        Frame.__init__(self, master)
        self.width = width
        self.height = height
        
        self.smoothing = IntVar(None, -2)

        self.offset = DoubleVar(None, self.width/2), DoubleVar(None, self.height/2)
        
        self.canvas = None
        self.colored_circle = None

        self.create_ui()

        # Binding
        self.canvas.bind("<Motion>", self.motion_callback)
        self.canvas.bind("<Button>", self.button_callback)

    
    def motion_callback(self, event):
        alpha = 10.0**self.smoothing.get()
        self.offset[0].set((1.0 - alpha) * self.offset[0].get()
         + alpha * event.x)
        self.offset[1].set((1.0 - alpha) * self.offset[1].get()
         + alpha * event.y)
        self.move()

    def button_callback(self, event):
        if event.num == 1:
            self.canvas.create_oval(self.get_bbox(), fill=self.random_color(),
                                    tags="addedDot")
            self.canvas.tag_raise(self.colored_circle, "addedDot")       
        elif event.num == 3:
            self.canvas.delete("addedDot")
        else:
            print("Button-{}: No action implemented".format(event.num))

    def random_color(self):
        return "#{:02x}{:02x}{:02x}".format(randint(0, 255), randint(0, 255),
         randint(0, 255))

    def get_bbox(self):# self.offset is changing with mouse movement 
        return (self.offset[0].get()-10, self.offset[1].get()-10,
         self.offset[0].get()+10, self.offset[1].get()+10)

    def create_ui(self):
        self.canvas = Canvas(self, width=self.width, height=self.height,
         bg="black")
        self.canvas.grid(row=0,column=0, sticky=(W,E,S,N))

        # Draw a circle of radius 10
        # centered at (self.offset[0], self.offset[1])
        self.colored_circle = self.canvas.create_oval(self.get_bbox(), fill="red")

        # Create an horizontal scale for smoothing control
        Scale(self, from_=-3, to=0, resolution=1, tickinterval=1,
         orient=HORIZONTAL, variable= self.smoothing).grid(row=1, column=0,
         sticky=(W,E,S,N))
        
    def move(self):
        self.canvas.coords(self.colored_circle, self.get_bbox())
        self.update_idletasks()# Ask to process drawing events 

root = Tk()
root.title("Test Binding 3")

frame = Frame(root)
frame.grid()   

MovingColoredDot(frame).grid()

# Start event loop
root.mainloop()

