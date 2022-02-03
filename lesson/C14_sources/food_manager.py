import os
import json

from food import Food

class FoodManager():
    def __init__(self, file_name="food_data_base.json"):
        
        self.foods = {}

        self.file_name = file_name

        self.load()

    def load(self):
        try:
            with open(self.file_name, "r") as fd:
                self.foods = json.loads(fd.read())
        except FileNotFoundError:
            pass
        

    def save(self):
        with open(self.file_name, 'w') as fd:
            fd.write(json.dumps(self.foods))
        print("Data saved to file:", self.file_name)
        self.display()

    def add_food(self, food):
        self.foods[food.name] = [food.macro, food.energy]
        print("added preset:", food.info())

    def display(self):
        print("Number foods: {}",format(len(self.foods)))
        for k,v in self.foods.items():
            print(k, v)

    def get_macro_energy(self, name):
        if name in self.foods:
            return self.foods[name]
        else:
            return None


if __name__=="__main__":
    #Test

    food = Food("beef steak", 30, 10, 5)
    print("food {}: {}".format(food.name, food.energy))

    food_manager = FoodManager()
    food_manager.add_food(food)

    food_manager.display()

    food_manager.add_food(Food("pasta", 5, 0, 50))
    food_manager.display()

    food_manager.save()

    food_manager = FoodManager()
    food_manager.display()



    