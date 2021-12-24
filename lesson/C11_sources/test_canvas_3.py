from tkinter import Tk, Canvas, Frame, Button, BOTH, LEFT
from tkinter import TclError
from random import randint


class CanvasUI(Frame):
    def __init__(self, master=None, width = 400, height = 200, bg="white"):
        
        Frame.__init__(self, master)
        
        self.width = width
        self.height = height
        self.bg = bg

        self.canvas = None
        
        self.create_ui()

    def random_point(self):
        return randint(0, self.width), randint(0, self.height)

    def random_bounding_box(self):
        width, height = self.random_point()
        if width > 200 or height > 100:
            size = "big"
        else:
            size = "small"

        bbox_top_left = self.random_point()
        bbox_bottom_right = bbox_top_left[0] + width, bbox_top_left[1] + height 
        return bbox_top_left+bbox_bottom_right, size

    def create_ui(self):
        self.canvas = Canvas(self, bg = self.bg, width = self.width,
         height = self.height)
        self.canvas.pack()

        buttons_frame = Frame(self)
        buttons_frame.pack()

        draw_frame = Frame(buttons_frame)
        draw_frame.pack()
        delete_frame = Frame(buttons_frame)
        delete_frame.pack()

        Button(draw_frame, text = "draw oval",
         command=lambda : self.draw("oval")).pack(side=LEFT)

        Button(draw_frame, text = "draw rectangle",
         command=lambda : self.draw("rectangle")).pack(side=LEFT)
       
        Button(delete_frame, text = "small in front",
         command=lambda : self.draw("small front")).pack(side=LEFT)

        Button(delete_frame, text = "big in front",
         command=lambda : self.draw("big front")).pack(side=LEFT)

        Button(delete_frame, text = "reset",
         command=lambda : self.draw("reset")).pack(side=LEFT)

    def draw(self, choice):
        if choice == "oval":
            bbox, size = self.random_bounding_box()
            self.canvas.create_oval(bbox, fill="yellow", outline="black",
             width=3, tags=("oval", size))
        
        elif choice == "rectangle":
            bbox, size = self.random_bounding_box()
            self.canvas.create_rectangle(bbox, fill="#f000f0", outline="black",
             width=3, tags=("rectangle", size))        

        elif choice == "small front":
            try:
                self.canvas.tag_raise("small", "big")
            except TclError as e:
                print(e)

        elif choice == "big front":
            try:
                self.canvas.tag_raise("big", "small")                
            except TclError as e:
                print(e)

        elif choice == "reset":
            self.canvas.delete("all")        
        
        else:
            print("Not implemented!")

        # Show the information about the objects
        object_id_list = self.canvas.find_all()
        print("There are {} objects".format(len(object_id_list)))
        for oid in object_id_list:
            print("object id {}\ttype: {}\ttags: {}".format(oid,
             self.canvas.type(oid), self.canvas.gettags(oid)))
            

    

root = Tk()
root.title("Test Canvas 2")
CanvasUI(root).pack(fill=BOTH)

root.mainloop()
