# The rock paper scissor projects; 

import random

# whie loop
computer_choose = random.randint(1,3)
if computer_choose == 1:
    rock = 'rock'
    print(rock)
elif computer_choose == 2:
    paper = 'paper'
    print(paper)
elif computer_choose == 3:
    scissor = 'scissor'
    print(scissor)

user_input = input("Enter the r\p\s:")
while True:
    if user_input == 'r' and user_input == computer_choose:
        print(f"Win !  you have choose the {user_input} and the computer has choose the {user_input}")
