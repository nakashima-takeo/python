class Food():
    def __init__(self, name, protein, fat, carbo):
        self.name = name
        self.macro = [protein, fat, carbo]
        self.energy_per_macro = [4, 9, 4]
        self.energy = self.get_energy()

    def get_energy(self):
        energy = 0
        for m, e in zip(self.macro, self.energy_per_macro):
            energy += m * e
        return energy

    def info(self):
        return "name: {} macro: {} {} {} energy: {}".format(self.name,
         self.macro[0], self.macro[1], self.macro[2], self.energy)

if __name__=="__main__":
    #Test
    food = Food("beef steak", 30, 10, 5)
    print("Food {}: {}".format(food.name, food.energy))
    print(food.info())
    


