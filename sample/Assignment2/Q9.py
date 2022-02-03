from tkinter import Tk, Canvas, Frame, Button, BOTH, LEFT, RIGHT, X
from tkinter import TclError
from random import randint

class CanvasUI(Frame):
    def __init__(self, master=None, width = 400, height = 200, bg="#a0a0a0"):

        Frame.__init__(self, master)

        self.width = 600
        self.height = 400
        self.bg = bg

        self.canvas = None

        self.create_ui()

    def create_ui(self):
        self.canvas = Canvas(self, bg = self.bg, width = self.width,
         height = self.height)
        self.canvas.pack()

        buttons_frame = Frame(self)
        buttons_frame.pack(fill=X, expand = True)

        Button(buttons_frame, text = "Add",
         command=lambda : self.feedback("add")).pack(side=LEFT)
        Button(buttons_frame, text = "Shuffle",
         command=lambda : self.feedback("shuffle")).pack(side=LEFT)
        Button(buttons_frame, text = "Reset",
         command=lambda : self.feedback("reset")).pack(side=RIGHT)
        # add a 'color' button
        Button(buttons_frame, text = "color",
         command=lambda : self.feedback("color")).place(relx = 0.3)

    def random_color(self):
        return "#{:02x}{:02x}{:02x}".format(randint(0, 255), randint(0, 255),
         randint(0, 255))

    def random_gray(self):
        v = randint(64, 95)
        return "#{:02x}{:02x}{:02x}".format(v, v, v)

    def random_point(self):
        return randint(0, self.width), randint(0, self.height)

    def random_bounding_box(self, scale):
        width, height = self.random_point()
        width *= scale
        height *= scale
        bbox_top_left = self.random_point()
        bbox_bottom_right = bbox_top_left[0] + width, bbox_top_left[1] + height
        return bbox_top_left+bbox_bottom_right

    def draw(self):
        for i in range(randint(10, 50)):
            if randint(1, 100) > 95:
                c = self.random_color()
                bbox = self.random_bounding_box(0.1)
                # add a tag
                self.canvas.create_oval(bbox, fill=c, outline=c, tag = "all-color")
            else:
                c = self.random_gray()
                bbox = self.random_bounding_box(0.2)
                # add a tag
                self.canvas.create_oval(bbox, fill=c, outline=c, tag = "gray")

    def shuffle(self):
        object_id_list = self.canvas.find_all()
        number_objects = len(object_id_list)
        for i in range(number_objects):
            oid1 = object_id_list[randint(0, number_objects-1)]
            oid2 = object_id_list[randint(0, number_objects-1)]
            self.canvas.tag_raise(oid1, oid2)

    def reset(self):
        self.canvas.delete("all")

    # color function : This  bring color ovals in front of gray ovals
    def color(self):
            self.canvas.tag_raise("all-color")

    def feedback(self, choice):
        if choice == "add":
            self.draw()
        elif choice == "shuffle" :
            self.shuffle()
        elif choice == "reset" :
            self.reset()
        # color function execute
        elif choice == "color" :
            self.color()
        else:
            pass

if __name__ == "__main__":
    root = Tk()
    root.title("Moonscape")
    CanvasUI(root).pack(fill=BOTH)

    root.mainloop()
