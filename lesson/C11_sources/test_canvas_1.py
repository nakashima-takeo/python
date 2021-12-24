from tkinter import Tk, Canvas, Frame, Button, BOTH, LEFT
from random import randint


class CanvasUI(Frame):
    def __init__(self, master=None, width = 400, height = 200, bg="white"):
        
        Frame.__init__(self, master)
        
        self.width = width
        self.height = height
        self.bg = bg

        self.canvas = None
        
        self.create_ui()

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

        Button(draw_frame, text = "set backgound color", 
        command=lambda : self.draw("bg")).pack(side=LEFT)

        Button(draw_frame, text = "draw line", 
        command=lambda : self.draw("line")).pack(side=LEFT)

        Button(draw_frame, text = "drawlines",
         command=lambda : self.draw("lines")).pack(side=LEFT)

        Button(draw_frame, text = "draw curve",
         command=lambda : self.draw("curve")).pack(side=LEFT)

        Button(delete_frame, text = "delete lines",
         command=lambda : self.draw("delete lines")).pack(side=LEFT)

        Button(delete_frame, text = "delete blue",
         command=lambda : self.draw("delete blue")).pack(side=LEFT)

        Button(delete_frame, text = "delete smooth",
         command=lambda : self.draw("delete smooth")).pack(side=LEFT)

        Button(delete_frame, text = "reset",
         command=lambda : self.draw("reset")).pack(side=LEFT)

    def random_color(self):
        return "#{:02x}{:02x}{:02x}".format(randint(0, 255), randint(0, 255),
         randint(0, 255))

    def random_point(self):
        return randint(0, self.width), randint(0, self.height)

    def draw(self, choice):
        if choice == "bg":
            self.canvas["bg"] = self.random_color()
        elif choice == "line":
            start = self.random_point()
            end = self.random_point()
            self.canvas.create_line(start + end, fill="blue", width=2,
             tags=("line", "blue"))

        elif choice == "lines":
            points = self.random_point()
            for i in range(10):
                points += self.random_point()
            self.canvas.create_line(points, fill="green", width=2, smooth=0,
             tags=("lines", "green"))

        elif choice == "curve":
            points = self.random_point()
            for i in range(10):
                points += self.random_point()
            self.canvas.create_line(points, fill="cyan", width=2, smooth=1,
             tags=("curve", "cyan", "smooth")) 

        elif choice == "delete lines":
            self.canvas.delete("lines")        

        elif choice == "delete blue":
            self.canvas.delete("blue")    

        elif choice == "delete smooth":
            self.canvas.delete("smooth")    

        elif choice == "reset":
            self.canvas.delete("all")        
            self.canvas["bg"] = self.bg

        else:
            print("Not implemented!")

        # Show the information about the objects
        object_id_list = self.canvas.find_all()
        print("There are {} objects".format(len(object_id_list)))
        for oid in object_id_list:
            print("object id {}\ttype: {}\ttags: {}".format(oid,
             self.canvas.type(oid), self.canvas.gettags(oid)))

    

root = Tk()
root.title("Test Canvas 1")
CanvasUI(root).pack(fill=BOTH)

root.mainloop()
