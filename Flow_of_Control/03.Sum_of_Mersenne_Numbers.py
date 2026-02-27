# Mersenne Numbers are of form 2^n-1

num = int(input("How many terms: "))
sum = 0

for i in range(1, num+1):
    print(2**i-1 , end = " ")
    sum += 2**i-1

print("\n")
print("Sum =" , sum)