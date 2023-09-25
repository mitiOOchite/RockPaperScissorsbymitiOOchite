rock = ''
paper = ''
scissors = ''
player_move = ''
def player_attribute():
    global rock
    rock = 'Rock'
    global paper
    paper = 'Paper'
    global scissors
    scissors = 'Scissors'
    global player_move
    player_move = input('Choose [r]ock, [p]aper, [s]cissors: ')
    if player_move.lower() == 'r':
        player_move = rock
    elif player_move.lower() == 'p':
        player_move = paper
    elif player_move.lower() == 's':
        player_move = scissors
    else:
        raise SystemExit('Invalid Input. Please choose [r], [p] or [s]. Try again...')
