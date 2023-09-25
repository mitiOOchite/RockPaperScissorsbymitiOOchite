from player_moves import player_attribute
from computer_moves import computer_attribute
player_move = player_attribute()
computer_move = computer_attribute()
if player_move == computer_move:
    print('Draw')
else:
    print('Lose')
# elif computer_rock == computer_rock and player_move == scissors:
#     win_or_lose = 'You Lose!'
# elif computer_move == computer_paper and player_move == rock:
#     win_or_lose = 'You Lose!'
# elif computer_move == computer_scissors and player_move == paper:
#     win_or_lose = 'You Lose!'
# else:
#     win_or_lose = 'You Win!'
# print(win_or_lose)

