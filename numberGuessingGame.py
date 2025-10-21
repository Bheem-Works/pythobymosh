import random

print('user have to guess the number')
number_to_guess = random.randint(1,10)
while True:
    try:
      user_number = int(input("choose the number between (1/10): ")) 
    except ValueError:
        print("Mr enter the valid number")
        break
    if user_number == number_to_guess:
        print(f'congratulation you have win. computer move was = {number_to_guess} ')
        break
    elif user_number < number_to_guess:
        print("Sorry it's to low")
        print(f'({number_to_guess})')
    elif user_number > number_to_guess:
        print("sorry it's too high")

    



