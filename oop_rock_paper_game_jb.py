import random
# This imports the random module, so we can use ex.randint

# There is a BASE CLASS, I used Player as a base class
# The base class has a constructor which is __init__
# This initialiser below uses a placeholder which is None
# creating a class in order to define players, in this case they would be the pc and player
class Player:
    # use of the constructor
    def __init__(self, name):
        self.name = name
        self.choice = None

    # Just defining choose, it is a placeholder and can be overridden eventually
    def choose(self):
        pass

class You(Player):
    def choose(self):
        valid_choices = ['rock', 'paper', 'scissors']
        while True:
            choice = input(f"{self.name}, Welcome to Rock, Paper, Scissors! \n"
                           f"Please only choose rock, paper, or scissors: ").lower()
            if choice in valid_choices:
                self.choice = choice
                break
            else:
                print("Incorrect input, Please use the given options!")
# This class uses the base class and also uses choose(which is over-ridden by the input)

class NPC_player(Player):
    def choose(self):
        self.choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"{self.name} chooses {self.choice}.")

class Game:
    def __init__(self):
        self.player1 = You("Human")
        self.player2 = NPC_player("NPC")

    def determine_winner(self):
        choices = (self.player1.choice, self.player2.choice)

        if choices[0] == choices[1]:
            return "It's a tie!"
        elif (choices[0] == 'rock' and choices[1] == 'scissors') or \
             (choices[0] == 'paper' and choices[1] == 'rock') or \
             (choices[0] == 'scissors' and choices[1] == 'paper'):
            return f"{self.player1.name} wins!"
        else:
            return f"{self.player2.name} wins!"

    def play(self):
        self.player1.choose()
        self.player2.choose()

        print(f"{self.player1.name} chose {self.player1.choice}.")
        print(f"{self.player2.name} chose {self.player2.choice}.")

        result = self.determine_winner()
        print(result)

# Example usage of a dunderscore, so we can run it below
if __name__ == "__main__":
    game = Game()
    game.play()
