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
    