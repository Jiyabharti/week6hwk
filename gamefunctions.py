import random


def write_report(match_report, player_wins, computer_wins):
    match_report.write('Match Report \n' + ('*' * 50) + '\n')
    match_report.write('Good game! Well played!\n')
    match_report.write('Total Wins')
    match_report.write(f'\nPlayer 1: {player_wins} \nComputer: {computer_wins}')
    match_report.close()
    with open('matchreport.txt', 'r') as file:
        for line in file:
            print(line[:-1])


# function to validate that the user has entered the correct in
class Userinput:
    def __init__(self):
        self.player1 = ''
        self.computer = ''

    def validate_user(self):
        player1_outcomes = ['R', 'P', 'S']
        while True:
            self.player1 = input('1, 2, 3 GO - Type R or P or S: ').upper()
            if self.player1 not in player1_outcomes:
                print('Please enter a valid value - R, P, S')
            else:
                return self.player1

    def computer_choice(self):
        computer_outcomes = [0, 1, 2]
        self.computer = str(random.choice(computer_outcomes))
        return self.computer


class Gamefunctions:
    # creating the attributes to be passed when the class is initialised
    def __init__(self, player1, computer):
        self._player_input = player1
        self._computer_input = computer

    def player_convert(self):
        if self._player_input == 'R':
            self._player_input = 'Rock'

        elif self._player_input == 'P':
            self._player_input = 'Paper'

        else:
            self._player_input = 'Scissors'
        return self._player_input

    def computer_convert(self):
        if self._computer_input == '0':
            self._computer_input = 'Rock'

        elif self._computer_input == '1':
            self._computer_input = 'Paper'

        else:
            self._computer_input = 'Scissors'
        return self._computer_input

    def compare_outcomes(self, _player_input, _computer_input):
        winning_combinations = {
            'Rock': 'Scissors',
            'Paper': 'Rock',
            'Scissors': 'Paper'
            }

        if self._player_input == self._computer_input:
            player_win = 'Next time'
            computer_win = 'Next time'
            return player_win, computer_win
        elif winning_combinations[self._player_input] == self._computer_input:
            player_win = 'Winner'
            computer_win = 'Loser'
            return player_win, computer_win

        else:
            player_win = 'Loser'
            computer_win = 'Winner'
            return player_win, computer_win


if __name__ == "__main__":
    game = Gamefunctions('S', '0')
    result = game.player_convert()
    print(result)
    another_result = game.computer_convert()
    print(another_result)
    comparison = game.compare_outcomes(result, another_result)
    print(comparison)
