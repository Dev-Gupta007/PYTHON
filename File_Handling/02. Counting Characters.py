f = open("D:\\DEV\\Programming\\PYTHON\\File_Handling\\sample.txt" , "r")

file = f.read()

# Program to count the total number of characters in a text file.

char_count = 0
char_without_spaces = 0

for i in file:
    if not i.isspace():             # isspace ignore tabs , newlines & spaces
        char_without_spaces += 1
    char_count += 1 

print("Total characters with spaces: " , char_count)

print("Total characters without spaces: " , char_without_spaces)

# Program to count the number of alphabetic characters, digits, and special character. 

alphabets_count = 0
digits_count = 0
special_char_count = 0

for i in file:
    if i.isalpha():
        alphabets_count += 1
    elif i.isdigit():
        digits_count += 1
    elif not i.isspace():
        special_char_count += 1
    else:
        continue

print("Total Number of alphabets: " , alphabets_count)
print("Total Number of digits: " , digits_count)
print("Total Number of special characters: " , special_char_count)

f.close()