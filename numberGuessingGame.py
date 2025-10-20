import random

print('user have to guess the number')
computer_number = int(random.randint(1,10))
while True:
    user_number = int(input("choose the number between (1/10)"))
    if user_number == computer_number:
        print(f'congratulation you have win. computer move was = {computer_number} ')
        break
    elif user_number < computer_number:
        print("Sorry it's to low")
        print(f'({computer_number})')
    elif user_number > computer_number:
        print("sorry it's too high")
    else:
        print("invalid")



