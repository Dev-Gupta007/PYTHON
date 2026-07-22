f = open("sample.txt")

file = f.read()
words = file.split()

for i in words:
    if i.count('e') >= 2:
        print(i)

f.close()