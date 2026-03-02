import random
List = []
Counter = 0

while True:
    choice = input("Roll the Dice? (y/n): ")
    choice = choice.lower()
    if choice == "y":   
        number = int(input("Enter the Number of times you want to roll The Dice: "))
        for i in range(0,number):
            List.append(random.randint(1,6))
            Copy = List
            Counter += 1
        print(tuple(Copy))
        print(f"You have Rolled the Dice {Counter} times")
        List.clear()  
    elif choice == 'n':
        print("Thanks for Playing")
        break
    else:
        print("Invalid Choice")