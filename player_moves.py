import rock_paper_scissors_var
def player_attribute():
    player_move = input('Choose [r]ock, [p]aper, [s]cissors: ')
    if player_move.lower() == 'r':
        player_move = rock_paper_scissors_var.ROCK
    elif player_move.lower() == 'p':
        player_move = rock_paper_scissors_var.PAPER
    elif player_move.lower() == 's':
        player_move = rock_paper_scissors_var.SCISSORS
    else:
        raise SystemExit('Invalid Input. Please choose [r], [p] or [s]. Try again...')
    return player_move
