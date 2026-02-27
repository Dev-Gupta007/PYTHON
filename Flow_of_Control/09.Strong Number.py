def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negetive Numbers ") 
    if n == 1 or n == 0:
        return 1
    return n*factorial(n-1)

num = int(input("Enter a number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += factorial(digit)
    temp //= 10

if sum == num:
    print("Strong Number")
else:
    print("Not a Strong Number")