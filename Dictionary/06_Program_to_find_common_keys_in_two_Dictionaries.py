D1 = eval(input("Enter First Dictionary: "))
D2 = eval(input("Enter Second Dictionary: "))

Keys_1 = D1.keys()
Keys_2 = D2.keys()
Common_Keys = []

for i in Keys_1:
    if i in Keys_2:
        Common_Keys.append(i)

print(Common_Keys)