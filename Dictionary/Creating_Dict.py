# Creating Dict with Roll no. as key and marks as values

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

# Program to modify Marks while taking input as Roll Number

print("To Modify Marks: ")

r = eval(input("Enter roll no. "))

if r in M:
    M[r] = int(input("Enter new Marks: "))
else:
    print("No such roll Number")

print(f"Modified Dictionary: ")