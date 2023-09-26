import random
import rock_paper_scissors_var as var
def computer_attribute():
    computer_random_number = random.randint(1, 3)
    computer_move = ''
    if computer_random_number == 1:
        computer_move = var.ROCK
        icon = '⛰️'
    elif computer_random_number == 2:
        computer_move = var.PAPER
        icon = '📄'
    elif computer_random_number == 3:
        computer_move = var.SCISSORS
        icon = '✂'
    print(f'The computer chose: {computer_move} {icon}')
    return computer_move
