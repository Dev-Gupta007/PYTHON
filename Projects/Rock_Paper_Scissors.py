import random

ROCK = 'R'
SCISSORS = 'S'
PAPER = 'P'

Choice = 'y'

emojis = { ROCK:'🪨',SCISSORS:'✂️',PAPER :'📃' }
choices = tuple(emojis.keys())

def get_User_choice():
    while True:
        User_Choice = input("Rock,Paper or Scissors(R,P,S) ").upper()
        if User_Choice in choices:
            return User_Choice
        else:
            print('Invalid Choice')

def Display_Choices(User_Choice , Computer_Choice):
    print(f'You Chose {emojis[User_Choice]}')
    print(f'You Computer Chose {emojis[Computer_Choice]}')

def Determine_The_Winner(User_Choice , Computer_Choice):
    if (
        (User_Choice == ROCK and Computer_Choice == PAPER ) or
        (User_Choice == PAPER  and Computer_Choice == SCISSORS) or
        (User_Choice == SCISSORS and Computer_Choice == ROCK)):
        print(f"You Lost!")
    elif(
        (User_Choice == ROCK and Computer_Choice == SCISSORS) or
        (User_Choice == PAPER and Computer_Choice == ROCK) or
        (User_Choice == SCISSORS and Computer_Choice == PAPER )):      
        print(f"User Won!")
    elif User_Choice == Computer_Choice :
        print(f"Draw!")

def play_game():
    while True:

        User_Choice = get_User_choice()

        Computer_Choice = random.choice(choices)

        Display_Choices(User_Choice , Computer_Choice)

        Determine_The_Winner(User_Choice , Computer_Choice)

        Choice = input('Do you want to continue(y/n) : ')
        if Choice == 'n':
            break
   
play_game()