import random 

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

emojis = {ROCK:'🪨',PAPER:'📃',SCISSORS:'✂️'}
choices = tupel(emojis.keys())

def get_user_choice():
  while True:
    user_choice = input("Rock,paper,scissors ? (r,s,p)").lower()
    if user_choice in choices:
      return user_choice
    else:
        print('invalid choice!')
    
def display_choice(user_choice,computer_choice):
   print(f'you have choose the {emojis[user_choice]}')
   print(f'computer chose {emojis[computer_choice]}')
  
def determin_winner(user_choice,computer_choice):
  if user_choice == computer_choice:
    print('tie')
  elif(
    (user_choice == ROCK and computer_choice == SCISSORS) or 
    (user_choice == SCISSORS and computer_choice == PAPER) or 
    (user_choice == PAPER and computer_choice == rock)):
    print('you win')
  else:
    print('you lose')


def play_game():
  while True:
    user_choice = get_user_choice()
    computer_choice = random.choice(choices)
    display_choice(user_choice,computer_choice)
    determin_winner(user_choice,computer_choice)

    should_continue = input('continue ? (y/n)').lower()
    if should_continue == 'n':
      break

  play_game()
