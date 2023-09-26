from player_moves import player_attribute
from computer_moves import computer_attribute
import rock_paper_scissors_var as var
import game_variation_details


def rock_paper_scissors():
    var.NUMBER_OF_GAMES
    var.computer_win_count = 0
    var.player_win_count = 0
    var.win_count = 0
    i = var.NUMBER_OF_GAMES
    while i <= var.NUMBER_OF_GAMES:
        if i == 0:
            break
        if var.NUMBER_OF_GAMES == 3 and var.player_win_count == 2:
            winner = var.USER
            var.win_count = var.player_win_count
            break
        elif var.NUMBER_OF_GAMES == 3 and var.computer_win_count == 2:
            winner = "Computer"
            var.win_count = var.computer_win_count
            break
        if var.NUMBER_OF_GAMES == 5 and var.player_win_count == 3:
            winner = var.USER
            var.win_count = var.player_win_count
            break
        elif var.NUMBER_OF_GAMES == 5 and var.computer_win_count == 3:
            winner = "Computer"
            var.win_count = var.computer_win_count
            break
        if var.NUMBER_OF_GAMES == 7 and var.player_win_count == 4:
            winner = var.USER
            var.win_count = var.player_win_count
            break
        elif var.NUMBER_OF_GAMES == 7 and var.computer_win_count == 4:
            winner = "Computer"
            var.win_count = var.computer_win_count
            break
        if var.NUMBER_OF_GAMES == 9 and var.player_win_count == 5:
            winner = var.USER
            var.win_count = var.player_win_count
            break
        elif var.NUMBER_OF_GAMES == 9 and var.computer_win_count == 5:
            winner = "Computer"
            var.win_count = var.computer_win_count
            break
        player_move = player_attribute()
        computer_move = computer_attribute()
        if player_move == computer_move:
            win_or_lose = var.DRAW
            i -= 0
            print(win_or_lose)
            continue
        elif computer_move == var.ROCK and player_move == var.SCISSORS:
            win_or_lose = var.LOSE
            var.computer_win_count += 1
            i -= 1
        elif computer_move == var.PAPER and player_move == var.ROCK:
            win_or_lose = var.LOSE
            var.computer_win_count += 1
            i -= 1
        elif computer_move == var.SCISSORS and player_move == var.PAPER:
            win_or_lose = var.LOSE
            var.computer_win_count += 1
            i -= 1
        else:
            win_or_lose = var.WIN
            var.player_win_count += 1
            i -= 1
        print(win_or_lose)
    print(f'The winner is {winner} with {var.win_count} wins!')
