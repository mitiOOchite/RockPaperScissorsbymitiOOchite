import rock_paper_scissors_var as var
def player_attribute():
    player_move = input('Choose [r]ock ⛰️, [p]aper 📄 or [s]cissors ✂: ')
    if player_move.lower() == 'r':
        player_move = var.ROCK
    elif player_move.lower() == 'p':
        player_move = var.PAPER
    elif player_move.lower() == 's':
        player_move = var.SCISSORS
    else:
        raise SystemExit('Invalid Input. Please choose [r] , [p] or [s]. Try again...')
    return player_move
