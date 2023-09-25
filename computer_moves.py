import random
def computer_attribute():
    computer_rock = 'Rock'
    computer_paper = 'Paper'
    computer_scissors = 'Scissors'
    computer_random_number = random.randint(1, 3)
    computer_move = ''
    if computer_random_number == 1:
        computer_move = computer_rock
    elif computer_random_number == 2:
        computer_move = computer_paper
    elif computer_random_number == 3:
        computer_move = computer_scissors
    print(f'The computer chose: {computer_move}')
    return computer_move