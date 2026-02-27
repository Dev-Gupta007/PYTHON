# 1-x+x²-x³+....xⁿ

x = int(input("Enter the value of x : "))
n = int(input("Enter the power(n): "))
sign = 1
sum = 0

for i in range(0 , n+1):
    sum += sign*(x**i)
    sign *= -1
    

print(f"The sum of first {n} terms is {sum}")

# x + x²/2! - x³/3! + x⁴/4! - x⁵/5! + x⁶/6! - x⁷/7! + …xⁿ/n!

x = int(input("Enter the value of x: "))
n = int(input("Enter the power(n): "))
sum = x
sign = +1

for i in range(2,n+1):
    factorial = 1
    for j in range(1 , i+1):
        factorial *= j
    term = ((x**i)*sign)/factorial
    sum+=term
    sign *= -1   
print(f"Sum of first" , n , "terms:" , sum)
 
# S = 1 + (1+2) + (1+2+3) ..........

Sum = 0
n = int(input("How many Terms? "))

for i in range(1 , n+1):
    for j in range(1 , i+1):
        Sum += j
print(Sum)    

# Fibonacci Series
# 0 , 1 ,1 , 2 , 3 , 5 , 8 ...........

n = int(input("Enter how many terms: "))

Term_1 = 0
Term_2 = 1

if n == 1:
    print(Term_1)
elif n == 2:
    print(Term_1 , Term_2 , sep = "\n")
else:
    print(Term_1 , Term_2 , sep = "\n")
    for i in range(2 , n):
        Term = Term_1 + Term_2
        print(Term)
        Term_1 = Term_2
        Term_2 = Term
