f = open("sample.txt" , "r")

file = f.read()

n_f = open("new_file.txt" , "w")

for ch in file:
    if ch.islower():
        ch = ch.upper()
    elif ch.isupper():                # There is also .swapcase() if you want to use it
        ch = ch.lower()
    n_f.write(ch)

f.close()
n_f.close() 