L = [1,2,3,4,5,6,7,8]

Even = []
Odd = []

for i in L:
    if i % 2 == 0:
        Even.append(i)
    else:
        Odd.append(i)

print("Even" , Even)
print("Odd" , Odd)