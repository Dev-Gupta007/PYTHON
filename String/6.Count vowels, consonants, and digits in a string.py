
s = input("Enter the string: ")
Count_Vowels = 0
Count_Consonants = 0
Count_digits = 0
Count_Symbols = 0

for i in s:
    if i.isdigit():
        Count_digits += 1
    elif i.isalpha():
        if i in ['a' ,'e' ,'i' ,'o' ,'u']:
            Count_Vowels +=1
        else :
            Count_Consonants +=1
    elif i.isdigit():
        Count_digits +=1
    elif i.isalpha() != True and i != ' ':
        Count_Symbols +=1
    else:
        continue

print(f"Number of Vowels {Count_Vowels}")
print(f"Number of Consonants {Count_Consonants}")
print(f"Number of digits {Count_digits}")
print(f"Number of Symbols {Count_Symbols}")