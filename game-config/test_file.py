from player_moves import player_attribute
from computer_moves import computer_attribute
import rock_paper_scissors_var

i = rock_paper_scissors_var.NUMBER_OF_GAMES
while i <= rock_paper_scissors_var.NUMBER_OF_GAMES:
    if i == 0:
        break
    player_move = player_attribute()
    computer_move = computer_attribute()
    if player_move == computer_move:
        win_or_lose = rock_paper_scissors_var.DRAW
        i -= 0
        print(win_or_lose)
        continue
    elif computer_move == rock_paper_scissors_var.ROCK and player_move == rock_paper_scissors_var.SCISSORS:
        win_or_lose = rock_paper_scissors_var.LOSE
        rock_paper_scissors_var.computer_win_count += 1
        i -= 1
    elif computer_move == rock_paper_scissors_var.PAPER and player_move == rock_paper_scissors_var.ROCK:
        win_or_lose = rock_paper_scissors_var.LOSE
        rock_paper_scissors_var.computer_win_count += 1
        i -= 1
    elif computer_move == rock_paper_scissors_var.SCISSORS and player_move == rock_paper_scissors_var.PAPER:
        win_or_lose = rock_paper_scissors_var.LOSE
        rock_paper_scissors_var.computer_win_count += 1
        i -= 1
    else:
        win_or_lose = rock_paper_scissors_var.WIN
        rock_paper_scissors_var.player_win_count += 1
        i -= 1
    print(win_or_lose)
    if rock_paper_scissors_var.NUMBER_OF_GAMES == 3 and rock_paper_scissors_var.player_win_count == 2:
        winner = "User"
        rock_paper_scissors_var.win_count = rock_paper_scissors_var.player_win_count
        break
    elif rock_paper_scissors_var.NUMBER_OF_GAMES == 3 and rock_paper_scissors_var.computer_win_count == 2:
        winner = "Computer"
        rock_paper_scissors_var.win_count = rock_paper_scissors_var.computer_win_count
        break

print(f'The winner is {winner} with {rock_paper_scissors_var.win_count}')
