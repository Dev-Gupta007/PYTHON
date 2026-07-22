string = input("Enter a String: ")

D = {'a': 0,
     'e': 0,
     'i': 0,
     'o': 0,
     'u': 0,}

for ch in string:
    if ch in D:
        D[ch] += 1

print(D)