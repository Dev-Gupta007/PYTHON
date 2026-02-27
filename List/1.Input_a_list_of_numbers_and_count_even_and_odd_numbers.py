list_1 = eval(input("Enter the list: "))
count_even = 0
count_odd = 0

for i in list_1:
    if i % 2 == 0:
        count_even += 1
    elif i % 2 != 0 :
        count_odd += 1
        continue

print("Number of even integers are :" , count_even)
print("Number of odd integers are :" , count_odd)