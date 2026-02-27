num = int(input("Enter the Number : "))
Sum = 0
Sum_even = 0
Sum_odd = 0

# Sum of all Natural Numbers 

for i in range(0 , num ):
    Sum += i

print("Sum of all Numbers is : " , Sum)

# Sum of Even Natural Numbers
for i in range(0 , num , 2 ):
    Sum_even += i

print("Sum of all Even Numbers is: " , Sum_even)

# Sum of Odd Natural Numbers

for i in range(1 , num , 2 ):
    Sum_odd += i

print("Sum of all Even Numbers is: " , Sum_odd)