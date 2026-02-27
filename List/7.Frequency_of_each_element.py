list_1 = eval(input("Enter the list: "))
len_1 = len(list_1)
list_2 = []
list_3 = []

for i in list_1:
    if i not in list_2:
        list_2.append(i)
        count = list_1.count(i)
        print(f"Number of occurences of {i} are {count}")
    else:
        list_3.append(i)
        continue

print(f"Unique elements list {list_2}")
print(f"Repeated elements list {list_3}")