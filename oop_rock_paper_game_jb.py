import random



# QUESTIONS 4 Victoria

# differences between the big 4
# poly, inheritance,encapsulation and instantiation



# This imports the random module, so we can use ex.randint

# There is a BASE CLASS, I used Player as a base class
# The base class has a constructor which is __init__
# This initialiser below uses a placeholder which is None
# creating a class in order to define players, in this case they would be the pc and player
class Player:
    # defibes a class called Player
    # use of the constructor below
    def __init__(self, name):
        self.name = name
        self.choice = None

    # Just defining choose, it is a placeholder and can be overridden eventually
    def choose(self):
        pass
#      choose is a method, it is a placeholder to be used later on in the code

class You(Player):
    # this defines a class
    # the below overrides the choose previously in old class
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
#  the above is an edited version from my functions section turned into a class
class NPC_player(Player):
    # Inherits from the Base class - named Player
    # it takes choose and choice
    def choose(self):
        self.choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"{self.name} chooses {self.choice}.")
#         prints out the choices which have been inherited from the base class
class Game:
    # Game is an object and is initialised by the construtor below
    def __init__(self):
        self.player1 = You("Human")
        self.player2 = NPC_player("NPC")
    # it inherits from the 2 other classes
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
    #  this method compares both choiices of the PC and human
    # makes sure there is an output for a tie etc.. again pulled from functions

    def play(self):
        self.player1.choose()
        self.player2.choose()

        print(f"{self.player1.name} chose {self.player1.choice}.")
        print(f"{self.player2.name} chose {self.player2.choice}.")

        result = self.determine_winner()
        print(result)
# This is a method(it is an action) it puts it all together and runs
# the choose prints the choices, and uses determine winner to get the final
# output
# Example usage of a dunderscore, so we can run it below
if __name__ == "__main__":
    game = Game()
#     Turning a variable into a method = incapsulation
# Creates an instance of a class
#     this is instatiation
    # an instance of a class is also known as an object
    # instance is an object that belongs to that class
    # instantiation
    # this is when we create objects based on classes
    game.play()
#     calls game method on the play class!

# This a dunderscore, which allows the code to be used in this file
# We do not need to import it as a module, instead can use it here.
# __name__ is a variable because of the == which means the current modules
#name
# __main__ - means main program is being run
# using the statement, the condition ensures that the code is the main
# program, so everything is executed.