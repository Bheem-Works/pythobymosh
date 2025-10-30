import  random 

while True:
    computer_choice = random.choice(['rock','paper','scissor'])
    user_input = input("Enter (r,p,s): ").lower()
    if user_input == 'r':
        user_choose = 'rock'
    elif user_input == 'p':
        user_choose == 'paper'
    elif user_input == 's':
        user_choose == 'scissor'
    else:
        print("Please enter the valid choice (r,s,p)")
        continue
    print(f"Computer choose {computer_choice} ") 
    print(f"You choice{user_choose}")

    if computer_choice == user_choose:
        print("It's tie ")
    elif (
        (computer_choice == 'rock' and user_choose == 'scissor') or
        (computer_choice == 'paper' and user_choose == 'rock') or
        (computer_choice == 'scissor' and user_choose == 'paper')
    ):
      print("Computer win")
    else:
        print("You win ")
    user_wantTo = input("Want to continue ? (y/n):").lower()
    if user_wantTo!= 'y':
       print("Thanks for playing")
       break