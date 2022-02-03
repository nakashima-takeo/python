from tkinter import Tk, Frame, Canvas, Label, LEFT, BOTH
from tkinter.font import nametofont

class DisplayPanel(Frame):
    def __init__(self, master = None, recommended_energy = 2000):
        super().__init__(master=master)
        self.energy = 0
        self.macro = None
        self.recommended_energy = recommended_energy
        self.canvas = None

        self.energy_color = "#00ffff"
        self.macro_color = ["#00ff00", "#ffff00", "#ff00ff"]

        self.size = 600, 400
        self.margin = 5

        self.macro_bb = (self.margin, self.margin,
         self.size[0]*2.0/3.0-self.margin, self.size[1]-self.margin)

        self.energy_bb = (self.size[0]*2.0/3.0+self.margin,
         0+self.margin,self.size[0]-self.margin,self.size[1]-self.margin)

        self.create_ui()

    def create_ui(self):
        self.canvas = Canvas(self, width=self.size[0], height=self.size[1], bg ="#ffffff")
        self.canvas.pack()

        caption = Frame(self)
        caption.pack(fill=BOTH, expand=1)

        Label(caption, text="Prot", bg=self.macro_color[0]).pack(side=LEFT,
         fill=BOTH, expand=1)
        Label(caption, text="Fat", bg=self.macro_color[1]).pack(side=LEFT,
         fill=BOTH, expand=1)
        Label(caption, text="Carb", bg=self.macro_color[2]).pack(side=LEFT,
         fill=BOTH, expand=1)
        Label(caption, text="Energy", bg=self.energy_color).pack(side=LEFT,
         fill=BOTH, expand=1)


        self.canvas.create_rectangle(self.energy_bb, fill="#f0f0f0",
         outline="#000000", width=3, tags="placeholder")   

        self.canvas.create_oval(self.macro_bb, fill="#f0f0f0",
         outline="#000000", width=3, tags="placeholder")

    def display(self, macro, energy):
        self.energy = energy
        self.macro = macro

        self.canvas.delete("energy", "macro")

        energy_ratio = self.energy / self.recommended_energy

        bb = (self.size[0]*2.0/3.0 + self.margin,
         (1.0 - energy_ratio) * self.size[1] + self.margin, 
         self.size[0]-self.margin,
         self.size[1] - self.margin)
        self.canvas.create_rectangle(bb, fill=self.energy_color,
         outline="#000000", width=3, tags="energy")   

        macro_sum = sum(self.macro)
        macro_ratio = [x/macro_sum for x in self.macro]

        start = 0
        end = 0
        for i, r in enumerate(macro_ratio):
            end = r * 360 
            self.canvas.create_arc(self.macro_bb, start = start,
         extent = end, fill=self.macro_color[i], outline="#000000",
          width=3, tags="macro")
            start += end


if __name__ == '__main__':
    # Test the class
    
    root = Tk()

    default_font = nametofont("TkDefaultFont")
    text_font = nametofont("TkTextFont")
    default_font["size"] = 16
    text_font["size"] = 16

    display_panel = DisplayPanel(root, 2000)
    display_panel.pack()
    
    display_panel.display([50, 100, 80], 50*4+100*9+80*4)
    
    root.mainloop()
