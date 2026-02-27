import random

Number = random.randint(1,100)

while True:
    try:
        Guessed_Number = int(input("Guess a Number between 1 to 100: "))  

        if Guessed_Number > Number:
            print('Too High!')
        elif Guessed_Number < Number:
            print('Too Low!')
        else:
            print('Congratulations! You Guessed The Number')
            break
    except ValueError:
        print("Enter a Valid Number")
