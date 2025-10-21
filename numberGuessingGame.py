import random

print('user have to guess the number')
computer_number = random.randint(1,10)
while True:
    try:
      user_number = int(input("choose the number between (1/10): "))
      # the (try) will try this and when the string can not be converted to the number it throw the valueError 
      # and then we get the valueError and we except that and if it has then through the ouput  
    except ValueError:
        print("Mr enter the valid number")
        break
    if user_number == computer_number:
        print(f'congratulation you have win. computer move was = {computer_number} ')
        break
    elif user_number < computer_number:
        print("Sorry it's to low")
        print(f'({computer_number})')
    elif user_number > computer_number:
        print("sorry it's too high")
 
    



