string = input("Enter a string: ")
length = len(string)
str_2 = ""
a = 0
while a < length:
    if a == 0:
        str_2 += string[a].upper()
        a += 1
    elif string[a] == " " and string[a+1] != " ":
        str_2 = str_2 + string[a] + string[a+1].upper()
        a += 2
    else:
        str_2 += string[a]
        a += 1
print(str_2)