from player_moves import player_attribute
from computer_moves import computer_attribute
import rock_paper_scissors_var
player_move = player_attribute()
computer_move = computer_attribute()
def rock_paper_scissors():
    if player_move == computer_move:
        win_or_lose = rock_paper_scissors_var.DRAW
    elif computer_move == rock_paper_scissors_var.ROCK and player_move == rock_paper_scissors_var.SCISSORS:
        win_or_lose = rock_paper_scissors_var.LOSE
    elif computer_move == rock_paper_scissors_var.PAPER and player_move == rock_paper_scissors_var.ROCK:
        win_or_lose = rock_paper_scissors_var.LOSE
    elif computer_move == rock_paper_scissors_var.SCISSORS and player_move == rock_paper_scissors_var.PAPER:
        win_or_lose = rock_paper_scissors_var.LOSE
    else:
        win_or_lose = rock_paper_scissors_var.WIN
    print(win_or_lose)
