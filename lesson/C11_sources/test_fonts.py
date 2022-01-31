from tkinter import Tk, Label, Button
from random import randint
from tkinter.font import Font, families

root = Tk()

# Create a fond
font = Font(family = "Times New Roman", size = 36, weight = "bold")
# Show the attributes
print("Font attributes:", font.config())

# Get a list of installed fonts
fonts_tuple = families()

# Display these names
print("Installed fonts:")
for i_font in fonts_tuple:
    print(i_font)

# Function that:
#  picks a font randomly
#  changes the label font & text
def change_font():
    i = randint(0, len(fonts_tuple))
    font["family"] = fonts_tuple[i]
    label["text"] = font["family"]
    

# Label 
# use font family as text
label = Label(root, text = font["family"], font = font)
label.pack()

# Button to update font
Button(root, text = "Change font", command = change_font).pack()

root.mainloop()


