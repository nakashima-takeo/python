from random import randint
class Dice():
    """define a dice"""
    def __init__(self, faces):
        """initialize a dice with a given number of faces"""
        self.faces = faces
        self.value = 0
    def roll(self):
        """roll the dice"""
        self.value = randint(1, self.faces)
        print(f"Dice rolled: {self.value}")
class Player():
    """define a player"""
    def __init__(self,game):
        """initialize a player"""
        self.score = 0
        self.game = game
        self.prediction = 0
    def prediction_of_the_dice(self, dice):
        """return the prediction of the dice"""
        while True:
            try:
                prediction = int(input(f"Please enter a value between 1 and {dice.faces}:"))
                # if value is not in the interval [1, faces], ask again
                if prediction < 1 or prediction > dice.faces:
                    continue
                else:
                    self.prediction = prediction
                    break
            except ValueError:
                continue
    def add_score(self, score):
        """add a score to the player's score"""
        self.score += score

class Game():
    def __init__(self):
        """initialize a game"""
        self.trials = 0
        self.dice = Dice(int(input("Please enter the number of faces of the dice: ")))
        self.player = Player(Game)
        self.play()
    def play(self):
        try:
            while True:
                # prediction
                self.player.prediction_of_the_dice(self.dice)
                # roll
                self.dice.roll()
                self.trials += 1
                # compare
                if self.dice.value == self.player.prediction:
                    self.player.add_score(1)
                    print(f"Good guess!{self.player.score}/{self.trials}")
        # if the player press Ctrl-C, the game will stop
        except KeyboardInterrupt:
            print("\nthanks!")

def main():
    Game0 = Game()

if __name__ == "__main__":
    main()
