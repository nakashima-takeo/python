from tkinter import Tk, Frame, Label, Button, Listbox, SINGLE, BOTH, END

from food_manager import FoodManager
from display_panel import DisplayPanel

class PresetPanel(Frame):
    def __init__(self, master = None, food_manager=None, display_panel=None):
        super().__init__(master=master)
        self.food_manager = food_manager
        self.display_panel = display_panel
        self.lbox = None

        self.create_ui()
        self.update_item()
    
    def create_ui(self):
        Label(self, text="Presets:").pack()
        self.lbox = Listbox(self, selectmode = SINGLE)
        self.lbox.pack(fill=BOTH, expand=1)
        self.button = Button(self, text = "Show", command = self.show)
        self.button.pack()

    def update_item(self):
        if not self.food_manager:
            return

        self.lbox.delete(0, END)

        for i, name in enumerate(self.food_manager.foods.keys()):
            self.lbox.insert(i, name)
    
    def show(self):
        if not self.display_panel or not self.food_manager:
            return

        if not self.lbox.curselection():
            return

        food_name = self.lbox.get(0, END)[self.lbox.curselection()[0]]
        macro_energy = self.food_manager.get_macro_energy(food_name)
        if macro_energy:
            self.display_panel.display(*macro_energy)

if __name__=="__main__":

     # Test the class

    food_manager = FoodManager()

    root = Tk()
    #root.geometry("800x400")
    
    preset_panel = PresetPanel(root, food_manager=food_manager)
    preset_panel.pack(side="left",fill=BOTH, expand=1)
    
    preset_panel.update_item()
    
    root.mainloop()