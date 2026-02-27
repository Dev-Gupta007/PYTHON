n = int(input("Enter the number whose factorial you want: "))

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negetive Numbers ") 
    if n == 1 or n == 0:
        return 1
    return n*factorial(n-1)

print(factorial(n))