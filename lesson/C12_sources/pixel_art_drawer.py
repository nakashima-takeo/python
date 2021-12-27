import tkinter as tk
import json
#####################################################

class Painter():
    def __init__(
        self,
        canvas_width, canvas_height,
        init_x, init_y, init_color,
        display_info=False
        ):

        self.display_info = display_info

        self.canvas_width = canvas_width 
        self.canvas_height = canvas_height
        self.canvas_data = [
            [init_color for y in range(self.canvas_width)]
             for x in range(self.canvas_height)
             ]  

        self.cursor = init_x, init_y

        self.color_palette = ["black", "white", "red", "green", "blue"]
        self.pencil_color = None
        self.set_pencil_color(self.color_palette[0])

        self.updates_list = None
        self.has_updates = False

        self.init_canvas()

        self.ui = None

        self.file_name = "pixel_art.json"

    def set_UI(self, ui):
        self.ui = ui

    def get_color_palette(self):
        return self.color_palette.copy()

    def set_pencil_color(self, color):
        self.pencil_color = color
        if self.display_info:
            print(f"Change pencil color to {color}")

    def get_pencil_color(self):
        return self.pencil_color

    def get_size(self):
        return self.canvas_width, self.canvas_height

    def get_color(self):
        x, y = self.cursor
        return self.canvas_data[x][y]

    def paint(self):
        x, y = self.cursor
        self.canvas_data[x][y] = self.pencil_color

        if self.has_updates:
            self.updates_list.append((x,y,self.pencil_color))
        else:
            self.has_updates = True
            self.updates_list = [(x,y,self.pencil_color)]
            print("New update list")

        self.ui.refresh()

    def move_cursor(self, choice):
        x, y = self.cursor
        if choice == "up":
            if x > 0:
                x -=1
        elif choice == "down":
           if x < self.canvas_height-1:
               x +=1
        elif choice == "right":
            if y < self.canvas_width-1:
                y +=1
        elif choice == "left":
            if y > 0:
                y -=1
        else:
            print("Unknown move command:", choice)
        
        if self.display_info:
            print(f"Change pencil position to {x}, {y}")
        
        self.cursor = x, y

        self.ui.update_cursor()

    def get_cursor(self):
        return self.cursor

    def init_canvas(self):
        self.updates_list = []
        for x in range(self.canvas_height):
            for y in range(self.canvas_width):
              self.updates_list.append((x,y,self.canvas_data[x][y]))
        self.has_updates = True
        
    def get_update(self):
        self.has_updates = False
        return self.updates_list.copy()

    def save(self):
        data_dict = {}
        data_dict["size"] = self.get_size()
        data_dict["pixels"] = []
        for x in range(self.canvas_height):
            for y in range(self.canvas_width):
                data_dict["pixels"].append((x,y,self.canvas_data[x][y]))
        with open(self.file_name, 'w') as fd:
            fd.write(json.dumps(data_dict))

    def load(self):
        with open(self.file_name, 'r') as fd:
            json_data = json.loads(fd.read())
        print(json_data)

    
#####################################################

class ColorPanel(tk.Frame):
    def __init__(self, parent=None, painter=None):
        tk.Frame.__init__(self, parent)
        self.painter = painter

        self.pencil_color = tk.StringVar()
        self.pencil_color.set(self.painter.get_pencil_color())
        self.create_ui()

    def create_ui(self):
        row_index = 0
        tk.Label(
            self, text = "Color Panel", fg="#ffffff", bg="#909090"
            ).grid(
                row=row_index, column=0,
                rowspan = 1, columnspan=1,
                sticky=(tk.W, tk.E)
                )
        
        row_index += 1
        tk.Label(
            self
            ).grid(
                row=row_index, column=0,
                rowspan = 1, columnspan=1
                )

        for color in self.painter.get_color_palette():
            row_index += 1
            tk.Radiobutton(
                self, text = color, justify = tk.LEFT,
                var = self.pencil_color, value = color,
                command = self.selected
            ).grid(
                row=row_index, column=0,
                rowspan = 1, columnspan=1,
                sticky=tk.W
                )        
               
        for i in range(row_index):
            self.rowconfigure(i, weight=1)
        self.columnconfigure(0, weight=1)

    def selected(self):
        self.painter.set_pencil_color(self.pencil_color.get())

#####################################################

class PadPanel(tk.Frame):
    def __init__(self, parent=None, painter=None):
        tk.Frame.__init__(self, parent, relief=tk.RIDGE, borderwidth=3)
        self.painter = painter

        self.create_ui()

    def create_ui(self):
        tk.Button(
            self, text = "up", width=5, height=2,
            relief=tk.SOLID, borderwidth=1,
            command=lambda : self.move("up")
            ).grid(
                row=0, column=1,
                rowspan = 1, columnspan=1,
                sticky=(tk.N, tk.S, tk.W, tk.E)
                )
        tk.Button(
            self, text = "left", width=5, height=2,
            relief=tk.SOLID, borderwidth=1,
            command=lambda : self.move("left")
            ).grid(
                row=1, column=0,
                rowspan = 1, columnspan=1,
                sticky=(tk.N, tk.S, tk.W, tk.E)
                )
        tk.Button(
            self, text = "rigth", width=5, height=2,
            relief=tk.SOLID, borderwidth=1,
            command=lambda : self.move("right")
            ).grid(
                row=1, column=2,
                rowspan = 1, columnspan=1,
                sticky=(tk.N, tk.S, tk.W, tk.E)
                )
        tk.Button(
            self, text = "down", width=5, height=2,
            relief=tk.SOLID, borderwidth=1,
            command=lambda : self.move("down")
            ).grid(
                row=2, column=1,
                rowspan = 1, columnspan=1,
                sticky=(tk.N, tk.S, tk.W, tk.E)
                )
        tk.Button(
            self, text = "paint", width=5, height=2,
            relief=tk.FLAT, borderwidth=1, bg="#909090",
            command=self.paint
            ).grid(
                row=1, column=1,
                rowspan = 1, columnspan=1,
                sticky=(tk.N, tk.S, tk.W, tk.E)
                )

    def move(self, direction):
        self.painter.move_cursor(direction)
               
    def paint(self):
        self.painter.paint()

    #####################################################

class ControlPanel(tk.Frame):
    def __init__(self, parent=None, painter=None):
        tk.Frame.__init__(self, parent)
        self.painter = painter
        self.create_ui()

    def create_ui(self):
        tk.Label(
            self, text = "Control Panel",
            fg="#ffffff", bg="#909090"
            ).grid(
                row=0, column=0,
                rowspan = 1, columnspan=2,
                sticky=(tk.W, tk.E)
                )
        
        tk.Label(
            self
            ).grid(
                row=1, column=0,
                rowspan = 1, columnspan=2
                )
        
        PadPanel(
            self, self.painter
            ).grid(
                row=2, column=0,
                rowspan = 1, columnspan=2
                )
    
        tk.Label(
            self
            ).grid(
                row=3, column=0,
                rowspan = 1, columnspan=2
                )

        tk.Button(
            self, text = "save", command = self.painter.save
            ).grid(
                row=4, column=0,
                rowspan = 1, columnspan=1
                )
        tk.Button(
            self, text = "load", command = self.painter.load
            ).grid(
                row=4, column=1,
                rowspan = 1, columnspan=1
                )    
#####################################################

class CanvasPanel(tk.Frame):
    def __init__(
        self, parent=None,
        painter=None
        ):
        
        tk.Frame.__init__(self, parent, bg="black")

        self.painter = parent.painter
        self.painter.set_UI(self)   

        self.pixels = None


        self.show_cursor = tk.BooleanVar(None, True)

        self.create_ui()


        self.cursor = self.painter.get_cursor()
        self.is_overlaid = False
        self.cursor_color = None
        self.cursor_blinking()

        self.refresh()

    def create_ui(self):
        
        canvas_width, canvas_height = self.painter.get_size()
        
        self.pixels = [
            [
            tk.Frame(
                    self, width=32, height=24
                    )    
            for y in range(canvas_width)
            ]
            for x in range(canvas_height)
            ]
        
        for i in range(canvas_height):
            self.rowconfigure(i, weight=1)
            for j in range(canvas_width):
                self.columnconfigure(j, weight=1)                
                self.pixels[i][j].grid(
                    row=i, column=j,
                    rowspan=1, columnspan=1,
                    padx=1, pady=1,
                    sticky=(tk.N, tk.S, tk.W, tk.E))
                
        tk.Checkbutton(
            self, text = "show cursor",
            variable= self.show_cursor
            ).grid(
                row=canvas_height, column=0,
                rowspan=1, columnspan = canvas_width,
                sticky=(tk.W, tk.E)
                )

    def cursor_blinking(self):
        if self.show_cursor.get():
            if self.is_overlaid:
                self.is_overlaid = False
                x, y = self.cursor
                self.pixels[x][y]["bg"] = self.cursor_color
                self.after(400, self.cursor_blinking)
            else:
                self.is_overlaid = True
                x, y = self.cursor
                self.cursor_color = self.pixels[x][y]["bg"]
                self.pixels[x][y]["bg"] = "#ff00ff" 
                self.after(100, self.cursor_blinking)
        else:
            if self.is_overlaid:
                self.is_overlaid = False
                x, y = self.cursor
                self.pixels[x][y]["bg"] = self.cursor_color   
            self.after(500, self.cursor_blinking)

    def refresh(self):
        if self.is_overlaid:
            self.is_overlaid = False
            x, y = self.cursor
            self.pixels[x][y]["bg"] = self.cursor_color

        for i, j, color in self.painter.get_update():
            self.pixels[i][j]["bg"] = color
                
    def update_cursor(self):
        if self.is_overlaid:
            self.is_overlaid = False
            x, y = self.cursor
            self.pixels[x][y]["bg"] = self.cursor_color
        self.cursor = self.painter.get_cursor()

#####################################################

class PaintUI(tk.Frame):
    def __init__(self, parent=None, painter=None):
        tk.Frame.__init__(self, parent)
        parent.title("Pixel Art Drawer")
        self.painter = painter
        self.create_ui()

    def create_ui(self):

        color_panel = ColorPanel(self, self.painter)
        canvas_panel = CanvasPanel(self, self.painter)
        control_panel = ControlPanel(self, self.painter)

        color_panel.grid(
            row=0, column=0,
            rowspan=1, columnspan=1,
            sticky=(tk.N, tk.W)
            )

        canvas_panel.grid(
            row=0, column=1,
            rowspan=1, columnspan=1,
            sticky=(tk.N, tk.S, tk.W, tk.E)
            )

        control_panel.grid(
            row=0, column=2,
            rowspan=1, columnspan=1,
            sticky=(tk.N, tk.E)
            )

        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

#####################################################

def main():

    root = tk.Tk()

    painter = Painter(9, 9, 0, 0, "#ffffff")

    PaintUI(root, painter).grid(
        row=0, column=0,
        rowspan=1, columnspan=1,
        sticky=(tk.N, tk.S, tk.W, tk.E)
        )

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    root.mainloop()

if __name__ == '__main__':
    main()

