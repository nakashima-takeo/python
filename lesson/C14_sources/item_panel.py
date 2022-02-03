from tkinter import Tk, Frame, Label, Entry, Button, StringVar, DoubleVar,LEFT, BOTH
from item_manager import ItemManager, Item

class ItemPanel(Frame):
    def __init__(self, master = None, item_manager=None):
        super().__init__(master=master)

        self.item_manager=item_manager

        self.name = StringVar()
        self.protein = DoubleVar()
        self.fat = DoubleVar()
        self.carbo = DoubleVar()


        self.create_ui()
    
    def create_ui(self):
        Label(self, text="New Item:").pack()

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

    def add_preset(self):
        if not self.item_manager:
            return
        
        self.item_manager.add_item(Item(self.name.get(), self.protein.get(),
         self.fat.get(), self.carbo.get()))


if __name__ == '__main__':
     # Test the class
    item_manager = ItemManager()

    root = Tk()
    root.geometry("600x400")
    
    item_panel = ItemPanel(root, item_manager=item_manager)
    item_panel.pack(side="left",fill=BOTH, expand=1)
    
    root.mainloop()
