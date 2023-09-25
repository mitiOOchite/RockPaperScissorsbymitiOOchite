import random
computer_rock = ''
computer_paper = ''
computer_scissors = ''
computer_move = ''
def computer_attribute():
    global computer_rock
    computer_rock = 'Rock'
    global computer_paper
    computer_paper = 'Paper'
    global computer_scissors
    computer_scissors = 'Scissors'
    computer_random_number = random.randint(1, 3)
    global computer_move
    computer_move = ''
    if computer_random_number == 1:
        computer_move = computer_rock
    elif computer_random_number == 2:
        computer_move = computer_paper
    elif computer_random_number == 3:
        computer_move = computer_scissors
    print(f'The computer chose: {computer_move}')
computer_attribute()