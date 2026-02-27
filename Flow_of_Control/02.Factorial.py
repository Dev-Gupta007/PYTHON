num = int(input("Enter Number: "))
factorial = 1

if num > 1:
    for i in range(1 , num+1):
        factorial *= i
    print("Factorial is " , factorial)
elif num == 0 :
    print("Factorial is " , 1)
else :
    print("Factorial Not Defined")