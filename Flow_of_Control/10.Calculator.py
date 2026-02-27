print('''Welcome To Calculator
      1. Add
      2. Subtract
      3. Multiply
      4. Divide
      5. Percentage
''')

Choice  = 'y'

while Choice == 'y':
    n = int(input("Enter your choice : "))
    x = float(input("Enter First Number: "))
    y = float(input("Enter Second Number: "))
    if n == 1:
        print(f"Sum of {x} and {y} is {x+y}")
    elif n == 2:
        print(f"Difference of {x} and {y} is {x-y}")
    elif n == 3:
        print(f"Product of {x} and {y} is {x*y}")
    elif n == 4:
        print(f"Remainder of {x} divided by {y} is {x/y}")
    elif n == 5:
        print(f"{x} is {(x/y)*100} % of {y}")
    else :
        print("Enter valid Number")