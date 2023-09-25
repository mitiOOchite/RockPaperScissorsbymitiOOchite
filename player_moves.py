def player_attribute():
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
    return player_move