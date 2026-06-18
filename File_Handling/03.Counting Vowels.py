f = open(r"D:\DEV\Programming\PYTHON\File_Handling\sample.txt" , "r")

file = f.read()

#-------------------------------------------------------------------------

# Counting Total Vowels

vowel_count = 0

for i in file:
    if i.lower() in "aeiou":
        vowel_count += 1

print("Total Vowels" , vowel_count)

#-------------------------------------------------------------------------

# Counting Vowels Seperately

a_Count = 0
e_Count = 0
i_Count = 0
o_Count = 0
u_Count = 0

for i in file:
    ch = i.lower()

    if ch == "a":
        a_Count += 1
    elif ch == "e":
        e_Count += 1
    elif ch == "i":
        i_Count += 1
    elif ch == "o":
        o_Count += 1
    elif ch == "u":
        u_Count += 1

print(f"""Occurrences 
        A: {a_Count}
        E: {e_Count}
        I: {i_Count}
        O: {o_Count}
        U: {u_Count}""")

#------------------------------------------------------------------

# Program to find whether vowels or consonants are more frequent in a file.

vowels = 0
consonants = 0

for i in file:
    if i.isalpha():
        if i.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print(f"Vowels: {vowels}\nConsonants: {consonants}")

if vowels>consonants:
    print("Vowels are more Frequent")
elif vowels<consonants:
    print("Consonants are more Frequent")
else:
    print("Both Vowels and Consonants are Equal")

f.close()