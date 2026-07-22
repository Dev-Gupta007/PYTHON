f = open("D:\\DEV\\Programming\\PYTHON\\File_Handling\\sample.txt" , "r")

file = f.read()
words = file.split()

# Display words beginning with a vowel

for i in words:
    if i[0] in "AEIOUaeiou":
        print(i)

# Display words beginning with a consonant

for i in words:
    if i[0].isalpha() and i[0] not in "AEIOUaeiou":
        print(i)

# Display words ending with a vowel

for i in words:
    if i[-1] in "AEIOUaeiou":
        print(i)

# Display words ending with a consonant

for i in words:
    if i[-1].isalpha() and i[-1] not in "AEIOUaeiou":
        print(i)

# Display words having exactly 2 vowels

for i in words:
    count = 0
    for j in i:
        if j.lower() in "aeiou":
            count += 1
    if count == 2:
        print(i)

# Display words containing at least two lowercase 'e'

for i in words:
    if i.count('e') >=2 :
        print(i)

# Display words having more than 5 letters

for i in words:
    if len(i) > 5:
        print(i)

# Display palindromic words

for i in words:
    if i == i[::-1]:
        print(i)

# Display words containing digits

for i in words:
    for j in i:
        if j.isdigit():
            print(i)
            break