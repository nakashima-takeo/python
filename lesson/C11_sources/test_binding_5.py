from tkinter import Tk, Frame, Canvas, Scale, DoubleVar
from tkinter import HORIZONTAL, W, E, S, N
from random import randint

class MovingColoredDot(Frame):
    def __init__(self, master=None, width=200, height=200):
        Frame.__init__(self, master)
        self.width = width
        self.height = height
        
        self.radius = 5
        self.offset = DoubleVar(None, self.width/2), DoubleVar(None, self.height/2)

        # drawing is off at start
        self.is_drawing = False
        # no color selected
        self.pencil_color = None
        self.pencil_width = 3

        self.canvas = None
        self.colored_circle = None

        self.create_ui()

        # Binding
        self.canvas.bind("<Motion>", self.motion_callback)
        self.canvas.bind("<Button>", self.button_callback)

    
    def motion_callback(self, event):
        if self.is_drawing:
            # When drawing is on
            
            # Draw from previous position
            start_point = self.offset[0].get(), self.offset[1].get()
            # to mouse position
            end_point = event.x, event.y
            # tag the object to enable selective deletion
            oid = self.canvas.create_line(start_point + end_point,
                             fill=self.pencil_color, width= self.pencil_width,
                             tags="line")

            # Put the dot back on top
            self.canvas.tag_raise(self.colored_circle, oid)       

        # Update the position
        self.offset[0].set(event.x)
        self.offset[1].set(event.y)
        self.move()

    def button_callback(self, event):
        if event.num == 1:
            # Toggle the drawing
            if self.is_drawing:
                self.is_drawing = False
                # set to off color
                self.canvas.itemconfig(self.colored_circle,
                 fill = "red")
            else:
                # pick a random color for the line
                self.pencil_color = self.random_color()
                # set the on color
                self.canvas.itemconfig(self.colored_circle,
                 fill = "green")
                self.is_drawing = True
        elif event.num == 3:
            # We use the tag here for selective delete
            self.canvas.delete("line")
        else:
            print("Button-{}: No action implemented".format(event.num))

    def random_color(self):
        return "#{:02x}{:02x}{:02x}".format(randint(0, 255), randint(0, 255),
         randint(0, 255))

    def get_bbox(self):# self.offset is changing with mouse movement
        return (self.offset[0].get() - self.radius, 
         self.offset[1].get() - self.radius, self.offset[0].get() + self.radius,
         self.offset[1].get() + self.radius)

    def create_ui(self):
        self.canvas = Canvas(self, width=self.width, height=self.height,
         bg="black")
        self.canvas.grid(row=0,column=0, sticky=(W,E,S,N))

        # Draw a circle of radius self.radius
        # centered at (self.offset[0], self.offset[1])
        self.colored_circle = self.canvas.create_oval(self.get_bbox(), fill="red")
                
    def move(self):
        # Use the canvas method to move the dot
        self.canvas.coords(self.colored_circle, self.get_bbox())
        self.update_idletasks()# ask to draw

root = Tk()
root.title("Test Binding 4")

frame = Frame(root)
frame.grid()   

MovingColoredDot(frame).grid()

# Start event loop
root.mainloop()

