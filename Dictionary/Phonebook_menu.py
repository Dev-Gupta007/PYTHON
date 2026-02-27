n = int(input("Enter the number of Friends: "))
D = {}

for i in range(n):
    print(f"Enter Details of Friend {i+1}")
    Name = input("Enter Name: ")
    Number  = int(input("Enter Number : "))
    D[Name] = Number

print("-"*50)

def pretty_printing(D):
    for key, value in D.items():
        print(f"{key}\t{value}")

ch = 0

while ch != 7:
    print("""\tMenu
          1. Display all friends
          2. Add a Friend
          3. Delete a Friend
          4. Modify a Phone Number
          5. Search for a friend
          6. Sort on names
          7. Exit
    """)

    ch = int(input("Enter your choice(1,2...7): "))

    if ch == 1:
        pretty_printing(D)

    elif ch == 2:
        print("Enter Details of a new friend: ")
        Name = input("Name: ")
        Number = int(input("Enter Number: "))
        D[Name] = Number

    elif ch == 3:
        Name = input("Name: ")
        D_no = D.pop(Name, -1)
        if D_no != -1:
            print("Deleted:", Name)
        else:
            print("No such friend")

    elif ch == 4:
        Name = input("Name: ")
        if Name in D:
            Number = int(input("Changed Number: "))
            D[Name] = Number
        else:
            print("Friend not found")

    elif ch == 5:
        name = input("Friend Name: ")
        if name in D:
            print(name, "exists in dictionary")
        else:
            print(name, "does not exist in dictionary")

    elif ch == 6:
        for key in sorted(D):
            print(f"{key}\t{D[key]}")

    elif ch == 7:
        print("Exiting program...")

    else:
        print("Valid Choices Are (1,2,3,4,5,6,7)")