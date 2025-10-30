# The rock paper scissor projects; 

import random

computer_choose = random.randint(1,3)
if computer_choose == 1:
    r = 'rock'
    print(rock)
elif computer_choose == 2:
    p = 'paper'
    print(paper)
elif computer_choose == 3:
    s = 'scissor'
    print(scissor)
user_input = input("Enter the (r,p,s)")
if user_input == 'r':
    u_r = 'rock'
elif user_input == 's':
    u_s = 'scissor'
elif user_input == 'p':
    u_p = 'paper'
else:
    print("Please enter according to the statement")
while True:
    if rock == u_r:
        print("Computer has choose the rock and you also have choose the rock")
    elif rock == u_s:
        print("Computer has choose the rock and you have choose the paper")
    elif rock == u_p:
        print("computer has choose the rock and you have choose the paper")
    elif paper == u_s:
        print("Computer have choose the paper and You  choosen the scissor")
    elif paper == u_r:
        print("computer hass choosen the paper and you have choosen the rock")
    elif paper == u_p:
        print("Computer has choosen the paper and the you have choosen the paper")
    elif scissor == u_r:
        print("Computer has choose the scissor and you have choosen the rock")
    elif scissor == u_p:
        print("Computer has choosen the scissor and you have choosen the paper")
    elif scissor == u_s:
        print("Computer has chosen the scissor and you have also choosen the scissor")
    else:
        print("Why don't you choose anythuing's else")