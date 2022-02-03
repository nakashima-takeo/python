from tkinter import Tk, Frame, Label, Entry, Button, StringVar, IntVar,LEFT, BOTH
from food_manager import FoodManager
from food import Food
from tkinter.font import nametofont

class FoodPanel(Frame):
    def __init__(self, master = None, food_manager=None):
        super().__init__(master=master)

        self.food_manager=food_manager

        self.name = StringVar()
        self.protein = IntVar()
        self.fat = IntVar()
        self.carbo = IntVar()


        self.create_ui()
    
    def create_ui(self):
        Label(self, text="New Food:").pack()

        name_frame = Frame(self)        
        name_frame.pack()
        Label(name_frame, text="Name:", width=10).pack(side=LEFT)
        Entry(name_frame, textvariable=self.name, width=10).pack(side=LEFT)


        protein_frame = Frame(self)        
        protein_frame.pack()
        Label(protein_frame, text="Prot:", width=10).pack(side=LEFT)
        Entry(protein_frame, textvariable=self.protein, width=10).pack(side=LEFT)

        fat_frame = Frame(self)        
        fat_frame.pack()
        Label(fat_frame, text="Fat:", width=10).pack(side=LEFT)
        Entry(fat_frame, textvariable=self.fat, width=10).pack(side=LEFT)

        carbo_frame = Frame(self)        
        carbo_frame.pack()
        Label(carbo_frame, text="Carb:", width=10).pack(side=LEFT)
        Entry(carbo_frame, textvariable=self.carbo, width=10).pack(side=LEFT)

        Button(self, text="Add", command = self.add_preset).pack()
        Button(self, text="Save", command = self.save_presets).pack()

    def add_preset(self):
        food = Food(self.name.get(), self.protein.get(), self.fat.get(),
         self.carbo.get())
        self.food_manager.add_food(food)
    
    def save_presets(self):
        self.food_manager.save()


if __name__ == '__main__':
     # Test the class
    food_manager = FoodManager()

    root = Tk()

    default_font = nametofont("TkDefaultFont")
    text_font = nametofont("TkTextFont")
    default_font["size"] = 16
    text_font["size"] = 16

    food_panel = FoodPanel(root, food_manager=food_manager)
    food_panel.pack(side="left",fill=BOTH, expand=1)
    
    root.mainloop()
