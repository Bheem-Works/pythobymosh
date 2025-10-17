import random 

def rock_paper_scissor():
    print("enter the rock,paper and scissor")
    user_move = input().strip().lower()
    computer_move = random.choice(['rock','paper','scissor'])
    print(f"computer choose the 🩻{computer_move}")
    if user_move not in ['rock','paper','scissor']:
        print("this is not valid")
        return
    if computer_move == user_move:
        print("it is a tie")
    elif (user_move == 'rock' and computer_move == 'scissor') or \
        (user_move == 'scissor' and computer_move == 'paper' ) or \
            (user_move == 'paper' and computer_move == 'rock'):
            print("You win! 😉💜")
    else:
        print("You loose! 😭 and computer win")

rock_paper_scissor()

        

        

    
