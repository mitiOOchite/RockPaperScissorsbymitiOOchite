import random
rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
player_move = input('Choose [r]ock, [p]aper, [s]cissors: ')
if player_move.lower() == 'r':
    player_move = rock
elif player_move.lower() == 'p':
    player_move = paper
elif player_move.lower() == 's':
    player_move = scissors
else:
    raise SystemExit('Invalid Input. Please choose [r], [p] or [s]. Try again...')

computer_random_number = random.randint(1, 3)
computer_move = ''
if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
elif computer_random_number == 3:
    computer_move = scissors
print(f'The computer chose: {computer_move}')
if computer_move == player_move:
    win_or_lose = 'Draw'
elif computer_move == rock and player_move == scissors:
    win_or_lose = 'You Lose!'
elif computer_move == paper and player_move == rock:
    win_or_lose = 'You Lose!'
elif computer_move == scissors and player_move == paper:
    win_or_lose = 'You Lose!'
else:
    win_or_lose = 'You Win!'
print(win_or_lose)