list_1 = eval(input("Enter list: "))
len_1 = len(list_1)

mean = sum = 0

for i in range(0 , len_1):
    sum += list_1[i]

mean = sum/len_1
print("Given List is " , list_1)
print("Mean is" , mean)