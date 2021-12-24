from tkinter import Tk, Frame, Label, Button, Entry, StringVar
import math

class DiskSquare():
    def __init__(self, root):
        self.root = root

        self.edge = StringVar()
        self.edge.set(1.0)
        self.radius = StringVar()
        self.radius.set(1.0)
        
        self.square_area = StringVar()
        self.disk_area = StringVar()
        self.area_difference = StringVar()

        self.disk_area.trace('w', lambda *args : print("Writing to disk_area detected"))

        self.createUI()

        self.compute()

    def createUI(self):
        self.root.title("Disk Square")
        self.root.geometry("300x200")

        mainframe = Frame(self.root)
        mainframe.pack()
        
        Label(mainframe, text="Square Edge").pack()
        edge_entry = Entry(mainframe, width=7, textvariable=self.edge)
        edge_entry.pack()   

        Label(mainframe, text="Disk radius").pack()
        radius_entry = Entry(mainframe, width=7, textvariable=self.radius)
        radius_entry.pack()  

        self.square_area_label = Label(mainframe, textvariable=self.square_area)
        self.square_area_label.pack()
        self.disk_area_label = Label(mainframe, textvariable=self.disk_area)
        self.disk_area_label.pack()
        Label(mainframe, textvariable=self.area_difference).pack()

        Button(mainframe, text="Compute", command = self.compute).pack()
        
    def compute(self, *args):
        try:
            square_area = float(self.edge.get())**2
            disk_area = math.pi * float(self.radius.get())**2
            area_difference = square_area - disk_area
        except ValueError:
            pass
        self.square_area.set("Square area: {:.3}".format(square_area))
        self.disk_area.set("Disk area: {:.3}".format(disk_area))
        self.area_difference.set("Square area - Disk area = {:.3}".format(area_difference))        

        if square_area > disk_area:
            self.square_area_label["fg"] = "red"
            self.disk_area_label["fg"] = "black"
        elif square_area < disk_area:
            self.square_area_label["fg"] = "black"
            self.disk_area_label["fg"] = "red"
        else:
            self.square_area_label["fg"] = "black"
            self.disk_area_label["fg"] = "black"
            
def main():
    root = Tk()
    DiskSquare(root)
    root.mainloop()

if __name__ == "__main__":
    main()