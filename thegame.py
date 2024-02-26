import random
from gamefunctions import write_report, Userinput, Gamefunctions

player_wins = 0
computer_wins = 0
# TODO: Creating a file that can then be written to with the ending match report
match_report = open('matchreport.txt', 'w')
print(f"Are you ready to play? Your choices are R, P, S. First to three wins!")
while player_wins < 3 and computer_wins < 3:
    # TODO: Prompts the user to enter a value: R,P,S
    # TODO: validate the user input to make sure it is R,S,P
    # instantiating the class for the user and computer input
    user_start = Userinput()
    # using method to validate the user input
    player1 = user_start.validate_user()
    # TODO: Computer generates a random number from the list of numbers provided
    # using method to get computer choice - object is user_start, method is computer_choice
    computer = user_start.computer_choice()
    # instantiating the game class using the data attributes returned in the user input class
    game = Gamefunctions(player1, computer)
    player_choice = game.player_convert()
    print(f"Player one you have chosen {player_choice}")
    computer_choice = game.computer_convert()
    print(f"Computer you have chosen {computer_choice}")
    # TODO: Compare users choice with computers choice indicating who won
    player_win, computer_win = game.compare_outcomes(player_choice, computer_choice)
    if player_win == 'Winner':
        player_wins += 1
        print('You have beaten computer!!\n')
        print(f'You have won {player_wins} matches!')
        print('#' * 50)

    elif computer_win == 'Winner':
        computer_wins +=1
        print(f"Sorry player one you have lost!\n")
        print(f"Computer has won {computer_wins} matches!")
        print('#' * 50)
    else:
        print("Nobody wins!")
        print("It's a draw - go again?")
        print('#' * 50)

print('The game has ended! Well played')

write_report(match_report, player_wins, computer_wins)

