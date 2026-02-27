M = {}
n = int(input("How many students? "))
for i in range(n):
    r,m = eval(input("Enter the Roll No. , Marks "))
    M[r] = m
    
print("Created Dictionary")
Choice = 'y'
  
while Choice == 'y':
    r,m = eval(input("Enter details of new students "))   
    M[r] = m
    Choice = input("More Students? ")
    continue 
print(M)