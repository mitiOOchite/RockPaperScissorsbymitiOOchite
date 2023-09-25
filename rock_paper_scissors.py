from player_moves import player_attribute
from computer_moves import computer_attribute
player_move = player_attribute()
computer_move = computer_attribute()
ROCK = 'Rock'
SCISSORS = 'Scissors'
PAPER = 'Paper'

if player_move == computer_move:
    win_or_lose = 'Draw!'
elif computer_move == ROCK and player_move == SCISSORS:
    win_or_lose = 'You Lose!'
elif computer_move == PAPER and player_move == ROCK:
    win_or_lose = 'You Lose!'
elif computer_move == SCISSORS and player_move == PAPER:
    win_or_lose = 'You Lose!'
else:
    win_or_lose = 'You Win!'
print(win_or_lose)

