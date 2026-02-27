list_1 = eval(input("Enter The list: "))

# Using set()

set_1 = set(list_1)

list_2 = list(set_1)

print(list_2)

# Without Using Set

result = []

for i in list_1:
    if i not in result:
        result.append(i)
    else:
        continue
print(result)