f = open("D:\\DEV\\Programming\\PYTHON\\File_Handling\\sample.txt" , "r")

lines = f.readlines()

# Display lines starting with a vowel

for i in lines:
    if i[0].lower() in "aeiou":
        print(i)
print("-"*150)
# Display lines starting with a consonant

for i in lines:
    if i[0].isalpha() and i[0].lower() not in "aeiou":
        print(i)
print("-"*50)
# Display lines ending with '.'

for i in lines:
    line = i.strip()
    if line and line[-1] == ".":
        print(i)
print("-"*150)
# Display the longest line

l = ""
for i in lines:
    if len(i) > len(l):
        l = i

print(l)
print("-"*150)
# Display the shortest line

l = lines[0]

for i in lines:
    if len(i.strip()) != 0 and len(i.strip()) < len(l.strip()):
        l = i

print(l.strip())

print("-"*150)

# Count empty lines
count = 0

for i in lines:
    if i == "\n":
        count += 1

print(count)

print("-"*150)

# Print alternate lines

for i in range(0 , len(lines) , 2):
    print(lines[i])

print("-"*150)

# Print even-numbered lines

for i in range(0 , len(lines) , 2):
    print(lines[i])

print("-"*150)

# Print odd-numbered lines

for i in range(1 , len(lines) , 2):
    print(lines[i])

print("-"*150)