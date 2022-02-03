from tkinter import Tk, Frame, LEFT, BOTH
from tkinter.font import nametofont

from display_panel import DisplayPanel
from food_manager import FoodManager
from preset_panel import PresetPanel


food_manager = FoodManager()

root = Tk()

default_font = nametofont("TkDefaultFont")
text_font = nametofont("TkTextFont")
default_font["size"] = 16
text_font["size"] = 16

#root.geometry("800x400")
display_panel = DisplayPanel(root)
display_panel.pack(side=LEFT)
preset_panel = PresetPanel(root, food_manager=food_manager, display_panel=display_panel)
preset_panel.pack(side=LEFT, fill=BOTH, expand=1)

root.mainloop()
