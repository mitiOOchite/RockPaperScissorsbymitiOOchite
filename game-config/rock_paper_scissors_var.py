ROCK = 'Rock'
SCISSORS = 'Scissors'
PAPER = 'Paper'
DRAW = 'This round was a draw, it won\'t be counted!'
WIN = 'You win this round!'
LOSE = 'You lose this round!'
USER = input('Please choose a username: ')
COMPUTER = 'Computer'
NUMBER_OF_GAMES = int(input('You are able to choose to play [3], [5], [7] or [9] games: '))
computer_win_count = 0 # win count stores the number of games won by the computer
player_win_count = 0 # stored the number of games won by the player
win_count = 0
#game variations for a win count as follows:
#best of 3 = 2 wins out of 3 games are considered a win(2 of 3)
#best of 5 = 3 wins out of 5 games are considered a win(3 of 5)
#best of 7 = 4 wins out of 7 games ar econsidered a win(4 of 7)
#best of 9 = 5 wins out of 7 games are considered a win(5 of 9)