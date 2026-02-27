list_1 = eval(input("Enter a list: "))
len_1 = len(list_1)

#Sorting

for j in range(0,len_1):
    for i in range(0 , len_1-1):
        if list_1[i]<list_1[i+1]:
            list_1[i] , list_1[i+1] = list_1[i+1] , list_1[i]
        else :
            continue
    
print(list_1)
