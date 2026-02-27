list_1 = eval(input("Enter a list: "))

largest = second = float('-inf')

for num in list_1:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

if second == float('-inf'):
    print("No second largest element.")
else:
    print("Second Largest Number is:", second)