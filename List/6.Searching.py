list_1 = eval(input("Enter the List: "))

len_1 = len(list_1)

element = eval(input("Enter the element to be searched for: "))

for i in range(0 , len_1):
    if element == list_1[i]:
        print(f'element , found at index {i}')
        break
else:
    print(f"{element} , not found in the given list")