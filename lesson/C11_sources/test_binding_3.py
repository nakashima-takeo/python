from tkinter import Tk, Frame, Canvas, Scale, DoubleVar
from tkinter import HORIZONTAL, W, E, S, N
from random import randint

class MovingColoredDot(Frame):
    def __init__(self, master=None, width=200, height=200):
        Frame.__init__(self, master)
        self.width = width
        self.height = height

        self.step = 5

        self.offset = (DoubleVar(None, self.width/2),
         DoubleVar(None, self.height/2))

        self.canvas = None
        self.colored_circle = None

        self.create_ui()

        ####################################
        # Bindings
        self.canvas.bind("<Enter>", self.enter_callback)
        self.canvas.bind("<Leave>", self.leave_callback)
        self.canvas.bind("<KeyPress>", self.keypress_callback)
        ####################################

    def random_color(self):
        return "#{:02x}{:02x}{:02x}".format(randint(0, 255), randint(0, 255),
         randint(0, 255))

    ####################################
    # Callbacks
    def enter_callback(self, event):
        # Gives the focus to canvas
        event.widget.focus_set()

    def leave_callback(self, event):
        # Gives the focus to the instance of MovingColoredDot
        # that contains the canvas
        self.focus_set()

    def keypress_callback(self, event):
        # Flag to check for movement
        trigger_move = True

        # Check the key pressed
        if event.keysym == "Up":
            value = self.offset[1].get() - self.step
            if value < 0:
                value = 0
            self.offset[1].set(value)

        elif event.keysym == "Down":
            value = self.offset[1].get() + self.step
            if value > self.height - 1:
                value = self.height - 1
            self.offset[1].set(value)

        elif event.keysym == "Left":
            value = self.offset[0].get() - self.step
            if value < 0:
                value = 0
            self.offset[0].set(value)

        elif event.keysym == "Right":
            value = self.offset[0].get() + self.step
            if value > self.width - 1:
                value = self.width - 1
            self.offset[0].set(value)

        else:
            # It was not a movement key
            # set the flag to False
            trigger_move = False

            # Check for non movement keys

            if event.keysym == "space":
                self.canvas.itemconfig(self.colored_circle,
                 fill = self.random_color())
                self.canvas["bg"] = self.random_color()
            elif event.keysym == "q":
                print("Stopping the application")
                self.quit()
            else:
                print("key '{}': not used".format(event.keysym))

        if trigger_move:
            self.move(0)
            # We reuse the method made for the Scale command attribute
            # This method expects to get a value from the Scale
            # Here, we put a dummy value (0) to use it.
    ####################################

    def get_bbox(self):# self.offset is changing with keys or scales
        return (self.offset[0].get()-10, self.offset[1].get()-10,
         self.offset[0].get()+10, self.offset[1].get()+10)

    def create_ui(self):
        self.canvas = Canvas(self, width=self.width, height=self.height,
         bg="black")
        self.canvas.grid(row=0,column=0, sticky=(W,E,S,N))

        # Draw a circle of radius 10
        # centered at (self.offset[0], self.offset[1])
        self.colored_circle = self.canvas.create_oval(self.get_bbox(),
         fill="red")

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
        self.canvas.coords(self.colored_circle, self.get_bbox())
        self.update_idletasks()# Ask to process drawing events

root = Tk()
root.title("Test Binding 3")

frame = Frame(root)
frame.grid()

MovingColoredDot(frame).grid()

# Start event loop
root.mainloop()

