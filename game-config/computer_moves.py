import random
import rock_paper_scissors_var
def computer_attribute():
    computer_random_number = random.randint(1, 3)
    computer_move = ''
    if computer_random_number == 1:
        computer_move = rock_paper_scissors_var.ROCK
    elif computer_random_number == 2:
        computer_move = rock_paper_scissors_var.PAPER
    elif computer_random_number == 3:
        computer_move = rock_paper_scissors_var.SCISSORS
    print(f'The computer chose: {computer_move}')
    return computer_move
